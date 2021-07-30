import json
import logging
from configparser import ConfigParser
from pathlib import Path

from behave import *
from utilities.Driver import Driver
from utilities.HitRequest import HitRequest
from utilities.Login import Login
from utilities.RandomVariable import RandomVariable
from utilities.Element import Element


@given("Open the webWindow")
def step_impl(context):
    Driver.open_browser()


@given('Login to weather website')
def step_impl(context):
    Login.login(context)


@given(u'I click on "(.*)"')
def step_impl(context, text):
    Element.click(context, text)


@given(u'I input text "(.*)" to object "(.*)"')
def step_impl(context, text, obj):
    Element.input(context, text, obj)


@given(u'I get text of "(.*)" and store it in variable "(.*)"')
def step_impl(context, obj, var):
    res = Element.get_text_for_all(context, obj)
    RandomVariable.variable(str(var), str(res))


@given(u'I set api with URL "(.*)"')
def step_impl(context, issue_resource):
    path = Path('..').cwd().as_posix()
    context.parser = ConfigParser()
    file = path + '/properties/' + 'config.properties'
    context.parser.read(file)
    context.hostname = context.parser.get("config", issue_resource)
    context.endpoint = None


@step(u'I hit api with API "(.*)"')
def step_impl(context, filename):
    context.response = HitRequest.send_post_request(context, filename)



