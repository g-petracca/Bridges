import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('seempd','seempd')
G.edge['seempd']['seempd']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('seempd','seempd')
G.edge['seempd']['seempd']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('seempd','seempd')
G.edge['seempd']['seempd']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['seempd']['seempd']['fill'] = 'red'
G.add_edge('seempd','seempd')
G.edge['seempd']['seempd']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('seempd','seempd')
G.edge['seempd']['seempd']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','seempd')
G.edge['s_system_app']['seempd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','seempd')
G.edge['s_system_app']['seempd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','seempd')
G.edge['s_system_app']['seempd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['seempd']['fill'] = 'red'
G.add_edge('s_system_app','seempd')
G.edge['s_system_app']['seempd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','seempd')
G.edge['s_system_app']['seempd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','seempd')
G.edge['system_app']['seempd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','seempd')
G.edge['system_app']['seempd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','seempd')
G.edge['system_app']['seempd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['seempd']['fill'] = 'red'
G.add_edge('system_app','seempd')
G.edge['system_app']['seempd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','seempd')
G.edge['system_app']['seempd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()