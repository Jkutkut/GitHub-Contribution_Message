#!/bin/bash

COMMIT_DATE_FILE="../commits"
# COMMIT_DATE_FILE="testing/commits"
REPO="testing/repo/"
README_NAME="README.md"
README="res/$README_NAME"
COMMIT_MESSAGE="this commit is made by commitMaker.sh. Find out more at https://github.com/Jkutkut/GitHub-Contribution_Message"


cd $REPO

cp $README $REPO$README_NAME

awk '{print $0}' testing/commits | while read c; do
	git add $README_NAME > /dev/null
	git commit -m "$COMMIT_MESSAGE" --date="$c" > /dev/null
done

cd -