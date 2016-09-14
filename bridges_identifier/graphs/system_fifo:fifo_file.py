import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('domain','immvibed')
G.edge['domain']['immvibed']['write-read'] = '[open open]'
G.add_edge('domain','s_system_app')
G.edge['domain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][add_name search][remove_name search][open open]'
G.add_edge('domain','system_app')
G.edge['domain']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][add_name search][remove_name search][open open]'
G.add_edge('domain','immvibed')
G.edge['domain']['immvibed']['write-read'] = '[open open][setattr getattr]'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['domain']['domain']['fill'] = 'red'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('domain','immvibed')
G.edge['domain']['immvibed']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['domain']['immvibed']['fill'] = 'red'
G.add_edge('domain','immvibed')
G.edge['domain']['immvibed']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('domain','s_system_app')
G.edge['domain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][add_name search][remove_name search][open open][write read]'
G.edge['domain']['s_system_app']['fill'] = 'red'
G.add_edge('domain','s_system_app')
G.edge['domain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','system_app')
G.edge['domain']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][add_name search][remove_name search][open open][write read]'
G.edge['domain']['system_app']['fill'] = 'red'
G.add_edge('domain','system_app')
G.edge['domain']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('immvibed','domain')
G.edge['immvibed']['domain']['write-read'] = '[open open]'
G.add_edge('immvibed','immvibed')
G.edge['immvibed']['immvibed']['write-read'] = '[open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open]'
G.add_edge('immvibed','s_system_app')
G.edge['immvibed']['s_system_app']['write-read'] = '[open open]'
G.add_edge('immvibed','system_app')
G.edge['immvibed']['system_app']['write-read'] = '[open open]'
G.add_edge('immvibed','immvibed')
G.edge['immvibed']['immvibed']['write-read'] = '[open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr]'
G.add_edge('immvibed','domain')
G.edge['immvibed']['domain']['write-read'] = '[open open][write read]'
G.edge['immvibed']['domain']['fill'] = 'red'
G.add_edge('immvibed','domain')
G.edge['immvibed']['domain']['write-read'] = '[open open][write read][append read]'
G.add_edge('immvibed','immvibed')
G.edge['immvibed']['immvibed']['write-read'] = '[open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read]'
G.edge['immvibed']['immvibed']['fill'] = 'red'
G.add_edge('immvibed','immvibed')
G.edge['immvibed']['immvibed']['write-read'] = '[open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('immvibed','s_system_app')
G.edge['immvibed']['s_system_app']['write-read'] = '[open open][write read]'
G.edge['immvibed']['s_system_app']['fill'] = 'red'
G.add_edge('immvibed','s_system_app')
G.edge['immvibed']['s_system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('immvibed','system_app')
G.edge['immvibed']['system_app']['write-read'] = '[open open][write read]'
G.edge['immvibed']['system_app']['fill'] = 'red'
G.add_edge('immvibed','system_app')
G.edge['immvibed']['system_app']['write-read'] = '[open open][write read][append read]'
app = Viewer(G)
app.mainloop()