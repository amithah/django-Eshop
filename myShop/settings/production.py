from myShop.settings.common import *
DEBUG =False
SECRET_KEY =os.getenv("SECRET_KEY")
ALLOWED_HOSTS = ['127.0.0.1','.ec2-34-226-147-101.compute-1.amazonaws.com']