# CeneoScraper


## Struktura opinii w serwisie (ceneo.pl)
(https://www.ceneo.pl)

|Składowa|Selesktor|Nazwa zmiennej|Typ zmiennej|
|--------|---------|--------------|------------|
|opinia|div.js_produkt-review|opinion|bs4.element.Tag|
|identyfikator opinii| div.js_product-review \["data-entry-id"\]|opinion_id|str|
|autor opinii|user-post-post__author-name|author|str|
|rekomendacje|span.user-post__author-recomendation > em|recommendation|str|
|liczba gwiazdek|span.user-post__score-count|stars|int|
|treśc opinii|div.user-post__text|content|str|
|lista zalet|div.review-feature__item--positives ~ div.review-feature__item |pros||
|lista wad|div.review-feature__item--negatives ~ div.review-feature__item |cons||
|dla ilu osób przydatna|span[id^="votes-yes"]|useful||
|dla ilu osób nieprzydatna|span[id^="votes-no"]|useless||
|data wystawienia opinii|span.user-post__published > time:nth-child(1)["datetime"]|publish_date||
|data zakupu|span.user-post__published > time:nth-child(2_["datetime"]|purchase_date||
