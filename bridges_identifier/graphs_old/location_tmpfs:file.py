import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('location','location')
G.edge['location']['location']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][write read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['location']['location']['fill'] = 'red'
app = Viewer(G)
app.mainloop()