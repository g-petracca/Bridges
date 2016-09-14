import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['wcnss_service']['wcnss_service']['fill'] = 'red'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
app = Viewer(G)
app.mainloop()