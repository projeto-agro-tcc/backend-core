from datetime import datetime

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.utils import json
from rest_framework.viewsets import ModelViewSet

from emw.api.EmwService import EmwService
from emw.api.serializer import EmwSerializer


class EmwViewSet(ModelViewSet):
    serializer_class = EmwSerializer

    @action(detail=False, methods=['GET'])
    def findbyparams(self, request, *args, **kwargs):
        time_to_start = request.query_params.get('timetostart')
        time_to_end = request.query_params.get('timetoend')
        dev_id = request.query_params.get('dev_id')
        colection = request.query_params.get('var')
        if (time_to_start and dev_id and colection) is not None:
            if time_to_end is None:
                time_to_end = datetime.now().timestamp()
            response = EmwService.getDataByParams(time_to_start, time_to_end, dev_id, colection)
            result_data = EmwSerializer(json.loads(response.text), many=True).data
            return Response(result_data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Verify the fields"}, status=status.HTTP_400_BAD_REQUEST)
