-- Terminal Workbench — highlight engine
-- https://github.com/Real-Fruit-Snacks/terminal-workbench-suite

local palette = require("twb.palette")

local M = {}

local function set(group, opts)
  vim.api.nvim_set_hl(0, group, opts)
end

-- Diagnostic underline: undercurl only, no fg/bg change.
local function underline(group, color)
  set(group, { undercurl = true, sp = color })
end

function M.setup(mode)
  local p = palette[mode]
  if not p then
    error("twb: unknown mode '" .. tostring(mode) .. "', expected 'dark' or 'light'")
  end

  vim.cmd("highlight clear")
  if vim.fn.exists("syntax_on") == 1 then
    vim.cmd("syntax reset")
  end

  vim.o.background = mode
  vim.g.colors_name = "twb-" .. mode

  -- Core UI -----------------------------------------------------------
  set("Normal", { fg = p.text_normal, bg = p.bg0 })
  set("NormalNC", { fg = p.text_normal, bg = p.bg0 })
  set("NormalFloat", { fg = p.text_normal, bg = p.bg1 })
  set("FloatBorder", { fg = p.border, bg = p.bg1 })
  set("Cursor", { fg = p.text_on_accent, bg = p.accent })
  set("CursorLine", { bg = p.bg2 })
  set("CursorLineNr", { fg = p.text_soft, bold = true })
  set("LineNr", { fg = p.text_faint })
  set("SignColumn", { fg = p.text_faint, bg = p.bg0 })
  set("ColorColumn", { bg = p.bg1 })
  set("VertSplit", { fg = p.border, bg = p.bg0 })
  set("WinSeparator", { fg = p.border, bg = p.bg0 })
  set("StatusLine", { fg = p.text_muted, bg = p.bg1 })
  set("StatusLineNC", { fg = p.text_faint, bg = p.bg1 })
  set("TabLine", { fg = p.text_muted, bg = p.bg1 })
  set("TabLineFill", { bg = p.bg1 })
  set("TabLineSel", { fg = p.accent, bg = p.bg0, bold = true })
  set("Pmenu", { fg = p.text_normal, bg = p.bg2 })
  set("PmenuSel", { fg = p.text_on_accent, bg = p.accent })
  set("PmenuSbar", { bg = p.bg3 })
  set("PmenuThumb", { bg = p.border_strong })
  set("Visual", { bg = p.visual })
  set("Search", { fg = p.text_normal, bg = p.search_bg })
  set("IncSearch", { fg = p.text_on_accent, bg = p.accent })
  set("CurSearch", { fg = p.text_on_accent, bg = p.accent })
  set("MatchParen", { fg = p.accent_alt, bg = p.bg3, bold = true })
  set("Folded", { fg = p.text_muted, bg = p.bg1 })
  set("FoldColumn", { fg = p.text_faint })
  set("NonText", { fg = p.text_faint })
  set("Whitespace", { fg = p.text_faint })
  set("SpecialKey", { fg = p.text_faint })
  set("Directory", { fg = p.accent_alt })
  set("Title", { fg = p.accent, bold = true })
  set("ErrorMsg", { fg = p.red, bold = true })
  set("WarningMsg", { fg = p.warm })
  set("MoreMsg", { fg = p.accent })
  set("Question", { fg = p.accent })
  set("QuickFixLine", { fg = p.text_normal, bg = p.search_bg })
  set("WildMenu", { fg = p.text_on_accent, bg = p.accent })

  -- Classic syntax ------------------------------------------------------
  set("Comment", { fg = p.text_muted })
  set("SpecialComment", { fg = p.text_muted })
  set("String", { fg = p.accent })
  set("Character", { fg = p.accent })
  set("Number", { fg = p.orange })
  set("Float", { fg = p.orange })
  set("Boolean", { fg = p.orange })
  set("Constant", { fg = p.orange })
  set("Identifier", { fg = p.text_normal })
  set("Function", { fg = p.accent_alt })
  set("Statement", { fg = p.violet })
  set("Conditional", { fg = p.violet })
  set("Repeat", { fg = p.violet })
  set("Label", { fg = p.violet })
  set("Operator", { fg = p.text_soft })
  set("Keyword", { fg = p.violet })
  set("Exception", { fg = p.violet })
  set("PreProc", { fg = p.violet })
  set("Include", { fg = p.violet })
  set("Define", { fg = p.violet })
  set("Macro", { fg = p.violet })
  set("Type", { fg = p.accent_alt })
  set("StorageClass", { fg = p.violet })
  set("Structure", { fg = p.accent_alt })
  set("Special", { fg = p.warm })
  set("SpecialChar", { fg = p.accent_alt })
  set("Tag", { fg = p.red })
  set("Delimiter", { fg = p.text_soft })
  set("Todo", { fg = p.warm, bg = p.todo_bg, bold = true })
  set("Error", { fg = p.red, bold = true })
  set("Underlined", { fg = p.accent_alt, underline = true })

  -- Treesitter ------------------------------------------------------------
  set("@comment", { fg = p.text_muted })
  set("@string", { fg = p.accent })
  set("@string.escape", { fg = p.accent_alt })
  set("@string.regexp", { fg = p.orange })
  set("@keyword", { fg = p.violet })
  set("@keyword.operator", { fg = p.text_soft })
  set("@operator", { fg = p.text_soft })
  set("@function", { fg = p.accent_alt })
  set("@function.builtin", { fg = p.accent_alt })
  set("@function.method", { fg = p.accent_alt })
  set("@type", { fg = p.accent_alt })
  set("@type.builtin", { fg = p.accent_alt })
  set("@constructor", { fg = p.accent_alt })
  set("@constant", { fg = p.orange })
  set("@constant.builtin", { fg = p.orange })
  set("@number", { fg = p.orange })
  set("@boolean", { fg = p.orange })
  set("@property", { fg = p.warm })
  set("@field", { fg = p.warm })
  set("@attribute", { fg = p.warm })
  set("@tag", { fg = p.red })
  set("@tag.attribute", { fg = p.warm })
  set("@tag.delimiter", { fg = p.text_soft })
  set("@variable", { fg = p.text_normal })
  set("@variable.member", { fg = p.warm })
  set("@variable.parameter", { fg = p.text_normal })
  set("@punctuation", { fg = p.text_soft })
  set("@markup.heading.1", { fg = p.text_normal, bold = true })
  set("@markup.heading.2", { fg = p.accent, bold = true })
  set("@markup.heading.3", { fg = p.accent_alt, bold = true })
  set("@markup.heading.4", { fg = p.warm, bold = true })
  set("@markup.link", { fg = p.accent_alt })
  set("@markup.raw", { fg = p.text_soft })

  -- LSP / diagnostics -------------------------------------------------
  set("DiagnosticError", { fg = p.red })
  set("DiagnosticWarn", { fg = p.warm })
  set("DiagnosticInfo", { fg = p.accent_alt })
  set("DiagnosticHint", { fg = p.text_muted })
  underline("DiagnosticUnderlineError", p.red)
  underline("DiagnosticUnderlineWarn", p.warm)
  underline("DiagnosticUnderlineInfo", p.accent_alt)
  underline("DiagnosticUnderlineHint", p.text_muted)
  set("DiagnosticVirtualTextError", { fg = p.red, bg = p.bg1 })
  set("DiagnosticVirtualTextWarn", { fg = p.warm, bg = p.bg1 })
  set("DiagnosticVirtualTextInfo", { fg = p.accent_alt, bg = p.bg1 })
  set("DiagnosticVirtualTextHint", { fg = p.text_muted, bg = p.bg1 })
  set("LspReferenceText", { bg = p.bg3 })
  set("LspReferenceRead", { bg = p.bg3 })
  set("LspReferenceWrite", { bg = p.bg3 })

  -- Diff ------------------------------------------------------------------
  set("DiffAdd", { bg = p.diff_add })
  set("DiffDelete", { fg = p.text_faint, bg = p.diff_delete })
  set("DiffChange", { bg = p.diff_change })
  set("DiffText", { bg = p.diff_text, bold = true })
  set("diffAdded", { fg = p.accent })
  set("diffRemoved", { fg = p.red })
  set("diffChanged", { fg = p.accent_alt })

  -- Plugins -----------------------------------------------------------
  set("GitSignsAdd", { fg = p.accent })
  set("GitSignsChange", { fg = p.accent_alt })
  set("GitSignsDelete", { fg = p.red })

  set("TelescopeNormal", { fg = p.text_normal, bg = p.bg1 })
  set("TelescopeBorder", { fg = p.border, bg = p.bg1 })
  set("TelescopeSelection", { fg = p.text_normal, bg = p.bg3 })
  set("TelescopeMatching", { fg = p.accent, bold = true })

  set("NvimTreeNormal", { fg = p.text_normal, bg = p.bg1 })
  set("NvimTreeFolderName", { fg = p.accent_alt })
  set("NvimTreeRootFolder", { fg = p.accent, bold = true })

  set("WhichKey", { fg = p.accent_alt })
  set("WhichKeyGroup", { fg = p.violet })
  set("WhichKeyDesc", { fg = p.text_normal })
  set("WhichKeySeparator", { fg = p.text_faint })
  set("WhichKeyFloat", { bg = p.bg1 })
  set("WhichKeyBorder", { fg = p.border, bg = p.bg1 })

  set("LazyNormal", { fg = p.text_normal, bg = p.bg1 })

  -- :terminal ANSI palette + cursor --------------------------------------
  local ansi_order = {
    "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white",
    "brblack", "brred", "brgreen", "bryellow", "brblue", "brmagenta", "brcyan", "brwhite",
  }
  for i, name in ipairs(ansi_order) do
    vim.g["terminal_color_" .. (i - 1)] = p.ansi[name]
  end
  vim.g.terminal_color_background = p.bg0
  vim.g.terminal_color_foreground = p.text_normal
  set("TermCursor", { fg = p.text_on_accent, bg = p.accent })
  set("TermCursorNC", { fg = p.text_on_accent, bg = p.text_faint })
end

return M
