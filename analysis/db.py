# coding:utf-8
import sqlite3
from contextlib import closing
import analysis.video_found_check as video_found_check


class DB_order_split:
    def __init__(self):
        # videodata01
        self.db01 = sqlite3.connect('./analysis/videodata_split/videodata01.db')
        self.cur01 = self.db01.cursor()
        # videodata12
        self.db12 = sqlite3.connect('./analysis/videodata_split/videodata12.db')
        self.cur12 = self.db12.cursor()
        # videodata23
        self.db23 = sqlite3.connect('./analysis/videodata_split/videodata23.db')
        self.cur23 = self.db23.cursor()
        # videodata34
        self.db34 = sqlite3.connect('./analysis/videodata_split/videodata34.db')
        self.cur34 = self.db34.cursor()

    # カテゴリタグに関連した動画の各項目を取得
    def tag_videoid_list_sql(self, tag):
        sql = tag_sql_sentance(tag, "video_id")
        videoid_list = list()
        # videodata01
        self.cur01.execute(sql)
        for video_id in self.cur01.fetchall():
            video_id = str(video_id)[2:-3]
            videoid_list.append(str(video_id))
        # videodata12
        self.cur12.execute(sql)
        for video_id in self.cur12.fetchall():
            video_id = str(video_id)[2:-3]
            videoid_list.append(str(video_id))
        # videodata23
        self.cur23.execute(sql)
        for video_id in self.cur23.fetchall():
            video_id = str(video_id)[2:-3]
            videoid_list.append(str(video_id))
        # videodata34
        self.cur34.execute(sql)
        for video_id in self.cur34.fetchall():
            video_id = str(video_id)[2:-3]
            videoid_list.append(str(video_id))
        
        return videoid_list

    # カテゴリタグに関連した動画の各項目を取得
    def tag_contributorid_list_sql(self, tag):
        sql = tag_sql_sentance(tag, "contributor_id")
        contributorid_list = list()
        # videodata01
        self.cur01.execute(sql)
        for contributor_id in self.cur01.fetchall():
            contributor_id = str(contributor_id)[1:-2]
            if contributor_id == "None":
                contributor_id = 0
            contributorid_list.append(str(contributor_id))
        # videodata12
        self.cur12.execute(sql)
        for contributor_id in self.cur12.fetchall():
            contributor_id = str(contributor_id)[1:-2]
            if contributor_id == "None":
                contributor_id = 0
            contributorid_list.append(str(contributor_id))
        # videodata23
        self.cur23.execute(sql)
        for contributor_id in self.cur23.fetchall():
            contributor_id = str(contributor_id)[1:-2]
            if contributor_id == "None":
                contributor_id = 0
            contributorid_list.append(str(contributor_id))
        # videodata34
        self.cur34.execute(sql)
        for contributor_id in self.cur34.fetchall():
            contributor_id = str(contributor_id)[1:-2]
            if contributor_id == "None":
                contributor_id = 0
            contributorid_list.append(str(contributor_id))
        
        return contributorid_list

    # カテゴリタグに関連した動画の各項目を取得
    def tag_registdate_list_sql(self, tag):
        sql = tag_sql_sentance(tag, "regist_date")
        registdate_list = list()
        # videodata01
        self.cur01.execute(sql)
        for regist_date in self.cur01.fetchall():
            regist_date = str(regist_date)[1:-2]
            registdate_list.append(str(regist_date))
        # videodata12
        self.cur12.execute(sql)
        for regist_date in self.cur12.fetchall():
            regist_date = str(regist_date)[1:-2]
            registdate_list.append(str(regist_date))
        # videodata23
        self.cur23.execute(sql)
        for regist_date in self.cur23.fetchall():
            regist_date = str(regist_date)[1:-2]
            registdate_list.append(str(regist_date))
        # videodata34
        self.cur34.execute(sql)
        for regist_date in self.cur34.fetchall():
            regist_date = str(regist_date)[1:-2]
            registdate_list.append(str(regist_date))
        
        return registdate_list

    # カテゴリタグに関連した動画の各項目を取得
    def tag_uploaddate_list_sql(self, tag):
        sql = tag_sql_sentance(tag, "upload_date")
        uploaddate_list = list()
        # videodata01
        self.cur01.execute(sql)
        for upload_date in self.cur01.fetchall():
            upload_date = str(upload_date)[1:-2]
            uploaddate_list.append(str(upload_date))
        # videodata12
        self.cur12.execute(sql)
        for upload_date in self.cur12.fetchall():
            upload_date = str(upload_date)[1:-2]
            uploaddate_list.append(str(upload_date))
        # videodata23
        self.cur23.execute(sql)
        for upload_date in self.cur23.fetchall():
            upload_date = str(upload_date)[1:-2]
            uploaddate_list.append(str(upload_date))
        # videodata34
        self.cur34.execute(sql)
        for upload_date in self.cur34.fetchall():
            upload_date = str(upload_date)[1:-2]
            uploaddate_list.append(str(upload_date))
        
        return uploaddate_list

    # カテゴリタグに関連した動画の各項目を取得
    def tag_title_list_sql(self, tag):
        sql = tag_sql_sentance(tag, "title")
        title_list = list()
        # videodata01
        self.cur01.execute(sql)
        for title in self.cur01.fetchall():
            title = str(title)[1:-2]
            if title == "None":
                title = 0
            title_list.append(str(title))
        # videodata12
        self.cur12.execute(sql)
        for title in self.cur12.fetchall():
            title = str(title)[1:-2]
            if title == "None":
                title = 0
            title_list.append(str(title))
        # videodata23
        self.cur23.execute(sql)
        for title in self.cur23.fetchall():
            title = str(title)[1:-2]
            if title == "None":
                title = 0
            title_list.append(str(title))
        # videodata34
        self.cur34.execute(sql)
        for title in self.cur34.fetchall():
            title = str(title)[1:-2]
            if title == "None":
                title = 0
            title_list.append(str(title))
        
        return title_list

    # カテゴリタグに関連した動画の各項目を取得
    def tag_viewlist_sql(self, tag):
        sql = tag_sql_sentance(tag, "view")
        view_list = list()
        # videodata01
        self.cur01.execute(sql)
        for view in self.cur01.fetchall():
            view = str(view)[1:-2]
            if view == "None":
                view = 0
            view_list.append(str(view))
        # videodata12
        self.cur12.execute(sql)
        for view in self.cur12.fetchall():
            view = str(view)[1:-2]
            if view == "None":
                view = 0
            view_list.append(str(view))
        # videodata23
        self.cur23.execute(sql)
        for view in self.cur23.fetchall():
            view = str(view)[1:-2]
            if view == "None":
                view = 0
            view_list.append(str(view))
        # videodata34
        self.cur34.execute(sql)
        for view in self.cur34.fetchall():
            view = str(view)[1:-2]
            if view == "None":
                view = 0
            view_list.append(str(view))

        return view_list

    def tag_commentlist_sql(self, tag):
        sql = tag_sql_sentance(tag, "comment")
        comment_list = list()
        # videodata01
        self.cur01.execute(sql)
        for comment in self.cur01.fetchall():
            comment = str(comment)[1:-2]
            if comment == "None":
                comment = 0
            comment_list.append(str(comment))
        # videodata12
        self.cur12.execute(sql)
        for comment in self.cur12.fetchall():
            comment = str(comment)[1:-2]
            if comment == "None":
                comment = 0
            comment_list.append(str(comment))
        # videodata23
        self.cur23.execute(sql)
        for comment in self.cur23.fetchall():
            comment = str(comment)[1:-2]
            if comment == "None":
                comment = 0
            comment_list.append(str(comment))
        # videodata34
        self.cur34.execute(sql)
        for comment in self.cur34.fetchall():
            comment = str(comment)[1:-2]
            if comment == "None":
                comment = 0
            comment_list.append(str(comment))

        return comment_list

    def tag_mylistlist_sql(self, tag):
        sql = tag_sql_sentance(tag, "mylist")
        mylist_list = list()
        # videodata01
        self.cur01.execute(sql)
        for mylist in self.cur01.fetchall():
            mylist = str(mylist)[1:-2]
            if mylist == "None":
                mylist = 0
            mylist_list.append(str(mylist))
        # videodata12
        self.cur12.execute(sql)
        for mylist in self.cur12.fetchall():
            mylist = str(mylist)[1:-2]
            if mylist == "None":
                mylist = 0
            mylist_list.append(str(mylist))
        # videodata23
        self.cur23.execute(sql)
        for mylist in self.cur23.fetchall():
            mylist = str(mylist)[1:-2]
            if mylist == "None":
                mylist = 0
            mylist_list.append(str(mylist))
        # videodata34
        self.cur34.execute(sql)
        for mylist in self.cur34.fetchall():
            mylist = str(mylist)[1:-2]
            if mylist == "None":
                mylist = 0
            mylist_list.append(str(mylist))

        return mylist_list
    
    def tag_totallist_sql(self, tag):
        sql = tag_sql_sentance(tag, "total")
        total_list = list()
        # videodata01
        self.cur01.execute(sql)
        for total in self.cur01.fetchall():
            total = str(total)[1:-2]
            if total == "None":
                total = 0
            total_list.append(str(total))
        # videodata12
        self.cur12.execute(sql)
        for total in self.cur12.fetchall():
            total = str(total)[1:-2]
            if total == "None":
                total = 0
            total_list.append(str(total))
        # videodata23
        self.cur23.execute(sql)
        for total in self.cur23.fetchall():
            total = str(total)[1:-2]
            if total == "None":
                total = 0
            total_list.append(str(total))
        # videodata34
        self.cur34.execute(sql)
        for total in self.cur34.fetchall():
            total = str(total)[1:-2]
            if total == "None":
                total = 0
            total_list.append(str(total))

        return total_list


