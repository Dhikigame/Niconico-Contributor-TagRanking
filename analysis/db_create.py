# coding:utf-8
import sqlite3

def db_create(db_path, table_name):
    # キーワードに合致する動画情報を保存するテーブル作成
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    sql = 'create table ' + str(table_name) + '(video_id varchar(50) primary key, contributor_id integer, title varchar(200), regist_date date, upload_date date, view integer, comment integer, mylist integer, total integer)'
    cur.execute(sql)
    con.commit()
    con.close()

    # 累計総合ポイントの高い100位の投稿者のテーブル作成
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    sql = 'create table best100(contributor_id integer primary key, view integer, comment integer, mylist integer, total integer)'
    cur.execute(sql)
    con.commit()
    con.close()
    
    # 累計総合ポイントの高い100位の投稿者のキーワード合致の投稿動画テーブル作成
    for rank_num in range(1, 101):
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        sql = 'create table rank' + str(rank_num) + '(video_id varchar(50) primary key, contributor_id integer, title varchar(200), regist_date date, upload_date date, view integer, comment integer, mylist integer, total integer)'
        cur.execute(sql)
        con.commit()
        con.close()

# def db_best100_create():
#     con = sqlite3.connect('./analysis/db_ranking/MusicMAD.db')
#     cur = con.cursor()
    
#     sql = 'create table best100(contributor_id integer, view integer, comment integer, mylist integer, total integer)'
#     cur.execute(sql)

#     con.commit()
#     con.close()