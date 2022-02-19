#!/bin/bash

repo="testing/repo"

cd $repo

# get all commits ids
git log --pretty=format:"%H" > ../all_commits.txt

cd - > /dev/null