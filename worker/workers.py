from celery import Celery
from model_class import ML_model
import os

CELERY_BROKER = os.environ['CELERY_BROKER']
CELERY_BACKEND = os.environ['CELERY_BACKEND']

celery = Celery('tasks', broker=CELERY_BROKER, backend=CELERY_BACKEND)
ml = ML_model()

@celery.task(name='train_model')
def train_model(model_name, x_train, y_train, x_test, y_test, params):
    score = ml.train_model(model_name, x_train, y_train, x_test, y_test, params)
    return score

@celery.task(name='predict_model')
def predict_model(model_name, x_test):
    pred = ml.predict_model(model_name, x_test)
    return pred

@celery.task(name='del_model')
def del_model(model_name):
    res = ml.del_model(model_name)
    return res

@celery.task(name='model_list')
def model_list():
    model_list = list(ml.model_base.keys())
    return model_list

@celery.task(name='pretrained_model_list')
def pretrained_model_list():
    model_list = list(ml.pretrained_model.keys())
    return model_list


