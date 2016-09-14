import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('qlogd','qlogd')
G.edge['qlogd']['qlogd']['write-read'] = '[open open][setattr getattr][write read][append read][setopt getopt][write read][open open][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qlogd','qlogd')
G.edge['qlogd']['qlogd']['write-read'] = '[open open][setattr getattr][write read][append read][setopt getopt][write read][open open][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('qlogd','qlogd')
G.edge['qlogd']['qlogd']['write-read'] = '[open open][setattr getattr][write read][append read][setopt getopt][write read][open open][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['qlogd']['qlogd']['fill'] = 'red'
G.add_edge('qlogd','qlogd')
G.edge['qlogd']['qlogd']['write-read'] = '[open open][setattr getattr][write read][append read][setopt getopt][write read][open open][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()