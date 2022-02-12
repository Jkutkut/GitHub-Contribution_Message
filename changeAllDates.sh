#!/bin/sh

echo "Changing dates of all repositories"

newDate="Sat 2022 22:42:42 +0100"

git rebase -i --exec "git commit --amend --date=\"$newDate\" --no-edit" --root