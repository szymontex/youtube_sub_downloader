# youtube_sub_downloader
Download all available subs from all videos from particular yt channel


==============================================

Python script that can download all subtitles from youtube channel you specify. 

You need to specify API_KEY inside '' brackets 
You can get one by creating a google app yourself. 

create new project in your google cloud console
https://console.cloud.google.com
Then enable YouTube Data API v3 interface for your project
Create API credentials, copy one, and paste inside script.



You also need to specify youtube channel id
just google some tool and use one


To download libraries, type in your terminal:

<code>pip install google-auth google-auth-httplib2 google-api-python-client youtube_transcript_api</code>



Script will create folders with channel name and TXT files with subtitles without timings, just text. 
Perfect for grasping a lot of knowledge and then parsing it thru some AI to extract most useful information. 

