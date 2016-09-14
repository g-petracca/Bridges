import os


def pull():

	allows = open("./out/allows.out", "w")
	#policy = open("./policy.conf.x86emu", "r")
	policy = open("./policy.conf.zeroflte", "r")

	# Copy out all allow rules	
	for line in policy:
		if line.startswith("allow ") and line.endswith(";\n"): # Ignore malformed rules
			allows.write(line)
	allows.close()
	
	# Sort and remove duplicates
	os.system('sort ./out/allows.out > ./out/allows_sorted.out')
	os.system('uniq ./out/allows_sorted.out > ./out/allows_unique.out')
	os.system('mv ./out/allows_unique.out ./out/allows.out')

	# Format Rules to have always 4 fields easy to identify <rule> <sub_domain> <obj_domain> <ops>
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
		dest.write('#')
	    	continue
	    dest.write(ch)
	os.system('mv ./out/allows_parsed.out ./out/allows.out')
	source.close()
	dest.close()

	# Unroll domains
	source = open("./out/allows.out", 'r')
	dest = open("./out/allows_unrolled.out", 'w')
	for line in source:
		if line.startswith("allow ") and line.endswith(";\n"):
			fields = line.split()
			head = fields[0];
			tail = fields[2] + " " + fields[3] +"\n"
			if '#' in fields[1]:
				domains = fields[1].split('#')
				for d in domains:
					if d != '{' and d != '}':
						dest.write(head +' '+ d +' '+tail)	
			else:
				dest.write(head +' '+ fields[1] +' '+ tail)

	os.system('mv ./out/allows_unrolled.out ./out/allows.out')
	source.close()
	dest.close()

	# Unroll objects
	source = open("./out/allows.out", 'r')
	dest = open("./out/allows_unrolled.out", 'w')
	for line in source:
		if line.startswith("allow ") and line.endswith(";\n"):
			fields = line.split()
			#print fields
			head = fields[0] + " " + fields[1]
			tail = fields[3] +"\n"
			#print fields
			if '#' in fields[2]:
				if ':' in fields[2]:
					domain_fields = fields[2].split(':')
					#print domain_fields
					if '#' in domain_fields[0]:
						domains = domain_fields[0].split('#')
						for d in domains:
							if d != '{' and d != '}':
								if '#' in domain_fields[1]:
									domain_classes = domain_fields[1].split('#')
									for c in domain_classes:
										if c != '{' and c != '}':
											dest.write(head +' '+ d +':'+ c +' '+ tail)
								else:
									dest.write(head +' '+ d +':'+ domain_fields[1] +' '+ tail)
			
					else:
						if '#' in domain_fields[1]:
							domain_classes = domain_fields[1].split('#')
							for c in domain_classes:
								if c != '{' and c != '}':
									dest.write(head +' '+ domain_fields[0] +':'+ c +' '+ tail)
						else:
							dest.write(head +' '+ domain_fields[0] +':'+ domain_fields[1] +' '+ tail)
			
			else:
				dest.write(head +' '+ fields[2] +' '+ tail)

	os.system('mv ./out/allows_unrolled.out ./out/allows.out')						
	source.close()
	dest.close()


if __name__ == '__main__':
    pull()


