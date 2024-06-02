import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

import re

# Regex pattern for names
name_regex = re.compile(r"^[A-Z][a-zA-Z]*([ '-][A-Z][a-zA-Z]*)*$")

# Regex pattern for phone numbers
phone_regex = re.compile(r"^(\d{10}|\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4})$")

# Regex pattern for email addresses
email_regex = re.compile(r"^[a-zA-Z][\w.]*@[a-zA-Z]+\.[a-zA-Z]+$")
