#!/bin/bash

dir="../testRepoDate"
date="Mon 20 Aug 2018 20:42:42 BST"

mkdir $dir
cd $dir
git init

touch file1
git add file1
git commit -m "first commit" --date "$date"
git log

cd - # Go back to the initial directory