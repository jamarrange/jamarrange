import os
import os.path
from os import listdir
from os.path import isfile, join

root = 'C:\\Users\\User\\Music\\test folder'
path = os.path.join(root, "targetdirectory")
all_files_in_dir = []
all_files_dir = []

search_file = 'C:\\Users\\User\\Music\\test folder\\b'
for path, subdirs, files in os.walk(unicode(root, 'utf-8')):
    print len(subdirs)
    all_files_dir.append(subdirs)
##    for i in range(len(subdirs)):
##        if subdirs[i] == search_file:
##            print "found matching file"
    for name in files:
        pass
