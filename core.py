#!/usr/bin/python
from music21 import *
from music21 import corpus
from mapping import *
	
def generateFiguredBass(piece):
    key = piece.analyze('key')
    print key
    map = Mapping(str(key)).getMapper()
    print map
    numMeasures = len(piece.getElementsByClass('Part')[0].getElementsByClass('Measure'))
    figuredBass = []
    # goes through every measure
    for measure in range(1, numMeasures + 1):
        print measure
        getParts = piece.parts[0:len(piece.parts)].measures(measure, measure)
        getParts.show('text')
        for item in getParts:
            if type(item) is stream.Measure:
                st = item.notes
                st.show('text')
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
                            chord.append(elemName)
                            if num == len(st) - 1 and len(chord) != 0:
                                print(chord)
                                analyze(chord)
                        elif found == 1:
                            found = 0
                            print(chord)
                            analyze(chord)
                            break
        
def analyze(chord):
    
	print "hello world"	

generateFiguredBass(corpus.parse('bach/bwv7.7'))

