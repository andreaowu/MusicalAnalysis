#!/usr/bin/python

keyToSignature = {}

# Sharp keys going around circle of fifths
keyToSignature['C major'] = ['0', 0]
keyToSignature['a minor'] = ['0', 9]
keyToSignature['G major'] = ['1#', 7]
keyToSignature['e minor'] = ['1#', 4]
keyToSignature['D major'] = ['2#', 2]
keyToSignature['b minor'] = ['2#', 11]
keyToSignature['A major'] = ['3#', 9]
keyToSignature['f# minor'] = ['3#', 6] 
keyToSignature['E major'] = ['4#', 4]
keyToSignature['g# minor'] = ['4#', 8]
keyToSignature['B major'] = ['5#', 11]
keyToSignature['g# minor'] = ['5#', 8]
keyToSignature['F# major'] = ['6#', 6] 
keyToSignature['d# minor'] = ['6#', 3] 
keyToSignature['C# major'] = ['7#', 1] 
keyToSignature['a# minor'] = ['7#', 10] 

# Flat keys going around circle of fourths
keyToSignature['Cb major'] = ['7b', 11]
keyToSignature['ab minor'] = ['7b', 8]
keyToSignature['Gb major'] = ['6b', 6]
keyToSignature['eb minor'] = ['6b', 3]
keyToSignature['Db major'] = ['5b', 1]
keyToSignature['bb minor'] = ['5b', 10]
keyToSignature['Ab major'] = ['4b', 8]
keyToSignature['f minor'] = ['4b', 5]
keyToSignature['Eb major'] = ['3b', 3]
keyToSignature['c minor'] = ['3b', 0]
keyToSignature['Bb major'] = ['2b', 10]
keyToSignature['g minor'] = ['2b', 7]
keyToSignature['F major'] = ['1b', 5]
keyToSignature['d minor'] = ['1b', 2]

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

class Mapping:
    def __init__(self, key):
        self.mapper = {}
        self.key = key
        self.keySig = keyToSignature[key][0]
        self.offset = keyToSignature[key][1]
        if self.keySig == 0 or self.keySig[1] == '#':
            self.mapper['C'] = self.calculateIndex(0)
            self.mapper['B#'] = self.calculateIndex(0)
            self.mapper['C#'] = self.calculateIndex(1)
            self.mapper['D'] = self.calculateIndex(2)
            self.mapper['D#'] = self.calculateIndex(3)
            self.mapper['E'] = self.calculateIndex(4)
            self.mapper['F'] = self.calculateIndex(5)
            self.mapper['F#'] = self.calculateIndex(6)
            self.mapper['G'] = self.calculateIndex(7)
            self.mapper['G#'] = self.calculateIndex(8)
            self.mapper['A'] = self.calculateIndex(9)
            self.mapper['A#'] = self.calculateIndex(10)
            self.mapper['B'] = self.calculateIndex(11)
        else:
            self.mapper['C'] = self.calculateIndex(0)
            self.mapper['Db'] = self.calculateIndex(1)
            self.mapper['D'] = self.calculateIndex(2)
            self.mapper['Eb'] = self.calculateIndex(3)
            self.mapper['E'] = self.calculateIndex(4)
            self.mapper['Fb'] = self.calculateIndex(4)
            self.mapper['F'] = self.calculateIndex(5)
            self.mapper['Gb'] = self.calculateIndex(6)
            self.mapper['G'] = self.calculateIndex(7)
            self.mapper['Ab'] = self.calculateIndex(8)
            self.mapper['A'] = self.calculateIndex(9)
            self.mapper['Bb'] = self.calculateIndex(10)
            self.mapper['B'] = self.calculateIndex(11)
            self.mapper['Cb'] = self.calculateIndex(11)

    def calculateIndex(self, orig):
        if orig - self.offset >= 0:
            return orig - self.offset
        else:
            return 12 + (orig - self.offset)

    def getMapper(self):
        return self.mapper
    
    def getRoman(self):
        return chordToRoman
