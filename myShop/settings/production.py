from myShop.settings.common import *
DEBUG =False
SECRET_KEY =os.getenv("SECRET_KEY")
ALLOWED_HOSTS = ['127.0.0.1','.ec2-54-90-75-96.compute-1.amazonaws.com','54.90.75.96']