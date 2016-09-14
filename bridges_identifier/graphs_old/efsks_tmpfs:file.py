import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('efsks','efsks')
G.edge['efsks']['efsks']['write-read'] = '[open open][write read][add_name search][write read]'
G.edge['efsks']['efsks']['fill'] = 'red'
app = Viewer(G)
app.mainloop()