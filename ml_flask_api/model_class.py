from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

class ml_model():
    def __init__(self):
        self.model_base = {"linear": LogisticRegression,
                           "randomforest": RandomForestClassifier,
                           "boosting": GradientBoostingClassifier
                           }

        self.pretrained_model = {}

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
            model = self.pretrained_model[model_name]
            return model.predict(x_test).tolist()
        except Exception as ex:
            return 'input incorrect model_name'


    def save_model(self, model, model_name):
        self.pretrained_model[model_name] = model

    def del_model(self, model_name):
        try:
            del self.pretrained_model[model_name]
            return model_name+' model has deleted'
        except Exception as ex:
            return 'input incorrect model_name'

