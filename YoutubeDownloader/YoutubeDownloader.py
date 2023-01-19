# Step 1: Import the package
from pytube import YouTube
import moviepy.editor as mp


# Step 2: Get Youtube Link
link = "https://www.youtube.com/watch?v=UBxxEyVIdO4&ab_channel=LondonGrammar"


# Step 3: Call Youtube Function And Assign It To A Variable
yt = YouTube(link)


#Step 4: Assign Values To Variables
yt.streams.filter(progressive = True, 
file_extension = "mp4").first().download(output_path = "/Users/katlegomatebane/Desktop",
filename = "Video.mp4")


# Step 5: Assign Video To A Variable Named 'Video'
video = mp.VideoFileClip(r'/Users/katlegomatebane/Desktop/Video.mp4')


# Step 6: Convert Video To Mp3
video.audio.write_audiofile(r'/Users/katlegomatebane/Desktop/Audio.mp3')

