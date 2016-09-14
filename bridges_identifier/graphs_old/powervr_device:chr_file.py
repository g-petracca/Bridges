import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('adbd','adbd')
G.edge['adbd']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][open open]'
G.add_edge('adbd','appdomain')
G.edge['adbd']['appdomain']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][open open][open open][write read][append read][append read][open open][write read][append read][open open]'
G.add_edge('adbd','domain')
G.edge['adbd']['domain']['write-read'] = '[open open]'
G.add_edge('adbd','adbd')
G.edge['adbd']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][open open][write read]'
G.edge['adbd']['adbd']['fill'] = 'red'
G.add_edge('adbd','adbd')
G.edge['adbd']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][open open][write read][append read]'
G.add_edge('adbd','appdomain')
G.edge['adbd']['appdomain']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][open open][open open][write read][append read][append read][open open][write read][append read][open open][write read]'
G.edge['adbd']['appdomain']['fill'] = 'red'
G.add_edge('adbd','appdomain')
G.edge['adbd']['appdomain']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][open open][open open][write read][append read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('adbd','domain')
G.edge['adbd']['domain']['write-read'] = '[open open][write read]'
G.edge['adbd']['domain']['fill'] = 'red'
G.add_edge('adbd','domain')
G.edge['adbd']['domain']['write-read'] = '[open open][write read][append read]'
G.add_edge('appdomain','adbd')
G.edge['appdomain']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][open open]'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][open execmod][write read][open open][open open][write read][append read][append read][open open][open open][write read][append read][append read][open open][write read][append read][open open]'
G.add_edge('appdomain','domain')
G.edge['appdomain']['domain']['write-read'] = '[open open]'
G.add_edge('appdomain','adbd')
G.edge['appdomain']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][open open][write read]'
G.edge['appdomain']['adbd']['fill'] = 'red'
G.add_edge('appdomain','adbd')
G.edge['appdomain']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][open open][write read][append read]'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][open execmod][write read][open open][open open][write read][append read][append read][open open][open open][write read][append read][append read][open open][write read][append read][open open][write read]'
G.edge['appdomain']['appdomain']['fill'] = 'red'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][open execmod][write read][open open][open open][write read][append read][append read][open open][open open][write read][append read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('appdomain','domain')
G.edge['appdomain']['domain']['write-read'] = '[open open][write read]'
G.edge['appdomain']['domain']['fill'] = 'red'
G.add_edge('appdomain','domain')
G.edge['appdomain']['domain']['write-read'] = '[open open][write read][append read]'
G.add_edge('domain','adbd')
G.edge['domain']['adbd']['write-read'] = '[write read][add_name search][add_name search][setattr getattr][add_name search][remove_name search][open open]'
G.add_edge('domain','appdomain')
G.edge['domain']['appdomain']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setpgid getpgid][setcap getcap][setsched getsched][open open]'
G.add_edge('domain','adbd')
G.edge['domain']['adbd']['write-read'] = '[write read][add_name search][add_name search][setattr getattr][add_name search][remove_name search][open open][write read]'
G.edge['domain']['adbd']['fill'] = 'red'
G.add_edge('domain','adbd')
G.edge['domain']['adbd']['write-read'] = '[write read][add_name search][add_name search][setattr getattr][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','appdomain')
G.edge['domain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['domain']['appdomain']['fill'] = 'red'
G.add_edge('domain','appdomain')
G.edge['domain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setpgid getpgid][setcap getcap][setsched getsched][open open][write read]'
G.edge['domain']['domain']['fill'] = 'red'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setpgid getpgid][setcap getcap][setsched getsched][open open][write read][append read]'
app = Viewer(G)
app.mainloop()