# word2vec_from_wikipedia
 WikipediaからWord2Vecを行うプログラム群

# Step
## Wikipediaからデータをダウンロード
~~~ cmd
curl https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-pages-articles.xml.bz2 -o jawiki-latest-pages-articles.xml.bz2
~~~

## xmlからデータを取り出し
~~~ cmd
python -m wikiextractor.WikiExtractor jawiki-latest-pages-articles.xml.bz2
~~~

> [!NOTE]
> Windows + Python 3.11ではエラーが出ました．  
> どうやっても解決できなかったので，この処理はLinux上で行いました．

## 取り出したデータをまとめる
~~~ cmd
# Windows
for /r text %f in (*wiki*) do type "%f" >> wiki.txt
# Linux
find text/ | grep wiki | awk '{system("cat "$0" >> wiki.txt")}'
~~~

## データをきれいにする
~~~ cmd
python norm_words.py
~~~

## 単語ごとに分割する
~~~ cmd
python separating_words.py
~~~

## Word2Vecを実行する
~~~ cmd
python train_model.py
~~~