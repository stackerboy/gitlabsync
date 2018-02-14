# Sync GitLab Repository from On-premise to AWS 

### This project demonstrates a simple scripted apporach on how to scale you GitLab repository to AWS
Setting up revision control repositories on on premise datacenter can be made easier using GitLab CE.How ever there are points which has to be noted and taken care before going full phase deployment to production.
1. GitLab server as a single point of failure.
2. GitLab Server backup frequency.
3. Server Capacity and daily commit size of existing GitLab server.
4. How many active user and the admins.

Use for this particular apporach comes when you have a single GitLab Server Community Edition in your on-premise DC.For better reliability and  as a part of securing you code there is a business requirement to secure the application source code forn any disater or virus attacks. 

The easiest way to replicate as is to enable a DB replication which can be done using GitLab Enterprise editionwhich is chargable wrt the users .Same implementation in GitLab CE is not yet supported by GitLab and moreover this has to be implemented in the same DC because of latency constraints.

[x] GitLab has a hierachry structure which has Groups-SubGroups-Projects.
