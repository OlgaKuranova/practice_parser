# Создание парсера на Python

Описание:
В ходе работы создается парсер веб-сайта [Quotes to Scrape](https://quotes.toscrape.com/), который обходит указанный сайт и извлекает цитаты и их авторов с каждой страницы. Данные преобразуются в CSV-файл. 
В проекте используются библиотеки requests для выполнения HTTP-запросов и bs4 для сбора информации и извлечения данных.


## Как запустить программу
1. Скачайте все файлы проекта из репозитория и запустите в любой среде разработке, поддерживающей Python
2. Установите необходимые библиотеки для проекта с помощью команды:
   
```
$ pip install requests bs4
```

3. После успешной работы программы, извлеченные данные (цитаты и их авторы) появятся в файле quotes.csv



### Дополнительная информация
Полезные материалы:

[User agents для веб-скрапинга](https://ru-brightdata.com/blog/how-tos-ru/user-agents-for-web-scraping-101)

[Основы парсинга на Python](https://habr.com/ru/companies/selectel/articles/754674/)

[Парсинг сайта вместе с Python и библиотекой Beautiful Soup](https://skillbox.ru/media/code/parsing-sayta-vmeste-s-python-i-bibliotekoy-beautiful-soup-prostaya-instruktsiya-v-tri-shaga/)


Программа разрабатывалась в IDE PyCharm Community Edition 2022.2.3.
