import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('jackservice','jackservice')
G.edge['jackservice']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['jackservice']['jackservice']['fill'] = 'red'
app = Viewer(G)
app.mainloop()