from monitoramento.enviroments import API_IOT
import requests

class EmwService:

    def __init__(self):
        pass

    def getDataByParams(time_to_start, time_to_end, dev_id, colection):
        time_to_start += "000000"
        time_to_end += "000000"
        response = requests.get(API_IOT +
                                "iot/findbyparams?timetostart=" + time_to_start +
                                "&timetoend=" + time_to_end +
                                "&dev_id=" + dev_id +
                                "&var=" + colection)
        return response


