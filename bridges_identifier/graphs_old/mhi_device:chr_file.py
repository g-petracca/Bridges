import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('port-bridge','port-bridge')
G.edge['port-bridge']['port-bridge']['write-read'] = '[write read][open open][write read][append read][open open]'
G.add_edge('port-bridge','qmuxd')
G.edge['port-bridge']['qmuxd']['write-read'] = '[open open]'
G.add_edge('port-bridge','qti')
G.edge['port-bridge']['qti']['write-read'] = '[open open]'
G.add_edge('port-bridge','port-bridge')
G.edge['port-bridge']['port-bridge']['write-read'] = '[write read][open open][write read][append read][open open][write read]'
G.edge['port-bridge']['port-bridge']['fill'] = 'red'
G.add_edge('port-bridge','port-bridge')
G.edge['port-bridge']['port-bridge']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read]'
G.add_edge('port-bridge','qmuxd')
G.edge['port-bridge']['qmuxd']['write-read'] = '[open open][write read]'
G.edge['port-bridge']['qmuxd']['fill'] = 'red'
G.add_edge('port-bridge','qmuxd')
G.edge['port-bridge']['qmuxd']['write-read'] = '[open open][write read][append read]'
G.add_edge('port-bridge','qti')
G.edge['port-bridge']['qti']['write-read'] = '[open open][write read]'
G.edge['port-bridge']['qti']['fill'] = 'red'
G.add_edge('port-bridge','qti')
G.edge['port-bridge']['qti']['write-read'] = '[open open][write read][append read]'
G.add_edge('qmuxd','port-bridge')
G.edge['qmuxd']['port-bridge']['write-read'] = '[open open]'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][write read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('qmuxd','qti')
G.edge['qmuxd']['qti']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qmuxd','port-bridge')
G.edge['qmuxd']['port-bridge']['write-read'] = '[open open][write read]'
G.edge['qmuxd']['port-bridge']['fill'] = 'red'
G.add_edge('qmuxd','port-bridge')
G.edge['qmuxd']['port-bridge']['write-read'] = '[open open][write read][append read]'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][write read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['qmuxd']['qmuxd']['fill'] = 'red'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][write read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('qmuxd','qti')
G.edge['qmuxd']['qti']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['qmuxd']['qti']['fill'] = 'red'
G.add_edge('qmuxd','qti')
G.edge['qmuxd']['qti']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qti','port-bridge')
G.edge['qti']['port-bridge']['write-read'] = '[open open]'
G.add_edge('qti','qmuxd')
G.edge['qti']['qmuxd']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qti','qti')
G.edge['qti']['qti']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][write read][setattr getattr][write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('qti','port-bridge')
G.edge['qti']['port-bridge']['write-read'] = '[open open][write read]'
G.edge['qti']['port-bridge']['fill'] = 'red'
G.add_edge('qti','port-bridge')
G.edge['qti']['port-bridge']['write-read'] = '[open open][write read][append read]'
G.add_edge('qti','qmuxd')
G.edge['qti']['qmuxd']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['qti']['qmuxd']['fill'] = 'red'
G.add_edge('qti','qmuxd')
G.edge['qti']['qmuxd']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qti','qti')
G.edge['qti']['qti']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][write read][setattr getattr][write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['qti']['qti']['fill'] = 'red'
G.add_edge('qti','qti')
G.edge['qti']['qti']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][write read][setattr getattr][write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()