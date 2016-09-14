import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('qcomsysd','mmi')
G.edge['qcomsysd']['mmi']['write-read'] = '[open open]'
G.add_edge('qcomsysd','qcomsysd')
G.edge['qcomsysd']['qcomsysd']['write-read'] = '[open open][write read][open open]'
G.add_edge('qcomsysd','mmi')
G.edge['qcomsysd']['mmi']['write-read'] = '[open open][write read]'
G.edge['qcomsysd']['mmi']['fill'] = 'red'
G.add_edge('qcomsysd','mmi')
G.edge['qcomsysd']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('qcomsysd','qcomsysd')
G.edge['qcomsysd']['qcomsysd']['write-read'] = '[open open][write read][open open][write read]'
G.edge['qcomsysd']['qcomsysd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()