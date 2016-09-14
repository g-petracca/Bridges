import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('device_domain','device_domain')
G.edge['device_domain']['device_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('device_domain','system_domain')
G.edge['device_domain']['system_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('device_domain','device_domain')
G.edge['device_domain']['device_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('device_domain','system_domain')
G.edge['device_domain']['system_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('device_domain','device_domain')
G.edge['device_domain']['device_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['device_domain']['device_domain']['fill'] = 'red'
G.add_edge('device_domain','device_domain')
G.edge['device_domain']['device_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('device_domain','system_domain')
G.edge['device_domain']['system_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['device_domain']['system_domain']['fill'] = 'red'
G.add_edge('device_domain','system_domain')
G.edge['device_domain']['system_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','device_domain')
G.edge['mediaserver']['device_domain']['write-read'] = '[open open]'
G.add_edge('mediaserver','system_domain')
G.edge['mediaserver']['system_domain']['write-read'] = '[open open]'
G.add_edge('mediaserver','device_domain')
G.edge['mediaserver']['device_domain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','system_domain')
G.edge['mediaserver']['system_domain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','device_domain')
G.edge['mediaserver']['device_domain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['device_domain']['fill'] = 'red'
G.add_edge('mediaserver','device_domain')
G.edge['mediaserver']['device_domain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','system_domain')
G.edge['mediaserver']['system_domain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['system_domain']['fill'] = 'red'
G.add_edge('mediaserver','system_domain')
G.edge['mediaserver']['system_domain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('surfaceflinger','device_domain')
G.edge['surfaceflinger']['device_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('surfaceflinger','system_domain')
G.edge['surfaceflinger']['system_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('surfaceflinger','device_domain')
G.edge['surfaceflinger']['device_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('surfaceflinger','system_domain')
G.edge['surfaceflinger']['system_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('surfaceflinger','device_domain')
G.edge['surfaceflinger']['device_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['surfaceflinger']['device_domain']['fill'] = 'red'
G.add_edge('surfaceflinger','device_domain')
G.edge['surfaceflinger']['device_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('surfaceflinger','system_domain')
G.edge['surfaceflinger']['system_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['surfaceflinger']['system_domain']['fill'] = 'red'
G.add_edge('surfaceflinger','system_domain')
G.edge['surfaceflinger']['system_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_domain','device_domain')
G.edge['system_domain']['device_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_domain','system_domain')
G.edge['system_domain']['system_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_domain','device_domain')
G.edge['system_domain']['device_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_domain','system_domain')
G.edge['system_domain']['system_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_domain','device_domain')
G.edge['system_domain']['device_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_domain']['device_domain']['fill'] = 'red'
G.add_edge('system_domain','device_domain')
G.edge['system_domain']['device_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_domain','system_domain')
G.edge['system_domain']['system_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_domain']['system_domain']['fill'] = 'red'
G.add_edge('system_domain','system_domain')
G.edge['system_domain']['system_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()