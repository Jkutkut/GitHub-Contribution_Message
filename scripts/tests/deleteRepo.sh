repo="repo"
. $PWD/.configuration

echo "Deleting repo \"$repo\""
curl -X DELETE -H "Authorization: token $REPO_TOKEN" "https://api.github.com/repos/$REPO_USR/$repo" > result.tmp

if [ ! -s result.tmp ]; then
	echo "Repo \"$repo\" deleted"
else
	echo "Repo \"$repo\" not deleted"
fi
rm -f result.tmp