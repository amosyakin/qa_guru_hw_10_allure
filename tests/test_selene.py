from selene import browser, by, be


def test_github_selene():
    browser.open("https://github.com")

    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").type("qa-guru/allure-notifications")
    browser.element("#query-builder-test").submit()

    browser.element(by.link_text("qa-guru/allure-notifications")).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text('#172')).should(be.visible)
