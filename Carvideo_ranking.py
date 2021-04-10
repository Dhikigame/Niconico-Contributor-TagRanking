# coding:utf-8
import sqlite3
import analysis.db as db
import analysis.stats as stats
import analysis.db_create as db_create
import os


# DB作成
db_path = "./analysis/db_ranking/Carvideo.db"
table_name = "Carvideo"
if os.path.exists(db_path) == True:
    os.remove(db_path)
db_create.db_create(db_path, table_name)

# タグ別のリストと動画総数のインスタンス生成 #
print("【キーワードに合致する動画を全てDBに保存】")
stats_carvideo = stats.Statistics_order_split()

videoid_list = stats_carvideo.video_id_taglist("車載動画")
contributorid_list = stats_carvideo.contributor_id_taglist("車載動画")
title_list = stats_carvideo.title_taglist("車載動画")
view_list = stats_carvideo.view_taglist("車載動画")
comment_list = stats_carvideo.comment_taglist("車載動画")
mylist_list = stats_carvideo.mylist_taglist("車載動画")
total_list = stats_carvideo.total_taglist("車載動画")

db.db_insert(videoid_list, contributorid_list, title_list, view_list, comment_list, mylist_list, total_list, db_path, table_name)

print("【累計総合ポイント高い100人の投稿者の情報を全てDBに保存】")
db.db_best_100(db_path, table_name)