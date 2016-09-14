import re

source = open("./out/allows.out", 'r')
dest = open("./out/allows_parsed.out", 'w')

count = 0

while True:
    ch = source.read(1)
    if not ch: break
    if ch == '{':
	count = count + 1
    elif ch == '}':
	count = count - 1
    elif ch == ' ' and count > 0:
	dest.write('*')
    	continue
    dest.write(ch)

source = open("./out/neverallows.out", 'r')
dest = open("./out/neverallows_parsed.out", 'w')

count = 0

while True:
    ch = source.read(1)
    if not ch: break
    if ch == '{':
	count = count + 1
    elif ch == '}':
	count = count - 1
    elif ch == ' ' and count > 0:
	dest.write('*')
    	continue
    dest.write(ch)
#for line in source:
#	print(re.findall(r"\{[^\]]*\}",line)[0])

