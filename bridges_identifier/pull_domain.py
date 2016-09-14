import os

source = open("./out/allows.out",'r')
dest = open("./out/domains.out",'w')

for line in source:
	fields = line.split();
	dest.write(fields[1]+ '\n')

source.close()
dest.close()

# Sort and remove duplicates
os.system('sort ./out/domains.out > ./out/domains_sorted.out')
os.system('uniq ./out/domains_sorted.out > ./out/domains_unique.out')
os.system('mv ./out/domains_unique.out ./out/domains.out')