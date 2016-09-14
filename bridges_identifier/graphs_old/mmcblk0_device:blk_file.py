import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('kapd','kapd')
G.edge['kapd']['kapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('kapd','kapd')
G.edge['kapd']['kapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['kapd']['kapd']['fill'] = 'red'
G.add_edge('kapd','kapd')
G.edge['kapd']['kapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('rmt_storage','kapd')
G.edge['rmt_storage']['kapd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('rmt_storage','kapd')
G.edge['rmt_storage']['kapd']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['rmt_storage']['kapd']['fill'] = 'red'
G.add_edge('rmt_storage','kapd')
G.edge['rmt_storage']['kapd']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('vold','kapd')
G.edge['vold']['kapd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('vold','kapd')
G.edge['vold']['kapd']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['vold']['kapd']['fill'] = 'red'
G.add_edge('vold','kapd')
G.edge['vold']['kapd']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()