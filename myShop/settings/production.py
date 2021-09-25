from .common import *

DEBUG = False
SECRET_KEY = os.getenv("SECRET_KEY")
ALLOWED_HOSTS = ['127.0.0.1', '.ec2-54-89-68-86.compute-1.amazonaws.com', '54.89.68.86', '0.0.0.0', 'localhost']
