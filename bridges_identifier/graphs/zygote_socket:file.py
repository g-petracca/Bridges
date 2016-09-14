import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('newAttr98','newAttr98')
G.edge['newAttr98']['newAttr98']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr98','newAttr98')
G.edge['newAttr98']['newAttr98']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['newAttr98']['newAttr98']['fill'] = 'red'
G.add_edge('newAttr98','newAttr98')
G.edge['newAttr98']['newAttr98']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
app = Viewer(G)
app.mainloop()