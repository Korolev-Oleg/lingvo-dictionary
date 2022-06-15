from typing import overload

from src.lingvo_api import LangMap


class LingvoAPI:
    auth_url: str
    token: str

    def auth(self): ...

    @overload
    def translation(self, text: str, srcLang: LangMap, dstLang: LangMap) -> str: ...

    def word_list(self, prefix: str, srcLang: LangMap, dstLang: LangMap, pageSize: int,
                  startPos: str = None) -> str: ...

    def minicard(self, text: str, srcLang: LangMap, dstLang: LangMap) -> str: ...

    def search(self, text: str, srcLang: LangMap, dstLang: LangMap, searchZone: int, startIndex: int,
               page_size: int) -> str: ...

    def article(self, heading: str, dictionary: str, srcLang: LangMap, dstLang: LangMap) -> str: ...

    def suggests(self, text: str, srcLang: LangMap, dstLang: LangMap) -> str: ...

    def word_forms(self, text: str, lang: int) -> str: ...

    def sound(self, dictionaryName, fileName: str): ...
