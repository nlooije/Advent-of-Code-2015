"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

For example:

    ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
    aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
    jchzalrnumimnmhp is naughty because it has no double letter.
    haegwjzuvuyypxyu is naughty because it contains the string xy.
    dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?

--- Part Two ---

Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

    It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

For example:

    qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
    xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
    uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
    ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

How many strings are nice under these new rules?

"""

import re

# --- Part 1 ---
def check_nosubstrings(line):
  # check if substrings do not contain the strings 'ab', 'cd', 'pq', or 'xy'
  for substr in ['ab', 'cd', 'pq', 'xy']:
    # if match for substring return False
    cond = False if re.search(substr, line) else True
    # if cond is False, return False
    if not cond:
      return False
  return True

def check_threevowels(line):
  # check if string contains at least three vowels
  nvowels = 0
  for vowel in ['a','e','i','o','u']:
    # check for matching vowel
    matches = re.findall(vowel, line)
    # if any matches add number of matches
    nvowels += len(matches) if matches else 0
    # if atleast 3 vowels, return True
    if nvowels >= 3:
      return True
  return False

def check_doubleletters(line):
  # check if any letters occur more than once
  regexp = re.compile(r'(.)\1') # use a backreference
  match = re.search(regexp, line)
  return True if match else False

# --- Part 2 ---  
def check_pairtwoletters(line):
  # extract string to list
  l = map(str, line)
  # create permutation list of every two characters
  l = [''.join(l[n:n+2]) for n in xrange(len(l)-1)]
  for i, p in enumerate(l):
    # If permutation is in rest of permutation list, return True
    if p in l[i+2:]:
      return True
  return False

def check_repeatoneletter(line):
  # extract string to list
  l = map(str, line)
  for i, s in enumerate(l):
    # If char is the same as its next-neighbor, return True
    try:
      if s == l[i+2]:
        return True
    # catch error at end of list
    except IndexError:
      return False

# --- Common ---
def check_niceness(line, part):
  if part == 1:
    return (check_nosubstrings(line) and 
            check_threevowels(line) and 
            check_doubleletters(line))
  elif part == 2:
    return (check_pairtwoletters(line) and
            check_repeatoneletter(line))

test = False
if test:
  print 'testing: Part 1...'
  for line in ['ugknbfddgicrmopn', 'aaa', 'jchzalrnumimnmhp', 
               'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']:
    print line + ' is nice: ', check_niceness(line, part=1)

  print 'testing: Part 2...'
  for line in ['qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 
               'ieodomkazucvgmuy']:
    print line + ' is nice: ', check_niceness(line, part=2)

with open('data/day5.txt', 'r') as file:
  number_p1 = 0 
  number_p2 = 0 
  for line in file:
    number_p1 += 1 if check_niceness(line, part=1) else 0
    number_p2 += 1 if check_niceness(line, part=2) else 0
  print 'Part 1 - The number of nice strings is: ', number_p1
  print 'Part 2 - The number of nice strings is: ', number_p2