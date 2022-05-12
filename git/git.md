# git

## Clone Repository
```sh
git clone https://github.com/degiwo/mlops.git
```

## Create own branch
```sh
git branch own-feature-branch
```

## Rebase feature branch from main
```sh
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