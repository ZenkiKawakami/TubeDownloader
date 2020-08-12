#[参考]:https://qiita.com/Cyber_Hacnosuke/items/d722eae05d6f7c41a9b7
#[参考2]:https://github.com/Zulko/moviepy/issues/591
#[参考3]:https://stackoverflow.com/questions/61960657/getting-keyerror-url-with-pytube

#[参考4]:https://github.com/nficano/pytube/issues/203
#itunesやQuickTimePlayerだとmp3が二倍の長さになる(再生できるが，後ろ部分は再生出来ない)/mp4がうまく再生できない，現象を確認
#pytubeではバグ報告されてはいるが，特にこれと言って対策はされていないらしい
#VLCではうまく再生できるみたいなのでそちらをご利用ください

from pytube import YouTube
import moviepy.editor as mp
import os
import re

def downloadVideo(yt, title):
    # get video for mp4
    print("start download video...")
    yt.streams.filter(file_extension='mp4', progressive=False).order_by('resolution').desc().first().download(
        './video', title)
    print("completed!")

def downloadAudio(yt, title):
    #get audio for mp4
    print("start download audio...")
    yt.streams.get_by_itag(140).download('./audio', title)
    #yt.streams.get_audio_only().download('./audio', title)
    print("completed!")

    #generate mp3 from mp4
    audio_input = mp.AudioFileClip('./audio/' + title + '.mp4').subclip()
    audio_input.write_audiofile('./audio/' + title + '.mp3')

    #remove mp4
    os.remove('./audio/' + title + '.mp4')

def mix(yt, title):
    #mix video and audio
    output_file = mp.VideoFileClip('./video/' + title + '.mp4').subclip()
    output_file.write_videofile('./mix/' + title + '.mp4', audio ='./audio/' + yt.title + '.mp3')

    # remove video and audio
    # os.remove('./audio/' + title + '.mp4')
    # os.remove('./video/' + title + '.mp4')

def getTitle(yt):
    #タイトル中にファイル名禁止文字やドットがあると危ないので消す
    title = yt.title
    return re.sub(r'[\\/:*?"<>|.]+','', title)

def main():
    types =''
    while types != 'video' and types != 'audio' and types != 'mix':
        print("which type do you want?(video/audio/mix)")
        types = input('>')

    print("please input target url.")
    url = input('>')

    yt = YouTube(url)
    title = getTitle(yt)

    if types == 'video':
        downloadVideo(yt, title)

    elif types == 'audio':
        downloadAudio(yt, title)

    elif types == 'mix':
        downloadVideo(yt, title)
        downloadAudio(yt, title)
        mix(yt, title)

    print('process finished!')
    os.system('PAUSE')


if __name__ == '__main__':
    main()