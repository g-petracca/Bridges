import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('bootanim','bootanim')
G.edge['bootanim']['bootanim']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][write read]'
G.edge['bootanim']['bootanim']['fill'] = 'red'
app = Viewer(G)
app.mainloop()