" Attempt to determine the type of a file based on its name and possibly its
" contents. Use this to allow intelligent auto-indenting for each filetype,
" and for plugins that are filetype specific.
if has('filetype')
  filetype indent plugin on
endif

" Enable syntax highlighting
if has('syntax')
  syntax on
endif

" Better command-line completion
set wildmenu

" Show partial commands in the last line of the screen
set showcmd

" Instead of failing a command because of unsaved changes,
" raise a dialogue if you wish to save changed files
set confirm

# Display relative line number
set number relativenumber

" Always display the status line even if only one window is displayed
set laststatus=2
