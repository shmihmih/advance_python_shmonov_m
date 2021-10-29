#генерируем датасет
def gen_dataset(n_samples = 100, n_features=20, n_classes = 4, n_informative = 4):
    x, y = make_classification(n_samples = n_samples, n_features = n_features, n_classes = n_classes, n_informative = n_informative)
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    return X_train, X_test, y_train, y_test

#создаём списки признаков для модели    
def create_params_for_api(X_train, X_test, y_train, y_test, model_type = 'linear', model_params = {'penalty':'l2', 'max_iter':10}):
    p_train = {}
    p_train['model_name'] = model_type
    p_train['x_train'] = X_train.tolist()
    p_train['y_train'] = y_train.tolist()
    p_train['x_test'] = X_test.tolist()
    p_train['y_test'] = y_test.tolist()
    p_train['params'] = model_params

    p_test = {}
    p_test['model_name'] = model_type
    p_test['x_test'] = X_test.tolist()

    p_del = {}
    p_del['model_name'] = model_type
    return p_train, p_test, p_del

def test_api(p_train, p_test, p_del):
    #получить список моделей доступных для обучения 
    r = requests.get('http://neokind.pro/get_model_list')
    print(r.json())
    #получить список предобученных моделей доступных для обучения 
    r = requests.get('http://neokind.pro/get_pretrained_model_list')
    print(r.json())

    #получить предсказания модели
    r = requests.get('http://neokind.pro/predict_model/', json = p_test)
    print(r.json())
    #обучить модель и получить её score 
    r = requests.get('http://neokind.pro/train_model', json = p_train)
    print(r.json())
    #обучить модель и получить её score 
    r = requests.get('http://neokind.pro/train_model/', json = p_train)
    print(r.json())
    #получить предсказания модели
    r = requests.get('http://neokind.pro/predict_model/', json = p_test)
    print(r.json())
    #обучить модель и получить её score 
    r = requests.get('http://neokind.pro/train_model/', json = p_train)
    print(r.json())
    #удалить модель
    r = requests.get('http://neokind.pro/del_model/', json = p_del)
    print(r.json())
    #повторное удаление модели должно выдать что удалить модель нельзя 
    r = requests.get('http://neokind.pro/del_model/', json = p_del)
    print(r.json())