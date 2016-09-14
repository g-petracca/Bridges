import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('playready','playready')
G.edge['playready']['playready']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['playready']['playready']['fill'] = 'red'
app = Viewer(G)
app.mainloop()