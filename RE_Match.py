import re
txt="Use of python in Machine Learning"
x=re.match("^Use.*Machine",txt)
if x:
    print("YES! we have a match!")
else:
    print("No Match")
