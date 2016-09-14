import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('hci_attach','hci_attach')
G.edge['hci_attach']['hci_attach']['write-read'] = '[write read]'
G.edge['hci_attach']['hci_attach']['fill'] = 'red'
app = Viewer(G)
app.mainloop()