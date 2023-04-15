from moviepy.editor import VideoFileClip
import os

def video_to_gif():
    for file in os.listdir('C:/Users/Hladkyi Dmytro/Desktop/IT Oprogromowanie/Python_Projects/project4_mp4_to_gif/video/'):
        if file.endswith((".mp4", ".MP4")):
            file_name = file.split(".")[0]
            gif_file = file_name + ".gif"

        clip = VideoFileClip(f"C:/Users/Hladkyi Dmytro/Desktop/IT Oprogromowanie/Python_Projects/project4_mp4_to_gif/video/{file}")
        clip.write_gif(f"C:/Users/Hladkyi Dmytro/Desktop/IT Oprogromowanie/Python_Projects/project4_mp4_to_gif/gif/{gif_file}", fps=20)


def main():
    video_to_gif()

if __name__ == "__main__":
    main()
