#!/usr/bin/python

keyToSignature = {}
keyToSignature['a minor'] = '0b'
keyToSignature['a# minor'] = '0b'
keyToSignature['ab minor'] = 'b'
keyToSignature['b'] = 'b'
keyToSignature['bb minor'] = 'b'
keyToSignature[''] = 'b'
keyToSignature['minor'] = 'b'
keyToSignature[''] = 'b'
keyToSignature['minor'] = 'b'
keyToSignature[''] = 'b'
keyToSignature['minor'] = 'b'
keyToSignature[''] = 'b'
keyToSignature['minor'] = 'b'
keyToSignature[''] = 'b'
keyToSignature['C major'] = '0'
keyToSignature['G major'] = '1#'
keyToSignature['D major'] = '2#'
keyToSignature['A major'] = '3#'
keyToSignature['E major'] = '4#'
keyToSignature['B major'] = '5#'
keyToSignature['Cb major'] = '7b'
keyToSignature['F# major'] = '6#'
keyToSignature['Gb major'] = '6b'
keyToSignature['C# major'] = '7#'
keyToSignature['Db major'] = '5b'


class Mapping:
    def __init__(self, note):
        self.mapper = {}
        if len(note) > 1 and note[1] == '#':
            print "sharp"
        else:
            self.mapper['c'] = 1
            self.mapper['c#'] = 2
            self.mapper['d'] = 3
            self.mapper['d#'] = 4
            self.mapper['e'] = 5
            self.mapper['f'] = 6
            self.mapper['f#'] = 7
            self.mapper['g'] = 8
            self.mapper['g#'] = 9
            self.mapper['a'] = 10
            self.mapper['a#'] = 11
            self.mapper['b'] = 12
            print note

    def getMapper(self):
        return self.mapper
    

