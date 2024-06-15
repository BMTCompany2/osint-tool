from pytube import YouTube

def download_youtube_video(url, save_path="."):
    try:
        # Create a YouTube object with the provided URL
        yt = YouTube(url)
        
        # Get the 720p resolution stream if available
        stream = yt.streams.get_highest_resolution()
        
        if stream:
            # Print video details
            print(f"Title: {yt.title}")
            print(f"Author: {yt.author}")
            print(f"Views: {yt.views}")
            print(f"Length: {yt.length} seconds")
            
            # Download the video to the specified path
            print("Downloading...")
            stream.download(output_path=save_path)
            print("Download completed!")
        else:
            print("720p stream is not available for this video.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # URL of the YouTube video to be downloaded
    video_url = "https://www.youtube.com/watch?v=t8qb0LMNvo8"
    
    # Path where the video will be saved
    save_directory = "C:/Users/thayn/Desktop"
    
    download_youtube_video(video_url, save_directory)
