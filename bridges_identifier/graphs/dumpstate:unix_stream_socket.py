import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][open execmod][write read][open open][open open][write read][append read][append read][open open][open open][write read][append read][append read][open open][write read][append read][open open][write read][append read][write read][write read][write read][write read][setopt getopt][setopt getopt][open open][setattr getattr][open execmod][write read][write read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][add_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read][append read][write read][open open][write read][append read][write read][write read][append read][write read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['appdomain']['appdomain']['fill'] = 'red'
G.add_edge('appdomain','binderservicedomain')
G.edge['appdomain']['binderservicedomain']['write-read'] = '[write read][append read][write read]'
G.edge['appdomain']['binderservicedomain']['fill'] = 'red'
G.add_edge('appdomain','domain')
G.edge['appdomain']['domain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['appdomain']['domain']['fill'] = 'red'
G.add_edge('appdomain','vdc')
G.edge['appdomain']['vdc']['write-read'] = '[write read][write read]'
G.edge['appdomain']['vdc']['fill'] = 'red'
G.add_edge('appdomain','domain')
G.edge['appdomain']['domain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][setopt getopt]'
G.add_edge('binderservicedomain','appdomain')
G.edge['binderservicedomain']['appdomain']['write-read'] = '[write read][write read]'
G.edge['binderservicedomain']['appdomain']['fill'] = 'red'
G.add_edge('binderservicedomain','binderservicedomain')
G.edge['binderservicedomain']['binderservicedomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['binderservicedomain']['binderservicedomain']['fill'] = 'red'
G.add_edge('binderservicedomain','domain')
G.edge['binderservicedomain']['domain']['write-read'] = '[write read]'
G.edge['binderservicedomain']['domain']['fill'] = 'red'
G.add_edge('binderservicedomain','vdc')
G.edge['binderservicedomain']['vdc']['write-read'] = '[write read]'
G.edge['binderservicedomain']['vdc']['fill'] = 'red'
G.add_edge('binderservicedomain','domain')
G.edge['binderservicedomain']['domain']['write-read'] = '[write read][setopt getopt]'
G.add_edge('domain','appdomain')
G.edge['domain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['domain']['appdomain']['fill'] = 'red'
G.add_edge('domain','binderservicedomain')
G.edge['domain']['binderservicedomain']['write-read'] = '[write read]'
G.edge['domain']['binderservicedomain']['fill'] = 'red'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setpgid getpgid][setcap getcap][setsched getsched][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['domain']['domain']['fill'] = 'red'
G.add_edge('domain','vdc')
G.edge['domain']['vdc']['write-read'] = '[write read][write read]'
G.edge['domain']['vdc']['fill'] = 'red'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setpgid getpgid][setcap getcap][setsched getsched][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setopt getopt]'
G.add_edge('vdc','appdomain')
G.edge['vdc']['appdomain']['write-read'] = '[write read]'
G.edge['vdc']['appdomain']['fill'] = 'red'
G.add_edge('vdc','binderservicedomain')
G.edge['vdc']['binderservicedomain']['write-read'] = '[write read]'
G.edge['vdc']['binderservicedomain']['fill'] = 'red'
G.add_edge('vdc','domain')
G.edge['vdc']['domain']['write-read'] = '[write read]'
G.edge['vdc']['domain']['fill'] = 'red'
G.add_edge('vdc','vdc')
G.edge['vdc']['vdc']['write-read'] = '[write read][write read][write read][write read]'
G.edge['vdc']['vdc']['fill'] = 'red'
app = Viewer(G)
app.mainloop()