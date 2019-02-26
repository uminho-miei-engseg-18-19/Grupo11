"""
Command line app that writes initComponents and pRDashComponents to STDOUT.
"""

import sys
import os
from eVotUM.Cripto import eccblind

def printUsage():
    print("Usage: \"python init-app.py -init\" to init components")

def parseArgs():
    if ((len(sys.argv) == 2 and sys.argv[1] != "-init") or len(sys.argv) > 2):
		printUsage()
    else:
        main()

def main():
    if (len(sys.argv) == 2):
        initComponents, pRDashComponents = eccblind.initSigner()
        with open("sigFile.txt", 'w') as f:
            f.write('%s:%s\n' % ("initComponents", initComponents))
            f.write('%s:%s\n' % ("pRDashComponents", pRDashComponents))
    else:
        print("\nOutput")
        if(os.path.isfile('./sigFile.txt')):
            fileData = dict()
            with open("sigFile.txt") as raw_data:
                for item in raw_data:
                    if ':' in item:
                        key,value = item.split(':', 1)
                        fileData[key]=value
                    else:
                        pass # deal with bad lines of text here
            print("pRDashComponents: " + fileData["pRDashComponents"])
        else:
            print("Init components first: python init-app.py -init")
            print("")
if __name__ == "__main__":
    parseArgs()
