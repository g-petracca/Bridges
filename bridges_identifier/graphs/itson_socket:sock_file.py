import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('itsonclient_app','itsonclient_app')
G.edge['itsonclient_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('itsonclient_app','itsonclient_app')
G.edge['itsonclient_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('itsonclient_app','carrier_app')
G.edge['itsonclient_app']['carrier_app']['write-read'] = '[write read]'
G.edge['itsonclient_app']['carrier_app']['fill'] = 'red'
G.add_edge('itsonclient_app','filtered_google_app')
G.edge['itsonclient_app']['filtered_google_app']['write-read'] = '[write read]'
G.edge['itsonclient_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('itsonclient_app','filtered_untrusted_app')
G.edge['itsonclient_app']['filtered_untrusted_app']['write-read'] = '[write read]'
G.edge['itsonclient_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('itsonclient_app','gad_untrusted_app')
G.edge['itsonclient_app']['gad_untrusted_app']['write-read'] = '[write read]'
G.edge['itsonclient_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('itsonclient_app','irm_app')
G.edge['itsonclient_app']['irm_app']['write-read'] = '[write read]'
G.edge['itsonclient_app']['irm_app']['fill'] = 'red'
G.add_edge('itsonclient_app','itsonclient_app')
G.edge['itsonclient_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['itsonclient_app']['itsonclient_app']['fill'] = 'red'
G.add_edge('itsonclient_app','itsonclient_app')
G.edge['itsonclient_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('itsonclient_app','knox_untrusted_app')
G.edge['itsonclient_app']['knox_untrusted_app']['write-read'] = '[write read]'
G.edge['itsonclient_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('itsonclient_app','llk_untrusted_app')
G.edge['itsonclient_app']['llk_untrusted_app']['write-read'] = '[write read]'
G.edge['itsonclient_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('itsonclient_app','system_server')
G.edge['itsonclient_app']['system_server']['write-read'] = '[write read]'
G.edge['itsonclient_app']['system_server']['fill'] = 'red'
G.add_edge('itsonclient_app','trustonicpartner_app')
G.edge['itsonclient_app']['trustonicpartner_app']['write-read'] = '[write read]'
G.edge['itsonclient_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('itsonclient_app','umcagent_app')
G.edge['itsonclient_app']['umcagent_app']['write-read'] = '[write read]'
G.edge['itsonclient_app']['umcagent_app']['fill'] = 'red'
G.add_edge('itsonclient_app','untrusted_app')
G.edge['itsonclient_app']['untrusted_app']['write-read'] = '[write read]'
G.edge['itsonclient_app']['untrusted_app']['fill'] = 'red'
G.add_edge('itsonclient_app','vpn_untrusted_app')
G.edge['itsonclient_app']['vpn_untrusted_app']['write-read'] = '[write read]'
G.edge['itsonclient_app']['vpn_untrusted_app']['fill'] = 'red'
app = Viewer(G)
app.mainloop()