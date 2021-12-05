# advance_python_shmonov_m
flask api for fit ml model with docker 
<pre>
docker-compose состоит из 4 образов
1. flask-api
2. celery-worker
3. redis
4. mongo

Образы опубликованы по ссылке 
1. https://hub.docker.com/r/shmihmih/flask_api
2. https://hub.docker.com/r/shmihmih/celery_worker

В проекте реализовано:
1. работа с БД 
2. Приложение поддерживает вычисления не в рамках Flask-приложения
3. Получившееся приложение собрано в Docker-образы и они опубликованы в DockerHub
4. Приложение можно запустить утилитой docker-compose

Для запуска приложения необходимо сделать:
1. docker-compose build
2. docker-compose up
</pre>


