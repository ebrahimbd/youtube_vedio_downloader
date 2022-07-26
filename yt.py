from operator import truediv
from alive_progress import alive_bar
import time
from pytube import Playlist
from termcolor import colored, cprint

text = colored('Ebrahim free cracking youtube downloader!', 'red', attrs=['reverse', 'blink'])
print(text)
 




# fuchsia = '\033[38;2;255;00;255m'   #  color as hex #FF00FF

 

i = 0
error_call=0
while i < 2:
    answer = input("Download YouTube playlist? (yes or no, y/n) =")
    if any(answer.lower() == f for f in ["yes", 'y',]):
        link = input("Enter YouTube Playlist URL: ")
        yt_playlist = Playlist(link)
        print("\nDownloading please wait .........") 
        def call():
                try:
                    var=1
                    for video in yt_playlist.videos:
                        with alive_bar(bar='blocks', spinner='waves3') as bar: 
                                print(f'\n' + 'Downloaded : ',video.title, '~ viewed', video.views, 'times.', )
                                video.streams.get_highest_resolution().download("/mnt/Ebrahim/tutorial/playlist_download")
                                var=var+1
                                bar()
                    print("\nAll videos are downloaded.✅")
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
