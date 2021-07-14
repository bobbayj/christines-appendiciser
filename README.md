# christines-appendiciser

Automatically add in appendixes in the bookmarts, made for Christine.

You can build this yourself with `pyinstaller`

Just type `pyinstaller --onefile app.py`

Otherwise, run `app.py` to play around with it yourself!

## Report Folder Hierarchy Requirements

- There must be a folder named `appendix` in the folder containing your main report

- The appendix files must be numbered `A. {name of file}...`

- The main report must have the appendix headers numbered `A. ..., B. ..., etc`.

- The main report must have a table of contents page, with links to the appendix page
