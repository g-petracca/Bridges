import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('location','rfs_access')
G.edge['location']['rfs_access']['write-read'] = '[open open]'
G.add_edge('location','rfs_access')
G.edge['location']['rfs_access']['write-read'] = '[open open][setattr getattr]'
G.add_edge('location','rfs_access')
G.edge['location']['rfs_access']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['location']['rfs_access']['fill'] = 'red'
G.add_edge('location','rfs_access')
G.edge['location']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('rfs_access','rfs_access')
G.edge['rfs_access']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open]'
G.add_edge('rfs_access','rfs_access')
G.edge['rfs_access']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][setattr getattr]'
G.add_edge('rfs_access','rfs_access')
G.edge['rfs_access']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][setattr getattr][write read]'
G.edge['rfs_access']['rfs_access']['fill'] = 'red'
G.add_edge('rfs_access','rfs_access')
G.edge['rfs_access']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()