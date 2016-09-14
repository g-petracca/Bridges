import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('platform_app','tlc_server')
G.edge['platform_app']['tlc_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('platform_app','tlc_server')
G.edge['platform_app']['tlc_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('platform_app','tlc_server')
G.edge['platform_app']['tlc_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['platform_app']['tlc_server']['fill'] = 'red'
G.add_edge('platform_app','tlc_server')
G.edge['platform_app']['tlc_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('platform_app','tlc_server')
G.edge['platform_app']['tlc_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_platform_app','tlc_server')
G.edge['s_platform_app']['tlc_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][open open]'
G.add_edge('s_platform_app','tlc_server')
G.edge['s_platform_app']['tlc_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr]'
G.add_edge('s_platform_app','tlc_server')
G.edge['s_platform_app']['tlc_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read]'
G.edge['s_platform_app']['tlc_server']['fill'] = 'red'
G.add_edge('s_platform_app','tlc_server')
G.edge['s_platform_app']['tlc_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_platform_app','tlc_server')
G.edge['s_platform_app']['tlc_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('tlc_server','tlc_server')
G.edge['tlc_server']['tlc_server']['write-read'] = '[write read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][open open]'
G.add_edge('tlc_server','tlc_server')
G.edge['tlc_server']['tlc_server']['write-read'] = '[write read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][open open][setattr getattr]'
G.add_edge('tlc_server','tlc_server')
G.edge['tlc_server']['tlc_server']['write-read'] = '[write read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][open open][setattr getattr][write read]'
G.edge['tlc_server']['tlc_server']['fill'] = 'red'
G.add_edge('tlc_server','tlc_server')
G.edge['tlc_server']['tlc_server']['write-read'] = '[write read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('tlc_server','tlc_server')
G.edge['tlc_server']['tlc_server']['write-read'] = '[write read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('umcagent_app','tlc_server')
G.edge['umcagent_app']['tlc_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('umcagent_app','tlc_server')
G.edge['umcagent_app']['tlc_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('umcagent_app','tlc_server')
G.edge['umcagent_app']['tlc_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['umcagent_app']['tlc_server']['fill'] = 'red'
G.add_edge('umcagent_app','tlc_server')
G.edge['umcagent_app']['tlc_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('umcagent_app','tlc_server')
G.edge['umcagent_app']['tlc_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()