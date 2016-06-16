from pytube import YouTube
yt = YouTube()

yt.url = "https://youtu.be/QqzT48wZGgU"

#print "原檔名:"+yt.filename
yt.set_filename('rs')
print "改過後檔名:"+yt.filename
print "-----------------------------------------------"

videos = []
for i, video in enumerate(yt.get_videos()):
    ext = video.extension
    res = video.resolution
    videos.append("{} {}".format(ext, res))

print videos

vid = max(videos)
print "影片選項:"+str(yt.get_videos())
print "最大值:"+vid
print "-----------------------------------------------"
print "將檔案類型webm換成mp4:"+vid.replace('webm','mp4')
vid=vid.replace('webm','mp4')
#print vid.split()

vid=vid.split()
print "檔案類型:"+vid[0]

video = yt.get("mp4", "720p")
video.download('D:\\tmpdisk')
