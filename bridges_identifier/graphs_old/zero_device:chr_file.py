import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][open execmod][write read][open open][open open][write read][append read][append read][open open][open open][write read][append read][append read][open open][write read][append read][open open][write read][append read][write read][write read][write read][write read][setopt getopt][setopt getopt][open open][setattr getattr][open execmod][write read][write read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][add_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open]'
G.add_edge('appdomain','domain')
G.edge['appdomain']['domain']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('appdomain','untrustedappdomain')
G.edge['appdomain']['untrustedappdomain']['write-read'] = '[open open]'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][open execmod][write read][open open][open open][write read][append read][append read][open open][open open][write read][append read][append read][open open][write read][append read][open open][write read][append read][write read][write read][write read][write read][setopt getopt][setopt getopt][open open][setattr getattr][open execmod][write read][write read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][add_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read]'
G.edge['appdomain']['appdomain']['fill'] = 'red'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][open execmod][write read][open open][open open][write read][append read][append read][open open][open open][write read][append read][append read][open open][write read][append read][open open][write read][append read][write read][write read][write read][write read][setopt getopt][setopt getopt][open open][setattr getattr][open execmod][write read][write read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][add_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read][append read]'
G.add_edge('appdomain','domain')
G.edge['appdomain']['domain']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['appdomain']['domain']['fill'] = 'red'
G.add_edge('appdomain','domain')
G.edge['appdomain']['domain']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('appdomain','untrustedappdomain')
G.edge['appdomain']['untrustedappdomain']['write-read'] = '[open open][write read]'
G.edge['appdomain']['untrustedappdomain']['fill'] = 'red'
G.add_edge('appdomain','untrustedappdomain')
G.edge['appdomain']['untrustedappdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('domain','appdomain')
G.edge['domain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open]'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setpgid getpgid][setcap getcap][setsched getsched][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('domain','untrustedappdomain')
G.edge['domain']['untrustedappdomain']['write-read'] = '[open open]'
G.add_edge('domain','appdomain')
G.edge['domain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][write read]'
G.edge['domain']['appdomain']['fill'] = 'red'
G.add_edge('domain','appdomain')
G.edge['domain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setpgid getpgid][setcap getcap][setsched getsched][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['domain']['domain']['fill'] = 'red'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setpgid getpgid][setcap getcap][setsched getsched][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('domain','untrustedappdomain')
G.edge['domain']['untrustedappdomain']['write-read'] = '[open open][write read]'
G.edge['domain']['untrustedappdomain']['fill'] = 'red'
G.add_edge('domain','untrustedappdomain')
G.edge['domain']['untrustedappdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrustedappdomain','appdomain')
G.edge['untrustedappdomain']['appdomain']['write-read'] = '[open open]'
G.add_edge('untrustedappdomain','domain')
G.edge['untrustedappdomain']['domain']['write-read'] = '[open open]'
G.add_edge('untrustedappdomain','untrustedappdomain')
G.edge['untrustedappdomain']['untrustedappdomain']['write-read'] = '[open open]'
G.add_edge('untrustedappdomain','appdomain')
G.edge['untrustedappdomain']['appdomain']['write-read'] = '[open open][write read]'
G.edge['untrustedappdomain']['appdomain']['fill'] = 'red'
G.add_edge('untrustedappdomain','appdomain')
G.edge['untrustedappdomain']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrustedappdomain','domain')
G.edge['untrustedappdomain']['domain']['write-read'] = '[open open][write read]'
G.edge['untrustedappdomain']['domain']['fill'] = 'red'
G.add_edge('untrustedappdomain','domain')
G.edge['untrustedappdomain']['domain']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrustedappdomain','untrustedappdomain')
G.edge['untrustedappdomain']['untrustedappdomain']['write-read'] = '[open open][write read]'
G.edge['untrustedappdomain']['untrustedappdomain']['fill'] = 'red'
G.add_edge('untrustedappdomain','untrustedappdomain')
G.edge['untrustedappdomain']['untrustedappdomain']['write-read'] = '[open open][write read][append read]'
app = Viewer(G)
app.mainloop()