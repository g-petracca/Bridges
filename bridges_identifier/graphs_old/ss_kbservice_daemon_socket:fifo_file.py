import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('ss_kbservice_daemon','ss_kbservice_daemon')
G.edge['ss_kbservice_daemon']['ss_kbservice_daemon']['write-read'] = '[open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open]'
G.add_edge('ss_kbservice_daemon','ss_kbservice_daemon')
G.edge['ss_kbservice_daemon']['ss_kbservice_daemon']['write-read'] = '[open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr]'
G.add_edge('ss_kbservice_daemon','ss_kbservice_daemon')
G.edge['ss_kbservice_daemon']['ss_kbservice_daemon']['write-read'] = '[open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read]'
G.edge['ss_kbservice_daemon']['ss_kbservice_daemon']['fill'] = 'red'
G.add_edge('ss_kbservice_daemon','ss_kbservice_daemon')
G.edge['ss_kbservice_daemon']['ss_kbservice_daemon']['write-read'] = '[open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()