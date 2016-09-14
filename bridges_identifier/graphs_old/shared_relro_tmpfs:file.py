import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('shared_relro','shared_relro')
G.edge['shared_relro']['shared_relro']['write-read'] = '[open open][write read][add_name search][remove_name search][write read]'
G.edge['shared_relro']['shared_relro']['fill'] = 'red'
app = Viewer(G)
app.mainloop()