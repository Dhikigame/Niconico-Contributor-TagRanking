# coding:utf-8
import sqlite3
import analysis.db as db
import analysis.stats as stats
import analysis.db_create as db_create
import os


# DB作成
db_path = "./analysis/db_ranking/RTA.db"
table_name = "RTA"
if os.path.exists(db_path) == True:
    os.remove(db_path)
db_create.db_create(db_path, table_name)

# タグ別のリストと動画総数のインスタンス生成 #
print("【キーワードに合致する動画を全てDBに保存】")
stats_RTA = stats.Statistics_order_split()

videoid_list = stats_RTA.video_id_taglist("RTA")
contributorid_list = stats_RTA.contributor_id_taglist("RTA")
registdate_list = stats_RTA.regist_date_taglist("RTA")
uploaddate_list = stats_RTA.upload_date_taglist("RTA")
title_list = stats_RTA.title_taglist("RTA")
view_list = stats_RTA.view_taglist("RTA")
comment_list = stats_RTA.comment_taglist("RTA")
mylist_list = stats_RTA.mylist_taglist("RTA")
total_list = stats_RTA.total_taglist("RTA")

db.db_insert(videoid_list, contributorid_list, registdate_list, uploaddate_list, title_list, view_list, comment_list, mylist_list, total_list, db_path, table_name)

print("【累計総合ポイント高い100人の投稿者の情報を全てDBに保存】")
db.db_best_100(db_path, table_name)