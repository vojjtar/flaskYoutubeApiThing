This is a simple flask api that lets you download youtube videos in mp3 or mp4 format (using pytube).

You can either call it with a url like this: `http://your.IP/apiRequestDownload?url=someVideoUrl&type=video/audio`
Or use the simple web interface

# Requirements

- You will need ffmpeg: `sudo apt install ffmpeg` on linux
  (You could also use a python-ffmpeg with a bit of change to the code, but I found it to be pretty slow.)
- All the requirements for python are listed in the requirements.txt and can be installed with `pip3 install -r requirements.txt` command


