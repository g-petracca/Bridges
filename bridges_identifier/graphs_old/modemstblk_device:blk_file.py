import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('qcks','ks')
G.edge['qcks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][append read][open open][write read][add_name search][open open][write read][append read][open open]'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open][write read][add_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][open open][write read][append read][open open]'
G.add_edge('qcks','rmt_storage')
G.edge['qcks']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('qcks','ks')
G.edge['qcks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][append read][open open][write read][add_name search][open open][write read][append read][open open][write read]'
G.edge['qcks']['ks']['fill'] = 'red'
G.add_edge('qcks','ks')
G.edge['qcks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][append read][open open][write read][add_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open][write read][add_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][open open][write read][append read][open open][write read]'
G.edge['qcks']['qcks']['fill'] = 'red'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open][write read][add_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('qcks','rmt_storage')
G.edge['qcks']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['qcks']['rmt_storage']['fill'] = 'red'
G.add_edge('qcks','rmt_storage')
G.edge['qcks']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('rmt_storage','ks')
G.edge['rmt_storage']['ks']['write-read'] = '[open open][write read][add_name search][open open][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('rmt_storage','qcks')
G.edge['rmt_storage']['qcks']['write-read'] = '[open open][write read][append read][open open][append read][open open][write read][append read][open open]'
G.add_edge('rmt_storage','rmt_storage')
G.edge['rmt_storage']['rmt_storage']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('rmt_storage','ks')
G.edge['rmt_storage']['ks']['write-read'] = '[open open][write read][add_name search][open open][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['rmt_storage']['ks']['fill'] = 'red'
G.add_edge('rmt_storage','ks')
G.edge['rmt_storage']['ks']['write-read'] = '[open open][write read][add_name search][open open][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('rmt_storage','qcks')
G.edge['rmt_storage']['qcks']['write-read'] = '[open open][write read][append read][open open][append read][open open][write read][append read][open open][write read]'
G.edge['rmt_storage']['qcks']['fill'] = 'red'
G.add_edge('rmt_storage','qcks')
G.edge['rmt_storage']['qcks']['write-read'] = '[open open][write read][append read][open open][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('rmt_storage','rmt_storage')
G.edge['rmt_storage']['rmt_storage']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['rmt_storage']['rmt_storage']['fill'] = 'red'
G.add_edge('rmt_storage','rmt_storage')
G.edge['rmt_storage']['rmt_storage']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()