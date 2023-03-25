import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import httplib2
from google.oauth2 import service_account
from youtube_transcript_api import YouTubeTranscriptApi

# TYPE YOUR API FROM GOOGLE CLOUD CONSOLE AND CHANNEL ID TO DOWNLOAD SUBS FROM
API_KEY = ''
CHANNEL_ID = ''

# Uwierzytelnianie
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)

def get_channel_videos(channel_id):
    videos = []
    request = youtube.search().list(part="id,snippet", channelId=channel_id, type="video", maxResults=50)
    response = request.execute()

    while response:
        for item in response["items"]:
            video_id = item["id"]["videoId"]
            title = item["snippet"]["title"]
            videos.append((video_id, title))

        if "nextPageToken" in response:
            request = youtube.search().list(part="id,snippet", channelId=channel_id, type="video", maxResults=50, pageToken=response["nextPageToken"])
            response = request.execute()
        else:
            break

    return videos

def sanitize_filename(title):
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in invalid_chars:
        title = title.replace(char, '_')
    return title

def download_subtitles(videos):
    for video_id, title in videos:
        sanitized_title = sanitize_filename(title)
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['pl', 'en'])
            transcript_text = "\n".join([entry['text'] for entry in transcript])

            with open(f"{sanitized_title}.txt", "w", encoding="utf-8") as file:
                file.write(transcript_text)

            print(f"Napisy pobrane dla filmu: {title}")

        except Exception as e:
            print(f"Błąd pobierania napisów dla filmu {title}: {e}")

if __name__ == "__main__":
    channel_videos = get_channel_videos(CHANNEL_ID)
    download_subtitles(channel_videos)