def tag_sql_sentance(tag, select):

    if tag == "音MAD":
        sql = 'SELECT ' + str(select) + ' FROM video_data WHERE tag1 LIKE "%' + str(tag) + '%" OR tag2 LIKE "%' + str(tag) + '%" OR tag3 LIKE "%' + str(tag) + '%" OR tag4 LIKE "%' + str(tag) + '%" OR tag5 LIKE "%' + str(tag) + '%" OR tag6 LIKE "%' + str(tag) + '%" OR tag7 LIKE "%' + str(tag) + '%" OR tag8 LIKE "%' + str(tag) + '%" OR tag9 LIKE "%' + str(tag) + '%" OR tag10 LIKE "%' + str(tag) + '%" OR tag11 LIKE "%' + str(tag) + '%" OR title LIKE "%' + str(tag) + '%" OR '
        
        tag = "音mad"
        sql += 'tag1 LIKE "%' + str(tag) + '%" OR tag2 LIKE "%' + str(tag) + '%" OR tag3 LIKE "%' + str(tag) + '%" OR tag4 LIKE "%' + str(tag) + '%" OR tag5 LIKE "%' + str(tag) + '%" OR tag6 LIKE "%' + str(tag) + '%" OR tag7 LIKE "%' + str(tag) + '%" OR tag8 LIKE "%' + str(tag) + '%" OR tag9 LIKE "%' + str(tag) + '%" OR tag10 LIKE "%' + str(tag) + '%" OR tag11 LIKE "%' + str(tag) + '%" OR title LIKE "%' + str(tag) + '%" OR '

        tag = "音Mad"
        sql += 'tag1 LIKE "%' + str(tag) + '%" OR tag2 LIKE "%' + str(tag) + '%" OR tag3 LIKE "%' + str(tag) + '%" OR tag4 LIKE "%' + str(tag) + '%" OR tag5 LIKE "%' + str(tag) + '%" OR tag6 LIKE "%' + str(tag) + '%" OR tag7 LIKE "%' + str(tag) + '%" OR tag8 LIKE "%' + str(tag) + '%" OR tag9 LIKE "%' + str(tag) + '%" OR tag10 LIKE "%' + str(tag) + '%" OR tag11 LIKE "%' + str(tag) + '%" OR title LIKE "%' + str(tag) + '%"'
        return sql

    if tag == "VOICEROID劇場":
        sql = 'SELECT ' + str(select) + ' FROM video_data WHERE tag1 LIKE "%' + str(tag) + '%" OR tag2 LIKE "%' + str(tag) + '%" OR tag3 LIKE "%' + str(tag) + '%" OR tag4 LIKE "%' + str(tag) + '%" OR tag5 LIKE "%' + str(tag) + '%" OR tag6 LIKE "%' + str(tag) + '%" OR tag7 LIKE "%' + str(tag) + '%" OR tag8 LIKE "%' + str(tag) + '%" OR tag9 LIKE "%' + str(tag) + '%" OR tag10 LIKE "%' + str(tag) + '%" OR tag11 LIKE "%' + str(tag) + '%" OR title LIKE "%' + str(tag) + '%" OR '
        
        tag = "voiceroid劇場"
        sql += 'tag1 LIKE "%' + str(tag) + '%" OR tag2 LIKE "%' + str(tag) + '%" OR tag3 LIKE "%' + str(tag) + '%" OR tag4 LIKE "%' + str(tag) + '%" OR tag5 LIKE "%' + str(tag) + '%" OR tag6 LIKE "%' + str(tag) + '%" OR tag7 LIKE "%' + str(tag) + '%" OR tag8 LIKE "%' + str(tag) + '%" OR tag9 LIKE "%' + str(tag) + '%" OR tag10 LIKE "%' + str(tag) + '%" OR tag11 LIKE "%' + str(tag) + '%" OR title LIKE "%' + str(tag) + '%" OR '

        tag = "VOICELOID劇場"
        sql += 'tag1 LIKE "%' + str(tag) + '%" OR tag2 LIKE "%' + str(tag) + '%" OR tag3 LIKE "%' + str(tag) + '%" OR tag4 LIKE "%' + str(tag) + '%" OR tag5 LIKE "%' + str(tag) + '%" OR tag6 LIKE "%' + str(tag) + '%" OR tag7 LIKE "%' + str(tag) + '%" OR tag8 LIKE "%' + str(tag) + '%" OR tag9 LIKE "%' + str(tag) + '%" OR tag10 LIKE "%' + str(tag) + '%" OR tag11 LIKE "%' + str(tag) + '%" OR title LIKE "%' + str(tag) + '%" OR '
        
        tag = "voiceloid劇場"
        sql += 'tag1 LIKE "%' + str(tag) + '%" OR tag2 LIKE "%' + str(tag) + '%" OR tag3 LIKE "%' + str(tag) + '%" OR tag4 LIKE "%' + str(tag) + '%" OR tag5 LIKE "%' + str(tag) + '%" OR tag6 LIKE "%' + str(tag) + '%" OR tag7 LIKE "%' + str(tag) + '%" OR tag8 LIKE "%' + str(tag) + '%" OR tag9 LIKE "%' + str(tag) + '%" OR tag10 LIKE "%' + str(tag) + '%" OR tag11 LIKE "%' + str(tag) + '%" OR title LIKE "%' + str(tag) + '%" OR '

        tag = "ＶＯＩＣＥＲＯＩＤ劇場"
        sql += 'tag1 LIKE "%' + str(tag) + '%" OR tag2 LIKE "%' + str(tag) + '%" OR tag3 LIKE "%' + str(tag) + '%" OR tag4 LIKE "%' + str(tag) + '%" OR tag5 LIKE "%' + str(tag) + '%" OR tag6 LIKE "%' + str(tag) + '%" OR tag7 LIKE "%' + str(tag) + '%" OR tag8 LIKE "%' + str(tag) + '%" OR tag9 LIKE "%' + str(tag) + '%" OR tag10 LIKE "%' + str(tag) + '%" OR tag11 LIKE "%' + str(tag) + '%" OR title LIKE "%' + str(tag) + '%" OR '

        tag = "ボイスロイド劇場"
        sql += 'tag1 LIKE "%' + str(tag) + '%" OR tag2 LIKE "%' + str(tag) + '%" OR tag3 LIKE "%' + str(tag) + '%" OR tag4 LIKE "%' + str(tag) + '%" OR tag5 LIKE "%' + str(tag) + '%" OR tag6 LIKE "%' + str(tag) + '%" OR tag7 LIKE "%' + str(tag) + '%" OR tag8 LIKE "%' + str(tag) + '%" OR tag9 LIKE "%' + str(tag) + '%" OR tag10 LIKE "%' + str(tag) + '%" OR tag11 LIKE "%' + str(tag) + '%" OR title LIKE "%' + str(tag) + '%" OR '

        # tag = "VOICEROID遊劇場"
        # sql += 'tag1 LIKE "%' + str(tag) + '%" OR tag2 LIKE "%' + str(tag) + '%" OR tag3 LIKE "%' + str(tag) + '%" OR tag4 LIKE "%' + str(tag) + '%" OR tag5 LIKE "%' + str(tag) + '%" OR tag6 LIKE "%' + str(tag) + '%" OR tag7 LIKE "%' + str(tag) + '%" OR tag8 LIKE "%' + str(tag) + '%" OR tag9 LIKE "%' + str(tag) + '%" OR tag10 LIKE "%' + str(tag) + '%" OR tag11 LIKE "%' + str(tag) + '%" OR title LIKE "%' + str(tag) + '%" OR '

        tag = "ボイロ劇場"
        sql += 'tag1 LIKE "%' + str(tag) + '%" OR tag2 LIKE "%' + str(tag) + '%" OR tag3 LIKE "%' + str(tag) + '%" OR tag4 LIKE "%' + str(tag) + '%" OR tag5 LIKE "%' + str(tag) + '%" OR tag6 LIKE "%' + str(tag) + '%" OR tag7 LIKE "%' + str(tag) + '%" OR tag8 LIKE "%' + str(tag) + '%" OR tag9 LIKE "%' + str(tag) + '%" OR tag10 LIKE "%' + str(tag) + '%" OR tag11 LIKE "%' + str(tag) + '%" OR title LIKE "%' + str(tag) + '%"'
        return sql

    if tag == "BB先輩劇場":
        sql = 'SELECT ' + str(select) + ' FROM video_data WHERE tag1 LIKE "%' + str(tag) + '%" OR tag2 LIKE "%' + str(tag) + '%" OR tag3 LIKE "%' + str(tag) + '%" OR tag4 LIKE "%' + str(tag) + '%" OR tag5 LIKE "%' + str(tag) + '%" OR tag6 LIKE "%' + str(tag) + '%" OR tag7 LIKE "%' + str(tag) + '%" OR tag8 LIKE "%' + str(tag) + '%" OR tag9 LIKE "%' + str(tag) + '%" OR tag10 LIKE "%' + str(tag) + '%" OR tag11 LIKE "%' + str(tag) + '%" OR title LIKE "%' + str(tag) + '%" OR '
        
        tag = "bb先輩劇場"
        sql += 'tag1 LIKE "%' + str(tag) + '%" OR tag2 LIKE "%' + str(tag) + '%" OR tag3 LIKE "%' + str(tag) + '%" OR tag4 LIKE "%' + str(tag) + '%" OR tag5 LIKE "%' + str(tag) + '%" OR tag6 LIKE "%' + str(tag) + '%" OR tag7 LIKE "%' + str(tag) + '%" OR tag8 LIKE "%' + str(tag) + '%" OR tag9 LIKE "%' + str(tag) + '%" OR tag10 LIKE "%' + str(tag) + '%" OR tag11 LIKE "%' + str(tag) + '%" OR title LIKE "%' + str(tag) + '%" OR '

        tag = "ＢＢ先輩劇場"
        sql += 'tag1 LIKE "%' + str(tag) + '%" OR tag2 LIKE "%' + str(tag) + '%" OR tag3 LIKE "%' + str(tag) + '%" OR tag4 LIKE "%' + str(tag) + '%" OR tag5 LIKE "%' + str(tag) + '%" OR tag6 LIKE "%' + str(tag) + '%" OR tag7 LIKE "%' + str(tag) + '%" OR tag8 LIKE "%' + str(tag) + '%" OR tag9 LIKE "%' + str(tag) + '%" OR tag10 LIKE "%' + str(tag) + '%" OR tag11 LIKE "%' + str(tag) + '%" OR title LIKE "%' + str(tag) + '%"'        
        return sql

    if tag == "艦これ":
        sql = 'SELECT ' + str(select) + ' FROM video_data WHERE tag1 LIKE "%' + str(tag) + '%" OR tag2 LIKE "%' + str(tag) + '%" OR tag3 LIKE "%' + str(tag) + '%" OR tag4 LIKE "%' + str(tag) + '%" OR tag5 LIKE "%' + str(tag) + '%" OR tag6 LIKE "%' + str(tag) + '%" OR tag7 LIKE "%' + str(tag) + '%" OR tag8 LIKE "%' + str(tag) + '%" OR tag9 LIKE "%' + str(tag) + '%" OR tag10 LIKE "%' + str(tag) + '%" OR tag11 LIKE "%' + str(tag) + '%" OR title LIKE "%' + str(tag) + '%" OR '
        
        tag = "艦隊これくしょん"
        sql += 'tag1 LIKE "%' + str(tag) + '%" OR tag2 LIKE "%' + str(tag) + '%" OR tag3 LIKE "%' + str(tag) + '%" OR tag4 LIKE "%' + str(tag) + '%" OR tag5 LIKE "%' + str(tag) + '%" OR tag6 LIKE "%' + str(tag) + '%" OR tag7 LIKE "%' + str(tag) + '%" OR tag8 LIKE "%' + str(tag) + '%" OR tag9 LIKE "%' + str(tag) + '%" OR tag10 LIKE "%' + str(tag) + '%" OR tag11 LIKE "%' + str(tag) + '%" OR title LIKE "%' + str(tag) + '%" OR '

        tag = "艦隊これくしょん -艦これ-"
        sql += 'tag1 LIKE "%' + str(tag) + '%" OR tag2 LIKE "%' + str(tag) + '%" OR tag3 LIKE "%' + str(tag) + '%" OR tag4 LIKE "%' + str(tag) + '%" OR tag5 LIKE "%' + str(tag) + '%" OR tag6 LIKE "%' + str(tag) + '%" OR tag7 LIKE "%' + str(tag) + '%" OR tag8 LIKE "%' + str(tag) + '%" OR tag9 LIKE "%' + str(tag) + '%" OR tag10 LIKE "%' + str(tag) + '%" OR tag11 LIKE "%' + str(tag) + '%" OR title LIKE "%' + str(tag) + '%"'        
        return sql

    if tag == "車載動画":
        sql = 'SELECT ' + str(select) + ' FROM video_data WHERE tag1 LIKE "%' + str(tag) + '%" OR tag2 LIKE "%' + str(tag) + '%" OR tag3 LIKE "%' + str(tag) + '%" OR tag4 LIKE "%' + str(tag) + '%" OR tag5 LIKE "%' + str(tag) + '%" OR tag6 LIKE "%' + str(tag) + '%" OR tag7 LIKE "%' + str(tag) + '%" OR tag8 LIKE "%' + str(tag) + '%" OR tag9 LIKE "%' + str(tag) + '%" OR tag10 LIKE "%' + str(tag) + '%" OR tag11 LIKE "%' + str(tag) + '%" OR title LIKE "%' + str(tag) + '%" OR '

        tag = "車載"
        sql += 'tag1 LIKE "%' + str(tag) + '%" OR tag2 LIKE "%' + str(tag) + '%" OR tag3 LIKE "%' + str(tag) + '%" OR tag4 LIKE "%' + str(tag) + '%" OR tag5 LIKE "%' + str(tag) + '%" OR tag6 LIKE "%' + str(tag) + '%" OR tag7 LIKE "%' + str(tag) + '%" OR tag8 LIKE "%' + str(tag) + '%" OR tag9 LIKE "%' + str(tag) + '%" OR tag10 LIKE "%' + str(tag) + '%" OR tag11 LIKE "%' + str(tag) + '%" OR title LIKE "%' + str(tag) + '%"'        
        return sql

    if tag == "RTA":
        sql = 'SELECT ' + str(select) + ' FROM video_data WHERE tag1 = "' + str(tag) + '" OR tag2 = "' + str(tag) + '" OR tag3 = "' + str(tag) + '" OR tag4 = "' + str(tag) + '" OR tag5 = "' + str(tag) + '" OR tag6 = "' + str(tag) + '" OR tag7 = "' + str(tag) + '" OR tag8 = "' + str(tag) + '" OR tag9 = "' + str(tag) + '" OR tag10 = "' + str(tag) + '" OR tag11 = "' + str(tag) + '" OR '

        tag = "ＲＴＡ"
        sql += 'tag1 = "' + str(tag) + '" OR tag2 = "' + str(tag) + '" OR tag3 = "' + str(tag) + '" OR tag4 = "' + str(tag) + '" OR tag5 = "' + str(tag) + '" OR tag6 = "' + str(tag) + '" OR tag7 = "' + str(tag) + '" OR tag8 = "' + str(tag) + '" OR tag9 = "' + str(tag) + '" OR tag10 = "' + str(tag) + '" OR tag11 = "' + str(tag) + '" OR '

        tag = "Rta"
        sql += 'tag1 = "' + str(tag) + '" OR tag2 = "' + str(tag) + '" OR tag3 = "' + str(tag) + '" OR tag4 = "' + str(tag) + '" OR tag5 = "' + str(tag) + '" OR tag6 = "' + str(tag) + '" OR tag7 = "' + str(tag) + '" OR tag8 = "' + str(tag) + '" OR tag9 = "' + str(tag) + '" OR tag10 = "' + str(tag) + '" OR tag11 = "' + str(tag) + '" OR '        

        tag = "rta"
        sql += 'tag1 = "' + str(tag) + '" OR tag2 = "' + str(tag) + '" OR tag3 = "' + str(tag) + '" OR tag4 = "' + str(tag) + '" OR tag5 = "' + str(tag) + '" OR tag6 = "' + str(tag) + '" OR tag7 = "' + str(tag) + '" OR tag8 = "' + str(tag) + '" OR tag9 = "' + str(tag) + '" OR tag10 = "' + str(tag) + '" OR tag11 = "' + str(tag) + '" OR '

        tag = "RTA（リアル登山アタック）"
        sql += 'tag1 = "' + str(tag) + '" OR tag2 = "' + str(tag) + '" OR tag3 = "' + str(tag) + '" OR tag4 = "' + str(tag) + '" OR tag5 = "' + str(tag) + '" OR tag6 = "' + str(tag) + '" OR tag7 = "' + str(tag) + '" OR tag8 = "' + str(tag) + '" OR tag9 = "' + str(tag) + '" OR tag10 = "' + str(tag) + '" OR tag11 = "' + str(tag) + '" OR '

        tag = "初見RTA"
        sql += 'tag1 = "' + str(tag) + '" OR tag2 = "' + str(tag) + '" OR tag3 = "' + str(tag) + '" OR tag4 = "' + str(tag) + '" OR tag5 = "' + str(tag) + '" OR tag6 = "' + str(tag) + '" OR tag7 = "' + str(tag) + '" OR tag8 = "' + str(tag) + '" OR tag9 = "' + str(tag) + '" OR tag10 = "' + str(tag) + '" OR tag11 = "' + str(tag) + '" OR '

        tag = "RTA芸人"
        sql += 'tag1 = "' + str(tag) + '" OR tag2 = "' + str(tag) + '" OR tag3 = "' + str(tag) + '" OR tag4 = "' + str(tag) + '" OR tag5 = "' + str(tag) + '" OR tag6 = "' + str(tag) + '" OR tag7 = "' + str(tag) + '" OR tag8 = "' + str(tag) + '" OR tag9 = "' + str(tag) + '" OR tag10 = "' + str(tag) + '" OR tag11 = "' + str(tag) + '" OR '

        tag = "料理RTA"
        sql += 'tag1 = "' + str(tag) + '" OR tag2 = "' + str(tag) + '" OR tag3 = "' + str(tag) + '" OR tag4 = "' + str(tag) + '" OR tag5 = "' + str(tag) + '" OR tag6 = "' + str(tag) + '" OR tag7 = "' + str(tag) + '" OR tag8 = "' + str(tag) + '" OR tag9 = "' + str(tag) + '" OR tag10 = "' + str(tag) + '" OR tag11 = "' + str(tag) + '" OR '

        tag = "料理rta"
        sql += 'tag1 = "' + str(tag) + '" OR tag2 = "' + str(tag) + '" OR tag3 = "' + str(tag) + '" OR tag4 = "' + str(tag) + '" OR tag5 = "' + str(tag) + '" OR tag6 = "' + str(tag) + '" OR tag7 = "' + str(tag) + '" OR tag8 = "' + str(tag) + '" OR tag9 = "' + str(tag) + '" OR tag10 = "' + str(tag) + '" OR tag11 = "' + str(tag) + '" OR '
 
        tag = "エロゲRTA"
        sql += 'tag1 = "' + str(tag) + '" OR tag2 = "' + str(tag) + '" OR tag3 = "' + str(tag) + '" OR tag4 = "' + str(tag) + '" OR tag5 = "' + str(tag) + '" OR tag6 = "' + str(tag) + '" OR tag7 = "' + str(tag) + '" OR tag8 = "' + str(tag) + '" OR tag9 = "' + str(tag) + '" OR tag10 = "' + str(tag) + '" OR tag11 = "' + str(tag) + '" OR '

        tag = "Speedrun"
        sql += 'tag1 = "' + str(tag) + '" OR tag2 = "' + str(tag) + '" OR tag3 = "' + str(tag) + '" OR tag4 = "' + str(tag) + '" OR tag5 = "' + str(tag) + '" OR tag6 = "' + str(tag) + '" OR tag7 = "' + str(tag) + '" OR tag8 = "' + str(tag) + '" OR tag9 = "' + str(tag) + '" OR tag10 = "' + str(tag) + '" OR tag11 = "' + str(tag) + '" OR '        

        tag = "speedrun"
        sql += 'tag1 = "' + str(tag) + '" OR tag2 = "' + str(tag) + '" OR tag3 = "' + str(tag) + '" OR tag4 = "' + str(tag) + '" OR tag5 = "' + str(tag) + '" OR tag6 = "' + str(tag) + '" OR tag7 = "' + str(tag) + '" OR tag8 = "' + str(tag) + '" OR tag9 = "' + str(tag) + '" OR tag10 = "' + str(tag) + '" OR tag11 = "' + str(tag) + '"'        
        return sql

    sql = 'SELECT ' + str(select) + ' FROM video_data WHERE tag1 LIKE "%' + str(tag) + '%" OR tag2 LIKE "%' + str(tag) + '%" OR tag3 LIKE "%' + str(tag) + '%" OR tag4 LIKE "%' + str(tag) + '%" OR tag5 LIKE "%' + str(tag) + '%" OR tag6 LIKE "%' + str(tag) + '%" OR tag7 LIKE "%' + str(tag) + '%" OR tag8 LIKE "%' + str(tag) + '%" OR tag9 LIKE "%' + str(tag) + '%" OR tag10 LIKE "%' + str(tag) + '%" OR tag11 LIKE "%' + str(tag) + '%" OR title LIKE "%' + str(tag) + '%"'
    return sql

