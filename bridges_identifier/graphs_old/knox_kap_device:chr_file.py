import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('ime_app','kapd')
G.edge['ime_app']['kapd']['write-read'] = '[open open]'
G.add_edge('ime_app','kapd')
G.edge['ime_app']['kapd']['write-read'] = '[open open][write read]'
G.edge['ime_app']['kapd']['fill'] = 'red'
G.add_edge('ime_app','kapd')
G.edge['ime_app']['kapd']['write-read'] = '[open open][write read][append read]'
G.add_edge('kapd','kapd')
G.edge['kapd']['kapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('kapd','kapd')
G.edge['kapd']['kapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['kapd']['kapd']['fill'] = 'red'
G.add_edge('kapd','kapd')
G.edge['kapd']['kapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('rild','kapd')
G.edge['rild']['kapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('rild','kapd')
G.edge['rild']['kapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['rild']['kapd']['fill'] = 'red'
G.add_edge('rild','kapd')
G.edge['rild']['kapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('s_system_app','kapd')
G.edge['s_system_app']['kapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('s_system_app','kapd')
G.edge['s_system_app']['kapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['s_system_app']['kapd']['fill'] = 'red'
G.add_edge('s_system_app','kapd')
G.edge['s_system_app']['kapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_app','kapd')
G.edge['system_app']['kapd']['write-read'] = '[open open]'
G.add_edge('system_app','kapd')
G.edge['system_app']['kapd']['write-read'] = '[open open][write read]'
G.edge['system_app']['kapd']['fill'] = 'red'
G.add_edge('system_app','kapd')
G.edge['system_app']['kapd']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','kapd')
G.edge['system_server']['kapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','kapd')
G.edge['system_server']['kapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['kapd']['fill'] = 'red'
G.add_edge('system_server','kapd')
G.edge['system_server']['kapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()