import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('irm_platform_app','irm_platform_app')
G.edge['irm_platform_app']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['irm_platform_app']['irm_platform_app']['fill'] = 'red'
G.add_edge('irm_platform_app','irm_platform_app')
G.edge['irm_platform_app']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][write read]'
G.edge['irm_platform_app']['irm_platform_app']['fill'] = 'red'
G.add_edge('irm_platform_app','platform_app')
G.edge['irm_platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['irm_platform_app']['platform_app']['fill'] = 'red'
G.add_edge('irm_platform_app','s_platform_app')
G.edge['irm_platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['irm_platform_app']['s_platform_app']['fill'] = 'red'
app = Viewer(G)
app.mainloop()