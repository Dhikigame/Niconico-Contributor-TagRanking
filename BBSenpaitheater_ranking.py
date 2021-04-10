# coding:utf-8
import sqlite3
import analysis.db as db
import analysis.stats as stats
import analysis.db_create as db_create
import os


# DB作成
db_path = "./analysis/db_ranking/BBSenpaitheater.db"
table_name = "BBSenpai_theater"
if os.path.exists(db_path) == True:
    os.remove(db_path)
db_create.db_create(db_path, table_name)

# タグ別のリストと動画総数のインスタンス生成 #
print("【キーワードに合致する動画を全てDBに保存】")
stats_BBSenpaitheater = stats.Statistics_order_split()

videoid_list = stats_BBSenpaitheater.video_id_taglist("BB先輩劇場")
contributorid_list = stats_BBSenpaitheater.contributor_id_taglist("BB先輩劇場")
title_list = stats_BBSenpaitheater.title_taglist("BB先輩劇場")
view_list = stats_BBSenpaitheater.view_taglist("BB先輩劇場")
comment_list = stats_BBSenpaitheater.comment_taglist("BB先輩劇場")
mylist_list = stats_BBSenpaitheater.mylist_taglist("BB先輩劇場")
total_list = stats_BBSenpaitheater.total_taglist("BB先輩劇場")

db.db_insert(videoid_list, contributorid_list, title_list, view_list, comment_list, mylist_list, total_list, db_path, table_name)

print("【累計総合ポイント高い100人の投稿者の情報を全てDBに保存】")
db.db_best_100(db_path, table_name)