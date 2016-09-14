import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('itsonclient_app','itsonclient_app')
G.edge['itsonclient_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open]'
G.add_edge('itsonclient_app','itsonclient_app')
G.edge['itsonclient_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][setattr getattr]'
G.add_edge('itsonclient_app','itsonclient_app')
G.edge['itsonclient_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][setattr getattr][write read]'
G.edge['itsonclient_app']['itsonclient_app']['fill'] = 'red'
G.add_edge('itsonclient_app','itsonclient_app')
G.edge['itsonclient_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()