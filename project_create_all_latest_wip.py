from subprocess import call
import urllib2
import json
import subprocess, shlex
import os
allProjectsON = urllib2.urlopen("http://10.10.2.63/api/v3/projects/all?private_token=BhzxixsqEG_WEyWxnTR5&per_page=100&page=1")
allProjectsON1   = json.loads(allProjectsON.read().decode())
for thisGroup in allProjectsON1:
        g=open('project_onprem.txt','a')
        call(["echo",str(thisGroup['name'])],stdout=g)
allProjectsON3 = urllib2.urlopen("http://10.10.2.63/api/v3/projects/all?private_token=BhzxixsqEG_WEyWxnTR5&per_page=100&page=2")
allProjectsON4 = json.loads(allProjectsON3.read().decode())
for thisGroup in allProjectsON4:
        g=open('project_onprem.txt','a')
        call(["echo",str(thisGroup['name'])],stdout=g)


allProjectsAWS = urllib2.urlopen("http://10.10.2.64/api/v3/projects?private_token=QcySbaKWbRisJ7sKWF3j&per_page=100&page=1")
allProjectsAWS1   = json.loads(allProjectsAWS.read().decode())
for thisGroup in allProjectsAWS1:
        g=open('project_aws.txt','a')
        #j=str(thisGroup['ssh_url_repo'])
        #j=j.replace('gitlab.example.com', 'fw-dw-apacmaven.cyber.bestinet.com')
        call(["echo",str(thisGroup['name'])],stdout=g)
allProjectsAWS3 = urllib2.urlopen("http://10.10.2.64/api/v3/projects?private_token=QcySbaKWbRisJ7sKWF3j&per_page=100&page=2")
allProjectsAWS4   = json.loads(allProjectsAWS3.read().decode())
for thisGroup in allProjectsAWS4:
        g=open('project_aws.txt','a')
        #j1=str(thisGroup['ssh_url_to_repo'])
        #j2=j1.replace('gitlab.example.com', 'fw-dw-apacmaven.cyber.bestinet.com')
        call(["echo",str(thisGroup['name'])],stdout=g)

with open(r'project_onprem.txt','r') as masterdata:
        with open(r'project_aws.txt','r') as useddata:
                with open(r'diff_projects_all.txt','w+') as Newdata:

                        usedfile = [ x.strip('\n') for x in list(useddata) ] #1
                        masterfile = [ x.strip('\n') for x in list(masterdata) ] #2

                        for line in masterfile: #3
                                if line not in usedfile: #4
                                        Newdata.write(line + '\n') #5


with open("diff_projects_all.txt") as file1:
        path = [l.strip() for l in file1]
        allProj1 = urllib2.urlopen("http://10.10.2.63/api/v3/projects/all?private_token=BhzxixsqEG_WEyWxnTR5&per_page=100&page=1")
        allProj11   = json.loads(allProj1.read().decode())
        allGroup1       = urllib2.urlopen("http://10.10.2.64/api/v3/groups?private_token=QcySbaKWbRisJ7sKWF3j&per_page=100")
        allGroup11   = json.loads(allGroup1.read().decode())
        for i in path:
                for thisGroup in allProj11:
                        if i==str(thisGroup['name']):
                                grpname=str(thisGroup['namespace']['name'])
                                for group in allGroup11:
                                        if grpname==str(group['name']):
                                                print str(group['id'])
                                                name='name='+str(thisGroup['name'])+'&'+'namespace_id='+str(group['id'])
                                                url="http://10.10.2.64/api/v3/projects?private_token=QcySbaKWbRisJ7sKWF3j"
                                                call(["curl","-X","POST","-d",name,url])


        #print i
        #allProj = urllib2.urlopen("http://10.10.2.63/api/v3/projects/all?private_token=BhzxixsqEG_WEyWxnTR5&per_page=100&page=1")
        #allGroups64diff   = json.loads(allProj.read().decode())
        #for thisGroup in allGroups64diff:
        #git remote add
        #       if i==str(thisGroup['name']):
        #               grpname=str(thisGroup['namespace']['name'])
        #               print grpname









########################################################################################################################
                        #name='name='+str(thisGroup['name'])+'&'+'namespace_id='+GroupID

                        #url="http://10.10.2.64/api/v3/projects?private_token=QcySbaKWbRisJ7sKWF3j"
                        #call(["curl","-X","POST","-d",name,url])
                        #url=str(thisGroup['ssh_url_to_repo'])
                        #newurl=url.replace('fw-dw-apacmaven.cyber.bestinet.com','10.10.2.64')
                        #call(['git','clone',url])
                        #call(['git','remote','add','AWS',newurl])

###########################################################################################################################
#with open("diff_projects_all.txt") as file1:

#        path = [l.strip() for l in file1]
#        for i in path:
                #line='name='+str(i)+'&'+'path='+str(j)
                #path='path='+str(i)
                #url="http://10.10.2.64/api/v3/groups?private_token=QcySbaKWbRisJ7sKWF3j"
                #call(["cd","/home/gituser/git_clone"])
                #print i
                #call(["ls"])
                #call(["git","clone",i])
#               os.chdir(x)
#               y='git'+' '+'remote'+' '+'add'+i
#               subprocess.Popen(y)
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



####################################################################################################


