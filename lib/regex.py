import re

my_pattern = r"^\s*([^ ].*\b(?:today|yesterday)\b.*[.?])\s*$"
my_regex = re.compile(my_pattern, re.MULTILINE)