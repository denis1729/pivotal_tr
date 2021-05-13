from core.rest_client.request_manager import config_data
from core.utils.common_data import CommonData


class ListFeature:

    @staticmethod
    def select_feature(endpoint, client):
        client.set_method(CommonData.get)
        client.set_endpoint(config_data[CommonData.endpoint][endpoint])
        response_data = client.execute_request()
        id = response_data.json()[0][CommonData.id]
        return id
