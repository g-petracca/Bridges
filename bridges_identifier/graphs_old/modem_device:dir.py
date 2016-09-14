import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('efsks','qcks')
G.edge['efsks']['qcks']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][add_name search]'
G.add_edge('efsks','qcks')
G.edge['efsks']['qcks']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][add_name search][remove_name search]'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open][write read][add_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open][write read][add_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['qcks']['qcks']['fill'] = 'red'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open][write read][add_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open][write read][add_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()