import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('mobicoredaemon','mobicoredaemon')
G.edge['mobicoredaemon']['mobicoredaemon']['write-read'] = '[write read]'
G.edge['mobicoredaemon']['mobicoredaemon']['fill'] = 'red'
app = Viewer(G)
app.mainloop()