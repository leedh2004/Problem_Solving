# https://www.hackerrank.com/challenges/backreferences-to-failed-groups/problem?isFullScreen=true

Regex_Pattern = r'^([a-z]\w\s\W\d\D[A-Z]\w[aeiouAEIOU]\S)\1$'	# Do not delete 'r'.

import re

def input():
  return "12-34-56-78"

print(str(bool(re.search(Regex_Pattern, input()))).lower())