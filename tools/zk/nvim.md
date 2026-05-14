```
brew install neovim
brew install zk
brew install fzf
git clone https://github.com/folke/lazy.nvim.git ~/.config/nvim/lazy/lazy.nvim
zk init my-notebook
```

```
-- ~/.config/zk/config.toml
[notebook]
dir = "~/my-notebook"
```

```
-- ~/my-notebook/.zk/config.toml
# zk configuration file
#
# Uncomment the properties you want to customize.

# NOTE SETTINGS
#
# Defines the default options used when generating new notes.
[note]

# Language used when writing notes.
# This is used to generate slugs or with date formats.
language = "en"

# The default title used for new note, if no `--title` flag is provided.
default-title = "Untitled"

# Template used to generate a note's filename, without extension.
filename = "{{slug title}}"

# The file extension used for the notes.
extension = "md"

# Template used to generate a note's content.
# If not an absolute path or "~/unix/path", it's relative to .zk/templates/
template = "default.md"

# Path globs ignored while indexing existing notes.
#exclude = [
#    "drafts/*",
#    "log.md"
#]

# Configure random ID generation.

# The charset used for random IDs. You can use:
#   * letters: only letters from a to z.
#   * numbers: 0 to 9
#   * alphanum: letters + numbers
#   * hex: hexadecimal, from a to f and 0 to 9
#   * custom string: will use any character from the provided value
#id-charset = "alphanum"

# Length of the generated IDs.
#id-length = 4

# Letter case for the random IDs, among lower, upper or mixed.
#id-case = "lower"


# EXTRA VARIABLES
#
# A dictionary of variables you can use for any custom values when generating
# new notes. They are accessible in templates with {{extra.<key>}}
[extra]

#key = "value"


# GROUP OVERRIDES
#
# You can override global settings from [note] and [extra] for a particular
# group of notes by declaring a [group."<name>"] section.
#
# Specify the list of directories which will automatically belong to the group
# with the optional `paths` property.
#
# Omitting `paths` is equivalent to providing a single path equal to the name of
# the group. This can be useful to quickly declare a group by the name of the
# directory it applies to.

[group.daily]
paths = ["journal/daily"]
[group.daily.note]
filename = "{{format-date now}}"
template = "daily.md"
extension = "md"

[group.meeting]
paths = ["meetings"]
[group.meeting.note]
filename = "{{format-date now}}_{{slug title}}"
template = "meeting.md"
extension = "md"

# MARKDOWN SETTINGS
[format.markdown]

# Format used to generate links between notes.
# Either "wiki", "markdown" or a custom template. Default is "markdown".
link-format = "wiki"
# Indicates whether a link's path will be percent-encoded.
# Defaults to true for "markdown" format and false for "wiki" format.
#link-encode-path = true
# Indicates whether a link's path file extension will be removed.
# Defaults to true.
#link-drop-extension = true

# Enable support for #hashtags.
hashtags = true
# Enable support for :colon:separated:tags:.
colon-tags = false
# Enable support for Bear's #multi-word tags#
# Hashtags must be enabled for multi-word tags to work.
multiword-tags = false


# EXTERNAL TOOLS
[tool]

# Default editor used to open notes. When not set, the EDITOR or VISUAL
# environment variables are used.
editor = "nvim"

# Pager used to scroll through long output. If you want to disable paging
# altogether, set it to an empty string "".
#pager = "less -FIRX"

# Command used to preview a note during interactive fzf mode.
# Set it to an empty string "" to disable preview.

# bat is a great tool to render Markdown document with syntax highlighting.
#https://github.com/sharkdp/bat
#fzf-preview = "bat -p --color always {-1}"
fzf-preview = "zk list --quiet --format full --limit 1 {-1}"


# LSP
#
#   Configure basic editor integration for LSP-compatible editors.
#   See https://github.com/zk-org/zk/blob/main/docs/editors-integration.md
#
[lsp]

[lsp.diagnostics]
# Each diagnostic can have for value: none, hint, info, warning, error

# Report titles of wiki-links as hints.
#wiki-title = "hint"
# Warn for dead links between notes.
dead-link = "error"

[lsp.completion]
# Customize the completion pop-up of your LSP client.

# Show the note title in the completion pop-up, or fallback on its path if empty.
#note-label = "{{title-or-path}}"
# Filter out the completion pop-up using the note title or its path.
#note-filter-text = "{{title}} {{path}}"
# Show the note filename without extension as detail.
#note-detail = "{{filename-stem}}"


# NAMED FILTERS
#
#    A named filter is a set of note filtering options used frequently together.
#
[filter]

# Matches the notes created the last two weeks. For example:
#    $ zk list recents --limit 15
#    $ zk edit recents --interactive
#recents = "--sort created- --created-after 'last two weeks'"


# COMMAND ALIASES
#
#   Aliases are user commands called with `zk <alias> [<flags>] [<args>]`.
#
#   The alias will be executed with `$SHELL -c`, please refer to your shell's
#   man page to see the available syntax. In most shells:
#     * $@ can be used to expand all the provided flags and arguments
#     * you can pipe commands together with the usual | character
#
[alias]
# Here are a few aliases to get you started.

# Shortcut to a command.
#ls = "zk list $@"
ed = "zk edit --interactive"
daily = 'zk new --no-input "$ZK_NOTEBOOK_DIR/journal/daily"'
meeting = 'zk new --title "$*" "$ZK_NOTEBOOK_DIR/meetings"'

# Default flags for an existing command.
#list = "zk list --quiet $@"

# Edit the last modified note.
#editlast = "zk edit --limit 1 --sort modified- $@"

# Edit the notes selected interactively among the notes created the last two weeks.
# This alias doesn't take any argument, so we don't use $@.
#recent = "zk edit --sort created- --created-after 'last two weeks' --interactive"

# Print paths separated with colons for the notes found with the given
# arguments. This can be useful to expand a complex search query into a flag
# taking only paths. For example:
#   zk list --link-to "`zk path -m potatoe`"
#path = "zk list --quiet --format {{path}} --delimiter , $@"

# Show a random note.
#lucky = "zk list --quiet --format full --sort random --limit 1"

# Returns the Git history for the notes found with the given arguments.
# Note the use of a pipe and the location of $@.
#hist = "zk list --format path --delimiter0 --quiet $@ | xargs -t -0 git log --patch --"

# Edit this configuration file.
conf = 'nvim "$ZK_NOTEBOOK_DIR/.zk/config.toml"'
```

