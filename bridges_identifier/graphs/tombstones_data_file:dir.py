import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('efsks','ks')
G.edge['efsks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open]'
G.add_edge('efsks','qcks')
G.edge['efsks']['qcks']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][open open]'
G.add_edge('efsks','qcks')
G.edge['efsks']['qcks']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][open open][setattr getattr]'
G.add_edge('efsks','ks')
G.edge['efsks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][write read]'
G.edge['efsks']['ks']['fill'] = 'red'
G.add_edge('efsks','qcks')
G.edge['efsks']['qcks']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][open open][setattr getattr][write read]'
G.edge['efsks']['qcks']['fill'] = 'red'
G.add_edge('efsks','ks')
G.edge['efsks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][write read][add_name search]'
G.add_edge('efsks','qcks')
G.edge['efsks']['qcks']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('efsks','qcks')
G.edge['efsks']['qcks']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ks','ks')
G.edge['ks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][append read][open open][write read][append read][open open]'
G.add_edge('ks','qcks')
G.edge['ks']['qcks']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][open open][append read][open open][write read][append read][open open]'
G.add_edge('ks','qcks')
G.edge['ks']['qcks']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][open open][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('ks','ks')
G.edge['ks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][append read][open open][write read][append read][open open][write read]'
G.edge['ks']['ks']['fill'] = 'red'
G.add_edge('ks','qcks')
G.edge['ks']['qcks']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][open open][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['ks']['qcks']['fill'] = 'red'
G.add_edge('ks','ks')
G.edge['ks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][append read][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('ks','qcks')
G.edge['ks']['qcks']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][open open][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('ks','qcks')
G.edge['ks']['qcks']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][open open][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qcks','ks')
G.edge['qcks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][append read][open open]'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open][write read][add_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open][write read][add_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('qcks','ks')
G.edge['qcks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][append read][open open][write read]'
G.edge['qcks']['ks']['fill'] = 'red'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open][write read][add_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['qcks']['qcks']['fill'] = 'red'
G.add_edge('qcks','ks')
G.edge['qcks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][append read][open open][write read][add_name search]'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open][write read][add_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open][write read][add_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','ks')
G.edge['system_server']['ks']['write-read'] = '[add_name search][open open][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','qcks')
G.edge['system_server']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','qcks')
G.edge['system_server']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','ks')
G.edge['system_server']['ks']['write-read'] = '[add_name search][open open][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['ks']['fill'] = 'red'
G.add_edge('system_server','qcks')
G.edge['system_server']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['qcks']['fill'] = 'red'
G.add_edge('system_server','ks')
G.edge['system_server']['ks']['write-read'] = '[add_name search][open open][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('system_server','qcks')
G.edge['system_server']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','qcks')
G.edge['system_server']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()