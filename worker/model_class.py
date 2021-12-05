from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
import pymongo
import pickle
import os

MONGO_DB = os.environ['MONGO_DB']

class ML_model():
    def __init__(self):
        with pymongo.MongoClient(MONGO_DB) as client:
            mongo_table = client["ml_data"]["pretrained_models"]

        self.model_base = {
            "linear": LogisticRegression,
            "randomforest": RandomForestClassifier,
            "boosting": GradientBoostingClassifier
        }

    def train_model(self, model_name, x_train, y_train, x_test, y_test, params):
        try:
            if params != 0:
                model = self.model_base[model_name](**params)
            else:
                model = self.model_base[model_name]()
        except Exception as ex:
            return ex
        model.fit(x_train, y_train)
        self.save_model(model, model_name)
        return str(model.score(x_test, y_test))

    def predict_model(self, model_name, x_test):
        try:
            with pymongo.MongoClient(MONGO_DB) as client:
                mongo_table = client["ml_data"]["pretrained_models"]
                pickle_model = mongo_table.find_one(filter={"name": model_name})['model']

            model = pickle.loads(pickle_model)

            return model.predict(x_test).tolist()
        except Exception as ex:
            return 'input incorrect model_name'

    def save_model(self, model, model_name):
        patient = {'name': model_name, 'model': pickle.dumps(model)}
        with pymongo.MongoClient(MONGO_DB) as client:
            mongo_table = client["ml_data"]["pretrained_models"]

            cur_model = list(mongo_table.find(filter={"name": model_name}))

            if len(cur_model) == 0:
                mongo_table.insert_one(patient)
            else:
                mongo_table.update_one({"name": model_name}, {"$set": patient})

    def del_model(self, model_name):
        try:
            with pymongo.MongoClient(MONGO_DB) as client:
                mongo_table = client["ml_data"]["pretrained_models"]
                deleted_status = mongo_table.delete_one({"name": model_name})
                assert deleted_status.deleted_count == 1
            return model_name + ' model has deleted'
        except Exception as ex:
            return 'input incorrect model_name'
