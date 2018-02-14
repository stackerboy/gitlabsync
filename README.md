# Sync GitLab Repository from On-premise to AWS 

### This project demonstrates a simple scripted apporach on how to scale GitLab repository to AWS
Setting up revision control repositories on on premise datacenter can be made easier using GitLab CE.How ever there are points which has to be noted and taken care before going full phase deployment to production.
1. GitLab server as a single point of failure.
2. GitLab Server backup frequency.
3. Server Capacity and daily commit size of existing GitLab server.
4. How many active user and the admins.

Use for this particular apporach comes when you have a single GitLab Server Community Edition in your on-premise DC.For better reliability and  as a part of securing you code there is a business requirement to secure the application source code forn any disater or virus attacks. 

The easiest way to replicate as is to enable a DB replication which can be done using GitLab Enterprise editionwhich is chargable wrt the users .Same implementation in GitLab CE is not yet supported by GitLab and moreover this has to be implemented in the same DC because of latency constraints.

- [x] GitLab has a hierachry structure which has Groups-SubGroups-Projects.
- [x] Server in Cloud has to follow the same structure to replicate sync the data from on-prem to cloud
- [x] Developer should be able to checkin to Cloud based repository in case of any failure.
- [x] Changes has to be synced back or restored back during the failover
- [x] Sync frequency has to be setup manually and is based on the repository size and number

Program-Flow

- [x] **Main.py**

*Script calls the other scripts to achieve the sync thorugh a step by step process*

- [x] **dirempty.py**

*This uses writing output to files and string manipulation .This script will clear of any previous data stored in the file*

- [x] **grpcreate.py**

*This step will compare the groups in on-premise and AWS GitLab servers and write the difference to a file.The file contains the newly added groups in on-premise.The next steps in the script calls the GitLab API and exeuctes the Group creation REST API call and create the same group in AWS GitLab.

- [x] **project_create_all_latest_wip.py**

*This phase will compare the projects in the groups and write the difference to a file .The file now contains the newly added porjects and its parent  group ID in a file ,Next step will create new projects tages to the same group id.*

- [x] **clone_and_push_new_projectsv4.py**

*To update any changes to AWS GitLab repository we need to push the changes to the AWS Project repo path.To achieve this step we follow the below approach .
Clone all the projects to a new directory
Pull the changes to the directory 





