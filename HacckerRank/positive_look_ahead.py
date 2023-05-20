Regex_Pattern = r'o(?=oo)'	# Do not delete 'r'.

import re

def input():
  return "gooooo!"

match = re.findall(Regex_Pattern, input())

print("Number of matches :", len(match), match)