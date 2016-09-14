import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('adbd','ueventd')
G.edge['adbd']['ueventd']['write-read'] = '[open open]'
G.add_edge('adbd','ueventd')
G.edge['adbd']['ueventd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('adbd','ueventd')
G.edge['adbd']['ueventd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['adbd']['ueventd']['fill'] = 'red'
G.add_edge('adbd','ueventd')
G.edge['adbd']['ueventd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('adbd','ueventd')
G.edge['adbd']['ueventd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('appdomain','ueventd')
G.edge['appdomain']['ueventd']['write-read'] = '[open open]'
G.add_edge('appdomain','ueventd')
G.edge['appdomain']['ueventd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('appdomain','ueventd')
G.edge['appdomain']['ueventd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['appdomain']['ueventd']['fill'] = 'red'
G.add_edge('appdomain','ueventd')
G.edge['appdomain']['ueventd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('appdomain','ueventd')
G.edge['appdomain']['ueventd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','ueventd')
G.edge['system_server']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('system_server','ueventd')
G.edge['system_server']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('system_server','ueventd')
G.edge['system_server']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['system_server']['ueventd']['fill'] = 'red'
G.add_edge('system_server','ueventd')
G.edge['system_server']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','ueventd')
G.edge['system_server']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['ueventd']['ueventd']['fill'] = 'red'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()