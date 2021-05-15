from googleapiclient.discovery import build
import time
import sys

# YouTube API key
APIkey = str(sys.argv[1])

# Video ID
videoID = str(sys.argv[2])

# Keyword to look for
keyword = str(sys.argv[3])

# Open file for writing
f = open("output.txt", "a")
  
def videoComments(videoID):

    # Keep track of commets scraped
    commentsScraped = 0
  
    # Creating youtube resource object
    youtube = build("youtube", "v3",
                    developerKey = APIkey)
  
    # Retrieve youtube video results
    video_response = youtube.commentThreads().list(
    part = "snippet,replies",
    videoId = videoID
    ).execute()

    print("Scraping..")
  
    # Iterate video response
    while video_response:

        # Get next page token
        try:
            nextPageToken = video_response["nextPageToken"]
        except:

            # If next page token doesn't exist
            print("Checking last page")

        # extracting required info
        # from each result object 
        for item in video_response["items"]:
            
            # Extracting comments
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]

            # Write comment into output file
            # If comment contains specified keyword
            try:
                if(keyword.lower() in comment.lower()):
                    f.write(comment + "\n \n")
                    commentsScraped += 1
            
            # Some coments might contain unicode characters
            # These kind of comments are skipped
            except:
                print("Skipped")
  
        # Repeat the procces if response contains
        # Another page to check
        if "nextPageToken" in video_response:
            time.sleep(0.5) # Don't overflow the API
            video_response = youtube.commentThreads().list(
                    part = "snippet,replies",
                    pageToken = nextPageToken,
                    videoId = videoID
                ).execute()
        else:
            f.close()
            print("Scraping done, total results:", commentsScraped)
            break

# Call function
videoComments(videoID)