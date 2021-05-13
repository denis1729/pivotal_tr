from behave import given, then
from compare import expect

from core.logger.singleton_logger import SingletonLogger
from core.rest_client.request_manager import RequestManager, config_data
from core.utils.json_helper import JsonHelper

logger = SingletonLogger().get_logger()


@given(u'I {method} to {endpoint} endpoint')
def step_impl(context, method, endpoint):
    logger.info("Configure Client")
    client = RequestManager()
    client.set_method(method)
    client.set_endpoint(config_data['endpoints'][endpoint])
    context.client = client


@given(u'I send the request')
def step_impl(context):
    logger.info("Execute Request")
    client = context.client
    context.response = client.execute_request()
    client.set_endpoint(config_data['endpoints']['project'] % 2203385)
    JsonHelper.print_pretty_json(client.execute_request().json())
    print(client.execute_request().json())


@then(u'I should get response with status code {status_code}')
def step_impl(context, status_code):
    logger.info("Validation Smoke")
    expect(int(status_code)).to_equal(context.response.status_code)
