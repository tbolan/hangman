import re

n = "The ghost that says boo haunts the loo."

m = re.findall(".oo", n)

print(m)
