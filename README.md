# School-Inf

  Git - step
  
    touch - make a file
    git init - init repository
    git config --global user.name '  '
    git config --global user.email gg@gg.com 
    git status - current status 
    git add *  -  add all files
    git rm --cached index.html - remove file from staging area
    git commit - open a default editor to stage changes
    git commit -m 'Just debbug it' - small note without need to open code editor 
    touch .gitignore - make a gitignore where you can add all of files to be ignored
    git remote add origin /link/  - the line from repositionry 
    
    git push -u origin master

    IF ERROR  
    
    git fetch origin master
    git merge origin master
    git fetch origin master:tmp
    git rebase tmp
    git push origin HEAD:master

    CLONE REPOSITORY
    
    git clone /link of repository/
    
    git pull - get new files if other person do change
