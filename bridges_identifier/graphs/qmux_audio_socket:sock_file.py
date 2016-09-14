import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('mediaserver','qmuxd')
G.edge['mediaserver']['qmuxd']['write-read'] = '[open open]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','qmuxd')
G.edge['mediaserver']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['mediaserver']['fill'] = 'red'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','qmuxd')
G.edge['mediaserver']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['qmuxd']['fill'] = 'red'
G.add_edge('mediaserver','qmuxd')
G.edge['mediaserver']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('qmuxd','mediaserver')
G.edge['qmuxd']['mediaserver']['write-read'] = '[open open]'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qmuxd','mediaserver')
G.edge['qmuxd']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('qmuxd','mediaserver')
G.edge['qmuxd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmuxd']['mediaserver']['fill'] = 'red'
G.add_edge('qmuxd','mediaserver')
G.edge['qmuxd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['qmuxd']['qmuxd']['fill'] = 'red'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()