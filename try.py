import re
regex ="^[a-zA-Z]*$"
if not re.match(regex, "H1arsga"):
    print("Error")
else:
    print("Success")