import re


def formatFontLine(line):
    pattern = r':'
    line = re.split(pattern,line)[0]
    return line

def getFonts():
    fileObject = open("fonts.txt", "r")

    fontList = []

    while (True):
        # read next line
        line = fileObject.readline()
        # if line is empty, you are done with all lines in the file
        if not line:
            break

        fontList.append(formatFontLine(line.strip()))

    fileObject.close()

    return fontList

def writeCommandList():
    fontList = getFonts()
    fontList.pop(0)
    outputFile = open("command.txt", "w")
    outputFile.write("sudo dnf install --skip-broken ")

    for font in fontList:
        print(font)
        pattern = r'noarch'

        #texlive is removed due to conflicts with other fonts
        if(re.search(pattern,font) and not re.search(r'texlive',font)):
            outputFile.write(font+" ")


if __name__ == '__main__':
    writeCommandList()
