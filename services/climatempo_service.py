import requests


class ClimatempoService():
    _api_url = "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale"
    _token_climatempo = "b22460a8b91ac5f1d48f5b7029891b53"
    _default_days = 15

    def get(self, id):
        request = requests.get(
            f"{self._api_url}/{id}/days/{self._default_days}?token={self._token_climatempo}")

        return request.json()
