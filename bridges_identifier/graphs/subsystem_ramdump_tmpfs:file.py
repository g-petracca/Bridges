import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('subsystem_ramdump','subsystem_ramdump')
G.edge['subsystem_ramdump']['subsystem_ramdump']['write-read'] = '[write read]'
G.edge['subsystem_ramdump']['subsystem_ramdump']['fill'] = 'red'
app = Viewer(G)
app.mainloop()