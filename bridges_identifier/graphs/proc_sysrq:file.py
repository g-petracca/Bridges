import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('healthd','healthd')
G.edge['healthd']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open]'
G.add_edge('healthd','lpm')
G.edge['healthd']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open]'
G.add_edge('healthd','system_server')
G.edge['healthd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('healthd','vold')
G.edge['healthd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('healthd','healthd')
G.edge['healthd']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read]'
G.edge['healthd']['healthd']['fill'] = 'red'
G.add_edge('healthd','healthd')
G.edge['healthd']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read]'
G.add_edge('healthd','lpm')
G.edge['healthd']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read]'
G.edge['healthd']['lpm']['fill'] = 'red'
G.add_edge('healthd','lpm')
G.edge['healthd']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read][append read]'
G.add_edge('healthd','system_server')
G.edge['healthd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['healthd']['system_server']['fill'] = 'red'
G.add_edge('healthd','system_server')
G.edge['healthd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('healthd','vold')
G.edge['healthd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['healthd']['vold']['fill'] = 'red'
G.add_edge('healthd','vold')
G.edge['healthd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('lpm','healthd')
G.edge['lpm']['healthd']['write-read'] = '[write read][append read][open open][write read][append read][open open]'
G.add_edge('lpm','lpm')
G.edge['lpm']['lpm']['write-read'] = '[open open][write read][append read][write read][open open]'
G.add_edge('lpm','system_server')
G.edge['lpm']['system_server']['write-read'] = '[write read][append read][open open]'
G.add_edge('lpm','vold')
G.edge['lpm']['vold']['write-read'] = '[write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('lpm','healthd')
G.edge['lpm']['healthd']['write-read'] = '[write read][append read][open open][write read][append read][open open][write read]'
G.edge['lpm']['healthd']['fill'] = 'red'
G.add_edge('lpm','healthd')
G.edge['lpm']['healthd']['write-read'] = '[write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('lpm','lpm')
G.edge['lpm']['lpm']['write-read'] = '[open open][write read][append read][write read][open open][write read]'
G.edge['lpm']['lpm']['fill'] = 'red'
G.add_edge('lpm','lpm')
G.edge['lpm']['lpm']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read]'
G.add_edge('lpm','system_server')
G.edge['lpm']['system_server']['write-read'] = '[write read][append read][open open][write read]'
G.edge['lpm']['system_server']['fill'] = 'red'
G.add_edge('lpm','system_server')
G.edge['lpm']['system_server']['write-read'] = '[write read][append read][open open][write read][append read]'
G.add_edge('lpm','vold')
G.edge['lpm']['vold']['write-read'] = '[write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['lpm']['vold']['fill'] = 'red'
G.add_edge('lpm','vold')
G.edge['lpm']['vold']['write-read'] = '[write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','healthd')
G.edge['system_server']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('system_server','lpm')
G.edge['system_server']['lpm']['write-read'] = '[setopt getopt][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('system_server','healthd')
G.edge['system_server']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['system_server']['healthd']['fill'] = 'red'
G.add_edge('system_server','healthd')
G.edge['system_server']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('system_server','lpm')
G.edge['system_server']['lpm']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['system_server']['lpm']['fill'] = 'red'
G.add_edge('system_server','lpm')
G.edge['system_server']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['vold']['fill'] = 'red'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','healthd')
G.edge['vold']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('vold','lpm')
G.edge['vold']['lpm']['write-read'] = '[setopt getopt][open open]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('vold','healthd')
G.edge['vold']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['vold']['healthd']['fill'] = 'red'
G.add_edge('vold','healthd')
G.edge['vold']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('vold','lpm')
G.edge['vold']['lpm']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['vold']['lpm']['fill'] = 'red'
G.add_edge('vold','lpm')
G.edge['vold']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['system_server']['fill'] = 'red'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['vold']['vold']['fill'] = 'red'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()