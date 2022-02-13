#!/bin/bash

COMMIT_DATE_FILE="../commits"
# COMMIT_DATE_FILE="testing/commits"
REPO="testing/repo/"
README_NAME="README.md"
README="res/$README_NAME"
COMMIT_MESSAGE="this commit is made by commitMaker.sh. Find out more at https://github.com/Jkutkut/GitHub-Contribution_Message"
USER_MAIL="jkutkutTesting <jorgeregonzalezetsit@gmail.com>"
REMOTE_URL="https://github.com/JkutkutTesting/repo.git"


rm -rf $REPO # Remove previous repo

mkdir $REPO

cp $README $REPO$README_NAME

cd $REPO

git init
git remote add origin $REMOTE_URL

awk '{print $0}' $COMMIT_DATE_FILE | while read c; do
	echo -n " " >> $README_NAME
	git add $README_NAME > /dev/null
	git commit -m "$COMMIT_MESSAGE" --date="$c" --author="$USER_MAIL" > /dev/null
done

git push --force --set-upstream origin main

cd - > /dev/null