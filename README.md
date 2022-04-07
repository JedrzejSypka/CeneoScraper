# CeneoScraper


## Struktura opinii w serwisie (ceneo.pl)
(https://www.ceneo.pl)

|Składowa|Selesktor|Nazwa zmiennej|Typ zmiennej|
|--------|---------|--------------|------------|
|opinia|div.js_produkt-review|||
|identyfikator opinii| div.js_product-review \["data-entry-id"\]|||
|autor opinii|user-post-post__author-name|||
|rekomendacje|span.user-post__author-recoendation > em|||
|liczba gwiazdek|span.user-post__score-count|||
|treśc opinii|div.user-post__text|||
|lista zalet|div.review-feature__item--positives ~ div.review-feature__item |||
|lista wad|div.review-feature__item--negatives ~ div.review-feature__item |||
|dla ilu osób przydatna|span[id^="votes-yes"]|||
|dla ilu osób nieprzydatna|span[id^="votes-no"]|||
|data wystawienia opinii|span.user-post__published > time:nth-child(1)["datetime"]|||
|data zakupu|span.user-post__published > time:nth-child(2_["datetime"]|||