def db_insert(videoid_list, contributorid_list, registdate_list, uploaddate_list, title_list, view_list, comment_list, mylist_list, total_list, db_path, table_name):

    db = sqlite3.connect(db_path)

    print("動画ID")
    print(len(videoid_list))
    print("投稿者ID")
    print(len(contributorid_list))
    print("データ取得日時")
    print(len(registdate_list))
    print("投稿日時")
    print(len(uploaddate_list))
    print("タイトル")
    print(len(title_list))
    print("再生")
    print(len(view_list))
    print("コメント")
    print(len(comment_list))
    print("マイリスト")
    print(len(mylist_list))
    print("合計")
    print(len(total_list))

    with closing(db) as con:
        c = con.cursor()
        cursor = db.cursor()
        for i in range(0, len(videoid_list)):

            video_check_result = video_found_check.video_found_check(videoid_list[i])
            print(str(i) + " " + video_check_result)
            if video_check_result == "found":
                # sql = 'insert into ' + str(table_name) + '(video_id, contributor_id, title, upload_date, view, comment, mylist, total) '
                # sql += 'values ("' + str(videoid_list[i]) + '",' + str(contributorid_list[i]) + ',"' + str(title_list[i]) + '","' str(uploaddate_list[i]) + '",' + str(view_list[i]) + ',' + str(comment_list[i]) + ',' + str(mylist_list[i]) + ',' + str(total_list[i]) + ')'
                sql = 'insert into ' + str(table_name) + '(video_id, contributor_id, title, regist_date, upload_date, view, comment, mylist, total) '
                sql += 'values ("' + str(videoid_list[i]) + '",' + str(contributorid_list[i]) + ',"' + str(title_list[i]) + '","' + str(registdate_list[i]) + '","' + str(uploaddate_list[i]) + '",' + str(view_list[i]) + ',' + str(comment_list[i]) + ',' + str(mylist_list[i]) + ',' + str(total_list[i]) + ')'

                cursor.execute(sql)
                con.commit()
            else:
                continue
        con.close()


