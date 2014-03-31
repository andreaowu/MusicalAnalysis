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
                                print(chord)
                                analyze(chord)
                        elif found == 1:
                            found = 0
                            print chord
                            analyze(chord)
                            break
        
def analyze(chord):
    first = chord[3]
    chord = list(set(chord))
    chord.sort()
    pos = chord.index(first)
    print pos
    if len(chord) == 3:
        if chord[1] - chord[0] == 3:
            if chord[2] - chord[1] == 3:
                print chordToRoman[str(pos) + "dim"]
            else:
                print chordToRoman[str(pos) + "minor"]
        elif chord[1] - chord[0] == 4:
            if chord[2] - chord[1] == 3:
                print chordToRoman[str(pos) + "major"]
            else:
                print chordToRoman[str(pos) + "aug"]
                


generateFiguredBass(corpus.parse('bach/bwv7.7'))

