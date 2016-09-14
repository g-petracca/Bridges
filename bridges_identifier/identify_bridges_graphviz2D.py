import re
import pull_reads
import pull_writes
import pull_neverallows
import pull_allows
import identify_bridging_objs
import functools
import graphviz as gv


graph = functools.partial(gv.Graph, format='png')
digraph = functools.partial(gv.Digraph, format='png')


'''def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            graph.node(n[0], **n[1])
        else:
            graph.node(n)
    return graph

def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1])
        else:
            graph.edge(*e)
    return graph
'''




def identify():

	# Dictionary Construction to map read-to-write

	ops_map = {}

	ops_map["read"] = ["write", "append", "override"]
	ops_map["getattr"] = ["setattr"]
	ops_map["relabelfrom"] = ["relabelto"]
	ops_map["execute"] = ["write", "append"]
	ops_map["recvfrom"] = ["sendto"]
	ops_map["recv_msg"] = ["send_msg"]
	ops_map["unix_read"] = ["unix_write"]
	ops_map["getfocus"] = ["setfocus"]
	ops_map["list_property"] = ["set_property"]
	ops_map["get_property"] = ["set_property"]
	ops_map["quotaget"] = ["quotamod"]
	ops_map["tcp_recv"] = ["tcp_send"]
	ops_map["udp_recv"] = ["udp_send"]
	ops_map["rawip_recv"] = ["rawip_send"]
	ops_map["dccp_recv"] = ["dccp_send"]
	ops_map["ingress"] = ["egress"]
	ops_map["acceptfrom"] = ["connectto"]
	ops_map["getsched"] = ["setsched"]
	ops_map["getpgid"] = ["setpgid"]
	ops_map["getcap"] = ["setcap"]
	ops_map["receive"] = ["send"]
	ops_map["dac_read_search"] = ["dac_override"]
	ops_map["nlmsg_read"] = ["nlmsg_write"]
	ops_map["recv"] = ["send"]
	ops_map["flow_in"] = ["flow_out"]
	ops_map["forward_in"] = ["forward_out"]
	ops_map["select"] = ["update", "insert", "delete"]
	ops_map["execute"] = ["install"]
	ops_map["import"] = ["export"]
	ops_map["search"] = ["add_name", "remove_name"]
	ops_map["get_value"] = ["set_value"]
	ops_map["find"] = ["add"]
	ops_map["list"] = ["add"]
	ops_map["get"] = ["insert", "delete"]
	ops_map["list"] = ["insert", "delete"]
	ops_map["verify"] = ["sign"]
	ops_map["getopt"] = ["setopt"]
	ops_map["manage"] = ["manage"]
	ops_map["open"] = ["open"]
	ops_map["execmod"] = ["open"]

	# CHECK ALSO FOR *


	file_in = open("./out/bridging_objects.out", 'r')
	file_out = open("./out/bridges.out", 'w')


	writes = []
	reads = []
	iswrite = 0
	isread = 0
	intra = 0
	between = 0
	bridges = 0
	graph_name = ''
	#test = 1


	for line in file_in:
		file_out.write(line.replace('#',' ')) # Write all lines from bridging objects
		#print iswrite
		#print isread
		if (line[0].isalpha() or line[0]=='-' or line[0]=='#'): # New bridging object
			
			# Creating a new graph
			#if test == 1:		
			graph_name = line.split(' ', 1)[0]
				#graph = gv.Digraph(comment='graph_name')
			graph = gv.Digraph(comment='graph_name')
								
				#graph.node("A", "A")
				#graph.node("B", "B")
				#graph.edge('A','B')
			writes = []
			reads = []
			iswrite = 0
			isread = 0
			#print line[0]
			continue

		elif "WRITES:" in line:
			isread = 0 # not necessary		
			iswrite = 1
			continue

		elif "READS:" in line:
			iswrite = 0
			isread = 1
			continue
	
		elif ("NEVERALLOWS:"  in line) or ("neverallow" in line):
			#print "NEVER"
			iswrite = 0
			isread = 0
			continue
	
		elif (iswrite == 1):
			writes.append(line)
			continue
	
		elif (isread == 1):
			reads.append(line)
			continue
	
		else:

			
			#print "HERE"
			# Identify Bridiges
			file_out.write("\tBRIDGES:\n")
		
			for read in reads:
				tmp_read = read								
				read_fields = tmp_read.split();
				for key in ops_map:
					if ('#'+key+'#' in read) or (' '+key+';' in read):	
						for write in writes:
							tmp_write = write								
							write_fields = write.split();
							if write_fields[3] == "*;":
								file_out.write("\t\t" + read_fields[0] +" " + read_fields[1] +" " + read_fields[2] +" " + key+ '\n')
								file_out.write("\t\t" + write_fields[0] +" " + write_fields[1] +" " + write_fields[2] +" *" +'\n\n')
								# ADD NODE ONLY IF NOT ALREADY EXISITNG
								#if test == 1 :		
			
								graph.node(read_fields[1])
								graph.node(write_fields[1])
								# ADD EDGE
								graph.edge(write_fields[1],read_fields[1], label="* >"+key)
								

								if read_fields[1] == write_fields[1]:
									intra = intra + 1
								else:
									between = between + 1
								bridges = bridges + 1
							else:						
								for value in ops_map.get(key):
									if  ('#'+value+'#' in write) or (' '+value+';' in write) :								
										file_out.write("\t\t" + read_fields[0] +" " + read_fields[1] +" " + read_fields[2] +" " + key+ '\n')
										file_out.write("\t\t" + write_fields[0] +" " + write_fields[1] +" " + write_fields[2] +" " + value + '\n\n')

										#if test == 1 :		
			
										graph.node(read_fields[1])
										graph.node(write_fields[1])
										# ADD EDGE
										graph.edge(write_fields[1],read_fields[1], label=value+" > "+ key)
								

										if read_fields[1] == write_fields[1]:
											intra = intra + 1
										else:
											between = between + 1
										bridges = bridges + 1
					elif read_fields[3] == "*;":
						for write in writes:
							tmp_write = write								
							write_fields = write.split();
							if write_fields[3] != "*;":
								file_out.write("\t\t" + read_fields[0] +" " + read_fields[1] +" " + read_fields[2] +" *"+ '\n')
								file_out.write("\t\t" + write_fields[0] +" " + write_fields[1] +" " + write_fields[2] +" *"+ '\n\n')
								#if test == 1 :		
			
								graph.node(read_fields[1])
								graph.node(write_fields[1])
								# ADD EDGE
								graph.edge(write_fields[1],read_fields[1], label="* > *")


							else:
								tmp_w = write_fields[3].split("#")
								for value in tmp_w:
									file_out.write("\t\t" + read_fields[0] +" " + read_fields[1] +" " + read_fields[2] +" *"+ '\n')
									file_out.write("\t\t" + write_fields[0] +" " + write_fields[1] +" " + write_fields[2] +" " + value + '\n\n')
									#if test == 1 :		
									graph.node(read_fields[1])
									graph.node(write_fields[1])
									# ADD EDGE
									graph.edge(write_fields[1],read_fields[1], label=value+" > *")									
									
							if read_fields[1] == write_fields[1]:
								intra = intra + 1
							else:
								between = between + 1			
							bridges = bridges + 1
				
			filename = graph.render(filename='img/'+graph_name, view=True)
			#if test == 1 :			
			#filename = graph.render(filename='img/'+graph_name)
				#print filename
		print "running"			
		file_out.write("\n")	
								
	file_out.write("Bridges = " + str(bridges) + "\n")		
	file_out.write("Intra-Domain Bridges = " + str(intra) + "\n")								
	file_out.write("Between-Domain Bridges = " + str(between) + "\n")
	

if __name__ == '__main__':
	pull_allows.pull()
	pull_neverallows.pull()
	pull_reads.pull()
	pull_writes.pull()
	identify_bridging_objs.identify()
	identify()





