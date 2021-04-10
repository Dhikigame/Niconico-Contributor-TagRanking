# coding:utf-8
import sqlite3
import analysis.db as db
import analysis.stats as stats
import analysis.db_create as db_create
import os


# DB作成
db_path = "./analysis/db_ranking/MusicMAD.db"
table_name = "music_mad"
if os.path.exists(db_path) == True:
    os.remove(db_path)
db_create.db_create(db_path, table_name)

# タグ別のリストと動画総数のインスタンス生成 #
print("【キーワードに合致する動画を全てDBに保存】")
stats_MusicMAD = stats.Statistics_order_split()

videoid_list = stats_MusicMAD.video_id_taglist("音MAD")
contributorid_list = stats_MusicMAD.contributor_id_taglist("音MAD")
view_list = stats_MusicMAD.view_taglist("音MAD")
comment_list = stats_MusicMAD.comment_taglist("音MAD")
mylist_list = stats_MusicMAD.mylist_taglist("音MAD")
total_list = stats_MusicMAD.total_taglist("音MAD")

db.db_insert(videoid_list, contributorid_list, view_list, comment_list, mylist_list, total_list, db_path, table_name)

print("【累計総合ポイント高い100人の投稿者の情報を全てDBに保存】")
db.db_best_100(db_path, table_name)