This is a simple flask api that lets you download youtube videos in mp3 or mp4 format (using pytube). \

You can either call it with a url or use the web interface

# Requirements

- You will need ffmpeg: `sudo apt install ffmpeg` on linux\
     (You could also use a python-ffmpeg with a bit of change to the code, but I found it to be pretty slow.) \
- All the requirements for python are listed in the requirements.txt and can be installed with `pip3 install -r requirements.txt` command


# Usage

You can start the program by running the **main.py** \
On default it will be running on local host so you can access the site by opening `http://127.0.0.1:5000` \
And call it with `http://127.0.0.1:5000/apiRequestDownload?url=someVideoUrl&type=video/audio`

