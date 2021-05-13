import json
from core.utils.common_data import CommonData
from core.utils.json_helper import JsonHelper


class Created:

    @staticmethod
    def created_feature(file_feature, client, file):
        client.set_method(CommonData.post)
        body = json.loads(open(file % file_feature).read())
        client.set_body(body)
        response_data = client.execute_request()
        JsonHelper.print_pretty_json(response_data.json())
        return response_data
