# TubeDownloader
You can download movie/audio from Youtube with python.  
This code automatically peform  
* 1.downloading high quality audio/video respectively  
* 2.mixing them without installing movie editor　　

So you could easily get high quality movie with this software.  

#  Background
When downloading high quality movie with pytube3,  
you must download "high quality audio_only" and "high quality video_only",  and mix them by yourself.   
If you have not installed movie editor like ffmpeg, you must also install it before audio/video mix.  
This software would help if you want to avoid such a time-consuming manual method.

# Requirement
pyTube3 9.6.4  
moviepy 1.0.3  

# Installation

```bash
pip install pyTube3
pip install moviepy
```
# Usage
1.git clone https://github.com/ZenkiKawakami/TubeDownloader.git  
2.cd TubeDownloader  
3.python TubeDownloader.py  
4.input **video(movie without audio)**, **audio(audio only)** or **mix(combined data of video and audio)**  
5.input target URL(YouTube)  
6.start downloading data to the corresponding folder

# For iTunes or QuickTimePlayer User
1.Mix movie might not be well played with quick time player   
2.Duration of the audio data(mp3) might be twice as long as origin(but only first-half would be played on iTunes)  
  
I'm not sure, but these problem might be caused by a bug in moviepy.  
You might play the mix movie with VLC Media Player. So please play with it. 
