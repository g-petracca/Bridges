import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('cs','cs')
G.edge['cs']['cs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['cs']['cs']['fill'] = 'red'
app = Viewer(G)
app.mainloop()