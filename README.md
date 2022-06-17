### Installation

``` shell
pip install lingvo-dictionary
```

### Usage
``` python
from lingvo_dictionary import LingvoAPI, LangMap

client = LingvoAPI("YOUR_API_KEY")
client.auth()

# you can extract language code by using LangMap
src_lang = LangMap.English
dst_lang = LangMap.French

# all client methods using key=value api arguments 
# described in lingvio_dictionary._client.pyi
result: dict = client.translation(
    text="Floccinaucinihilipilification",
    srcLang=src_lang,
    dstLang=dst_lang
)
```

### Get available languages
``` python
from pprint import pprint
from lingvo_dictionary import LangMap

pprint(LangMap().__dict__)
```
