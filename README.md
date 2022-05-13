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


## Etapy pracy nad projektem
1. Pobranie do pojedynczych zmiennych składowych pojedyńczych opinii
2. Zapisanie wszystkich składowych pojedynczej opinii do słownika
3. Pobranie wszystkich opinii z pojedynczej strony do słowników i zapisanie ich na liście
4. Zapisanie wszystkich opinii z listy do pliku .json
5. Pobranie wszystkich opinii o produkcie i zapisanie ich na liście w postaci słowników
6. Dodanie mozliwości podania kodu produktu przez uzytkownikow
7. Optymalizacja kodu:
    a. utworzenie funkcji do ekstrakcji elementow strony 
    b. utworzenie slownika selektorow
    c. uzycie dictionary comprehension do pobrania skladowych pojedynczej opinii na podstawie slownika selektorow
8.  Analiza pobranych opinii dla konkretnego produktu:
    a. wyliczenie podstawowych statystyk:
        - liczba wszystkich opinii
        - liczba opinii dla ktorych podano zalety
        - liczba opinii dla ktorych podano wady 
        -srednia ocena produktu
    b.przygotowanie wykresow:
        -udzial poszczegolnych rekomendacji w ogolnej liczbie opinii
        - histogram wystepowania poszzgolnych ocen