import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][append read][setopt getopt][setattr getattr][write read][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][append read][setopt getopt][setattr getattr][write read][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('cnd','appdomain')
G.edge['cnd']['appdomain']['write-read'] = '[write read][write read]'
G.edge['cnd']['appdomain']['fill'] = 'red'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][append read][setopt getopt][setattr getattr][write read][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['cnd']['cnd']['fill'] = 'red'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][append read][setopt getopt][setattr getattr][write read][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('cnd','dhcp')
G.edge['cnd']['dhcp']['write-read'] = '[write read]'
G.edge['cnd']['dhcp']['fill'] = 'red'
G.add_edge('cnd','ims')
G.edge['cnd']['ims']['write-read'] = '[add_name search][remove_name search][write read]'
G.edge['cnd']['ims']['fill'] = 'red'
G.add_edge('cnd','mediaserver')
G.edge['cnd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['cnd']['mediaserver']['fill'] = 'red'
G.add_edge('cnd','netd')
G.edge['cnd']['netd']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][write read]'
G.edge['cnd']['netd']['fill'] = 'red'
G.add_edge('cnd','netdomain')
G.edge['cnd']['netdomain']['write-read'] = '[write read]'
G.edge['cnd']['netdomain']['fill'] = 'red'
G.add_edge('cnd','netmgrd')
G.edge['cnd']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['cnd']['netmgrd']['fill'] = 'red'
G.add_edge('cnd','system_server')
G.edge['cnd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['cnd']['system_server']['fill'] = 'red'
app = Viewer(G)
app.mainloop()