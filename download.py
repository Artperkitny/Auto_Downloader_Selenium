
#TODO

# - Delete mp4 files once done
# - Deal with video foramts
# - Ablum art use thumbnail image 
# - Handle videos that have copy right claim but show up in csv as available 

# Bug

# https://www.youtube.com/watch?v=D_VRSFpUcp0
# Traceback (most recent call last):
#   File "download.py", line 32, in <module>
#     video.download(download_dir)
#   File "/usr/local/lib/python2.7/dist-packages/pytube/models.py", line 62, in download
#     if isfile(fullpath) and not force_overwrite:
#   File "/usr/lib/python2.7/genericpath.py", line 29, in isfile
#     st = os.stat(path)
# UnicodeEncodeError: 'latin-1' codec can't encode character u'\u2013' in position 73: ordinal not in range(256)

# https://www.youtube.com/watch?v=Txg4ZSFendw
# Traceback (most recent call last):
#   File "download.py", line 44, in <module>
#     video.download(download_dir)
#   File "/usr/local/lib/python2.7/dist-packages/pytube/models.py", line 64, in download
#     self.filename))
# OSError: \Error: Conflicting filename:'Artistic Raw - Miami (Havok Roth & HLTRKLTR Festival Trap Remix)'

# https://www.youtube.com/watch?v=o1ke86Gj8Mo
# Traceback (most recent call last):
#   File "download.py", line 53, in <module>
#     video.download(download_dir)
#   File "/usr/local/lib/python2.7/dist-packages/pytube/models.py", line 95, in download
#     "filename.".format(path, self.filename, self.extension))
# IOError

# - Present videos are not being accounted for a duplication error is raised 

from pytube import YouTube
import sys,os
import time
import csv
from pprint import pprint

csv_file = "urls_2015-09-04 17_46_09.099326.csv"
f = open(csv_file, 'rU')
csv_f = csv.reader(f)
blacklist = [
              "https://www.youtube.com/watch?v=_OsjBYxrR0c",
#             "https://www.youtube.com/watch?v=o1ke86Gj8Mo",
#             "https://www.youtube.com/watch?v=Txg4ZSFendw",
#             "https://www.youtube.com/watch?v=8iEdQ912xQQ",
#             "https://www.youtube.com/watch?v=D_VRSFpUcp0",
#             "https://www.youtube.com/watch?v=xvtZEOpG1Wo",
#             "https://www.youtube.com/watch?v=dlnAcp-_Vsg",
#             "https://www.youtube.com/watch?v=IheNxWNbYNA",
]

for i, row in enumerate(csv_f):
    download_dir = '{}/{}/'.format(os.path.dirname(os.path.realpath(__file__)),row[1])
    filename = str(i+1)+" "+str(row[2]).replace("/","").replace("-","").replace("@","").replace('"',"").replace("$","")
    if not os.path.exists(download_dir+filename+".mp3") and row[0] not in blacklist and row[2] != "Private video" and row[2]!= "Deleted video":
        #print row[0]
        yt = YouTube()
        yt.from_url(row[0])
        video = yt.filter('mp4')[-1]
        if video is None:
            print "Mp4 format void: {} {} ".format(row[0],filename)
            #pprint(yt.videos)
        else: 
            if not os.path.exists(download_dir):
                os.makedirs(download_dir)
            #import pdb;pdb.set_trace()
            video.download(download_dir)
            sys.stdout.flush()
            cmd='ffmpeg -i "{}{}.mp4" -acodec libmp3lame -aq 4 "Music 6/{}.mp3"'.format(download_dir,yt.filename,filename)
            print cmd
            os.system(cmd)
            delete = 'rm {}{}.mp4'.format(download_dir,yt.filename)
            #os.system(delete)
    else:
        if os.path.exists(download_dir+filename+".mp3"):
            print "Already downloaded, skipping: {}".format(filename)
        else:
            print "Blacklisted, skipping: {}".format(filename)


