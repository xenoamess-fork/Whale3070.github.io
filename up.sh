#!/bin/bash
rm -fr .git  

git init  

git remote add origin https://github.com/Whale3070/Whale3070.github.io

git fetch  

git reset --hard origin/master  

git branch --set-upstream-to=origin/master master