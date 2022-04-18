#!/bin/bash

export getCommitsIds() {
	repo=$1
	echo "Getting commits ids from $repo"
	cd $repo ||
	{
		echo "Error: $repo does not exist"
		return 1
	}
	if [ ! -d .git ]; then
		echo "Error: $repo is not a git repository"
		cd - > /dev/null
		return 1
	fi
	git log --pretty=format:"%H" | cat
	cd - > /dev/null
}

# main() {
# 	repo="testing/repo"

# 	getCommitsIds $repo
# }
# main