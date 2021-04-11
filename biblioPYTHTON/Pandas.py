#задание1
import pandas as pd


a = {
    "author_id": [1, 2, 3],
    "author_name": ['Тургенев', 'Чехов', 'Островский']
}
authors = pd.DataFrame(a)

b = {
    "author_id": [1, 1, 1, 2, 2, 3, 3],
    "book_title": ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий',
                   'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
    "price": [450, 300, 350, 500, 450, 370, 290]
}

book = pd.DataFrame(b)

#задание2

author_price = pd.merge(authors, book, on='author_id', how='inner')

#задание3

top5 = author_price.nlargest(5, "price")

#задание4
gr = author_price.groupby("author_name")
ma = gr.agg({"price": "max"})
mi = gr.agg({"price": "min"})
me = gr.agg({"price": "mean"})

e = pd.merge(mi, ma, on="author_name", how="outer")
author_stat = pd.merge(e, me, on="author_name", how="outer")
author_stat

#Остальное не успел...