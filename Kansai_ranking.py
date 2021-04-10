# coding:utf-8
import sqlite3
import analysis.db as db
import analysis.stats as stats
import analysis.db_create as db_create
import os


# DB作成
db_path = "./analysis/db_ranking/Kansai.db"
table_name = "kansai"
if os.path.exists(db_path) == True:
    os.remove(db_path)
db_create.db_create(db_path, table_name)

# タグ別のリストと動画総数のインスタンス生成 #
print("【キーワードに合致する動画を全てDBに保存】")
stats_Kansai = stats.Statistics_order_split()

videoid_list = stats_Kansai.video_id_taglist("関西クレーマー")
contributorid_list = stats_Kansai.contributor_id_taglist("関西クレーマー")
view_list = stats_Kansai.view_taglist("関西クレーマー")
comment_list = stats_Kansai.comment_taglist("関西クレーマー")
mylist_list = stats_Kansai.mylist_taglist("関西クレーマー")
total_list = stats_Kansai.total_taglist("関西クレーマー")

db.db_insert(videoid_list, contributorid_list, view_list, comment_list, mylist_list, total_list, db_path, table_name)

print("【累計総合ポイント高い100人の投稿者の情報を全てDBに保存】")
db.db_best_100(db_path, table_name)