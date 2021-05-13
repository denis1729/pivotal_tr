import json

from behave import given, then, step, when
from compare import expect
from jsonschema import validate

from core.logger.singleton_logger import SingletonLogger
from core.rest_client.request_manager import RequestManager, config_data
from core.utils.json_helper import JsonHelper
from core.utils.common_data import CommonData

logger = SingletonLogger().get_logger()


@given(u'I {method} to {endpoint} endpoints')
def step_impl(context, method, endpoint):
    logger.info("Configure Client for account membership ")
    client = RequestManager()
    client.set_method(method)
    client.set_endpoint(config_data[CommonData.endpoint][endpoint] % context.id_account)
    context.client = client


@given("I {method} to {endpoint} endpoint with specific id")
def step_impl(context, method, endpoint):
    logger.info("Configure Client for account membership with specific id")
    client = RequestManager()
    client.set_method(method)
    client.set_endpoint(config_data[CommonData.endpoint][endpoint] % (context.id_account, context.id))
    context.client = client


@given("I {method} to {endpoint} endpoint for account")
def step_impl(context, method, endpoint):
    logger.info("Configure Client for accounts and account summaries")
    client = RequestManager()
    client.set_method(method)
    client.set_endpoint(config_data[CommonData.endpoint][endpoint])
    context.client = client


@given("I {method} to {endpoint} endpoint with id {id}")
def step_impl(context, method, endpoint, id):
    logger.info("Configure Client for account with specific id")
    client = RequestManager()
    client.set_method(method)
    client.set_endpoint(config_data[CommonData.endpoint][endpoint] % context.id_account)
    context.client = client


@step(u'I send the requests')
def step_impl(context):
    logger.info("Execute Request for a feature")
    client = context.client
    context.response = client.execute_request()
    print(context.response.json)


@then(u'I should get responses with status code {status_code}')
def step_impl(context, status_code):
    logger.info("Validation Smoke code response= " + str(context.response.status_code))
    expect(int(status_code)).to_equal(context.response.status_code)


@step("I send the following information {file} for the feature")
def step_impl(context, file):
    logger.info("Execute Request for create and update feature")
    client = context.client
    body = json.loads(open(CommonData.file_accounts % file).read())
    context.file_json = body
    client.set_body(body)


@then("I will validate that the created fields are the same")
def step_impl(context):
    logger.info("Validation crud for created ")
    for data, value in context.file_json.items():
        print(">>>>>> " + str(context.file_json[data]), ">>>>>" + str(context.response.json()[CommonData.person][data]))
        expect(context.file_json[data]).to_equal(context.response.json()[CommonData.person][data])


@step("I will validate that the update fields are the same")
def step_impl(context):
    logger.info("Validation crud for updated ")
    JsonHelper.print_pretty_json(context.response.json())
    for data, value in context.file_json.items():
        print(">>>>>> " + str(context.file_json[data]), ">>>>>" + str(context.response.json()[data]))
        expect(context.file_json[data]).to_equal(context.response.json()[data])


@then("I will validate that the feature has been deleted")
def step_impl(context):
    pass


@then("I will validate that the information is correct for {file}")
def step_impl(context, file):
    schema = json.loads(open(CommonData.schema_accounts % file).read())
    expect(True).to_equal(validate_schema(context.response, schema))


@step("I sent the {permission}")
def step_impl(context, permission):
    client = context.client
    client.set_parameters(json.loads(open(CommonData.file_accounts % permission).read()))
    context.client = client


@when("I update the next fields with {name},{email},{initials}")
def step_impl(context, name, email, initials):
    client = context.client
    data = context.file_json
    data["name"] = name
    print(type(name))
    data["email"] = email
    data["initials"] = initials
    print(data)
    client.set_body(data)
    context.client = client


@step("I keep the id the created feature")
def step_impl(context):
    print(context.response.json)
    context.id = context.response.json()[CommonData.person][CommonData.id]
    JsonHelper.print_pretty_json(context.response.json())


def validate_schema(response, schema):
    try:
        data = validate(response, schema)
        if str(data).__eq__('None'):
            return True
    except ValueError:
        return ValueError


@step("I send the following information for create a membership")
def step_impl(context):
    client = context.client
    print(context.text)
    body = json.dumps(context.text)
    print(body)
    client.set_body(json.loads(context.text))
    context.client = client


@step("I verify the {message}")
def step_impl(context, message):
    """
    :type context: behave.runner.Context
    :type message: str
    """
    raise NotImplementedError(u'STEP: And  I verify the <message>')