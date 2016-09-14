import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('install_recovery','install_recovery')
G.edge['install_recovery']['install_recovery']['write-read'] = '[write read]'
G.edge['install_recovery']['install_recovery']['fill'] = 'red'
app = Viewer(G)
app.mainloop()