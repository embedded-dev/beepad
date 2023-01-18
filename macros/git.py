# Macros for 'git' command

from beepad.keymap import TypeAction, NullAction

keymap = {   # REQUIRED dictionary - must be named "keymap"
    'name': "Git",      # Keymap name
    'actions': [        # list of key actions/macros
        #          COLOR     LABEL     KEY SEQUENCE
        # 1st row ----------
        TypeAction(0xff0000, "gst",    "git status\n"),
        TypeAction(0x00ff00, "gc",     "git commit\n"),
        TypeAction(0x0000ff, "gc -m",  "git commit -m @"),
        # 2nd row ----------
        TypeAction(0x0000ff, "gca!",   "git commit --amend\n"),
        TypeAction(0x00ff00, "gd",     "git diff \n"),
        TypeAction(0xff0000, "gd -s",  "git diff --staged\n"),
        # 3rd row ----------
        TypeAction(None,     "ga .",   "git add .\n"),        
        TypeAction(None,     "ggpush", "git push origin $(git rev-parse --abbrev-ref HEAD)\n"),
        TypeAction(None,     "ggpull", "git pull origin $(git rev-parse --abbrev-ref HEAD)\n"),
        # 4th row ----------
        TypeAction(0xff0000, "main",   "git checkout main\n"),
        TypeAction(0x00ff00, "grm",    "git rebase origin/main\n"),
        TypeAction(0x0000ff, "dgt",    "git checkout -b dgt/"),
        # Encoder button ---
        NullAction()
    ]
}
