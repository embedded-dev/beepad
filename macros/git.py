# Macros for "git" command

from beepad.keymap import TypeAction, NullAction

keymap = {   # REQUIRED dictionary - must be named "keymap"
    "name": "Git",      # Keymap name
    "actions": [        # list of key actions/macros
        #          COLOR     LABEL     KEY SEQUENCE
        # 1st row ----------
        TypeAction(0xff0000, "status", "git status\n"),
        TypeAction(0x00ff00, "commit", "git commit\n"),
        TypeAction(0x0000ff, "cmt-m",  "git commit -m '"),
        # 2nd row ----------
        TypeAction(0x0000ff, "amend!", "git commit --amend\n"),
        TypeAction(0x00ff00, "diff",   "git diff\n"),
        TypeAction(0xff0000, "diff-s", "git diff --staged\n"),
        # 3rd row ----------
        TypeAction(None,     "add .",  "git add .\n"),        
        TypeAction(None,     "push",   "git push origin $(git rev-parse --abbrev-ref HEAD)\n"),
        TypeAction(None,     "pull",   "git pull origin $(git rev-parse --abbrev-ref HEAD)\n"),
        # 4th row ----------
        TypeAction(0xff0000, "main",   "git checkout main\n"),
        TypeAction(0x00ff00, "rebase", "git rebase origin/main\n"),
        TypeAction(0x0000ff, "jeff",   "git checkout -b jeff/"),
        # Encoder button ---
        NullAction()
    ]
}
