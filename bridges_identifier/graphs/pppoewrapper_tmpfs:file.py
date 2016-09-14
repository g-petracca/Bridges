import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('pppoewrapper','pppoewrapper')
G.edge['pppoewrapper']['pppoewrapper']['write-read'] = '[write read]'
G.edge['pppoewrapper']['pppoewrapper']['fill'] = 'red'
app = Viewer(G)
app.mainloop()