# coding:utf-8
import sqlite3
import analysis.db as db
import analysis.stats as stats
import analysis.db_Inm as db_Inm
import os


# DB作成
db_path = "./analysis/db_ranking/Inm.db"
table_name = "inm"
if os.path.exists(db_path) == True:
    os.remove(db_path)
db_Inm.db_create()

# タグ別のリストと動画総数のインスタンス生成 #
stats_Inm = stats.Statistics_order_split()

videoid_list = stats_Inm.video_id_taglist("真夏の夜の淫夢")
contributorid_list = stats_Inm.contributor_id_taglist("真夏の夜の淫夢")
view_list = stats_Inm.view_taglist("真夏の夜の淫夢")
comment_list = stats_Inm.comment_taglist("真夏の夜の淫夢")
mylist_list = stats_Inm.mylist_taglist("真夏の夜の淫夢")
total_list = stats_Inm.total_taglist("真夏の夜の淫夢")

db.db_insert(videoid_list, contributorid_list, view_list, comment_list, mylist_list, total_list, db_path, table_name)