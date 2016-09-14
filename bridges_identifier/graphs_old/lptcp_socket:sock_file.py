import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('lptcpgc','lptcpgc')
G.edge['lptcpgc']['lptcpgc']['write-read'] = '[open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('lptcpgc','lptcpgc')
G.edge['lptcpgc']['lptcpgc']['write-read'] = '[open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('lptcpgc','appdomain')
G.edge['lptcpgc']['appdomain']['write-read'] = '[write read]'
G.edge['lptcpgc']['appdomain']['fill'] = 'red'
G.add_edge('lptcpgc','lptcpgc')
G.edge['lptcpgc']['lptcpgc']['write-read'] = '[open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['lptcpgc']['lptcpgc']['fill'] = 'red'
G.add_edge('lptcpgc','lptcpgc')
G.edge['lptcpgc']['lptcpgc']['write-read'] = '[open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()