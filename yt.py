import os
from alive_progress import alive_bar
from pytube import Playlist
from termcolor import colored
from pyfiglet import *
 
# Here is some valid colors that we can use to color our art
# valid_color = ('red', 'green', 'yellow', 'blue', 'cyan', 'white')

ascii_art =figlet_format("Youtube free vedio Downloader ", font = "digital" )
colored_ascii = colored(ascii_art, 'red')
ascii_art1 =figlet_format("© 2022 Developed by Ebrahim Mohammad Saleh https://salehcv.web.app/", font = "digital" )
colored_ascii1 = colored(ascii_art1, 'cyan')
print(colored_ascii)


# fuchsia = '\033[38;2;255;00;255m'   #  color as hex #FF00FF


def create_file(name):
    print(yt_playlist.title)
    try:
        os.mkdir(name)
    except FileExistsError:
        pass


i = 0
error_call=0
while i < 2:
    answer = input("Download YouTube playlist? (yes or no, y/n) =")
    if any(answer.lower() == f for f in ["yes", 'y',]):
        link = input("Enter YouTube Playlist URL: ")
        yt_playlist = Playlist(link)
        print("\nDownloading please wait .........") 
        split_line = yt_playlist.title.split("/")
        playlist_name = ' '.join(split_line )
        create_file(playlist_name)
        def call():
                try:
                    var=1
                    for video in yt_playlist.videos:
                        pass
                        with alive_bar(bar='blocks', spinner='waves3') as bar: 
                                print(f'\n' + 'Downloaded : ',video.title, '~ viewed', video.views, 'times.', )
                                # video.streams.get_highest_resolution().download("/mnt/Ebrahim/tutorial/playlist_download")
                                video.streams.get_highest_resolution().download(playlist_name)
                                var=var+1
                                bar()
                    print("\nAll videos are downloaded.✅")
                    print(colored_ascii1)
                except:
                    call()
                    error_call=error_call+1
                    if(error_call>=100):
                        print("\nFailed Connection Error.............!!!!!!!!!")
                        return
        call()
        break
    elif any(answer.lower() == f for f in ['no', 'n',]):
        print('Single video download is not available right now')
        break
    else:
        i += 1
        if i < 2:
            print('Please enter yes or no')
        else:
            print("Invalid answer Nothing done")
