import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('debug_interface_proxy','debug_interface_proxy')
G.edge['debug_interface_proxy']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('debug_interface_proxy','debug_interface_proxy')
G.edge['debug_interface_proxy']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][add_name search]'
G.add_edge('debug_interface_proxy','debug_interface_proxy')
G.edge['debug_interface_proxy']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][add_name search][remove_name search]'
G.add_edge('untrusted_app','debug_interface_proxy')
G.edge['untrusted_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusted_app','debug_interface_proxy')
G.edge['untrusted_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['untrusted_app']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('untrusted_app','debug_interface_proxy')
G.edge['untrusted_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('untrusted_app','debug_interface_proxy')
G.edge['untrusted_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('umcagent_app','debug_interface_proxy')
G.edge['umcagent_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('umcagent_app','debug_interface_proxy')
G.edge['umcagent_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['umcagent_app']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('umcagent_app','debug_interface_proxy')
G.edge['umcagent_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('umcagent_app','debug_interface_proxy')
G.edge['umcagent_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('vpn_untrusted_app','debug_interface_proxy')
G.edge['vpn_untrusted_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('vpn_untrusted_app','debug_interface_proxy')
G.edge['vpn_untrusted_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['vpn_untrusted_app']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','debug_interface_proxy')
G.edge['vpn_untrusted_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('vpn_untrusted_app','debug_interface_proxy')
G.edge['vpn_untrusted_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('trustonicpartner_app','debug_interface_proxy')
G.edge['trustonicpartner_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('trustonicpartner_app','debug_interface_proxy')
G.edge['trustonicpartner_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['trustonicpartner_app']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('trustonicpartner_app','debug_interface_proxy')
G.edge['trustonicpartner_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('trustonicpartner_app','debug_interface_proxy')
G.edge['trustonicpartner_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('llk_untrusted_app','debug_interface_proxy')
G.edge['llk_untrusted_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('llk_untrusted_app','debug_interface_proxy')
G.edge['llk_untrusted_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['llk_untrusted_app']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('llk_untrusted_app','debug_interface_proxy')
G.edge['llk_untrusted_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('llk_untrusted_app','debug_interface_proxy')
G.edge['llk_untrusted_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('filtered_untrusted_app','debug_interface_proxy')
G.edge['filtered_untrusted_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_untrusted_app','debug_interface_proxy')
G.edge['filtered_untrusted_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_untrusted_app']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','debug_interface_proxy')
G.edge['filtered_untrusted_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('filtered_untrusted_app','debug_interface_proxy')
G.edge['filtered_untrusted_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('filtered_google_app','debug_interface_proxy')
G.edge['filtered_google_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_google_app','debug_interface_proxy')
G.edge['filtered_google_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_google_app']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('filtered_google_app','debug_interface_proxy')
G.edge['filtered_google_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('filtered_google_app','debug_interface_proxy')
G.edge['filtered_google_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('knox_untrusted_app','debug_interface_proxy')
G.edge['knox_untrusted_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_untrusted_app','debug_interface_proxy')
G.edge['knox_untrusted_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['knox_untrusted_app']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('knox_untrusted_app','debug_interface_proxy')
G.edge['knox_untrusted_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('knox_untrusted_app','debug_interface_proxy')
G.edge['knox_untrusted_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('irm_app','debug_interface_proxy')
G.edge['irm_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('irm_app','debug_interface_proxy')
G.edge['irm_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['irm_app']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('irm_app','debug_interface_proxy')
G.edge['irm_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('irm_app','debug_interface_proxy')
G.edge['irm_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('gad_untrusted_app','debug_interface_proxy')
G.edge['gad_untrusted_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('gad_untrusted_app','debug_interface_proxy')
G.edge['gad_untrusted_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['gad_untrusted_app']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('gad_untrusted_app','debug_interface_proxy')
G.edge['gad_untrusted_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('gad_untrusted_app','debug_interface_proxy')
G.edge['gad_untrusted_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('carrier_app','debug_interface_proxy')
G.edge['carrier_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('carrier_app','debug_interface_proxy')
G.edge['carrier_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['carrier_app']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('carrier_app','debug_interface_proxy')
G.edge['carrier_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('carrier_app','debug_interface_proxy')
G.edge['carrier_app']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('adbd','debug_interface_proxy')
G.edge['adbd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('adbd','debug_interface_proxy')
G.edge['adbd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['adbd']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('adbd','debug_interface_proxy')
G.edge['adbd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('adbd','debug_interface_proxy')
G.edge['adbd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('shell','debug_interface_proxy')
G.edge['shell']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('shell','debug_interface_proxy')
G.edge['shell']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['shell']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('shell','debug_interface_proxy')
G.edge['shell']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('shell','debug_interface_proxy')
G.edge['shell']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()