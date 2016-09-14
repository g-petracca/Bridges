import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('domain','qcomsysd')
G.edge['domain']['qcomsysd']['write-read'] = '[open open]'
G.add_edge('domain','ueventd')
G.edge['domain']['ueventd']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][write read][append read][write read][append read][open open]'
G.add_edge('domain','qcomsysd')
G.edge['domain']['qcomsysd']['write-read'] = '[open open][write read]'
G.edge['domain']['qcomsysd']['fill'] = 'red'
G.add_edge('domain','ueventd')
G.edge['domain']['ueventd']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][write read][append read][write read][append read][open open][write read]'
G.edge['domain']['ueventd']['fill'] = 'red'
G.add_edge('domain','ueventd')
G.edge['domain']['ueventd']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][write read][append read][write read][append read][open open][write read][append read]'
G.add_edge('qcomsysd','qcomsysd')
G.edge['qcomsysd']['qcomsysd']['write-read'] = '[open open][write read][open open][write read][write read][open open]'
G.add_edge('qcomsysd','ueventd')
G.edge['qcomsysd']['ueventd']['write-read'] = '[open open]'
G.add_edge('qcomsysd','qcomsysd')
G.edge['qcomsysd']['qcomsysd']['write-read'] = '[open open][write read][open open][write read][write read][open open][write read]'
G.edge['qcomsysd']['qcomsysd']['fill'] = 'red'
G.add_edge('qcomsysd','ueventd')
G.edge['qcomsysd']['ueventd']['write-read'] = '[open open][write read]'
G.edge['qcomsysd']['ueventd']['fill'] = 'red'
G.add_edge('qcomsysd','ueventd')
G.edge['qcomsysd']['ueventd']['write-read'] = '[open open][write read][append read]'
app = Viewer(G)
app.mainloop()