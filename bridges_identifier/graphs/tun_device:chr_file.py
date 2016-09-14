import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open]'
G.add_edge('appdomain','bluetooth')
G.edge['appdomain']['bluetooth']['write-read'] = '[write read][open open]'
G.add_edge('appdomain','bluetooth')
G.edge['appdomain']['bluetooth']['write-read'] = '[write read][open open][open open]'
G.add_edge('appdomain','carrier_app')
G.edge['appdomain']['carrier_app']['write-read'] = '[write read][open open]'
G.add_edge('appdomain','charon')
G.edge['appdomain']['charon']['write-read'] = '[open open]'
G.add_edge('appdomain','clatd')
G.edge['appdomain']['clatd']['write-read'] = '[open open]'
G.add_edge('appdomain','filtered_google_app')
G.edge['appdomain']['filtered_google_app']['write-read'] = '[write read][open open]'
G.add_edge('appdomain','filtered_untrusted_app')
G.edge['appdomain']['filtered_untrusted_app']['write-read'] = '[write read][open open]'
G.add_edge('appdomain','gad_untrusted_app')
G.edge['appdomain']['gad_untrusted_app']['write-read'] = '[write read][open open]'
G.add_edge('appdomain','irm_app')
G.edge['appdomain']['irm_app']['write-read'] = '[write read][open open]'
G.add_edge('appdomain','knox_untrusted_app')
G.edge['appdomain']['knox_untrusted_app']['write-read'] = '[write read][open open]'
G.add_edge('appdomain','llk_untrusted_app')
G.edge['appdomain']['llk_untrusted_app']['write-read'] = '[write read][open open]'
G.add_edge('appdomain','netd')
G.edge['appdomain']['netd']['write-read'] = '[write read][append read][open open]'
G.add_edge('appdomain','rild')
G.edge['appdomain']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open execmod][write read][append read][open open]'
G.add_edge('appdomain','trustonicpartner_app')
G.edge['appdomain']['trustonicpartner_app']['write-read'] = '[write read][open open]'
G.add_edge('appdomain','umcagent_app')
G.edge['appdomain']['umcagent_app']['write-read'] = '[write read][open open]'
G.add_edge('appdomain','untrusted_app')
G.edge['appdomain']['untrusted_app']['write-read'] = '[write read][open open]'
G.add_edge('appdomain','untrusteddomain')
G.edge['appdomain']['untrusteddomain']['write-read'] = '[write read][append read][open open]'
G.add_edge('appdomain','vpnclientd')
G.edge['appdomain']['vpnclientd']['write-read'] = '[open open]'
G.add_edge('appdomain','vpn_untrusted_app')
G.edge['appdomain']['vpn_untrusted_app']['write-read'] = '[write read][open open]'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read]'
G.edge['appdomain']['appdomain']['fill'] = 'red'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read]'
G.add_edge('appdomain','bluetooth')
G.edge['appdomain']['bluetooth']['write-read'] = '[write read][open open][open open][write read]'
G.edge['appdomain']['bluetooth']['fill'] = 'red'
G.add_edge('appdomain','bluetooth')
G.edge['appdomain']['bluetooth']['write-read'] = '[write read][open open][open open][write read][append read]'
G.add_edge('appdomain','bluetooth')
G.edge['appdomain']['bluetooth']['write-read'] = '[write read][open open][open open][write read][append read][write read]'
G.edge['appdomain']['bluetooth']['fill'] = 'red'
G.add_edge('appdomain','bluetooth')
G.edge['appdomain']['bluetooth']['write-read'] = '[write read][open open][open open][write read][append read][write read][append read]'
G.add_edge('appdomain','carrier_app')
G.edge['appdomain']['carrier_app']['write-read'] = '[write read][open open][write read]'
G.edge['appdomain']['carrier_app']['fill'] = 'red'
G.add_edge('appdomain','carrier_app')
G.edge['appdomain']['carrier_app']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('appdomain','charon')
G.edge['appdomain']['charon']['write-read'] = '[open open][write read]'
G.edge['appdomain']['charon']['fill'] = 'red'
G.add_edge('appdomain','charon')
G.edge['appdomain']['charon']['write-read'] = '[open open][write read][append read]'
G.add_edge('appdomain','clatd')
G.edge['appdomain']['clatd']['write-read'] = '[open open][write read]'
G.edge['appdomain']['clatd']['fill'] = 'red'
G.add_edge('appdomain','clatd')
G.edge['appdomain']['clatd']['write-read'] = '[open open][write read][append read]'
G.add_edge('appdomain','filtered_google_app')
G.edge['appdomain']['filtered_google_app']['write-read'] = '[write read][open open][write read]'
G.edge['appdomain']['filtered_google_app']['fill'] = 'red'
G.add_edge('appdomain','filtered_google_app')
G.edge['appdomain']['filtered_google_app']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('appdomain','filtered_untrusted_app')
G.edge['appdomain']['filtered_untrusted_app']['write-read'] = '[write read][open open][write read]'
G.edge['appdomain']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('appdomain','filtered_untrusted_app')
G.edge['appdomain']['filtered_untrusted_app']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('appdomain','gad_untrusted_app')
G.edge['appdomain']['gad_untrusted_app']['write-read'] = '[write read][open open][write read]'
G.edge['appdomain']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('appdomain','gad_untrusted_app')
G.edge['appdomain']['gad_untrusted_app']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('appdomain','irm_app')
G.edge['appdomain']['irm_app']['write-read'] = '[write read][open open][write read]'
G.edge['appdomain']['irm_app']['fill'] = 'red'
G.add_edge('appdomain','irm_app')
G.edge['appdomain']['irm_app']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('appdomain','knox_untrusted_app')
G.edge['appdomain']['knox_untrusted_app']['write-read'] = '[write read][open open][write read]'
G.edge['appdomain']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('appdomain','knox_untrusted_app')
G.edge['appdomain']['knox_untrusted_app']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('appdomain','llk_untrusted_app')
G.edge['appdomain']['llk_untrusted_app']['write-read'] = '[write read][open open][write read]'
G.edge['appdomain']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('appdomain','llk_untrusted_app')
G.edge['appdomain']['llk_untrusted_app']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('appdomain','netd')
G.edge['appdomain']['netd']['write-read'] = '[write read][append read][open open][write read]'
G.edge['appdomain']['netd']['fill'] = 'red'
G.add_edge('appdomain','netd')
G.edge['appdomain']['netd']['write-read'] = '[write read][append read][open open][write read][append read]'
G.add_edge('appdomain','rild')
G.edge['appdomain']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['appdomain']['rild']['fill'] = 'red'
G.add_edge('appdomain','rild')
G.edge['appdomain']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open execmod][write read][append read][open open][write read]'
G.edge['appdomain']['system_server']['fill'] = 'red'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open execmod][write read][append read][open open][write read][append read]'
G.add_edge('appdomain','trustonicpartner_app')
G.edge['appdomain']['trustonicpartner_app']['write-read'] = '[write read][open open][write read]'
G.edge['appdomain']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('appdomain','trustonicpartner_app')
G.edge['appdomain']['trustonicpartner_app']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('appdomain','umcagent_app')
G.edge['appdomain']['umcagent_app']['write-read'] = '[write read][open open][write read]'
G.edge['appdomain']['umcagent_app']['fill'] = 'red'
G.add_edge('appdomain','umcagent_app')
G.edge['appdomain']['umcagent_app']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('appdomain','untrusted_app')
G.edge['appdomain']['untrusted_app']['write-read'] = '[write read][open open][write read]'
G.edge['appdomain']['untrusted_app']['fill'] = 'red'
G.add_edge('appdomain','untrusted_app')
G.edge['appdomain']['untrusted_app']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('appdomain','untrusteddomain')
G.edge['appdomain']['untrusteddomain']['write-read'] = '[write read][append read][open open][write read]'
G.edge['appdomain']['untrusteddomain']['fill'] = 'red'
G.add_edge('appdomain','untrusteddomain')
G.edge['appdomain']['untrusteddomain']['write-read'] = '[write read][append read][open open][write read][append read]'
G.add_edge('appdomain','vpnclientd')
G.edge['appdomain']['vpnclientd']['write-read'] = '[open open][write read]'
G.edge['appdomain']['vpnclientd']['fill'] = 'red'
G.add_edge('appdomain','vpnclientd')
G.edge['appdomain']['vpnclientd']['write-read'] = '[open open][write read][append read]'
G.add_edge('appdomain','vpn_untrusted_app')
G.edge['appdomain']['vpn_untrusted_app']['write-read'] = '[write read][open open][write read]'
G.edge['appdomain']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('appdomain','vpn_untrusted_app')
G.edge['appdomain']['vpn_untrusted_app']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('bluetooth','appdomain')
G.edge['bluetooth']['appdomain']['write-read'] = '[write read][open open]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('bluetooth','carrier_app')
G.edge['bluetooth']['carrier_app']['write-read'] = '[open open]'
G.add_edge('bluetooth','charon')
G.edge['bluetooth']['charon']['write-read'] = '[open open]'
G.add_edge('bluetooth','clatd')
G.edge['bluetooth']['clatd']['write-read'] = '[open open]'
G.add_edge('bluetooth','filtered_google_app')
G.edge['bluetooth']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('bluetooth','filtered_untrusted_app')
G.edge['bluetooth']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('bluetooth','gad_untrusted_app')
G.edge['bluetooth']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('bluetooth','irm_app')
G.edge['bluetooth']['irm_app']['write-read'] = '[open open]'
G.add_edge('bluetooth','knox_untrusted_app')
G.edge['bluetooth']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('bluetooth','llk_untrusted_app')
G.edge['bluetooth']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('bluetooth','netd')
G.edge['bluetooth']['netd']['write-read'] = '[write read][append read][write read][open open]'
G.add_edge('bluetooth','rild')
G.edge['bluetooth']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('bluetooth','trustonicpartner_app')
G.edge['bluetooth']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('bluetooth','umcagent_app')
G.edge['bluetooth']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('bluetooth','untrusted_app')
G.edge['bluetooth']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('bluetooth','untrusteddomain')
G.edge['bluetooth']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('bluetooth','vpnclientd')
G.edge['bluetooth']['vpnclientd']['write-read'] = '[write read][open open]'
G.add_edge('bluetooth','vpn_untrusted_app')
G.edge['bluetooth']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('bluetooth','appdomain')
G.edge['bluetooth']['appdomain']['write-read'] = '[write read][open open][write read]'
G.edge['bluetooth']['appdomain']['fill'] = 'red'
G.add_edge('bluetooth','appdomain')
G.edge['bluetooth']['appdomain']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read]'
G.edge['bluetooth']['bluetooth']['fill'] = 'red'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read]'
G.edge['bluetooth']['bluetooth']['fill'] = 'red'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read]'
G.add_edge('bluetooth','carrier_app')
G.edge['bluetooth']['carrier_app']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['carrier_app']['fill'] = 'red'
G.add_edge('bluetooth','carrier_app')
G.edge['bluetooth']['carrier_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','charon')
G.edge['bluetooth']['charon']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['charon']['fill'] = 'red'
G.add_edge('bluetooth','charon')
G.edge['bluetooth']['charon']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','clatd')
G.edge['bluetooth']['clatd']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['clatd']['fill'] = 'red'
G.add_edge('bluetooth','clatd')
G.edge['bluetooth']['clatd']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','filtered_google_app')
G.edge['bluetooth']['filtered_google_app']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['filtered_google_app']['fill'] = 'red'
G.add_edge('bluetooth','filtered_google_app')
G.edge['bluetooth']['filtered_google_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','filtered_untrusted_app')
G.edge['bluetooth']['filtered_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('bluetooth','filtered_untrusted_app')
G.edge['bluetooth']['filtered_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','gad_untrusted_app')
G.edge['bluetooth']['gad_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('bluetooth','gad_untrusted_app')
G.edge['bluetooth']['gad_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','irm_app')
G.edge['bluetooth']['irm_app']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['irm_app']['fill'] = 'red'
G.add_edge('bluetooth','irm_app')
G.edge['bluetooth']['irm_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','knox_untrusted_app')
G.edge['bluetooth']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['bluetooth']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('bluetooth','knox_untrusted_app')
G.edge['bluetooth']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','llk_untrusted_app')
G.edge['bluetooth']['llk_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('bluetooth','llk_untrusted_app')
G.edge['bluetooth']['llk_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','netd')
G.edge['bluetooth']['netd']['write-read'] = '[write read][append read][write read][open open][write read]'
G.edge['bluetooth']['netd']['fill'] = 'red'
G.add_edge('bluetooth','netd')
G.edge['bluetooth']['netd']['write-read'] = '[write read][append read][write read][open open][write read][append read]'
G.add_edge('bluetooth','rild')
G.edge['bluetooth']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['bluetooth']['rild']['fill'] = 'red'
G.add_edge('bluetooth','rild')
G.edge['bluetooth']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['bluetooth']['system_server']['fill'] = 'red'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','trustonicpartner_app')
G.edge['bluetooth']['trustonicpartner_app']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('bluetooth','trustonicpartner_app')
G.edge['bluetooth']['trustonicpartner_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','umcagent_app')
G.edge['bluetooth']['umcagent_app']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['umcagent_app']['fill'] = 'red'
G.add_edge('bluetooth','umcagent_app')
G.edge['bluetooth']['umcagent_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','untrusted_app')
G.edge['bluetooth']['untrusted_app']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['untrusted_app']['fill'] = 'red'
G.add_edge('bluetooth','untrusted_app')
G.edge['bluetooth']['untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','untrusteddomain')
G.edge['bluetooth']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['bluetooth']['untrusteddomain']['fill'] = 'red'
G.add_edge('bluetooth','untrusteddomain')
G.edge['bluetooth']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','vpnclientd')
G.edge['bluetooth']['vpnclientd']['write-read'] = '[write read][open open][write read]'
G.edge['bluetooth']['vpnclientd']['fill'] = 'red'
G.add_edge('bluetooth','vpnclientd')
G.edge['bluetooth']['vpnclientd']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('bluetooth','vpn_untrusted_app')
G.edge['bluetooth']['vpn_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('bluetooth','vpn_untrusted_app')
G.edge['bluetooth']['vpn_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','appdomain')
G.edge['bluetooth']['appdomain']['write-read'] = '[write read][open open][write read][append read][open open]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open]'
G.add_edge('bluetooth','carrier_app')
G.edge['bluetooth']['carrier_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bluetooth','charon')
G.edge['bluetooth']['charon']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bluetooth','clatd')
G.edge['bluetooth']['clatd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bluetooth','filtered_google_app')
G.edge['bluetooth']['filtered_google_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bluetooth','filtered_untrusted_app')
G.edge['bluetooth']['filtered_untrusted_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bluetooth','gad_untrusted_app')
G.edge['bluetooth']['gad_untrusted_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bluetooth','irm_app')
G.edge['bluetooth']['irm_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bluetooth','knox_untrusted_app')
G.edge['bluetooth']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('bluetooth','llk_untrusted_app')
G.edge['bluetooth']['llk_untrusted_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bluetooth','netd')
G.edge['bluetooth']['netd']['write-read'] = '[write read][append read][write read][open open][write read][append read][open open]'
G.add_edge('bluetooth','rild')
G.edge['bluetooth']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('bluetooth','trustonicpartner_app')
G.edge['bluetooth']['trustonicpartner_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bluetooth','umcagent_app')
G.edge['bluetooth']['umcagent_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bluetooth','untrusted_app')
G.edge['bluetooth']['untrusted_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bluetooth','untrusteddomain')
G.edge['bluetooth']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('bluetooth','vpnclientd')
G.edge['bluetooth']['vpnclientd']['write-read'] = '[write read][open open][write read][append read][open open]'
G.add_edge('bluetooth','vpn_untrusted_app')
G.edge['bluetooth']['vpn_untrusted_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bluetooth','appdomain')
G.edge['bluetooth']['appdomain']['write-read'] = '[write read][open open][write read][append read][open open][write read]'
G.edge['bluetooth']['appdomain']['fill'] = 'red'
G.add_edge('bluetooth','appdomain')
G.edge['bluetooth']['appdomain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read]'
G.edge['bluetooth']['bluetooth']['fill'] = 'red'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read]'
G.edge['bluetooth']['bluetooth']['fill'] = 'red'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read]'
G.add_edge('bluetooth','carrier_app')
G.edge['bluetooth']['carrier_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['bluetooth']['carrier_app']['fill'] = 'red'
G.add_edge('bluetooth','carrier_app')
G.edge['bluetooth']['carrier_app']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','charon')
G.edge['bluetooth']['charon']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['bluetooth']['charon']['fill'] = 'red'
G.add_edge('bluetooth','charon')
G.edge['bluetooth']['charon']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','clatd')
G.edge['bluetooth']['clatd']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['bluetooth']['clatd']['fill'] = 'red'
G.add_edge('bluetooth','clatd')
G.edge['bluetooth']['clatd']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','filtered_google_app')
G.edge['bluetooth']['filtered_google_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['bluetooth']['filtered_google_app']['fill'] = 'red'
G.add_edge('bluetooth','filtered_google_app')
G.edge['bluetooth']['filtered_google_app']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','filtered_untrusted_app')
G.edge['bluetooth']['filtered_untrusted_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['bluetooth']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('bluetooth','filtered_untrusted_app')
G.edge['bluetooth']['filtered_untrusted_app']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','gad_untrusted_app')
G.edge['bluetooth']['gad_untrusted_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['bluetooth']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('bluetooth','gad_untrusted_app')
G.edge['bluetooth']['gad_untrusted_app']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','irm_app')
G.edge['bluetooth']['irm_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['bluetooth']['irm_app']['fill'] = 'red'
G.add_edge('bluetooth','irm_app')
G.edge['bluetooth']['irm_app']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','knox_untrusted_app')
G.edge['bluetooth']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['bluetooth']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('bluetooth','knox_untrusted_app')
G.edge['bluetooth']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','llk_untrusted_app')
G.edge['bluetooth']['llk_untrusted_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['bluetooth']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('bluetooth','llk_untrusted_app')
G.edge['bluetooth']['llk_untrusted_app']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','netd')
G.edge['bluetooth']['netd']['write-read'] = '[write read][append read][write read][open open][write read][append read][open open][write read]'
G.edge['bluetooth']['netd']['fill'] = 'red'
G.add_edge('bluetooth','netd')
G.edge['bluetooth']['netd']['write-read'] = '[write read][append read][write read][open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','rild')
G.edge['bluetooth']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['bluetooth']['rild']['fill'] = 'red'
G.add_edge('bluetooth','rild')
G.edge['bluetooth']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['bluetooth']['system_server']['fill'] = 'red'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','trustonicpartner_app')
G.edge['bluetooth']['trustonicpartner_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['bluetooth']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('bluetooth','trustonicpartner_app')
G.edge['bluetooth']['trustonicpartner_app']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','umcagent_app')
G.edge['bluetooth']['umcagent_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['bluetooth']['umcagent_app']['fill'] = 'red'
G.add_edge('bluetooth','umcagent_app')
G.edge['bluetooth']['umcagent_app']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','untrusted_app')
G.edge['bluetooth']['untrusted_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['bluetooth']['untrusted_app']['fill'] = 'red'
G.add_edge('bluetooth','untrusted_app')
G.edge['bluetooth']['untrusted_app']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','untrusteddomain')
G.edge['bluetooth']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['bluetooth']['untrusteddomain']['fill'] = 'red'
G.add_edge('bluetooth','untrusteddomain')
G.edge['bluetooth']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','vpnclientd')
G.edge['bluetooth']['vpnclientd']['write-read'] = '[write read][open open][write read][append read][open open][write read]'
G.edge['bluetooth']['vpnclientd']['fill'] = 'red'
G.add_edge('bluetooth','vpnclientd')
G.edge['bluetooth']['vpnclientd']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','vpn_untrusted_app')
G.edge['bluetooth']['vpn_untrusted_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['bluetooth']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('bluetooth','vpn_untrusted_app')
G.edge['bluetooth']['vpn_untrusted_app']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('carrier_app','appdomain')
G.edge['carrier_app']['appdomain']['write-read'] = '[open open]'
G.add_edge('carrier_app','bluetooth')
G.edge['carrier_app']['bluetooth']['write-read'] = '[open open]'
G.add_edge('carrier_app','bluetooth')
G.edge['carrier_app']['bluetooth']['write-read'] = '[open open][open open]'
G.add_edge('carrier_app','carrier_app')
G.edge['carrier_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('carrier_app','charon')
G.edge['carrier_app']['charon']['write-read'] = '[open open]'
G.add_edge('carrier_app','clatd')
G.edge['carrier_app']['clatd']['write-read'] = '[open open]'
G.add_edge('carrier_app','filtered_google_app')
G.edge['carrier_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('carrier_app','filtered_untrusted_app')
G.edge['carrier_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('carrier_app','gad_untrusted_app')
G.edge['carrier_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('carrier_app','irm_app')
G.edge['carrier_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('carrier_app','knox_untrusted_app')
G.edge['carrier_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('carrier_app','llk_untrusted_app')
G.edge['carrier_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('carrier_app','netd')
G.edge['carrier_app']['netd']['write-read'] = '[open open]'
G.add_edge('carrier_app','rild')
G.edge['carrier_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('carrier_app','system_server')
G.edge['carrier_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('carrier_app','trustonicpartner_app')
G.edge['carrier_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('carrier_app','umcagent_app')
G.edge['carrier_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('carrier_app','untrusted_app')
G.edge['carrier_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('carrier_app','untrusteddomain')
G.edge['carrier_app']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('carrier_app','vpnclientd')
G.edge['carrier_app']['vpnclientd']['write-read'] = '[open open]'
G.add_edge('carrier_app','vpn_untrusted_app')
G.edge['carrier_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('carrier_app','appdomain')
G.edge['carrier_app']['appdomain']['write-read'] = '[open open][write read]'
G.edge['carrier_app']['appdomain']['fill'] = 'red'
G.add_edge('carrier_app','appdomain')
G.edge['carrier_app']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('carrier_app','bluetooth')
G.edge['carrier_app']['bluetooth']['write-read'] = '[open open][open open][write read]'
G.edge['carrier_app']['bluetooth']['fill'] = 'red'
G.add_edge('carrier_app','bluetooth')
G.edge['carrier_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('carrier_app','bluetooth')
G.edge['carrier_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['carrier_app']['bluetooth']['fill'] = 'red'
G.add_edge('carrier_app','bluetooth')
G.edge['carrier_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('carrier_app','carrier_app')
G.edge['carrier_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['carrier_app']['carrier_app']['fill'] = 'red'
G.add_edge('carrier_app','carrier_app')
G.edge['carrier_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('carrier_app','charon')
G.edge['carrier_app']['charon']['write-read'] = '[open open][write read]'
G.edge['carrier_app']['charon']['fill'] = 'red'
G.add_edge('carrier_app','charon')
G.edge['carrier_app']['charon']['write-read'] = '[open open][write read][append read]'
G.add_edge('carrier_app','clatd')
G.edge['carrier_app']['clatd']['write-read'] = '[open open][write read]'
G.edge['carrier_app']['clatd']['fill'] = 'red'
G.add_edge('carrier_app','clatd')
G.edge['carrier_app']['clatd']['write-read'] = '[open open][write read][append read]'
G.add_edge('carrier_app','filtered_google_app')
G.edge['carrier_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['carrier_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('carrier_app','filtered_google_app')
G.edge['carrier_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('carrier_app','filtered_untrusted_app')
G.edge['carrier_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['carrier_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('carrier_app','filtered_untrusted_app')
G.edge['carrier_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('carrier_app','gad_untrusted_app')
G.edge['carrier_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['carrier_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('carrier_app','gad_untrusted_app')
G.edge['carrier_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('carrier_app','irm_app')
G.edge['carrier_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['carrier_app']['irm_app']['fill'] = 'red'
G.add_edge('carrier_app','irm_app')
G.edge['carrier_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('carrier_app','knox_untrusted_app')
G.edge['carrier_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['carrier_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('carrier_app','knox_untrusted_app')
G.edge['carrier_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('carrier_app','llk_untrusted_app')
G.edge['carrier_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['carrier_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('carrier_app','llk_untrusted_app')
G.edge['carrier_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('carrier_app','netd')
G.edge['carrier_app']['netd']['write-read'] = '[open open][write read]'
G.edge['carrier_app']['netd']['fill'] = 'red'
G.add_edge('carrier_app','netd')
G.edge['carrier_app']['netd']['write-read'] = '[open open][write read][append read]'
G.add_edge('carrier_app','rild')
G.edge['carrier_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['carrier_app']['rild']['fill'] = 'red'
G.add_edge('carrier_app','rild')
G.edge['carrier_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('carrier_app','system_server')
G.edge['carrier_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read]'
G.edge['carrier_app']['system_server']['fill'] = 'red'
G.add_edge('carrier_app','system_server')
G.edge['carrier_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read]'
G.add_edge('carrier_app','trustonicpartner_app')
G.edge['carrier_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['carrier_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('carrier_app','trustonicpartner_app')
G.edge['carrier_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('carrier_app','umcagent_app')
G.edge['carrier_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['carrier_app']['umcagent_app']['fill'] = 'red'
G.add_edge('carrier_app','umcagent_app')
G.edge['carrier_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('carrier_app','untrusted_app')
G.edge['carrier_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['carrier_app']['untrusted_app']['fill'] = 'red'
G.add_edge('carrier_app','untrusted_app')
G.edge['carrier_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('carrier_app','untrusteddomain')
G.edge['carrier_app']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['carrier_app']['untrusteddomain']['fill'] = 'red'
G.add_edge('carrier_app','untrusteddomain')
G.edge['carrier_app']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('carrier_app','vpnclientd')
G.edge['carrier_app']['vpnclientd']['write-read'] = '[open open][write read]'
G.edge['carrier_app']['vpnclientd']['fill'] = 'red'
G.add_edge('carrier_app','vpnclientd')
G.edge['carrier_app']['vpnclientd']['write-read'] = '[open open][write read][append read]'
G.add_edge('carrier_app','vpn_untrusted_app')
G.edge['carrier_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['carrier_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('carrier_app','vpn_untrusted_app')
G.edge['carrier_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('charon','appdomain')
G.edge['charon']['appdomain']['write-read'] = '[write read][open open]'
G.add_edge('charon','bluetooth')
G.edge['charon']['bluetooth']['write-read'] = '[open open]'
G.add_edge('charon','bluetooth')
G.edge['charon']['bluetooth']['write-read'] = '[open open][open open]'
G.add_edge('charon','carrier_app')
G.edge['charon']['carrier_app']['write-read'] = '[open open]'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('charon','clatd')
G.edge['charon']['clatd']['write-read'] = '[add_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('charon','filtered_google_app')
G.edge['charon']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('charon','filtered_untrusted_app')
G.edge['charon']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('charon','gad_untrusted_app')
G.edge['charon']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('charon','irm_app')
G.edge['charon']['irm_app']['write-read'] = '[open open]'
G.add_edge('charon','knox_untrusted_app')
G.edge['charon']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('charon','llk_untrusted_app')
G.edge['charon']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('charon','netd')
G.edge['charon']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read][open open]'
G.add_edge('charon','rild')
G.edge['charon']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('charon','system_server')
G.edge['charon']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open]'
G.add_edge('charon','trustonicpartner_app')
G.edge['charon']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('charon','umcagent_app')
G.edge['charon']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('charon','untrusted_app')
G.edge['charon']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('charon','untrusteddomain')
G.edge['charon']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('charon','vpnclientd')
G.edge['charon']['vpnclientd']['write-read'] = '[open open]'
G.add_edge('charon','vpn_untrusted_app')
G.edge['charon']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('charon','appdomain')
G.edge['charon']['appdomain']['write-read'] = '[write read][open open][write read]'
G.edge['charon']['appdomain']['fill'] = 'red'
G.add_edge('charon','appdomain')
G.edge['charon']['appdomain']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('charon','bluetooth')
G.edge['charon']['bluetooth']['write-read'] = '[open open][open open][write read]'
G.edge['charon']['bluetooth']['fill'] = 'red'
G.add_edge('charon','bluetooth')
G.edge['charon']['bluetooth']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('charon','bluetooth')
G.edge['charon']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['charon']['bluetooth']['fill'] = 'red'
G.add_edge('charon','bluetooth')
G.edge['charon']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('charon','carrier_app')
G.edge['charon']['carrier_app']['write-read'] = '[open open][write read]'
G.edge['charon']['carrier_app']['fill'] = 'red'
G.add_edge('charon','carrier_app')
G.edge['charon']['carrier_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['charon']['charon']['fill'] = 'red'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('charon','clatd')
G.edge['charon']['clatd']['write-read'] = '[add_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['charon']['clatd']['fill'] = 'red'
G.add_edge('charon','clatd')
G.edge['charon']['clatd']['write-read'] = '[add_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('charon','filtered_google_app')
G.edge['charon']['filtered_google_app']['write-read'] = '[open open][write read]'
G.edge['charon']['filtered_google_app']['fill'] = 'red'
G.add_edge('charon','filtered_google_app')
G.edge['charon']['filtered_google_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','filtered_untrusted_app')
G.edge['charon']['filtered_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['charon']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('charon','filtered_untrusted_app')
G.edge['charon']['filtered_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','gad_untrusted_app')
G.edge['charon']['gad_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['charon']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('charon','gad_untrusted_app')
G.edge['charon']['gad_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','irm_app')
G.edge['charon']['irm_app']['write-read'] = '[open open][write read]'
G.edge['charon']['irm_app']['fill'] = 'red'
G.add_edge('charon','irm_app')
G.edge['charon']['irm_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','knox_untrusted_app')
G.edge['charon']['knox_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['charon']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('charon','knox_untrusted_app')
G.edge['charon']['knox_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','llk_untrusted_app')
G.edge['charon']['llk_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['charon']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('charon','llk_untrusted_app')
G.edge['charon']['llk_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','netd')
G.edge['charon']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][write read]'
G.edge['charon']['netd']['fill'] = 'red'
G.add_edge('charon','netd')
G.edge['charon']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][write read][append read]'
G.add_edge('charon','rild')
G.edge['charon']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['charon']['rild']['fill'] = 'red'
G.add_edge('charon','rild')
G.edge['charon']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('charon','system_server')
G.edge['charon']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read]'
G.edge['charon']['system_server']['fill'] = 'red'
G.add_edge('charon','system_server')
G.edge['charon']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read]'
G.add_edge('charon','trustonicpartner_app')
G.edge['charon']['trustonicpartner_app']['write-read'] = '[open open][write read]'
G.edge['charon']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('charon','trustonicpartner_app')
G.edge['charon']['trustonicpartner_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','umcagent_app')
G.edge['charon']['umcagent_app']['write-read'] = '[open open][write read]'
G.edge['charon']['umcagent_app']['fill'] = 'red'
G.add_edge('charon','umcagent_app')
G.edge['charon']['umcagent_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','untrusted_app')
G.edge['charon']['untrusted_app']['write-read'] = '[open open][write read]'
G.edge['charon']['untrusted_app']['fill'] = 'red'
G.add_edge('charon','untrusted_app')
G.edge['charon']['untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','untrusteddomain')
G.edge['charon']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['charon']['untrusteddomain']['fill'] = 'red'
G.add_edge('charon','untrusteddomain')
G.edge['charon']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','vpnclientd')
G.edge['charon']['vpnclientd']['write-read'] = '[open open][write read]'
G.edge['charon']['vpnclientd']['fill'] = 'red'
G.add_edge('charon','vpnclientd')
G.edge['charon']['vpnclientd']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','vpn_untrusted_app')
G.edge['charon']['vpn_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['charon']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('charon','vpn_untrusted_app')
G.edge['charon']['vpn_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('clatd','appdomain')
G.edge['clatd']['appdomain']['write-read'] = '[open open]'
G.add_edge('clatd','bluetooth')
G.edge['clatd']['bluetooth']['write-read'] = '[open open]'
G.add_edge('clatd','bluetooth')
G.edge['clatd']['bluetooth']['write-read'] = '[open open][open open]'
G.add_edge('clatd','carrier_app')
G.edge['clatd']['carrier_app']['write-read'] = '[open open]'
G.add_edge('clatd','charon')
G.edge['clatd']['charon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('clatd','clatd')
G.edge['clatd']['clatd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('clatd','filtered_google_app')
G.edge['clatd']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('clatd','filtered_untrusted_app')
G.edge['clatd']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('clatd','gad_untrusted_app')
G.edge['clatd']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('clatd','irm_app')
G.edge['clatd']['irm_app']['write-read'] = '[open open]'
G.add_edge('clatd','knox_untrusted_app')
G.edge['clatd']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('clatd','llk_untrusted_app')
G.edge['clatd']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('clatd','netd')
G.edge['clatd']['netd']['write-read'] = '[open open]'
G.add_edge('clatd','rild')
G.edge['clatd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('clatd','system_server')
G.edge['clatd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('clatd','trustonicpartner_app')
G.edge['clatd']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('clatd','umcagent_app')
G.edge['clatd']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('clatd','untrusted_app')
G.edge['clatd']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('clatd','untrusteddomain')
G.edge['clatd']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('clatd','vpnclientd')
G.edge['clatd']['vpnclientd']['write-read'] = '[open open]'
G.add_edge('clatd','vpn_untrusted_app')
G.edge['clatd']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('clatd','appdomain')
G.edge['clatd']['appdomain']['write-read'] = '[open open][write read]'
G.edge['clatd']['appdomain']['fill'] = 'red'
G.add_edge('clatd','appdomain')
G.edge['clatd']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('clatd','bluetooth')
G.edge['clatd']['bluetooth']['write-read'] = '[open open][open open][write read]'
G.edge['clatd']['bluetooth']['fill'] = 'red'
G.add_edge('clatd','bluetooth')
G.edge['clatd']['bluetooth']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('clatd','bluetooth')
G.edge['clatd']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['clatd']['bluetooth']['fill'] = 'red'
G.add_edge('clatd','bluetooth')
G.edge['clatd']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('clatd','carrier_app')
G.edge['clatd']['carrier_app']['write-read'] = '[open open][write read]'
G.edge['clatd']['carrier_app']['fill'] = 'red'
G.add_edge('clatd','carrier_app')
G.edge['clatd']['carrier_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('clatd','charon')
G.edge['clatd']['charon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['clatd']['charon']['fill'] = 'red'
G.add_edge('clatd','charon')
G.edge['clatd']['charon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('clatd','clatd')
G.edge['clatd']['clatd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['clatd']['clatd']['fill'] = 'red'
G.add_edge('clatd','clatd')
G.edge['clatd']['clatd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('clatd','filtered_google_app')
G.edge['clatd']['filtered_google_app']['write-read'] = '[open open][write read]'
G.edge['clatd']['filtered_google_app']['fill'] = 'red'
G.add_edge('clatd','filtered_google_app')
G.edge['clatd']['filtered_google_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('clatd','filtered_untrusted_app')
G.edge['clatd']['filtered_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['clatd']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('clatd','filtered_untrusted_app')
G.edge['clatd']['filtered_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('clatd','gad_untrusted_app')
G.edge['clatd']['gad_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['clatd']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('clatd','gad_untrusted_app')
G.edge['clatd']['gad_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('clatd','irm_app')
G.edge['clatd']['irm_app']['write-read'] = '[open open][write read]'
G.edge['clatd']['irm_app']['fill'] = 'red'
G.add_edge('clatd','irm_app')
G.edge['clatd']['irm_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('clatd','knox_untrusted_app')
G.edge['clatd']['knox_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['clatd']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('clatd','knox_untrusted_app')
G.edge['clatd']['knox_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('clatd','llk_untrusted_app')
G.edge['clatd']['llk_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['clatd']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('clatd','llk_untrusted_app')
G.edge['clatd']['llk_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('clatd','netd')
G.edge['clatd']['netd']['write-read'] = '[open open][write read]'
G.edge['clatd']['netd']['fill'] = 'red'
G.add_edge('clatd','netd')
G.edge['clatd']['netd']['write-read'] = '[open open][write read][append read]'
G.add_edge('clatd','rild')
G.edge['clatd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['clatd']['rild']['fill'] = 'red'
G.add_edge('clatd','rild')
G.edge['clatd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('clatd','system_server')
G.edge['clatd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['clatd']['system_server']['fill'] = 'red'
G.add_edge('clatd','system_server')
G.edge['clatd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('clatd','trustonicpartner_app')
G.edge['clatd']['trustonicpartner_app']['write-read'] = '[open open][write read]'
G.edge['clatd']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('clatd','trustonicpartner_app')
G.edge['clatd']['trustonicpartner_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('clatd','umcagent_app')
G.edge['clatd']['umcagent_app']['write-read'] = '[open open][write read]'
G.edge['clatd']['umcagent_app']['fill'] = 'red'
G.add_edge('clatd','umcagent_app')
G.edge['clatd']['umcagent_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('clatd','untrusted_app')
G.edge['clatd']['untrusted_app']['write-read'] = '[open open][write read]'
G.edge['clatd']['untrusted_app']['fill'] = 'red'
G.add_edge('clatd','untrusted_app')
G.edge['clatd']['untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('clatd','untrusteddomain')
G.edge['clatd']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['clatd']['untrusteddomain']['fill'] = 'red'
G.add_edge('clatd','untrusteddomain')
G.edge['clatd']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('clatd','vpnclientd')
G.edge['clatd']['vpnclientd']['write-read'] = '[open open][write read]'
G.edge['clatd']['vpnclientd']['fill'] = 'red'
G.add_edge('clatd','vpnclientd')
G.edge['clatd']['vpnclientd']['write-read'] = '[open open][write read][append read]'
G.add_edge('clatd','vpn_untrusted_app')
G.edge['clatd']['vpn_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['clatd']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('clatd','vpn_untrusted_app')
G.edge['clatd']['vpn_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('filtered_google_app','appdomain')
G.edge['filtered_google_app']['appdomain']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','bluetooth')
G.edge['filtered_google_app']['bluetooth']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','bluetooth')
G.edge['filtered_google_app']['bluetooth']['write-read'] = '[open open][open open]'
G.add_edge('filtered_google_app','carrier_app')
G.edge['filtered_google_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_google_app','charon')
G.edge['filtered_google_app']['charon']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','clatd')
G.edge['filtered_google_app']['clatd']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','filtered_google_app')
G.edge['filtered_google_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_google_app','filtered_untrusted_app')
G.edge['filtered_google_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_google_app','gad_untrusted_app')
G.edge['filtered_google_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_google_app','irm_app')
G.edge['filtered_google_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_google_app','knox_untrusted_app')
G.edge['filtered_google_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_google_app','llk_untrusted_app')
G.edge['filtered_google_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_google_app','netd')
G.edge['filtered_google_app']['netd']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','rild')
G.edge['filtered_google_app']['rild']['write-read'] = '[setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_google_app','system_server')
G.edge['filtered_google_app']['system_server']['write-read'] = '[setattr getattr][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('filtered_google_app','trustonicpartner_app')
G.edge['filtered_google_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_google_app','umcagent_app')
G.edge['filtered_google_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_google_app','untrusted_app')
G.edge['filtered_google_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_google_app','untrusteddomain')
G.edge['filtered_google_app']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','vpnclientd')
G.edge['filtered_google_app']['vpnclientd']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','vpn_untrusted_app')
G.edge['filtered_google_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_google_app','appdomain')
G.edge['filtered_google_app']['appdomain']['write-read'] = '[open open][write read]'
G.edge['filtered_google_app']['appdomain']['fill'] = 'red'
G.add_edge('filtered_google_app','appdomain')
G.edge['filtered_google_app']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('filtered_google_app','bluetooth')
G.edge['filtered_google_app']['bluetooth']['write-read'] = '[open open][open open][write read]'
G.edge['filtered_google_app']['bluetooth']['fill'] = 'red'
G.add_edge('filtered_google_app','bluetooth')
G.edge['filtered_google_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('filtered_google_app','bluetooth')
G.edge['filtered_google_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['filtered_google_app']['bluetooth']['fill'] = 'red'
G.add_edge('filtered_google_app','bluetooth')
G.edge['filtered_google_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('filtered_google_app','carrier_app')
G.edge['filtered_google_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_google_app']['carrier_app']['fill'] = 'red'
G.add_edge('filtered_google_app','carrier_app')
G.edge['filtered_google_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('filtered_google_app','charon')
G.edge['filtered_google_app']['charon']['write-read'] = '[open open][write read]'
G.edge['filtered_google_app']['charon']['fill'] = 'red'
G.add_edge('filtered_google_app','charon')
G.edge['filtered_google_app']['charon']['write-read'] = '[open open][write read][append read]'
G.add_edge('filtered_google_app','clatd')
G.edge['filtered_google_app']['clatd']['write-read'] = '[open open][write read]'
G.edge['filtered_google_app']['clatd']['fill'] = 'red'
G.add_edge('filtered_google_app','clatd')
G.edge['filtered_google_app']['clatd']['write-read'] = '[open open][write read][append read]'
G.add_edge('filtered_google_app','filtered_google_app')
G.edge['filtered_google_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_google_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('filtered_google_app','filtered_google_app')
G.edge['filtered_google_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('filtered_google_app','filtered_untrusted_app')
G.edge['filtered_google_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_google_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_google_app','filtered_untrusted_app')
G.edge['filtered_google_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('filtered_google_app','gad_untrusted_app')
G.edge['filtered_google_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_google_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_google_app','gad_untrusted_app')
G.edge['filtered_google_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('filtered_google_app','irm_app')
G.edge['filtered_google_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_google_app']['irm_app']['fill'] = 'red'
G.add_edge('filtered_google_app','irm_app')
G.edge['filtered_google_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('filtered_google_app','knox_untrusted_app')
G.edge['filtered_google_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_google_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_google_app','knox_untrusted_app')
G.edge['filtered_google_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('filtered_google_app','llk_untrusted_app')
G.edge['filtered_google_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_google_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_google_app','llk_untrusted_app')
G.edge['filtered_google_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('filtered_google_app','netd')
G.edge['filtered_google_app']['netd']['write-read'] = '[open open][write read]'
G.edge['filtered_google_app']['netd']['fill'] = 'red'
G.add_edge('filtered_google_app','netd')
G.edge['filtered_google_app']['netd']['write-read'] = '[open open][write read][append read]'
G.add_edge('filtered_google_app','rild')
G.edge['filtered_google_app']['rild']['write-read'] = '[setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_google_app']['rild']['fill'] = 'red'
G.add_edge('filtered_google_app','rild')
G.edge['filtered_google_app']['rild']['write-read'] = '[setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('filtered_google_app','system_server')
G.edge['filtered_google_app']['system_server']['write-read'] = '[setattr getattr][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read]'
G.edge['filtered_google_app']['system_server']['fill'] = 'red'
G.add_edge('filtered_google_app','system_server')
G.edge['filtered_google_app']['system_server']['write-read'] = '[setattr getattr][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read]'
G.add_edge('filtered_google_app','trustonicpartner_app')
G.edge['filtered_google_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_google_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('filtered_google_app','trustonicpartner_app')
G.edge['filtered_google_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('filtered_google_app','umcagent_app')
G.edge['filtered_google_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_google_app']['umcagent_app']['fill'] = 'red'
G.add_edge('filtered_google_app','umcagent_app')
G.edge['filtered_google_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('filtered_google_app','untrusted_app')
G.edge['filtered_google_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_google_app']['untrusted_app']['fill'] = 'red'
G.add_edge('filtered_google_app','untrusted_app')
G.edge['filtered_google_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('filtered_google_app','untrusteddomain')
G.edge['filtered_google_app']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['filtered_google_app']['untrusteddomain']['fill'] = 'red'
G.add_edge('filtered_google_app','untrusteddomain')
G.edge['filtered_google_app']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('filtered_google_app','vpnclientd')
G.edge['filtered_google_app']['vpnclientd']['write-read'] = '[open open][write read]'
G.edge['filtered_google_app']['vpnclientd']['fill'] = 'red'
G.add_edge('filtered_google_app','vpnclientd')
G.edge['filtered_google_app']['vpnclientd']['write-read'] = '[open open][write read][append read]'
G.add_edge('filtered_google_app','vpn_untrusted_app')
G.edge['filtered_google_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_google_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_google_app','vpn_untrusted_app')
G.edge['filtered_google_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('filtered_untrusted_app','appdomain')
G.edge['filtered_untrusted_app']['appdomain']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','bluetooth')
G.edge['filtered_untrusted_app']['bluetooth']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','bluetooth')
G.edge['filtered_untrusted_app']['bluetooth']['write-read'] = '[open open][open open]'
G.add_edge('filtered_untrusted_app','carrier_app')
G.edge['filtered_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_untrusted_app','charon')
G.edge['filtered_untrusted_app']['charon']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','clatd')
G.edge['filtered_untrusted_app']['clatd']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','filtered_google_app')
G.edge['filtered_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_untrusted_app','filtered_untrusted_app')
G.edge['filtered_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_untrusted_app','gad_untrusted_app')
G.edge['filtered_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_untrusted_app','irm_app')
G.edge['filtered_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_untrusted_app','knox_untrusted_app')
G.edge['filtered_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_untrusted_app','llk_untrusted_app')
G.edge['filtered_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_untrusted_app','netd')
G.edge['filtered_untrusted_app']['netd']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','rild')
G.edge['filtered_untrusted_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_untrusted_app','system_server')
G.edge['filtered_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('filtered_untrusted_app','trustonicpartner_app')
G.edge['filtered_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_untrusted_app','umcagent_app')
G.edge['filtered_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_untrusted_app','untrusted_app')
G.edge['filtered_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_untrusted_app','untrusteddomain')
G.edge['filtered_untrusted_app']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','vpnclientd')
G.edge['filtered_untrusted_app']['vpnclientd']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','vpn_untrusted_app')
G.edge['filtered_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_untrusted_app','appdomain')
G.edge['filtered_untrusted_app']['appdomain']['write-read'] = '[open open][write read]'
G.edge['filtered_untrusted_app']['appdomain']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','appdomain')
G.edge['filtered_untrusted_app']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('filtered_untrusted_app','bluetooth')
G.edge['filtered_untrusted_app']['bluetooth']['write-read'] = '[open open][open open][write read]'
G.edge['filtered_untrusted_app']['bluetooth']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','bluetooth')
G.edge['filtered_untrusted_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('filtered_untrusted_app','bluetooth')
G.edge['filtered_untrusted_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['filtered_untrusted_app']['bluetooth']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','bluetooth')
G.edge['filtered_untrusted_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('filtered_untrusted_app','carrier_app')
G.edge['filtered_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_untrusted_app']['carrier_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','carrier_app')
G.edge['filtered_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('filtered_untrusted_app','charon')
G.edge['filtered_untrusted_app']['charon']['write-read'] = '[open open][write read]'
G.edge['filtered_untrusted_app']['charon']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','charon')
G.edge['filtered_untrusted_app']['charon']['write-read'] = '[open open][write read][append read]'
G.add_edge('filtered_untrusted_app','clatd')
G.edge['filtered_untrusted_app']['clatd']['write-read'] = '[open open][write read]'
G.edge['filtered_untrusted_app']['clatd']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','clatd')
G.edge['filtered_untrusted_app']['clatd']['write-read'] = '[open open][write read][append read]'
G.add_edge('filtered_untrusted_app','filtered_google_app')
G.edge['filtered_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_untrusted_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','filtered_google_app')
G.edge['filtered_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('filtered_untrusted_app','filtered_untrusted_app')
G.edge['filtered_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_untrusted_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','filtered_untrusted_app')
G.edge['filtered_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('filtered_untrusted_app','gad_untrusted_app')
G.edge['filtered_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_untrusted_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','gad_untrusted_app')
G.edge['filtered_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('filtered_untrusted_app','irm_app')
G.edge['filtered_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_untrusted_app']['irm_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','irm_app')
G.edge['filtered_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('filtered_untrusted_app','knox_untrusted_app')
G.edge['filtered_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_untrusted_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','knox_untrusted_app')
G.edge['filtered_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('filtered_untrusted_app','llk_untrusted_app')
G.edge['filtered_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_untrusted_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','llk_untrusted_app')
G.edge['filtered_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('filtered_untrusted_app','netd')
G.edge['filtered_untrusted_app']['netd']['write-read'] = '[open open][write read]'
G.edge['filtered_untrusted_app']['netd']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','netd')
G.edge['filtered_untrusted_app']['netd']['write-read'] = '[open open][write read][append read]'
G.add_edge('filtered_untrusted_app','rild')
G.edge['filtered_untrusted_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_untrusted_app']['rild']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','rild')
G.edge['filtered_untrusted_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('filtered_untrusted_app','system_server')
G.edge['filtered_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read]'
G.edge['filtered_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','system_server')
G.edge['filtered_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read]'
G.add_edge('filtered_untrusted_app','trustonicpartner_app')
G.edge['filtered_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_untrusted_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','trustonicpartner_app')
G.edge['filtered_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('filtered_untrusted_app','umcagent_app')
G.edge['filtered_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_untrusted_app']['umcagent_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','umcagent_app')
G.edge['filtered_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('filtered_untrusted_app','untrusted_app')
G.edge['filtered_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_untrusted_app']['untrusted_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','untrusted_app')
G.edge['filtered_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('filtered_untrusted_app','untrusteddomain')
G.edge['filtered_untrusted_app']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['filtered_untrusted_app']['untrusteddomain']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','untrusteddomain')
G.edge['filtered_untrusted_app']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('filtered_untrusted_app','vpnclientd')
G.edge['filtered_untrusted_app']['vpnclientd']['write-read'] = '[open open][write read]'
G.edge['filtered_untrusted_app']['vpnclientd']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','vpnclientd')
G.edge['filtered_untrusted_app']['vpnclientd']['write-read'] = '[open open][write read][append read]'
G.add_edge('filtered_untrusted_app','vpn_untrusted_app')
G.edge['filtered_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_untrusted_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','vpn_untrusted_app')
G.edge['filtered_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('gad_untrusted_app','appdomain')
G.edge['gad_untrusted_app']['appdomain']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','bluetooth')
G.edge['gad_untrusted_app']['bluetooth']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','bluetooth')
G.edge['gad_untrusted_app']['bluetooth']['write-read'] = '[open open][open open]'
G.add_edge('gad_untrusted_app','carrier_app')
G.edge['gad_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('gad_untrusted_app','charon')
G.edge['gad_untrusted_app']['charon']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','clatd')
G.edge['gad_untrusted_app']['clatd']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','filtered_google_app')
G.edge['gad_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('gad_untrusted_app','filtered_untrusted_app')
G.edge['gad_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('gad_untrusted_app','gad_untrusted_app')
G.edge['gad_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('gad_untrusted_app','irm_app')
G.edge['gad_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('gad_untrusted_app','knox_untrusted_app')
G.edge['gad_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('gad_untrusted_app','llk_untrusted_app')
G.edge['gad_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('gad_untrusted_app','netd')
G.edge['gad_untrusted_app']['netd']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','rild')
G.edge['gad_untrusted_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gad_untrusted_app','system_server')
G.edge['gad_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('gad_untrusted_app','trustonicpartner_app')
G.edge['gad_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('gad_untrusted_app','umcagent_app')
G.edge['gad_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('gad_untrusted_app','untrusted_app')
G.edge['gad_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('gad_untrusted_app','untrusteddomain')
G.edge['gad_untrusted_app']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','vpnclientd')
G.edge['gad_untrusted_app']['vpnclientd']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','vpn_untrusted_app')
G.edge['gad_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('gad_untrusted_app','appdomain')
G.edge['gad_untrusted_app']['appdomain']['write-read'] = '[open open][write read]'
G.edge['gad_untrusted_app']['appdomain']['fill'] = 'red'
G.add_edge('gad_untrusted_app','appdomain')
G.edge['gad_untrusted_app']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('gad_untrusted_app','bluetooth')
G.edge['gad_untrusted_app']['bluetooth']['write-read'] = '[open open][open open][write read]'
G.edge['gad_untrusted_app']['bluetooth']['fill'] = 'red'
G.add_edge('gad_untrusted_app','bluetooth')
G.edge['gad_untrusted_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('gad_untrusted_app','bluetooth')
G.edge['gad_untrusted_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['gad_untrusted_app']['bluetooth']['fill'] = 'red'
G.add_edge('gad_untrusted_app','bluetooth')
G.edge['gad_untrusted_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('gad_untrusted_app','carrier_app')
G.edge['gad_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['gad_untrusted_app']['carrier_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','carrier_app')
G.edge['gad_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('gad_untrusted_app','charon')
G.edge['gad_untrusted_app']['charon']['write-read'] = '[open open][write read]'
G.edge['gad_untrusted_app']['charon']['fill'] = 'red'
G.add_edge('gad_untrusted_app','charon')
G.edge['gad_untrusted_app']['charon']['write-read'] = '[open open][write read][append read]'
G.add_edge('gad_untrusted_app','clatd')
G.edge['gad_untrusted_app']['clatd']['write-read'] = '[open open][write read]'
G.edge['gad_untrusted_app']['clatd']['fill'] = 'red'
G.add_edge('gad_untrusted_app','clatd')
G.edge['gad_untrusted_app']['clatd']['write-read'] = '[open open][write read][append read]'
G.add_edge('gad_untrusted_app','filtered_google_app')
G.edge['gad_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['gad_untrusted_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','filtered_google_app')
G.edge['gad_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('gad_untrusted_app','filtered_untrusted_app')
G.edge['gad_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['gad_untrusted_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','filtered_untrusted_app')
G.edge['gad_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('gad_untrusted_app','gad_untrusted_app')
G.edge['gad_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['gad_untrusted_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','gad_untrusted_app')
G.edge['gad_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('gad_untrusted_app','irm_app')
G.edge['gad_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['gad_untrusted_app']['irm_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','irm_app')
G.edge['gad_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('gad_untrusted_app','knox_untrusted_app')
G.edge['gad_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['gad_untrusted_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','knox_untrusted_app')
G.edge['gad_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('gad_untrusted_app','llk_untrusted_app')
G.edge['gad_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['gad_untrusted_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','llk_untrusted_app')
G.edge['gad_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('gad_untrusted_app','netd')
G.edge['gad_untrusted_app']['netd']['write-read'] = '[open open][write read]'
G.edge['gad_untrusted_app']['netd']['fill'] = 'red'
G.add_edge('gad_untrusted_app','netd')
G.edge['gad_untrusted_app']['netd']['write-read'] = '[open open][write read][append read]'
G.add_edge('gad_untrusted_app','rild')
G.edge['gad_untrusted_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['gad_untrusted_app']['rild']['fill'] = 'red'
G.add_edge('gad_untrusted_app','rild')
G.edge['gad_untrusted_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('gad_untrusted_app','system_server')
G.edge['gad_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read]'
G.edge['gad_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('gad_untrusted_app','system_server')
G.edge['gad_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read]'
G.add_edge('gad_untrusted_app','trustonicpartner_app')
G.edge['gad_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['gad_untrusted_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','trustonicpartner_app')
G.edge['gad_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('gad_untrusted_app','umcagent_app')
G.edge['gad_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['gad_untrusted_app']['umcagent_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','umcagent_app')
G.edge['gad_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('gad_untrusted_app','untrusted_app')
G.edge['gad_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['gad_untrusted_app']['untrusted_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','untrusted_app')
G.edge['gad_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('gad_untrusted_app','untrusteddomain')
G.edge['gad_untrusted_app']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['gad_untrusted_app']['untrusteddomain']['fill'] = 'red'
G.add_edge('gad_untrusted_app','untrusteddomain')
G.edge['gad_untrusted_app']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('gad_untrusted_app','vpnclientd')
G.edge['gad_untrusted_app']['vpnclientd']['write-read'] = '[open open][write read]'
G.edge['gad_untrusted_app']['vpnclientd']['fill'] = 'red'
G.add_edge('gad_untrusted_app','vpnclientd')
G.edge['gad_untrusted_app']['vpnclientd']['write-read'] = '[open open][write read][append read]'
G.add_edge('gad_untrusted_app','vpn_untrusted_app')
G.edge['gad_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['gad_untrusted_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','vpn_untrusted_app')
G.edge['gad_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('irm_app','appdomain')
G.edge['irm_app']['appdomain']['write-read'] = '[open open]'
G.add_edge('irm_app','bluetooth')
G.edge['irm_app']['bluetooth']['write-read'] = '[setopt getopt][open open]'
G.add_edge('irm_app','bluetooth')
G.edge['irm_app']['bluetooth']['write-read'] = '[setopt getopt][open open][open open]'
G.add_edge('irm_app','carrier_app')
G.edge['irm_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('irm_app','charon')
G.edge['irm_app']['charon']['write-read'] = '[open open]'
G.add_edge('irm_app','clatd')
G.edge['irm_app']['clatd']['write-read'] = '[open open]'
G.add_edge('irm_app','filtered_google_app')
G.edge['irm_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('irm_app','filtered_untrusted_app')
G.edge['irm_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('irm_app','gad_untrusted_app')
G.edge['irm_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('irm_app','irm_app')
G.edge['irm_app']['irm_app']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('irm_app','knox_untrusted_app')
G.edge['irm_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('irm_app','llk_untrusted_app')
G.edge['irm_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('irm_app','netd')
G.edge['irm_app']['netd']['write-read'] = '[open open]'
G.add_edge('irm_app','rild')
G.edge['irm_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('irm_app','system_server')
G.edge['irm_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('irm_app','trustonicpartner_app')
G.edge['irm_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('irm_app','umcagent_app')
G.edge['irm_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('irm_app','untrusted_app')
G.edge['irm_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('irm_app','untrusteddomain')
G.edge['irm_app']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('irm_app','vpnclientd')
G.edge['irm_app']['vpnclientd']['write-read'] = '[open open]'
G.add_edge('irm_app','vpn_untrusted_app')
G.edge['irm_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('irm_app','appdomain')
G.edge['irm_app']['appdomain']['write-read'] = '[open open][write read]'
G.edge['irm_app']['appdomain']['fill'] = 'red'
G.add_edge('irm_app','appdomain')
G.edge['irm_app']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('irm_app','bluetooth')
G.edge['irm_app']['bluetooth']['write-read'] = '[setopt getopt][open open][open open][write read]'
G.edge['irm_app']['bluetooth']['fill'] = 'red'
G.add_edge('irm_app','bluetooth')
G.edge['irm_app']['bluetooth']['write-read'] = '[setopt getopt][open open][open open][write read][append read]'
G.add_edge('irm_app','bluetooth')
G.edge['irm_app']['bluetooth']['write-read'] = '[setopt getopt][open open][open open][write read][append read][write read]'
G.edge['irm_app']['bluetooth']['fill'] = 'red'
G.add_edge('irm_app','bluetooth')
G.edge['irm_app']['bluetooth']['write-read'] = '[setopt getopt][open open][open open][write read][append read][write read][append read]'
G.add_edge('irm_app','carrier_app')
G.edge['irm_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['irm_app']['carrier_app']['fill'] = 'red'
G.add_edge('irm_app','carrier_app')
G.edge['irm_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('irm_app','charon')
G.edge['irm_app']['charon']['write-read'] = '[open open][write read]'
G.edge['irm_app']['charon']['fill'] = 'red'
G.add_edge('irm_app','charon')
G.edge['irm_app']['charon']['write-read'] = '[open open][write read][append read]'
G.add_edge('irm_app','clatd')
G.edge['irm_app']['clatd']['write-read'] = '[open open][write read]'
G.edge['irm_app']['clatd']['fill'] = 'red'
G.add_edge('irm_app','clatd')
G.edge['irm_app']['clatd']['write-read'] = '[open open][write read][append read]'
G.add_edge('irm_app','filtered_google_app')
G.edge['irm_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['irm_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('irm_app','filtered_google_app')
G.edge['irm_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('irm_app','filtered_untrusted_app')
G.edge['irm_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['irm_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('irm_app','filtered_untrusted_app')
G.edge['irm_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('irm_app','gad_untrusted_app')
G.edge['irm_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['irm_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('irm_app','gad_untrusted_app')
G.edge['irm_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('irm_app','irm_app')
G.edge['irm_app']['irm_app']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['irm_app']['irm_app']['fill'] = 'red'
G.add_edge('irm_app','irm_app')
G.edge['irm_app']['irm_app']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('irm_app','knox_untrusted_app')
G.edge['irm_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['irm_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('irm_app','knox_untrusted_app')
G.edge['irm_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('irm_app','llk_untrusted_app')
G.edge['irm_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['irm_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('irm_app','llk_untrusted_app')
G.edge['irm_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('irm_app','netd')
G.edge['irm_app']['netd']['write-read'] = '[open open][write read]'
G.edge['irm_app']['netd']['fill'] = 'red'
G.add_edge('irm_app','netd')
G.edge['irm_app']['netd']['write-read'] = '[open open][write read][append read]'
G.add_edge('irm_app','rild')
G.edge['irm_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['irm_app']['rild']['fill'] = 'red'
G.add_edge('irm_app','rild')
G.edge['irm_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('irm_app','system_server')
G.edge['irm_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read]'
G.edge['irm_app']['system_server']['fill'] = 'red'
G.add_edge('irm_app','system_server')
G.edge['irm_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read]'
G.add_edge('irm_app','trustonicpartner_app')
G.edge['irm_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['irm_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('irm_app','trustonicpartner_app')
G.edge['irm_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('irm_app','umcagent_app')
G.edge['irm_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['irm_app']['umcagent_app']['fill'] = 'red'
G.add_edge('irm_app','umcagent_app')
G.edge['irm_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('irm_app','untrusted_app')
G.edge['irm_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['irm_app']['untrusted_app']['fill'] = 'red'
G.add_edge('irm_app','untrusted_app')
G.edge['irm_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('irm_app','untrusteddomain')
G.edge['irm_app']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['irm_app']['untrusteddomain']['fill'] = 'red'
G.add_edge('irm_app','untrusteddomain')
G.edge['irm_app']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('irm_app','vpnclientd')
G.edge['irm_app']['vpnclientd']['write-read'] = '[open open][write read]'
G.edge['irm_app']['vpnclientd']['fill'] = 'red'
G.add_edge('irm_app','vpnclientd')
G.edge['irm_app']['vpnclientd']['write-read'] = '[open open][write read][append read]'
G.add_edge('irm_app','vpn_untrusted_app')
G.edge['irm_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['irm_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('irm_app','vpn_untrusted_app')
G.edge['irm_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('knox_untrusted_app','appdomain')
G.edge['knox_untrusted_app']['appdomain']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','bluetooth')
G.edge['knox_untrusted_app']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_untrusted_app','bluetooth')
G.edge['knox_untrusted_app']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('knox_untrusted_app','carrier_app')
G.edge['knox_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_untrusted_app','charon')
G.edge['knox_untrusted_app']['charon']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','clatd')
G.edge['knox_untrusted_app']['clatd']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','filtered_google_app')
G.edge['knox_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_untrusted_app','filtered_untrusted_app')
G.edge['knox_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_untrusted_app','gad_untrusted_app')
G.edge['knox_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_untrusted_app','irm_app')
G.edge['knox_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_untrusted_app','knox_untrusted_app')
G.edge['knox_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_untrusted_app','llk_untrusted_app')
G.edge['knox_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_untrusted_app','netd')
G.edge['knox_untrusted_app']['netd']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','rild')
G.edge['knox_untrusted_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_untrusted_app','system_server')
G.edge['knox_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_untrusted_app','trustonicpartner_app')
G.edge['knox_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_untrusted_app','umcagent_app')
G.edge['knox_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_untrusted_app','untrusted_app')
G.edge['knox_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_untrusted_app','untrusteddomain')
G.edge['knox_untrusted_app']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_untrusted_app','vpnclientd')
G.edge['knox_untrusted_app']['vpnclientd']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','vpn_untrusted_app')
G.edge['knox_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_untrusted_app','appdomain')
G.edge['knox_untrusted_app']['appdomain']['write-read'] = '[open open][write read]'
G.edge['knox_untrusted_app']['appdomain']['fill'] = 'red'
G.add_edge('knox_untrusted_app','appdomain')
G.edge['knox_untrusted_app']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('knox_untrusted_app','bluetooth')
G.edge['knox_untrusted_app']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read]'
G.edge['knox_untrusted_app']['bluetooth']['fill'] = 'red'
G.add_edge('knox_untrusted_app','bluetooth')
G.edge['knox_untrusted_app']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read][append read]'
G.add_edge('knox_untrusted_app','bluetooth')
G.edge['knox_untrusted_app']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read]'
G.edge['knox_untrusted_app']['bluetooth']['fill'] = 'red'
G.add_edge('knox_untrusted_app','bluetooth')
G.edge['knox_untrusted_app']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read]'
G.add_edge('knox_untrusted_app','carrier_app')
G.edge['knox_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['knox_untrusted_app']['carrier_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','carrier_app')
G.edge['knox_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('knox_untrusted_app','charon')
G.edge['knox_untrusted_app']['charon']['write-read'] = '[open open][write read]'
G.edge['knox_untrusted_app']['charon']['fill'] = 'red'
G.add_edge('knox_untrusted_app','charon')
G.edge['knox_untrusted_app']['charon']['write-read'] = '[open open][write read][append read]'
G.add_edge('knox_untrusted_app','clatd')
G.edge['knox_untrusted_app']['clatd']['write-read'] = '[open open][write read]'
G.edge['knox_untrusted_app']['clatd']['fill'] = 'red'
G.add_edge('knox_untrusted_app','clatd')
G.edge['knox_untrusted_app']['clatd']['write-read'] = '[open open][write read][append read]'
G.add_edge('knox_untrusted_app','filtered_google_app')
G.edge['knox_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['knox_untrusted_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','filtered_google_app')
G.edge['knox_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('knox_untrusted_app','filtered_untrusted_app')
G.edge['knox_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['knox_untrusted_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','filtered_untrusted_app')
G.edge['knox_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('knox_untrusted_app','gad_untrusted_app')
G.edge['knox_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['knox_untrusted_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','gad_untrusted_app')
G.edge['knox_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('knox_untrusted_app','irm_app')
G.edge['knox_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['knox_untrusted_app']['irm_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','irm_app')
G.edge['knox_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('knox_untrusted_app','knox_untrusted_app')
G.edge['knox_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['knox_untrusted_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','knox_untrusted_app')
G.edge['knox_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('knox_untrusted_app','llk_untrusted_app')
G.edge['knox_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['knox_untrusted_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','llk_untrusted_app')
G.edge['knox_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('knox_untrusted_app','netd')
G.edge['knox_untrusted_app']['netd']['write-read'] = '[open open][write read]'
G.edge['knox_untrusted_app']['netd']['fill'] = 'red'
G.add_edge('knox_untrusted_app','netd')
G.edge['knox_untrusted_app']['netd']['write-read'] = '[open open][write read][append read]'
G.add_edge('knox_untrusted_app','rild')
G.edge['knox_untrusted_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['knox_untrusted_app']['rild']['fill'] = 'red'
G.add_edge('knox_untrusted_app','rild')
G.edge['knox_untrusted_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('knox_untrusted_app','system_server')
G.edge['knox_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['knox_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('knox_untrusted_app','system_server')
G.edge['knox_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('knox_untrusted_app','trustonicpartner_app')
G.edge['knox_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['knox_untrusted_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','trustonicpartner_app')
G.edge['knox_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('knox_untrusted_app','umcagent_app')
G.edge['knox_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['knox_untrusted_app']['umcagent_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','umcagent_app')
G.edge['knox_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('knox_untrusted_app','untrusted_app')
G.edge['knox_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['knox_untrusted_app']['untrusted_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','untrusted_app')
G.edge['knox_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('knox_untrusted_app','untrusteddomain')
G.edge['knox_untrusted_app']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['knox_untrusted_app']['untrusteddomain']['fill'] = 'red'
G.add_edge('knox_untrusted_app','untrusteddomain')
G.edge['knox_untrusted_app']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('knox_untrusted_app','vpnclientd')
G.edge['knox_untrusted_app']['vpnclientd']['write-read'] = '[open open][write read]'
G.edge['knox_untrusted_app']['vpnclientd']['fill'] = 'red'
G.add_edge('knox_untrusted_app','vpnclientd')
G.edge['knox_untrusted_app']['vpnclientd']['write-read'] = '[open open][write read][append read]'
G.add_edge('knox_untrusted_app','vpn_untrusted_app')
G.edge['knox_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['knox_untrusted_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','vpn_untrusted_app')
G.edge['knox_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('llk_untrusted_app','appdomain')
G.edge['llk_untrusted_app']['appdomain']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','bluetooth')
G.edge['llk_untrusted_app']['bluetooth']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','bluetooth')
G.edge['llk_untrusted_app']['bluetooth']['write-read'] = '[open open][open open]'
G.add_edge('llk_untrusted_app','carrier_app')
G.edge['llk_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('llk_untrusted_app','charon')
G.edge['llk_untrusted_app']['charon']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','clatd')
G.edge['llk_untrusted_app']['clatd']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','filtered_google_app')
G.edge['llk_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('llk_untrusted_app','filtered_untrusted_app')
G.edge['llk_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('llk_untrusted_app','gad_untrusted_app')
G.edge['llk_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('llk_untrusted_app','irm_app')
G.edge['llk_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('llk_untrusted_app','knox_untrusted_app')
G.edge['llk_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('llk_untrusted_app','llk_untrusted_app')
G.edge['llk_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('llk_untrusted_app','netd')
G.edge['llk_untrusted_app']['netd']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','rild')
G.edge['llk_untrusted_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('llk_untrusted_app','system_server')
G.edge['llk_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('llk_untrusted_app','trustonicpartner_app')
G.edge['llk_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('llk_untrusted_app','umcagent_app')
G.edge['llk_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('llk_untrusted_app','untrusted_app')
G.edge['llk_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('llk_untrusted_app','untrusteddomain')
G.edge['llk_untrusted_app']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','vpnclientd')
G.edge['llk_untrusted_app']['vpnclientd']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','vpn_untrusted_app')
G.edge['llk_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('llk_untrusted_app','appdomain')
G.edge['llk_untrusted_app']['appdomain']['write-read'] = '[open open][write read]'
G.edge['llk_untrusted_app']['appdomain']['fill'] = 'red'
G.add_edge('llk_untrusted_app','appdomain')
G.edge['llk_untrusted_app']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('llk_untrusted_app','bluetooth')
G.edge['llk_untrusted_app']['bluetooth']['write-read'] = '[open open][open open][write read]'
G.edge['llk_untrusted_app']['bluetooth']['fill'] = 'red'
G.add_edge('llk_untrusted_app','bluetooth')
G.edge['llk_untrusted_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('llk_untrusted_app','bluetooth')
G.edge['llk_untrusted_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['llk_untrusted_app']['bluetooth']['fill'] = 'red'
G.add_edge('llk_untrusted_app','bluetooth')
G.edge['llk_untrusted_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('llk_untrusted_app','carrier_app')
G.edge['llk_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['llk_untrusted_app']['carrier_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','carrier_app')
G.edge['llk_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('llk_untrusted_app','charon')
G.edge['llk_untrusted_app']['charon']['write-read'] = '[open open][write read]'
G.edge['llk_untrusted_app']['charon']['fill'] = 'red'
G.add_edge('llk_untrusted_app','charon')
G.edge['llk_untrusted_app']['charon']['write-read'] = '[open open][write read][append read]'
G.add_edge('llk_untrusted_app','clatd')
G.edge['llk_untrusted_app']['clatd']['write-read'] = '[open open][write read]'
G.edge['llk_untrusted_app']['clatd']['fill'] = 'red'
G.add_edge('llk_untrusted_app','clatd')
G.edge['llk_untrusted_app']['clatd']['write-read'] = '[open open][write read][append read]'
G.add_edge('llk_untrusted_app','filtered_google_app')
G.edge['llk_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['llk_untrusted_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','filtered_google_app')
G.edge['llk_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('llk_untrusted_app','filtered_untrusted_app')
G.edge['llk_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['llk_untrusted_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','filtered_untrusted_app')
G.edge['llk_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('llk_untrusted_app','gad_untrusted_app')
G.edge['llk_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['llk_untrusted_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','gad_untrusted_app')
G.edge['llk_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('llk_untrusted_app','irm_app')
G.edge['llk_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['llk_untrusted_app']['irm_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','irm_app')
G.edge['llk_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('llk_untrusted_app','knox_untrusted_app')
G.edge['llk_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['llk_untrusted_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','knox_untrusted_app')
G.edge['llk_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('llk_untrusted_app','llk_untrusted_app')
G.edge['llk_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['llk_untrusted_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','llk_untrusted_app')
G.edge['llk_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('llk_untrusted_app','netd')
G.edge['llk_untrusted_app']['netd']['write-read'] = '[open open][write read]'
G.edge['llk_untrusted_app']['netd']['fill'] = 'red'
G.add_edge('llk_untrusted_app','netd')
G.edge['llk_untrusted_app']['netd']['write-read'] = '[open open][write read][append read]'
G.add_edge('llk_untrusted_app','rild')
G.edge['llk_untrusted_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['llk_untrusted_app']['rild']['fill'] = 'red'
G.add_edge('llk_untrusted_app','rild')
G.edge['llk_untrusted_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('llk_untrusted_app','system_server')
G.edge['llk_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read]'
G.edge['llk_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('llk_untrusted_app','system_server')
G.edge['llk_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read]'
G.add_edge('llk_untrusted_app','trustonicpartner_app')
G.edge['llk_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['llk_untrusted_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','trustonicpartner_app')
G.edge['llk_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('llk_untrusted_app','umcagent_app')
G.edge['llk_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['llk_untrusted_app']['umcagent_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','umcagent_app')
G.edge['llk_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('llk_untrusted_app','untrusted_app')
G.edge['llk_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['llk_untrusted_app']['untrusted_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','untrusted_app')
G.edge['llk_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('llk_untrusted_app','untrusteddomain')
G.edge['llk_untrusted_app']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['llk_untrusted_app']['untrusteddomain']['fill'] = 'red'
G.add_edge('llk_untrusted_app','untrusteddomain')
G.edge['llk_untrusted_app']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('llk_untrusted_app','vpnclientd')
G.edge['llk_untrusted_app']['vpnclientd']['write-read'] = '[open open][write read]'
G.edge['llk_untrusted_app']['vpnclientd']['fill'] = 'red'
G.add_edge('llk_untrusted_app','vpnclientd')
G.edge['llk_untrusted_app']['vpnclientd']['write-read'] = '[open open][write read][append read]'
G.add_edge('llk_untrusted_app','vpn_untrusted_app')
G.edge['llk_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['llk_untrusted_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','vpn_untrusted_app')
G.edge['llk_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('netd','appdomain')
G.edge['netd']['appdomain']['write-read'] = '[write read][open open]'
G.add_edge('netd','bluetooth')
G.edge['netd']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('netd','bluetooth')
G.edge['netd']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('netd','carrier_app')
G.edge['netd']['carrier_app']['write-read'] = '[open open]'
G.add_edge('netd','charon')
G.edge['netd']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','clatd')
G.edge['netd']['clatd']['write-read'] = '[add_name search][open open]'
G.add_edge('netd','filtered_google_app')
G.edge['netd']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('netd','filtered_untrusted_app')
G.edge['netd']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('netd','gad_untrusted_app')
G.edge['netd']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('netd','irm_app')
G.edge['netd']['irm_app']['write-read'] = '[open open]'
G.add_edge('netd','knox_untrusted_app')
G.edge['netd']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('netd','llk_untrusted_app')
G.edge['netd']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','rild')
G.edge['netd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('netd','trustonicpartner_app')
G.edge['netd']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('netd','umcagent_app')
G.edge['netd']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('netd','untrusted_app')
G.edge['netd']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('netd','untrusteddomain')
G.edge['netd']['untrusteddomain']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('netd','vpnclientd')
G.edge['netd']['vpnclientd']['write-read'] = '[open open]'
G.add_edge('netd','vpn_untrusted_app')
G.edge['netd']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('netd','appdomain')
G.edge['netd']['appdomain']['write-read'] = '[write read][open open][write read]'
G.edge['netd']['appdomain']['fill'] = 'red'
G.add_edge('netd','appdomain')
G.edge['netd']['appdomain']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('netd','bluetooth')
G.edge['netd']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][open open][write read]'
G.edge['netd']['bluetooth']['fill'] = 'red'
G.add_edge('netd','bluetooth')
G.edge['netd']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][open open][write read][append read]'
G.add_edge('netd','bluetooth')
G.edge['netd']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read]'
G.edge['netd']['bluetooth']['fill'] = 'red'
G.add_edge('netd','bluetooth')
G.edge['netd']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read]'
G.add_edge('netd','carrier_app')
G.edge['netd']['carrier_app']['write-read'] = '[open open][write read]'
G.edge['netd']['carrier_app']['fill'] = 'red'
G.add_edge('netd','carrier_app')
G.edge['netd']['carrier_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('netd','charon')
G.edge['netd']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['netd']['charon']['fill'] = 'red'
G.add_edge('netd','charon')
G.edge['netd']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('netd','clatd')
G.edge['netd']['clatd']['write-read'] = '[add_name search][open open][write read]'
G.edge['netd']['clatd']['fill'] = 'red'
G.add_edge('netd','clatd')
G.edge['netd']['clatd']['write-read'] = '[add_name search][open open][write read][append read]'
G.add_edge('netd','filtered_google_app')
G.edge['netd']['filtered_google_app']['write-read'] = '[open open][write read]'
G.edge['netd']['filtered_google_app']['fill'] = 'red'
G.add_edge('netd','filtered_google_app')
G.edge['netd']['filtered_google_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('netd','filtered_untrusted_app')
G.edge['netd']['filtered_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['netd']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('netd','filtered_untrusted_app')
G.edge['netd']['filtered_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('netd','gad_untrusted_app')
G.edge['netd']['gad_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['netd']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('netd','gad_untrusted_app')
G.edge['netd']['gad_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('netd','irm_app')
G.edge['netd']['irm_app']['write-read'] = '[open open][write read]'
G.edge['netd']['irm_app']['fill'] = 'red'
G.add_edge('netd','irm_app')
G.edge['netd']['irm_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('netd','knox_untrusted_app')
G.edge['netd']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['netd']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('netd','knox_untrusted_app')
G.edge['netd']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('netd','llk_untrusted_app')
G.edge['netd']['llk_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['netd']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('netd','llk_untrusted_app')
G.edge['netd']['llk_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['netd']['netd']['fill'] = 'red'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('netd','rild')
G.edge['netd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['netd']['rild']['fill'] = 'red'
G.add_edge('netd','rild')
G.edge['netd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['netd']['system_server']['fill'] = 'red'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('netd','trustonicpartner_app')
G.edge['netd']['trustonicpartner_app']['write-read'] = '[open open][write read]'
G.edge['netd']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('netd','trustonicpartner_app')
G.edge['netd']['trustonicpartner_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('netd','umcagent_app')
G.edge['netd']['umcagent_app']['write-read'] = '[open open][write read]'
G.edge['netd']['umcagent_app']['fill'] = 'red'
G.add_edge('netd','umcagent_app')
G.edge['netd']['umcagent_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('netd','untrusted_app')
G.edge['netd']['untrusted_app']['write-read'] = '[open open][write read]'
G.edge['netd']['untrusted_app']['fill'] = 'red'
G.add_edge('netd','untrusted_app')
G.edge['netd']['untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('netd','untrusteddomain')
G.edge['netd']['untrusteddomain']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['netd']['untrusteddomain']['fill'] = 'red'
G.add_edge('netd','untrusteddomain')
G.edge['netd']['untrusteddomain']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('netd','vpnclientd')
G.edge['netd']['vpnclientd']['write-read'] = '[open open][write read]'
G.edge['netd']['vpnclientd']['fill'] = 'red'
G.add_edge('netd','vpnclientd')
G.edge['netd']['vpnclientd']['write-read'] = '[open open][write read][append read]'
G.add_edge('netd','vpn_untrusted_app')
G.edge['netd']['vpn_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['netd']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('netd','vpn_untrusted_app')
G.edge['netd']['vpn_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('racoon','appdomain')
G.edge['racoon']['appdomain']['write-read'] = '[open open]'
G.add_edge('racoon','bluetooth')
G.edge['racoon']['bluetooth']['write-read'] = '[open open]'
G.add_edge('racoon','bluetooth')
G.edge['racoon']['bluetooth']['write-read'] = '[open open][open open]'
G.add_edge('racoon','carrier_app')
G.edge['racoon']['carrier_app']['write-read'] = '[open open]'
G.add_edge('racoon','charon')
G.edge['racoon']['charon']['write-read'] = '[open open]'
G.add_edge('racoon','clatd')
G.edge['racoon']['clatd']['write-read'] = '[open open]'
G.add_edge('racoon','filtered_google_app')
G.edge['racoon']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('racoon','filtered_untrusted_app')
G.edge['racoon']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('racoon','gad_untrusted_app')
G.edge['racoon']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('racoon','irm_app')
G.edge['racoon']['irm_app']['write-read'] = '[open open]'
G.add_edge('racoon','knox_untrusted_app')
G.edge['racoon']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('racoon','llk_untrusted_app')
G.edge['racoon']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('racoon','netd')
G.edge['racoon']['netd']['write-read'] = '[open open]'
G.add_edge('racoon','rild')
G.edge['racoon']['rild']['write-read'] = '[open open]'
G.add_edge('racoon','system_server')
G.edge['racoon']['system_server']['write-read'] = '[open open]'
G.add_edge('racoon','trustonicpartner_app')
G.edge['racoon']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('racoon','umcagent_app')
G.edge['racoon']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('racoon','untrusted_app')
G.edge['racoon']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('racoon','untrusteddomain')
G.edge['racoon']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('racoon','vpnclientd')
G.edge['racoon']['vpnclientd']['write-read'] = '[open open]'
G.add_edge('racoon','vpn_untrusted_app')
G.edge['racoon']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('racoon','appdomain')
G.edge['racoon']['appdomain']['write-read'] = '[open open][write read]'
G.edge['racoon']['appdomain']['fill'] = 'red'
G.add_edge('racoon','appdomain')
G.edge['racoon']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('racoon','bluetooth')
G.edge['racoon']['bluetooth']['write-read'] = '[open open][open open][write read]'
G.edge['racoon']['bluetooth']['fill'] = 'red'
G.add_edge('racoon','bluetooth')
G.edge['racoon']['bluetooth']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('racoon','bluetooth')
G.edge['racoon']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['racoon']['bluetooth']['fill'] = 'red'
G.add_edge('racoon','bluetooth')
G.edge['racoon']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('racoon','carrier_app')
G.edge['racoon']['carrier_app']['write-read'] = '[open open][write read]'
G.edge['racoon']['carrier_app']['fill'] = 'red'
G.add_edge('racoon','carrier_app')
G.edge['racoon']['carrier_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('racoon','charon')
G.edge['racoon']['charon']['write-read'] = '[open open][write read]'
G.edge['racoon']['charon']['fill'] = 'red'
G.add_edge('racoon','charon')
G.edge['racoon']['charon']['write-read'] = '[open open][write read][append read]'
G.add_edge('racoon','clatd')
G.edge['racoon']['clatd']['write-read'] = '[open open][write read]'
G.edge['racoon']['clatd']['fill'] = 'red'
G.add_edge('racoon','clatd')
G.edge['racoon']['clatd']['write-read'] = '[open open][write read][append read]'
G.add_edge('racoon','filtered_google_app')
G.edge['racoon']['filtered_google_app']['write-read'] = '[open open][write read]'
G.edge['racoon']['filtered_google_app']['fill'] = 'red'
G.add_edge('racoon','filtered_google_app')
G.edge['racoon']['filtered_google_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('racoon','filtered_untrusted_app')
G.edge['racoon']['filtered_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['racoon']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('racoon','filtered_untrusted_app')
G.edge['racoon']['filtered_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('racoon','gad_untrusted_app')
G.edge['racoon']['gad_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['racoon']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('racoon','gad_untrusted_app')
G.edge['racoon']['gad_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('racoon','irm_app')
G.edge['racoon']['irm_app']['write-read'] = '[open open][write read]'
G.edge['racoon']['irm_app']['fill'] = 'red'
G.add_edge('racoon','irm_app')
G.edge['racoon']['irm_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('racoon','knox_untrusted_app')
G.edge['racoon']['knox_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['racoon']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('racoon','knox_untrusted_app')
G.edge['racoon']['knox_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('racoon','llk_untrusted_app')
G.edge['racoon']['llk_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['racoon']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('racoon','llk_untrusted_app')
G.edge['racoon']['llk_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('racoon','netd')
G.edge['racoon']['netd']['write-read'] = '[open open][write read]'
G.edge['racoon']['netd']['fill'] = 'red'
G.add_edge('racoon','netd')
G.edge['racoon']['netd']['write-read'] = '[open open][write read][append read]'
G.add_edge('racoon','rild')
G.edge['racoon']['rild']['write-read'] = '[open open][write read]'
G.edge['racoon']['rild']['fill'] = 'red'
G.add_edge('racoon','rild')
G.edge['racoon']['rild']['write-read'] = '[open open][write read][append read]'
G.add_edge('racoon','system_server')
G.edge['racoon']['system_server']['write-read'] = '[open open][write read]'
G.edge['racoon']['system_server']['fill'] = 'red'
G.add_edge('racoon','system_server')
G.edge['racoon']['system_server']['write-read'] = '[open open][write read][append read]'
G.add_edge('racoon','trustonicpartner_app')
G.edge['racoon']['trustonicpartner_app']['write-read'] = '[open open][write read]'
G.edge['racoon']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('racoon','trustonicpartner_app')
G.edge['racoon']['trustonicpartner_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('racoon','umcagent_app')
G.edge['racoon']['umcagent_app']['write-read'] = '[open open][write read]'
G.edge['racoon']['umcagent_app']['fill'] = 'red'
G.add_edge('racoon','umcagent_app')
G.edge['racoon']['umcagent_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('racoon','untrusted_app')
G.edge['racoon']['untrusted_app']['write-read'] = '[open open][write read]'
G.edge['racoon']['untrusted_app']['fill'] = 'red'
G.add_edge('racoon','untrusted_app')
G.edge['racoon']['untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('racoon','untrusteddomain')
G.edge['racoon']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['racoon']['untrusteddomain']['fill'] = 'red'
G.add_edge('racoon','untrusteddomain')
G.edge['racoon']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('racoon','vpnclientd')
G.edge['racoon']['vpnclientd']['write-read'] = '[open open][write read]'
G.edge['racoon']['vpnclientd']['fill'] = 'red'
G.add_edge('racoon','vpnclientd')
G.edge['racoon']['vpnclientd']['write-read'] = '[open open][write read][append read]'
G.add_edge('racoon','vpn_untrusted_app')
G.edge['racoon']['vpn_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['racoon']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('racoon','vpn_untrusted_app')
G.edge['racoon']['vpn_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('rild','appdomain')
G.edge['rild']['appdomain']['write-read'] = '[open open]'
G.add_edge('rild','bluetooth')
G.edge['rild']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('rild','bluetooth')
G.edge['rild']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('rild','carrier_app')
G.edge['rild']['carrier_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','charon')
G.edge['rild']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','clatd')
G.edge['rild']['clatd']['write-read'] = '[add_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open]'
G.add_edge('rild','filtered_google_app')
G.edge['rild']['filtered_google_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','filtered_untrusted_app')
G.edge['rild']['filtered_untrusted_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','gad_untrusted_app')
G.edge['rild']['gad_untrusted_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','irm_app')
G.edge['rild']['irm_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','knox_untrusted_app')
G.edge['rild']['knox_untrusted_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('rild','llk_untrusted_app')
G.edge['rild']['llk_untrusted_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','netd')
G.edge['rild']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('rild','trustonicpartner_app')
G.edge['rild']['trustonicpartner_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','umcagent_app')
G.edge['rild']['umcagent_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','untrusted_app')
G.edge['rild']['untrusted_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','untrusteddomain')
G.edge['rild']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('rild','vpnclientd')
G.edge['rild']['vpnclientd']['write-read'] = '[write read][open open]'
G.add_edge('rild','vpn_untrusted_app')
G.edge['rild']['vpn_untrusted_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','appdomain')
G.edge['rild']['appdomain']['write-read'] = '[open open][write read]'
G.edge['rild']['appdomain']['fill'] = 'red'
G.add_edge('rild','appdomain')
G.edge['rild']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('rild','bluetooth')
G.edge['rild']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read]'
G.edge['rild']['bluetooth']['fill'] = 'red'
G.add_edge('rild','bluetooth')
G.edge['rild']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read]'
G.add_edge('rild','bluetooth')
G.edge['rild']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read]'
G.edge['rild']['bluetooth']['fill'] = 'red'
G.add_edge('rild','bluetooth')
G.edge['rild']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read]'
G.add_edge('rild','carrier_app')
G.edge['rild']['carrier_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['carrier_app']['fill'] = 'red'
G.add_edge('rild','carrier_app')
G.edge['rild']['carrier_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','charon')
G.edge['rild']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['charon']['fill'] = 'red'
G.add_edge('rild','charon')
G.edge['rild']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','clatd')
G.edge['rild']['clatd']['write-read'] = '[add_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read]'
G.edge['rild']['clatd']['fill'] = 'red'
G.add_edge('rild','clatd')
G.edge['rild']['clatd']['write-read'] = '[add_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read]'
G.add_edge('rild','filtered_google_app')
G.edge['rild']['filtered_google_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['filtered_google_app']['fill'] = 'red'
G.add_edge('rild','filtered_google_app')
G.edge['rild']['filtered_google_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','filtered_untrusted_app')
G.edge['rild']['filtered_untrusted_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('rild','filtered_untrusted_app')
G.edge['rild']['filtered_untrusted_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','gad_untrusted_app')
G.edge['rild']['gad_untrusted_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('rild','gad_untrusted_app')
G.edge['rild']['gad_untrusted_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','irm_app')
G.edge['rild']['irm_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['irm_app']['fill'] = 'red'
G.add_edge('rild','irm_app')
G.edge['rild']['irm_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','knox_untrusted_app')
G.edge['rild']['knox_untrusted_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['rild']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('rild','knox_untrusted_app')
G.edge['rild']['knox_untrusted_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('rild','llk_untrusted_app')
G.edge['rild']['llk_untrusted_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('rild','llk_untrusted_app')
G.edge['rild']['llk_untrusted_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','netd')
G.edge['rild']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read]'
G.edge['rild']['netd']['fill'] = 'red'
G.add_edge('rild','netd')
G.edge['rild']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['rild']['rild']['fill'] = 'red'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['rild']['system_server']['fill'] = 'red'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('rild','trustonicpartner_app')
G.edge['rild']['trustonicpartner_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('rild','trustonicpartner_app')
G.edge['rild']['trustonicpartner_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','umcagent_app')
G.edge['rild']['umcagent_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['umcagent_app']['fill'] = 'red'
G.add_edge('rild','umcagent_app')
G.edge['rild']['umcagent_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','untrusted_app')
G.edge['rild']['untrusted_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['untrusted_app']['fill'] = 'red'
G.add_edge('rild','untrusted_app')
G.edge['rild']['untrusted_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','untrusteddomain')
G.edge['rild']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['rild']['untrusteddomain']['fill'] = 'red'
G.add_edge('rild','untrusteddomain')
G.edge['rild']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('rild','vpnclientd')
G.edge['rild']['vpnclientd']['write-read'] = '[write read][open open][write read]'
G.edge['rild']['vpnclientd']['fill'] = 'red'
G.add_edge('rild','vpnclientd')
G.edge['rild']['vpnclientd']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('rild','vpn_untrusted_app')
G.edge['rild']['vpn_untrusted_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('rild','vpn_untrusted_app')
G.edge['rild']['vpn_untrusted_app']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','appdomain')
G.edge['system_server']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open]'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('system_server','carrier_app')
G.edge['system_server']['carrier_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','charon')
G.edge['system_server']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','clatd')
G.edge['system_server']['clatd']['write-read'] = '[add_name search][setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('system_server','filtered_google_app')
G.edge['system_server']['filtered_google_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','filtered_untrusted_app')
G.edge['system_server']['filtered_untrusted_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','gad_untrusted_app')
G.edge['system_server']['gad_untrusted_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','irm_app')
G.edge['system_server']['irm_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','knox_untrusted_app')
G.edge['system_server']['knox_untrusted_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','llk_untrusted_app')
G.edge['system_server']['llk_untrusted_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][write read][write read][open open]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open]'
G.add_edge('system_server','trustonicpartner_app')
G.edge['system_server']['trustonicpartner_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','umcagent_app')
G.edge['system_server']['umcagent_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','untrusted_app')
G.edge['system_server']['untrusted_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','untrusteddomain')
G.edge['system_server']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','vpnclientd')
G.edge['system_server']['vpnclientd']['write-read'] = '[write read][open open]'
G.add_edge('system_server','vpn_untrusted_app')
G.edge['system_server']['vpn_untrusted_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','appdomain')
G.edge['system_server']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read]'
G.edge['system_server']['appdomain']['fill'] = 'red'
G.add_edge('system_server','appdomain')
G.edge['system_server']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read]'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read]'
G.edge['system_server']['bluetooth']['fill'] = 'red'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read]'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read]'
G.edge['system_server']['bluetooth']['fill'] = 'red'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read]'
G.add_edge('system_server','carrier_app')
G.edge['system_server']['carrier_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['carrier_app']['fill'] = 'red'
G.add_edge('system_server','carrier_app')
G.edge['system_server']['carrier_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','charon')
G.edge['system_server']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['charon']['fill'] = 'red'
G.add_edge('system_server','charon')
G.edge['system_server']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','clatd')
G.edge['system_server']['clatd']['write-read'] = '[add_name search][setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['system_server']['clatd']['fill'] = 'red'
G.add_edge('system_server','clatd')
G.edge['system_server']['clatd']['write-read'] = '[add_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('system_server','filtered_google_app')
G.edge['system_server']['filtered_google_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['filtered_google_app']['fill'] = 'red'
G.add_edge('system_server','filtered_google_app')
G.edge['system_server']['filtered_google_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','filtered_untrusted_app')
G.edge['system_server']['filtered_untrusted_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('system_server','filtered_untrusted_app')
G.edge['system_server']['filtered_untrusted_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','gad_untrusted_app')
G.edge['system_server']['gad_untrusted_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('system_server','gad_untrusted_app')
G.edge['system_server']['gad_untrusted_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','irm_app')
G.edge['system_server']['irm_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['irm_app']['fill'] = 'red'
G.add_edge('system_server','irm_app')
G.edge['system_server']['irm_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','knox_untrusted_app')
G.edge['system_server']['knox_untrusted_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['system_server']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('system_server','knox_untrusted_app')
G.edge['system_server']['knox_untrusted_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('system_server','llk_untrusted_app')
G.edge['system_server']['llk_untrusted_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('system_server','llk_untrusted_app')
G.edge['system_server']['llk_untrusted_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][write read][write read][open open][write read]'
G.edge['system_server']['netd']['fill'] = 'red'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][write read][write read][open open][write read][append read]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['system_server']['rild']['fill'] = 'red'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read]'
G.add_edge('system_server','trustonicpartner_app')
G.edge['system_server']['trustonicpartner_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('system_server','trustonicpartner_app')
G.edge['system_server']['trustonicpartner_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','umcagent_app')
G.edge['system_server']['umcagent_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['umcagent_app']['fill'] = 'red'
G.add_edge('system_server','umcagent_app')
G.edge['system_server']['umcagent_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','untrusted_app')
G.edge['system_server']['untrusted_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['untrusted_app']['fill'] = 'red'
G.add_edge('system_server','untrusted_app')
G.edge['system_server']['untrusted_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','untrusteddomain')
G.edge['system_server']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['system_server']['untrusteddomain']['fill'] = 'red'
G.add_edge('system_server','untrusteddomain')
G.edge['system_server']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('system_server','vpnclientd')
G.edge['system_server']['vpnclientd']['write-read'] = '[write read][open open][write read]'
G.edge['system_server']['vpnclientd']['fill'] = 'red'
G.add_edge('system_server','vpnclientd')
G.edge['system_server']['vpnclientd']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('system_server','vpn_untrusted_app')
G.edge['system_server']['vpn_untrusted_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('system_server','vpn_untrusted_app')
G.edge['system_server']['vpn_untrusted_app']['write-read'] = '[write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('trustonicpartner_app','appdomain')
G.edge['trustonicpartner_app']['appdomain']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','bluetooth')
G.edge['trustonicpartner_app']['bluetooth']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','bluetooth')
G.edge['trustonicpartner_app']['bluetooth']['write-read'] = '[open open][open open]'
G.add_edge('trustonicpartner_app','carrier_app')
G.edge['trustonicpartner_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('trustonicpartner_app','charon')
G.edge['trustonicpartner_app']['charon']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','clatd')
G.edge['trustonicpartner_app']['clatd']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','filtered_google_app')
G.edge['trustonicpartner_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('trustonicpartner_app','filtered_untrusted_app')
G.edge['trustonicpartner_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('trustonicpartner_app','gad_untrusted_app')
G.edge['trustonicpartner_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('trustonicpartner_app','irm_app')
G.edge['trustonicpartner_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('trustonicpartner_app','knox_untrusted_app')
G.edge['trustonicpartner_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('trustonicpartner_app','llk_untrusted_app')
G.edge['trustonicpartner_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('trustonicpartner_app','netd')
G.edge['trustonicpartner_app']['netd']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','rild')
G.edge['trustonicpartner_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('trustonicpartner_app','system_server')
G.edge['trustonicpartner_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('trustonicpartner_app','trustonicpartner_app')
G.edge['trustonicpartner_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('trustonicpartner_app','umcagent_app')
G.edge['trustonicpartner_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('trustonicpartner_app','untrusted_app')
G.edge['trustonicpartner_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('trustonicpartner_app','untrusteddomain')
G.edge['trustonicpartner_app']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','vpnclientd')
G.edge['trustonicpartner_app']['vpnclientd']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','vpn_untrusted_app')
G.edge['trustonicpartner_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('trustonicpartner_app','appdomain')
G.edge['trustonicpartner_app']['appdomain']['write-read'] = '[open open][write read]'
G.edge['trustonicpartner_app']['appdomain']['fill'] = 'red'
G.add_edge('trustonicpartner_app','appdomain')
G.edge['trustonicpartner_app']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('trustonicpartner_app','bluetooth')
G.edge['trustonicpartner_app']['bluetooth']['write-read'] = '[open open][open open][write read]'
G.edge['trustonicpartner_app']['bluetooth']['fill'] = 'red'
G.add_edge('trustonicpartner_app','bluetooth')
G.edge['trustonicpartner_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('trustonicpartner_app','bluetooth')
G.edge['trustonicpartner_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['trustonicpartner_app']['bluetooth']['fill'] = 'red'
G.add_edge('trustonicpartner_app','bluetooth')
G.edge['trustonicpartner_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('trustonicpartner_app','carrier_app')
G.edge['trustonicpartner_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['trustonicpartner_app']['carrier_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','carrier_app')
G.edge['trustonicpartner_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('trustonicpartner_app','charon')
G.edge['trustonicpartner_app']['charon']['write-read'] = '[open open][write read]'
G.edge['trustonicpartner_app']['charon']['fill'] = 'red'
G.add_edge('trustonicpartner_app','charon')
G.edge['trustonicpartner_app']['charon']['write-read'] = '[open open][write read][append read]'
G.add_edge('trustonicpartner_app','clatd')
G.edge['trustonicpartner_app']['clatd']['write-read'] = '[open open][write read]'
G.edge['trustonicpartner_app']['clatd']['fill'] = 'red'
G.add_edge('trustonicpartner_app','clatd')
G.edge['trustonicpartner_app']['clatd']['write-read'] = '[open open][write read][append read]'
G.add_edge('trustonicpartner_app','filtered_google_app')
G.edge['trustonicpartner_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['trustonicpartner_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','filtered_google_app')
G.edge['trustonicpartner_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('trustonicpartner_app','filtered_untrusted_app')
G.edge['trustonicpartner_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['trustonicpartner_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','filtered_untrusted_app')
G.edge['trustonicpartner_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('trustonicpartner_app','gad_untrusted_app')
G.edge['trustonicpartner_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['trustonicpartner_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','gad_untrusted_app')
G.edge['trustonicpartner_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('trustonicpartner_app','irm_app')
G.edge['trustonicpartner_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['trustonicpartner_app']['irm_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','irm_app')
G.edge['trustonicpartner_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('trustonicpartner_app','knox_untrusted_app')
G.edge['trustonicpartner_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['trustonicpartner_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','knox_untrusted_app')
G.edge['trustonicpartner_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('trustonicpartner_app','llk_untrusted_app')
G.edge['trustonicpartner_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['trustonicpartner_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','llk_untrusted_app')
G.edge['trustonicpartner_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('trustonicpartner_app','netd')
G.edge['trustonicpartner_app']['netd']['write-read'] = '[open open][write read]'
G.edge['trustonicpartner_app']['netd']['fill'] = 'red'
G.add_edge('trustonicpartner_app','netd')
G.edge['trustonicpartner_app']['netd']['write-read'] = '[open open][write read][append read]'
G.add_edge('trustonicpartner_app','rild')
G.edge['trustonicpartner_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['trustonicpartner_app']['rild']['fill'] = 'red'
G.add_edge('trustonicpartner_app','rild')
G.edge['trustonicpartner_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('trustonicpartner_app','system_server')
G.edge['trustonicpartner_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read]'
G.edge['trustonicpartner_app']['system_server']['fill'] = 'red'
G.add_edge('trustonicpartner_app','system_server')
G.edge['trustonicpartner_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read]'
G.add_edge('trustonicpartner_app','trustonicpartner_app')
G.edge['trustonicpartner_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['trustonicpartner_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','trustonicpartner_app')
G.edge['trustonicpartner_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('trustonicpartner_app','umcagent_app')
G.edge['trustonicpartner_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['trustonicpartner_app']['umcagent_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','umcagent_app')
G.edge['trustonicpartner_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('trustonicpartner_app','untrusted_app')
G.edge['trustonicpartner_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['trustonicpartner_app']['untrusted_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','untrusted_app')
G.edge['trustonicpartner_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('trustonicpartner_app','untrusteddomain')
G.edge['trustonicpartner_app']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['trustonicpartner_app']['untrusteddomain']['fill'] = 'red'
G.add_edge('trustonicpartner_app','untrusteddomain')
G.edge['trustonicpartner_app']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('trustonicpartner_app','vpnclientd')
G.edge['trustonicpartner_app']['vpnclientd']['write-read'] = '[open open][write read]'
G.edge['trustonicpartner_app']['vpnclientd']['fill'] = 'red'
G.add_edge('trustonicpartner_app','vpnclientd')
G.edge['trustonicpartner_app']['vpnclientd']['write-read'] = '[open open][write read][append read]'
G.add_edge('trustonicpartner_app','vpn_untrusted_app')
G.edge['trustonicpartner_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['trustonicpartner_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','vpn_untrusted_app')
G.edge['trustonicpartner_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('umcagent_app','appdomain')
G.edge['umcagent_app']['appdomain']['write-read'] = '[open open]'
G.add_edge('umcagent_app','bluetooth')
G.edge['umcagent_app']['bluetooth']['write-read'] = '[open open]'
G.add_edge('umcagent_app','bluetooth')
G.edge['umcagent_app']['bluetooth']['write-read'] = '[open open][open open]'
G.add_edge('umcagent_app','carrier_app')
G.edge['umcagent_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('umcagent_app','charon')
G.edge['umcagent_app']['charon']['write-read'] = '[open open]'
G.add_edge('umcagent_app','clatd')
G.edge['umcagent_app']['clatd']['write-read'] = '[open open]'
G.add_edge('umcagent_app','filtered_google_app')
G.edge['umcagent_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('umcagent_app','filtered_untrusted_app')
G.edge['umcagent_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('umcagent_app','gad_untrusted_app')
G.edge['umcagent_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('umcagent_app','irm_app')
G.edge['umcagent_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('umcagent_app','knox_untrusted_app')
G.edge['umcagent_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('umcagent_app','llk_untrusted_app')
G.edge['umcagent_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('umcagent_app','netd')
G.edge['umcagent_app']['netd']['write-read'] = '[open open]'
G.add_edge('umcagent_app','rild')
G.edge['umcagent_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('umcagent_app','system_server')
G.edge['umcagent_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('umcagent_app','trustonicpartner_app')
G.edge['umcagent_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('umcagent_app','umcagent_app')
G.edge['umcagent_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('umcagent_app','untrusted_app')
G.edge['umcagent_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('umcagent_app','untrusteddomain')
G.edge['umcagent_app']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('umcagent_app','vpnclientd')
G.edge['umcagent_app']['vpnclientd']['write-read'] = '[open open]'
G.add_edge('umcagent_app','vpn_untrusted_app')
G.edge['umcagent_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('umcagent_app','appdomain')
G.edge['umcagent_app']['appdomain']['write-read'] = '[open open][write read]'
G.edge['umcagent_app']['appdomain']['fill'] = 'red'
G.add_edge('umcagent_app','appdomain')
G.edge['umcagent_app']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('umcagent_app','bluetooth')
G.edge['umcagent_app']['bluetooth']['write-read'] = '[open open][open open][write read]'
G.edge['umcagent_app']['bluetooth']['fill'] = 'red'
G.add_edge('umcagent_app','bluetooth')
G.edge['umcagent_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('umcagent_app','bluetooth')
G.edge['umcagent_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['umcagent_app']['bluetooth']['fill'] = 'red'
G.add_edge('umcagent_app','bluetooth')
G.edge['umcagent_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('umcagent_app','carrier_app')
G.edge['umcagent_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['umcagent_app']['carrier_app']['fill'] = 'red'
G.add_edge('umcagent_app','carrier_app')
G.edge['umcagent_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('umcagent_app','charon')
G.edge['umcagent_app']['charon']['write-read'] = '[open open][write read]'
G.edge['umcagent_app']['charon']['fill'] = 'red'
G.add_edge('umcagent_app','charon')
G.edge['umcagent_app']['charon']['write-read'] = '[open open][write read][append read]'
G.add_edge('umcagent_app','clatd')
G.edge['umcagent_app']['clatd']['write-read'] = '[open open][write read]'
G.edge['umcagent_app']['clatd']['fill'] = 'red'
G.add_edge('umcagent_app','clatd')
G.edge['umcagent_app']['clatd']['write-read'] = '[open open][write read][append read]'
G.add_edge('umcagent_app','filtered_google_app')
G.edge['umcagent_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['umcagent_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('umcagent_app','filtered_google_app')
G.edge['umcagent_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('umcagent_app','filtered_untrusted_app')
G.edge['umcagent_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['umcagent_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('umcagent_app','filtered_untrusted_app')
G.edge['umcagent_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('umcagent_app','gad_untrusted_app')
G.edge['umcagent_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['umcagent_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('umcagent_app','gad_untrusted_app')
G.edge['umcagent_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('umcagent_app','irm_app')
G.edge['umcagent_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['umcagent_app']['irm_app']['fill'] = 'red'
G.add_edge('umcagent_app','irm_app')
G.edge['umcagent_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('umcagent_app','knox_untrusted_app')
G.edge['umcagent_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['umcagent_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('umcagent_app','knox_untrusted_app')
G.edge['umcagent_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('umcagent_app','llk_untrusted_app')
G.edge['umcagent_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['umcagent_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('umcagent_app','llk_untrusted_app')
G.edge['umcagent_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('umcagent_app','netd')
G.edge['umcagent_app']['netd']['write-read'] = '[open open][write read]'
G.edge['umcagent_app']['netd']['fill'] = 'red'
G.add_edge('umcagent_app','netd')
G.edge['umcagent_app']['netd']['write-read'] = '[open open][write read][append read]'
G.add_edge('umcagent_app','rild')
G.edge['umcagent_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['umcagent_app']['rild']['fill'] = 'red'
G.add_edge('umcagent_app','rild')
G.edge['umcagent_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('umcagent_app','system_server')
G.edge['umcagent_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read]'
G.edge['umcagent_app']['system_server']['fill'] = 'red'
G.add_edge('umcagent_app','system_server')
G.edge['umcagent_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read]'
G.add_edge('umcagent_app','trustonicpartner_app')
G.edge['umcagent_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['umcagent_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('umcagent_app','trustonicpartner_app')
G.edge['umcagent_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('umcagent_app','umcagent_app')
G.edge['umcagent_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['umcagent_app']['umcagent_app']['fill'] = 'red'
G.add_edge('umcagent_app','umcagent_app')
G.edge['umcagent_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('umcagent_app','untrusted_app')
G.edge['umcagent_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['umcagent_app']['untrusted_app']['fill'] = 'red'
G.add_edge('umcagent_app','untrusted_app')
G.edge['umcagent_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('umcagent_app','untrusteddomain')
G.edge['umcagent_app']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['umcagent_app']['untrusteddomain']['fill'] = 'red'
G.add_edge('umcagent_app','untrusteddomain')
G.edge['umcagent_app']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('umcagent_app','vpnclientd')
G.edge['umcagent_app']['vpnclientd']['write-read'] = '[open open][write read]'
G.edge['umcagent_app']['vpnclientd']['fill'] = 'red'
G.add_edge('umcagent_app','vpnclientd')
G.edge['umcagent_app']['vpnclientd']['write-read'] = '[open open][write read][append read]'
G.add_edge('umcagent_app','vpn_untrusted_app')
G.edge['umcagent_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['umcagent_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('umcagent_app','vpn_untrusted_app')
G.edge['umcagent_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('untrusted_app','appdomain')
G.edge['untrusted_app']['appdomain']['write-read'] = '[open open]'
G.add_edge('untrusted_app','bluetooth')
G.edge['untrusted_app']['bluetooth']['write-read'] = '[open open]'
G.add_edge('untrusted_app','bluetooth')
G.edge['untrusted_app']['bluetooth']['write-read'] = '[open open][open open]'
G.add_edge('untrusted_app','carrier_app')
G.edge['untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusted_app','charon')
G.edge['untrusted_app']['charon']['write-read'] = '[open open]'
G.add_edge('untrusted_app','clatd')
G.edge['untrusted_app']['clatd']['write-read'] = '[open open]'
G.add_edge('untrusted_app','filtered_google_app')
G.edge['untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusted_app','filtered_untrusted_app')
G.edge['untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusted_app','gad_untrusted_app')
G.edge['untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusted_app','irm_app')
G.edge['untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusted_app','knox_untrusted_app')
G.edge['untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusted_app','llk_untrusted_app')
G.edge['untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusted_app','netd')
G.edge['untrusted_app']['netd']['write-read'] = '[open open]'
G.add_edge('untrusted_app','rild')
G.edge['untrusted_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusted_app','system_server')
G.edge['untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('untrusted_app','trustonicpartner_app')
G.edge['untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusted_app','umcagent_app')
G.edge['untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusted_app','untrusted_app')
G.edge['untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusted_app','untrusteddomain')
G.edge['untrusted_app']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('untrusted_app','vpnclientd')
G.edge['untrusted_app']['vpnclientd']['write-read'] = '[open open]'
G.add_edge('untrusted_app','vpn_untrusted_app')
G.edge['untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusted_app','appdomain')
G.edge['untrusted_app']['appdomain']['write-read'] = '[open open][write read]'
G.edge['untrusted_app']['appdomain']['fill'] = 'red'
G.add_edge('untrusted_app','appdomain')
G.edge['untrusted_app']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrusted_app','bluetooth')
G.edge['untrusted_app']['bluetooth']['write-read'] = '[open open][open open][write read]'
G.edge['untrusted_app']['bluetooth']['fill'] = 'red'
G.add_edge('untrusted_app','bluetooth')
G.edge['untrusted_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('untrusted_app','bluetooth')
G.edge['untrusted_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['untrusted_app']['bluetooth']['fill'] = 'red'
G.add_edge('untrusted_app','bluetooth')
G.edge['untrusted_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('untrusted_app','carrier_app')
G.edge['untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['untrusted_app']['carrier_app']['fill'] = 'red'
G.add_edge('untrusted_app','carrier_app')
G.edge['untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('untrusted_app','charon')
G.edge['untrusted_app']['charon']['write-read'] = '[open open][write read]'
G.edge['untrusted_app']['charon']['fill'] = 'red'
G.add_edge('untrusted_app','charon')
G.edge['untrusted_app']['charon']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrusted_app','clatd')
G.edge['untrusted_app']['clatd']['write-read'] = '[open open][write read]'
G.edge['untrusted_app']['clatd']['fill'] = 'red'
G.add_edge('untrusted_app','clatd')
G.edge['untrusted_app']['clatd']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrusted_app','filtered_google_app')
G.edge['untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['untrusted_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('untrusted_app','filtered_google_app')
G.edge['untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('untrusted_app','filtered_untrusted_app')
G.edge['untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['untrusted_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('untrusted_app','filtered_untrusted_app')
G.edge['untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('untrusted_app','gad_untrusted_app')
G.edge['untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['untrusted_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('untrusted_app','gad_untrusted_app')
G.edge['untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('untrusted_app','irm_app')
G.edge['untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['untrusted_app']['irm_app']['fill'] = 'red'
G.add_edge('untrusted_app','irm_app')
G.edge['untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('untrusted_app','knox_untrusted_app')
G.edge['untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['untrusted_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('untrusted_app','knox_untrusted_app')
G.edge['untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('untrusted_app','llk_untrusted_app')
G.edge['untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['untrusted_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('untrusted_app','llk_untrusted_app')
G.edge['untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('untrusted_app','netd')
G.edge['untrusted_app']['netd']['write-read'] = '[open open][write read]'
G.edge['untrusted_app']['netd']['fill'] = 'red'
G.add_edge('untrusted_app','netd')
G.edge['untrusted_app']['netd']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrusted_app','rild')
G.edge['untrusted_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['untrusted_app']['rild']['fill'] = 'red'
G.add_edge('untrusted_app','rild')
G.edge['untrusted_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('untrusted_app','system_server')
G.edge['untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read]'
G.edge['untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('untrusted_app','system_server')
G.edge['untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read]'
G.add_edge('untrusted_app','trustonicpartner_app')
G.edge['untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['untrusted_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('untrusted_app','trustonicpartner_app')
G.edge['untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('untrusted_app','umcagent_app')
G.edge['untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['untrusted_app']['umcagent_app']['fill'] = 'red'
G.add_edge('untrusted_app','umcagent_app')
G.edge['untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('untrusted_app','untrusted_app')
G.edge['untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['untrusted_app']['untrusted_app']['fill'] = 'red'
G.add_edge('untrusted_app','untrusted_app')
G.edge['untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('untrusted_app','untrusteddomain')
G.edge['untrusted_app']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['untrusted_app']['untrusteddomain']['fill'] = 'red'
G.add_edge('untrusted_app','untrusteddomain')
G.edge['untrusted_app']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrusted_app','vpnclientd')
G.edge['untrusted_app']['vpnclientd']['write-read'] = '[open open][write read]'
G.edge['untrusted_app']['vpnclientd']['fill'] = 'red'
G.add_edge('untrusted_app','vpnclientd')
G.edge['untrusted_app']['vpnclientd']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrusted_app','vpn_untrusted_app')
G.edge['untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['untrusted_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('untrusted_app','vpn_untrusted_app')
G.edge['untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('untrusteddomain','appdomain')
G.edge['untrusteddomain']['appdomain']['write-read'] = '[open open][write read][append read][write read][write read][open open]'
G.add_edge('untrusteddomain','bluetooth')
G.edge['untrusteddomain']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusteddomain','bluetooth')
G.edge['untrusteddomain']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('untrusteddomain','carrier_app')
G.edge['untrusteddomain']['carrier_app']['write-read'] = '[write read][open open]'
G.add_edge('untrusteddomain','charon')
G.edge['untrusteddomain']['charon']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','clatd')
G.edge['untrusteddomain']['clatd']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','filtered_google_app')
G.edge['untrusteddomain']['filtered_google_app']['write-read'] = '[write read][open open]'
G.add_edge('untrusteddomain','filtered_untrusted_app')
G.edge['untrusteddomain']['filtered_untrusted_app']['write-read'] = '[write read][open open]'
G.add_edge('untrusteddomain','gad_untrusted_app')
G.edge['untrusteddomain']['gad_untrusted_app']['write-read'] = '[write read][open open]'
G.add_edge('untrusteddomain','irm_app')
G.edge['untrusteddomain']['irm_app']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][open open]'
G.add_edge('untrusteddomain','knox_untrusted_app')
G.edge['untrusteddomain']['knox_untrusted_app']['write-read'] = '[write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusteddomain','llk_untrusted_app')
G.edge['untrusteddomain']['llk_untrusted_app']['write-read'] = '[write read][open open]'
G.add_edge('untrusteddomain','netd')
G.edge['untrusteddomain']['netd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('untrusteddomain','rild')
G.edge['untrusteddomain']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open]'
G.add_edge('untrusteddomain','trustonicpartner_app')
G.edge['untrusteddomain']['trustonicpartner_app']['write-read'] = '[write read][open open]'
G.add_edge('untrusteddomain','umcagent_app')
G.edge['untrusteddomain']['umcagent_app']['write-read'] = '[write read][open open]'
G.add_edge('untrusteddomain','untrusted_app')
G.edge['untrusteddomain']['untrusted_app']['write-read'] = '[write read][open open]'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusteddomain','vpnclientd')
G.edge['untrusteddomain']['vpnclientd']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','vpn_untrusted_app')
G.edge['untrusteddomain']['vpn_untrusted_app']['write-read'] = '[write read][open open]'
G.add_edge('untrusteddomain','appdomain')
G.edge['untrusteddomain']['appdomain']['write-read'] = '[open open][write read][append read][write read][write read][open open][write read]'
G.edge['untrusteddomain']['appdomain']['fill'] = 'red'
G.add_edge('untrusteddomain','appdomain')
G.edge['untrusteddomain']['appdomain']['write-read'] = '[open open][write read][append read][write read][write read][open open][write read][append read]'
G.add_edge('untrusteddomain','bluetooth')
G.edge['untrusteddomain']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read]'
G.edge['untrusteddomain']['bluetooth']['fill'] = 'red'
G.add_edge('untrusteddomain','bluetooth')
G.edge['untrusteddomain']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read]'
G.add_edge('untrusteddomain','bluetooth')
G.edge['untrusteddomain']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read]'
G.edge['untrusteddomain']['bluetooth']['fill'] = 'red'
G.add_edge('untrusteddomain','bluetooth')
G.edge['untrusteddomain']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read]'
G.add_edge('untrusteddomain','carrier_app')
G.edge['untrusteddomain']['carrier_app']['write-read'] = '[write read][open open][write read]'
G.edge['untrusteddomain']['carrier_app']['fill'] = 'red'
G.add_edge('untrusteddomain','carrier_app')
G.edge['untrusteddomain']['carrier_app']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('untrusteddomain','charon')
G.edge['untrusteddomain']['charon']['write-read'] = '[open open][write read]'
G.edge['untrusteddomain']['charon']['fill'] = 'red'
G.add_edge('untrusteddomain','charon')
G.edge['untrusteddomain']['charon']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrusteddomain','clatd')
G.edge['untrusteddomain']['clatd']['write-read'] = '[open open][write read]'
G.edge['untrusteddomain']['clatd']['fill'] = 'red'
G.add_edge('untrusteddomain','clatd')
G.edge['untrusteddomain']['clatd']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrusteddomain','filtered_google_app')
G.edge['untrusteddomain']['filtered_google_app']['write-read'] = '[write read][open open][write read]'
G.edge['untrusteddomain']['filtered_google_app']['fill'] = 'red'
G.add_edge('untrusteddomain','filtered_google_app')
G.edge['untrusteddomain']['filtered_google_app']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('untrusteddomain','filtered_untrusted_app')
G.edge['untrusteddomain']['filtered_untrusted_app']['write-read'] = '[write read][open open][write read]'
G.edge['untrusteddomain']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('untrusteddomain','filtered_untrusted_app')
G.edge['untrusteddomain']['filtered_untrusted_app']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('untrusteddomain','gad_untrusted_app')
G.edge['untrusteddomain']['gad_untrusted_app']['write-read'] = '[write read][open open][write read]'
G.edge['untrusteddomain']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('untrusteddomain','gad_untrusted_app')
G.edge['untrusteddomain']['gad_untrusted_app']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('untrusteddomain','irm_app')
G.edge['untrusteddomain']['irm_app']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][open open][write read]'
G.edge['untrusteddomain']['irm_app']['fill'] = 'red'
G.add_edge('untrusteddomain','irm_app')
G.edge['untrusteddomain']['irm_app']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read]'
G.add_edge('untrusteddomain','knox_untrusted_app')
G.edge['untrusteddomain']['knox_untrusted_app']['write-read'] = '[write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['untrusteddomain']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('untrusteddomain','knox_untrusted_app')
G.edge['untrusteddomain']['knox_untrusted_app']['write-read'] = '[write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('untrusteddomain','llk_untrusted_app')
G.edge['untrusteddomain']['llk_untrusted_app']['write-read'] = '[write read][open open][write read]'
G.edge['untrusteddomain']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('untrusteddomain','llk_untrusted_app')
G.edge['untrusteddomain']['llk_untrusted_app']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('untrusteddomain','netd')
G.edge['untrusteddomain']['netd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['untrusteddomain']['netd']['fill'] = 'red'
G.add_edge('untrusteddomain','netd')
G.edge['untrusteddomain']['netd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('untrusteddomain','rild')
G.edge['untrusteddomain']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['untrusteddomain']['rild']['fill'] = 'red'
G.add_edge('untrusteddomain','rild')
G.edge['untrusteddomain']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read]'
G.edge['untrusteddomain']['system_server']['fill'] = 'red'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][append read]'
G.add_edge('untrusteddomain','trustonicpartner_app')
G.edge['untrusteddomain']['trustonicpartner_app']['write-read'] = '[write read][open open][write read]'
G.edge['untrusteddomain']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('untrusteddomain','trustonicpartner_app')
G.edge['untrusteddomain']['trustonicpartner_app']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('untrusteddomain','umcagent_app')
G.edge['untrusteddomain']['umcagent_app']['write-read'] = '[write read][open open][write read]'
G.edge['untrusteddomain']['umcagent_app']['fill'] = 'red'
G.add_edge('untrusteddomain','umcagent_app')
G.edge['untrusteddomain']['umcagent_app']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('untrusteddomain','untrusted_app')
G.edge['untrusteddomain']['untrusted_app']['write-read'] = '[write read][open open][write read]'
G.edge['untrusteddomain']['untrusted_app']['fill'] = 'red'
G.add_edge('untrusteddomain','untrusted_app')
G.edge['untrusteddomain']['untrusted_app']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['untrusteddomain']['untrusteddomain']['fill'] = 'red'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('untrusteddomain','vpnclientd')
G.edge['untrusteddomain']['vpnclientd']['write-read'] = '[open open][write read]'
G.edge['untrusteddomain']['vpnclientd']['fill'] = 'red'
G.add_edge('untrusteddomain','vpnclientd')
G.edge['untrusteddomain']['vpnclientd']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrusteddomain','vpn_untrusted_app')
G.edge['untrusteddomain']['vpn_untrusted_app']['write-read'] = '[write read][open open][write read]'
G.edge['untrusteddomain']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('untrusteddomain','vpn_untrusted_app')
G.edge['untrusteddomain']['vpn_untrusted_app']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('vpnclientd','appdomain')
G.edge['vpnclientd']['appdomain']['write-read'] = '[open open]'
G.add_edge('vpnclientd','bluetooth')
G.edge['vpnclientd']['bluetooth']['write-read'] = '[open open]'
G.add_edge('vpnclientd','bluetooth')
G.edge['vpnclientd']['bluetooth']['write-read'] = '[open open][open open]'
G.add_edge('vpnclientd','carrier_app')
G.edge['vpnclientd']['carrier_app']['write-read'] = '[open open]'
G.add_edge('vpnclientd','charon')
G.edge['vpnclientd']['charon']['write-read'] = '[open open]'
G.add_edge('vpnclientd','clatd')
G.edge['vpnclientd']['clatd']['write-read'] = '[open open]'
G.add_edge('vpnclientd','filtered_google_app')
G.edge['vpnclientd']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('vpnclientd','filtered_untrusted_app')
G.edge['vpnclientd']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('vpnclientd','gad_untrusted_app')
G.edge['vpnclientd']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('vpnclientd','irm_app')
G.edge['vpnclientd']['irm_app']['write-read'] = '[open open]'
G.add_edge('vpnclientd','knox_untrusted_app')
G.edge['vpnclientd']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('vpnclientd','llk_untrusted_app')
G.edge['vpnclientd']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('vpnclientd','netd')
G.edge['vpnclientd']['netd']['write-read'] = '[open open]'
G.add_edge('vpnclientd','rild')
G.edge['vpnclientd']['rild']['write-read'] = '[open open]'
G.add_edge('vpnclientd','system_server')
G.edge['vpnclientd']['system_server']['write-read'] = '[open open]'
G.add_edge('vpnclientd','trustonicpartner_app')
G.edge['vpnclientd']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('vpnclientd','umcagent_app')
G.edge['vpnclientd']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('vpnclientd','untrusted_app')
G.edge['vpnclientd']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('vpnclientd','untrusteddomain')
G.edge['vpnclientd']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('vpnclientd','vpnclientd')
G.edge['vpnclientd']['vpnclientd']['write-read'] = '[add_name search][write read][open open][write read][append read][open open]'
G.add_edge('vpnclientd','vpn_untrusted_app')
G.edge['vpnclientd']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('vpnclientd','appdomain')
G.edge['vpnclientd']['appdomain']['write-read'] = '[open open][write read]'
G.edge['vpnclientd']['appdomain']['fill'] = 'red'
G.add_edge('vpnclientd','appdomain')
G.edge['vpnclientd']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('vpnclientd','bluetooth')
G.edge['vpnclientd']['bluetooth']['write-read'] = '[open open][open open][write read]'
G.edge['vpnclientd']['bluetooth']['fill'] = 'red'
G.add_edge('vpnclientd','bluetooth')
G.edge['vpnclientd']['bluetooth']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('vpnclientd','bluetooth')
G.edge['vpnclientd']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['vpnclientd']['bluetooth']['fill'] = 'red'
G.add_edge('vpnclientd','bluetooth')
G.edge['vpnclientd']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('vpnclientd','carrier_app')
G.edge['vpnclientd']['carrier_app']['write-read'] = '[open open][write read]'
G.edge['vpnclientd']['carrier_app']['fill'] = 'red'
G.add_edge('vpnclientd','carrier_app')
G.edge['vpnclientd']['carrier_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('vpnclientd','charon')
G.edge['vpnclientd']['charon']['write-read'] = '[open open][write read]'
G.edge['vpnclientd']['charon']['fill'] = 'red'
G.add_edge('vpnclientd','charon')
G.edge['vpnclientd']['charon']['write-read'] = '[open open][write read][append read]'
G.add_edge('vpnclientd','clatd')
G.edge['vpnclientd']['clatd']['write-read'] = '[open open][write read]'
G.edge['vpnclientd']['clatd']['fill'] = 'red'
G.add_edge('vpnclientd','clatd')
G.edge['vpnclientd']['clatd']['write-read'] = '[open open][write read][append read]'
G.add_edge('vpnclientd','filtered_google_app')
G.edge['vpnclientd']['filtered_google_app']['write-read'] = '[open open][write read]'
G.edge['vpnclientd']['filtered_google_app']['fill'] = 'red'
G.add_edge('vpnclientd','filtered_google_app')
G.edge['vpnclientd']['filtered_google_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('vpnclientd','filtered_untrusted_app')
G.edge['vpnclientd']['filtered_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['vpnclientd']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('vpnclientd','filtered_untrusted_app')
G.edge['vpnclientd']['filtered_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('vpnclientd','gad_untrusted_app')
G.edge['vpnclientd']['gad_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['vpnclientd']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('vpnclientd','gad_untrusted_app')
G.edge['vpnclientd']['gad_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('vpnclientd','irm_app')
G.edge['vpnclientd']['irm_app']['write-read'] = '[open open][write read]'
G.edge['vpnclientd']['irm_app']['fill'] = 'red'
G.add_edge('vpnclientd','irm_app')
G.edge['vpnclientd']['irm_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('vpnclientd','knox_untrusted_app')
G.edge['vpnclientd']['knox_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['vpnclientd']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('vpnclientd','knox_untrusted_app')
G.edge['vpnclientd']['knox_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('vpnclientd','llk_untrusted_app')
G.edge['vpnclientd']['llk_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['vpnclientd']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('vpnclientd','llk_untrusted_app')
G.edge['vpnclientd']['llk_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('vpnclientd','netd')
G.edge['vpnclientd']['netd']['write-read'] = '[open open][write read]'
G.edge['vpnclientd']['netd']['fill'] = 'red'
G.add_edge('vpnclientd','netd')
G.edge['vpnclientd']['netd']['write-read'] = '[open open][write read][append read]'
G.add_edge('vpnclientd','rild')
G.edge['vpnclientd']['rild']['write-read'] = '[open open][write read]'
G.edge['vpnclientd']['rild']['fill'] = 'red'
G.add_edge('vpnclientd','rild')
G.edge['vpnclientd']['rild']['write-read'] = '[open open][write read][append read]'
G.add_edge('vpnclientd','system_server')
G.edge['vpnclientd']['system_server']['write-read'] = '[open open][write read]'
G.edge['vpnclientd']['system_server']['fill'] = 'red'
G.add_edge('vpnclientd','system_server')
G.edge['vpnclientd']['system_server']['write-read'] = '[open open][write read][append read]'
G.add_edge('vpnclientd','trustonicpartner_app')
G.edge['vpnclientd']['trustonicpartner_app']['write-read'] = '[open open][write read]'
G.edge['vpnclientd']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('vpnclientd','trustonicpartner_app')
G.edge['vpnclientd']['trustonicpartner_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('vpnclientd','umcagent_app')
G.edge['vpnclientd']['umcagent_app']['write-read'] = '[open open][write read]'
G.edge['vpnclientd']['umcagent_app']['fill'] = 'red'
G.add_edge('vpnclientd','umcagent_app')
G.edge['vpnclientd']['umcagent_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('vpnclientd','untrusted_app')
G.edge['vpnclientd']['untrusted_app']['write-read'] = '[open open][write read]'
G.edge['vpnclientd']['untrusted_app']['fill'] = 'red'
G.add_edge('vpnclientd','untrusted_app')
G.edge['vpnclientd']['untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('vpnclientd','untrusteddomain')
G.edge['vpnclientd']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['vpnclientd']['untrusteddomain']['fill'] = 'red'
G.add_edge('vpnclientd','untrusteddomain')
G.edge['vpnclientd']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('vpnclientd','vpnclientd')
G.edge['vpnclientd']['vpnclientd']['write-read'] = '[add_name search][write read][open open][write read][append read][open open][write read]'
G.edge['vpnclientd']['vpnclientd']['fill'] = 'red'
G.add_edge('vpnclientd','vpnclientd')
G.edge['vpnclientd']['vpnclientd']['write-read'] = '[add_name search][write read][open open][write read][append read][open open][write read][append read]'
G.add_edge('vpnclientd','vpn_untrusted_app')
G.edge['vpnclientd']['vpn_untrusted_app']['write-read'] = '[open open][write read]'
G.edge['vpnclientd']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('vpnclientd','vpn_untrusted_app')
G.edge['vpnclientd']['vpn_untrusted_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('vpn_untrusted_app','appdomain')
G.edge['vpn_untrusted_app']['appdomain']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','bluetooth')
G.edge['vpn_untrusted_app']['bluetooth']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','bluetooth')
G.edge['vpn_untrusted_app']['bluetooth']['write-read'] = '[open open][open open]'
G.add_edge('vpn_untrusted_app','carrier_app')
G.edge['vpn_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vpn_untrusted_app','charon')
G.edge['vpn_untrusted_app']['charon']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','clatd')
G.edge['vpn_untrusted_app']['clatd']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','filtered_google_app')
G.edge['vpn_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vpn_untrusted_app','filtered_untrusted_app')
G.edge['vpn_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vpn_untrusted_app','gad_untrusted_app')
G.edge['vpn_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vpn_untrusted_app','irm_app')
G.edge['vpn_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vpn_untrusted_app','knox_untrusted_app')
G.edge['vpn_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vpn_untrusted_app','llk_untrusted_app')
G.edge['vpn_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vpn_untrusted_app','netd')
G.edge['vpn_untrusted_app']['netd']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','rild')
G.edge['vpn_untrusted_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vpn_untrusted_app','system_server')
G.edge['vpn_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('vpn_untrusted_app','trustonicpartner_app')
G.edge['vpn_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vpn_untrusted_app','umcagent_app')
G.edge['vpn_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vpn_untrusted_app','untrusted_app')
G.edge['vpn_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vpn_untrusted_app','untrusteddomain')
G.edge['vpn_untrusted_app']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','vpnclientd')
G.edge['vpn_untrusted_app']['vpnclientd']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','vpn_untrusted_app')
G.edge['vpn_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vpn_untrusted_app','appdomain')
G.edge['vpn_untrusted_app']['appdomain']['write-read'] = '[open open][write read]'
G.edge['vpn_untrusted_app']['appdomain']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','appdomain')
G.edge['vpn_untrusted_app']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('vpn_untrusted_app','bluetooth')
G.edge['vpn_untrusted_app']['bluetooth']['write-read'] = '[open open][open open][write read]'
G.edge['vpn_untrusted_app']['bluetooth']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','bluetooth')
G.edge['vpn_untrusted_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('vpn_untrusted_app','bluetooth')
G.edge['vpn_untrusted_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['vpn_untrusted_app']['bluetooth']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','bluetooth')
G.edge['vpn_untrusted_app']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('vpn_untrusted_app','carrier_app')
G.edge['vpn_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['vpn_untrusted_app']['carrier_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','carrier_app')
G.edge['vpn_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('vpn_untrusted_app','charon')
G.edge['vpn_untrusted_app']['charon']['write-read'] = '[open open][write read]'
G.edge['vpn_untrusted_app']['charon']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','charon')
G.edge['vpn_untrusted_app']['charon']['write-read'] = '[open open][write read][append read]'
G.add_edge('vpn_untrusted_app','clatd')
G.edge['vpn_untrusted_app']['clatd']['write-read'] = '[open open][write read]'
G.edge['vpn_untrusted_app']['clatd']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','clatd')
G.edge['vpn_untrusted_app']['clatd']['write-read'] = '[open open][write read][append read]'
G.add_edge('vpn_untrusted_app','filtered_google_app')
G.edge['vpn_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['vpn_untrusted_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','filtered_google_app')
G.edge['vpn_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('vpn_untrusted_app','filtered_untrusted_app')
G.edge['vpn_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['vpn_untrusted_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','filtered_untrusted_app')
G.edge['vpn_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('vpn_untrusted_app','gad_untrusted_app')
G.edge['vpn_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['vpn_untrusted_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','gad_untrusted_app')
G.edge['vpn_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('vpn_untrusted_app','irm_app')
G.edge['vpn_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['vpn_untrusted_app']['irm_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','irm_app')
G.edge['vpn_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('vpn_untrusted_app','knox_untrusted_app')
G.edge['vpn_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['vpn_untrusted_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','knox_untrusted_app')
G.edge['vpn_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('vpn_untrusted_app','llk_untrusted_app')
G.edge['vpn_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['vpn_untrusted_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','llk_untrusted_app')
G.edge['vpn_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('vpn_untrusted_app','netd')
G.edge['vpn_untrusted_app']['netd']['write-read'] = '[open open][write read]'
G.edge['vpn_untrusted_app']['netd']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','netd')
G.edge['vpn_untrusted_app']['netd']['write-read'] = '[open open][write read][append read]'
G.add_edge('vpn_untrusted_app','rild')
G.edge['vpn_untrusted_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vpn_untrusted_app']['rild']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','rild')
G.edge['vpn_untrusted_app']['rild']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vpn_untrusted_app','system_server')
G.edge['vpn_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read]'
G.edge['vpn_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','system_server')
G.edge['vpn_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read]'
G.add_edge('vpn_untrusted_app','trustonicpartner_app')
G.edge['vpn_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['vpn_untrusted_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','trustonicpartner_app')
G.edge['vpn_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('vpn_untrusted_app','umcagent_app')
G.edge['vpn_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['vpn_untrusted_app']['umcagent_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','umcagent_app')
G.edge['vpn_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('vpn_untrusted_app','untrusted_app')
G.edge['vpn_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['vpn_untrusted_app']['untrusted_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','untrusted_app')
G.edge['vpn_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('vpn_untrusted_app','untrusteddomain')
G.edge['vpn_untrusted_app']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['vpn_untrusted_app']['untrusteddomain']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','untrusteddomain')
G.edge['vpn_untrusted_app']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('vpn_untrusted_app','vpnclientd')
G.edge['vpn_untrusted_app']['vpnclientd']['write-read'] = '[open open][write read]'
G.edge['vpn_untrusted_app']['vpnclientd']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','vpnclientd')
G.edge['vpn_untrusted_app']['vpnclientd']['write-read'] = '[open open][write read][append read]'
G.add_edge('vpn_untrusted_app','vpn_untrusted_app')
G.edge['vpn_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['vpn_untrusted_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','vpn_untrusted_app')
G.edge['vpn_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()