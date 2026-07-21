-- Terminal Workbench — palette tokens
-- https://github.com/Real-Fruit-Snacks/terminal-workbench-suite

local M = {}

M.dark = {
  bg0 = "#090c0d",
  bg1 = "#0e1214",
  bg2 = "#13191c",
  bg3 = "#182024",
  bg4 = "#202a2f",
  border = "#2a363d",
  border_strong = "#39484f",

  text_normal = "#dce4df",
  text_soft = "#b4c3bd",
  text_muted = "#879994",
  text_faint = "#63736f",
  text_on_accent = "#07100d",

  accent = "#63f2ab",
  accent_alt = "#6bdcff",
  warm = "#f0c674",
  red = "#ff6e7a",
  orange = "#f7a35c",
  violet = "#b78cff",
  blue = "#74a8ff",

  visual = "#204634",
  selection_terminal = "#1b3a2d",
  search_bg = "#264a56",
  diff_add = "#162e25",
  diff_delete = "#2e1b1d",
  diff_change = "#15252a",
  diff_text = "#2b5562",
  todo_bg = "#2c281c",

  ansi = {
    black = "#202a2f",
    red = "#ff6e7a",
    green = "#63f2ab",
    yellow = "#f0c674",
    blue = "#74a8ff",
    magenta = "#b78cff",
    cyan = "#6bdcff",
    white = "#b4c3bd",
    brblack = "#63736f",
    brred = "#ff7f8a",
    brgreen = "#76f4b5",
    bryellow = "#f2cd85",
    brblue = "#85b2ff",
    brmagenta = "#c09aff",
    brcyan = "#7de0ff",
    brwhite = "#dce4df",
  },
}

M.light = {
  bg0 = "#f5f7f4",
  bg1 = "#edf2ee",
  bg2 = "#e2eae5",
  bg3 = "#d6e1db",
  bg4 = "#c8d5cf",
  border = "#bfcbc5",
  border_strong = "#9daea7",

  text_normal = "#17201d",
  text_soft = "#34443f",
  text_muted = "#60706a",
  text_faint = "#81918a",
  text_on_accent = "#f9fbf8",

  accent = "#007a4d",
  accent_alt = "#006f9e",
  warm = "#a46600",
  red = "#c8324c",
  orange = "#b65800",
  violet = "#7357b8",
  blue = "#2e62b8",

  visual = "#b8d8ca",
  selection_terminal = "#cbe2d8",
  search_bg = "#acceda",
  diff_add = "#d0e4db",
  diff_delete = "#eed9db",
  diff_change = "#d8e7ea",
  diff_text = "#9fc7d6",
  todo_bg = "#e9e1cf",

  ansi = {
    black = "#17201d",
    red = "#c8324c",
    green = "#007a4d",
    yellow = "#a46600",
    blue = "#2e62b8",
    magenta = "#7357b8",
    cyan = "#006f9e",
    white = "#c8d5cf",
    brblack = "#60706a",
    brred = "#b42d44",
    brgreen = "#006e45",
    bryellow = "#945c00",
    brblue = "#2958a6",
    brmagenta = "#684ea6",
    brcyan = "#00648e",
    brwhite = "#f5f7f4",
  },
}

return M
