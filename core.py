#!/usr/bin/python
from music21 import *
from music21 import corpus
from mapping import *
    
chordToRoman = {}
chordToRoman['0major'] = "I" 
chordToRoman['1major'] = "II"
chordToRoman['2major'] = "III"
chordToRoman['3major'] = "IV"
chordToRoman['4major'] = "V" 
chordToRoman['5major'] = "VI"
chordToRoman['6major'] = "VII"
chordToRoman['0minor'] = "i" 
chordToRoman['1minor'] = "ii"
chordToRoman['2minor'] = "iii"
chordToRoman['3minor'] = "iv"
chordToRoman['4minor'] = "v" 
chordToRoman['5minor'] = "vi"
chordToRoman['6minor'] = "vii"
chordToRoman['0aug'] = "I+"
chordToRoman['1aug'] = "II+"
chordToRoman['2aug'] = "III+"
chordToRoman['3aug'] = "IV+"
chordToRoman['4aug'] = "V+"
chordToRoman['5aug'] = "VI+"
chordToRoman['6aug'] = "VII+"
chordToRoman['0dim'] = "io"
chordToRoman['1dim'] = "iio"
chordToRoman['2dim'] = "iiio"
chordToRoman['3dim'] = "ivo"
chordToRoman['4dim'] = "vo"
chordToRoman['5dim'] = "vio"
chordToRoman['6dim'] = "viio"

def generateFiguredBass(piece):
    f = open('Analysis', 'w')
    key = piece.analyze('key')
    map = Mapping(str(key)).getMapper()
    numMeasures = len(piece.getElementsByClass('Part')[0].getElementsByClass('Measure'))
    figuredBass = []
    # goes through every measure
    for measure in range(1, numMeasures + 1):
        getParts = piece.parts[0:len(piece.parts)].measures(measure, measure)
        for item in getParts:
            if type(item) is stream.Measure:
                st = item.notes
                start = -1 # start here next loo
                # goes through every count 
                for count in range(int(st.lowestOffset), int(st.highestOffset + 1)):
                    found = 0 # stop loop if already came to end of true elems
                    chord = []
                    # goes through minimally every note
                    for num in range(start + 1, len(st)):
                        elem = st[num]
                        if elem.offset == count:
                            elemName = elem.name
                            found = 1
                            start = num
                            chord.append(map.get(elemName))
                            if num == len(st) - 1 and len(chord) != 0:
                                analyze(chord, f)
                        elif found == 1:
                            found = 0
                            analyze(chord, f)
                            break
        
def analyze(chord, f):
    first = chord[len(chord) - 1]
    chord = list(set(chord))
    chord.sort()
    pos = chord.index(first)
    romanNumeral = ""
    if len(chord) == 3:
        diffOne = chordDiff(chord, 0, 1)
        diffTwo = chordDiff(chord, 1, 2)
        if diffOne == 3:
            if diffTwo == 3 or diffTwo == 6:
                romanNumeral = chordToRoman[str(pos) + "dim"]
            elif diffTwo == 4:
                romanNumeral = chordToRoman[str(pos) + "minor"]
            elif diffTwo == 5:
                romanNumeral = chordToRoman[str(pos) + "major"]
        elif diffOne == 4:
            if diffTwo == 3:
                romanNumeral = chordToRoman[str(pos) + "major"]
            elif diffTwo == 4:
                romanNumeral = chordToRoman[str(pos) + "aug"]
            elif diffTwo == 5:
                romanNumeral = chordToRoman[str(pos) + "minor"]
        elif diffOne == 5:
            if diffTwo == 4:
                romanNumeral = chordToRoman[str(pos) + "major"]
            elif diffTwo == 3:
                romanNumeral = chordToRoman[str(pos) + "minor"]
        elif diffOne == 6:
            if diffTwo == 4:
                romanNumeral = chordToRoman[str(pos) + "aug"]
            elif diffTwo == 3:
                romanNumeral = chordToRoman[str(pos) + "dim"]
        if pos == 1:
            romanNumeral += " 6"
        elif pos == 2:
            romanNumeral += " 6 4"

    if len(chord) == 4:
        diffOne = chordDiff(chord, 0, 1)
        diffTwo = chordDiff(chord, 1, 2)
        diffThree = chordDiff(chord, 2, 3)
        if diffOne == 4:
            if diffTwo == 3:
                if diffThree == 4:
                    romanNumeral = "Major V"
                elif diffThree == 3:
                    romanNumeral = "Dom V"
                elif diffThree == 2:
                    romanNumeral = "v"
            elif diffTwo == 2:
                if diffThree == 3:
                    romanNumeral = "Half Dim v"
            elif diffTwo == 1:
                if diffThree == 4:
                    romanNumeral = "Major V"
        elif diffOne == 3:
            if diffTwo == 4:
                if diffThree == 3:
                    romanNumeral = "v"
                elif diffThree == 2:
                    romanNumeral = "Half Dim v"
                elif diffThree == 1:
                    romanNumeral = "Major V"
            elif diffTwo == 3:
                if diffThree == 4:
                    romanNumeral = "v"
                elif diffThree == 3:
                    romanNumeral = "Dim v"
                elif diffThree == 2:
                    romanNumeral = "Dom V"
            elif diffTwo == 2:
                if diffThree == 4:
                    romanNumeral = "Dom V"
        if pos == 1:
            romanNumeral += "7"
        elif pos == 2:
            romanNumeral += " 6 5"
        elif pos == 3:
            romanNumeral += " 4 3"
        elif pos == 4:
            romanNumeral += " 2"
    f.write(chord + ": " + romanNumeral + "\n")

def chordDiff(chord, pos1, pos2):
    return chord[pos2] - chord[pos1]

generateFiguredBass(corpus.parse('bach/bwv7.7'))

