import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('dhcp','dhcp')
G.edge['dhcp']['dhcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read][write read][write read][write read][write read]'
G.edge['dhcp']['dhcp']['fill'] = 'red'
app = Viewer(G)
app.mainloop()