import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('store_app','store_app')
G.edge['store_app']['store_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['store_app']['store_app']['fill'] = 'red'
app = Viewer(G)
app.mainloop()