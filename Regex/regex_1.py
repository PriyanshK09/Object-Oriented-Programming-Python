import re

value = "This is a test string"
output = re.search("^This. *string$", value)
print(output)

# ====================