from flask import Flask, request, jsonify
from model_class import ml_model

application = Flask(__name__)
ml = ml_model()

@application.route('/get_model_list/', methods=['GET', 'POST'])
def show_models():
    return jsonify({'model_list':list(ml.model_base.keys())})

@application.route('/get_pretrained_model_list/', methods=['GET', 'POST'])
def show_pretrained_models():
    return jsonify({'pretrained_model_list':list(ml.pretrained_model.keys())})

@application.route('/train_model/', methods=['GET', 'POST'])
def train_model():
    content = request.json
    try:
        model_name = content['model_name']
        x_train = content['x_train']
        y_train = content['y_train']
        x_test = content['x_test']
        y_test = content['y_test']
    except Exception as ex:
        return jsonify('key_error '+str(ex))
    params = content.get('params', 0)
    return jsonify({'train_model_score':ml.train_model(model_name, x_train, y_train, x_test, y_test, params)})


@application.route('/predict_model/', methods=['GET', 'POST'])
def predict_model():
    content = request.json
    try:
        model_name = content['model_name']
        x_test = content['x_test']
    except Exception as ex:
        return jsonify(ex)
    return jsonify({'prediction':ml.predict_model(model_name, x_test)})

@application.route('/del_model/', methods=['GET', 'POST'])
def del_model():
    content = request.json
    try:
        model_name = content['model_name']
    except Exception as ex:
        return jsonify(ex)
    return jsonify({'del model':ml.del_model(model_name)})

#обычный запуск
if __name__ == "__main__":
   application.run(host='0.0.0.0')

#запуск в случае если обычный не работает
#if __name__ == '__main__':
#    from werkzeug.serving import run_simple
#    run_simple('localhost', 500, application)



