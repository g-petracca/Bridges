import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('vpnclientd','vpnclientd')
G.edge['vpnclientd']['vpnclientd']['write-read'] = '[add_name search]'
app = Viewer(G)
app.mainloop()