import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('appdomain','shared_relro')
G.edge['appdomain']['shared_relro']['write-read'] = '[add_name search][remove_name search][open open]'
G.add_edge('appdomain','shared_relro')
G.edge['appdomain']['shared_relro']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('appdomain','shared_relro')
G.edge['appdomain']['shared_relro']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['appdomain']['shared_relro']['fill'] = 'red'
G.add_edge('appdomain','shared_relro')
G.edge['appdomain']['shared_relro']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('debuggerd','shared_relro')
G.edge['debuggerd']['shared_relro']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('debuggerd','shared_relro')
G.edge['debuggerd']['shared_relro']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('debuggerd','shared_relro')
G.edge['debuggerd']['shared_relro']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['debuggerd']['shared_relro']['fill'] = 'red'
G.add_edge('debuggerd','shared_relro')
G.edge['debuggerd']['shared_relro']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('good_app','shared_relro')
G.edge['good_app']['shared_relro']['write-read'] = '[add_name search][remove_name search][open open]'
G.add_edge('good_app','shared_relro')
G.edge['good_app']['shared_relro']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('good_app','shared_relro')
G.edge['good_app']['shared_relro']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['good_app']['shared_relro']['fill'] = 'red'
G.add_edge('good_app','shared_relro')
G.edge['good_app']['shared_relro']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('shared_relro','shared_relro')
G.edge['shared_relro']['shared_relro']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('shared_relro','shared_relro')
G.edge['shared_relro']['shared_relro']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('shared_relro','shared_relro')
G.edge['shared_relro']['shared_relro']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['shared_relro']['shared_relro']['fill'] = 'red'
G.add_edge('shared_relro','shared_relro')
G.edge['shared_relro']['shared_relro']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()