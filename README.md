# PyScrapYt
Simple python script that can be used to get the video comments from YouTube using YouTube API.

## Prerequisites
- Youtube API key.
- Python interpreter.

## Installation
- Get API key at: https://console.cloud.google.com/apis/credentials
- Download / Clone this repo.
```
git clone https://github.com/Username070/PyScrapYt.git
```
- Install google API's client library.
```
pip install --upgrade google-api-python-client
```
- Install `google-auth-oauthlib` and `google-auth-httplib2` libraries for user authorization.
```
pip install --upgrade google-auth-oauthlib google-auth-httplib2
```

## Usage
- Run the script
```py main.py arg1 arg2 arg3```
- Args being:
  - YouTube API key.
  - YouTube video id from video URL, for example: `dQw4w9WgXcQ`, full video url: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
  - Keyword to look for in comments.
- Results are stored in `output.txt` file.
