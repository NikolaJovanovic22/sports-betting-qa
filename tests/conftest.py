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

    driver.quit()


@pytest.fixture
def api():
    return api_client.ApiClient(base_url=config.API_URL)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, driver):
    yield

    if request.node.rep_call.failed:
        screenshot = driver.get_screenshot_as_png()

        allure.attach(
            screenshot,
            name="Screenshot on Failure",
            attachment_type=allure.attachment_type.PNG
        )
