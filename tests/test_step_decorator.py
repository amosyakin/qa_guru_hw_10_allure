import allure
from allure_commons.types import Severity
from selene import browser, by, be


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.feature("Поиск репозитория")
@allure.story("Шаги с декоратором @allure.step")
@allure.link("https://github.com", name="Testing")
def test_github_decorator_steps():
    open_github()
    search_repo()
    open_repo()
    open_issue_tab()
    search_issue()

@allure.step("Открыть странцу GitHub в браузере")
def open_github():
    browser.open("https://github.com")

@allure.step("Выполнить поиск репозитория")
def search_repo():
    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").type("qa-guru/allure-notifications")
    browser.element("#query-builder-test").submit()

@allure.step("Перейти по ссылки репозитория")
def open_repo():
    browser.element(by.link_text("qa-guru/allure-notifications")).click()

@allure.step("Перейти на вкладку Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()

@allure.step("Найти issue с номером ")
def search_issue():
    browser.element(by.partial_text('#172')).should(be.visible)
