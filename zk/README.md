https://github.com/zk-org/zk

## Prerequisites
* vim
* vim-plug
  * fzf
  * ripgrep
  * coc

```zsh
# .vimrc
call plug#begin("~/.vim/plugged")
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'neoclide/coc.nvim', { 'branch': 'release' }
call plug#end()

" Verwende gd für 'go to definition' und 'go to references' mit coc.nvim
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gr <Plug>(coc-references)
```
* then in vim: `:PlugInstall`

## Install
```zsh
brew install zk
```

## Config
```zsh
# <notebook>/.zk/config.toml
# or globally: ~/.config/zk/config.toml
[group.daily]
paths = ["journal/daily"]
[group.daily.note]
filename = "{{format-date now '%Y-%m-%d'}}"
template = "daily.md"
```

## coc settings
```zsh
# .vim/coc-settings.json
{
  // Important, otherwise link completion containing spaces and other special characters won't work.
  "suggest.invalidInsertCharacters": [],

  "languageserver": {
    "zk": {
      "command": "zk",
      "args": ["lsp"],
      "trace.server": "messages",
      "filetypes": ["markdown"],
      // important to be able to use 'gd'
      "rootPatterns": [".zk"],
      "trace.server": "verbose"
    },
  },
}
```
