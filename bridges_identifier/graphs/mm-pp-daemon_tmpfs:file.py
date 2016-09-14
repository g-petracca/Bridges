import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('mm-pp-daemon','mm-pp-daemon')
G.edge['mm-pp-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['mm-pp-daemon']['mm-pp-daemon']['fill'] = 'red'
app = Viewer(G)
app.mainloop()