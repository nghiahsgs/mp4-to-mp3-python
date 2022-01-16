import os
from moviepy.editor import *
# video = VideoFileClip(os.path.join("path","to","movie.mp4"))
# video.audio.write_audiofile(os.path.join("path","to","movie_sound.mp3"))

# source = 'Ink in Water Background (360p).mp4'
source = 'Aston Villa 2-2 Man United_ Khi giá trị TÂN BINH nhấn chìm ngày vui của BRUNO.mp4'
dest = "test.mp3"

video = VideoFileClip(source)
video.audio.write_audiofile(dest)