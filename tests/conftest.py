import allure
import pytest
from selenium import webdriver
from utils import config, api_client


@pytest.fixture
def driver(request):
    if config.BROWSER == "chrome":
        driver = webdriver.Chrome()
    elif config.BROWSER == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")
    driver.maximize_window()
    yield driver

    # if request.node.rep_call.failed:
    #     # Attach screenshot
    #     allure.attach(
    #         driver.get_screenshot_as_png(),
    #         name="screenshot",
    #         attachment_type=allure.attachment_type.PNG
    #     )
    #     # Attach page source
    #     allure.attach(
    #         driver.page_source,
    #         name="page_source",
    #         attachment_type=allure.attachment_type.HTML
    #     )
    driver.quit()


@pytest.fixture
def api():
    return api_client.ApiClient(base_url=config.API_URL)


# Hook for attaching screenshots on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"Failure Screenshot - {item.name}",
                attachment_type=allure.attachment_type.PNG
            )
            # Attach page source
            allure.attach(
                driver.page_source,
                name="page_source",
                attachment_type=allure.attachment_type.HTML
            )
