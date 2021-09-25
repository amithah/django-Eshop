from myShop.settings.common import *

DEBUG = False
SECRET_KEY = os.getenv("SECRET_KEY")
ALLOWED_HOSTS = ['127.0.0.1', '.ec2-52-91-52-24.compute-1.amazonaws.com', '52.91.52.24', '0.0.0.0', 'localhost']
