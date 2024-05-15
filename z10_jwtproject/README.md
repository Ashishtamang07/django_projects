# set up simple jwt 
# setup corsheaders 
 when u connect api to frontend cors policy error occurs 
 how to setup - 
 install package,
 python -m pip install django-cors-headers
 INSTALLED_APPS = [
    ...,
    "corsheaders",
    ...,
]
MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    ...,
]
CORS_ALLOWED_ORIGINS = [

    "http://localhost:8080",
    "http://127.0.0.1:9000",
]
# .env file 
pip install django-dotenv
load env_load() in manage.py 
