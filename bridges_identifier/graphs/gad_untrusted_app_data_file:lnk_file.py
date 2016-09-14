import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('adbd','apaservice')
G.edge['adbd']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('adbd','carrier_app')
G.edge['adbd']['carrier_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open]'
G.add_edge('adbd','filtered_google_app')
G.edge['adbd']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open]'
G.add_edge('adbd','filtered_untrusted_app')
G.edge['adbd']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open]'
G.add_edge('adbd','gad_untrusted_app')
G.edge['adbd']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open]'
G.add_edge('adbd','good_app')
G.edge['adbd']['good_app']['write-read'] = '[open open][write read][append read][add_name search][remove_name search][open open]'
G.add_edge('adbd','irm_app')
G.edge['adbd']['irm_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open]'
G.add_edge('adbd','knox_untrusted_app')
G.edge['adbd']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('adbd','llk_untrusted_app')
G.edge['adbd']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open]'
G.add_edge('adbd','newAttr1')
G.edge['adbd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][open open][write read][write read][open open]'
G.add_edge('adbd','trustonicpartner_app')
G.edge['adbd']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open]'
G.add_edge('adbd','umcagent_app')
G.edge['adbd']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open]'
G.add_edge('adbd','untrusted_app')
G.edge['adbd']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open]'
G.add_edge('adbd','vpn_untrusted_app')
G.edge['adbd']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open]'
G.add_edge('adbd','carrier_app')
G.edge['adbd']['carrier_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('adbd','filtered_google_app')
G.edge['adbd']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('adbd','filtered_untrusted_app')
G.edge['adbd']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('adbd','gad_untrusted_app')
G.edge['adbd']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('adbd','good_app')
G.edge['adbd']['good_app']['write-read'] = '[open open][write read][append read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('adbd','installd')
G.edge['adbd']['installd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('adbd','installd')
G.edge['adbd']['installd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('adbd','irm_app')
G.edge['adbd']['irm_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('adbd','knox_untrusted_app')
G.edge['adbd']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('adbd','llk_untrusted_app')
G.edge['adbd']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('adbd','newAttr1')
G.edge['adbd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][open open][write read][write read][open open][setattr getattr]'
G.add_edge('adbd','trustonicpartner_app')
G.edge['adbd']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('adbd','umcagent_app')
G.edge['adbd']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('adbd','untrusted_app')
G.edge['adbd']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('adbd','vpn_untrusted_app')
G.edge['adbd']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('adbd','apaservice')
G.edge['adbd']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['adbd']['apaservice']['fill'] = 'red'
G.add_edge('adbd','apaservice')
G.edge['adbd']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('adbd','carrier_app')
G.edge['adbd']['carrier_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['adbd']['carrier_app']['fill'] = 'red'
G.add_edge('adbd','carrier_app')
G.edge['adbd']['carrier_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('adbd','filtered_google_app')
G.edge['adbd']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['adbd']['filtered_google_app']['fill'] = 'red'
G.add_edge('adbd','filtered_google_app')
G.edge['adbd']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('adbd','filtered_untrusted_app')
G.edge['adbd']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['adbd']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('adbd','filtered_untrusted_app')
G.edge['adbd']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('adbd','gad_untrusted_app')
G.edge['adbd']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['adbd']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('adbd','gad_untrusted_app')
G.edge['adbd']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('adbd','good_app')
G.edge['adbd']['good_app']['write-read'] = '[open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['adbd']['good_app']['fill'] = 'red'
G.add_edge('adbd','good_app')
G.edge['adbd']['good_app']['write-read'] = '[open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('adbd','irm_app')
G.edge['adbd']['irm_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['adbd']['irm_app']['fill'] = 'red'
G.add_edge('adbd','irm_app')
G.edge['adbd']['irm_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('adbd','knox_untrusted_app')
G.edge['adbd']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['adbd']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('adbd','knox_untrusted_app')
G.edge['adbd']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('adbd','llk_untrusted_app')
G.edge['adbd']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['adbd']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('adbd','llk_untrusted_app')
G.edge['adbd']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('adbd','newAttr1')
G.edge['adbd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['adbd']['newAttr1']['fill'] = 'red'
G.add_edge('adbd','newAttr1')
G.edge['adbd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('adbd','trustonicpartner_app')
G.edge['adbd']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['adbd']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('adbd','trustonicpartner_app')
G.edge['adbd']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('adbd','umcagent_app')
G.edge['adbd']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['adbd']['umcagent_app']['fill'] = 'red'
G.add_edge('adbd','umcagent_app')
G.edge['adbd']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('adbd','untrusted_app')
G.edge['adbd']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['adbd']['untrusted_app']['fill'] = 'red'
G.add_edge('adbd','untrusted_app')
G.edge['adbd']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('adbd','vpn_untrusted_app')
G.edge['adbd']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['adbd']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('adbd','vpn_untrusted_app')
G.edge['adbd']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('apaservice','apaservice')
G.edge['apaservice']['apaservice']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('apaservice','carrier_app')
G.edge['apaservice']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('apaservice','filtered_google_app')
G.edge['apaservice']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('apaservice','filtered_untrusted_app')
G.edge['apaservice']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('apaservice','gad_untrusted_app')
G.edge['apaservice']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('apaservice','good_app')
G.edge['apaservice']['good_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('apaservice','irm_app')
G.edge['apaservice']['irm_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('apaservice','knox_untrusted_app')
G.edge['apaservice']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('apaservice','llk_untrusted_app')
G.edge['apaservice']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('apaservice','newAttr1')
G.edge['apaservice']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('apaservice','trustonicpartner_app')
G.edge['apaservice']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('apaservice','umcagent_app')
G.edge['apaservice']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('apaservice','untrusted_app')
G.edge['apaservice']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('apaservice','vpn_untrusted_app')
G.edge['apaservice']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('apaservice','carrier_app')
G.edge['apaservice']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('apaservice','filtered_google_app')
G.edge['apaservice']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('apaservice','filtered_untrusted_app')
G.edge['apaservice']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('apaservice','gad_untrusted_app')
G.edge['apaservice']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('apaservice','good_app')
G.edge['apaservice']['good_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('apaservice','installd')
G.edge['apaservice']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('apaservice','installd')
G.edge['apaservice']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('apaservice','irm_app')
G.edge['apaservice']['irm_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('apaservice','knox_untrusted_app')
G.edge['apaservice']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('apaservice','llk_untrusted_app')
G.edge['apaservice']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('apaservice','newAttr1')
G.edge['apaservice']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('apaservice','trustonicpartner_app')
G.edge['apaservice']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('apaservice','umcagent_app')
G.edge['apaservice']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('apaservice','untrusted_app')
G.edge['apaservice']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('apaservice','vpn_untrusted_app')
G.edge['apaservice']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('apaservice','apaservice')
G.edge['apaservice']['apaservice']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['apaservice']['apaservice']['fill'] = 'red'
G.add_edge('apaservice','apaservice')
G.edge['apaservice']['apaservice']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('apaservice','carrier_app')
G.edge['apaservice']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['apaservice']['carrier_app']['fill'] = 'red'
G.add_edge('apaservice','carrier_app')
G.edge['apaservice']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('apaservice','filtered_google_app')
G.edge['apaservice']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['apaservice']['filtered_google_app']['fill'] = 'red'
G.add_edge('apaservice','filtered_google_app')
G.edge['apaservice']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('apaservice','filtered_untrusted_app')
G.edge['apaservice']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['apaservice']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('apaservice','filtered_untrusted_app')
G.edge['apaservice']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('apaservice','gad_untrusted_app')
G.edge['apaservice']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['apaservice']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('apaservice','gad_untrusted_app')
G.edge['apaservice']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('apaservice','good_app')
G.edge['apaservice']['good_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['apaservice']['good_app']['fill'] = 'red'
G.add_edge('apaservice','good_app')
G.edge['apaservice']['good_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('apaservice','irm_app')
G.edge['apaservice']['irm_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['apaservice']['irm_app']['fill'] = 'red'
G.add_edge('apaservice','irm_app')
G.edge['apaservice']['irm_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('apaservice','knox_untrusted_app')
G.edge['apaservice']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['apaservice']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('apaservice','knox_untrusted_app')
G.edge['apaservice']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('apaservice','llk_untrusted_app')
G.edge['apaservice']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['apaservice']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('apaservice','llk_untrusted_app')
G.edge['apaservice']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('apaservice','newAttr1')
G.edge['apaservice']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['apaservice']['newAttr1']['fill'] = 'red'
G.add_edge('apaservice','newAttr1')
G.edge['apaservice']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('apaservice','trustonicpartner_app')
G.edge['apaservice']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['apaservice']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('apaservice','trustonicpartner_app')
G.edge['apaservice']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('apaservice','umcagent_app')
G.edge['apaservice']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['apaservice']['umcagent_app']['fill'] = 'red'
G.add_edge('apaservice','umcagent_app')
G.edge['apaservice']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('apaservice','untrusted_app')
G.edge['apaservice']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['apaservice']['untrusted_app']['fill'] = 'red'
G.add_edge('apaservice','untrusted_app')
G.edge['apaservice']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('apaservice','vpn_untrusted_app')
G.edge['apaservice']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['apaservice']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('apaservice','vpn_untrusted_app')
G.edge['apaservice']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','apaservice')
G.edge['carrier_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('carrier_app','carrier_app')
G.edge['carrier_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('carrier_app','filtered_google_app')
G.edge['carrier_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('carrier_app','filtered_untrusted_app')
G.edge['carrier_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('carrier_app','gad_untrusted_app')
G.edge['carrier_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('carrier_app','good_app')
G.edge['carrier_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('carrier_app','irm_app')
G.edge['carrier_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('carrier_app','knox_untrusted_app')
G.edge['carrier_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('carrier_app','llk_untrusted_app')
G.edge['carrier_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('carrier_app','newAttr1')
G.edge['carrier_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('carrier_app','trustonicpartner_app')
G.edge['carrier_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('carrier_app','umcagent_app')
G.edge['carrier_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('carrier_app','untrusted_app')
G.edge['carrier_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('carrier_app','vpn_untrusted_app')
G.edge['carrier_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('carrier_app','carrier_app')
G.edge['carrier_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('carrier_app','filtered_google_app')
G.edge['carrier_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('carrier_app','filtered_untrusted_app')
G.edge['carrier_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('carrier_app','gad_untrusted_app')
G.edge['carrier_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('carrier_app','good_app')
G.edge['carrier_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('carrier_app','installd')
G.edge['carrier_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('carrier_app','installd')
G.edge['carrier_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('carrier_app','irm_app')
G.edge['carrier_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('carrier_app','knox_untrusted_app')
G.edge['carrier_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('carrier_app','llk_untrusted_app')
G.edge['carrier_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('carrier_app','newAttr1')
G.edge['carrier_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('carrier_app','trustonicpartner_app')
G.edge['carrier_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('carrier_app','umcagent_app')
G.edge['carrier_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('carrier_app','untrusted_app')
G.edge['carrier_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('carrier_app','vpn_untrusted_app')
G.edge['carrier_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('carrier_app','apaservice')
G.edge['carrier_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['carrier_app']['apaservice']['fill'] = 'red'
G.add_edge('carrier_app','apaservice')
G.edge['carrier_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('carrier_app','carrier_app')
G.edge['carrier_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['carrier_app']['carrier_app']['fill'] = 'red'
G.add_edge('carrier_app','carrier_app')
G.edge['carrier_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','filtered_google_app')
G.edge['carrier_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['carrier_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('carrier_app','filtered_google_app')
G.edge['carrier_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','filtered_untrusted_app')
G.edge['carrier_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['carrier_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('carrier_app','filtered_untrusted_app')
G.edge['carrier_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','gad_untrusted_app')
G.edge['carrier_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['carrier_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('carrier_app','gad_untrusted_app')
G.edge['carrier_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','good_app')
G.edge['carrier_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['carrier_app']['good_app']['fill'] = 'red'
G.add_edge('carrier_app','good_app')
G.edge['carrier_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','irm_app')
G.edge['carrier_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['carrier_app']['irm_app']['fill'] = 'red'
G.add_edge('carrier_app','irm_app')
G.edge['carrier_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','knox_untrusted_app')
G.edge['carrier_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['carrier_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('carrier_app','knox_untrusted_app')
G.edge['carrier_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','llk_untrusted_app')
G.edge['carrier_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['carrier_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('carrier_app','llk_untrusted_app')
G.edge['carrier_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','newAttr1')
G.edge['carrier_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['carrier_app']['newAttr1']['fill'] = 'red'
G.add_edge('carrier_app','newAttr1')
G.edge['carrier_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','trustonicpartner_app')
G.edge['carrier_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['carrier_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('carrier_app','trustonicpartner_app')
G.edge['carrier_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','umcagent_app')
G.edge['carrier_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['carrier_app']['umcagent_app']['fill'] = 'red'
G.add_edge('carrier_app','umcagent_app')
G.edge['carrier_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','untrusted_app')
G.edge['carrier_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['carrier_app']['untrusted_app']['fill'] = 'red'
G.add_edge('carrier_app','untrusted_app')
G.edge['carrier_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','vpn_untrusted_app')
G.edge['carrier_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['carrier_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('carrier_app','vpn_untrusted_app')
G.edge['carrier_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('DMM-daemon','apaservice')
G.edge['DMM-daemon']['apaservice']['write-read'] = '[open open]'
G.add_edge('DMM-daemon','carrier_app')
G.edge['DMM-daemon']['carrier_app']['write-read'] = '[open open]'
G.add_edge('DMM-daemon','filtered_google_app')
G.edge['DMM-daemon']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('DMM-daemon','filtered_untrusted_app')
G.edge['DMM-daemon']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('DMM-daemon','gad_untrusted_app')
G.edge['DMM-daemon']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('DMM-daemon','good_app')
G.edge['DMM-daemon']['good_app']['write-read'] = '[open open]'
G.add_edge('DMM-daemon','irm_app')
G.edge['DMM-daemon']['irm_app']['write-read'] = '[open open]'
G.add_edge('DMM-daemon','knox_untrusted_app')
G.edge['DMM-daemon']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('DMM-daemon','llk_untrusted_app')
G.edge['DMM-daemon']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('DMM-daemon','newAttr1')
G.edge['DMM-daemon']['newAttr1']['write-read'] = '[open open]'
G.add_edge('DMM-daemon','trustonicpartner_app')
G.edge['DMM-daemon']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('DMM-daemon','umcagent_app')
G.edge['DMM-daemon']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('DMM-daemon','untrusted_app')
G.edge['DMM-daemon']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('DMM-daemon','vpn_untrusted_app')
G.edge['DMM-daemon']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('DMM-daemon','carrier_app')
G.edge['DMM-daemon']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('DMM-daemon','filtered_google_app')
G.edge['DMM-daemon']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('DMM-daemon','filtered_untrusted_app')
G.edge['DMM-daemon']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('DMM-daemon','gad_untrusted_app')
G.edge['DMM-daemon']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('DMM-daemon','good_app')
G.edge['DMM-daemon']['good_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('DMM-daemon','installd')
G.edge['DMM-daemon']['installd']['write-read'] = '[setattr getattr]'
G.add_edge('DMM-daemon','installd')
G.edge['DMM-daemon']['installd']['write-read'] = '[setattr getattr][setattr getattr]'
G.add_edge('DMM-daemon','irm_app')
G.edge['DMM-daemon']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('DMM-daemon','knox_untrusted_app')
G.edge['DMM-daemon']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('DMM-daemon','llk_untrusted_app')
G.edge['DMM-daemon']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('DMM-daemon','newAttr1')
G.edge['DMM-daemon']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('DMM-daemon','trustonicpartner_app')
G.edge['DMM-daemon']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('DMM-daemon','umcagent_app')
G.edge['DMM-daemon']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('DMM-daemon','untrusted_app')
G.edge['DMM-daemon']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('DMM-daemon','vpn_untrusted_app')
G.edge['DMM-daemon']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('DMM-daemon','apaservice')
G.edge['DMM-daemon']['apaservice']['write-read'] = '[open open][write read]'
G.edge['DMM-daemon']['apaservice']['fill'] = 'red'
G.add_edge('DMM-daemon','apaservice')
G.edge['DMM-daemon']['apaservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('DMM-daemon','carrier_app')
G.edge['DMM-daemon']['carrier_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['DMM-daemon']['carrier_app']['fill'] = 'red'
G.add_edge('DMM-daemon','carrier_app')
G.edge['DMM-daemon']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('DMM-daemon','filtered_google_app')
G.edge['DMM-daemon']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['DMM-daemon']['filtered_google_app']['fill'] = 'red'
G.add_edge('DMM-daemon','filtered_google_app')
G.edge['DMM-daemon']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('DMM-daemon','filtered_untrusted_app')
G.edge['DMM-daemon']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['DMM-daemon']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('DMM-daemon','filtered_untrusted_app')
G.edge['DMM-daemon']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('DMM-daemon','gad_untrusted_app')
G.edge['DMM-daemon']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['DMM-daemon']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('DMM-daemon','gad_untrusted_app')
G.edge['DMM-daemon']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('DMM-daemon','good_app')
G.edge['DMM-daemon']['good_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['DMM-daemon']['good_app']['fill'] = 'red'
G.add_edge('DMM-daemon','good_app')
G.edge['DMM-daemon']['good_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('DMM-daemon','irm_app')
G.edge['DMM-daemon']['irm_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['DMM-daemon']['irm_app']['fill'] = 'red'
G.add_edge('DMM-daemon','irm_app')
G.edge['DMM-daemon']['irm_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('DMM-daemon','knox_untrusted_app')
G.edge['DMM-daemon']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['DMM-daemon']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('DMM-daemon','knox_untrusted_app')
G.edge['DMM-daemon']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('DMM-daemon','llk_untrusted_app')
G.edge['DMM-daemon']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['DMM-daemon']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('DMM-daemon','llk_untrusted_app')
G.edge['DMM-daemon']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('DMM-daemon','newAttr1')
G.edge['DMM-daemon']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['DMM-daemon']['newAttr1']['fill'] = 'red'
G.add_edge('DMM-daemon','newAttr1')
G.edge['DMM-daemon']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('DMM-daemon','trustonicpartner_app')
G.edge['DMM-daemon']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['DMM-daemon']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('DMM-daemon','trustonicpartner_app')
G.edge['DMM-daemon']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('DMM-daemon','umcagent_app')
G.edge['DMM-daemon']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['DMM-daemon']['umcagent_app']['fill'] = 'red'
G.add_edge('DMM-daemon','umcagent_app')
G.edge['DMM-daemon']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('DMM-daemon','untrusted_app')
G.edge['DMM-daemon']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['DMM-daemon']['untrusted_app']['fill'] = 'red'
G.add_edge('DMM-daemon','untrusted_app')
G.edge['DMM-daemon']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('DMM-daemon','vpn_untrusted_app')
G.edge['DMM-daemon']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['DMM-daemon']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('DMM-daemon','vpn_untrusted_app')
G.edge['DMM-daemon']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('drmserver','apaservice')
G.edge['drmserver']['apaservice']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('drmserver','carrier_app')
G.edge['drmserver']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('drmserver','filtered_google_app')
G.edge['drmserver']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('drmserver','filtered_untrusted_app')
G.edge['drmserver']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('drmserver','gad_untrusted_app')
G.edge['drmserver']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('drmserver','good_app')
G.edge['drmserver']['good_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('drmserver','irm_app')
G.edge['drmserver']['irm_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('drmserver','knox_untrusted_app')
G.edge['drmserver']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('drmserver','llk_untrusted_app')
G.edge['drmserver']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('drmserver','newAttr1')
G.edge['drmserver']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('drmserver','trustonicpartner_app')
G.edge['drmserver']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('drmserver','umcagent_app')
G.edge['drmserver']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('drmserver','untrusted_app')
G.edge['drmserver']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('drmserver','vpn_untrusted_app')
G.edge['drmserver']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('drmserver','carrier_app')
G.edge['drmserver']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('drmserver','filtered_google_app')
G.edge['drmserver']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('drmserver','filtered_untrusted_app')
G.edge['drmserver']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('drmserver','gad_untrusted_app')
G.edge['drmserver']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('drmserver','good_app')
G.edge['drmserver']['good_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('drmserver','installd')
G.edge['drmserver']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('drmserver','installd')
G.edge['drmserver']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('drmserver','irm_app')
G.edge['drmserver']['irm_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('drmserver','knox_untrusted_app')
G.edge['drmserver']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('drmserver','llk_untrusted_app')
G.edge['drmserver']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('drmserver','newAttr1')
G.edge['drmserver']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('drmserver','trustonicpartner_app')
G.edge['drmserver']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('drmserver','umcagent_app')
G.edge['drmserver']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('drmserver','untrusted_app')
G.edge['drmserver']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('drmserver','vpn_untrusted_app')
G.edge['drmserver']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('drmserver','apaservice')
G.edge['drmserver']['apaservice']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['drmserver']['apaservice']['fill'] = 'red'
G.add_edge('drmserver','apaservice')
G.edge['drmserver']['apaservice']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('drmserver','carrier_app')
G.edge['drmserver']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['drmserver']['carrier_app']['fill'] = 'red'
G.add_edge('drmserver','carrier_app')
G.edge['drmserver']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('drmserver','filtered_google_app')
G.edge['drmserver']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['drmserver']['filtered_google_app']['fill'] = 'red'
G.add_edge('drmserver','filtered_google_app')
G.edge['drmserver']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('drmserver','filtered_untrusted_app')
G.edge['drmserver']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['drmserver']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('drmserver','filtered_untrusted_app')
G.edge['drmserver']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('drmserver','gad_untrusted_app')
G.edge['drmserver']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['drmserver']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('drmserver','gad_untrusted_app')
G.edge['drmserver']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('drmserver','good_app')
G.edge['drmserver']['good_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['drmserver']['good_app']['fill'] = 'red'
G.add_edge('drmserver','good_app')
G.edge['drmserver']['good_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('drmserver','irm_app')
G.edge['drmserver']['irm_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['drmserver']['irm_app']['fill'] = 'red'
G.add_edge('drmserver','irm_app')
G.edge['drmserver']['irm_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('drmserver','knox_untrusted_app')
G.edge['drmserver']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['drmserver']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('drmserver','knox_untrusted_app')
G.edge['drmserver']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('drmserver','llk_untrusted_app')
G.edge['drmserver']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['drmserver']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('drmserver','llk_untrusted_app')
G.edge['drmserver']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('drmserver','newAttr1')
G.edge['drmserver']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['drmserver']['newAttr1']['fill'] = 'red'
G.add_edge('drmserver','newAttr1')
G.edge['drmserver']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('drmserver','trustonicpartner_app')
G.edge['drmserver']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['drmserver']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('drmserver','trustonicpartner_app')
G.edge['drmserver']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('drmserver','umcagent_app')
G.edge['drmserver']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['drmserver']['umcagent_app']['fill'] = 'red'
G.add_edge('drmserver','umcagent_app')
G.edge['drmserver']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('drmserver','untrusted_app')
G.edge['drmserver']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['drmserver']['untrusted_app']['fill'] = 'red'
G.add_edge('drmserver','untrusted_app')
G.edge['drmserver']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('drmserver','vpn_untrusted_app')
G.edge['drmserver']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['drmserver']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('drmserver','vpn_untrusted_app')
G.edge['drmserver']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','apaservice')
G.edge['filtered_google_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_google_app','carrier_app')
G.edge['filtered_google_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('filtered_google_app','filtered_google_app')
G.edge['filtered_google_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('filtered_google_app','filtered_untrusted_app')
G.edge['filtered_google_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('filtered_google_app','gad_untrusted_app')
G.edge['filtered_google_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('filtered_google_app','good_app')
G.edge['filtered_google_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('filtered_google_app','irm_app')
G.edge['filtered_google_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('filtered_google_app','knox_untrusted_app')
G.edge['filtered_google_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('filtered_google_app','llk_untrusted_app')
G.edge['filtered_google_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('filtered_google_app','newAttr1')
G.edge['filtered_google_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('filtered_google_app','trustonicpartner_app')
G.edge['filtered_google_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('filtered_google_app','umcagent_app')
G.edge['filtered_google_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('filtered_google_app','untrusted_app')
G.edge['filtered_google_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('filtered_google_app','vpn_untrusted_app')
G.edge['filtered_google_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('filtered_google_app','carrier_app')
G.edge['filtered_google_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('filtered_google_app','filtered_google_app')
G.edge['filtered_google_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('filtered_google_app','filtered_untrusted_app')
G.edge['filtered_google_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('filtered_google_app','gad_untrusted_app')
G.edge['filtered_google_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('filtered_google_app','good_app')
G.edge['filtered_google_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('filtered_google_app','installd')
G.edge['filtered_google_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('filtered_google_app','installd')
G.edge['filtered_google_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('filtered_google_app','irm_app')
G.edge['filtered_google_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('filtered_google_app','knox_untrusted_app')
G.edge['filtered_google_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('filtered_google_app','llk_untrusted_app')
G.edge['filtered_google_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('filtered_google_app','newAttr1')
G.edge['filtered_google_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('filtered_google_app','trustonicpartner_app')
G.edge['filtered_google_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('filtered_google_app','umcagent_app')
G.edge['filtered_google_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('filtered_google_app','untrusted_app')
G.edge['filtered_google_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('filtered_google_app','vpn_untrusted_app')
G.edge['filtered_google_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('filtered_google_app','apaservice')
G.edge['filtered_google_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_google_app']['apaservice']['fill'] = 'red'
G.add_edge('filtered_google_app','apaservice')
G.edge['filtered_google_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('filtered_google_app','carrier_app')
G.edge['filtered_google_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['filtered_google_app']['carrier_app']['fill'] = 'red'
G.add_edge('filtered_google_app','carrier_app')
G.edge['filtered_google_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','filtered_google_app')
G.edge['filtered_google_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['filtered_google_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('filtered_google_app','filtered_google_app')
G.edge['filtered_google_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','filtered_untrusted_app')
G.edge['filtered_google_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['filtered_google_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_google_app','filtered_untrusted_app')
G.edge['filtered_google_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','gad_untrusted_app')
G.edge['filtered_google_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['filtered_google_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_google_app','gad_untrusted_app')
G.edge['filtered_google_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','good_app')
G.edge['filtered_google_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['filtered_google_app']['good_app']['fill'] = 'red'
G.add_edge('filtered_google_app','good_app')
G.edge['filtered_google_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','irm_app')
G.edge['filtered_google_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['filtered_google_app']['irm_app']['fill'] = 'red'
G.add_edge('filtered_google_app','irm_app')
G.edge['filtered_google_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','knox_untrusted_app')
G.edge['filtered_google_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['filtered_google_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_google_app','knox_untrusted_app')
G.edge['filtered_google_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','llk_untrusted_app')
G.edge['filtered_google_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['filtered_google_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_google_app','llk_untrusted_app')
G.edge['filtered_google_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','newAttr1')
G.edge['filtered_google_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['filtered_google_app']['newAttr1']['fill'] = 'red'
G.add_edge('filtered_google_app','newAttr1')
G.edge['filtered_google_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','trustonicpartner_app')
G.edge['filtered_google_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['filtered_google_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('filtered_google_app','trustonicpartner_app')
G.edge['filtered_google_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','umcagent_app')
G.edge['filtered_google_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['filtered_google_app']['umcagent_app']['fill'] = 'red'
G.add_edge('filtered_google_app','umcagent_app')
G.edge['filtered_google_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','untrusted_app')
G.edge['filtered_google_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['filtered_google_app']['untrusted_app']['fill'] = 'red'
G.add_edge('filtered_google_app','untrusted_app')
G.edge['filtered_google_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','vpn_untrusted_app')
G.edge['filtered_google_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['filtered_google_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_google_app','vpn_untrusted_app')
G.edge['filtered_google_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','apaservice')
G.edge['filtered_untrusted_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_untrusted_app','carrier_app')
G.edge['filtered_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('filtered_untrusted_app','filtered_google_app')
G.edge['filtered_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('filtered_untrusted_app','filtered_untrusted_app')
G.edge['filtered_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('filtered_untrusted_app','gad_untrusted_app')
G.edge['filtered_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('filtered_untrusted_app','good_app')
G.edge['filtered_untrusted_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('filtered_untrusted_app','irm_app')
G.edge['filtered_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('filtered_untrusted_app','knox_untrusted_app')
G.edge['filtered_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('filtered_untrusted_app','llk_untrusted_app')
G.edge['filtered_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('filtered_untrusted_app','newAttr1')
G.edge['filtered_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('filtered_untrusted_app','trustonicpartner_app')
G.edge['filtered_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('filtered_untrusted_app','umcagent_app')
G.edge['filtered_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('filtered_untrusted_app','untrusted_app')
G.edge['filtered_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('filtered_untrusted_app','vpn_untrusted_app')
G.edge['filtered_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('filtered_untrusted_app','carrier_app')
G.edge['filtered_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','filtered_google_app')
G.edge['filtered_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','filtered_untrusted_app')
G.edge['filtered_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','gad_untrusted_app')
G.edge['filtered_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','good_app')
G.edge['filtered_untrusted_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','installd')
G.edge['filtered_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('filtered_untrusted_app','installd')
G.edge['filtered_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('filtered_untrusted_app','irm_app')
G.edge['filtered_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','knox_untrusted_app')
G.edge['filtered_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','llk_untrusted_app')
G.edge['filtered_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','newAttr1')
G.edge['filtered_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','trustonicpartner_app')
G.edge['filtered_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','umcagent_app')
G.edge['filtered_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','untrusted_app')
G.edge['filtered_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','vpn_untrusted_app')
G.edge['filtered_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','apaservice')
G.edge['filtered_untrusted_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_untrusted_app']['apaservice']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','apaservice')
G.edge['filtered_untrusted_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('filtered_untrusted_app','carrier_app')
G.edge['filtered_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['carrier_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','carrier_app')
G.edge['filtered_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','filtered_google_app')
G.edge['filtered_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','filtered_google_app')
G.edge['filtered_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','filtered_untrusted_app')
G.edge['filtered_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','filtered_untrusted_app')
G.edge['filtered_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','gad_untrusted_app')
G.edge['filtered_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','gad_untrusted_app')
G.edge['filtered_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','good_app')
G.edge['filtered_untrusted_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['good_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','good_app')
G.edge['filtered_untrusted_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','irm_app')
G.edge['filtered_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['irm_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','irm_app')
G.edge['filtered_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','knox_untrusted_app')
G.edge['filtered_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','knox_untrusted_app')
G.edge['filtered_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','llk_untrusted_app')
G.edge['filtered_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','llk_untrusted_app')
G.edge['filtered_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','newAttr1')
G.edge['filtered_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['newAttr1']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','newAttr1')
G.edge['filtered_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','trustonicpartner_app')
G.edge['filtered_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','trustonicpartner_app')
G.edge['filtered_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','umcagent_app')
G.edge['filtered_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['umcagent_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','umcagent_app')
G.edge['filtered_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','untrusted_app')
G.edge['filtered_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['untrusted_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','untrusted_app')
G.edge['filtered_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','vpn_untrusted_app')
G.edge['filtered_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','vpn_untrusted_app')
G.edge['filtered_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','apaservice')
G.edge['gad_untrusted_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('gad_untrusted_app','carrier_app')
G.edge['gad_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('gad_untrusted_app','filtered_google_app')
G.edge['gad_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('gad_untrusted_app','filtered_untrusted_app')
G.edge['gad_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('gad_untrusted_app','gad_untrusted_app')
G.edge['gad_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('gad_untrusted_app','good_app')
G.edge['gad_untrusted_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('gad_untrusted_app','irm_app')
G.edge['gad_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('gad_untrusted_app','knox_untrusted_app')
G.edge['gad_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('gad_untrusted_app','llk_untrusted_app')
G.edge['gad_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('gad_untrusted_app','newAttr1')
G.edge['gad_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('gad_untrusted_app','trustonicpartner_app')
G.edge['gad_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('gad_untrusted_app','umcagent_app')
G.edge['gad_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('gad_untrusted_app','untrusted_app')
G.edge['gad_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('gad_untrusted_app','vpn_untrusted_app')
G.edge['gad_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('gad_untrusted_app','carrier_app')
G.edge['gad_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('gad_untrusted_app','filtered_google_app')
G.edge['gad_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('gad_untrusted_app','filtered_untrusted_app')
G.edge['gad_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('gad_untrusted_app','gad_untrusted_app')
G.edge['gad_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('gad_untrusted_app','good_app')
G.edge['gad_untrusted_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('gad_untrusted_app','installd')
G.edge['gad_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('gad_untrusted_app','installd')
G.edge['gad_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('gad_untrusted_app','irm_app')
G.edge['gad_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('gad_untrusted_app','knox_untrusted_app')
G.edge['gad_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('gad_untrusted_app','llk_untrusted_app')
G.edge['gad_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('gad_untrusted_app','newAttr1')
G.edge['gad_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('gad_untrusted_app','trustonicpartner_app')
G.edge['gad_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('gad_untrusted_app','umcagent_app')
G.edge['gad_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('gad_untrusted_app','untrusted_app')
G.edge['gad_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('gad_untrusted_app','vpn_untrusted_app')
G.edge['gad_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('gad_untrusted_app','apaservice')
G.edge['gad_untrusted_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['gad_untrusted_app']['apaservice']['fill'] = 'red'
G.add_edge('gad_untrusted_app','apaservice')
G.edge['gad_untrusted_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('gad_untrusted_app','carrier_app')
G.edge['gad_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['carrier_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','carrier_app')
G.edge['gad_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','filtered_google_app')
G.edge['gad_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','filtered_google_app')
G.edge['gad_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','filtered_untrusted_app')
G.edge['gad_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','filtered_untrusted_app')
G.edge['gad_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','gad_untrusted_app')
G.edge['gad_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','gad_untrusted_app')
G.edge['gad_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','good_app')
G.edge['gad_untrusted_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['good_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','good_app')
G.edge['gad_untrusted_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','irm_app')
G.edge['gad_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['irm_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','irm_app')
G.edge['gad_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','knox_untrusted_app')
G.edge['gad_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','knox_untrusted_app')
G.edge['gad_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','llk_untrusted_app')
G.edge['gad_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','llk_untrusted_app')
G.edge['gad_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','newAttr1')
G.edge['gad_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['newAttr1']['fill'] = 'red'
G.add_edge('gad_untrusted_app','newAttr1')
G.edge['gad_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','trustonicpartner_app')
G.edge['gad_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','trustonicpartner_app')
G.edge['gad_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','umcagent_app')
G.edge['gad_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['umcagent_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','umcagent_app')
G.edge['gad_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','untrusted_app')
G.edge['gad_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['untrusted_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','untrusted_app')
G.edge['gad_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','vpn_untrusted_app')
G.edge['gad_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','vpn_untrusted_app')
G.edge['gad_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('good_app','apaservice')
G.edge['good_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('good_app','carrier_app')
G.edge['good_app']['carrier_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('good_app','filtered_google_app')
G.edge['good_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('good_app','filtered_untrusted_app')
G.edge['good_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('good_app','gad_untrusted_app')
G.edge['good_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('good_app','good_app')
G.edge['good_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open]'
G.add_edge('good_app','irm_app')
G.edge['good_app']['irm_app']['write-read'] = '[open open][setattr getattr][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('good_app','knox_untrusted_app')
G.edge['good_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('good_app','llk_untrusted_app')
G.edge['good_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('good_app','newAttr1')
G.edge['good_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('good_app','trustonicpartner_app')
G.edge['good_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('good_app','umcagent_app')
G.edge['good_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('good_app','untrusted_app')
G.edge['good_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('good_app','vpn_untrusted_app')
G.edge['good_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('good_app','carrier_app')
G.edge['good_app']['carrier_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('good_app','filtered_google_app')
G.edge['good_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('good_app','filtered_untrusted_app')
G.edge['good_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('good_app','gad_untrusted_app')
G.edge['good_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('good_app','good_app')
G.edge['good_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr]'
G.add_edge('good_app','installd')
G.edge['good_app']['installd']['write-read'] = '[setattr getattr][setattr getattr][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('good_app','installd')
G.edge['good_app']['installd']['write-read'] = '[setattr getattr][setattr getattr][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('good_app','irm_app')
G.edge['good_app']['irm_app']['write-read'] = '[open open][setattr getattr][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('good_app','knox_untrusted_app')
G.edge['good_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('good_app','llk_untrusted_app')
G.edge['good_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('good_app','newAttr1')
G.edge['good_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('good_app','trustonicpartner_app')
G.edge['good_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('good_app','umcagent_app')
G.edge['good_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('good_app','untrusted_app')
G.edge['good_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('good_app','vpn_untrusted_app')
G.edge['good_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('good_app','apaservice')
G.edge['good_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['good_app']['apaservice']['fill'] = 'red'
G.add_edge('good_app','apaservice')
G.edge['good_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('good_app','carrier_app')
G.edge['good_app']['carrier_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['good_app']['carrier_app']['fill'] = 'red'
G.add_edge('good_app','carrier_app')
G.edge['good_app']['carrier_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('good_app','filtered_google_app')
G.edge['good_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['good_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('good_app','filtered_google_app')
G.edge['good_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('good_app','filtered_untrusted_app')
G.edge['good_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['good_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('good_app','filtered_untrusted_app')
G.edge['good_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('good_app','gad_untrusted_app')
G.edge['good_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['good_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('good_app','gad_untrusted_app')
G.edge['good_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('good_app','good_app')
G.edge['good_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read]'
G.edge['good_app']['good_app']['fill'] = 'red'
G.add_edge('good_app','good_app')
G.edge['good_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('good_app','irm_app')
G.edge['good_app']['irm_app']['write-read'] = '[open open][setattr getattr][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['good_app']['irm_app']['fill'] = 'red'
G.add_edge('good_app','irm_app')
G.edge['good_app']['irm_app']['write-read'] = '[open open][setattr getattr][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('good_app','knox_untrusted_app')
G.edge['good_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['good_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('good_app','knox_untrusted_app')
G.edge['good_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('good_app','llk_untrusted_app')
G.edge['good_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['good_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('good_app','llk_untrusted_app')
G.edge['good_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('good_app','newAttr1')
G.edge['good_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['good_app']['newAttr1']['fill'] = 'red'
G.add_edge('good_app','newAttr1')
G.edge['good_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('good_app','trustonicpartner_app')
G.edge['good_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['good_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('good_app','trustonicpartner_app')
G.edge['good_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('good_app','umcagent_app')
G.edge['good_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['good_app']['umcagent_app']['fill'] = 'red'
G.add_edge('good_app','umcagent_app')
G.edge['good_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('good_app','untrusted_app')
G.edge['good_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['good_app']['untrusted_app']['fill'] = 'red'
G.add_edge('good_app','untrusted_app')
G.edge['good_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('good_app','vpn_untrusted_app')
G.edge['good_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['good_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('good_app','vpn_untrusted_app')
G.edge['good_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('installd','carrier_app')
G.edge['installd']['carrier_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','filtered_google_app')
G.edge['installd']['filtered_google_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','filtered_untrusted_app')
G.edge['installd']['filtered_untrusted_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','gad_untrusted_app')
G.edge['installd']['gad_untrusted_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','good_app')
G.edge['installd']['good_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][setattr getattr]'
G.add_edge('installd','irm_app')
G.edge['installd']['irm_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','knox_untrusted_app')
G.edge['installd']['knox_untrusted_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','llk_untrusted_app')
G.edge['installd']['llk_untrusted_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','newAttr1')
G.edge['installd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','trustonicpartner_app')
G.edge['installd']['trustonicpartner_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','umcagent_app')
G.edge['installd']['umcagent_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','untrusted_app')
G.edge['installd']['untrusted_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','vpn_untrusted_app')
G.edge['installd']['vpn_untrusted_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom]'
G.add_edge('irm_app','apaservice')
G.edge['irm_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('irm_app','carrier_app')
G.edge['irm_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('irm_app','filtered_google_app')
G.edge['irm_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('irm_app','filtered_untrusted_app')
G.edge['irm_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('irm_app','gad_untrusted_app')
G.edge['irm_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('irm_app','good_app')
G.edge['irm_app']['good_app']['write-read'] = '[open open][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('irm_app','irm_app')
G.edge['irm_app']['irm_app']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][write read][open open]'
G.add_edge('irm_app','knox_untrusted_app')
G.edge['irm_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('irm_app','llk_untrusted_app')
G.edge['irm_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('irm_app','newAttr1')
G.edge['irm_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('irm_app','trustonicpartner_app')
G.edge['irm_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('irm_app','umcagent_app')
G.edge['irm_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('irm_app','untrusted_app')
G.edge['irm_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('irm_app','vpn_untrusted_app')
G.edge['irm_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('irm_app','carrier_app')
G.edge['irm_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('irm_app','filtered_google_app')
G.edge['irm_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('irm_app','filtered_untrusted_app')
G.edge['irm_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('irm_app','gad_untrusted_app')
G.edge['irm_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('irm_app','good_app')
G.edge['irm_app']['good_app']['write-read'] = '[open open][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('irm_app','installd')
G.edge['irm_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('irm_app','installd')
G.edge['irm_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('irm_app','irm_app')
G.edge['irm_app']['irm_app']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][write read][open open][setattr getattr]'
G.add_edge('irm_app','knox_untrusted_app')
G.edge['irm_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('irm_app','llk_untrusted_app')
G.edge['irm_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('irm_app','newAttr1')
G.edge['irm_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('irm_app','trustonicpartner_app')
G.edge['irm_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('irm_app','umcagent_app')
G.edge['irm_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('irm_app','untrusted_app')
G.edge['irm_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('irm_app','vpn_untrusted_app')
G.edge['irm_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('irm_app','apaservice')
G.edge['irm_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['irm_app']['apaservice']['fill'] = 'red'
G.add_edge('irm_app','apaservice')
G.edge['irm_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('irm_app','carrier_app')
G.edge['irm_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['irm_app']['carrier_app']['fill'] = 'red'
G.add_edge('irm_app','carrier_app')
G.edge['irm_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','filtered_google_app')
G.edge['irm_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['irm_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('irm_app','filtered_google_app')
G.edge['irm_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','filtered_untrusted_app')
G.edge['irm_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['irm_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('irm_app','filtered_untrusted_app')
G.edge['irm_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','gad_untrusted_app')
G.edge['irm_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['irm_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('irm_app','gad_untrusted_app')
G.edge['irm_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','good_app')
G.edge['irm_app']['good_app']['write-read'] = '[open open][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['irm_app']['good_app']['fill'] = 'red'
G.add_edge('irm_app','good_app')
G.edge['irm_app']['good_app']['write-read'] = '[open open][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','irm_app')
G.edge['irm_app']['irm_app']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['irm_app']['irm_app']['fill'] = 'red'
G.add_edge('irm_app','irm_app')
G.edge['irm_app']['irm_app']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','knox_untrusted_app')
G.edge['irm_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['irm_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('irm_app','knox_untrusted_app')
G.edge['irm_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','llk_untrusted_app')
G.edge['irm_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['irm_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('irm_app','llk_untrusted_app')
G.edge['irm_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','newAttr1')
G.edge['irm_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['irm_app']['newAttr1']['fill'] = 'red'
G.add_edge('irm_app','newAttr1')
G.edge['irm_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','trustonicpartner_app')
G.edge['irm_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['irm_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('irm_app','trustonicpartner_app')
G.edge['irm_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','umcagent_app')
G.edge['irm_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['irm_app']['umcagent_app']['fill'] = 'red'
G.add_edge('irm_app','umcagent_app')
G.edge['irm_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','untrusted_app')
G.edge['irm_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['irm_app']['untrusted_app']['fill'] = 'red'
G.add_edge('irm_app','untrusted_app')
G.edge['irm_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','vpn_untrusted_app')
G.edge['irm_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['irm_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('irm_app','vpn_untrusted_app')
G.edge['irm_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','apaservice')
G.edge['knox_untrusted_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_untrusted_app','carrier_app')
G.edge['knox_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('knox_untrusted_app','filtered_google_app')
G.edge['knox_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('knox_untrusted_app','filtered_untrusted_app')
G.edge['knox_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('knox_untrusted_app','gad_untrusted_app')
G.edge['knox_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('knox_untrusted_app','good_app')
G.edge['knox_untrusted_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('knox_untrusted_app','irm_app')
G.edge['knox_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('knox_untrusted_app','knox_untrusted_app')
G.edge['knox_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_untrusted_app','llk_untrusted_app')
G.edge['knox_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('knox_untrusted_app','newAttr1')
G.edge['knox_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('knox_untrusted_app','trustonicpartner_app')
G.edge['knox_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('knox_untrusted_app','umcagent_app')
G.edge['knox_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('knox_untrusted_app','untrusted_app')
G.edge['knox_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('knox_untrusted_app','vpn_untrusted_app')
G.edge['knox_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('knox_untrusted_app','carrier_app')
G.edge['knox_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('knox_untrusted_app','filtered_google_app')
G.edge['knox_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('knox_untrusted_app','filtered_untrusted_app')
G.edge['knox_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('knox_untrusted_app','gad_untrusted_app')
G.edge['knox_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('knox_untrusted_app','good_app')
G.edge['knox_untrusted_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('knox_untrusted_app','installd')
G.edge['knox_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('knox_untrusted_app','installd')
G.edge['knox_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('knox_untrusted_app','irm_app')
G.edge['knox_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('knox_untrusted_app','knox_untrusted_app')
G.edge['knox_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('knox_untrusted_app','llk_untrusted_app')
G.edge['knox_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('knox_untrusted_app','newAttr1')
G.edge['knox_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('knox_untrusted_app','trustonicpartner_app')
G.edge['knox_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('knox_untrusted_app','umcagent_app')
G.edge['knox_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('knox_untrusted_app','untrusted_app')
G.edge['knox_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('knox_untrusted_app','vpn_untrusted_app')
G.edge['knox_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('knox_untrusted_app','apaservice')
G.edge['knox_untrusted_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['knox_untrusted_app']['apaservice']['fill'] = 'red'
G.add_edge('knox_untrusted_app','apaservice')
G.edge['knox_untrusted_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('knox_untrusted_app','carrier_app')
G.edge['knox_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['carrier_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','carrier_app')
G.edge['knox_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','filtered_google_app')
G.edge['knox_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','filtered_google_app')
G.edge['knox_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','filtered_untrusted_app')
G.edge['knox_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','filtered_untrusted_app')
G.edge['knox_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','gad_untrusted_app')
G.edge['knox_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','gad_untrusted_app')
G.edge['knox_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','good_app')
G.edge['knox_untrusted_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['good_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','good_app')
G.edge['knox_untrusted_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','irm_app')
G.edge['knox_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['irm_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','irm_app')
G.edge['knox_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','knox_untrusted_app')
G.edge['knox_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','knox_untrusted_app')
G.edge['knox_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','llk_untrusted_app')
G.edge['knox_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','llk_untrusted_app')
G.edge['knox_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','newAttr1')
G.edge['knox_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['newAttr1']['fill'] = 'red'
G.add_edge('knox_untrusted_app','newAttr1')
G.edge['knox_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','trustonicpartner_app')
G.edge['knox_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','trustonicpartner_app')
G.edge['knox_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','umcagent_app')
G.edge['knox_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['umcagent_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','umcagent_app')
G.edge['knox_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','untrusted_app')
G.edge['knox_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['untrusted_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','untrusted_app')
G.edge['knox_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','vpn_untrusted_app')
G.edge['knox_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','vpn_untrusted_app')
G.edge['knox_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','apaservice')
G.edge['llk_untrusted_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('llk_untrusted_app','carrier_app')
G.edge['llk_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('llk_untrusted_app','filtered_google_app')
G.edge['llk_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('llk_untrusted_app','filtered_untrusted_app')
G.edge['llk_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('llk_untrusted_app','gad_untrusted_app')
G.edge['llk_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('llk_untrusted_app','good_app')
G.edge['llk_untrusted_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('llk_untrusted_app','irm_app')
G.edge['llk_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('llk_untrusted_app','knox_untrusted_app')
G.edge['llk_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('llk_untrusted_app','llk_untrusted_app')
G.edge['llk_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('llk_untrusted_app','newAttr1')
G.edge['llk_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('llk_untrusted_app','trustonicpartner_app')
G.edge['llk_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('llk_untrusted_app','umcagent_app')
G.edge['llk_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('llk_untrusted_app','untrusted_app')
G.edge['llk_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('llk_untrusted_app','vpn_untrusted_app')
G.edge['llk_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('llk_untrusted_app','carrier_app')
G.edge['llk_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('llk_untrusted_app','filtered_google_app')
G.edge['llk_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('llk_untrusted_app','filtered_untrusted_app')
G.edge['llk_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('llk_untrusted_app','gad_untrusted_app')
G.edge['llk_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('llk_untrusted_app','good_app')
G.edge['llk_untrusted_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('llk_untrusted_app','installd')
G.edge['llk_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('llk_untrusted_app','installd')
G.edge['llk_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('llk_untrusted_app','irm_app')
G.edge['llk_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('llk_untrusted_app','knox_untrusted_app')
G.edge['llk_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('llk_untrusted_app','llk_untrusted_app')
G.edge['llk_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('llk_untrusted_app','newAttr1')
G.edge['llk_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('llk_untrusted_app','trustonicpartner_app')
G.edge['llk_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('llk_untrusted_app','umcagent_app')
G.edge['llk_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('llk_untrusted_app','untrusted_app')
G.edge['llk_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('llk_untrusted_app','vpn_untrusted_app')
G.edge['llk_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('llk_untrusted_app','apaservice')
G.edge['llk_untrusted_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['llk_untrusted_app']['apaservice']['fill'] = 'red'
G.add_edge('llk_untrusted_app','apaservice')
G.edge['llk_untrusted_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('llk_untrusted_app','carrier_app')
G.edge['llk_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['carrier_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','carrier_app')
G.edge['llk_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','filtered_google_app')
G.edge['llk_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','filtered_google_app')
G.edge['llk_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','filtered_untrusted_app')
G.edge['llk_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','filtered_untrusted_app')
G.edge['llk_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','gad_untrusted_app')
G.edge['llk_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','gad_untrusted_app')
G.edge['llk_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','good_app')
G.edge['llk_untrusted_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['good_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','good_app')
G.edge['llk_untrusted_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','irm_app')
G.edge['llk_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['irm_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','irm_app')
G.edge['llk_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','knox_untrusted_app')
G.edge['llk_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','knox_untrusted_app')
G.edge['llk_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','llk_untrusted_app')
G.edge['llk_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','llk_untrusted_app')
G.edge['llk_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','newAttr1')
G.edge['llk_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['newAttr1']['fill'] = 'red'
G.add_edge('llk_untrusted_app','newAttr1')
G.edge['llk_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','trustonicpartner_app')
G.edge['llk_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','trustonicpartner_app')
G.edge['llk_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','umcagent_app')
G.edge['llk_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['umcagent_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','umcagent_app')
G.edge['llk_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','untrusted_app')
G.edge['llk_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['untrusted_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','untrusted_app')
G.edge['llk_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','vpn_untrusted_app')
G.edge['llk_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','vpn_untrusted_app')
G.edge['llk_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','apaservice')
G.edge['newAttr1']['apaservice']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr1','carrier_app')
G.edge['newAttr1']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr1','filtered_google_app')
G.edge['newAttr1']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr1','filtered_untrusted_app')
G.edge['newAttr1']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr1','gad_untrusted_app')
G.edge['newAttr1']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr1','good_app')
G.edge['newAttr1']['good_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr1','irm_app')
G.edge['newAttr1']['irm_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr1','knox_untrusted_app')
G.edge['newAttr1']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr1','llk_untrusted_app')
G.edge['newAttr1']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open execmod][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][write read][write read][open open]'
G.add_edge('newAttr1','trustonicpartner_app')
G.edge['newAttr1']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr1','umcagent_app')
G.edge['newAttr1']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr1','untrusted_app')
G.edge['newAttr1']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr1','vpn_untrusted_app')
G.edge['newAttr1']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr1','carrier_app')
G.edge['newAttr1']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('newAttr1','filtered_google_app')
G.edge['newAttr1']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('newAttr1','filtered_untrusted_app')
G.edge['newAttr1']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('newAttr1','gad_untrusted_app')
G.edge['newAttr1']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('newAttr1','good_app')
G.edge['newAttr1']['good_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('newAttr1','installd')
G.edge['newAttr1']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('newAttr1','installd')
G.edge['newAttr1']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('newAttr1','irm_app')
G.edge['newAttr1']['irm_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('newAttr1','knox_untrusted_app')
G.edge['newAttr1']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('newAttr1','llk_untrusted_app')
G.edge['newAttr1']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open execmod][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][write read][write read][open open][setattr getattr]'
G.add_edge('newAttr1','trustonicpartner_app')
G.edge['newAttr1']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('newAttr1','umcagent_app')
G.edge['newAttr1']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('newAttr1','untrusted_app')
G.edge['newAttr1']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('newAttr1','vpn_untrusted_app')
G.edge['newAttr1']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('newAttr1','apaservice')
G.edge['newAttr1']['apaservice']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['newAttr1']['apaservice']['fill'] = 'red'
G.add_edge('newAttr1','apaservice')
G.edge['newAttr1']['apaservice']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('newAttr1','carrier_app')
G.edge['newAttr1']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['newAttr1']['carrier_app']['fill'] = 'red'
G.add_edge('newAttr1','carrier_app')
G.edge['newAttr1']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','filtered_google_app')
G.edge['newAttr1']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['newAttr1']['filtered_google_app']['fill'] = 'red'
G.add_edge('newAttr1','filtered_google_app')
G.edge['newAttr1']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','filtered_untrusted_app')
G.edge['newAttr1']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['newAttr1']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('newAttr1','filtered_untrusted_app')
G.edge['newAttr1']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','gad_untrusted_app')
G.edge['newAttr1']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['newAttr1']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('newAttr1','gad_untrusted_app')
G.edge['newAttr1']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','good_app')
G.edge['newAttr1']['good_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['newAttr1']['good_app']['fill'] = 'red'
G.add_edge('newAttr1','good_app')
G.edge['newAttr1']['good_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','irm_app')
G.edge['newAttr1']['irm_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['newAttr1']['irm_app']['fill'] = 'red'
G.add_edge('newAttr1','irm_app')
G.edge['newAttr1']['irm_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','knox_untrusted_app')
G.edge['newAttr1']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['newAttr1']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('newAttr1','knox_untrusted_app')
G.edge['newAttr1']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','llk_untrusted_app')
G.edge['newAttr1']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['newAttr1']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('newAttr1','llk_untrusted_app')
G.edge['newAttr1']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open execmod][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['newAttr1']['newAttr1']['fill'] = 'red'
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open execmod][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','trustonicpartner_app')
G.edge['newAttr1']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['newAttr1']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('newAttr1','trustonicpartner_app')
G.edge['newAttr1']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','umcagent_app')
G.edge['newAttr1']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['newAttr1']['umcagent_app']['fill'] = 'red'
G.add_edge('newAttr1','umcagent_app')
G.edge['newAttr1']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','untrusted_app')
G.edge['newAttr1']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['newAttr1']['untrusted_app']['fill'] = 'red'
G.add_edge('newAttr1','untrusted_app')
G.edge['newAttr1']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','vpn_untrusted_app')
G.edge['newAttr1']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['newAttr1']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('newAttr1','vpn_untrusted_app')
G.edge['newAttr1']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','apaservice')
G.edge['trustonicpartner_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('trustonicpartner_app','carrier_app')
G.edge['trustonicpartner_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('trustonicpartner_app','filtered_google_app')
G.edge['trustonicpartner_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('trustonicpartner_app','filtered_untrusted_app')
G.edge['trustonicpartner_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('trustonicpartner_app','gad_untrusted_app')
G.edge['trustonicpartner_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('trustonicpartner_app','good_app')
G.edge['trustonicpartner_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('trustonicpartner_app','irm_app')
G.edge['trustonicpartner_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('trustonicpartner_app','knox_untrusted_app')
G.edge['trustonicpartner_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('trustonicpartner_app','llk_untrusted_app')
G.edge['trustonicpartner_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('trustonicpartner_app','newAttr1')
G.edge['trustonicpartner_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('trustonicpartner_app','trustonicpartner_app')
G.edge['trustonicpartner_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('trustonicpartner_app','umcagent_app')
G.edge['trustonicpartner_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('trustonicpartner_app','untrusted_app')
G.edge['trustonicpartner_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('trustonicpartner_app','vpn_untrusted_app')
G.edge['trustonicpartner_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('trustonicpartner_app','carrier_app')
G.edge['trustonicpartner_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('trustonicpartner_app','filtered_google_app')
G.edge['trustonicpartner_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('trustonicpartner_app','filtered_untrusted_app')
G.edge['trustonicpartner_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('trustonicpartner_app','gad_untrusted_app')
G.edge['trustonicpartner_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('trustonicpartner_app','good_app')
G.edge['trustonicpartner_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('trustonicpartner_app','installd')
G.edge['trustonicpartner_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('trustonicpartner_app','installd')
G.edge['trustonicpartner_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('trustonicpartner_app','irm_app')
G.edge['trustonicpartner_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('trustonicpartner_app','knox_untrusted_app')
G.edge['trustonicpartner_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('trustonicpartner_app','llk_untrusted_app')
G.edge['trustonicpartner_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('trustonicpartner_app','newAttr1')
G.edge['trustonicpartner_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('trustonicpartner_app','trustonicpartner_app')
G.edge['trustonicpartner_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('trustonicpartner_app','umcagent_app')
G.edge['trustonicpartner_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('trustonicpartner_app','untrusted_app')
G.edge['trustonicpartner_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('trustonicpartner_app','vpn_untrusted_app')
G.edge['trustonicpartner_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('trustonicpartner_app','apaservice')
G.edge['trustonicpartner_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['trustonicpartner_app']['apaservice']['fill'] = 'red'
G.add_edge('trustonicpartner_app','apaservice')
G.edge['trustonicpartner_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('trustonicpartner_app','carrier_app')
G.edge['trustonicpartner_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['carrier_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','carrier_app')
G.edge['trustonicpartner_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','filtered_google_app')
G.edge['trustonicpartner_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','filtered_google_app')
G.edge['trustonicpartner_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','filtered_untrusted_app')
G.edge['trustonicpartner_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','filtered_untrusted_app')
G.edge['trustonicpartner_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','gad_untrusted_app')
G.edge['trustonicpartner_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','gad_untrusted_app')
G.edge['trustonicpartner_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','good_app')
G.edge['trustonicpartner_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['good_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','good_app')
G.edge['trustonicpartner_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','irm_app')
G.edge['trustonicpartner_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['irm_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','irm_app')
G.edge['trustonicpartner_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','knox_untrusted_app')
G.edge['trustonicpartner_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','knox_untrusted_app')
G.edge['trustonicpartner_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','llk_untrusted_app')
G.edge['trustonicpartner_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','llk_untrusted_app')
G.edge['trustonicpartner_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','newAttr1')
G.edge['trustonicpartner_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['newAttr1']['fill'] = 'red'
G.add_edge('trustonicpartner_app','newAttr1')
G.edge['trustonicpartner_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','trustonicpartner_app')
G.edge['trustonicpartner_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','trustonicpartner_app')
G.edge['trustonicpartner_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','umcagent_app')
G.edge['trustonicpartner_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['umcagent_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','umcagent_app')
G.edge['trustonicpartner_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','untrusted_app')
G.edge['trustonicpartner_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['untrusted_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','untrusted_app')
G.edge['trustonicpartner_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','vpn_untrusted_app')
G.edge['trustonicpartner_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','vpn_untrusted_app')
G.edge['trustonicpartner_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','apaservice')
G.edge['umcagent_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('umcagent_app','carrier_app')
G.edge['umcagent_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('umcagent_app','filtered_google_app')
G.edge['umcagent_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('umcagent_app','filtered_untrusted_app')
G.edge['umcagent_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('umcagent_app','gad_untrusted_app')
G.edge['umcagent_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('umcagent_app','good_app')
G.edge['umcagent_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('umcagent_app','irm_app')
G.edge['umcagent_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('umcagent_app','knox_untrusted_app')
G.edge['umcagent_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('umcagent_app','llk_untrusted_app')
G.edge['umcagent_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('umcagent_app','newAttr1')
G.edge['umcagent_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('umcagent_app','trustonicpartner_app')
G.edge['umcagent_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('umcagent_app','umcagent_app')
G.edge['umcagent_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('umcagent_app','untrusted_app')
G.edge['umcagent_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('umcagent_app','vpn_untrusted_app')
G.edge['umcagent_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('umcagent_app','carrier_app')
G.edge['umcagent_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('umcagent_app','filtered_google_app')
G.edge['umcagent_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('umcagent_app','filtered_untrusted_app')
G.edge['umcagent_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('umcagent_app','gad_untrusted_app')
G.edge['umcagent_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('umcagent_app','good_app')
G.edge['umcagent_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('umcagent_app','installd')
G.edge['umcagent_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('umcagent_app','installd')
G.edge['umcagent_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('umcagent_app','irm_app')
G.edge['umcagent_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('umcagent_app','knox_untrusted_app')
G.edge['umcagent_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('umcagent_app','llk_untrusted_app')
G.edge['umcagent_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('umcagent_app','newAttr1')
G.edge['umcagent_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('umcagent_app','trustonicpartner_app')
G.edge['umcagent_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('umcagent_app','umcagent_app')
G.edge['umcagent_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('umcagent_app','untrusted_app')
G.edge['umcagent_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('umcagent_app','vpn_untrusted_app')
G.edge['umcagent_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('umcagent_app','apaservice')
G.edge['umcagent_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['umcagent_app']['apaservice']['fill'] = 'red'
G.add_edge('umcagent_app','apaservice')
G.edge['umcagent_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('umcagent_app','carrier_app')
G.edge['umcagent_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['umcagent_app']['carrier_app']['fill'] = 'red'
G.add_edge('umcagent_app','carrier_app')
G.edge['umcagent_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','filtered_google_app')
G.edge['umcagent_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['umcagent_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('umcagent_app','filtered_google_app')
G.edge['umcagent_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','filtered_untrusted_app')
G.edge['umcagent_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['umcagent_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('umcagent_app','filtered_untrusted_app')
G.edge['umcagent_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','gad_untrusted_app')
G.edge['umcagent_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['umcagent_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('umcagent_app','gad_untrusted_app')
G.edge['umcagent_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','good_app')
G.edge['umcagent_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['umcagent_app']['good_app']['fill'] = 'red'
G.add_edge('umcagent_app','good_app')
G.edge['umcagent_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','irm_app')
G.edge['umcagent_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['umcagent_app']['irm_app']['fill'] = 'red'
G.add_edge('umcagent_app','irm_app')
G.edge['umcagent_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','knox_untrusted_app')
G.edge['umcagent_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['umcagent_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('umcagent_app','knox_untrusted_app')
G.edge['umcagent_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','llk_untrusted_app')
G.edge['umcagent_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['umcagent_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('umcagent_app','llk_untrusted_app')
G.edge['umcagent_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','newAttr1')
G.edge['umcagent_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['umcagent_app']['newAttr1']['fill'] = 'red'
G.add_edge('umcagent_app','newAttr1')
G.edge['umcagent_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','trustonicpartner_app')
G.edge['umcagent_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['umcagent_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('umcagent_app','trustonicpartner_app')
G.edge['umcagent_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','umcagent_app')
G.edge['umcagent_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['umcagent_app']['umcagent_app']['fill'] = 'red'
G.add_edge('umcagent_app','umcagent_app')
G.edge['umcagent_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','untrusted_app')
G.edge['umcagent_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['umcagent_app']['untrusted_app']['fill'] = 'red'
G.add_edge('umcagent_app','untrusted_app')
G.edge['umcagent_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','vpn_untrusted_app')
G.edge['umcagent_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['umcagent_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('umcagent_app','vpn_untrusted_app')
G.edge['umcagent_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('uncrypt','apaservice')
G.edge['uncrypt']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('uncrypt','carrier_app')
G.edge['uncrypt']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('uncrypt','filtered_google_app')
G.edge['uncrypt']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('uncrypt','filtered_untrusted_app')
G.edge['uncrypt']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('uncrypt','gad_untrusted_app')
G.edge['uncrypt']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('uncrypt','good_app')
G.edge['uncrypt']['good_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('uncrypt','irm_app')
G.edge['uncrypt']['irm_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('uncrypt','knox_untrusted_app')
G.edge['uncrypt']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('uncrypt','llk_untrusted_app')
G.edge['uncrypt']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('uncrypt','newAttr1')
G.edge['uncrypt']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][write read][write read][open open]'
G.add_edge('uncrypt','trustonicpartner_app')
G.edge['uncrypt']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('uncrypt','umcagent_app')
G.edge['uncrypt']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('uncrypt','untrusted_app')
G.edge['uncrypt']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('uncrypt','vpn_untrusted_app')
G.edge['uncrypt']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('uncrypt','carrier_app')
G.edge['uncrypt']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('uncrypt','filtered_google_app')
G.edge['uncrypt']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('uncrypt','filtered_untrusted_app')
G.edge['uncrypt']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('uncrypt','gad_untrusted_app')
G.edge['uncrypt']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('uncrypt','good_app')
G.edge['uncrypt']['good_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('uncrypt','installd')
G.edge['uncrypt']['installd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('uncrypt','installd')
G.edge['uncrypt']['installd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('uncrypt','irm_app')
G.edge['uncrypt']['irm_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('uncrypt','knox_untrusted_app')
G.edge['uncrypt']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('uncrypt','llk_untrusted_app')
G.edge['uncrypt']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('uncrypt','newAttr1')
G.edge['uncrypt']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][write read][write read][open open][setattr getattr]'
G.add_edge('uncrypt','trustonicpartner_app')
G.edge['uncrypt']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('uncrypt','umcagent_app')
G.edge['uncrypt']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('uncrypt','untrusted_app')
G.edge['uncrypt']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('uncrypt','vpn_untrusted_app')
G.edge['uncrypt']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('uncrypt','apaservice')
G.edge['uncrypt']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['uncrypt']['apaservice']['fill'] = 'red'
G.add_edge('uncrypt','apaservice')
G.edge['uncrypt']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('uncrypt','carrier_app')
G.edge['uncrypt']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['uncrypt']['carrier_app']['fill'] = 'red'
G.add_edge('uncrypt','carrier_app')
G.edge['uncrypt']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('uncrypt','filtered_google_app')
G.edge['uncrypt']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['uncrypt']['filtered_google_app']['fill'] = 'red'
G.add_edge('uncrypt','filtered_google_app')
G.edge['uncrypt']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('uncrypt','filtered_untrusted_app')
G.edge['uncrypt']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['uncrypt']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('uncrypt','filtered_untrusted_app')
G.edge['uncrypt']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('uncrypt','gad_untrusted_app')
G.edge['uncrypt']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['uncrypt']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('uncrypt','gad_untrusted_app')
G.edge['uncrypt']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('uncrypt','good_app')
G.edge['uncrypt']['good_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['uncrypt']['good_app']['fill'] = 'red'
G.add_edge('uncrypt','good_app')
G.edge['uncrypt']['good_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('uncrypt','irm_app')
G.edge['uncrypt']['irm_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['uncrypt']['irm_app']['fill'] = 'red'
G.add_edge('uncrypt','irm_app')
G.edge['uncrypt']['irm_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('uncrypt','knox_untrusted_app')
G.edge['uncrypt']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['uncrypt']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('uncrypt','knox_untrusted_app')
G.edge['uncrypt']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('uncrypt','llk_untrusted_app')
G.edge['uncrypt']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['uncrypt']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('uncrypt','llk_untrusted_app')
G.edge['uncrypt']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('uncrypt','newAttr1')
G.edge['uncrypt']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['uncrypt']['newAttr1']['fill'] = 'red'
G.add_edge('uncrypt','newAttr1')
G.edge['uncrypt']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('uncrypt','trustonicpartner_app')
G.edge['uncrypt']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['uncrypt']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('uncrypt','trustonicpartner_app')
G.edge['uncrypt']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('uncrypt','umcagent_app')
G.edge['uncrypt']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['uncrypt']['umcagent_app']['fill'] = 'red'
G.add_edge('uncrypt','umcagent_app')
G.edge['uncrypt']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('uncrypt','untrusted_app')
G.edge['uncrypt']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['uncrypt']['untrusted_app']['fill'] = 'red'
G.add_edge('uncrypt','untrusted_app')
G.edge['uncrypt']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('uncrypt','vpn_untrusted_app')
G.edge['uncrypt']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['uncrypt']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('uncrypt','vpn_untrusted_app')
G.edge['uncrypt']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','apaservice')
G.edge['untrusted_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusted_app','carrier_app')
G.edge['untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('untrusted_app','filtered_google_app')
G.edge['untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('untrusted_app','filtered_untrusted_app')
G.edge['untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('untrusted_app','gad_untrusted_app')
G.edge['untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('untrusted_app','good_app')
G.edge['untrusted_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('untrusted_app','irm_app')
G.edge['untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('untrusted_app','knox_untrusted_app')
G.edge['untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('untrusted_app','llk_untrusted_app')
G.edge['untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('untrusted_app','newAttr1')
G.edge['untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('untrusted_app','trustonicpartner_app')
G.edge['untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('untrusted_app','umcagent_app')
G.edge['untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('untrusted_app','untrusted_app')
G.edge['untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('untrusted_app','vpn_untrusted_app')
G.edge['untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('untrusted_app','carrier_app')
G.edge['untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('untrusted_app','filtered_google_app')
G.edge['untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('untrusted_app','filtered_untrusted_app')
G.edge['untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('untrusted_app','gad_untrusted_app')
G.edge['untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('untrusted_app','good_app')
G.edge['untrusted_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('untrusted_app','installd')
G.edge['untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('untrusted_app','installd')
G.edge['untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('untrusted_app','irm_app')
G.edge['untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('untrusted_app','knox_untrusted_app')
G.edge['untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('untrusted_app','llk_untrusted_app')
G.edge['untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('untrusted_app','newAttr1')
G.edge['untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('untrusted_app','trustonicpartner_app')
G.edge['untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('untrusted_app','umcagent_app')
G.edge['untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('untrusted_app','untrusted_app')
G.edge['untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('untrusted_app','vpn_untrusted_app')
G.edge['untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('untrusted_app','apaservice')
G.edge['untrusted_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['untrusted_app']['apaservice']['fill'] = 'red'
G.add_edge('untrusted_app','apaservice')
G.edge['untrusted_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('untrusted_app','carrier_app')
G.edge['untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['untrusted_app']['carrier_app']['fill'] = 'red'
G.add_edge('untrusted_app','carrier_app')
G.edge['untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','filtered_google_app')
G.edge['untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['untrusted_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('untrusted_app','filtered_google_app')
G.edge['untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','filtered_untrusted_app')
G.edge['untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['untrusted_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('untrusted_app','filtered_untrusted_app')
G.edge['untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','gad_untrusted_app')
G.edge['untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['untrusted_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('untrusted_app','gad_untrusted_app')
G.edge['untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','good_app')
G.edge['untrusted_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['untrusted_app']['good_app']['fill'] = 'red'
G.add_edge('untrusted_app','good_app')
G.edge['untrusted_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','irm_app')
G.edge['untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['untrusted_app']['irm_app']['fill'] = 'red'
G.add_edge('untrusted_app','irm_app')
G.edge['untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','knox_untrusted_app')
G.edge['untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['untrusted_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('untrusted_app','knox_untrusted_app')
G.edge['untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','llk_untrusted_app')
G.edge['untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['untrusted_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('untrusted_app','llk_untrusted_app')
G.edge['untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','newAttr1')
G.edge['untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['untrusted_app']['newAttr1']['fill'] = 'red'
G.add_edge('untrusted_app','newAttr1')
G.edge['untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','trustonicpartner_app')
G.edge['untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['untrusted_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('untrusted_app','trustonicpartner_app')
G.edge['untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','umcagent_app')
G.edge['untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['untrusted_app']['umcagent_app']['fill'] = 'red'
G.add_edge('untrusted_app','umcagent_app')
G.edge['untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','untrusted_app')
G.edge['untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['untrusted_app']['untrusted_app']['fill'] = 'red'
G.add_edge('untrusted_app','untrusted_app')
G.edge['untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','vpn_untrusted_app')
G.edge['untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['untrusted_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('untrusted_app','vpn_untrusted_app')
G.edge['untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','apaservice')
G.edge['vpn_untrusted_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('vpn_untrusted_app','carrier_app')
G.edge['vpn_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('vpn_untrusted_app','filtered_google_app')
G.edge['vpn_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('vpn_untrusted_app','filtered_untrusted_app')
G.edge['vpn_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('vpn_untrusted_app','gad_untrusted_app')
G.edge['vpn_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('vpn_untrusted_app','good_app')
G.edge['vpn_untrusted_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('vpn_untrusted_app','irm_app')
G.edge['vpn_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('vpn_untrusted_app','knox_untrusted_app')
G.edge['vpn_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('vpn_untrusted_app','llk_untrusted_app')
G.edge['vpn_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('vpn_untrusted_app','newAttr1')
G.edge['vpn_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('vpn_untrusted_app','trustonicpartner_app')
G.edge['vpn_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('vpn_untrusted_app','umcagent_app')
G.edge['vpn_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('vpn_untrusted_app','untrusted_app')
G.edge['vpn_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('vpn_untrusted_app','vpn_untrusted_app')
G.edge['vpn_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open]'
G.add_edge('vpn_untrusted_app','carrier_app')
G.edge['vpn_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','filtered_google_app')
G.edge['vpn_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','filtered_untrusted_app')
G.edge['vpn_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','gad_untrusted_app')
G.edge['vpn_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','good_app')
G.edge['vpn_untrusted_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','installd')
G.edge['vpn_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('vpn_untrusted_app','installd')
G.edge['vpn_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('vpn_untrusted_app','irm_app')
G.edge['vpn_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','knox_untrusted_app')
G.edge['vpn_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','llk_untrusted_app')
G.edge['vpn_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','newAttr1')
G.edge['vpn_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','trustonicpartner_app')
G.edge['vpn_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','umcagent_app')
G.edge['vpn_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','untrusted_app')
G.edge['vpn_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','vpn_untrusted_app')
G.edge['vpn_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','apaservice')
G.edge['vpn_untrusted_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['vpn_untrusted_app']['apaservice']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','apaservice')
G.edge['vpn_untrusted_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vpn_untrusted_app','carrier_app')
G.edge['vpn_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['carrier_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','carrier_app')
G.edge['vpn_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','filtered_google_app')
G.edge['vpn_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','filtered_google_app')
G.edge['vpn_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','filtered_untrusted_app')
G.edge['vpn_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','filtered_untrusted_app')
G.edge['vpn_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','gad_untrusted_app')
G.edge['vpn_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','gad_untrusted_app')
G.edge['vpn_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','good_app')
G.edge['vpn_untrusted_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['good_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','good_app')
G.edge['vpn_untrusted_app']['good_app']['write-read'] = '[open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','irm_app')
G.edge['vpn_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['irm_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','irm_app')
G.edge['vpn_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','knox_untrusted_app')
G.edge['vpn_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','knox_untrusted_app')
G.edge['vpn_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','llk_untrusted_app')
G.edge['vpn_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','llk_untrusted_app')
G.edge['vpn_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','newAttr1')
G.edge['vpn_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['newAttr1']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','newAttr1')
G.edge['vpn_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','trustonicpartner_app')
G.edge['vpn_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','trustonicpartner_app')
G.edge['vpn_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','umcagent_app')
G.edge['vpn_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['umcagent_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','umcagent_app')
G.edge['vpn_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','untrusted_app')
G.edge['vpn_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['untrusted_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','untrusted_app')
G.edge['vpn_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','vpn_untrusted_app')
G.edge['vpn_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','vpn_untrusted_app')
G.edge['vpn_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()