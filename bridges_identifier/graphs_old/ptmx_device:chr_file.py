import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['domain']['domain']['fill'] = 'red'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()