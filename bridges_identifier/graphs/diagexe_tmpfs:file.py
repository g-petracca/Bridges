import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('diagexe','diagexe')
G.edge['diagexe']['diagexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][open open][write read][append read][write read]'
G.edge['diagexe']['diagexe']['fill'] = 'red'
app = Viewer(G)
app.mainloop()