from typing import Optional
import requests
import allure
from tenacity import retry, stop_after_attempt, wait_exponential

from api.base.logger.api_logger import setup_logger

logger = setup_logger()
DEFAULT_TIMEOUT = 10


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

    DEFAULT_HEADERS = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    def get(self, endpoint: str, **kwargs):
        return self._request("get", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs):
        return self._request("post", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs):
        return self._request("put", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self._request("delete", endpoint, **kwargs)

    def set_headers(self, headers=None):
        final_headers = self.default_headers.copy()

        if headers:
            final_headers.update(headers)

        logger.info(f"Headers: {headers}")

        if headers is not None and not isinstance(headers, dict):
            raise TypeError("headers must be a dict")

        return final_headers

    @retry(stop=stop_after_attempt(3),
           wait=wait_exponential(multiplier=1, min=2, max=8))
    def _request(self, method: str, endpoint: str, **kwargs
                 ) -> requests.Response:

        # build URL
        url = self._build_url(endpoint)
        logger.info(f"{method.upper()} {url}")

        # logging json payload
        logger.info(f"Payload: {kwargs.get('data')}")

        with allure.step(f"{method.upper()} {endpoint}"):
            response = self.session.request(
                method=method,
                url=url,
                timeout=DEFAULT_TIMEOUT,
                **kwargs
            )

            logger.info(f"Status: {response.status_code}")
            logger.info(f"Response: {response.text}")

            allure.attach(
                response.text,
                name="Response",
                attachment_type=allure.attachment_type.JSON
            )

            return response

    def get_users(self, page=1):
        return requests.get(f"{self.base_url}/users", params={"page": page})

    def create_user(self, name, job):
        return requests.post(f"{self.base_url}/users", json={"name": name, "job": job})

    def _build_url(self, endpoint: str) -> str:
        return f"{self.base_url}/{endpoint.lstrip('/')}"
