import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('sysmon','sysmon')
G.edge['sysmon']['sysmon']['write-read'] = '[write read]'
G.edge['sysmon']['sysmon']['fill'] = 'red'
app = Viewer(G)
app.mainloop()