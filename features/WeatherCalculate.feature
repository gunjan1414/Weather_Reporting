#noinspection CucumberUndefinedStep
Feature: WeatherCalculate

  @WeatherCalculate
  Scenario Outline: WeatherCalculate
    Given Open the webWindow
    Given Login to weather website
    Given I click on "input_tab"
    Given I input text "<city>" to object "input_tab"
    Given I get text of "temp" and store it in variable "city_temperature"
    Given I set api with URL "api_url"
    Given I hit json with file "JSON"
    Examples:
      | city|
      | Kota, Rajasthan|