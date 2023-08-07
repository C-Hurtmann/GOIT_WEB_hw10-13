import configparser
from mongoengine import connect

from pathlib import Path

import environ
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()
env.read_env(BASE_DIR / '.env')

user = env('MONGO_USER')
password = env('MONGO_PASS')
db_name = env('MONGO_DB_NAME')
domain = env('MONGO_DOMAIN')

connect(db=db_name,
        username=user,
        password=password,
        host=f'mongodb+srv://{user}:{password}@{domain}.{db_name}.mongodb.net/?retryWrites=true&w=majority',
        ssl=True)
