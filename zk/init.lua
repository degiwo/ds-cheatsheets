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
vim.opt.cursorline = true
vim.opt.wrap = false
vim.opt.ignorecase = true
vim.opt.smartcase = true
vim.opt.clipboard:append("unnamedplus")
vim.opt.foldcolumn = "1"
vim.opt.splitright = true
vim.opt.splitbelow = true
vim.opt.clipboard = "unnamed"

local map = vim.keymap.set
map("n", "gd", vim.lsp.buf.definition)
map("n", "gr", vim.lsp.buf.references)
map("n", "gh", vim.lsp.buf.hover)
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

		{
			"folke/which-key.nvim",
			event = "VeryLazy",
			config = function()
				require("which-key").setup()
			end,
		},

	},
	-- automatically check for plugin updates
	checker = { enabled = true },
})
