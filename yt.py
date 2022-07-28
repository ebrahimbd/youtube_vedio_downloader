import os
from pickle import TRUE
from alive_progress import alive_bar
from pytube import Playlist, YouTube
from termcolor import colored
from pyfiglet import *
 
# Here is some valid colors that we can use to color our art
# valid_color = ('red', 'green', 'yellow', 'blue', 'cyan', 'white')

ascii_art =figlet_format("     Youtube    free    vedio    Downloader ", font = "digital" )
colored_ascii = colored(ascii_art, 'red')
print(colored_ascii)

print(colored("All files are downloaded in the current directory--> %s"%os.getcwd(), 'yellow'))
print("") 
 

def copyright():
    ascii_art1 =figlet_format("---- ---- Thanks For Download ---- ----  ", font = "digital" )
    colored_ascii1 = colored(ascii_art1, 'cyan')
    ascii_art2 =("© 2022 Developed by Ebrahim Mohammad Saleh , visit ->  https://salehcv.web.app/")
    colored_ascii2= colored(ascii_art2, 'yellow')
    print(colored_ascii1)
    print(colored_ascii2)


# fuchsia = '\033[38;2;255;00;255m'   #  color as hex #FF00FF


def create_file(name, yt_playlist):
    print(yt_playlist.title)
    try:
        os.mkdir(name)
    except FileExistsError:
        pass

i = 0
error_call=0
link=""
is_single_vedio=False
is_playlist=False
is_error_vedio=False


while i < 2:
    answer = input("Download YouTube playlist? (yes or no, y/n) =")
    if any(answer.lower() == f for f in ["yes", 'y',]):
        is_playlist=True
        link = input("Enter a Valid YouTube Playlist URL: ")
        break
    elif any(answer.lower() == f for f in ['no', 'n',]):
        link = input("Enter a Valid YouTube vedio URL: ")
        is_single_vedio=True
        break
    else:
        i += 1
        if i < 2:
            print('Please enter yes or no')
        else:
            print("Invalid answer Nothing done")


def single_vedio():
    global is_error_vedio
    try:
        video= YouTube(link)
        video_get= YouTube(link).streams.get_highest_resolution()
        print("\nPlease Wait Download Will Start Shortly .........") 
        # video_get= YouTube(link).streams.filter(adaptive=True, file_extension='mp4').order_by('resolution').desc().first()
        with alive_bar(bar='blocks', spinner='waves3') as bar: 
            print(f'\n' + 'Downloaded : ',video.title, '~ viewed', video.views, 'times.', )
            video_get.download()
            # video.streams.get_highest_resolution().download("/mnt/Ebrahim/tutorial/playlist_download")
            bar()
        print("\n Videos are downloaded.✅")
        copyright()
        is_error_vedio=False
    except:
        is_error_vedio=True



def playlist_vedio():
    global is_error_vedio
    try:
        yt_playlist = Playlist(link)
        split_line = yt_playlist.title.split("/")
        print("\nPlease Wait Download Will Start Shortly .........") 
        playlist_name = ' '.join(split_line )
        create_file(playlist_name, yt_playlist)
        for video in yt_playlist.videos:
            with alive_bar(bar='blocks', spinner='waves3') as bar: 
                    print(f'\n' + 'Downloaded : ',video.title, '~ viewed', video.views, 'times.', )
                    # video.streams.get_highest_resolution().download("/mnt/Ebrahim/tutorial/playlist_download")
                    # down=video.streams.filter(adaptive=True, file_extension='mp4').order_by('resolution').desc().first()
                    down=video.streams.get_highest_resolution()
                    down.download(playlist_name)
                    bar()
        print("\nAll videos are downloaded.✅")
        copyright()
        is_error_vedio=False
    except:
        is_error_vedio=True



i=0
while i<1000:
    i=i+1
    if is_error_vedio==False:
        if i>=2:
            break
    if i==999:
        print(colored("\nFailed invalid link or Connection Error.............!!", 'red'))
        break
    else:
        if is_single_vedio:
            single_vedio()
        elif is_playlist:
            playlist_vedio()


    
# pip install pyinstaller
# cd /path/to/your/program
# pyinstaller --onefile yourscript.py