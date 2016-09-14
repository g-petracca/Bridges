import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['domain']['domain']['fill'] = 'red'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('sec-ril','domain')
G.edge['sec-ril']['domain']['write-read'] = '[open open]'
G.add_edge('sec-ril','domain')
G.edge['sec-ril']['domain']['write-read'] = '[open open][write read]'
G.edge['sec-ril']['domain']['fill'] = 'red'
G.add_edge('sec-ril','domain')
G.edge['sec-ril']['domain']['write-read'] = '[open open][write read][append read]'
G.add_edge('vmware_app','domain')
G.edge['vmware_app']['domain']['write-read'] = '[open open]'
G.add_edge('vmware_app','domain')
G.edge['vmware_app']['domain']['write-read'] = '[open open][write read]'
G.edge['vmware_app']['domain']['fill'] = 'red'
G.add_edge('vmware_app','domain')
G.edge['vmware_app']['domain']['write-read'] = '[open open][write read][append read]'
app = Viewer(G)
app.mainloop()