import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('secure_storage','secure_storage')
G.edge['secure_storage']['secure_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['secure_storage']['secure_storage']['fill'] = 'red'
app = Viewer(G)
app.mainloop()