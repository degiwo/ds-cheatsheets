https://github.com/zk-org/zk

## Prerequisites
* vim
* vim-plug
  * fzf
  * ripgrep
  * coc

```zsh
call plug#begin("~/.vim/plugged")
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'neoclide/coc.nvim', { 'branch': 'release' }
call plug#end()
```
* then in vim: `:PlugInstall`

## Install
```zsh
brew install zk
```

## Config
```zsh
# ~/.config/zk/config.toml
[group.daily]
paths = ["journal/daily"]
[group.daily.note]
filename = "{{format-date now '%Y-%m-%d'}}"
template = "daily.md"
```

## coc settings
```zsh
{
  // Important, otherwise link completion containing spaces and other special characters won't work.
  "suggest.invalidInsertCharacters": [],

  "languageserver": {
    "zk": {
      "command": "zk",
      "args": ["lsp"],
      "trace.server": "messages",
      "filetypes": ["markdown"],
    },
  },
}
```
