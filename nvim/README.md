```
-- ~/.config/nvim/init.lua
require("config.lazy")
```

```
-- ~/.config/nvim/lua/config/lazy.lua
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git", "clone", "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

require("lazy").setup({
  -- Zettelkasten
  { import = "config.zk" },

  -- Completion Engine
  {
    "hrsh7th/nvim-cmp",
    dependencies = {
      "hrsh7th/cmp-nvim-lsp",
      "hrsh7th/cmp-buffer",
      "hrsh7th/cmp-path",
      "L3MON4D3/LuaSnip",
      "saadparwaiz1/cmp_luasnip",
    },
    config = function()
      local cmp = require("cmp")
      cmp.setup({
        mapping = cmp.mapping.preset.insert({
          ["<Tab>"] = cmp.mapping.confirm({ select = true }),
          ["<C-Space>"] = cmp.mapping.complete(),
        }),
        sources = cmp.config.sources({
          { name = "nvim_lsp" },
          { name = "buffer" },
          { name = "path" },
        }),
      })
    end,
  },
})
```

```
-- ~/.config/nvim/lua/config/zk.lua
return {
  "mickael-menu/zk-nvim",
  dependencies = { "nvim-telescope/telescope.nvim" },
  ft = "markdown",
  config = function()
    local cmp_capabilities = require("cmp_nvim_lsp").default_capabilities()

    require("zk").setup({
      picker = "telescope",
      lsp = {
        config = {
          cmd = { "zk", "lsp" },
          name = "zk",
          capabilities = cmp_capabilities,
        },
        auto_attach = {
          enabled = true,
          filetypes = { "markdown" },
        },
      }
    })

    -- Keymaps
    local map = vim.keymap.set
    map("n", "<leader>zn", "<cmd>ZkNew { title = vim.fn.input('Title: ') }<CR>", { desc = "Neue Notiz" })
    map("n", "<leader>zf", "<cmd>ZkNotes { sort = { 'modified' } }<CR>", { desc = "Notiz suchen" })
    map("n", "<leader>zt", "<cmd>ZkTags<CR>", { desc = "Tags durchsuchen" })
  end,
}
```
