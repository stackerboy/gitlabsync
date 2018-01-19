from subprocess import call
import urllib2
import json
import subprocess, shlex
import os

allProjectsAWS = urllib2.urlopen("http://10.10.2.64/api/v3/projects?private_token=QcySbaKWbRisJ7sKWF3j&per_page=100&page=1")
allProjectsAWS1   = json.loads(allProjectsAWS.read().decode())
for thisGroup in allProjectsAWS1:
        g=open('project_aws.txt','a')
        #j=str(thisGroup['ssh_url_repo'])
        #j=j.replace('gitlab.example.com', 'fw-dw-apacmaven.cyber.bestinet.com')
        call(["echo",str(thisGroup['ssh_url_to_repo'])],stdout=g)
allProjectsAWS3 = urllib2.urlopen("http://10.10.2.64/api/v3/projects?private_token=QcySbaKWbRisJ7sKWF3j&per_page=100&page=2")
allProjectsAWS4   = json.loads(allProjectsAWS3.read().decode())
for thisGroup in allProjectsAWS4:
        g=open('project_aws.txt','a')
        #j1=str(thisGroup['ssh_url_to_repo'])
        #j2=j1.replace('gitlab.example.com', 'fw-dw-apacmaven.cyber.bestinet.com')
        call(["echo",str(thisGroup['ssh_url_to_repo'])],stdout=g)


with open("project_aws.txt") as file2:
	path1 = [l.strip() for l in file2]
	for x in path1:
		call(["git","clone",x])



cmd = 'ls -d */ > list_dir.txt'
os.system(cmd)

with open("list_dir.txt") as file1:
        path = [l.strip() for l in file1]
for i in path:
#	line='name='+str(i)+'&'+'path='+str(j)
                #path='path='+str(i)
                #url="http://10.10.2.64/api/v3/groups?private_token=QcySbaKWbRisJ7sKWF3j"
                #call(["cd","/home/gituser/git_clone"])
                #print i
                #call(["ls"])
		#print "step1"
		#j= i + "/"
		j = i.replace("/", "")
		for thisGroup in allProjectsAWS1:
			#j= i + "/"
			#print j
			#print thisGroup['name']
			if j==str(thisGroup['name']):
				print "step4"
				wd=os.getcwd()
				os.chdir(i)				
				call(['git','remote','add','AWS',str(thisGroup['ssh_url_to_repo'])])
				os.chdir(wd)
		for thisGroup in allProjectsAWS4:
			#print "step3"
			if j==str(thisGroup['name']):
				print "step 3"
                                wd=os.getcwd()
                                os.chdir(i)
                                call(['git','remote','add','AWS',str(thisGroup['ssh_url_to_repo'])])
                                os.chdir(wd)

		j=0






		#if name =
                #call(["git","clone",i])
                #os.chdir(x)

		#md = 'ls -td -- */ | head -n 1 > list_dir1.txt'
		#s.system(cmd)
#call(['ls','-d','*/','>','list_dir.txt'])
		#with open("project_aws.txt") as file2:
        	#	path1 = [l.strip() for l in file2]
        	#	print path1
        	#	for x in path1:
                		#print x
				#=i.replace('fw-dw-apacmaven.cyber.bestinet.com', '10.10.2.64')
                #		call(['git','remote','add','AWS',x])		
#                subprocess.Popen(y)
		#call(['python','pushpython.py'])
#               os.chdir(wd)
#               i=i.replace('fw-dw-apacmaven.cyber.bestinet.com', '10.10.2.64')
#               k=open("list_dir.txt")
#                call(["ls"],stdout=k)
#                with open("diff_projects.txt") as file2:
#                        path1 = [l.strip() for l in file2]
#                        for x in path1:
#                                wd = os.getcwd()
#                                #x="/home/gituser"
#                                os.chdir(x)
#                                y='git'+' '+'remote'+' '+'add'+i
#                                subprocess.Popen(y)
#                                os.chdir(wd)


