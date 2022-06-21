# Visual Studio Code

## Open VS Code via Shell

```
cd /path/to/project
code .
```

## Global User Settings for Python

### Install pipx

```
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

### Install Packages

```
pipx install pylint && \
  pipx install black && \
  pipx install poetry && \
  pipx install pipenv && \
  pipx install bandit && \
  pipx install mypy && \
  pipx install flake8
```

### Add to settings.json to apply to all projects

```
"python.pipenvPath": "${env:HOME}/.local/bin/pipenv",
"python.poetryPath": "${env:HOME}/.local/bin/poetry",
"python.condaPath": "${env:HOME}/.local/bin/conda",
"python.linting.enabled": true,
"python.linting.banditPath": "${env:HOME}/.local/bin/bandit",
"python.linting.banditEnabled": true,
"python.linting.pylintPath": "${env:HOME}/.local/bin/pylint",
"python.linting.mypyPath": "${env:HOME}/.local/bin/mypy",
"python.linting.flake8Path": "${env:HOME}/.local/bin/flake8",
"python.formatting.blackPath": "${env:HOME}/.local/bin/black"
```

## Keyboard Shortcuts

|Action|Shortcut|
|-|-|
|Command Palette|F1 OR Ctrl + Shift + P|
|Explorer|Ctrl + Shift + E|
|New Terminal|Ctrl + Alt + Ö|
