# merge strategy

## Start a new branch of master
```sh
git checkout master
git fetch
git merge
git branch new-feature
```

## Develop new-feature
```sh
git checkout new-feature
git fetch
git merge
# Resolve merge conflicts
# Do some changes and commit
git fetch
git merge
# Resolve merge conflicts
git push
```

## Ready to merge to master
```sh
git checkout master
git fetch
git merge
git checkout new-feature
git merge --no-ff master
# Resolve merge conflicts
git commit
git push
# Create pull request
```
