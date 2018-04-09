import re
x = 'Hello Gokhan. How r u? R u 45 years old? I am 40'
print(x)
y = re.findall('[0-9]+', x)
tot = re.search('[0-9]+', x)

print(y)
x1 = 'From: Using the : character'
y1 = re.findall('^F.+?:', x1)
print(y1)

x2 = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y2 = re.findall('\S+?@\S+', x2)
print(y2)