```
-- ~/.config/nvim/init.lua
-- Bootstrap lazy.nvim
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not (vim.uv or vim.loop).fs_stat(lazypath) then
	local lazyrepo = "https://github.com/folke/lazy.nvim.git"
	local out = vim.fn.system({ "git", "clone", "--filter=blob:none", "--branch=stable", lazyrepo, lazypath })
	if vim.v.shell_error ~= 0 then
		vim.api.nvim_echo({
			{ "Failed to clone lazy.nvim:\n", "ErrorMsg" },
			{ out, "WarningMsg" },
			{ "\nPress any key to exit..." },
		}, true, {})
		vim.fn.getchar()
		os.exit(1)
	end
end
vim.opt.rtp:prepend(lazypath)

-- Make sure to setup `mapleader` and `maplocalleader` before
-- loading lazy.nvim so that mappings are correct.
-- This is also a good place to setup other settings (vim.opt)
vim.g.mapleader = " "

vim.opt.number = true
vim.opt.tabstop = 4
vim.opt.shiftwidth = 4

local map = vim.keymap.set
map("n", "gd", vim.lsp.buf.definition)
map("n", "gr", vim.lsp.buf.references)
map("n", "<leader>fb", "<cmd>lua require('fzf-lua').buffers()<CR>")


vim.api.nvim_create_user_command("ZkFind", function()
	require("fzf-lua").grep({
		search = "",
		prompt = "> ",
		cwd = "$ZK_NOTEBOOK_DIR",
	})
end, { desc = "zk: Find in notes" })

-- Setup lazy.nvim
require("lazy").setup({
	spec = {
		{
			"zk-org/zk-nvim",
			config = function()
				require("zk").setup({
					-- Can be "telescope", "fzf", "fzf_lua", "minipick", "snacks_picker",
					-- or select" (`vim.ui.select`).
					picker = "fzf_lua",

					lsp = {
						-- `config` is passed to `vim.lsp.start(config)`
						config = {
							name = "zk",
							cmd = { "zk", "lsp" },
							filetypes = { "markdown" },
							-- on_attach = ...
							-- etc, see `:h vim.lsp.start()`
						},

						-- automatically attach buffers in a zk notebook that match the given filetypes
						auto_attach = {
							enabled = true,
						},
					},
				})
			end,
		},

		{
			"ibhagwan/fzf-lua",
		},
	},
	-- automatically check for plugin updates
	checker = { enabled = true },
})
```
