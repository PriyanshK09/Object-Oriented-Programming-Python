pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=-])(?=.{8,})"

# Explanation from ChatGPT
# This looks like a regular expression that is used to check if a string meets certain criteria.
# The regular expression is made up of several "lookaheads",
# which are special types of assertions that check for the presence of certain patterns in the string without consuming any characters.
# The first lookahead ((?=.*[a-z])) checks if the string contains at least one lowercase letter.
# The second lookahead ((?=.*[A-Z])) checks if the string contains at least one uppercase letter.
# The third lookahead ((?=.*[!@#$%^&*()_+=-])) checks if the string contains at least one of the special characters listed inside the square brackets. 
# The fourth lookahead ((?=.{8,})) checks if the string is at least 8 characters long.
# Together, these lookaheads ensure that the string contains at least one lowercase letter, one uppercase letter, one special character, and is at least 8 characters long.

# ^ is the start of the string
# ? is the zero or one quantifier
# + Matches the expression to its left 1 or more times.
# * Matches the expression to its left 0 or more times.
# {p} Matches the expression to its left exactly p times.
# {p,q} Matches the expression to its left at least p times, but not more than q times.
# {p,} Matches the expression to its left at least p times.
# {,q} Matches the expression to its left at most q times.
# {,} Matches the expression to its left 0 or more times.
# . Matches any character except a newline.
# .{8,} Matches any character except a newline 8 or more times.
# [a-z] Matches a single character in the range between a and z (case sensitive).
# [A-Z] Matches a single character in the range between A and Z (case sensitive).
# [!@#$%^&*()_+=-] Matches a single character in the list.
# (?=.*[a-z]) Matches any character that is followed by a lowercase letter

# Raw String is a string prefixed with 'r' or 'R'.
# Difference between string and raw string is that raw string doesn't escape any character. 
# It is used to represent the string as it is.