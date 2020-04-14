# git_usage

## SSH_generate
create an empty repository

`ssh-keygen -t rsa -C "myname@mymail.com"`

## git config

****
git config --global user.name 

git config --global user.email 

****

## git usage


```
echo "# records" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:traviscn/records.git
git push -u origin master
                
```
