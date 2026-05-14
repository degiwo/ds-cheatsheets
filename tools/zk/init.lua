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
vim.api.nvim_set_keymap("n", "<leader>zbf", ":ZkBuffers<CR>", { noremap = true, silent = true })
vim.api.nvim_set_keymap("n", "<leader>zf", ":ZkFind<CR>", { noremap = true, silent = true })
vim.api.nvim_set_keymap("v", "<leader>znt", ":ZkNewFromTitleSelection<CR>", { noremap = true, silent = true })
vim.api.nvim_set_keymap("n", "<leader>zbl", ":ZkBacklinks<CR>", { noremap = true, silent = true })
vim.api.nvim_set_keymap("n", "<leader>zl", ":ZkLinks<CR>", { noremap = true, silent = true })
vim.api.nvim_set_keymap("v", "<leader>zm", ":ZkMatch<CR>", { noremap = true, silent = true })
vim.api.nvim_set_keymap("n", "<leader>zt", ":ZkMatch<CR>", { noremap = true, silent = true })
vim.api.nvim_set_keymap("i", "<C-z>l", "<C-c>:ZkInsertLink<CR>i", { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', '<leader>zt', ':ZkTodo<CR>', { noremap = true, silent = true })

map("n", "<leader>fb", "<cmd>lua require('fzf-lua').buffers()<CR>")

vim.api.nvim_create_user_command("ZkMeeting", function()
	local output = vim.fn.systemlist("zk edit --interactive")
	vim.cmd("new")
	vim.api.nvim_buf_set_lines(0, 0, -1, false, output)
end, {})

vim.api.nvim_create_user_command('ZkTodo', function()
  local notebook_path = vim.fn.expand("$ZK_NOTEBOOK_DIR")  -- passe deinen Pfad an
  local grep_pattern = "TODO"

  -- Alle Dateien mit TODO finden (filtern auf *.md)
  local handle = io.popen(
    string.format('rg --files-with-matches "%s" --glob "*.md" "%s"', grep_pattern, notebook_path)
  )
  if not handle then
    print("Fehler beim Ausführen von rg")
    return
  end

  local result = {}
  for filepath in handle:lines() do
    table.insert(result, filepath)
  end
  handle:close()

  if #result == 0 then
    print("Keine TODOs gefunden")
    return
  end

  require('fzf-lua').fzf_exec(result, {
    prompt = "TODO notes> ",
    previewer = "bat",
    actions = {
      ['default'] = function(selected)
        local file = selected[1]
        vim.cmd("edit " .. file)
        -- Optional: springe zum ersten TODO
        vim.fn.search("TODO")
      end,
      ['ctrl-s'] = function(selected)
        local file = selected[1]
        vim.cmd("split " .. file)
        vim.fn.search("TODO")
      end,
      ['ctrl-x'] = function(selected)
        local file = selected[1]
        vim.cmd("vsplit " .. file)
        vim.fn.search("TODO")
      end,
    },
  })
end, {})

vim.api.nvim_create_user_command("ZkFind", function()
	local notebook_path = vim.fn.expand("$ZK_NOTEBOOK_DIR")

	-- Finde alle .md-Dateien (rekursiv)
	local files = vim.fn.globpath(notebook_path, "**/*.md", false, true)

	local entries = {}

	for _, file in ipairs(files) do
		local lines = vim.fn.readfile(file)
		local flat = table.concat(lines, " ")
		local display = string.format("%s: %s", vim.fn.fnamemodify(file, ":."), flat)
		table.insert(entries, display)
	end

	require('fzf-lua').fzf_exec(entries, {
		prompt = "ZkFind > ",
		previewer = "builtin",
		actions = {
			['default'] = function(selected)
				local full_line = selected[1]
				local filename = full_line:match("^(.-):")
				vim.cmd("edit " .. filename)
			end,
			["ctrl-s"] = function(selected)
				local full_line = selected[1]
				local filename = full_line:match("^(.-):")
				vim.cmd("split " .. filename)
			end,
		},
	})
end, { desc = "Find in Notes" })



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
			opts = {
				preset = "helix",
				icons = {
					keys = {
						Up = '<Up> ',
						Down = '<Down> ',
						Left = '<Left> ',
						Right = '<Right> ',
						C = '<C-…> ',
						M = '<M-…> ',
						D = '<D-…> ',
						S = '<S-…> ',
						CR = '<CR> ',
						Esc = '<Esc> ',
						ScrollWheelDown = '<ScrollWheelDown> ',
						ScrollWheelUp = '<ScrollWheelUp> ',
						NL = '<NL> ',
						BS = '<BS> ',
						Space = '<Space> ',
						Tab = '<Tab> ',
						F1 = '<F1>',
						F2 = '<F2>',
						F3 = '<F3>',
						F4 = '<F4>',
						F5 = '<F5>',
						F6 = '<F6>',
						F7 = '<F7>',
						F8 = '<F8>',
						F9 = '<F9>',
						F10 = '<F10>',
						F11 = '<F11>',
						F12 = '<F12>',
					},
					mappings = false,
				}, 
			},
		},


	},
	-- automatically check for plugin updates
	checker = { enabled = true },
})
