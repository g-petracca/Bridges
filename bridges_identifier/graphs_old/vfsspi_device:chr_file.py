import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('bauthserver','bauthserver')
G.edge['bauthserver']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('bauthserver','vcsFPService')
G.edge['bauthserver']['vcsFPService']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bauthserver','bauthserver')
G.edge['bauthserver']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['bauthserver']['bauthserver']['fill'] = 'red'
G.add_edge('bauthserver','bauthserver')
G.edge['bauthserver']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('bauthserver','vcsFPService')
G.edge['bauthserver']['vcsFPService']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bauthserver']['vcsFPService']['fill'] = 'red'
G.add_edge('bauthserver','vcsFPService')
G.edge['bauthserver']['vcsFPService']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vcsFPService','bauthserver')
G.edge['vcsFPService']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vcsFPService','vcsFPService')
G.edge['vcsFPService']['vcsFPService']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('vcsFPService','bauthserver')
G.edge['vcsFPService']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vcsFPService']['bauthserver']['fill'] = 'red'
G.add_edge('vcsFPService','bauthserver')
G.edge['vcsFPService']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vcsFPService','vcsFPService')
G.edge['vcsFPService']['vcsFPService']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['vcsFPService']['vcsFPService']['fill'] = 'red'
G.add_edge('vcsFPService','vcsFPService')
G.edge['vcsFPService']['vcsFPService']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()