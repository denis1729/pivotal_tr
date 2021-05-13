from core.utils.common_data import CommonData


class Deleted:

    @staticmethod
    def delete_feature(client):
        client.set_method(CommonData.delete)
        response_data = client.execute_request()
        return response_data
