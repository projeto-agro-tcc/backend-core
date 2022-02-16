from datetime import datetime

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.utils import json
from rest_framework.viewsets import ModelViewSet

from emw.api.EmwService import EmwService
from emw.api.serializer import EmwSerializer, EmxSampleSerializer
from utils.exceptions.catalogo_exceptions import CustomValidation


class EmwViewSet(ModelViewSet):
    emw_service = EmwService()

    @action(detail=False, methods=['GET'])
    def findbyparams(self, request, *args, **kwargs):
        try:
            time_to_start = request.query_params.get('timetostart')
            time_to_end = request.query_params.get('timetoend')
            dev_id = request.query_params.get('dev_id')
            colection = request.query_params.get('var')
            if (time_to_start and dev_id and colection) is not None:
                if time_to_end is None:
                    time_to_end = datetime.now().timestamp()
                response = self.emw_service.getDataByParams(time_to_start, time_to_end, dev_id, colection)
                result_data = EmwSerializer(json.loads(response.text), many=True).data
                return Response(result_data, status=status.HTTP_200_OK)
            raise Exception("Verify fields")
        except Exception as err:
            raise CustomValidation(err, 'detail', status_code=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'])
    def samples(self, request, *args, **kwargs):
        try:
            time_to_start = request.query_params.get('timetostart')
            time_to_end = request.query_params.get('timetoend')
            dev_id = request.query_params.get('dev_id')
            colection = request.query_params.get('var')
            if (time_to_start and dev_id and colection) is not None:
                if time_to_end is None:
                    time_to_end = datetime.now().timestamp()
                response_json = json.loads(self.emw_service.getDataByParams(time_to_start, time_to_end, dev_id, colection).text)
                response = self.emw_service.getSamples(response_json)
                result_data = EmxSampleSerializer(response, many=True).data
                return Response(result_data, status=status.HTTP_200_OK)
            raise Exception("Verify fields")
        except Exception as err:
            raise CustomValidation(err, 'detail', status_code=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'])
    def prediction(self, request, *args, **kwargs):
        try:
            time_to_end = request.query_params.get('timetoend')
            dev_id = request.query_params.get('dev_id')
            colection = request.query_params.get('var')
            type_forecast = request.query_params.get('typeforecast')
            if (time_to_end and dev_id and colection and type_forecast) is not None:
                response_json = json.loads(self.emw_service.getPrediction(time_to_end, dev_id, colection, type_forecast).text)
                result_data = EmxSampleSerializer(response_json, many=True).data
                return Response(result_data, status=status.HTTP_200_OK)
            raise Exception("Verify fields")
        except Exception as err:
            raise CustomValidation(err, 'detail', status_code=status.HTTP_400_BAD_REQUEST)
