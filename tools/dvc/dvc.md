# DVC

## Initialize DVC
```sh
dvc init
```

## Set up Google Drive as a remote
```sh
dvc remote add -d myremote gdrive://1pmhbDZEa6QpHZQj6CfLm9tgT16Sv40t_
```

## Add data to remote and dvc file to git
```sh
dvc add data.csv
dvc push
git add data.csv.dvc
```

## Pull data from remote
```sh
dvc pull data.csv
```
