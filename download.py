import sys,os
import time
import csv
from pprint import pprint
from pytube import YouTube

# This needs to be atuomated, finds the correct csv somehow
# This could propably be put into a function 
csv_file = "urls_2015-09-04 17_46_09.099326.csv"
f = open(csv_file, 'rU')
csv_f = csv.reader(f)

# Lets get rid of this eventually, I want all videos to work properly 
blacklist = [
              "https://www.youtube.com/watch?v=_OsjBYxrR0c",
              "https://www.youtube.com/watch?v=FstH-FYDASo",
#             "https://www.youtube.com/watch?v=o1ke86Gj8Mo",
#             "https://www.youtube.com/watch?v=Txg4ZSFendw",
#             "https://www.youtube.com/watch?v=8iEdQ912xQQ",
#             "https://www.youtube.com/watch?v=D_VRSFpUcp0",
#             "https://www.youtube.com/watch?v=xvtZEOpG1Wo",
#             "https://www.youtube.com/watch?v=dlnAcp-_Vsg",
#             "https://www.youtube.com/watch?v=IheNxWNbYNA",
]


def clean_name_mp3(filename,i):
    filename = str(i+1)+" "+unicode(filename)
    filename = filename.replace("/","")
    filename = filename.replace("$","")
    filename = filename.replace('"',"")
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
        video = yt.filter('mp4')[-1]
        if video is None:
            print "Mp4 format void: {} {} ".format(row[0],filename)
        else: 
            if not os.path.exists(download_dir):
                os.makedirs(download_dir)
            import pdb;pdb.set_trace()
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




