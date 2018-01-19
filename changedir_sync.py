from subprocess import call
import urllib2
import json
import subprocess, shlex
import os
#k=open("list_dir.txt")
#call(["ls",'/home/gituser/'],stdout=k)



#md = "ls -d */"
#s = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
#utput = ps.communicate()[0]
#=open('list_dir.txt','w')
#rint >>f,output
cmd = 'ls -d */ > list_dir.txt'
os.system(cmd)
#call(['ls','-d','*/','>','list_dir.txt'])
with open("list_dir.txt") as file2:
        path1 = [l.strip() for l in file2]
        print path1
        for x in path1:
		print x
                #with open("list_dir.txt") as file1:
                 #       path = [l.strip() for l in file1]
                #print "asdasdasda"
			#for i in path:
                        #p=0
                        #i=path[p]
                        #i=i.replace('fw-dw-apacmaven.cyber.bestinet.com', '10.10.2.64')
                wd = os.getcwd()
                os.chdir(x)
                        #y='git'+' '+'remote'+' '+'add'+x+i
                        #subprocess.Popen(y)
			#call(['python','fetch.py'])
		call(['echo','entering',x])
		call(['python','/home/gituser/final_git/pullpython.py'])
                        #a='git'+' '+'push'+' '+x+ 'HEAD=master'
                        #subprocess.Popen(a)
                os.chdir(wd)

