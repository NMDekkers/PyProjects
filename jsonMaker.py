from __future__ import unicode_literals
def jsonMaker(): # make a json with the client secrets
    import json
    
    client_secret_dict={
      "installed": {
        "client_id":"368049033169-utuq7os7joom342pi5l56elv5vm2cp19.apps.googleusercontent.com",
        "client_secret":"Z2aslUa2JGcjmbfQI4_gfpU-",
        "redirect_uris": ["http://localhost", "urn:ietf:wg:oauth:2.0:oob"],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://accounts.google.com/o/oauth2/token"
      }
    }
    with open('client_secrets.json', 'w') as outfile:
        json.dump(client_secret_dict, outfile)
    
    return

def youtube_auth(): # after having a json file, and using this service for the first time, 
  
    import os
    import sys
    
    from oauth2client.client import flow_from_clientsecrets
    from oauth2client.file import Storage
    from oauth2client.tools import argparser, run_flow
    
    
    # The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
    # the OAuth 2.0 information for this application, including its client_id and
    # client_secret. You can acquire an OAuth 2.0 client ID and client secret from
    # the {{ Google Cloud Console }} at
    # {{ https://cloud.google.com/console }}.
    # Please ensure that you have enabled the YouTube Data API for your project.
    # For more information about using OAuth2 to access the YouTube Data API, see:
    #   https://developers.google.com/youtube/v3/guides/authentication
    # For more information about the client_secrets.json file format, see:
    #   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
    CLIENT_SECRETS_FILE = "client_secrets.json"
    
    # This variable defines a message to display if the CLIENT_SECRETS_FILE is
    # missing.
    MISSING_CLIENT_SECRETS_MESSAGE = """
    WARNING: Please configure OAuth 2.0
    
    To make this sample run you will need to populate the client_secrets.json file
    found at:
    
       %s
    
    with information from the {{ Cloud Console }}
    {{ https://cloud.google.com/console }}
    
    For more information about the client_secrets.json file format, please visit:
    https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
    """ % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                       CLIENT_SECRETS_FILE))
    
    # This OAuth 2.0 access scope allows for full read/write access to the
    # authenticated user's account.
    YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
    
    storage = Storage("%s-oauth2.json" % sys.argv[0])
    credentials = storage.get()
    
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
                                   message=MISSING_CLIENT_SECRETS_MESSAGE,
                                   scope=YOUTUBE_READ_WRITE_SCOPE)
      
    if credentials is None or credentials.invalid:
      flags = argparser.parse_args()
      credentials = run_flow(flow, storage, flags)
    
    return
      
def youtube_builder():  # make a youtube build from which you can request stuff.
    import sys
    import httplib2
    from oauth2client.file import Storage
    from apiclient.discovery import build
    
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    storage = Storage("%s-oauth2.json" % sys.argv[0]) # sys.argv is the name of the script
    credentials = storage.get()
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
      http=credentials.authorize(httplib2.Http()))
      
    return youtube,storage,credentials

def delete_client_sectrets(): # delete the initial json file
    import os   
#    print os.path.dirname(os.path.abspath(__file__))
#    print os.getcwd()
#    print os.path.dirname(__file__)
#    print sys.argv[0]
    
    path = str(os.getcwd()) + '\client_secrets.json'
    os.remove(path)
    return

#delete_credentials()

    
#jsonMaker()
#youtube_auth()
#youtube,storage,credentials = youtube_builder()

import os
import sys
import youtube_dl

# init settings

playlist_id= 'PLaH0iUC7M8fQa0xt-lInCSXivUOB_Yo4p'
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'C:\\Users\\Nick\\Documents\\PyProjects\\test\\%(title)s-%(id)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

# Make youtube build
if os.path.isfile("%s-oauth2.json" % sys.argv[0]):
    youtube,storage,credentials = youtube_builder() 

else:
    jsonMaker()
    youtube_auth()
    delete_client_sectrets()
    youtube,storage,credentials = youtube_builder() 

playlistitems_list_request = youtube.playlistItems().list(
    playlistId=playlist_id,
    part="snippet",
    maxResults=50)

while playlistitems_list_request: # check for every max results. (loops when you have a big playlist)
    playlistitems_list_response = playlistitems_list_request.execute()
    
    
    
    
    
    
    
    
    # download the songs
#    for song_link in :
#        
#        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#            ydl.download([song_link])
    
    
    
    
    
    
    
    playlistitems_list_request = youtube.playlistItems().list_next(
      playlistitems_list_request, playlistitems_list_response) # volgende pagina results

    
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    
    info_dict = ydl.extract_info(video, download=False)
    video_url = info_dict.get("url", None)
    video_id = info_dict.get("id", None)
    video_title = info_dict.get('title', None)
    
    
    #ydl.download([playlist_id])


