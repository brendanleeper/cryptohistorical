# enigma machine
import random, string

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getalphabetposition(character):
    return string.uppercase.index(character)

def getpositionletter(position):
    return '' + alphabet[position]

class Rotor:
    # each rotor has 26 inputs and 26 outputs
    configuration = ''
    inputs = {}
    outputs = {}
    offset = 0

    def init(self, rotorstring):
        self.configuration = rotorstring
        for i in range(0, len(rotorstring)):
            self.inputs[alphabet[i]] = rotorstring[i]
            self.outputs[rotorstring[i]] = alphabet[i]
        print self.inputs
        print self.outputs
        for k,v in self.inputs.items():
            print '%s:%s' % (self.outputs[self.inputs[k]], self.inputs[k])

    def positionstoalphabet(self):
        output = ''
        derivedalphabet = ''
        for k, v in self.inputs.items():
            output += getpositionletter(v)
            derivedalphabet += getpositionletter(k)
        print derivedalphabet
        print output
        assert output == self.configuration

    def forward(self, position):
        return self.inputs[position]

    def backward(self, letter):
        return self.outputs[letter]

class Reflector:
    def getPath(self):
        return 1

class Scrambler:
    def init(self):
        r = Rotor()
        r.init('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
        result = r.forward('G')
        print result
        print r.backward(result)

class PlugBoard:
    def test(self):
        return 1

class Plug:
    def getConnection(self):
        return 1

class EnigmaIO:
    def test(self):
        return 1

s = Scrambler()
s.init()

# I 	EKMFLGDQVZNTOWYHXUSPAIBRCJ 	1930 	Enigma I
