import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('androidshmservice','androidshmservice')
G.edge['androidshmservice']['androidshmservice']['write-read'] = '[write read][write read]'
G.edge['androidshmservice']['androidshmservice']['fill'] = 'red'
app = Viewer(G)
app.mainloop()