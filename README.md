# Sensehat-Game-of-Life

This is a simple simlation game which works on Sense Hat add-on board for Raspberry Pi. It requires sense_hat module for python. 
The game is based on 3 simple rules

1) If there are no adjacent neighbours to a pixel or if there are more than 3 neighbours to a pixel. The pixel dies.
2) If it has 1 or 3 neighbouring pixels. It might copy itself to an adjacent empty cell.
3) If it has 2 neighbours, it might randomly move to an adjacent empty pixel.
4) Simulation continues until all pixels die.

## How to run?
./gol.py probablity time

probablity = probability that a given cell will initially have a valid pixel. Input of 60 means, probablity is 1/60 for all the pixels.
time = time in seconds after which each iteration of simulation should run.
