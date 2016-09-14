import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('imscm','imscm')
G.edge['imscm']['imscm']['write-read'] = '[open open][write read][append read][write read]'
G.edge['imscm']['imscm']['fill'] = 'red'
app = Viewer(G)
app.mainloop()