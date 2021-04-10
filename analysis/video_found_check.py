import analysis.video_parse as video_parse


"""
動画が現存しているか調べる
@param {str} videoid 動画ID (sm0000000)
@returns {str} 取得したらfoundを返す(取得できなかったら消去・非公開にされているため、"novideo"を返す)
"""
def video_found_check(videoid):

    # XML形式からreadできる形式に変換
    xml_video = video_parse.XML_VideoData("http://ext.nicovideo.jp/api/getthumbinfo/", str(videoid))
    xml = xml_video.video_parse()

    # 形式がsmか判定
    if "sm" in str(xml[0][0].text):
        return "found"
    else:
        video_no_found = "novideo"
    # 形式がsoか判定
    if "so" in str(xml[0][0].text):
        return "found"
    else:
        video_no_found = "novideo"
    # 形式がnmか判定
    if "nm" in str(xml[0][0].text):
        return "found"
    else:
        video_no_found = "novideo"
    
    return video_no_found