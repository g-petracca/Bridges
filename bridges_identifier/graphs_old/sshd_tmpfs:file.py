import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('sshd','sshd')
G.edge['sshd']['sshd']['write-read'] = '[write read]'
G.edge['sshd']['sshd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()