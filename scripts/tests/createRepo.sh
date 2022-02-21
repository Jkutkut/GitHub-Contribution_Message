repo="repo"
usr="jkutkutTesting"
TOKEN=""

curl -X POST -H "Authorization: token $TOKEN" https://api.github.com/user/repos --data "{\"name\":\"$repo\"}"

# curl -H "Authorization: token ACCESS_TOKEN" --data '{"name":"NEW_REPO_NAME"}' https://api.github.com/orgs/ORGANIZATION_NAME/repos
