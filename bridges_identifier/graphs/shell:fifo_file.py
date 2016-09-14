import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('device_domain','device_domain')
G.edge['device_domain']['device_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('device_domain','system_domain')
G.edge['device_domain']['system_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('device_domain','system_server')
G.edge['device_domain']['system_server']['write-read'] = '[open open]'
G.add_edge('device_domain','device_domain')
G.edge['device_domain']['device_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('device_domain','system_domain')
G.edge['device_domain']['system_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('device_domain','device_domain')
G.edge['device_domain']['device_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['device_domain']['device_domain']['fill'] = 'red'
G.add_edge('device_domain','device_domain')
G.edge['device_domain']['device_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('device_domain','runas')
G.edge['device_domain']['runas']['write-read'] = '[write read]'
G.edge['device_domain']['runas']['fill'] = 'red'
G.add_edge('device_domain','system_domain')
G.edge['device_domain']['system_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['device_domain']['system_domain']['fill'] = 'red'
G.add_edge('device_domain','system_domain')
G.edge['device_domain']['system_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('device_domain','system_server')
G.edge['device_domain']['system_server']['write-read'] = '[open open][write read]'
G.edge['device_domain']['system_server']['fill'] = 'red'
G.add_edge('device_domain','system_server')
G.edge['device_domain']['system_server']['write-read'] = '[open open][write read][append read]'
G.add_edge('runas','device_domain')
G.edge['runas']['device_domain']['write-read'] = '[write read]'
G.edge['runas']['device_domain']['fill'] = 'red'
G.add_edge('runas','device_domain')
G.edge['runas']['device_domain']['write-read'] = '[write read][append read]'
G.add_edge('runas','runas')
G.edge['runas']['runas']['write-read'] = '[write read]'
G.edge['runas']['runas']['fill'] = 'red'
G.add_edge('runas','system_domain')
G.edge['runas']['system_domain']['write-read'] = '[write read]'
G.edge['runas']['system_domain']['fill'] = 'red'
G.add_edge('runas','system_domain')
G.edge['runas']['system_domain']['write-read'] = '[write read][append read]'
G.add_edge('runas','system_server')
G.edge['runas']['system_server']['write-read'] = '[write read]'
G.edge['runas']['system_server']['fill'] = 'red'
G.add_edge('runas','system_server')
G.edge['runas']['system_server']['write-read'] = '[write read][append read]'
G.add_edge('system_domain','device_domain')
G.edge['system_domain']['device_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_domain','system_domain')
G.edge['system_domain']['system_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_domain','system_server')
G.edge['system_domain']['system_server']['write-read'] = '[open open]'
G.add_edge('system_domain','device_domain')
G.edge['system_domain']['device_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_domain','system_domain')
G.edge['system_domain']['system_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_domain','device_domain')
G.edge['system_domain']['device_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_domain']['device_domain']['fill'] = 'red'
G.add_edge('system_domain','device_domain')
G.edge['system_domain']['device_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_domain','runas')
G.edge['system_domain']['runas']['write-read'] = '[write read]'
G.edge['system_domain']['runas']['fill'] = 'red'
G.add_edge('system_domain','system_domain')
G.edge['system_domain']['system_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_domain']['system_domain']['fill'] = 'red'
G.add_edge('system_domain','system_domain')
G.edge['system_domain']['system_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_domain','system_server')
G.edge['system_domain']['system_server']['write-read'] = '[open open][write read]'
G.edge['system_domain']['system_server']['fill'] = 'red'
G.add_edge('system_domain','system_server')
G.edge['system_domain']['system_server']['write-read'] = '[open open][write read][append read]'
app = Viewer(G)
app.mainloop()