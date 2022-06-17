import json
import os
from pprint import pprint

from src.lingvo_dictionary import LingvoAPI, LangMap
from dotenv import load_dotenv
import unittest


def assert_response_with_file(response, file_path):
    with open(file_path, 'r') as f:
        expected_response = json.load(f)


class TestLingvoApi(unittest.TestCase):
    api_key: str
    client: LingvoAPI

    def setUp(self) -> None:
        ...

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.api_key = os.getenv('LINGVO_API_KEY')
        assert cls.api_key is not None, 'LINGVO_API_KEY is not set in .env'
        cls.client = LingvoAPI(cls.api_key)
        cls.client.auth()
        cls.test = 'success'

    def test_translation(self):
        response = self.client.translation(
            text='mother',
            srcLang=LangMap.English,
            dstLang=LangMap.Russian
        )

        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)

    def test_wordlist(self):
        response = self.client.word_list(
            prefix='cheap',
            srcLang=LangMap.English,
            dstLang=LangMap.Russian,
            pageSize=10
        )
        self.assertIsInstance(response, dict)

    @unittest.skip('Not implemented')
    def test_wordlist_get_next_page(self):
        ...

    def test_minicard(self):
        response = self.client.minicard(
            srcLang=LangMap.English,
            dstLang=LangMap.Russian,
            text='durable'
        )
        self.assertIsInstance(response, dict)
        with open('response_mocks/minicard_durable_en_ru.json', 'r', encoding='utf-8') as f:
            self.assertDictEqual(response, json.load(f))

    def test_search(self):
        response = self.client.minicard(
            srcLang=LangMap.English,
            dstLang=LangMap.Russian,
            text='persistence'
        )
        self.assertIsInstance(response, dict)

    def test_article(self):
        response = self.client.article(
            srcLang=LangMap.English,
            dstLang=LangMap.Russian,
            heading='persistence',
            dict='Electronics%20(En-Ru)'
        )
        self.assertIsInstance(response, dict)

    def test_suggests(self):
        response = self.client.suggests(
            text='hello',
            srcLang=LangMap.English,
            dstLang=LangMap.Russian
        )

    #
    # def test_sound(self):
    #     ...
