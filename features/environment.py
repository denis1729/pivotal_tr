from core.rest_client.request_manager import RequestManager, config_data

from core.utils.common_data import CommonData
from core.utils.created import Created
from core.utils.deleted import Deleted
from core.utils.list_feature import ListFeature


def before_scenario(context, scenario):
    client = RequestManager()
    if 'account_list' in scenario.tags:
        print("___________________Select account_________________")
        context.id_account = ListFeature.select_feature(CommonData.endpoint_accounts, client)
        print(context.id_account)

    if 'create' in scenario.tags:
        print("___________________Created membership_________________")
        client.set_endpoint(config_data[CommonData.endpoint][CommonData.endpoint_create] % context.id_account)
        data = Created.created_feature(CommonData.account_file, client, CommonData.file_accounts)
        context.id = data.json()[CommonData.person][CommonData.id]


def after_scenario(context, scenario):
    client = RequestManager()
    if 'delete' in scenario.tags:
        print("___________________Deleted membership_________________")
        client.set_endpoint(
            config_data[CommonData.endpoint][CommonData.endpoint_delete] % (context.id_account, context.id))
        Deleted.delete_feature(client)
