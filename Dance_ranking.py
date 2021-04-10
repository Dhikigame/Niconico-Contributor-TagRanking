# coding:utf-8
import sqlite3
import analysis.db as db
import analysis.stats as stats
import analysis.db_create as db_create
import os


# DB作成
db_path = "./analysis/db_ranking/DANCE.db"
table_name = "dance"
if os.path.exists(db_path) == True:
    os.remove(db_path)
db_create.db_create(db_path, table_name)

# タグ別のリストと動画総数のインスタンス生成 #
print("【キーワードに合致する動画を全てDBに保存】")
stats_DANCE = stats.Statistics_order_split()

videoid_list = stats_DANCE.video_id_taglist("踊ってみた")
contributorid_list = stats_DANCE.contributor_id_taglist("踊ってみた")
title_list = stats_DANCE.title_taglist("踊ってみた")
view_list = stats_DANCE.view_taglist("踊ってみた")
comment_list = stats_DANCE.comment_taglist("踊ってみた")
mylist_list = stats_DANCE.mylist_taglist("踊ってみた")
total_list = stats_DANCE.total_taglist("踊ってみた")

db.db_insert(videoid_list, contributorid_list, title_list, view_list, comment_list, mylist_list, total_list, db_path, table_name)

print("【累計総合ポイント高い100人の投稿者の情報を全てDBに保存】")
db.db_best_100(db_path, table_name)