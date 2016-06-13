#pico 8 compiler

This is a proof of concept for a compiler script for the Pico 8 fantasy console

Pico-8
http://www.lexaloffle.com/pico-8.php

### Dependencies
Requires watchdog
https://pypi.python.org/pypi/watchdog

###Use it like this
python picocompiler.py --folder 'folder for scripts' --output 'valid pico-8 file' -r

Put lua files inside of the defined folder and a valid p8 file generated from Pico 8. The compiler should allow you to edit your graphics, sounds and maps separately, but it's not two-way and always keep a backup!!!

Just let it run while you edit the files. If the p8 file doesn't generate at first, try saving a .lua file in the designated folder. You should get a confirmation that a file changed in the terminal log.

### Disclaimer

I am not responsible for any lost carts this may result in. Please keep frequent backups or use version control while using this compiler. This script replaces all of the text between '__lua__' and '__gfx__' on compile, so you will lose any edits made inside of the Pico-8 text editor.

## Future Plans
- Auto-generate p8 file when no valid one is given
- Merge images and sounds inside folder
- Two-way script editing
- Better formatting
- Show char, token, and space counts in compiler
