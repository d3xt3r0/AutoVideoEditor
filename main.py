from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *

def cut_video(loc, start, interval, clip_duration, output_name):

    stop = 0.0
    try:
        clip = VideoFileClip(loc)
        duration = clip.duration
        while stop < duration-10:
            start += interval
            stop = start + clip_duration
            print("#")
            tempclip = clip.subclip(start, stop)
            final = concatenate_videoclips([final, tempclip])
        final.write_videofile(output_name)
        return True

    except FileNotFoundError:
        return False

if __name__ == "__main__":
    print("Welcome to AutoVideoEditor!")

    loc = input("> Enter input file path [eg: res/input.mp4]")
    start = input("> Enter the start time [eg: 0.0]")
    interval = input("> Enter the interval time [eg: 10 ie, every 10 seconds]")
    clip_duration = input("> Enter the clip duration [eg: 2 ie, for 2 seconds]")
    output = input("> Enter the output path [eg: res/output/output.mp4]")

    cut_video(loc, start, interval, clip_duration, output)

    

        


    
    
    