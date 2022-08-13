# git

## Clone Repository
```sh
git clone https://github.com/degiwo/mlops.git
```

## Create own branch
```sh
git branch own-feature-branch
```

## Pull from Remote and keep local uncommited changes
```sh
git stash
git pull
git stash pop
```

## Rebase feature branch from main
```sh
# USE THIS ONLY FOR LOCAL BRANCHES!!!
git checkout main
git pull
git checkout feature-branch
git rebase main
```

## Merge feature branch with main
```sh
git checkout main
git pull
git merge feature-branch
```

## Squash commit messages
```sh
git rebase -i HEAD~20 # in the interactive editor: ESC > :wq!
git commit --amend
git push -f
```

## Fetch from remote
```sh
git fetch --prune
```

## Merge two repositories: project-a into project-b
```sh
cd path/to/project-b
git remote add project-a /path/to/project-a
git fetch project-a --tags
git merge --allow-unrelated-histories project-a/master # or whichever branch you want to merge
git remote remove project-a
```
