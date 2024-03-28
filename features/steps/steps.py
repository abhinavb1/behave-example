import requests
from behave import given, when, then
import sys

API_BASE_URL = "https://restcountries.com/v3.1/currency/"

@given('I give the currency code')
def step_impl(context):
    currency = context.config.userdata.get('currency')
    if currency is None:
        raise Exception("Currency not provided. Please provide currency using --D currency=<currency>")
    context.currency = currency

@given('I give the invalid currency code')
def step_impl(context):
    currency = context.config.userdata.get('Invalidcurrency')
    if currency is None:
        raise Exception("Currency not provided. Please provide Invalidcurrency using --D Invalidcurrency=<Invalidcurrency>")
    context.currency = currency

@when("I make a GET request to the restcountries API")
def make_get_request(context):
    context.response = requests.get(API_BASE_URL + context.currency)

@then("the status code should be {status_code}")
def verify_status_code(context, status_code):
    assert context.response.status_code == int(status_code), f"Expected status code {status_code}, but got {context.response.status_code}"

@then("at least one country name should be returned")
def verify_country_name(context):
    data = context.response.json()
    assert len(data) > 0, "No countries found for the given currency"
    assert "name" in data[0], "Country name not found in response"

@then("Save the company name")
def verify_save_name(context):
    data = context.response.json()
    print(data[0]["name"]["common"])

@then(u'the response should contain a message indicating the currency doesn\'t exist')
def verify_nonexistent_currency_message(context):
    data = context.response.json()
    print(data)
    assert "message" in data, "No error message found in response"
    assert "Not Found" in data["message"], "Incorrect error message"
