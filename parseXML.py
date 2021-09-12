#!/usr/bin/python3
from typing import Deque
from xml.dom.minidom import parse, parseString
from midi2audio import FluidSynth

def is_rest(note):
    return len(note.getElementsByTagName("rest")) > 0

dom = parse("/Users/nitinpendekanti/Desktop/new.musicxml")

notes = dom.getElementsByTagName("note")

notes = filter(lambda note: not is_rest(note), notes)

intervalsArr = []
notesArr = []
alterArr = []
durationArr = []

for note in notes:
    stepNode = note.getElementsByTagName("step")[0]
    notesArr.append(str(stepNode.childNodes[0].nodeValue))

    stepNode = note.getElementsByTagName("octave")[0]
    intervalsArr.append(str(stepNode.childNodes[0].nodeValue))

    alters = note.getElementsByTagName("alter")
    if len(alters) == 0:
        alterArr.append('0')
    else:
        alterArr.append(str(alters[0].childNodes[0].nodeValue))
    
    stepNode = note.getElementsByTagName("duration")[0]
    durationArr.append(str(stepNode.childNodes[0].nodeValue))

totalNotesArr = []

for i in range(len(notesArr)):
    totalNotesArr.append([notesArr[i], intervalsArr[i], alterArr[i], durationArr[i]])

# for note in totalNotesArr:
#     print(note)

#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file: main.py

# u2800 - u283F
unibase = ['280', '281', '282', '283']
uniend = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
ordered_unicodes = [chr(int(''.join(['0x', j, i]),0)) for j in unibase for i in uniend]

# 64 symbols
brailles = ['⠙','⠹','⠝','⠽',    # C1-8
            '⠑','⠱','⠕','⠵',    # D1-8
            '⠋','⠫','⠏','⠯',    # E1-8
            '⠛','⠻','⠟','⠿',    # F1-8
            '⠓','⠳','⠗','⠷',    # G1-8
            '⠊','⠪','⠎','⠮',    # A1-8
            '⠚','⠺','⠞','⠾',    # B1-8
            '⠈','⠘','⠸','⠐','⠨','⠰','⠠'    # Octave Marks
            '⠣','','⠩']           # Accidental

            # '⠼','⠩','⠄','⠡','⠬','','⠤','','⠌','⠴','⠂','⠆','⠒','⠲','⠢',
            # '⠖','⠶','⠦','⠔','','','⠜','⠈','⠁','⠃','⠉','⠅',
            # '⠇','⠍','','⠥','⠧','⠭','','']

# corresponding unicodes for Braille symbols
unicodes = [u'\u2800',u'\u282e',u'\u2810',u'\u283c',u'\u282b',u'\u2829',u'\u282f',u'\u2804',
            u'\u2837',u'\u283e',u'\u2821',u'\u282c',u'\u2820',u'\u2824',u'\u2828',u'\u280c',
            u'\u2834',u'\u2802',u'\u2806',u'\u2812',u'\u2832',u'\u2822',u'\u2816',u'\u2836',
            u'\u2826',u'\u2814',u'\u2831',u'\u2830',u'\u2823',u'\u283f',u'\u281c',u'\u2839',
            u'\u2808',u'\u2801',u'\u2803',u'\u2809',u'\u2819',u'\u2811',u'\u280b',u'\u281b',
            u'\u2813',u'\u280a',u'\u281a',u'\u2805',u'\u2807',u'\u280d',u'\u281d',u'\u2815',
            u'\u280f',u'\u281f',u'\u2817',u'\u280e',u'\u281e',u'\u2825',u'\u2827',u'\u283a',
            u'\u282d',u'\u283d',u'\u2835',u'\u282a',u'\u2833',u'\u283b',u'\u2818',u'\u2838']


