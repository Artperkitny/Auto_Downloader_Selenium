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
