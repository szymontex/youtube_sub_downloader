# YouTube Subtitles Downloader

Download all available subtitles from any specified YouTube channel with ease.

## Overview

This Python script automates the process of downloading all subtitles from a specific YouTube channel. Perfect for amassing a wealth of knowledge and then processing it through AI to extract the most valuable information.

## Prerequisites

- **Python**: Ensure you have Python installed on your machine.
- **Google Cloud API Key**: Create a new project on your [Google Cloud Console](https://console.cloud.google.com). Next, enable the YouTube Data API v3 for your project. Finally, create API credentials and use the provided key in the script.

## Setup and Configuration

1. **Install Required Libraries**: Before running the script, make sure to install the necessary Python libraries:

    ```bash
    pip install google-auth google-auth-httplib2 google-api-python-client youtube_transcript_api
    ```

2. **Configuration**: Open the `youtube_sub_downloader.py` script and:

    - Set `API_KEY` to your Google Cloud API key.
    - Specify the `CHANNEL_ID` for the YouTube channel you want to download subtitles from.

## How to Use

1. **Run the Script**: Execute the `youtube_sub_downloader.py` script:

    ```bash
    python youtube_sub_downloader.py
    ```

2. **Check Downloaded Files**: The script will create folders named after the channel and store `.txt` files inside them. These files contain the subtitles without timings, just the raw text.

## ⚠️ Caution

Ensure you understand YouTube's terms of service and any applicable usage limits for the API. Make sure you have the necessary permissions to download content from the specified channels.

