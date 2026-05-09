import allure
import pytest
from selenium import webdriver
import config
from api.sports_betting_api import SportsBettingApi


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
def betting_api():
    return SportsBettingApi(
        base_url=config.API_URL,
        default_headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "x-user-id": config.USER_ID
        }
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)


@pytest.fixture(autouse=True)
def attach_artifacts_on_failure(request):
    yield

    report = getattr(request.node, "rep_call", None)

    if report is None or not report.failed:
        return

    driver = request.getfixturevalue("driver") if "driver" in request.fixturenames else None

    if driver is None:
        return

    allure.attach(
        driver.get_screenshot_as_png(),
        name="Failure Screenshot",
        attachment_type=allure.attachment_type.PNG
    )

    allure.attach(
        driver.page_source,
        name="Page Source",
        attachment_type=allure.attachment_type.HTML
    )
