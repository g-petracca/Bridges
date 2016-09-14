import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['ime_app']['fill'] = 'red'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['s_system_app']['fill'] = 'red'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['system_app']['fill'] = 'red'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['ime_app']['fill'] = 'red'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['system_app']['fill'] = 'red'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['ime_app']['fill'] = 'red'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['s_system_app']['fill'] = 'red'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['system_app']['fill'] = 'red'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open]'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['ime_app']['fill'] = 'red'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['s_system_app']['fill'] = 'red'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['system_app']['fill'] = 'red'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()