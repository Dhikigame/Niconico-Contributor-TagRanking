# coding:utf-8
import sqlite3
import analysis.db as db
import analysis.stats as stats
import analysis.db_create as db_create
import os


# DB作成
db_path = "./analysis/db_ranking/Kankore.db"
table_name = "kankore"
if os.path.exists(db_path) == True:
    os.remove(db_path)
db_create.db_create(db_path, table_name)

# タグ別のリストと動画総数のインスタンス生成 #
print("【キーワードに合致する動画を全てDBに保存】")
stats_Kankore = stats.Statistics_order_split()

videoid_list = stats_Kankore.video_id_taglist("艦これ")
contributorid_list = stats_Kankore.contributor_id_taglist("艦これ")
title_list = stats_Kankore.title_taglist("艦これ")
view_list = stats_Kankore.view_taglist("艦これ")
comment_list = stats_Kankore.comment_taglist("艦これ")
mylist_list = stats_Kankore.mylist_taglist("艦これ")
total_list = stats_Kankore.total_taglist("艦これ")

db.db_insert(videoid_list, contributorid_list, title_list, view_list, comment_list, mylist_list, total_list, db_path, table_name)

print("【累計総合ポイント高い100人の投稿者の情報を全てDBに保存】")
db.db_best_100(db_path, table_name)