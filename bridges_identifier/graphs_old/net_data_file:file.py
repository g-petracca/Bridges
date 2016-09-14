import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('dumpstate','netd')
G.edge['dumpstate']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('dumpstate','netd')
G.edge['dumpstate']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('dumpstate','netd')
G.edge['dumpstate']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['dumpstate']['netd']['fill'] = 'red'
G.add_edge('dumpstate','netd')
G.edge['dumpstate']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['netd']['netd']['fill'] = 'red'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('netmgrd','netd')
G.edge['netmgrd']['netd']['write-read'] = '[open open]'
G.add_edge('netmgrd','netd')
G.edge['netmgrd']['netd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('netmgrd','netd')
G.edge['netmgrd']['netd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['netmgrd']['netd']['fill'] = 'red'
G.add_edge('netmgrd','netd')
G.edge['netmgrd']['netd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('radio','netd')
G.edge['radio']['netd']['write-read'] = '[open open]'
G.add_edge('radio','netd')
G.edge['radio']['netd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','netd')
G.edge['radio']['netd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['radio']['netd']['fill'] = 'red'
G.add_edge('radio','netd')
G.edge['radio']['netd']['write-read'] = '[open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()