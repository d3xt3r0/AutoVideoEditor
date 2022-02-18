from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def cut_video(loc, start, stop, output_name):
    try:
        ffmpeg_extract_subclip(loc, start, stop, targetname=output_name)
        return True
    except FileNotFoundError:
        return False

if __name__ == "__main__":
    print("Welcome to AutoVideoEditor!")

    cut_video('/res/test.mkv', 0.0, 0.5, 'test.mp4')
    
    