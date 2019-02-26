# coding: latin-1
###############################################################################
# eVotUM - Electronic Voting System
#
# verifySignature-app.py
#
# Cripto-7.4.1 - Commmad line app to exemplify the usage of verifySignature
#       function (see eccblind.py)
#
# Copyright (c) 2016 Universidade do Minho
# Developed by André Baptista - Devise Futures, Lda. (andre.baptista@devisefutures.com)
# Reviewed by Ricardo Barroso - Devise Futures, Lda. (ricardo.barroso@devisefutures.com)
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
###############################################################################
"""
Command line app that receives signer's public key from file and Data, Signature, Blind Components and
prComponents from STDIN and writes a message to STDOUT indicating if the signature is valid..
"""

import sys
from eVotUM.Cripto import eccblind
from eVotUM.Cripto import utils

def printUsage():
    print("Usage: python verify-app.py -cert <Subscriber certificate> -msg <Original message> -sDash <Signature> -f <Applicant's file>")

def parseArgs():
    if (len(sys.argv) < 9 or sys.argv[1] != "-cert" or sys.argv[3] != "-msg" or sys.argv[5] != "-sDash" or sys.argv[7] != "-f"):
        printUsage()
    else:
        eccPublicKeyPath = sys.argv[2]
        main(eccPublicKeyPath)

def showResults(errorCode, validSignature):
    print("\nOutput")
    if (errorCode is None):
        if (validSignature):
            print("Valid signature")
        else:
            print("Invalid signature")
    elif (errorCode == 1):
        print("Error: it was not possible to retrieve the public key")
    elif (errorCode == 2):
        print("Error: pR components are invalid")
    elif (errorCode == 3):
        print("Error: blind components are invalid")
    elif (errorCode == 4):
        print("Error: invalid signature format")
    print("")

def main(eccPublicKeyPath):
    pemPublicKey = utils.readFile(eccPublicKeyPath)
    data = sys.argv[4]
    signature = sys.argv[6]
    fileData = dict()
    with open("reqFile.txt") as raw_data:
        for item in raw_data:
            if ':' in item:
                key,value = item.split(':', 1)
                fileData[key]=value
            else:
                pass # deal with bad lines of text here
    blindComponents = fileData["blindComponents"]
    pRComponents = fileData["pRComponents"]
    errorCode, validSignature = eccblind.verifySignature(pemPublicKey, signature, blindComponents, pRComponents, data)
    showResults(errorCode, validSignature)

if __name__ == "__main__":
    parseArgs()
