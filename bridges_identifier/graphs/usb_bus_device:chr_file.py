import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('appdomain','commonplatformappdomain')
G.edge['appdomain']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['appdomain']['appdomain']['fill'] = 'red'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('appdomain','commonplatformappdomain')
G.edge['appdomain']['commonplatformappdomain']['write-read'] = '[open open][write read]'
G.edge['appdomain']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('appdomain','commonplatformappdomain')
G.edge['appdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['appdomain']['system_server']['fill'] = 'red'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('commonplatformappdomain','appdomain')
G.edge['commonplatformappdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][open open]'
G.add_edge('commonplatformappdomain','system_server')
G.edge['commonplatformappdomain']['system_server']['write-read'] = '[write read][append read][open open][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('commonplatformappdomain','appdomain')
G.edge['commonplatformappdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['commonplatformappdomain']['appdomain']['fill'] = 'red'
G.add_edge('commonplatformappdomain','appdomain')
G.edge['commonplatformappdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][open open][write read]'
G.edge['commonplatformappdomain']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][open open][write read][append read]'
G.add_edge('commonplatformappdomain','system_server')
G.edge['commonplatformappdomain']['system_server']['write-read'] = '[write read][append read][open open][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['commonplatformappdomain']['system_server']['fill'] = 'red'
G.add_edge('commonplatformappdomain','system_server')
G.edge['commonplatformappdomain']['system_server']['write-read'] = '[write read][append read][open open][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('shell','appdomain')
G.edge['shell']['appdomain']['write-read'] = '[open open]'
G.add_edge('shell','commonplatformappdomain')
G.edge['shell']['commonplatformappdomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('shell','system_server')
G.edge['shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('shell','appdomain')
G.edge['shell']['appdomain']['write-read'] = '[open open][write read]'
G.edge['shell']['appdomain']['fill'] = 'red'
G.add_edge('shell','appdomain')
G.edge['shell']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('shell','commonplatformappdomain')
G.edge['shell']['commonplatformappdomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['shell']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('shell','commonplatformappdomain')
G.edge['shell']['commonplatformappdomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('shell','system_server')
G.edge['shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['shell']['system_server']['fill'] = 'red'
G.add_edge('shell','system_server')
G.edge['shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('system_server','appdomain')
G.edge['system_server']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','commonplatformappdomain')
G.edge['system_server']['commonplatformappdomain']['write-read'] = '[setopt getopt][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','appdomain')
G.edge['system_server']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['appdomain']['fill'] = 'red'
G.add_edge('system_server','appdomain')
G.edge['system_server']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','commonplatformappdomain')
G.edge['system_server']['commonplatformappdomain']['write-read'] = '[setopt getopt][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['system_server']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('system_server','commonplatformappdomain')
G.edge['system_server']['commonplatformappdomain']['write-read'] = '[setopt getopt][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
app = Viewer(G)
app.mainloop()