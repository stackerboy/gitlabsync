from subprocess import call
import urllib2
import json
import subprocess, shlex
#call([">","file1.txt"])
####################################################################################################################
#COMPARING GROUPS AND CREATING ANY NEW
##STAGE-1
##DC GITLAB
allGroups       = urllib2.urlopen("http://onpremgitip/api/v3/groups?private_token=BhzxixsqEG_WEyWxnTR5&per_page=100")
allGroupsDict   = json.loads(allGroups.read().decode())
for thisGroup in allGroupsDict:
        thisGroupID = str(thisGroup['name'])
        g=open('file1.txt','a')
        call(["echo",thisGroupID],stdout=g)
for thisGroup in allGroupsDict:
        thisGroupID = str(thisGroup['path'])
        g=open('file2.txt','a')
        call(["echo",thisGroupID],stdout=g)
###AWS GITLAB
allGroupsAWS       = urllib2.urlopen("http://AWSGitIP/api/v3/groups?private_token=Qcy&per_page=100")
allGroupsAWSDict   = json.loads(allGroupsAWS.read().decode())
for thisGroup in allGroupsAWSDict:
        thisGroupID = str(thisGroup['name'])
        g=open('file3.txt','a')
        call(["echo",thisGroupID],stdout=g)
for thisGroup in allGroupsAWSDict:
        thisGroupID = str(thisGroup['path'])
        g=open('file4.txt','a')
        call(["echo",thisGroupID],stdout=g)
###############################################################################################################3
#cmd = "sort file3.txt file4.txt | uniq -u"
#cmd="diff -a --suppress-common-lines -y file3.txt file1.txt | sed 's/\s*>.//'"
#ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
#output = ps.communicate()[0]
#f=open('new.txt','w')
#print >>f,output
#################################################################################################################
with open(r'file1.txt','r') as masterdata:
        with open(r'file3.txt','r') as useddata:
                with open(r'name_grp.txt','w+') as Newdata:

                        usedfile = [ x.strip('\n') for x in list(useddata) ] #1
                        masterfile = [ x.strip('\n') for x in list(masterdata) ] #2

                        for line in masterfile: #3
                                if line not in usedfile: #4
                                        Newdata.write(line + '\n') #5

with open(r'file2.txt','r') as masterdata:
        with open(r'file4.txt','r') as useddata:
                with open(r'path_grp.txt','w+') as Newdata:

                        usedfile = [ x.strip('\n') for x in list(useddata) ] #1
                        masterfile = [ x.strip('\n') for x in list(masterdata) ] #2

                        for line in masterfile: #3
                                if line not in usedfile: #4
                                        Newdata.write(line + '\n') #5



with open("name_grp.txt") as file:
        lines = [l.strip() for l in file]
with open("path_grp.txt") as file1:
        path = [l.strip() for l in file1]
        for i,j in zip(lines,path):
                line='name='+str(i)+'&'+'path='+str(j)
                #path='path='+str(i)
                url="http://AWSGitIP/api/v3/groups?private_token=Qcy"
                call(["curl","-X","POST","-d",line,url])
##END OF STAGE-1
