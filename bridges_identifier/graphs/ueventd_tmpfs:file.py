import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][relabelto relabelfrom][open open][write read][append read][write read]'
G.edge['ueventd']['ueventd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()