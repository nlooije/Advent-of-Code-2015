"""
--- Day 2: I Was Told There Would Be No Math ---

The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

For example:

    A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
    A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.

All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

--- Part Two ---

The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

For example:

    A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
    A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.

How many total feet of ribbon should they order?

"""

import re

def wrapping_surface_area(l, w, h):
  return 2*l*w + 2*w*h + 2*h*l

def surface_area_smallest_side(l, w, h):
  return min([l*w, w*h, h*l])

def ribbon_length_smallest_side(l, w, h):
  smallest_side = surface_area_smallest_side(l, w, h)
  if l*w == smallest_side:
    return 2*l + 2*w
  elif l*h == smallest_side:
    return 2*l + 2*h
  else:
    # remaining side
    return 2*w + 2*h

def ribbon_length_bow(l, w, h):
  return l*w*h

with open('data/day2.txt', 'r') as file:
  total_wrapping_surface_area = 0
  total_ribbon_and_bow_length = 0
  # Naively loop over all dimensions
  for dimensions in file:
    # convert dimensions of type 'str' ('lxwxh') to list of type 'int' ([l,w,h])
    lwh = map(int, re.findall('\d+', dimensions))
    total_wrapping_surface_area += wrapping_surface_area(*lwh)
    total_wrapping_surface_area += surface_area_smallest_side(*lwh)
    total_ribbon_and_bow_length += ribbon_length_smallest_side(*lwh)
    total_ribbon_and_bow_length += ribbon_length_bow(*lwh)

print 'Total square feet of wrapping paper they should order: ', total_wrapping_surface_area 
print 'Total feet of ribbon they should order: ', total_ribbon_and_bow_length