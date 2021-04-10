# Niconico-Contributor-TagRanking

ニコニコ動画におけるタイトルもしくはタグに検索キーワードを含む動画を投稿している合計総合ポイントの高い投稿者のランキングのDBを作成するためのスクリプト

以下のようにデータベースを解析してランキング動画で使用しています 

https://www.upload.nicovideo.jp/garage/series/97621

A script for creating a ranking of posters with a high total total points who are posting videos that include search keywords in the title or tag of Nico Nico Douga.

We analyze the database as follows and use it in the ranking video

https://www.upload.nicovideo.jp/garage/series/97621

# DEMO

RTAでランキングDBを作成した時のDB出力内容

![EbatL8rU4AAB9Qe](https://user-images.githubusercontent.com/12876144/114283308-185c6100-9a84-11eb-83b6-8d893f4cc691.jpeg)
![EbatBHUUcAAwetl](https://user-images.githubusercontent.com/12876144/114283314-1befe800-9a84-11eb-82cc-efbd33f0f0ad.png)


# Requirement
* Python3
* SQLite3
* niconicoAPI
  * getthumbinfo
  * スナップショット検索API v2 (https://site.nicovideo.jp/search-api-docs/snapshot)


# Features

* ランキング用のDBを作成してキーワードに一致する動画の動画IDや再生数のデータを登録する
* そのあとに、投稿者100位のランキングテーブルを作成する
<br>

* Create a ranking DB and register the video ID and playback count data of videos that match the keywords.
* After that, create a ranking table for the 100th contributor

# Usage
```bash
pip install contextlib2 xml-python
```


# Author
* Dhiki(Infrastructure engineer & Video contributor)
* https://twitter.com/DHIKI_pico


# License
ご自由に使用いただいて構いません。

Feel free to use it.
