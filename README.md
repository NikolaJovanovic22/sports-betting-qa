# Python QA Automation Framework

Enterprise-grade hybrid automation framework for **UI and API testing**, built with **Python, Selenium WebDriver,
Pytest, Requests, and Allure Reporting**.

Designed for scalability, maintainability, and clean test architecture.

---

# Overview

This framework supports:

- UI automation testing
- API automation testing
- Hybrid UI + API workflows
- Cross-browser execution
- Rich reporting with Allure
- Screenshot capture on UI test failure
- Configurable environments
- Reusable Page Object architecture
- API Response Object pattern
- Centralized locator management

The framework is built to support modern QA engineering practices and enterprise-scale test automation initiatives.

---

# Tech Stack

| Area              | Technology            |
|-------------------|-----------------------|
| Language          | Python 3.10+          |
| Test Runner       | Pytest                |
| UI Automation     | Selenium WebDriver    |
| API Testing       | Requests              |
| Reporting         | Allure                |
| Assertions        | Pytest                |
| Browser Support   | Chrome, Firefox       |
| Design Pattern    | Page Object Model     |
| API Pattern       | Response Object / DTO |
| Config Management | Python config module  |
| CI/CD Ready       | Yes                   |

---

# Architecture Principles

This framework follows:

- Separation of concerns
- Reusability
- DRY principles
- Clear domain abstraction
- Test readability
- Encapsulation
- Framework scalability

Core architectural layers:

- Test Layer
- Page Object Layer
- Locator Layer
- API Client Layer
- API Response Layer
- Utility Layer
- Fixture Layer

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd project-root
```

---

## Create Virtual Environment

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Dependencies

Example `requirements.txt`:

```text
pytest
selenium
requests
allure-pytest
```

Install:

```bash
pip install -r requirements.txt
```

---

# Configuration

Framework behavior is driven by configuration.

Example:

```python
class Config:
    BASE_URL = "https://example.com"
    API_BASE_URL = "https://api.example.com"
    BROWSER = "chrome"
```

Supported browsers:

- chrome
- firefox

---

# Running Tests

# Run All Tests

```bash
pytest
```

---

# Run UI Tests

```bash
pytest tests/ui
```

---

# Run API Tests

```bash
pytest tests/api
```

---

# Run Specific Test

```bash
pytest tests/ui/test_single_bet_placement.py
```

---

# Run Specific Test Method

```bash
pytest tests/ui/test_login.py::test_successful_login
```

---

# Parallel Execution (Optional)

If using pytest-xdist:

```bash
pytest -n 4
```

---

# Browser Fixture

Browser initialization occurs only when UI tests explicitly request the `driver` fixture.

Example:

```python
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
```

Benefits:

- no browser startup for API tests
- faster execution
- clean fixture dependency model

---

# Screenshot on Failure

Automatic screenshot capture for UI test failures.

Implemented via:

- pytest hooks
- Allure attachments
- conditional driver access

Behavior:

- UI tests → screenshot + page source
- API tests → no browser interaction

Example artifacts:

- screenshot
- page HTML
- current URL

---

# Reporting with Allure

## Generate Results

```bash
pytest --alluredir=allure-results
```

---

## Open Report

```bash
allure serve allure-results
```

---

## Generate Static Report

```bash
allure generate allure-results --clean -o allure-report
```

---

# UI Framework Design

## Page Object Model

UI automation uses Page Object Model.

Responsibilities:

- encapsulate UI behavior
- centralize interactions
- improve test readability
- reduce duplication

Example:

```python
class SportsBettingPage(BasePage):

    def select_home_odds_for_betting(self, home_team, away_team) -> BetSlipPage:
        self.__select_match_odds(home_team, away_team, "home")
        return BetSlipPage(self.driver)
```

Test:

```python
@allure.title("E2E UI test - Single Bet Placement")
def test_single_bet_placement(driver):
    sports_betting_page = SportsBettingPage(driver)

    with allure.step("Navigate to Sports Betting QA Page"):
        sports_betting_page.open(config.SPORTS_BETTING_URL)
        sports_betting_page.wait_for_spinner_to_disappear()

    with allure.step("Get current Balance"):
        initial_balance = sports_betting_page.get_balance()

    with allure.step("Click odds to select outcome for betting"):
        bet_slip = sports_betting_page.select_home_odds_for_betting(home_team="Arsenal", away_team="Chelsea")

