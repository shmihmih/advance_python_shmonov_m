# advance_python_shmonov_m
flask api for fit ml model

Дополнительно было реализовано
Валидация обученной модели
Возвращение списка уже обученных моделей
Поднятие сервера с функционалом апи на домене neokind.pro
Описание api
api состоит из 5 методов каждый из которых опишем ниже, каждый из методов возвращают словарь

получение списка доступных моделей
name: get_model_list
input: empty
output: словарь с моделями
example: {'model_list': ['linear', 'randomforest', 'boosting']}

получение списка обученных моделей
name: get_pretrained_model_list
input: empty
output: словарь с обученными моделями
example: {'pretrained_model_list': []}

обучение модели
name: train_model
input: X_train(type list(list)) - признаки для обучения
y_train(type list) - таргет для обучения
x_test(type list(list)) - признаки для теста
y_test(type list) - таргет для теста
model_name(type string) - имя модели
params(type dict) - дополнительные параметры для обучения модели
output: качество обученной модели
example: {'train_model_score': '0.76'}

предсказание модели
name: predict_model
input: x_test(type list(list)) - признаки для теста
model_name(type string) - имя модели
output: предсказания модели на тесте
example: {'prediction': [0, 0, 1, 2, 0, 0, 2, 1, 3, 0, 0, 1, 0, 2, 1, 1, 3, 0, 0, 0, 0, 3, 3, 0, 1]}

удаление модели
name: del_model
input: model_name(type string) - имя модели
output: удаление модели
example: {'del model': 'linear model has deleted'}
