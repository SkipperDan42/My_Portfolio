# This code needs to be used with a micro:bit on the micro:bit website.

from microbit import *
import music


for i in range(2):
    music.play(['C4:4', 'C5:12', 'B4:4', 'C5:2', 'C5:2','R', 'A4:4', 'A#4:2', 'A#4', 'A#4', 'A#4', 'A#4', 'A#4', 'C5', 'A4:4', 'A4', 'R:2'])

for i in range(2):
    music.play(['D4:4', 'D4:2', 'G4:3', 'A#4:2', 'D5', 'R','C4:4', 'C4:2', 'E4:3', 'F4:2', 'G4', 'R'])

music.play(['C4', 'C4:3', 'A#4:4', 'A4:2', 'G4:3','R:1', 'F4:5'])
