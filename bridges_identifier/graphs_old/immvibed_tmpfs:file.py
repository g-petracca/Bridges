import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('immvibed','immvibed')
G.edge['immvibed']['immvibed']['write-read'] = '[open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read]'
G.edge['immvibed']['immvibed']['fill'] = 'red'
app = Viewer(G)
app.mainloop()