# corresponding bitwise matrix for Braille symbols
matrixcodes = [
    [[0, 0], [0, 0], [0, 0]],[[0, 1], [1, 0], [1, 1]],[[0, 0], [0, 1], [0, 0]],[[0, 1], [0, 1], [1, 1]],
    [[1, 1], [1, 0], [0, 1]],[[1, 1], [0, 0], [0, 1]],[[1, 1], [1, 0], [1, 1]],[[0, 0], [0, 0], [1, 0]],
    [[1, 0], [1, 1], [1, 1]],[[0, 1], [1, 1], [1, 1]],[[1, 0], [0, 0], [0, 1]],[[0, 1], [0, 0], [1, 1]],
    [[0, 0], [0, 0], [0, 1]],[[0, 0], [0, 0], [1, 1]],[[0, 1], [0, 0], [0, 1]],[[0, 1], [0, 0], [1, 0]],
    [[0, 0], [0, 1], [1, 1]],[[0, 0], [1, 0], [0, 0]],[[0, 0], [1, 0], [1, 0]],[[0, 0], [1, 1], [0, 0]],
    [[0, 0], [1, 1], [0, 1]],[[0, 0], [1, 0], [0, 1]],[[0, 0], [1, 1], [1, 0]],[[0, 0], [1, 1], [1, 1]],
    [[0, 0], [1, 0], [1, 1]],[[0, 0], [0, 1], [1, 0]],[[1, 0], [0, 1], [0, 1]],[[0, 0], [0, 1], [0, 1]],
    [[1, 0], [1, 0], [0, 1]],[[1, 1], [1, 1], [1, 1]],[[0, 1], [0, 1], [1, 0]],[[1, 1], [0, 1], [0, 1]],
    [[0, 1], [0, 0], [0, 0]],[[1, 0], [0, 0], [0, 0]],[[1, 0], [1, 0], [0, 0]],[[1, 1], [0, 0], [0, 0]],
    [[1, 1], [0, 1], [0, 0]],[[1, 0], [0, 1], [0, 0]],[[1, 1], [1, 0], [0, 0]],[[1, 1], [1, 1], [0, 0]],
    [[1, 0], [1, 1], [0, 0]],[[0, 1], [1, 0], [0, 0]],[[0, 1], [1, 1], [0, 0]],[[1, 0], [0, 0], [1, 0]],
    [[1, 0], [1, 0], [1, 0]],[[1, 1], [0, 0], [1, 0]],[[1, 1], [0, 1], [1, 0]],[[1, 0], [0, 1], [1, 0]],
    [[1, 1], [1, 0], [1, 0]],[[1, 1], [1, 1], [1, 0]],[[1, 0], [1, 1], [1, 0]],[[0, 1], [1, 0], [1, 0]],
    [[0, 1], [1, 1], [1, 0]],[[1, 0], [0, 0], [1, 1]],[[1, 0], [1, 0], [1, 1]],[[0, 1], [1, 1], [0, 1]],
    [[1, 1], [0, 0], [1, 1]],[[1, 1], [0, 1], [1, 1]],[[1, 0], [0, 1], [1, 1]],[[0, 1], [1, 0], [0, 1]],
    [[1, 0], [1, 1], [0, 1]],[[1, 1], [1, 1], [0, 1]],[[0, 1], [0, 1], [0, 0]],[[0, 1], [0, 1], [0, 1]]
]

# corresponding hexcodes for Braille symbols
hexbase  = ['2', '3', '4', '5']
hexend   = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
hexcodes = [''.join([j, i]) for j in hexbase for i in hexend]

# corresponding ascii codes for Braille symbols
asciicodes = [  'C1', "C2", "C4", "C8", 
                "D1", "D2", "D4", "D8", 
                "E1", "E2", "E4", "E8", 
                "F1", "F2", "F4", "F8", 
                "G1", "G2", "G4", "G8", 
                "A1", "A2", "A4", "A8", 
                "B1", "B2", "B4", "B8",
                "1", "2", "3", "4", "5", "6", "7",
                "-1", "0", "1"]

             '4-5- ','4-5-6-']

def convert(string, toNotation, fromNotation):
    for i in range(len(asciicodes)):
        if string == fromNotation[i]:
            return toNotation[i]

# ascii to braille. currently supporting grade 1 conversion only
# you should use convert function to find out possible translations for braille code:
# convert("⠏⠽⠃⠗⠁⠊⠇⠇⠑⠀⠊⠎⠀⠉⠕⠕⠇⠮", meanings, brailles) OR
# convert("⠏⠽⠃⠗⠁⠊⠇⠇⠑⠀⠊⠎⠀⠉⠕⠕⠇⠮", words, brailles) OR
# convert("⠏⠽⠃⠗⠁⠊⠇⠇⠑⠀⠊⠎⠀⠉⠕⠕⠇⠮", decodings, brailles)
def braille(string):
    return ''.join(convert(string, brailles, asciicodes))

def braille2(string):
    return "Grade 2 conversion not supported yet. you should use convert function to find out translation possibilities for Grade 2."

# braille to ascii
def ascii(string):
    return ''.join(convert(string, asciicodes, brailles))

# braille to matrix
def matrix(string):
    return convert(string, matrixcodes, brailles)

# braille to hex
def hex(string):
    return convert(string, hexcodes, brailles)

# braille to dot
def dot(string):
    return convert(string, dotcodes, brailles)

# helper function for n2braille
# these functions differs from ascii, matrix, hex and dot by taking
# an array of items instead of a string
def convert_list(arr, toNotation, fromNotation):
    return [toNotation[fromNotation.index(c)] for c in arr]

# matrix to braille
def matrix2braille(arr):
    return ''.join(convert_list(arr, brailles, matrixcodes))

# hex to braille
def hex2braille(arr):
    return ''.join(convert_list(arr, brailles, hexcodes))

# dot to braille
def dot2braille(arr):
    return ''.join(convert_list(arr, brailles, dotcodes))

#print(braille("hellos"))
print(braille("B2"))
print(braille("6"))



def parseXML():
    with open("final.brf", "w+", encoding="utf-8") as f:
        measuresCount = 0
        for i in range(len(totalNotesArr)):
            print(braille(str(totalNotesArr[i][0]+totalNotesArr[i][3])))
            f.write(braille(totalNotesArr[i][1]))
            f.write(braille(totalNotesArr[i][2]))
            f.write(braille(totalNotesArr[i][0]+totalNotesArr[i][3]))
            measuresCount += int(totalNotesArr[i][3])
            if(measuresCount % 8 == 0):
                measuresCount = 0
                f.write('\n')
        
