import sys,os
import time
import csv
from pprint import pprint
from pytube import YouTube

# Need to fix interator since the count if offset due to missing videos 

# This needs to be atuomated, finds the correct csv somehow
# This could propably be put into a function 
csv_file = "urls_2015-10-13 18-38-07.841640.csv"
f = open(csv_file, 'rU')
csv_f = csv.reader(f)

# Lets get rid of this eventually, I want all videos to work properly 
blacklist = [
        # Music 6 
              "https://www.youtube.com/watch?v=_OsjBYxrR0c",
              "https://www.youtube.com/watch?v=FstH-FYDASo",
              "https://www.youtube.com/watch?v=r1kFZTL8H5A",
              "https://www.youtube.com/watch?v=D_VRSFpUcp0",
              'https://www.youtube.com/watch?v=xvtZEOpG1Wo',
              'https://www.youtube.com/watch?v=o1ke86Gj8Mo',
              'https://www.youtube.com/watch?v=1EWh5C6RAEY',
              'https://www.youtube.com/watch?v=K0qmBJNtYWI',
              'https://www.youtube.com/watch?v=Xnda3iSuJEQ',
            # Music titles that changed since the last csv was created, need to change the algorithem to 
            # use the incementing number instead of the entire title to sync. 
              'https://www.youtube.com/watch?v=PdwmM3vyHfA',
              'https://www.youtube.com/watch?v=YvpU1z6xf48',
        #  Music 4 
              'https://www.youtube.com/watch?v=cbPObMToy7M',
              'https://www.youtube.com/watch?v=WYUGI1mtt6c',
              'https://www.youtube.com/watch?v=ieJq8IInwiw',
              'https://www.youtube.com/watch?v=Vk5VuJ7QDq0',
              'https://www.youtube.com/watch?v=LFaQRNHFCzA',
              'https://www.youtube.com/watch?v=IkgekVh7oKI',
              'https://www.youtube.com/watch?v=7sogcfbqvsw',
        #   Music 5 
              'https://www.youtube.com/watch?v=FdAbmvcQ1F0',
              'https://www.youtube.com/watch?v=uVpQqdBzAcU',
              'https://www.youtube.com/watch?v=WaNeMOkfPF0',
              'https://www.youtube.com/watch?v=fEdnC4ohQLc',
              'https://www.youtube.com/watch?v=pZvDOTiypuM',


]


def clean_name_mp3(filename,i):
    filename = str(i+1)+" "+unicode(filename)
    filename = filename.replace("/","")
    filename = filename.replace("$","")
    filename = filename.replace('"',"")
    filename = filename.replace('?',"")
    # print "Cleaned mp3 filename: {}".format(filename)
    return filename

delete_cmd = "find . -name '*.mp4' -delete"
print delete_cmd
os.system(delete_cmd)

for i, row in enumerate(csv_f):
    download_dir = '{}/{}/'.format(os.path.dirname(os.path.realpath(__file__)),row[1])
    filename = clean_name_mp3(row[2],i)
    print "Downloading {0}    {1}".format(filename,row[0])
    if not os.path.exists(download_dir+filename+".mp3") and row[0] not in blacklist and row[2] != "Private video" and row[2]!= "Deleted video":
        yt = YouTube()
        yt.from_url(row[0])
        yt.set_filename(filename)
        video = yt.filter('mp4')[-1]
        if video is None:
            print "Mp4 format void: {} {} ".format(row[0],filename)
        else: 
            if not os.path.exists(download_dir):
                os.makedirs(download_dir)
            video.download(download_dir)
            sys.stdout.flush()
            #cmd_create = "touch {}{}.mp3".format(download_dir,filename)
            cmd='ffmpeg -i "{}{}.mp4" -acodec libmp3lame -aq 4 "{}{}.mp3"'.format(download_dir,yt.filename,download_dir,filename)
            #print cmd_create
            print cmd
            #os.system(cmd_create)
            os.system(cmd)
    else:
        if os.path.exists(download_dir+filename+".mp3"):
            print "Already downloaded, skipping: {}".format(filename)
        else:
            print "Blacklisted, skipping: {}".format(filename)




