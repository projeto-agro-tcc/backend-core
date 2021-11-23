from rest_framework import status
from previsao.models import Previsao
from utils.exceptions.catalogo_exceptions import CustomValidation

class PrevisaoService:

    def __init__(self):
        pass

    def save_previsao(previsao):
        try:
            previsao.save()
        except Exception as error:
            raise CustomValidation(error, 'detail', status_code=status.HTTP_409_CONFLICT)