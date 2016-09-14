import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('smdexe','smdexe')
G.edge['smdexe']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['smdexe']['smdexe']['fill'] = 'red'
app = Viewer(G)
app.mainloop()