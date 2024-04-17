import allure
from allure_commons.types import Severity
from selene import browser, by, be


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.feature("Поиск репозитория")
@allure.story("Лямбда шаги через with allure.step")
@allure.link("https://github.com", name="Testing")
def test_github_steps():
    with allure.step("Открыть странцу GitHub в браузере"):
        browser.open("https://github.com")

    with allure.step("Выполнить поиск репозитория"):
        browser.element(".header-search-button").click()
        browser.element("#query-builder-test").type("qa-guru/allure-notifications")
        browser.element("#query-builder-test").submit()

    with allure.step("Перейти по ссылки репозитория"):
        browser.element(by.link_text("qa-guru/allure-notifications")).click()

    with allure.step("Перейти на вкладку Issues"):
        browser.element("#issues-tab").click()

    with allure.step("Найти issue с номером "):
        browser.element(by.partial_text('#172')).should(be.visible)
