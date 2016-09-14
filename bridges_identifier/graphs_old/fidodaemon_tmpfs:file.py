import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('fidodaemon','fidodaemon')
G.edge['fidodaemon']['fidodaemon']['write-read'] = '[write read]'
G.edge['fidodaemon']['fidodaemon']['fill'] = 'red'
app = Viewer(G)
app.mainloop()