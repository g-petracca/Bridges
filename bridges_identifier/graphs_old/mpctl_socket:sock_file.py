import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('mpdecision','perfd')
G.edge['mpdecision']['perfd']['write-read'] = '[write read][open open]'
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('mpdecision','perfd')
G.edge['mpdecision']['perfd']['write-read'] = '[write read][open open][setattr getattr]'
G.add_edge('mpdecision','appdomain')
G.edge['mpdecision']['appdomain']['write-read'] = '[write read]'
G.edge['mpdecision']['appdomain']['fill'] = 'red'
G.add_edge('mpdecision','carrier_app')
G.edge['mpdecision']['carrier_app']['write-read'] = '[write read]'
G.edge['mpdecision']['carrier_app']['fill'] = 'red'
G.add_edge('mpdecision','filtered_google_app')
G.edge['mpdecision']['filtered_google_app']['write-read'] = '[write read]'
G.edge['mpdecision']['filtered_google_app']['fill'] = 'red'
G.add_edge('mpdecision','filtered_untrusted_app')
G.edge['mpdecision']['filtered_untrusted_app']['write-read'] = '[write read]'
G.edge['mpdecision']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('mpdecision','gad_untrusted_app')
G.edge['mpdecision']['gad_untrusted_app']['write-read'] = '[write read]'
G.edge['mpdecision']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('mpdecision','irm_app')
G.edge['mpdecision']['irm_app']['write-read'] = '[write read]'
G.edge['mpdecision']['irm_app']['fill'] = 'red'
G.add_edge('mpdecision','knox_untrusted_app')
G.edge['mpdecision']['knox_untrusted_app']['write-read'] = '[write read]'
G.edge['mpdecision']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('mpdecision','llk_untrusted_app')
G.edge['mpdecision']['llk_untrusted_app']['write-read'] = '[write read]'
G.edge['mpdecision']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('mpdecision','mediaserver')
G.edge['mpdecision']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read]'
G.edge['mpdecision']['mediaserver']['fill'] = 'red'
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['mpdecision']['mpdecision']['fill'] = 'red'
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mpdecision','perfd')
G.edge['mpdecision']['perfd']['write-read'] = '[write read][open open][setattr getattr][write read]'
G.edge['mpdecision']['perfd']['fill'] = 'red'
G.add_edge('mpdecision','perfd')
G.edge['mpdecision']['perfd']['write-read'] = '[write read][open open][setattr getattr][write read][append read]'
G.add_edge('mpdecision','s_system_app')
G.edge['mpdecision']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['mpdecision']['s_system_app']['fill'] = 'red'
G.add_edge('mpdecision','surfaceflinger')
G.edge['mpdecision']['surfaceflinger']['write-read'] = '[write read][append read][write read][append read][open open][write read][append read][write read][open open][write read][append read][write read]'
G.edge['mpdecision']['surfaceflinger']['fill'] = 'red'
G.add_edge('mpdecision','system_app')
G.edge['mpdecision']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['mpdecision']['system_app']['fill'] = 'red'
G.add_edge('mpdecision','system_server')
G.edge['mpdecision']['system_server']['write-read'] = '[write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][write read]'
G.edge['mpdecision']['system_server']['fill'] = 'red'
G.add_edge('mpdecision','thermal-engine')
G.edge['mpdecision']['thermal-engine']['write-read'] = '[write read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['mpdecision']['thermal-engine']['fill'] = 'red'
G.add_edge('mpdecision','trustonicpartner_app')
G.edge['mpdecision']['trustonicpartner_app']['write-read'] = '[write read]'
G.edge['mpdecision']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('mpdecision','umcagent_app')
G.edge['mpdecision']['umcagent_app']['write-read'] = '[write read]'
G.edge['mpdecision']['umcagent_app']['fill'] = 'red'
G.add_edge('mpdecision','untrusted_app')
G.edge['mpdecision']['untrusted_app']['write-read'] = '[write read]'
G.edge['mpdecision']['untrusted_app']['fill'] = 'red'
G.add_edge('mpdecision','vpn_untrusted_app')
G.edge['mpdecision']['vpn_untrusted_app']['write-read'] = '[write read]'
G.edge['mpdecision']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('perfd','mpdecision')
G.edge['perfd']['mpdecision']['write-read'] = '[open open]'
G.add_edge('perfd','perfd')
G.edge['perfd']['perfd']['write-read'] = '[open open][write read][append read][write read][open open]'
G.add_edge('perfd','mpdecision')
G.edge['perfd']['mpdecision']['write-read'] = '[open open][setattr getattr]'
G.add_edge('perfd','perfd')
G.edge['perfd']['perfd']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr]'
G.add_edge('perfd','appdomain')
G.edge['perfd']['appdomain']['write-read'] = '[write read]'
G.edge['perfd']['appdomain']['fill'] = 'red'
G.add_edge('perfd','carrier_app')
G.edge['perfd']['carrier_app']['write-read'] = '[write read]'
G.edge['perfd']['carrier_app']['fill'] = 'red'
G.add_edge('perfd','filtered_google_app')
G.edge['perfd']['filtered_google_app']['write-read'] = '[write read]'
G.edge['perfd']['filtered_google_app']['fill'] = 'red'
G.add_edge('perfd','filtered_untrusted_app')
G.edge['perfd']['filtered_untrusted_app']['write-read'] = '[write read]'
G.edge['perfd']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('perfd','gad_untrusted_app')
G.edge['perfd']['gad_untrusted_app']['write-read'] = '[write read]'
G.edge['perfd']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('perfd','irm_app')
G.edge['perfd']['irm_app']['write-read'] = '[write read]'
G.edge['perfd']['irm_app']['fill'] = 'red'
G.add_edge('perfd','knox_untrusted_app')
G.edge['perfd']['knox_untrusted_app']['write-read'] = '[write read]'
G.edge['perfd']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('perfd','llk_untrusted_app')
G.edge['perfd']['llk_untrusted_app']['write-read'] = '[write read]'
G.edge['perfd']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('perfd','mediaserver')
G.edge['perfd']['mediaserver']['write-read'] = '[write read]'
G.edge['perfd']['mediaserver']['fill'] = 'red'
G.add_edge('perfd','mpdecision')
G.edge['perfd']['mpdecision']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['perfd']['mpdecision']['fill'] = 'red'
G.add_edge('perfd','mpdecision')
G.edge['perfd']['mpdecision']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('perfd','perfd')
G.edge['perfd']['perfd']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read]'
G.edge['perfd']['perfd']['fill'] = 'red'
G.add_edge('perfd','perfd')
G.edge['perfd']['perfd']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('perfd','s_system_app')
G.edge['perfd']['s_system_app']['write-read'] = '[write read]'
G.edge['perfd']['s_system_app']['fill'] = 'red'
G.add_edge('perfd','surfaceflinger')
G.edge['perfd']['surfaceflinger']['write-read'] = '[write read][append read][write read]'
G.edge['perfd']['surfaceflinger']['fill'] = 'red'
G.add_edge('perfd','system_app')
G.edge['perfd']['system_app']['write-read'] = '[write read]'
G.edge['perfd']['system_app']['fill'] = 'red'
G.add_edge('perfd','system_server')
G.edge['perfd']['system_server']['write-read'] = '[write read][append read][write read]'
G.edge['perfd']['system_server']['fill'] = 'red'
G.add_edge('perfd','thermal-engine')
G.edge['perfd']['thermal-engine']['write-read'] = '[write read]'
G.edge['perfd']['thermal-engine']['fill'] = 'red'
G.add_edge('perfd','trustonicpartner_app')
G.edge['perfd']['trustonicpartner_app']['write-read'] = '[write read]'
G.edge['perfd']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('perfd','umcagent_app')
G.edge['perfd']['umcagent_app']['write-read'] = '[write read]'
G.edge['perfd']['umcagent_app']['fill'] = 'red'
G.add_edge('perfd','untrusted_app')
G.edge['perfd']['untrusted_app']['write-read'] = '[write read]'
G.edge['perfd']['untrusted_app']['fill'] = 'red'
G.add_edge('perfd','vpn_untrusted_app')
G.edge['perfd']['vpn_untrusted_app']['write-read'] = '[write read]'
G.edge['perfd']['vpn_untrusted_app']['fill'] = 'red'
app = Viewer(G)
app.mainloop()