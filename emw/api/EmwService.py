from estacoes.api.serializers import EstacaoSerializer
from estacoes.models import Estacao
from monitoramento.enviroments import API_IOT, API_IA
from datetime import datetime
import requests
import pandas as pd


class EmwService:

    def __init__(self):
        pass

    def getDataByParams(self, time_to_start, time_to_end, dev_id, colection):
        try:
            time_to_start += "000000"
            time_to_end += "000000"
            response = requests.get(API_IOT +
                                    "iot/findbyparams?timetostart=" + time_to_start +
                                    "&timetoend=" + time_to_end +
                                    "&dev_id=" + dev_id +
                                    "&var=" + colection)
            return response
        except Exception:
            raise Exception("error verify if api IOT is up")

    def getSamples(self, samples):
        times = []
        values = []
        data = []
        for sample in samples:
            times.append(datetime.fromtimestamp(sample['time'] / 1e6))
            values .append(sample['value'])
        data_frame = pd.DataFrame({"date": times, "value": values})
        data_frame_grouped = data_frame.groupby(pd.Grouper(key='date', freq='6H')).mean()
        for index, row in data_frame_grouped.iterrows():
            data.append({"time": str(index), "value": row.value})
        return data

    def getPrediction(self, time_to_end, dev_id, colection, type_forecast):
        try:
            estacao = Estacao.objects.filter(serial_number=dev_id).first()
            time_to_end += "000000"
            response = requests.get(API_IA +
                                    "?timetoend=" + time_to_end +
                                    "&dev_id=" + dev_id +
                                    "&var=" + colection +
                                    "&estacaomodelo=" + estacao.estacao_modelo.code +
                                    "&typeforecast=" + type_forecast)
            return response

        except Exception:
            raise Exception("error verify if api IA is up")
