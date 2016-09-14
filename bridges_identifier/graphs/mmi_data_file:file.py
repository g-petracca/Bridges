import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('mmi','mmi')
G.edge['mmi']['mmi']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('mmi','mmi')
G.edge['mmi']['mmi']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['mmi']['mmi']['fill'] = 'red'
G.add_edge('mmi','mmi')
G.edge['mmi']['mmi']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read]'
app = Viewer(G)
app.mainloop()