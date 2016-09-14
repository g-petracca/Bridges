import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('clatd','clatd')
G.edge['clatd']['clatd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][write read][write read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['clatd']['clatd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()