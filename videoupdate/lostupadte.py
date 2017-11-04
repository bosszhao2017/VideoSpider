# -*- coding:utf-8 -*-
from video.src.log import Log
from video.src.timenow import TimeNow
from video.videodownload.download import DownloadVideo


def lost_update(web_url, video_message, file_name, connect, video_url=''):

    conn = connect
    cur = conn.cursor()

    if 'http://v.ifeng.com' in web_url:
        download_video = DownloadVideo(video_message[10], unicode(video_message[1], "utf-8"), file_name)
        video_file = download_video.video_download()
        sql = "UPDATE fenghuang " \
              "SET Video_Id=%s, Video_Name=%s, Video_Author=%s, Video_Size=%s, Video_Time=%s, Video_Modify=%s" \
              ", Video_View=%s, Video_Oppose=%s, Video_Support=%s, Video_Comment=%s, Video_Url=%s, Video_File=%s " \
              "WHERE Video_Web=%s"
        try:
            cur.execute(sql, (video_message[0], video_message[1], video_message[2], video_message[3], video_message[4],
                              video_message[5], video_message[6], video_message[7], video_message[8],
                              video_message[9], video_message[10], video_file, web_url))
            conn.commit()
        except Exception as e:
            print (e)
            conn.rollback()

    if 'http://v.163.com' in web_url:
        download_video = DownloadVideo(video_url, unicode(video_message[1], "utf-8"), file_name)
        video_file = download_video.video_download()
        sql = "UPDATE wangyi " \
              "SET Video_Id=%s, Video_Name=%s, Video_Author=%s, Video_Size=%s, Video_Time=%s, Video_modify=%s" \
              ", Video_View=%s, Video_Oppose=%s, Video_Support=%s, Video_Comment=%s, Video_Comment_Fav=%s" \
              ", Video_Comment_Against=%s, Video_Url=%s, Video_File=%s " \
              "WHERE Video_Web=%s"
        try:
            cur.execute(sql, (video_message[0], video_message[1], video_message[2], video_message[3], video_message[4],
                              video_message[5], video_message[6], video_message[7], video_message[8],
                              video_message[9], video_message[10], video_message[11], video_url, video_file, web_url))
            conn.commit()
        except Exception as e:
            print (e)
            conn.rollback()

    if 'http://rr.tv' in web_url or 'http://www.rr.tv' in web_url:
        download_video = DownloadVideo(video_url, video_message[1], file_name)
        video_file = download_video.video_download()
        sql = "UPDATE renren " \
              "SET Video_Id=%s,Video_Name=%s,Video_Author=%s,Video_Size=%s,Video_Time=%s," \
              "Video_View=%s,Video_Support=%s,Video_Comment=%s,Video_Url=%s,Video_File=%s " \
              "WHERE Video_Web=%s"
        try:
            cur.execute(sql, (video_message[0], video_message[1], video_message[2],
                              video_message[3], video_message[4], video_message[5], video_message[6],
                              video_message[7], video_url, video_file, web_url))
            conn.commit()
        except Exception as e:
            print (e)
            conn.rollback()
    cur.close()
    mess = TimeNow.get_time() + ' 注意 : [ ' + video_message[1] + ' ] 信息已补全，请注意查看！'
    print (mess)
    Log.log(mess)