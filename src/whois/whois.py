import json
import os
from http import HTTPStatus

import requests

__all__ = ['Whois']

PROMPTAPI_ENDPOINT = 'https://api.promptapi.com/whois'
DEFAULT_TIMEOUT = 10


class Whois:
    def __init__(self):
        self.timeout = DEFAULT_TIMEOUT
        self.apikey = None
        self.data = None

    def _validate(self):
        apikey = os.environ.get('PROMPTAPI_TOKEN', None)
        if not apikey:
            return dict(error='You need to set PROMPTAPI_TOKEN environment variable')
        self.apikey = apikey
        return dict(valid=True)

    def _http(self, endpoint, method, params=None, body=None):
        if body is None:
            body = dict()

        headers = dict(apikey=self.apikey)
        http_error = None

        try:
            response = requests.request(
                method,
                endpoint,
                timeout=self.timeout,
                params=params,
                headers=headers,
                data=body,
            )
            response.raise_for_status()
        except requests.exceptions.Timeout:
            return dict(
                error='Connection timeout error',
                status=response.status_code,
            )
        except requests.exceptions.TooManyRedirects:
            return dict(
                error='Too many redirects error',
                status=response.status_code,
            )
        except requests.exceptions.ConnectionError:
            return dict(
                error='Connection error',
                status=response.status_code,
            )
        except requests.exceptions.HTTPError as err:
            http_error = dict(
                error=str(err),
                status=response.status_code,
            )
        try:
            result = response.json()
        except json.decoder.JSONDecodeError as err:
            return dict(
                error=f'JSON decoding error: {str(err)}',
                status=response.status_code,
            )

        if http_error:
            return dict(
                error=result.get('message', http_error),
                status=response.status_code,
            )

        if response.status_code != HTTPStatus.OK.value:
            return dict(
                error=result.get('message', response.reason),
                status=response.status_code,
            )
        return dict(result=result.get('result', None), status=response.status_code)

    def check(self, domain, timeout=DEFAULT_TIMEOUT):
        endpoint = f'{PROMPTAPI_ENDPOINT}/check'
        params = dict(domain=domain)

        validation_result = self._validate()
        if validation_result.get('error', None):
            return validation_result
        self.timeout = timeout

        response = self._http(endpoint, 'GET', params)
        return response

    def query(self, domain, timeout=DEFAULT_TIMEOUT):
        endpoint = f'{PROMPTAPI_ENDPOINT}/query'
        params = dict(domain=domain)

        validation_result = self._validate()
        if validation_result.get('error', None):
            return validation_result
        self.timeout = timeout

        response = self._http(endpoint, 'GET', params)
        return response
