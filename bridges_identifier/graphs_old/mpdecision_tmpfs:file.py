import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read]'
G.edge['mpdecision']['mpdecision']['fill'] = 'red'
app = Viewer(G)
app.mainloop()