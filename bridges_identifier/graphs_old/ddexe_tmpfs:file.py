import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('ddexe','ddexe')
G.edge['ddexe']['ddexe']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['ddexe']['ddexe']['fill'] = 'red'
app = Viewer(G)
app.mainloop()