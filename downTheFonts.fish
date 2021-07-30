#!/bin/fish
function downTheFonts -d "Downloads all the fonts you will ever need"
    sudo dnf search fonts > fonts.text
    python3 main.py
    fish command.txt
end

downTheFonts
