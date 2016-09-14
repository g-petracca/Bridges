import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('icd','icd')
G.edge['icd']['icd']['write-read'] = '[open open][write read][append read][write read]'
G.edge['icd']['icd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()