def db_best_100(db_path, table_name):

    best_100_contributor_list = list()
    best_100_title_list = list()
    best_100_total_list = list()
    best_100_view_list = list()
    best_100_comment_list = list()
    best_100_mylist_list = list()

    db = sqlite3.connect(db_path)
    cur = db.cursor()
    sql = "SELECT contributor_id, SUM(total), SUM(view), SUM(comment), SUM(mylist) FROM " + str(table_name) + " GROUP BY contributor_id ORDER BY SUM(total) DESC limit 100"
    cur.execute(sql)
    
    print("投稿者ID " + " 累計総合ポイント " + " 累計再生数 " + " 累計コメント数 " + " 累計マイリスト数 ")
    contributor_count = 0
    for row in cur:
        best_100_contributor_list.append(str(row[0]))
        best_100_total_list.append(str(row[1]))
        best_100_view_list.append(str(row[2]))
        best_100_comment_list.append(str(row[3]))
        best_100_mylist_list.append(str(row[4]))
        print(row[0], row[1], row[2], row[3], row[4])
        contributor_count = contributor_count + 1
    db.close()

    db = sqlite3.connect(db_path)
    with closing(db) as con:
        cursor = db.cursor()
        for i in range(0, contributor_count):
            sql = 'insert into best100(contributor_id, view, comment, mylist, total) '
            sql += 'values (' + str(best_100_contributor_list[i]) + ',' + str(best_100_view_list[i]) + ',' + str(best_100_comment_list[i]) + ',' + str(best_100_mylist_list[i]) + ',' + str(best_100_total_list[i]) + ')'
            print("rank_insert:" + str(i))
            cursor.execute(sql)
            con.commit()
        db.close()


    for i in range(0, contributor_count):
        rank = i + 1
        db = sqlite3.connect(db_path)
        cur = db.cursor()
        sql = "SELECT contributor_id, video_id, title, regist_date, upload_date, total, view, comment, mylist FROM " + str(table_name) + " WHERE contributor_id = " + str(best_100_contributor_list[i]) + " ORDER BY total DESC"
        cur.execute(sql)
    
        print("投稿者ID " + " 動画ID " + "タイトル" + "データ取得日時" + "投稿日時" + " 総合ポイント " + " 再生数 " + " コメント数 " + " マイリスト数 ")
        video_num = 0
        contributor_id = []
        video_id = []
        title = []
        regist_date = []
        upload_date = []
        total = []
        view = []
        comment = []
        mylist = []
        for row in cur:
            contributor_id.append(str(row[0]))
            video_id.append(str(row[1]))
            title.append(str(row[2]))
            regist_date.append(str(row[3]))
            upload_date.append(str(row[4]))
            total.append(str(row[5]))
            view.append(str(row[6]))
            comment.append(str(row[7]))
            mylist.append(str(row[8]))
            print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            video_num = video_num + 1
        db.close()
        
        db = sqlite3.connect(db_path)
        with closing(db) as con:
            cursor = db.cursor()
            for i in range(0, video_num):
                sql = 'insert into rank' + str(rank) + '(contributor_id, video_id, title, regist_date, upload_date, view, comment, mylist, total) '
                sql += 'values (' + str(contributor_id[i]) + ',"' + str(video_id[i]) + '","' + str(title[i]) + '","' + str(regist_date[i]) + '","' + str(upload_date[i]) + '",' + str(view[i]) + ',' + str(comment[i]) + ',' + str(mylist[i]) + ',' + str(total[i]) + ')'
                print("rank_insert:" + str(rank))
                print(contributor_id[i], video_id[i], title[i], regist_date[i], upload_date[i], view[i], comment[i], mylist[i], total[i])
                cursor.execute(sql)
                con.commit()
            con.close()
