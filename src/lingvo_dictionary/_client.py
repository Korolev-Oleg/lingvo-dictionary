import requests

from lingvo_dictionary._exceptions import LingvoException


class LingvoAPI:
    """
    Note:
        Documentation: https://developers.lingvolive.com/en-us/Help
    """
    service_url = 'https://developers.lingvolive.com/'
    api_prefix = 'api/v1/'
    token = None

    def __init__(self, api_key):
        self.api_key = api_key

    def auth(self):
        """ Upon successful authentication, the client receives a Bearer token,
        which must be applied to subsequent requests in the Authorization header.
        Otherwise, a message stating that authentication failed with code 401.
        The validity period of the token is a day. After a day, or when you
        receive a 401 error from the translation methods, you need to call this
        method again and get a new token."""
        headers = {'Authorization': 'Basic ' + self.api_key}
        response = requests.post(self.service_url + 'api/v1/authenticate',
                                 headers=headers)
        self.token = response.json()
        return self.token

    def translation(self, **kwargs):
        """Dictionary translation of a word/phrase.
        The search is carried out only in the specified direction."""
        return self._request(
            action='Translation',
            params=dict(**kwargs)
        )

    def word_list(self, **kwargs):
        """Part of the word list for available dictionaries."""
        return self._request(
            action='WordList',
            params=dict(**kwargs)
        )

    def minicard(self, **kwargs):
        """Minicard (short translation for word or phrase)."""
        return self._request(
            action='Minicard',
            params=dict(**kwargs)
        )

    def search(self, **kwargs):
        """Fulltext search among articles from available dictionaries."""
        return self._request(
            action='Search',
            params=dict(**kwargs)
        )

    def article(self, **kwargs):
        """Exact article from specified Lingvo dictionary."""
        return self._request(
            action='Article',
            params=dict(**kwargs)
        )

    def suggests(self, **kwargs):
        """Suggests / spelling for given word or phrase."""
        return self._request(
            action='Suggests',
            params=dict(**kwargs)
        )

    def word_forms(self, **kwargs):
        """Word forms (paradigms)."""
        return self._request(
            action='WordForms',
            params=dict(**kwargs)
        )

    def sound(self, **kwargs):
        """Returns sound file. All input parameters can be found in Lingvo articles
         (e. g. /Translation, /Minicard, etc.)."""
        return self._request(
            action='Sound',
            params=dict(**kwargs)
        )

    def _request(self, action, params):
        headers = {'Authorization': 'Bearer ' + self.token}
        query_params = "&".join(
            [f"{k}={params[k]}" if params[k] else "" for k in params]
        )

        url = self.service_url + self.api_prefix + action + f'?{query_params}'
        response = requests.get(url=url, headers=headers)

        if response.status_code != 200:
            raise LingvoException(response)
        return response.json()
