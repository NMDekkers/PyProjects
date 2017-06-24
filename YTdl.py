# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 19:04:21 2017

@author: Nick
"""
from __future__ import unicode_literals
import youtube_dl

# init settings
a='download_archive'
playlist_id= 'PLaH0iUC7M8fQa0xt-lInCSXivUOB_Yo4p'
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'C:\\Users\\Nick\\Documents\\PyProjects\\test\\%(title)s-%(id)s.%(ext)s',
    'download_archive':a,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

playlist ='https://www.youtube.com/playlist?list=PLaH0iUC7M8fRJPwnZcfVS0d6nPdKsVala'

#with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#        
#    ydl.download([playlist])
    