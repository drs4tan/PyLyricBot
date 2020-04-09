from bs4 import BeautifulSoup
import pyautogui
import re
import requests
import string
import time
import sys


'''
# ! Dependencies:
# ! BeautifulSoup
# ! pyautogui
# ! requests

# * README:
# * Script runs the defaults below without arguments
# * Usage: lyrics.py URL STARTLINE ENDLINE
# * Current timings:
# * 3secs until first line, 1/2sec line delay

# TODO: Allow user to change timings
# TODO: Allow user to cancel

'''


# ! Defaults
geniusurl = 'https://genius.com/Bee-gees-stayin-alive-lyrics'
linestart = 13
lineend = 20
# ! Chrome HTTP Header to allow easier scraping
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.123 Safari/537.36"
}


# * Just checks if the script is ran with arguments
# * If so, it replaces defaults
def SetArgs():
    # * Allows the globals to be edited 
    global geniusurl
    global linestart
    global lineend

    if (len(sys.argv) > 1):
        geniusurl = sys.argv[1]
        linestart = int(sys.argv[2])
        lineend = int(sys.argv[3])


# * Scrapes lyrics from genius url
# * Returns a list of lines
def GetLyrics():
    req = requests.get(
        geniusurl, headers=head)
    page = BeautifulSoup(req.text, features="lxml")
    lyricsblock = page.find("div", {"class": "lyrics"})
    lyrics = lyricsblock.find("p").text.splitlines()
    return lyrics


def main():
    SetArgs()
    # * Pause to let user focus on text input
    timer = 3
    while timer > 0:
        print(f'STARTING IN  {timer} ⚠️ ')
        time.sleep(1)
        timer -= 1
    print(' 🏁  GO ')
    # * Iterate through lines
    for line in GetLyrics()[linestart:lineend]:
        # * Check for genius lyric [Tags] / nl and skip
        # TODO: Add more conditions
        if (line == "" or line == "[Pre-Chorus]" or
                line == "[Chorus]"):

            print(f'skipped line: {line}')
        else:
            pyautogui.write(line)
            pyautogui.write(['enter'])
            time.sleep(.5)
    print('Done 😁 ')
if __name__ == "__main__":
    main()
