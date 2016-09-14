import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('daemon_app_process','daemon_app_process')
G.edge['daemon_app_process']['daemon_app_process']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('daemon_app_process','daemon_app_process')
G.edge['daemon_app_process']['daemon_app_process']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['daemon_app_process']['daemon_app_process']['fill'] = 'red'
G.add_edge('daemon_app_process','daemon_app_process')
G.edge['daemon_app_process']['daemon_app_process']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
app = Viewer(G)
app.mainloop()