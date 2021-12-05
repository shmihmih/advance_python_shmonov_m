from flask import Flask, request, jsonify
from celery import Celery
import os

CELERY_BROKER = os.environ['CELERY_BROKER']
CELERY_BACKEND = os.environ['CELERY_BACKEND']

celery = Celery('tasks', broker=CELERY_BROKER, backend=CELERY_BACKEND)
app = Flask(__name__)

@app.route('/get_model_list/', methods=['GET', 'POST'])
def show_models():
    task = celery.send_task('model_list')
    return jsonify({'task_id': str(task.id)}), 200


@app.route('/get_pretrained_model_list/', methods=['GET', 'POST'])
def show_pretrained_models():
    task = celery.send_task('pretrained_model_list')
    return jsonify({'task_id': str(task.id)}), 200


@app.route('/train_model/', methods=['GET', 'POST'])
def train_model():
    content = request.json
    try:
        model_name = content['model_name']
        x_train = content['x_train']
        y_train = content['y_train']
        x_test = content['x_test']
        y_test = content['y_test']
    except Exception as ex:
        return jsonify('key_error ' + str(ex)), 403
    params = content.get('params', 0)
    task = celery.send_task('train_model', args=[model_name, x_train, y_train, x_test, y_test, params])
    return jsonify({'task_id': str(task.id)}), 200


@app.route('/predict_model/', methods=['GET', 'POST'])
def predict_model():
    content = request.json
    try:
        model_name = content['model_name']
        x_test = content['x_test']
    except Exception as ex:
        return jsonify(ex)
    task = celery.send_task('predict_model', args=[model_name, x_test])
    # return str(task)
    return jsonify({'task_id': str(task.id)}), 200


@app.route('/del_model/', methods=['GET', 'POST'])
def del_model():
    content = request.json
    try:
        model_name = content['model_name']
    except Exception as ex:
        return jsonify(ex)
    task = celery.send_task('del_model', args=[model_name])
    return jsonify({'task_id': str(task.id)}), 200


@app.route('/get_results/', methods=['GET', 'POST'])
def get_results():
    task_id = request.json['task_id']
    res = celery.AsyncResult(task_id)
    if res.state == 'PENDING':
        return res.state, 200
    else:
        return jsonify({'task_result': res.results}), 200


# обычный запуск
if __name__ == "__main__":
    app.run(host='0.0.0.0')

HOST = os.environ['HOST']
PORT = os.environ['PORT']
DEBUG = os.environ['DEBUG']
# запуск в случае если обычный не работает
# if __name__ == '__main__':
#    from werkzeug.serving import run_simple
#    run_simple('localhost', 500, application)
