import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('efsks','qcks')
G.edge['efsks']['qcks']['write-read'] = '[open open]'
G.add_edge('efsks','qcks')
G.edge['efsks']['qcks']['write-read'] = '[open open][write read]'
G.edge['efsks']['qcks']['fill'] = 'red'
G.add_edge('efsks','qcks')
G.edge['efsks']['qcks']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','qcks')
G.edge['ks']['qcks']['write-read'] = '[open open]'
G.add_edge('ks','qcks')
G.edge['ks']['qcks']['write-read'] = '[open open][write read]'
G.edge['ks']['qcks']['fill'] = 'red'
G.add_edge('ks','qcks')
G.edge['ks']['qcks']['write-read'] = '[open open][write read][append read]'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open]'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read]'
G.edge['qcks']['qcks']['fill'] = 'red'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read]'
G.add_edge('rmt_storage','qcks')
G.edge['rmt_storage']['qcks']['write-read'] = '[open open]'
G.add_edge('rmt_storage','qcks')
G.edge['rmt_storage']['qcks']['write-read'] = '[open open][write read]'
G.edge['rmt_storage']['qcks']['fill'] = 'red'
G.add_edge('rmt_storage','qcks')
G.edge['rmt_storage']['qcks']['write-read'] = '[open open][write read][append read]'
app = Viewer(G)
app.mainloop()