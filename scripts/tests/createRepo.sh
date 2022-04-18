repo="repo"
. $PWD/.configuration

curl -X POST -H "Authorization: token $REPO_TOKEN" https://api.github.com/user/repos --data "{\"name\":\"$repo\"}"

# curl -H "Authorization: token ACCESS_TOKEN" --data '{"name":"NEW_REPO_NAME"}' https://api.github.com/orgs/ORGANIZATION_NAME/repos
