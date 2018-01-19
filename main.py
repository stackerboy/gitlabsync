from subprocess import call
import urllib2
import json
import subprocess, shlex
import os
print "Empty Directory"
call(['python','dirempty.py'])
print "Creating any New Groups"
call(['python','grpcreate.py'])
print "Creating New Projects"
call(['python','project_create_all_latest_wip.py'])
print "Empty Directory 2"
call(['python','dirempty.py'])
print "Clone and Push new Projects"
call(['python','clone_and_push_new_projectsv4.py'])
print "Empty Directory 3"
call(['python','dirempty.py'])
print "Change Directory and Sync"
call(['python','changedir_sync.py'])
