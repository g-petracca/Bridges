import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('tsdaemon','tsdaemon')
G.edge['tsdaemon']['tsdaemon']['write-read'] = '[write read]'
G.edge['tsdaemon']['tsdaemon']['fill'] = 'red'
app = Viewer(G)
app.mainloop()