import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('cellgeofenced','cellgeofenced')
G.edge['cellgeofenced']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','init_shell')
G.edge['cellgeofenced']['init_shell']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','system_server')
G.edge['cellgeofenced']['system_server']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','init_shell')
G.edge['cellgeofenced']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cellgeofenced','rtcc')
G.edge['cellgeofenced']['rtcc']['write-read'] = '[setattr getattr]'
G.add_edge('cellgeofenced','system_server')
G.edge['cellgeofenced']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cellgeofenced','ueventd')
G.edge['cellgeofenced']['ueventd']['write-read'] = '[setattr getattr]'
G.add_edge('cellgeofenced','cellgeofenced')
G.edge['cellgeofenced']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['cellgeofenced']['fill'] = 'red'
G.add_edge('cellgeofenced','init_shell')
G.edge['cellgeofenced']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cellgeofenced']['init_shell']['fill'] = 'red'
G.add_edge('cellgeofenced','system_server')
G.edge['cellgeofenced']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cellgeofenced']['system_server']['fill'] = 'red'
G.add_edge('cellgeofenced','cellgeofenced')
G.edge['cellgeofenced']['cellgeofenced']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('cellgeofenced','cellgeofenced')
G.edge['cellgeofenced']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('cellgeofenced','init_shell')
G.edge['cellgeofenced']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cellgeofenced','init_shell')
G.edge['cellgeofenced']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cellgeofenced','system_server')
G.edge['cellgeofenced']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cellgeofenced','system_server')
G.edge['cellgeofenced']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','cellgeofenced')
G.edge['domain']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open]'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('domain','rtcc')
G.edge['domain']['rtcc']['write-read'] = '[setattr getattr]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr]'
G.add_edge('domain','ueventd')
G.edge['domain']['ueventd']['write-read'] = '[setattr getattr]'
G.add_edge('domain','cellgeofenced')
G.edge['domain']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['domain']['cellgeofenced']['fill'] = 'red'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['domain']['init_shell']['fill'] = 'red'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['domain']['system_server']['fill'] = 'red'
G.add_edge('domain','cellgeofenced')
G.edge['domain']['cellgeofenced']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('domain','cellgeofenced')
G.edge['domain']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','cellgeofenced')
G.edge['init_shell']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('init_shell','rtcc')
G.edge['init_shell']['rtcc']['write-read'] = '[setattr getattr]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr]'
G.add_edge('init_shell','ueventd')
G.edge['init_shell']['ueventd']['write-read'] = '[setattr getattr]'
G.add_edge('init_shell','cellgeofenced')
G.edge['init_shell']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['init_shell']['cellgeofenced']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['init_shell']['init_shell']['fill'] = 'red'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['init_shell']['system_server']['fill'] = 'red'
G.add_edge('init_shell','cellgeofenced')
G.edge['init_shell']['cellgeofenced']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('init_shell','cellgeofenced')
G.edge['init_shell']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('kernel','ueventd')
G.edge['kernel']['ueventd']['write-read'] = '[relabelto relabelfrom]'
G.add_edge('system_server','cellgeofenced')
G.edge['system_server']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','rtcc')
G.edge['system_server']['rtcc']['write-read'] = '[setattr getattr]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','ueventd')
G.edge['system_server']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('system_server','cellgeofenced')
G.edge['system_server']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['system_server']['cellgeofenced']['fill'] = 'red'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['init_shell']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','cellgeofenced')
G.edge['system_server']['cellgeofenced']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('system_server','cellgeofenced')
G.edge['system_server']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom]'
app = Viewer(G)
app.mainloop()