# https://www.hackerrank.com/challenges/matching-same-text-again-again/problem?isFullScreen=true

Regex_Pattern = r'^\d\d(-?)\d\d\1\d\d\1\d\d$'	# Do not delete 'r'.

import re

def input():
  return "ab #1?AZa$ab #1?AZa$"

print(str(bool(re.search(Regex_Pattern, input()))).lower())