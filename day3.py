"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

    > delivers presents to 2 houses: one at the starting location, and one to the east.
    ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
    ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

--- Part Two ---

The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

    ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
    ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
    ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

"""

from collections import defaultdict

def make_moves(directions):
  houses = defaultdict(lambda: 0)
  x0, y0 = 0, 0
  houses[(x0,y0)] += 1
  for move in directions:
    if move is '>':
      x0 += 1
    elif move is '<':
      x0 -= 1
    elif move is 'v':
      y0 += 1
    else:
      y0 -= 1
    houses[(x0,y0)] += 1
  return houses
  
with open('data/day3.txt', 'r') as file:
  # read directions from file into list
  directions = map(str, file.read())
  # --- Part 1 ---
  houses = make_moves(directions)
  # find where in the grid the houses have value >= 1  
  number_of_houses = len(filter(lambda presents: presents >= 1, houses.values()))
  print 'The number of houses receiving at least one present is: ', number_of_houses
  # --- Part 2 ---
  santa_directions = [item for item in directions[::2]]
  robosanta_directions = [item for item in directions[1::2]]
  # find where in the grid the houses have value >= 1  
  santa_houses = make_moves(santa_directions)
  robosanta_houses = make_moves(robosanta_directions)
  # combine houses so duplicates are removed 
  # (number of presents will not be correct but that doesn't matter for filter)
  houses = santa_houses.copy()
  houses.update(robosanta_houses)
  # find how many houses in the grid have more than one present 
  number_of_houses = len(filter(lambda presents: presents >= 1, houses.values()))
  print 'The number of houses receiving at least one present is: ', number_of_houses  
  
