#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#RSA in Python by Antoni Szymanski 2021
#License: Freeware
#**************************************

import pyglet,time

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '?', "'", '!', '/', '(', ')', '&', ':', ';', '=', '+', '-', '_', '"', '$', '@', '¿', '¡', 'Ą', 'Ć', 'Ę', 'Ł', 'Ń', 'Ó', 'Ś', 'Ź', 'Ż', ' ']
morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '.-.-.-', '--..--', '..--..', '.----.', '-.-.--', '-..-.', '-.--.', '-.--.-', '.-...', '---...', '-.-.-.', '-...-', '.-.-.', '-....-', '..--.-', '.-..-.', '...-..-', '.--.-.', '..-.-', '--...-', '.-.-', '-.-..', '..-..', '.-..-', '--.--', '---.', '...-...', '--..-.', '--..-', '/']

def play(file):
    music = pyglet.resource.media(file)
    music.play()
    pyglet.app.exit()

def slownika(key):
    return morse_code[alphabet.index(key)]

def slownikb(key):
    return alphabet[morse_code.index(key)]

def coder(txt):
    txt = txt.upper()
    morse = ''
    for x in txt:
        if x in alphabet:
            morse += slownika(x) + ' '
        else:
            morse += '<CHR>'
    return morse.strip()

def decoder(morse):
    morselist = morse.split(' ')
    txt = ''
    for x in morselist:
        if x in morse_code:
            txt += slownikb(x)
        elif x == '':
            pass
        else:
            txt += '<CNF>'
    return txt
    
def morseplay(morse):
    times = 0
    for x in morse:
        if x == '.':
            play('dot.mp3')
            time.sleep(0.2)
            times += 0.2
        elif x == '-':
            play('line.mp3')
            time.sleep(0.4)
            times += 0.4
        elif x == '/':
            time.sleep(0.7)
            times += 0.7
        times = rounding_numbers(times*10)/10
    print('It took time to restore the signal:',times,'seconds.')

def rounding_numbers(n):
    n2 = int(n)
    n3 = n - n2
    if n3 >= 0.5:
        n2 += 1
    return n2
    
def main():
    print('Morse coder and decoder by Antoni Szymanski 2021')
    print('License: Freeware')
    print('**************************************')
    txt = input('Enter the text to code/decode ')
    code = 1
    output = ''
    for x in alphabet:
        if not x in txt:
            code = 0
            break
    if code == 0:
        output = decoder(txt)
        print('Your text to encoding is:',txt)
        print('Your text encoding is:',output')
    else:
        output = coder(txt)
        print('Your text to coding is:',txt)
        print('Your text coding is:',output')
    print('\n**************************************')
    print('Thanks for using my script')
    print('The next ones are coming soon')

main()