API_IOT = 'http://backend-iot-env.eba-prhv4rz9.sa-east-1.elasticbeanstalk.com/'
#API_IOT = 'http://127.0.0.1:8888/'

#API_IA = 'http://127.0.0.1:8801/'
API_IA = 'http://backend-ai-env.eba-p58uytsh.sa-east-1.elasticbeanstalk.com/'

#Database aws
database = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'monitoramento',
    'USER': 'root',
    'PASSWORD': '2021monitoramento',
    'HOST': 'monitoramento.csmwyo4wds2l.sa-east-1.rds.amazonaws.com',
    'PORT': '3306',
}

# Database localhost
# database = {
#     'ENGINE': 'django.db.backends.mysql',
#     'NAME': 'monitoramento',
#     'USER': 'root',
#     'PASSWORD': '123456',
#     'HOST': 'localhost',
#     'PORT': '3306',
# }