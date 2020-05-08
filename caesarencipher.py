# Caesar Encipher
# by @stephpirman
#
# Enciphers given a letter or number for the key
# Usage: python3 ./caesarencipher.py [-h] key pt
import argparse

# dictionaries to convert to and from numbers and letters easily with
lettersToNumbers = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,
    'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,
    'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}

numbersToLetters = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',
    9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',
    19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}

# shifts a single character using a shift key
def character_shift(letter, shift):
    position = lettersToNumbers.get(letter)
    return numbersToLetters.get((position + shift)%26)

# shifts the whole plaintext using a single shift key
def shifter(str, shift):
    res = ""
    str = str.upper()
    for let in str:
        res = res + character_shift(let, shift)
    return res

# parses out the arguments
parser = argparse.ArgumentParser(description='Enciphers plaintext using a key '
    + 'and the Caesar cipher.')
parser.add_argument('key', metavar='key', type=str, nargs='+',
    help='an integer (0-25) or a single letter')
parser.add_argument('plaintext', metavar='pt', type=str, nargs='+',
    help='plaintext to be enciphered')
args = parser.parse_args()

# defines the shift based on the passed in key
shift = 0
key = args.key[0]
if (key.isalpha()):
    key = key.upper()
    shift = lettersToNumbers.get(key)
else:
    shift = int(key)

# defines the plaintext based on the passed in pt
plaintext = args.plaintext[0]

# prints the enciphered text
print(shifter(plaintext.upper(),shift))