```

---

# Base Page

Shared browser actions:

- click
- type
- scroll
- waits
- assertions
- locator building

Example methods:

- `click()`
- `type()`
- `scroll_to_element()`
- `assert_enabled()`
- `assert_disabled()`
- `assert_attribute_value()`

---

# Locator Strategy

Locators are centralized.

Example:

```python
class MatchListLocators:
    MATCH_ODDS_BUTTON = (
        By.XPATH,
        "//div[@class='oddsGrid']//button[contains(@id, '{odds_button}')]"
    )

```

---

# LocatorBuilder

Reusable locator composition.

Supports:

- dynamic formatting
- xpath composition

Example:

```python
locator = LocatorBuilder.build(
    MatchListLocators.MATCH_CARD_BY_TEAMS,
    home_team=home_team,
    away_team=away_team
)
```

Appending child locator:

```python
odds_locator = LocatorBuilder.append_xpath(
    match_locator,
    odds_btn_locator
)
```

# API Framework Design

API layer follows:

- Base API Client
- Domain-specific clients
- Response DTO pattern

---

# Base API Client

Responsibilities:

- HTTP requests
- session management
- default headers
- request logging
- error handling

Example:

```python
class BaseApiClient:
    def __init__(
            self,
            base_url: str,
            default_headers: Optional[dict] = None
    ):
        self.base_url = base_url
        self.default_headers = default_headers or {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        self.session = requests.Session()
```

---

# API Fixtures

API clients are injected via fixtures.

Example:

```python
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
```

Benefits:

- clean dependency injection
- reusable clients
- isolated API testing

---

# API Response Object Pattern

Tests should not access raw JSON directly.

Preferred:

```python
response.id
```

---

# Match Response Example

```python
class MatchResponse(BaseApiResponse):

    @property
    def id(self):
        return get_by_path(self._data, "id")

    @property
    def competition(self):
        return get_by_path(self._data, "competition")
```

Usage:

```python
match = matches_response.first

assert match.id is not None
```

---

# Match List Response

Supports:

- indexing
- first item
- length
- assertions

Example:

```python
matches_response.assert_status(200)
matches_response.assert_not_empty()

match = matches_response.first
```

---

# Utilities

Reusable helpers:

## Path Utility

Safe nested JSON access.

Example:

```python
get_by_path(data, "odds.home")
```

---

## Date Utility

Example:

```python
get_current_time_hhmm()
```

Returns:

```text
15:42
```

---

## Parser Utility

Example:

```python
extract_amount("Balance: €120.00")
```

Returns:

```python
Decimal("120.00")
```

---

# Test Design Best Practices

Recommended:

- one business behavior per test
- clear assertions
- avoid implementation leakage
- no direct locator usage in tests
- no raw JSON parsing in tests
- API/UI abstraction boundaries

---

# Example UI Test

```python
def test_single_bet_placement(driver):
    sports_page = SportsBettingPage(driver)

    sports_page.select_match_odds(
        "Liverpool vs Arsenal",
        "2.35"
    )

    sports_page.bet_slip.assert_stake()
```

---

# Example API Test

```python
def test_api_sports_betting(betting_api):
    matches = betting_api.get_matches()

    matches.assert_status(200)
    matches.assert_not_empty()

    assert matches.first.id is not None
```

---

# Naming Conventions

Recommended:

## Tests

```text
test_api_sports_betting.py
test_single_bet_placement.py
```

---

## Pages

```text
bet_slip_page.py
sports_betting_page.py
```

---

## Locators

```text
modal_card_locators.py
match_list_locators.py
```

---

## API Clients

```text
sports_betting_api.py.py
```

---

# CI/CD Readiness

Framework supports CI execution.

Compatible with:

- Jenkins
- GitHub Actions
- GitLab CI
- Bitbucket Pipelines

Example:

```bash
pytest --alluredir=allure-results
```

---

# Troubleshooting

## Browser Starts During API Tests

Cause:

autouse fixture depends on driver.

Fix:

conditional fixture access.

---

## Circular Imports

Cause:

page objects importing each other.

Fix:

local imports inside methods.

---

## Invalid XPath

Cause:

appending full locator tuple instead of xpath string.

Fix:

use LocatorBuilder correctly.

---

## Allure Report Empty

Cause:

results folder missing.

Fix:

```bash
pytest --alluredir=allure-results
```

---

# Future Enhancements

Possible extensions:

- Selenium Grid support
- parallel browser matrix
- API schema validation
- contract testing
- DB validation layer
- test data factory
- authentication service abstraction
- environment switching
- retry strategy
- logging framework

---

# Author
njovanovic
QA Automation Framework  
Built for scalable enterprise-grade UI + API test automation.