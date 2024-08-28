# Тестовое задание на позицию Junior Developer. Якушев Олег
## Предварительная настройка и установка

1. Клонировать проект из репозитория на GitHub: ```git clone ```
>[!NOTE]
> Все команды и действия во время настройки выполняются в рабочей директории с клонированным репозиторием
### Запуск <u>без Docker</u>:
1. Сконфигурировать виртуальное окружение python: <br>
```
python -m venv venv
venv\Scripts\activate.bat
```
> [!IMPORTANT]
>Для корректной работы программы <important>необходимо</important> использовать Python <b>версии 3.10-3.11</b>
2. Обновить пакетный менеджер pip (если это необходимо) и установить зависимости
```
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```
3. Установить и запустить MongoDB ([см. документацию](https://www.mongodb.com/docs/))
> [!NOTE]
> В качестве демонстрации используется подключение к БД без логина и пароля, со стандартным портом и адресом: ```mongodb://localhost:27017/```
4. Сконфигурировать файл .env, для этого создать его и вставить следующие переменные окружения:
```dotenv
MONGODB_HOST=localhost
MONGODB_PORT=27017
MONGO_INITDB_DATABASE=GeogramintDB
MONGODB_RESULTS_COLLECTION=ScanningResults
MONGODB_USERS_COLLECTION=Users
MONGODB_GROUPS_COLLECTION=Groups
```
### Запуск с <u>Docker</u>:
1. Установить и запустить Docker и DockerCompose ([см. документацию](https://docs.docker.com))
2. Сконфигурировать файл .env.docker, для этого создать его и вставить следующие переменные окружения:
```dotenv
MONGODB_HOST=mongodb
MONGODB_PORT=27017
MONGO_INITDB_DATABASE=GeogramintDB
MONGODB_RESULTS_COLLECTION=ScanningResults
MONGODB_USERS_COLLECTION=Users
MONGODB_GROUPS_COLLECTION=Groups
```
> [!TIP]
> Рекомендуется также сконфигурировать файл ```.dockerignore``` для более оптимизированного запуска контейнеров: [см. документацию](https://docs.docker.com/build/concepts/context/)
3. Создать сборку контейнеров с помощью docker compose и запустить ее
```docker
docker compose up -d --build
```
> [!NOTE]
>По умолчанию файл docker compose настроен на запуск контейнера, вывод команды ```--help``` и остановку контейнера, чтобы настроить его на постоянную работу необходимо раскомментировать строку 
```#    command: tail -f /dev/null``` и закомментировать строку ```    command: python geogramint.py --help```
> >[!IMPORTANT]
> >База данных внутри docker-контейнера также работает без логина и пароля

### Базовые команды
1. Для начала работы сконфигурируйте файл ```config.ini``` командой:
<br>```
python geogramint.py set-config <api_id> <api_hash> <phone_number>```
<br><br>
```Где api_id и api_hash - данные для взаимодействия с API телеграм``` 
<br>([см. более подробно здесь](https://my.telegram.org))
<br>```phone_number - номер телефона пользователя```

2. Начните сканировать выбранную местность командой: <br>
```python geogramint.py start-scan <lat> <lon>```
<br><br>
```Где lat и lon - широта и долгота соответственно```
> [!IMPORTANT]
> Если программа выдает одни и те же адреса при разных показателях lat и lon подождите 5-10 минут и попробуйте повторить запрос

> [!NOTE]
> При первом запуске команды вас попросят авторизоваться в телеграм, выполните шаги по инструкции, которая отобразится в консоли

> [!NOTE]
> Данные о результатах запросов будут автоматически записаны в БД <important>GeogramintDB</important> с коллекциями <important>Groups, Users</important> и <important>ScanningResults</important>, где Groups и Users - группы и пользователи, ScanningResults - таблица-связка с временем отправки запроса и найденными группами и пользователями

3. Больше информации о CLI в официальной [Wiki](https://github.com/Alb-310/Geogramint/wiki/Demonstration:-CLI).
