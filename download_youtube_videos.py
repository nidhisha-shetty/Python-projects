

from youtube_dl import YoutubeDL #import YoutubeDL class from youtube_dl packa
import os 						 #importing os; used to change directory to save video files in a particular directory
video_url=["https://youtu.be/_jJZZFPQOvI"] #list of YT video urls 
path="C:/Users/Nidhisha Shetty/Desktop" #path of the directory where the YT videos will be saved 
print("Crnt dir" + os.getcwd())			#check the path of current directory
os.chdir(path)							#change the directory to save the video files in the given 'path'
print("Crnt dir" + os.getcwd())			#check the path of current directory
ydl = YoutubeDL()						#create object of the YoutubeDL class, this object is used to call the download function
print("Downloading youtube videos...")
ydl.download(video_url)					#call the download functin using object of the class, download function takes a list(of url's) as the argument
print("Download completed!!!")


