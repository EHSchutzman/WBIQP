import os


def main():

    rootDir = './RawWBData/'

    rootDir = './RawWBData/'
    directories = []  # directories is a 3d array containing all of the days in the collected data
    for dirName, subdirList, fileList in os.walk(rootDir):
        print(dirName)
        print("\t", subdirList)
        for fname in sorted(fileList):
            print("\t\t",dirName + "/" + fname)

if __name__ =="__main__":
    main()