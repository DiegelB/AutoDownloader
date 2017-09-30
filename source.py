# wget -i fileNameHere -r -A fileTypeHere -e robots=off --random-wait -U "Mozzila/5.0 Firefox/14.0.1 Chrome/31.0.1"
"""
"\n*****************************"
"\n*                           *"
"\n*                           *"
"\n*                           *"
"\n*                           *"
"\n*****************************"
"\n*****************************"
"\n*Press enter to continue    *"
"\n*(Y/N)?                     *"
"\n*****************************"
"""

import os

# main module that runs all the seperate checks
def main():
    fileCheck()
    linkCheck()
    fileTypeEx = fileTypeCheck()

    clearScreen()
    systemCommand = "wget -i sourceLink.txt" + fileTypeEx + \
                    " -e robots=off --random-wait -U 'Mozzila/5.0 Firefox/14.0.1 Chrome/31.0.1' -nv --progress=dot"

    os.system(systemCommand)
    os.system("find . -type d -empty -delete")


def fileCheck():
    if(os.path.isfile('./sourceLink.txt')):
        pass
    else:
        newFile = open('sourceLink.txt', 'w')
        newFile.write("!!If you see this you need to add your own link!!\n"
                      "!!              to sourceLink.txt              !!")
        newFile.close()

def linkCheck():
    clearScreen()
    print("\n\n")
    print("\n*****************************"
          "\n*Welcome to AutoDownloader  *"
          "\n*                           *"
          "\n*Please make sure you have  *"
          "\n*your link in sourceLink.txt*"
          "\n*                           *"
          "\n*Press enter to continue    *"
          "\n*****************************\n")
    input(">>")
    userBool = False
    while(userBool == False):
        clearScreen()
        print("\n\n")
        print("\n*****************************"
              "\n*Please confirm that this is*"
              "\n*your correct link          *"
              "\n*                           *"
              "\n*(Y/N)?                     *"
              "\n*****************************\n")
        sourceLinkFile = open('sourceLink.txt', 'r')
        sourceLink = sourceLinkFile.read()
        print(sourceLink)
        userInput = input("\n>>")

        if userInput == 'y' or userInput == 'Y':
            userBool = True
        elif userInput == 'n' or userInput == 'N':
            clearScreen()
            print("\n\n")
            print("\n*****************************"
                  "\n*Take the time now to enter *"
                  "\n*your link in sourceLink.txt*"
                  "\n*                           *"
                  "\n*Press enter to continue    *"
                  "\n*****************************\n")
            input(">>")
            pass

def fileTypeCheck():
    userBool = False
    while(userBool == False):
        clearScreen()
        print("\n\n")
        print("\n*****************************"
              "\n*Would you like to add a    *"
              "\n*file type extension?       *"
              "\n*                           *"
              "\n*(Y/N)?                     *"
              "\n*****************************\n")
        userInput = input(">>")

        if userInput == 'y' or userInput == 'Y':
            clearScreen()
            print("\n\n")
            print("\n*****************************"
                  "\n*Pick your file type        *"
                  "\n*                           *"
                  "\n*(I)mg (P)df (M)p3 mp(4)    *"
                  "\n*                           *"
                  "\n*****************************\n")
            fileType = input(">>")
            fileType = fileType.lower()

 
            if fileType == 'i':
                userBool = True
                return " -r -A jpeg,jpg,png,gif"
            elif fileType == 'p':
                userBool = True
                return " -r -A pdf"
            elif fileType == 'm':
                userBool = True
                return " -r -A mp3"
            elif fileType == '4':
                userBool = True
                return " -r -A mp4"
            else:
                clearScreen()
                print("\n\n")
                print("\n*****************************"
                      "\n*You did not enter a correct*"
                      "\n*response                   *"
                      "\n*                           *"
                      "\n*Press enter to continue    *"
                      "\n*****************************\n")
                input(">>")
        elif userInput == 'n' or userInput == 'N':
            userBool = True
            return ""
        
    


def clearScreen():
    os.system("clear")        


main()

