from moviepy.editor import VideoFileClip
import os

os.chdir("C:/Users/thayn/Videos/pnyx-stock-vidoes/process-clips/tech-science/tech-conference")

def edit_clips():
    # Parameters
    video_path = "C:/Users/thayn/Videos/pnyx-stock-vidoes/raw-clips/tech-science/What is TechCrunch Disrupt.mp4"

    # Check if the video file exists
    if not os.path.exists(video_path):
        print(f"Video file not found: {video_path}")
        return

    video = VideoFileClip(video_path)

    # Get the duration of the video
    duration = video.duration
    print(f"Video duration: {duration} seconds")

    # Split the video into 5-second clips
    for i, t in enumerate(range(0, int(duration), 5)):
        start_time = t
        end_time = min(t + 5, duration)

        print(f"Clip {i} :", start_time, end_time)

        clip = video.subclip(start_time, end_time)
        
        try:
            # Extract the clip
            clip = video.subclip(start_time, end_time)

            # Crop the clip to 9:16 aspect ratio
            width, height = clip.size
            aspect_ratio = width / height
            if aspect_ratio > 9 / 16:
                # Crop horizontally
                new_width = int(height * (9 / 16))
                new_height = height
                x1 = (width - new_width) // 2
                x2 = x1 + new_width
                y1 = 0
                y2 = height
                clip = clip.crop(x1=x1, y1=y1, x2=x2, y2=y2)
            else:
                # Crop vertically
                new_width = width
                new_height = int(width * (16 / 9))
                x1 = 0
                x2 = width
                y1 = (height - new_height) // 2
                y2 = y1 + new_height
                clip = clip.crop(x1=x1, y1=y1, x2=x2, y2=y2)

            # Save the clip
            clip.write_videofile(
                f"tech-conference_{i+168}.mp4", 
                fps=30,
                # codec='libx264',
                audio=False 
                )

            # Close the clip
            clip.close()
        except Exception as e:
            print(f"Error processing clip {i}: {e}")

    # Close the original video
    video.close()

# Example usage
if __name__ == "__main__":
    edit_clips()
