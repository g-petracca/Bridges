import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('samsungpowersoundplay','samsungpowersoundplay')
G.edge['samsungpowersoundplay']['samsungpowersoundplay']['write-read'] = '[write read]'
G.edge['samsungpowersoundplay']['samsungpowersoundplay']['fill'] = 'red'
app = Viewer(G)
app.mainloop()