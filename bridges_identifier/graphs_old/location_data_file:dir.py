import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('location_app','location_app')
G.edge['location_app']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('location_app','location')
G.edge['location_app']['location']['write-read'] = '[open open]'
G.add_edge('location_app','system_server')
G.edge['location_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][write read][append read][open open]'
G.add_edge('location_app','location_app')
G.edge['location_app']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['location_app']['location_app']['fill'] = 'red'
G.add_edge('location_app','location')
G.edge['location_app']['location']['write-read'] = '[open open][write read]'
G.edge['location_app']['location']['fill'] = 'red'
G.add_edge('location_app','system_server')
G.edge['location_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][write read][append read][open open][write read]'
G.edge['location_app']['system_server']['fill'] = 'red'
G.add_edge('location_app','location_app')
G.edge['location_app']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('location_app','location_app')
G.edge['location_app']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('location_app','location')
G.edge['location_app']['location']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('location_app','location')
G.edge['location_app']['location']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('location_app','system_server')
G.edge['location_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][write read][append read][open open][write read][add_name search]'
G.add_edge('location_app','system_server')
G.edge['location_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('location','location_app')
G.edge['location']['location_app']['write-read'] = '[open open]'
G.add_edge('location','location')
G.edge['location']['location']['write-read'] = '[open open]'
G.add_edge('location','system_server')
G.edge['location']['system_server']['write-read'] = '[open open]'
G.add_edge('location','location_app')
G.edge['location']['location_app']['write-read'] = '[open open][write read]'
G.edge['location']['location_app']['fill'] = 'red'
G.add_edge('location','location')
G.edge['location']['location']['write-read'] = '[open open][write read]'
G.edge['location']['location']['fill'] = 'red'
G.add_edge('location','system_server')
G.edge['location']['system_server']['write-read'] = '[open open][write read]'
G.edge['location']['system_server']['fill'] = 'red'
G.add_edge('location','location_app')
G.edge['location']['location_app']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('location','location_app')
G.edge['location']['location_app']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('location','location')
G.edge['location']['location']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('location','location')
G.edge['location']['location']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('location','system_server')
G.edge['location']['system_server']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('location','system_server')
G.edge['location']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('system_server','location_app')
G.edge['system_server']['location_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','location')
G.edge['system_server']['location']['write-read'] = '[open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','location_app')
G.edge['system_server']['location_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['system_server']['location_app']['fill'] = 'red'
G.add_edge('system_server','location')
G.edge['system_server']['location']['write-read'] = '[open open][write read]'
G.edge['system_server']['location']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','location_app')
G.edge['system_server']['location_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('system_server','location_app')
G.edge['system_server']['location_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('system_server','location')
G.edge['system_server']['location']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('system_server','location')
G.edge['system_server']['location']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()