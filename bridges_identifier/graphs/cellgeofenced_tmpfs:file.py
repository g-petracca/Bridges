import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('cellgeofenced','cellgeofenced')
G.edge['cellgeofenced']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['cellgeofenced']['cellgeofenced']['fill'] = 'red'
app = Viewer(G)
app.mainloop()