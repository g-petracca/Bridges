import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('vpnclientd','vpnclientd')
G.edge['vpnclientd']['vpnclientd']['write-read'] = '[add_name search][write read][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('vpnclientd','vpnclientd')
G.edge['vpnclientd']['vpnclientd']['write-read'] = '[add_name search][write read][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][append read]'
app = Viewer(G)
app.mainloop()