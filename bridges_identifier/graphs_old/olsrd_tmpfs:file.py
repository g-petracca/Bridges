import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('olsrd','olsrd')
G.edge['olsrd']['olsrd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['olsrd']['olsrd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()