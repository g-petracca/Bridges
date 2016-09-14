import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('appdomain','debuggerd')
G.edge['appdomain']['debuggerd']['write-read'] = '[open open]'
G.add_edge('appdomain','epmd')
G.edge['appdomain']['epmd']['write-read'] = '[open open]'
G.add_edge('appdomain','ime_app')
G.edge['appdomain']['ime_app']['write-read'] = '[open open]'
G.add_edge('appdomain','knox_system_app')
G.edge['appdomain']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('appdomain','location_app')
G.edge['appdomain']['location_app']['write-read'] = '[open open]'
G.add_edge('appdomain','mediaserver')
G.edge['appdomain']['mediaserver']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('appdomain','mediaserver')
G.edge['appdomain']['mediaserver']['write-read'] = '[open open][write read][append read][open open][open open]'
G.add_edge('appdomain','rild')
G.edge['appdomain']['rild']['write-read'] = '[open open]'
G.add_edge('appdomain','s_system_app')
G.edge['appdomain']['s_system_app']['write-read'] = '[setattr getattr][open open]'
G.add_edge('appdomain','syscope_app')
G.edge['appdomain']['syscope_app']['write-read'] = '[open open]'
G.add_edge('appdomain','system_app')
G.edge['appdomain']['system_app']['write-read'] = '[setattr getattr][open open]'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][open open]'
G.add_edge('appdomain','debuggerd')
G.edge['appdomain']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('appdomain','epmd')
G.edge['appdomain']['epmd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('appdomain','ime_app')
G.edge['appdomain']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('appdomain','installd')
G.edge['appdomain']['installd']['write-read'] = '[setattr getattr][setattr getattr][add_name search][remove_name search][setattr getattr]'
G.add_edge('appdomain','knox_system_app')
G.edge['appdomain']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('appdomain','location_app')
G.edge['appdomain']['location_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('appdomain','mediaserver')
G.edge['appdomain']['mediaserver']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr]'
G.add_edge('appdomain','radio')
G.edge['appdomain']['radio']['write-read'] = '[setattr getattr]'
G.add_edge('appdomain','rild')
G.edge['appdomain']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('appdomain','s_system_app')
G.edge['appdomain']['s_system_app']['write-read'] = '[setattr getattr][open open][setattr getattr]'
G.add_edge('appdomain','syscope_app')
G.edge['appdomain']['syscope_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('appdomain','system_app')
G.edge['appdomain']['system_app']['write-read'] = '[setattr getattr][open open][setattr getattr]'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('appdomain','carrier_app')
G.edge['appdomain']['carrier_app']['write-read'] = '[write read]'
G.edge['appdomain']['carrier_app']['fill'] = 'red'
G.add_edge('appdomain','debuggerd')
G.edge['appdomain']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['appdomain']['debuggerd']['fill'] = 'red'
G.add_edge('appdomain','debuggerd')
G.edge['appdomain']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('appdomain','epmd')
G.edge['appdomain']['epmd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['appdomain']['epmd']['fill'] = 'red'
G.add_edge('appdomain','epmd')
G.edge['appdomain']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('appdomain','filtered_google_app')
G.edge['appdomain']['filtered_google_app']['write-read'] = '[write read]'
G.edge['appdomain']['filtered_google_app']['fill'] = 'red'
G.add_edge('appdomain','filtered_untrusted_app')
G.edge['appdomain']['filtered_untrusted_app']['write-read'] = '[write read]'
G.edge['appdomain']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('appdomain','gad_untrusted_app')
G.edge['appdomain']['gad_untrusted_app']['write-read'] = '[write read]'
G.edge['appdomain']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('appdomain','ime_app')
G.edge['appdomain']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['appdomain']['ime_app']['fill'] = 'red'
G.add_edge('appdomain','ime_app')
G.edge['appdomain']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('appdomain','irm_app')
G.edge['appdomain']['irm_app']['write-read'] = '[write read]'
G.edge['appdomain']['irm_app']['fill'] = 'red'
G.add_edge('appdomain','knox_system_app')
G.edge['appdomain']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['appdomain']['knox_system_app']['fill'] = 'red'
G.add_edge('appdomain','knox_system_app')
G.edge['appdomain']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('appdomain','knox_untrusted_app')
G.edge['appdomain']['knox_untrusted_app']['write-read'] = '[write read]'
G.edge['appdomain']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('appdomain','llk_untrusted_app')
G.edge['appdomain']['llk_untrusted_app']['write-read'] = '[write read]'
G.edge['appdomain']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('appdomain','location_app')
G.edge['appdomain']['location_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['appdomain']['location_app']['fill'] = 'red'
G.add_edge('appdomain','location_app')
G.edge['appdomain']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('appdomain','mediaserver')
G.edge['appdomain']['mediaserver']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['appdomain']['mediaserver']['fill'] = 'red'
G.add_edge('appdomain','mediaserver')
G.edge['appdomain']['mediaserver']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('appdomain','mediaserver')
G.edge['appdomain']['mediaserver']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['appdomain']['mediaserver']['fill'] = 'red'
G.add_edge('appdomain','mediaserver')
G.edge['appdomain']['mediaserver']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('appdomain','platformappdomain')
G.edge['appdomain']['platformappdomain']['write-read'] = '[write read]'
G.edge['appdomain']['platformappdomain']['fill'] = 'red'
G.add_edge('appdomain','rild')
G.edge['appdomain']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['appdomain']['rild']['fill'] = 'red'
G.add_edge('appdomain','rild')
G.edge['appdomain']['rild']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('appdomain','s_system_app')
G.edge['appdomain']['s_system_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read]'
G.edge['appdomain']['s_system_app']['fill'] = 'red'
G.add_edge('appdomain','s_system_app')
G.edge['appdomain']['s_system_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][append read]'
G.add_edge('appdomain','syscope_app')
G.edge['appdomain']['syscope_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['appdomain']['syscope_app']['fill'] = 'red'
G.add_edge('appdomain','syscope_app')
G.edge['appdomain']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('appdomain','system_app')
G.edge['appdomain']['system_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read]'
G.edge['appdomain']['system_app']['fill'] = 'red'
G.add_edge('appdomain','system_app')
G.edge['appdomain']['system_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][append read]'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['appdomain']['system_server']['fill'] = 'red'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][write read]'
G.edge['appdomain']['system_server']['fill'] = 'red'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read]'
G.add_edge('appdomain','trustonicpartner_app')
G.edge['appdomain']['trustonicpartner_app']['write-read'] = '[write read]'
G.edge['appdomain']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('appdomain','umcagent_app')
G.edge['appdomain']['umcagent_app']['write-read'] = '[write read]'
G.edge['appdomain']['umcagent_app']['fill'] = 'red'
G.add_edge('appdomain','untrusted_app')
G.edge['appdomain']['untrusted_app']['write-read'] = '[write read]'
G.edge['appdomain']['untrusted_app']['fill'] = 'red'
G.add_edge('appdomain','vpn_untrusted_app')
G.edge['appdomain']['vpn_untrusted_app']['write-read'] = '[write read]'
G.edge['appdomain']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('carrier_app','debuggerd')
G.edge['carrier_app']['debuggerd']['write-read'] = '[setattr getattr]'
G.add_edge('carrier_app','epmd')
G.edge['carrier_app']['epmd']['write-read'] = '[setattr getattr]'
G.add_edge('carrier_app','ime_app')
G.edge['carrier_app']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','installd')
G.edge['carrier_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('carrier_app','knox_system_app')
G.edge['carrier_app']['knox_system_app']['write-read'] = '[setattr getattr]'
G.add_edge('carrier_app','location_app')
G.edge['carrier_app']['location_app']['write-read'] = '[setattr getattr]'
G.add_edge('carrier_app','mediaserver')
G.edge['carrier_app']['mediaserver']['write-read'] = '[setattr getattr]'
G.add_edge('carrier_app','radio')
G.edge['carrier_app']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','rild')
G.edge['carrier_app']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('carrier_app','s_system_app')
G.edge['carrier_app']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','syscope_app')
G.edge['carrier_app']['syscope_app']['write-read'] = '[setattr getattr]'
G.add_edge('carrier_app','system_app')
G.edge['carrier_app']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','system_server')
G.edge['carrier_app']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('carrier_app','carrier_app')
G.edge['carrier_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['carrier_app']['carrier_app']['fill'] = 'red'
G.add_edge('carrier_app','debuggerd')
G.edge['carrier_app']['debuggerd']['write-read'] = '[setattr getattr][write read]'
G.edge['carrier_app']['debuggerd']['fill'] = 'red'
G.add_edge('carrier_app','debuggerd')
G.edge['carrier_app']['debuggerd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('carrier_app','epmd')
G.edge['carrier_app']['epmd']['write-read'] = '[setattr getattr][write read]'
G.edge['carrier_app']['epmd']['fill'] = 'red'
G.add_edge('carrier_app','epmd')
G.edge['carrier_app']['epmd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('carrier_app','filtered_google_app')
G.edge['carrier_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['carrier_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('carrier_app','filtered_untrusted_app')
G.edge['carrier_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['carrier_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('carrier_app','gad_untrusted_app')
G.edge['carrier_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['carrier_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('carrier_app','ime_app')
G.edge['carrier_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['carrier_app']['ime_app']['fill'] = 'red'
G.add_edge('carrier_app','ime_app')
G.edge['carrier_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','irm_app')
G.edge['carrier_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['carrier_app']['irm_app']['fill'] = 'red'
G.add_edge('carrier_app','knox_system_app')
G.edge['carrier_app']['knox_system_app']['write-read'] = '[setattr getattr][write read]'
G.edge['carrier_app']['knox_system_app']['fill'] = 'red'
G.add_edge('carrier_app','knox_system_app')
G.edge['carrier_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('carrier_app','knox_untrusted_app')
G.edge['carrier_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['carrier_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('carrier_app','llk_untrusted_app')
G.edge['carrier_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['carrier_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('carrier_app','location_app')
G.edge['carrier_app']['location_app']['write-read'] = '[setattr getattr][write read]'
G.edge['carrier_app']['location_app']['fill'] = 'red'
G.add_edge('carrier_app','location_app')
G.edge['carrier_app']['location_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('carrier_app','mediaserver')
G.edge['carrier_app']['mediaserver']['write-read'] = '[setattr getattr][write read]'
G.edge['carrier_app']['mediaserver']['fill'] = 'red'
G.add_edge('carrier_app','mediaserver')
G.edge['carrier_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('carrier_app','mediaserver')
G.edge['carrier_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read]'
G.edge['carrier_app']['mediaserver']['fill'] = 'red'
G.add_edge('carrier_app','mediaserver')
G.edge['carrier_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read]'
G.add_edge('carrier_app','platformappdomain')
G.edge['carrier_app']['platformappdomain']['write-read'] = '[write read]'
G.edge['carrier_app']['platformappdomain']['fill'] = 'red'
G.add_edge('carrier_app','rild')
G.edge['carrier_app']['rild']['write-read'] = '[setattr getattr][write read]'
G.edge['carrier_app']['rild']['fill'] = 'red'
G.add_edge('carrier_app','rild')
G.edge['carrier_app']['rild']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('carrier_app','s_system_app')
G.edge['carrier_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['carrier_app']['s_system_app']['fill'] = 'red'
G.add_edge('carrier_app','s_system_app')
G.edge['carrier_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','syscope_app')
G.edge['carrier_app']['syscope_app']['write-read'] = '[setattr getattr][write read]'
G.edge['carrier_app']['syscope_app']['fill'] = 'red'
G.add_edge('carrier_app','syscope_app')
G.edge['carrier_app']['syscope_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('carrier_app','system_app')
G.edge['carrier_app']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['carrier_app']['system_app']['fill'] = 'red'
G.add_edge('carrier_app','system_app')
G.edge['carrier_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','system_server')
G.edge['carrier_app']['system_server']['write-read'] = '[setattr getattr][write read]'
G.edge['carrier_app']['system_server']['fill'] = 'red'
G.add_edge('carrier_app','system_server')
G.edge['carrier_app']['system_server']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['carrier_app']['system_server']['fill'] = 'red'
G.add_edge('carrier_app','system_server')
G.edge['carrier_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read]'
G.add_edge('carrier_app','trustonicpartner_app')
G.edge['carrier_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['carrier_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('carrier_app','umcagent_app')
G.edge['carrier_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['carrier_app']['umcagent_app']['fill'] = 'red'
G.add_edge('carrier_app','untrusted_app')
G.edge['carrier_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['carrier_app']['untrusted_app']['fill'] = 'red'
G.add_edge('carrier_app','vpn_untrusted_app')
G.edge['carrier_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['carrier_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('epmd','debuggerd')
G.edge['epmd']['debuggerd']['write-read'] = '[open open]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('epmd','ime_app')
G.edge['epmd']['ime_app']['write-read'] = '[open open]'
G.add_edge('epmd','knox_system_app')
G.edge['epmd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('epmd','location_app')
G.edge['epmd']['location_app']['write-read'] = '[open open]'
G.add_edge('epmd','mediaserver')
G.edge['epmd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('epmd','mediaserver')
G.edge['epmd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('epmd','rild')
G.edge['epmd']['rild']['write-read'] = '[open open]'
G.add_edge('epmd','s_system_app')
G.edge['epmd']['s_system_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][append read][open open]'
G.add_edge('epmd','syscope_app')
G.edge['epmd']['syscope_app']['write-read'] = '[open open]'
G.add_edge('epmd','system_app')
G.edge['epmd']['system_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][append read][open open]'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open]'
G.add_edge('epmd','debuggerd')
G.edge['epmd']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('epmd','ime_app')
G.edge['epmd']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('epmd','installd')
G.edge['epmd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('epmd','knox_system_app')
G.edge['epmd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('epmd','location_app')
G.edge['epmd']['location_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('epmd','mediaserver')
G.edge['epmd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('epmd','radio')
G.edge['epmd']['radio']['write-read'] = '[setattr getattr]'
G.add_edge('epmd','rild')
G.edge['epmd']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('epmd','s_system_app')
G.edge['epmd']['s_system_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('epmd','syscope_app')
G.edge['epmd']['syscope_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('epmd','system_app')
G.edge['epmd']['system_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('epmd','carrier_app')
G.edge['epmd']['carrier_app']['write-read'] = '[write read]'
G.edge['epmd']['carrier_app']['fill'] = 'red'
G.add_edge('epmd','debuggerd')
G.edge['epmd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['epmd']['debuggerd']['fill'] = 'red'
G.add_edge('epmd','debuggerd')
G.edge['epmd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['epmd']['epmd']['fill'] = 'red'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('epmd','filtered_google_app')
G.edge['epmd']['filtered_google_app']['write-read'] = '[write read]'
G.edge['epmd']['filtered_google_app']['fill'] = 'red'
G.add_edge('epmd','filtered_untrusted_app')
G.edge['epmd']['filtered_untrusted_app']['write-read'] = '[write read]'
G.edge['epmd']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('epmd','gad_untrusted_app')
G.edge['epmd']['gad_untrusted_app']['write-read'] = '[write read]'
G.edge['epmd']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('epmd','ime_app')
G.edge['epmd']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['epmd']['ime_app']['fill'] = 'red'
G.add_edge('epmd','ime_app')
G.edge['epmd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('epmd','irm_app')
G.edge['epmd']['irm_app']['write-read'] = '[write read]'
G.edge['epmd']['irm_app']['fill'] = 'red'
G.add_edge('epmd','knox_system_app')
G.edge['epmd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['epmd']['knox_system_app']['fill'] = 'red'
G.add_edge('epmd','knox_system_app')
G.edge['epmd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('epmd','knox_untrusted_app')
G.edge['epmd']['knox_untrusted_app']['write-read'] = '[write read]'
G.edge['epmd']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('epmd','llk_untrusted_app')
G.edge['epmd']['llk_untrusted_app']['write-read'] = '[write read]'
G.edge['epmd']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('epmd','location_app')
G.edge['epmd']['location_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['epmd']['location_app']['fill'] = 'red'
G.add_edge('epmd','location_app')
G.edge['epmd']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('epmd','mediaserver')
G.edge['epmd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['epmd']['mediaserver']['fill'] = 'red'
G.add_edge('epmd','mediaserver')
G.edge['epmd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read]'
G.add_edge('epmd','mediaserver')
G.edge['epmd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['epmd']['mediaserver']['fill'] = 'red'
G.add_edge('epmd','mediaserver')
G.edge['epmd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('epmd','platformappdomain')
G.edge['epmd']['platformappdomain']['write-read'] = '[write read]'
G.edge['epmd']['platformappdomain']['fill'] = 'red'
G.add_edge('epmd','rild')
G.edge['epmd']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['epmd']['rild']['fill'] = 'red'
G.add_edge('epmd','rild')
G.edge['epmd']['rild']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('epmd','s_system_app')
G.edge['epmd']['s_system_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['epmd']['s_system_app']['fill'] = 'red'
G.add_edge('epmd','s_system_app')
G.edge['epmd']['s_system_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('epmd','syscope_app')
G.edge['epmd']['syscope_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['epmd']['syscope_app']['fill'] = 'red'
G.add_edge('epmd','syscope_app')
G.edge['epmd']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('epmd','system_app')
G.edge['epmd']['system_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['epmd']['system_app']['fill'] = 'red'
G.add_edge('epmd','system_app')
G.edge['epmd']['system_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['epmd']['system_server']['fill'] = 'red'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read]'
G.edge['epmd']['system_server']['fill'] = 'red'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read]'
G.add_edge('epmd','trustonicpartner_app')
G.edge['epmd']['trustonicpartner_app']['write-read'] = '[write read]'
G.edge['epmd']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('epmd','umcagent_app')
G.edge['epmd']['umcagent_app']['write-read'] = '[write read]'
G.edge['epmd']['umcagent_app']['fill'] = 'red'
G.add_edge('epmd','untrusted_app')
G.edge['epmd']['untrusted_app']['write-read'] = '[write read]'
G.edge['epmd']['untrusted_app']['fill'] = 'red'
G.add_edge('epmd','vpn_untrusted_app')
G.edge['epmd']['vpn_untrusted_app']['write-read'] = '[write read]'
G.edge['epmd']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom]'
G.add_edge('epmd','installd')
G.edge['epmd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr][relabelto relabelfrom]'
G.add_edge('filtered_google_app','debuggerd')
G.edge['filtered_google_app']['debuggerd']['write-read'] = '[setattr getattr]'
G.add_edge('filtered_google_app','epmd')
G.edge['filtered_google_app']['epmd']['write-read'] = '[setattr getattr]'
G.add_edge('filtered_google_app','ime_app')
G.edge['filtered_google_app']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','installd')
G.edge['filtered_google_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('filtered_google_app','knox_system_app')
G.edge['filtered_google_app']['knox_system_app']['write-read'] = '[setattr getattr]'
G.add_edge('filtered_google_app','location_app')
G.edge['filtered_google_app']['location_app']['write-read'] = '[setattr getattr]'
G.add_edge('filtered_google_app','mediaserver')
G.edge['filtered_google_app']['mediaserver']['write-read'] = '[setattr getattr]'
G.add_edge('filtered_google_app','radio')
G.edge['filtered_google_app']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','rild')
G.edge['filtered_google_app']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('filtered_google_app','s_system_app')
G.edge['filtered_google_app']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','syscope_app')
G.edge['filtered_google_app']['syscope_app']['write-read'] = '[setattr getattr]'
G.add_edge('filtered_google_app','system_app')
G.edge['filtered_google_app']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','system_server')
G.edge['filtered_google_app']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('filtered_google_app','debuggerd')
G.edge['filtered_google_app']['debuggerd']['write-read'] = '[setattr getattr][setattr getattr]'
G.add_edge('filtered_google_app','epmd')
G.edge['filtered_google_app']['epmd']['write-read'] = '[setattr getattr][setattr getattr]'
G.add_edge('filtered_google_app','ime_app')
G.edge['filtered_google_app']['ime_app']['write-read'] = '[open open][setattr getattr][setattr getattr]'
G.add_edge('filtered_google_app','installd')
G.edge['filtered_google_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('filtered_google_app','knox_system_app')
G.edge['filtered_google_app']['knox_system_app']['write-read'] = '[setattr getattr][setattr getattr]'
G.add_edge('filtered_google_app','location_app')
G.edge['filtered_google_app']['location_app']['write-read'] = '[setattr getattr][setattr getattr]'
G.add_edge('filtered_google_app','mediaserver')
G.edge['filtered_google_app']['mediaserver']['write-read'] = '[setattr getattr][setattr getattr]'
G.add_edge('filtered_google_app','radio')
G.edge['filtered_google_app']['radio']['write-read'] = '[open open][setattr getattr][setattr getattr]'
G.add_edge('filtered_google_app','rild')
G.edge['filtered_google_app']['rild']['write-read'] = '[setattr getattr][setattr getattr]'
G.add_edge('filtered_google_app','s_system_app')
G.edge['filtered_google_app']['s_system_app']['write-read'] = '[open open][setattr getattr][setattr getattr]'
G.add_edge('filtered_google_app','syscope_app')
G.edge['filtered_google_app']['syscope_app']['write-read'] = '[setattr getattr][setattr getattr]'
G.add_edge('filtered_google_app','system_app')
G.edge['filtered_google_app']['system_app']['write-read'] = '[open open][setattr getattr][setattr getattr]'
G.add_edge('filtered_google_app','system_server')
G.edge['filtered_google_app']['system_server']['write-read'] = '[setattr getattr][setattr getattr]'
G.add_edge('filtered_google_app','carrier_app')
G.edge['filtered_google_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_google_app']['carrier_app']['fill'] = 'red'
G.add_edge('filtered_google_app','debuggerd')
G.edge['filtered_google_app']['debuggerd']['write-read'] = '[setattr getattr][setattr getattr][write read]'
G.edge['filtered_google_app']['debuggerd']['fill'] = 'red'
G.add_edge('filtered_google_app','debuggerd')
G.edge['filtered_google_app']['debuggerd']['write-read'] = '[setattr getattr][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','epmd')
G.edge['filtered_google_app']['epmd']['write-read'] = '[setattr getattr][setattr getattr][write read]'
G.edge['filtered_google_app']['epmd']['fill'] = 'red'
G.add_edge('filtered_google_app','epmd')
G.edge['filtered_google_app']['epmd']['write-read'] = '[setattr getattr][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','filtered_google_app')
G.edge['filtered_google_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_google_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('filtered_google_app','filtered_untrusted_app')
G.edge['filtered_google_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_google_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_google_app','gad_untrusted_app')
G.edge['filtered_google_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_google_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_google_app','ime_app')
G.edge['filtered_google_app']['ime_app']['write-read'] = '[open open][setattr getattr][setattr getattr][write read]'
G.edge['filtered_google_app']['ime_app']['fill'] = 'red'
G.add_edge('filtered_google_app','ime_app')
G.edge['filtered_google_app']['ime_app']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','irm_app')
G.edge['filtered_google_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_google_app']['irm_app']['fill'] = 'red'
G.add_edge('filtered_google_app','knox_system_app')
G.edge['filtered_google_app']['knox_system_app']['write-read'] = '[setattr getattr][setattr getattr][write read]'
G.edge['filtered_google_app']['knox_system_app']['fill'] = 'red'
G.add_edge('filtered_google_app','knox_system_app')
G.edge['filtered_google_app']['knox_system_app']['write-read'] = '[setattr getattr][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','knox_untrusted_app')
G.edge['filtered_google_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_google_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_google_app','llk_untrusted_app')
G.edge['filtered_google_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_google_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_google_app','location_app')
G.edge['filtered_google_app']['location_app']['write-read'] = '[setattr getattr][setattr getattr][write read]'
G.edge['filtered_google_app']['location_app']['fill'] = 'red'
G.add_edge('filtered_google_app','location_app')
G.edge['filtered_google_app']['location_app']['write-read'] = '[setattr getattr][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','mediaserver')
G.edge['filtered_google_app']['mediaserver']['write-read'] = '[setattr getattr][setattr getattr][write read]'
G.edge['filtered_google_app']['mediaserver']['fill'] = 'red'
G.add_edge('filtered_google_app','mediaserver')
G.edge['filtered_google_app']['mediaserver']['write-read'] = '[setattr getattr][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','mediaserver')
G.edge['filtered_google_app']['mediaserver']['write-read'] = '[setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['filtered_google_app']['mediaserver']['fill'] = 'red'
G.add_edge('filtered_google_app','mediaserver')
G.edge['filtered_google_app']['mediaserver']['write-read'] = '[setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('filtered_google_app','platformappdomain')
G.edge['filtered_google_app']['platformappdomain']['write-read'] = '[write read]'
G.edge['filtered_google_app']['platformappdomain']['fill'] = 'red'
G.add_edge('filtered_google_app','rild')
G.edge['filtered_google_app']['rild']['write-read'] = '[setattr getattr][setattr getattr][write read]'
G.edge['filtered_google_app']['rild']['fill'] = 'red'
G.add_edge('filtered_google_app','rild')
G.edge['filtered_google_app']['rild']['write-read'] = '[setattr getattr][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','s_system_app')
G.edge['filtered_google_app']['s_system_app']['write-read'] = '[open open][setattr getattr][setattr getattr][write read]'
G.edge['filtered_google_app']['s_system_app']['fill'] = 'red'
G.add_edge('filtered_google_app','s_system_app')
G.edge['filtered_google_app']['s_system_app']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','syscope_app')
G.edge['filtered_google_app']['syscope_app']['write-read'] = '[setattr getattr][setattr getattr][write read]'
G.edge['filtered_google_app']['syscope_app']['fill'] = 'red'
G.add_edge('filtered_google_app','syscope_app')
G.edge['filtered_google_app']['syscope_app']['write-read'] = '[setattr getattr][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','system_app')
G.edge['filtered_google_app']['system_app']['write-read'] = '[open open][setattr getattr][setattr getattr][write read]'
G.edge['filtered_google_app']['system_app']['fill'] = 'red'
G.add_edge('filtered_google_app','system_app')
G.edge['filtered_google_app']['system_app']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','system_server')
G.edge['filtered_google_app']['system_server']['write-read'] = '[setattr getattr][setattr getattr][write read]'
G.edge['filtered_google_app']['system_server']['fill'] = 'red'
G.add_edge('filtered_google_app','system_server')
G.edge['filtered_google_app']['system_server']['write-read'] = '[setattr getattr][setattr getattr][write read][write read]'
G.edge['filtered_google_app']['system_server']['fill'] = 'red'
G.add_edge('filtered_google_app','system_server')
G.edge['filtered_google_app']['system_server']['write-read'] = '[setattr getattr][setattr getattr][write read][write read][append read]'
G.add_edge('filtered_google_app','trustonicpartner_app')
G.edge['filtered_google_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_google_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('filtered_google_app','umcagent_app')
G.edge['filtered_google_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_google_app']['umcagent_app']['fill'] = 'red'
G.add_edge('filtered_google_app','untrusted_app')
G.edge['filtered_google_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_google_app']['untrusted_app']['fill'] = 'red'
G.add_edge('filtered_google_app','vpn_untrusted_app')
G.edge['filtered_google_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_google_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','debuggerd')
G.edge['filtered_untrusted_app']['debuggerd']['write-read'] = '[setattr getattr]'
G.add_edge('filtered_untrusted_app','epmd')
G.edge['filtered_untrusted_app']['epmd']['write-read'] = '[setattr getattr]'
G.add_edge('filtered_untrusted_app','ime_app')
G.edge['filtered_untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','installd')
G.edge['filtered_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('filtered_untrusted_app','knox_system_app')
G.edge['filtered_untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr]'
G.add_edge('filtered_untrusted_app','location_app')
G.edge['filtered_untrusted_app']['location_app']['write-read'] = '[setattr getattr]'
G.add_edge('filtered_untrusted_app','mediaserver')
G.edge['filtered_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr]'
G.add_edge('filtered_untrusted_app','radio')
G.edge['filtered_untrusted_app']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','rild')
G.edge['filtered_untrusted_app']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('filtered_untrusted_app','s_system_app')
G.edge['filtered_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','syscope_app')
G.edge['filtered_untrusted_app']['syscope_app']['write-read'] = '[setattr getattr]'
G.add_edge('filtered_untrusted_app','system_app')
G.edge['filtered_untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','system_server')
G.edge['filtered_untrusted_app']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('filtered_untrusted_app','carrier_app')
G.edge['filtered_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['carrier_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','debuggerd')
G.edge['filtered_untrusted_app']['debuggerd']['write-read'] = '[setattr getattr][write read]'
G.edge['filtered_untrusted_app']['debuggerd']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','debuggerd')
G.edge['filtered_untrusted_app']['debuggerd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','epmd')
G.edge['filtered_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read]'
G.edge['filtered_untrusted_app']['epmd']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','epmd')
G.edge['filtered_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','filtered_google_app')
G.edge['filtered_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','filtered_untrusted_app')
G.edge['filtered_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','gad_untrusted_app')
G.edge['filtered_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','ime_app')
G.edge['filtered_untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['ime_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','ime_app')
G.edge['filtered_untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','irm_app')
G.edge['filtered_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['irm_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','knox_system_app')
G.edge['filtered_untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr][write read]'
G.edge['filtered_untrusted_app']['knox_system_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','knox_system_app')
G.edge['filtered_untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','knox_untrusted_app')
G.edge['filtered_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','llk_untrusted_app')
G.edge['filtered_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','location_app')
G.edge['filtered_untrusted_app']['location_app']['write-read'] = '[setattr getattr][write read]'
G.edge['filtered_untrusted_app']['location_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','location_app')
G.edge['filtered_untrusted_app']['location_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','mediaserver')
G.edge['filtered_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read]'
G.edge['filtered_untrusted_app']['mediaserver']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','mediaserver')
G.edge['filtered_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','mediaserver')
G.edge['filtered_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read]'
G.edge['filtered_untrusted_app']['mediaserver']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','mediaserver')
G.edge['filtered_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read]'
G.add_edge('filtered_untrusted_app','platformappdomain')
G.edge['filtered_untrusted_app']['platformappdomain']['write-read'] = '[write read]'
G.edge['filtered_untrusted_app']['platformappdomain']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','rild')
G.edge['filtered_untrusted_app']['rild']['write-read'] = '[setattr getattr][write read]'
G.edge['filtered_untrusted_app']['rild']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','rild')
G.edge['filtered_untrusted_app']['rild']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','s_system_app')
G.edge['filtered_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['s_system_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','s_system_app')
G.edge['filtered_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','syscope_app')
G.edge['filtered_untrusted_app']['syscope_app']['write-read'] = '[setattr getattr][write read]'
G.edge['filtered_untrusted_app']['syscope_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','syscope_app')
G.edge['filtered_untrusted_app']['syscope_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','system_app')
G.edge['filtered_untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['system_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','system_app')
G.edge['filtered_untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','system_server')
G.edge['filtered_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read]'
G.edge['filtered_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','system_server')
G.edge['filtered_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['filtered_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','system_server')
G.edge['filtered_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read]'
G.add_edge('filtered_untrusted_app','trustonicpartner_app')
G.edge['filtered_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','umcagent_app')
G.edge['filtered_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['umcagent_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','untrusted_app')
G.edge['filtered_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['untrusted_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','vpn_untrusted_app')
G.edge['filtered_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','debuggerd')
G.edge['gad_untrusted_app']['debuggerd']['write-read'] = '[setattr getattr]'
G.add_edge('gad_untrusted_app','epmd')
G.edge['gad_untrusted_app']['epmd']['write-read'] = '[setattr getattr]'
G.add_edge('gad_untrusted_app','ime_app')
G.edge['gad_untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','installd')
G.edge['gad_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('gad_untrusted_app','knox_system_app')
G.edge['gad_untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr]'
G.add_edge('gad_untrusted_app','location_app')
G.edge['gad_untrusted_app']['location_app']['write-read'] = '[setattr getattr]'
G.add_edge('gad_untrusted_app','mediaserver')
G.edge['gad_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr]'
G.add_edge('gad_untrusted_app','radio')
G.edge['gad_untrusted_app']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','rild')
G.edge['gad_untrusted_app']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('gad_untrusted_app','s_system_app')
G.edge['gad_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','syscope_app')
G.edge['gad_untrusted_app']['syscope_app']['write-read'] = '[setattr getattr]'
G.add_edge('gad_untrusted_app','system_app')
G.edge['gad_untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','system_server')
G.edge['gad_untrusted_app']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('gad_untrusted_app','carrier_app')
G.edge['gad_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['carrier_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','debuggerd')
G.edge['gad_untrusted_app']['debuggerd']['write-read'] = '[setattr getattr][write read]'
G.edge['gad_untrusted_app']['debuggerd']['fill'] = 'red'
G.add_edge('gad_untrusted_app','debuggerd')
G.edge['gad_untrusted_app']['debuggerd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','epmd')
G.edge['gad_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read]'
G.edge['gad_untrusted_app']['epmd']['fill'] = 'red'
G.add_edge('gad_untrusted_app','epmd')
G.edge['gad_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','filtered_google_app')
G.edge['gad_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','filtered_untrusted_app')
G.edge['gad_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','gad_untrusted_app')
G.edge['gad_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','ime_app')
G.edge['gad_untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['ime_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','ime_app')
G.edge['gad_untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','irm_app')
G.edge['gad_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['irm_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','knox_system_app')
G.edge['gad_untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr][write read]'
G.edge['gad_untrusted_app']['knox_system_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','knox_system_app')
G.edge['gad_untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','knox_untrusted_app')
G.edge['gad_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','llk_untrusted_app')
G.edge['gad_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','location_app')
G.edge['gad_untrusted_app']['location_app']['write-read'] = '[setattr getattr][write read]'
G.edge['gad_untrusted_app']['location_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','location_app')
G.edge['gad_untrusted_app']['location_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','mediaserver')
G.edge['gad_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read]'
G.edge['gad_untrusted_app']['mediaserver']['fill'] = 'red'
G.add_edge('gad_untrusted_app','mediaserver')
G.edge['gad_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','mediaserver')
G.edge['gad_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read]'
G.edge['gad_untrusted_app']['mediaserver']['fill'] = 'red'
G.add_edge('gad_untrusted_app','mediaserver')
G.edge['gad_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read]'
G.add_edge('gad_untrusted_app','platformappdomain')
G.edge['gad_untrusted_app']['platformappdomain']['write-read'] = '[write read]'
G.edge['gad_untrusted_app']['platformappdomain']['fill'] = 'red'
G.add_edge('gad_untrusted_app','rild')
G.edge['gad_untrusted_app']['rild']['write-read'] = '[setattr getattr][write read]'
G.edge['gad_untrusted_app']['rild']['fill'] = 'red'
G.add_edge('gad_untrusted_app','rild')
G.edge['gad_untrusted_app']['rild']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','s_system_app')
G.edge['gad_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['s_system_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','s_system_app')
G.edge['gad_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','syscope_app')
G.edge['gad_untrusted_app']['syscope_app']['write-read'] = '[setattr getattr][write read]'
G.edge['gad_untrusted_app']['syscope_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','syscope_app')
G.edge['gad_untrusted_app']['syscope_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','system_app')
G.edge['gad_untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['system_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','system_app')
G.edge['gad_untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','system_server')
G.edge['gad_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read]'
G.edge['gad_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('gad_untrusted_app','system_server')
G.edge['gad_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['gad_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('gad_untrusted_app','system_server')
G.edge['gad_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read]'
G.add_edge('gad_untrusted_app','trustonicpartner_app')
G.edge['gad_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','umcagent_app')
G.edge['gad_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['umcagent_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','untrusted_app')
G.edge['gad_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['untrusted_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','vpn_untrusted_app')
G.edge['gad_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('ime_app','debuggerd')
G.edge['ime_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','epmd')
G.edge['ime_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','knox_system_app')
G.edge['ime_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','location_app')
G.edge['ime_app']['location_app']['write-read'] = '[open open]'
G.add_edge('ime_app','mediaserver')
G.edge['ime_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','mediaserver')
G.edge['ime_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('ime_app','rild')
G.edge['ime_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','syscope_app')
G.edge['ime_app']['syscope_app']['write-read'] = '[open open]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','debuggerd')
G.edge['ime_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ime_app','epmd')
G.edge['ime_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','installd')
G.edge['ime_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('ime_app','knox_system_app')
G.edge['ime_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','location_app')
G.edge['ime_app']['location_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','mediaserver')
G.edge['ime_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('ime_app','radio')
G.edge['ime_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('ime_app','rild')
G.edge['ime_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','syscope_app')
G.edge['ime_app']['syscope_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','carrier_app')
G.edge['ime_app']['carrier_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['ime_app']['carrier_app']['fill'] = 'red'
G.add_edge('ime_app','debuggerd')
G.edge['ime_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ime_app']['debuggerd']['fill'] = 'red'
G.add_edge('ime_app','debuggerd')
G.edge['ime_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','epmd')
G.edge['ime_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['epmd']['fill'] = 'red'
G.add_edge('ime_app','epmd')
G.edge['ime_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','filtered_google_app')
G.edge['ime_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['ime_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('ime_app','filtered_untrusted_app')
G.edge['ime_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['ime_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('ime_app','gad_untrusted_app')
G.edge['ime_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['ime_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['ime_app']['fill'] = 'red'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','irm_app')
G.edge['ime_app']['irm_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['ime_app']['irm_app']['fill'] = 'red'
G.add_edge('ime_app','knox_system_app')
G.edge['ime_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['knox_system_app']['fill'] = 'red'
G.add_edge('ime_app','knox_system_app')
G.edge['ime_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','knox_untrusted_app')
G.edge['ime_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['ime_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('ime_app','llk_untrusted_app')
G.edge['ime_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['ime_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('ime_app','location_app')
G.edge['ime_app']['location_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['location_app']['fill'] = 'red'
G.add_edge('ime_app','location_app')
G.edge['ime_app']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','mediaserver')
G.edge['ime_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['ime_app']['mediaserver']['fill'] = 'red'
G.add_edge('ime_app','mediaserver')
G.edge['ime_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','mediaserver')
G.edge['ime_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['ime_app']['mediaserver']['fill'] = 'red'
G.add_edge('ime_app','mediaserver')
G.edge['ime_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('ime_app','platformappdomain')
G.edge['ime_app']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['ime_app']['platformappdomain']['fill'] = 'red'
G.add_edge('ime_app','rild')
G.edge['ime_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['rild']['fill'] = 'red'
G.add_edge('ime_app','rild')
G.edge['ime_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['s_system_app']['fill'] = 'red'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','syscope_app')
G.edge['ime_app']['syscope_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['syscope_app']['fill'] = 'red'
G.add_edge('ime_app','syscope_app')
G.edge['ime_app']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['system_app']['fill'] = 'red'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['system_server']['fill'] = 'red'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read]'
G.edge['ime_app']['system_server']['fill'] = 'red'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read]'
G.add_edge('ime_app','trustonicpartner_app')
G.edge['ime_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['ime_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('ime_app','umcagent_app')
G.edge['ime_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['ime_app']['umcagent_app']['fill'] = 'red'
G.add_edge('ime_app','untrusted_app')
G.edge['ime_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['ime_app']['untrusted_app']['fill'] = 'red'
G.add_edge('ime_app','vpn_untrusted_app')
G.edge['ime_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['ime_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('ime_app','debuggerd')
G.edge['ime_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('ime_app','epmd')
G.edge['ime_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('ime_app','installd')
G.edge['ime_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('ime_app','knox_system_app')
G.edge['ime_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('ime_app','location_app')
G.edge['ime_app']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('ime_app','mediaserver')
G.edge['ime_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr]'
G.add_edge('ime_app','radio')
G.edge['ime_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr]'
G.add_edge('ime_app','rild')
G.edge['ime_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('ime_app','syscope_app')
G.edge['ime_app']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr]'
G.add_edge('installd','debuggerd')
G.edge['installd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','epmd')
G.edge['installd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','ime_app')
G.edge['installd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','knox_system_app')
G.edge['installd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','location_app')
G.edge['installd']['location_app']['write-read'] = '[setattr getattr]'
G.add_edge('installd','mediaserver')
G.edge['installd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','radio')
G.edge['installd']['radio']['write-read'] = '[setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('installd','rild')
G.edge['installd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','s_system_app')
G.edge['installd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('installd','syscope_app')
G.edge['installd']['syscope_app']['write-read'] = '[setattr getattr]'
G.add_edge('installd','system_app')
G.edge['installd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','epmd')
G.edge['installd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom]'
G.add_edge('irm_app','debuggerd')
G.edge['irm_app']['debuggerd']['write-read'] = '[setattr getattr]'
G.add_edge('irm_app','epmd')
G.edge['irm_app']['epmd']['write-read'] = '[setattr getattr]'
G.add_edge('irm_app','ime_app')
G.edge['irm_app']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','installd')
G.edge['irm_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('irm_app','knox_system_app')
G.edge['irm_app']['knox_system_app']['write-read'] = '[setattr getattr]'
G.add_edge('irm_app','location_app')
G.edge['irm_app']['location_app']['write-read'] = '[setattr getattr]'
G.add_edge('irm_app','mediaserver')
G.edge['irm_app']['mediaserver']['write-read'] = '[setattr getattr]'
G.add_edge('irm_app','radio')
G.edge['irm_app']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','rild')
G.edge['irm_app']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('irm_app','s_system_app')
G.edge['irm_app']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','syscope_app')
G.edge['irm_app']['syscope_app']['write-read'] = '[setattr getattr]'
G.add_edge('irm_app','system_app')
G.edge['irm_app']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','system_server')
G.edge['irm_app']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('irm_app','carrier_app')
G.edge['irm_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_app']['carrier_app']['fill'] = 'red'
G.add_edge('irm_app','debuggerd')
G.edge['irm_app']['debuggerd']['write-read'] = '[setattr getattr][write read]'
G.edge['irm_app']['debuggerd']['fill'] = 'red'
G.add_edge('irm_app','debuggerd')
G.edge['irm_app']['debuggerd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('irm_app','epmd')
G.edge['irm_app']['epmd']['write-read'] = '[setattr getattr][write read]'
G.edge['irm_app']['epmd']['fill'] = 'red'
G.add_edge('irm_app','epmd')
G.edge['irm_app']['epmd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('irm_app','filtered_google_app')
G.edge['irm_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('irm_app','filtered_untrusted_app')
G.edge['irm_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('irm_app','gad_untrusted_app')
G.edge['irm_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('irm_app','ime_app')
G.edge['irm_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_app']['ime_app']['fill'] = 'red'
G.add_edge('irm_app','ime_app')
G.edge['irm_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','irm_app')
G.edge['irm_app']['irm_app']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['irm_app']['irm_app']['fill'] = 'red'
G.add_edge('irm_app','knox_system_app')
G.edge['irm_app']['knox_system_app']['write-read'] = '[setattr getattr][write read]'
G.edge['irm_app']['knox_system_app']['fill'] = 'red'
G.add_edge('irm_app','knox_system_app')
G.edge['irm_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('irm_app','knox_untrusted_app')
G.edge['irm_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('irm_app','llk_untrusted_app')
G.edge['irm_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('irm_app','location_app')
G.edge['irm_app']['location_app']['write-read'] = '[setattr getattr][write read]'
G.edge['irm_app']['location_app']['fill'] = 'red'
G.add_edge('irm_app','location_app')
G.edge['irm_app']['location_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('irm_app','mediaserver')
G.edge['irm_app']['mediaserver']['write-read'] = '[setattr getattr][write read]'
G.edge['irm_app']['mediaserver']['fill'] = 'red'
G.add_edge('irm_app','mediaserver')
G.edge['irm_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('irm_app','mediaserver')
G.edge['irm_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read]'
G.edge['irm_app']['mediaserver']['fill'] = 'red'
G.add_edge('irm_app','mediaserver')
G.edge['irm_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read]'
G.add_edge('irm_app','platformappdomain')
G.edge['irm_app']['platformappdomain']['write-read'] = '[write read]'
G.edge['irm_app']['platformappdomain']['fill'] = 'red'
G.add_edge('irm_app','rild')
G.edge['irm_app']['rild']['write-read'] = '[setattr getattr][write read]'
G.edge['irm_app']['rild']['fill'] = 'red'
G.add_edge('irm_app','rild')
G.edge['irm_app']['rild']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('irm_app','s_system_app')
G.edge['irm_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_app']['s_system_app']['fill'] = 'red'
G.add_edge('irm_app','s_system_app')
G.edge['irm_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','syscope_app')
G.edge['irm_app']['syscope_app']['write-read'] = '[setattr getattr][write read]'
G.edge['irm_app']['syscope_app']['fill'] = 'red'
G.add_edge('irm_app','syscope_app')
G.edge['irm_app']['syscope_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('irm_app','system_app')
G.edge['irm_app']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_app']['system_app']['fill'] = 'red'
G.add_edge('irm_app','system_app')
G.edge['irm_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','system_server')
G.edge['irm_app']['system_server']['write-read'] = '[setattr getattr][write read]'
G.edge['irm_app']['system_server']['fill'] = 'red'
G.add_edge('irm_app','system_server')
G.edge['irm_app']['system_server']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['irm_app']['system_server']['fill'] = 'red'
G.add_edge('irm_app','system_server')
G.edge['irm_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read]'
G.add_edge('irm_app','trustonicpartner_app')
G.edge['irm_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('irm_app','umcagent_app')
G.edge['irm_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_app']['umcagent_app']['fill'] = 'red'
G.add_edge('irm_app','untrusted_app')
G.edge['irm_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_app']['untrusted_app']['fill'] = 'red'
G.add_edge('irm_app','vpn_untrusted_app')
G.edge['irm_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('knox_system_app','debuggerd')
G.edge['knox_system_app']['debuggerd']['write-read'] = '[open open]'
G.add_edge('knox_system_app','epmd')
G.edge['knox_system_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_system_app','ime_app')
G.edge['knox_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_system_app','location_app')
G.edge['knox_system_app']['location_app']['write-read'] = '[open open]'
G.add_edge('knox_system_app','mediaserver')
G.edge['knox_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_system_app','mediaserver')
G.edge['knox_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('knox_system_app','rild')
G.edge['knox_system_app']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_system_app','syscope_app')
G.edge['knox_system_app']['syscope_app']['write-read'] = '[open open]'
G.add_edge('knox_system_app','system_app')
G.edge['knox_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_system_app','debuggerd')
G.edge['knox_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','epmd')
G.edge['knox_system_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('knox_system_app','ime_app')
G.edge['knox_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('knox_system_app','installd')
G.edge['knox_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('knox_system_app','location_app')
G.edge['knox_system_app']['location_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','mediaserver')
G.edge['knox_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('knox_system_app','radio')
G.edge['knox_system_app']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('knox_system_app','rild')
G.edge['knox_system_app']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('knox_system_app','syscope_app')
G.edge['knox_system_app']['syscope_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','system_app')
G.edge['knox_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('knox_system_app','carrier_app')
G.edge['knox_system_app']['carrier_app']['write-read'] = '[write read]'
G.edge['knox_system_app']['carrier_app']['fill'] = 'red'
G.add_edge('knox_system_app','debuggerd')
G.edge['knox_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['debuggerd']['fill'] = 'red'
G.add_edge('knox_system_app','debuggerd')
G.edge['knox_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','epmd')
G.edge['knox_system_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_system_app']['epmd']['fill'] = 'red'
G.add_edge('knox_system_app','epmd')
G.edge['knox_system_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','filtered_google_app')
G.edge['knox_system_app']['filtered_google_app']['write-read'] = '[write read]'
G.edge['knox_system_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('knox_system_app','filtered_untrusted_app')
G.edge['knox_system_app']['filtered_untrusted_app']['write-read'] = '[write read]'
G.edge['knox_system_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('knox_system_app','gad_untrusted_app')
G.edge['knox_system_app']['gad_untrusted_app']['write-read'] = '[write read]'
G.edge['knox_system_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('knox_system_app','ime_app')
G.edge['knox_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_system_app']['ime_app']['fill'] = 'red'
G.add_edge('knox_system_app','ime_app')
G.edge['knox_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','irm_app')
G.edge['knox_system_app']['irm_app']['write-read'] = '[write read]'
G.edge['knox_system_app']['irm_app']['fill'] = 'red'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_system_app']['knox_system_app']['fill'] = 'red'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','knox_untrusted_app')
G.edge['knox_system_app']['knox_untrusted_app']['write-read'] = '[write read]'
G.edge['knox_system_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('knox_system_app','llk_untrusted_app')
G.edge['knox_system_app']['llk_untrusted_app']['write-read'] = '[write read]'
G.edge['knox_system_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('knox_system_app','location_app')
G.edge['knox_system_app']['location_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['location_app']['fill'] = 'red'
G.add_edge('knox_system_app','location_app')
G.edge['knox_system_app']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','mediaserver')
G.edge['knox_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['knox_system_app']['mediaserver']['fill'] = 'red'
G.add_edge('knox_system_app','mediaserver')
G.edge['knox_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','mediaserver')
G.edge['knox_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['knox_system_app']['mediaserver']['fill'] = 'red'
G.add_edge('knox_system_app','mediaserver')
G.edge['knox_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('knox_system_app','platformappdomain')
G.edge['knox_system_app']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['knox_system_app']['platformappdomain']['fill'] = 'red'
G.add_edge('knox_system_app','rild')
G.edge['knox_system_app']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_system_app']['rild']['fill'] = 'red'
G.add_edge('knox_system_app','rild')
G.edge['knox_system_app']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','syscope_app')
G.edge['knox_system_app']['syscope_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['syscope_app']['fill'] = 'red'
G.add_edge('knox_system_app','syscope_app')
G.edge['knox_system_app']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','system_app')
G.edge['knox_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_system_app']['system_app']['fill'] = 'red'
G.add_edge('knox_system_app','system_app')
G.edge['knox_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_system_app']['system_server']['fill'] = 'red'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read]'
G.edge['knox_system_app']['system_server']['fill'] = 'red'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read]'
G.add_edge('knox_system_app','trustonicpartner_app')
G.edge['knox_system_app']['trustonicpartner_app']['write-read'] = '[write read]'
G.edge['knox_system_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('knox_system_app','umcagent_app')
G.edge['knox_system_app']['umcagent_app']['write-read'] = '[write read]'
G.edge['knox_system_app']['umcagent_app']['fill'] = 'red'
G.add_edge('knox_system_app','untrusted_app')
G.edge['knox_system_app']['untrusted_app']['write-read'] = '[write read]'
G.edge['knox_system_app']['untrusted_app']['fill'] = 'red'
G.add_edge('knox_system_app','vpn_untrusted_app')
G.edge['knox_system_app']['vpn_untrusted_app']['write-read'] = '[write read]'
G.edge['knox_system_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('knox_system_app','debuggerd')
G.edge['knox_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('knox_system_app','epmd')
G.edge['knox_system_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('knox_system_app','ime_app')
G.edge['knox_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('knox_system_app','installd')
G.edge['knox_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('knox_system_app','location_app')
G.edge['knox_system_app']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('knox_system_app','mediaserver')
G.edge['knox_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr]'
G.add_edge('knox_system_app','radio')
G.edge['knox_system_app']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setattr getattr]'
G.add_edge('knox_system_app','rild')
G.edge['knox_system_app']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('knox_system_app','syscope_app')
G.edge['knox_system_app']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('knox_system_app','system_app')
G.edge['knox_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr]'
G.add_edge('knox_untrusted_app','debuggerd')
G.edge['knox_untrusted_app']['debuggerd']['write-read'] = '[setattr getattr]'
G.add_edge('knox_untrusted_app','epmd')
G.edge['knox_untrusted_app']['epmd']['write-read'] = '[setattr getattr]'
G.add_edge('knox_untrusted_app','ime_app')
G.edge['knox_untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','installd')
G.edge['knox_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('knox_untrusted_app','knox_system_app')
G.edge['knox_untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr]'
G.add_edge('knox_untrusted_app','location_app')
G.edge['knox_untrusted_app']['location_app']['write-read'] = '[setattr getattr]'
G.add_edge('knox_untrusted_app','mediaserver')
G.edge['knox_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr]'
G.add_edge('knox_untrusted_app','radio')
G.edge['knox_untrusted_app']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','rild')
G.edge['knox_untrusted_app']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('knox_untrusted_app','s_system_app')
G.edge['knox_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','syscope_app')
G.edge['knox_untrusted_app']['syscope_app']['write-read'] = '[setattr getattr]'
G.add_edge('knox_untrusted_app','system_app')
G.edge['knox_untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','system_server')
G.edge['knox_untrusted_app']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('knox_untrusted_app','carrier_app')
G.edge['knox_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['carrier_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','debuggerd')
G.edge['knox_untrusted_app']['debuggerd']['write-read'] = '[setattr getattr][write read]'
G.edge['knox_untrusted_app']['debuggerd']['fill'] = 'red'
G.add_edge('knox_untrusted_app','debuggerd')
G.edge['knox_untrusted_app']['debuggerd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','epmd')
G.edge['knox_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read]'
G.edge['knox_untrusted_app']['epmd']['fill'] = 'red'
G.add_edge('knox_untrusted_app','epmd')
G.edge['knox_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','filtered_google_app')
G.edge['knox_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','filtered_untrusted_app')
G.edge['knox_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','gad_untrusted_app')
G.edge['knox_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','ime_app')
G.edge['knox_untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['ime_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','ime_app')
G.edge['knox_untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','irm_app')
G.edge['knox_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['irm_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','knox_system_app')
G.edge['knox_untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr][write read]'
G.edge['knox_untrusted_app']['knox_system_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','knox_system_app')
G.edge['knox_untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','knox_untrusted_app')
G.edge['knox_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][open open][setattr getattr][write read][append read][write read]'
G.edge['knox_untrusted_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','llk_untrusted_app')
G.edge['knox_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','location_app')
G.edge['knox_untrusted_app']['location_app']['write-read'] = '[setattr getattr][write read]'
G.edge['knox_untrusted_app']['location_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','location_app')
G.edge['knox_untrusted_app']['location_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','mediaserver')
G.edge['knox_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read]'
G.edge['knox_untrusted_app']['mediaserver']['fill'] = 'red'
G.add_edge('knox_untrusted_app','mediaserver')
G.edge['knox_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','mediaserver')
G.edge['knox_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read]'
G.edge['knox_untrusted_app']['mediaserver']['fill'] = 'red'
G.add_edge('knox_untrusted_app','mediaserver')
G.edge['knox_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read]'
G.add_edge('knox_untrusted_app','platformappdomain')
G.edge['knox_untrusted_app']['platformappdomain']['write-read'] = '[write read]'
G.edge['knox_untrusted_app']['platformappdomain']['fill'] = 'red'
G.add_edge('knox_untrusted_app','rild')
G.edge['knox_untrusted_app']['rild']['write-read'] = '[setattr getattr][write read]'
G.edge['knox_untrusted_app']['rild']['fill'] = 'red'
G.add_edge('knox_untrusted_app','rild')
G.edge['knox_untrusted_app']['rild']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','s_system_app')
G.edge['knox_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['s_system_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','s_system_app')
G.edge['knox_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','syscope_app')
G.edge['knox_untrusted_app']['syscope_app']['write-read'] = '[setattr getattr][write read]'
G.edge['knox_untrusted_app']['syscope_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','syscope_app')
G.edge['knox_untrusted_app']['syscope_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','system_app')
G.edge['knox_untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['system_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','system_app')
G.edge['knox_untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','system_server')
G.edge['knox_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read]'
G.edge['knox_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('knox_untrusted_app','system_server')
G.edge['knox_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['knox_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('knox_untrusted_app','system_server')
G.edge['knox_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read]'
G.add_edge('knox_untrusted_app','trustonicpartner_app')
G.edge['knox_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','umcagent_app')
G.edge['knox_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['umcagent_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','untrusted_app')
G.edge['knox_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['untrusted_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','vpn_untrusted_app')
G.edge['knox_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','debuggerd')
G.edge['llk_untrusted_app']['debuggerd']['write-read'] = '[setattr getattr]'
G.add_edge('llk_untrusted_app','epmd')
G.edge['llk_untrusted_app']['epmd']['write-read'] = '[setattr getattr]'
G.add_edge('llk_untrusted_app','ime_app')
G.edge['llk_untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','installd')
G.edge['llk_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('llk_untrusted_app','knox_system_app')
G.edge['llk_untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr]'
G.add_edge('llk_untrusted_app','location_app')
G.edge['llk_untrusted_app']['location_app']['write-read'] = '[setattr getattr]'
G.add_edge('llk_untrusted_app','mediaserver')
G.edge['llk_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr]'
G.add_edge('llk_untrusted_app','radio')
G.edge['llk_untrusted_app']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','rild')
G.edge['llk_untrusted_app']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('llk_untrusted_app','s_system_app')
G.edge['llk_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','syscope_app')
G.edge['llk_untrusted_app']['syscope_app']['write-read'] = '[setattr getattr]'
G.add_edge('llk_untrusted_app','system_app')
G.edge['llk_untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','system_server')
G.edge['llk_untrusted_app']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('llk_untrusted_app','carrier_app')
G.edge['llk_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['carrier_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','debuggerd')
G.edge['llk_untrusted_app']['debuggerd']['write-read'] = '[setattr getattr][write read]'
G.edge['llk_untrusted_app']['debuggerd']['fill'] = 'red'
G.add_edge('llk_untrusted_app','debuggerd')
G.edge['llk_untrusted_app']['debuggerd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','epmd')
G.edge['llk_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read]'
G.edge['llk_untrusted_app']['epmd']['fill'] = 'red'
G.add_edge('llk_untrusted_app','epmd')
G.edge['llk_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','filtered_google_app')
G.edge['llk_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','filtered_untrusted_app')
G.edge['llk_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','gad_untrusted_app')
G.edge['llk_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','ime_app')
G.edge['llk_untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['ime_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','ime_app')
G.edge['llk_untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','irm_app')
G.edge['llk_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['irm_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','knox_system_app')
G.edge['llk_untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr][write read]'
G.edge['llk_untrusted_app']['knox_system_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','knox_system_app')
G.edge['llk_untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','knox_untrusted_app')
G.edge['llk_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','llk_untrusted_app')
G.edge['llk_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','location_app')
G.edge['llk_untrusted_app']['location_app']['write-read'] = '[setattr getattr][write read]'
G.edge['llk_untrusted_app']['location_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','location_app')
G.edge['llk_untrusted_app']['location_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','mediaserver')
G.edge['llk_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read]'
G.edge['llk_untrusted_app']['mediaserver']['fill'] = 'red'
G.add_edge('llk_untrusted_app','mediaserver')
G.edge['llk_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','mediaserver')
G.edge['llk_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read]'
G.edge['llk_untrusted_app']['mediaserver']['fill'] = 'red'
G.add_edge('llk_untrusted_app','mediaserver')
G.edge['llk_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read]'
G.add_edge('llk_untrusted_app','platformappdomain')
G.edge['llk_untrusted_app']['platformappdomain']['write-read'] = '[write read]'
G.edge['llk_untrusted_app']['platformappdomain']['fill'] = 'red'
G.add_edge('llk_untrusted_app','rild')
G.edge['llk_untrusted_app']['rild']['write-read'] = '[setattr getattr][write read]'
G.edge['llk_untrusted_app']['rild']['fill'] = 'red'
G.add_edge('llk_untrusted_app','rild')
G.edge['llk_untrusted_app']['rild']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','s_system_app')
G.edge['llk_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['s_system_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','s_system_app')
G.edge['llk_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','syscope_app')
G.edge['llk_untrusted_app']['syscope_app']['write-read'] = '[setattr getattr][write read]'
G.edge['llk_untrusted_app']['syscope_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','syscope_app')
G.edge['llk_untrusted_app']['syscope_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','system_app')
G.edge['llk_untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['system_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','system_app')
G.edge['llk_untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','system_server')
G.edge['llk_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read]'
G.edge['llk_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('llk_untrusted_app','system_server')
G.edge['llk_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['llk_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('llk_untrusted_app','system_server')
G.edge['llk_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read]'
G.add_edge('llk_untrusted_app','trustonicpartner_app')
G.edge['llk_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','umcagent_app')
G.edge['llk_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['umcagent_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','untrusted_app')
G.edge['llk_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['untrusted_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','vpn_untrusted_app')
G.edge['llk_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('location_app','debuggerd')
G.edge['location_app']['debuggerd']['write-read'] = '[open open]'
G.add_edge('location_app','epmd')
G.edge['location_app']['epmd']['write-read'] = '[open open]'
G.add_edge('location_app','ime_app')
G.edge['location_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('location_app','knox_system_app')
G.edge['location_app']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('location_app','location_app')
G.edge['location_app']['location_app']['write-read'] = '[open open]'
G.add_edge('location_app','mediaserver')
G.edge['location_app']['mediaserver']['write-read'] = '[open open]'
G.add_edge('location_app','mediaserver')
G.edge['location_app']['mediaserver']['write-read'] = '[open open][open open]'
G.add_edge('location_app','rild')
G.edge['location_app']['rild']['write-read'] = '[open open]'
G.add_edge('location_app','s_system_app')
G.edge['location_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('location_app','syscope_app')
G.edge['location_app']['syscope_app']['write-read'] = '[open open]'
G.add_edge('location_app','system_app')
G.edge['location_app']['system_app']['write-read'] = '[open open]'
G.add_edge('location_app','system_server')
G.edge['location_app']['system_server']['write-read'] = '[open open]'
G.add_edge('location_app','debuggerd')
G.edge['location_app']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('location_app','epmd')
G.edge['location_app']['epmd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('location_app','ime_app')
G.edge['location_app']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('location_app','installd')
G.edge['location_app']['installd']['write-read'] = '[setattr getattr]'
G.add_edge('location_app','knox_system_app')
G.edge['location_app']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('location_app','location_app')
G.edge['location_app']['location_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('location_app','mediaserver')
G.edge['location_app']['mediaserver']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('location_app','radio')
G.edge['location_app']['radio']['write-read'] = '[setattr getattr]'
G.add_edge('location_app','rild')
G.edge['location_app']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('location_app','s_system_app')
G.edge['location_app']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('location_app','syscope_app')
G.edge['location_app']['syscope_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('location_app','system_app')
G.edge['location_app']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('location_app','system_server')
G.edge['location_app']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('location_app','carrier_app')
G.edge['location_app']['carrier_app']['write-read'] = '[write read]'
G.edge['location_app']['carrier_app']['fill'] = 'red'
G.add_edge('location_app','debuggerd')
G.edge['location_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['location_app']['debuggerd']['fill'] = 'red'
G.add_edge('location_app','debuggerd')
G.edge['location_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('location_app','epmd')
G.edge['location_app']['epmd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['location_app']['epmd']['fill'] = 'red'
G.add_edge('location_app','epmd')
G.edge['location_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('location_app','filtered_google_app')
G.edge['location_app']['filtered_google_app']['write-read'] = '[write read]'
G.edge['location_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('location_app','filtered_untrusted_app')
G.edge['location_app']['filtered_untrusted_app']['write-read'] = '[write read]'
G.edge['location_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('location_app','gad_untrusted_app')
G.edge['location_app']['gad_untrusted_app']['write-read'] = '[write read]'
G.edge['location_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('location_app','ime_app')
G.edge['location_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['location_app']['ime_app']['fill'] = 'red'
G.add_edge('location_app','ime_app')
G.edge['location_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('location_app','irm_app')
G.edge['location_app']['irm_app']['write-read'] = '[write read]'
G.edge['location_app']['irm_app']['fill'] = 'red'
G.add_edge('location_app','knox_system_app')
G.edge['location_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['location_app']['knox_system_app']['fill'] = 'red'
G.add_edge('location_app','knox_system_app')
G.edge['location_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('location_app','knox_untrusted_app')
G.edge['location_app']['knox_untrusted_app']['write-read'] = '[write read]'
G.edge['location_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('location_app','llk_untrusted_app')
G.edge['location_app']['llk_untrusted_app']['write-read'] = '[write read]'
G.edge['location_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('location_app','location_app')
G.edge['location_app']['location_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['location_app']['location_app']['fill'] = 'red'
G.add_edge('location_app','location_app')
G.edge['location_app']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('location_app','mediaserver')
G.edge['location_app']['mediaserver']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['location_app']['mediaserver']['fill'] = 'red'
G.add_edge('location_app','mediaserver')
G.edge['location_app']['mediaserver']['write-read'] = '[open open][open open][setattr getattr][write read][append read]'
G.add_edge('location_app','mediaserver')
G.edge['location_app']['mediaserver']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read]'
G.edge['location_app']['mediaserver']['fill'] = 'red'
G.add_edge('location_app','mediaserver')
G.edge['location_app']['mediaserver']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('location_app','platformappdomain')
G.edge['location_app']['platformappdomain']['write-read'] = '[write read]'
G.edge['location_app']['platformappdomain']['fill'] = 'red'
G.add_edge('location_app','rild')
G.edge['location_app']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['location_app']['rild']['fill'] = 'red'
G.add_edge('location_app','rild')
G.edge['location_app']['rild']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('location_app','s_system_app')
G.edge['location_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['location_app']['s_system_app']['fill'] = 'red'
G.add_edge('location_app','s_system_app')
G.edge['location_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('location_app','syscope_app')
G.edge['location_app']['syscope_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['location_app']['syscope_app']['fill'] = 'red'
G.add_edge('location_app','syscope_app')
G.edge['location_app']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('location_app','system_app')
G.edge['location_app']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['location_app']['system_app']['fill'] = 'red'
G.add_edge('location_app','system_app')
G.edge['location_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('location_app','system_server')
G.edge['location_app']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['location_app']['system_server']['fill'] = 'red'
G.add_edge('location_app','system_server')
G.edge['location_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][write read]'
G.edge['location_app']['system_server']['fill'] = 'red'
G.add_edge('location_app','system_server')
G.edge['location_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][write read][append read]'
G.add_edge('location_app','trustonicpartner_app')
G.edge['location_app']['trustonicpartner_app']['write-read'] = '[write read]'
G.edge['location_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('location_app','umcagent_app')
G.edge['location_app']['umcagent_app']['write-read'] = '[write read]'
G.edge['location_app']['umcagent_app']['fill'] = 'red'
G.add_edge('location_app','untrusted_app')
G.edge['location_app']['untrusted_app']['write-read'] = '[write read]'
G.edge['location_app']['untrusted_app']['fill'] = 'red'
G.add_edge('location_app','vpn_untrusted_app')
G.edge['location_app']['vpn_untrusted_app']['write-read'] = '[write read]'
G.edge['location_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('mediaserver','debuggerd')
G.edge['mediaserver']['debuggerd']['write-read'] = '[open open]'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','ime_app')
G.edge['mediaserver']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','knox_system_app')
G.edge['mediaserver']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','location_app')
G.edge['mediaserver']['location_app']['write-read'] = '[open open]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('mediaserver','rild')
G.edge['mediaserver']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','s_system_app')
G.edge['mediaserver']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','syscope_app')
G.edge['mediaserver']['syscope_app']['write-read'] = '[open open]'
G.add_edge('mediaserver','system_app')
G.edge['mediaserver']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','debuggerd')
G.edge['mediaserver']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('mediaserver','ime_app')
G.edge['mediaserver']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','installd')
G.edge['mediaserver']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('mediaserver','knox_system_app')
G.edge['mediaserver']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','location_app')
G.edge['mediaserver']['location_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('mediaserver','radio')
G.edge['mediaserver']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('mediaserver','rild')
G.edge['mediaserver']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','s_system_app')
G.edge['mediaserver']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','syscope_app')
G.edge['mediaserver']['syscope_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','system_app')
G.edge['mediaserver']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','carrier_app')
G.edge['mediaserver']['carrier_app']['write-read'] = '[write read]'
G.edge['mediaserver']['carrier_app']['fill'] = 'red'
G.add_edge('mediaserver','debuggerd')
G.edge['mediaserver']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['debuggerd']['fill'] = 'red'
G.add_edge('mediaserver','debuggerd')
G.edge['mediaserver']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['mediaserver']['epmd']['fill'] = 'red'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','filtered_google_app')
G.edge['mediaserver']['filtered_google_app']['write-read'] = '[write read]'
G.edge['mediaserver']['filtered_google_app']['fill'] = 'red'
G.add_edge('mediaserver','filtered_untrusted_app')
G.edge['mediaserver']['filtered_untrusted_app']['write-read'] = '[write read]'
G.edge['mediaserver']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('mediaserver','gad_untrusted_app')
G.edge['mediaserver']['gad_untrusted_app']['write-read'] = '[write read]'
G.edge['mediaserver']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('mediaserver','ime_app')
G.edge['mediaserver']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['ime_app']['fill'] = 'red'
G.add_edge('mediaserver','ime_app')
G.edge['mediaserver']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','irm_app')
G.edge['mediaserver']['irm_app']['write-read'] = '[write read]'
G.edge['mediaserver']['irm_app']['fill'] = 'red'
G.add_edge('mediaserver','knox_system_app')
G.edge['mediaserver']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['knox_system_app']['fill'] = 'red'
G.add_edge('mediaserver','knox_system_app')
G.edge['mediaserver']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','knox_untrusted_app')
G.edge['mediaserver']['knox_untrusted_app']['write-read'] = '[write read]'
G.edge['mediaserver']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('mediaserver','llk_untrusted_app')
G.edge['mediaserver']['llk_untrusted_app']['write-read'] = '[write read]'
G.edge['mediaserver']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('mediaserver','location_app')
G.edge['mediaserver']['location_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['location_app']['fill'] = 'red'
G.add_edge('mediaserver','location_app')
G.edge['mediaserver']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['mediaserver']['mediaserver']['fill'] = 'red'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['mediaserver']['mediaserver']['fill'] = 'red'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('mediaserver','platformappdomain')
G.edge['mediaserver']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['mediaserver']['platformappdomain']['fill'] = 'red'
G.add_edge('mediaserver','rild')
G.edge['mediaserver']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['rild']['fill'] = 'red'
G.add_edge('mediaserver','rild')
G.edge['mediaserver']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','s_system_app')
G.edge['mediaserver']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['s_system_app']['fill'] = 'red'
G.add_edge('mediaserver','s_system_app')
G.edge['mediaserver']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','syscope_app')
G.edge['mediaserver']['syscope_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['syscope_app']['fill'] = 'red'
G.add_edge('mediaserver','syscope_app')
G.edge['mediaserver']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','system_app')
G.edge['mediaserver']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['system_app']['fill'] = 'red'
G.add_edge('mediaserver','system_app')
G.edge['mediaserver']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['system_server']['fill'] = 'red'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read]'
G.edge['mediaserver']['system_server']['fill'] = 'red'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read]'
G.add_edge('mediaserver','trustonicpartner_app')
G.edge['mediaserver']['trustonicpartner_app']['write-read'] = '[write read]'
G.edge['mediaserver']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('mediaserver','umcagent_app')
G.edge['mediaserver']['umcagent_app']['write-read'] = '[write read]'
G.edge['mediaserver']['umcagent_app']['fill'] = 'red'
G.add_edge('mediaserver','untrusted_app')
G.edge['mediaserver']['untrusted_app']['write-read'] = '[write read]'
G.edge['mediaserver']['untrusted_app']['fill'] = 'red'
G.add_edge('mediaserver','vpn_untrusted_app')
G.edge['mediaserver']['vpn_untrusted_app']['write-read'] = '[write read]'
G.edge['mediaserver']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('mediaserver','debuggerd')
G.edge['mediaserver']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','ime_app')
G.edge['mediaserver']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','knox_system_app')
G.edge['mediaserver']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','location_app')
G.edge['mediaserver']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open]'
G.add_edge('mediaserver','rild')
G.edge['mediaserver']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','s_system_app')
G.edge['mediaserver']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','syscope_app')
G.edge['mediaserver']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','system_app')
G.edge['mediaserver']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open]'
G.add_edge('mediaserver','debuggerd')
G.edge['mediaserver']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','ime_app')
G.edge['mediaserver']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','installd')
G.edge['mediaserver']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('mediaserver','knox_system_app')
G.edge['mediaserver']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','location_app')
G.edge['mediaserver']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr]'
G.add_edge('mediaserver','radio')
G.edge['mediaserver']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setattr getattr]'
G.add_edge('mediaserver','rild')
G.edge['mediaserver']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','s_system_app')
G.edge['mediaserver']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','syscope_app')
G.edge['mediaserver']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','system_app')
G.edge['mediaserver']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','carrier_app')
G.edge['mediaserver']['carrier_app']['write-read'] = '[write read][write read]'
G.edge['mediaserver']['carrier_app']['fill'] = 'red'
G.add_edge('mediaserver','debuggerd')
G.edge['mediaserver']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['debuggerd']['fill'] = 'red'
G.add_edge('mediaserver','debuggerd')
G.edge['mediaserver']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['epmd']['fill'] = 'red'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','filtered_google_app')
G.edge['mediaserver']['filtered_google_app']['write-read'] = '[write read][write read]'
G.edge['mediaserver']['filtered_google_app']['fill'] = 'red'
G.add_edge('mediaserver','filtered_untrusted_app')
G.edge['mediaserver']['filtered_untrusted_app']['write-read'] = '[write read][write read]'
G.edge['mediaserver']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('mediaserver','gad_untrusted_app')
G.edge['mediaserver']['gad_untrusted_app']['write-read'] = '[write read][write read]'
G.edge['mediaserver']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('mediaserver','ime_app')
G.edge['mediaserver']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['ime_app']['fill'] = 'red'
G.add_edge('mediaserver','ime_app')
G.edge['mediaserver']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','irm_app')
G.edge['mediaserver']['irm_app']['write-read'] = '[write read][write read]'
G.edge['mediaserver']['irm_app']['fill'] = 'red'
G.add_edge('mediaserver','knox_system_app')
G.edge['mediaserver']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['knox_system_app']['fill'] = 'red'
G.add_edge('mediaserver','knox_system_app')
G.edge['mediaserver']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','knox_untrusted_app')
G.edge['mediaserver']['knox_untrusted_app']['write-read'] = '[write read][write read]'
G.edge['mediaserver']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('mediaserver','llk_untrusted_app')
G.edge['mediaserver']['llk_untrusted_app']['write-read'] = '[write read][write read]'
G.edge['mediaserver']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('mediaserver','location_app')
G.edge['mediaserver']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['location_app']['fill'] = 'red'
G.add_edge('mediaserver','location_app')
G.edge['mediaserver']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['mediaserver']['mediaserver']['fill'] = 'red'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['mediaserver']['mediaserver']['fill'] = 'red'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('mediaserver','platformappdomain')
G.edge['mediaserver']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][write read][write read]'
G.edge['mediaserver']['platformappdomain']['fill'] = 'red'
G.add_edge('mediaserver','rild')
G.edge['mediaserver']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['rild']['fill'] = 'red'
G.add_edge('mediaserver','rild')
G.edge['mediaserver']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','s_system_app')
G.edge['mediaserver']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['s_system_app']['fill'] = 'red'
G.add_edge('mediaserver','s_system_app')
G.edge['mediaserver']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','syscope_app')
G.edge['mediaserver']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['syscope_app']['fill'] = 'red'
G.add_edge('mediaserver','syscope_app')
G.edge['mediaserver']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','system_app')
G.edge['mediaserver']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['system_app']['fill'] = 'red'
G.add_edge('mediaserver','system_app')
G.edge['mediaserver']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['system_server']['fill'] = 'red'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read]'
G.edge['mediaserver']['system_server']['fill'] = 'red'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read]'
G.add_edge('mediaserver','trustonicpartner_app')
G.edge['mediaserver']['trustonicpartner_app']['write-read'] = '[write read][write read]'
G.edge['mediaserver']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('mediaserver','umcagent_app')
G.edge['mediaserver']['umcagent_app']['write-read'] = '[write read][write read]'
G.edge['mediaserver']['umcagent_app']['fill'] = 'red'
G.add_edge('mediaserver','untrusted_app')
G.edge['mediaserver']['untrusted_app']['write-read'] = '[write read][write read]'
G.edge['mediaserver']['untrusted_app']['fill'] = 'red'
G.add_edge('mediaserver','vpn_untrusted_app')
G.edge['mediaserver']['vpn_untrusted_app']['write-read'] = '[write read][write read]'
G.edge['mediaserver']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('rild','debuggerd')
G.edge['rild']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','epmd')
G.edge['rild']['epmd']['write-read'] = '[open open]'
G.add_edge('rild','ime_app')
G.edge['rild']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('rild','knox_system_app')
G.edge['rild']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('rild','location_app')
G.edge['rild']['location_app']['write-read'] = '[open open]'
G.add_edge('rild','mediaserver')
G.edge['rild']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('rild','mediaserver')
G.edge['rild']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('rild','s_system_app')
G.edge['rild']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('rild','syscope_app')
G.edge['rild']['syscope_app']['write-read'] = '[open open]'
G.add_edge('rild','system_app')
G.edge['rild']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('rild','debuggerd')
G.edge['rild']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('rild','epmd')
G.edge['rild']['epmd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','ime_app')
G.edge['rild']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('rild','installd')
G.edge['rild']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('rild','knox_system_app')
G.edge['rild']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('rild','location_app')
G.edge['rild']['location_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','mediaserver')
G.edge['rild']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('rild','radio')
G.edge['rild']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('rild','s_system_app')
G.edge['rild']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('rild','syscope_app')
G.edge['rild']['syscope_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','system_app')
G.edge['rild']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('rild','carrier_app')
G.edge['rild']['carrier_app']['write-read'] = '[write read]'
G.edge['rild']['carrier_app']['fill'] = 'red'
G.add_edge('rild','debuggerd')
G.edge['rild']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['rild']['debuggerd']['fill'] = 'red'
G.add_edge('rild','debuggerd')
G.edge['rild']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('rild','epmd')
G.edge['rild']['epmd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['epmd']['fill'] = 'red'
G.add_edge('rild','epmd')
G.edge['rild']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('rild','filtered_google_app')
G.edge['rild']['filtered_google_app']['write-read'] = '[write read]'
G.edge['rild']['filtered_google_app']['fill'] = 'red'
G.add_edge('rild','filtered_untrusted_app')
G.edge['rild']['filtered_untrusted_app']['write-read'] = '[write read]'
G.edge['rild']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('rild','gad_untrusted_app')
G.edge['rild']['gad_untrusted_app']['write-read'] = '[write read]'
G.edge['rild']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('rild','ime_app')
G.edge['rild']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['ime_app']['fill'] = 'red'
G.add_edge('rild','ime_app')
G.edge['rild']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('rild','irm_app')
G.edge['rild']['irm_app']['write-read'] = '[write read]'
G.edge['rild']['irm_app']['fill'] = 'red'
G.add_edge('rild','knox_system_app')
G.edge['rild']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['knox_system_app']['fill'] = 'red'
G.add_edge('rild','knox_system_app')
G.edge['rild']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('rild','knox_untrusted_app')
G.edge['rild']['knox_untrusted_app']['write-read'] = '[write read]'
G.edge['rild']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('rild','llk_untrusted_app')
G.edge['rild']['llk_untrusted_app']['write-read'] = '[write read]'
G.edge['rild']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('rild','location_app')
G.edge['rild']['location_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['location_app']['fill'] = 'red'
G.add_edge('rild','location_app')
G.edge['rild']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('rild','mediaserver')
G.edge['rild']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['rild']['mediaserver']['fill'] = 'red'
G.add_edge('rild','mediaserver')
G.edge['rild']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('rild','mediaserver')
G.edge['rild']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['rild']['mediaserver']['fill'] = 'red'
G.add_edge('rild','mediaserver')
G.edge['rild']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('rild','platformappdomain')
G.edge['rild']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['rild']['platformappdomain']['fill'] = 'red'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['rild']['fill'] = 'red'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('rild','s_system_app')
G.edge['rild']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['s_system_app']['fill'] = 'red'
G.add_edge('rild','s_system_app')
G.edge['rild']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('rild','syscope_app')
G.edge['rild']['syscope_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['syscope_app']['fill'] = 'red'
G.add_edge('rild','syscope_app')
G.edge['rild']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('rild','system_app')
G.edge['rild']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['system_app']['fill'] = 'red'
G.add_edge('rild','system_app')
G.edge['rild']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['system_server']['fill'] = 'red'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read]'
G.edge['rild']['system_server']['fill'] = 'red'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read]'
G.add_edge('rild','trustonicpartner_app')
G.edge['rild']['trustonicpartner_app']['write-read'] = '[write read]'
G.edge['rild']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('rild','umcagent_app')
G.edge['rild']['umcagent_app']['write-read'] = '[write read]'
G.edge['rild']['umcagent_app']['fill'] = 'red'
G.add_edge('rild','untrusted_app')
G.edge['rild']['untrusted_app']['write-read'] = '[write read]'
G.edge['rild']['untrusted_app']['fill'] = 'red'
G.add_edge('rild','vpn_untrusted_app')
G.edge['rild']['vpn_untrusted_app']['write-read'] = '[write read]'
G.edge['rild']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','epmd')
G.edge['s_system_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','knox_system_app')
G.edge['s_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','location_app')
G.edge['s_system_app']['location_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','mediaserver')
G.edge['s_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','mediaserver')
G.edge['s_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('s_system_app','rild')
G.edge['s_system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','syscope_app')
G.edge['s_system_app']['syscope_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','epmd')
G.edge['s_system_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','installd')
G.edge['s_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('s_system_app','knox_system_app')
G.edge['s_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','location_app')
G.edge['s_system_app']['location_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','mediaserver')
G.edge['s_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('s_system_app','radio')
G.edge['s_system_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('s_system_app','rild')
G.edge['s_system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','syscope_app')
G.edge['s_system_app']['syscope_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','carrier_app')
G.edge['s_system_app']['carrier_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['s_system_app']['carrier_app']['fill'] = 'red'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['debuggerd']['fill'] = 'red'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','epmd')
G.edge['s_system_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['epmd']['fill'] = 'red'
G.add_edge('s_system_app','epmd')
G.edge['s_system_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','filtered_google_app')
G.edge['s_system_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['s_system_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('s_system_app','filtered_untrusted_app')
G.edge['s_system_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['s_system_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('s_system_app','gad_untrusted_app')
G.edge['s_system_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['s_system_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['ime_app']['fill'] = 'red'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','irm_app')
G.edge['s_system_app']['irm_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['s_system_app']['irm_app']['fill'] = 'red'
G.add_edge('s_system_app','knox_system_app')
G.edge['s_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['knox_system_app']['fill'] = 'red'
G.add_edge('s_system_app','knox_system_app')
G.edge['s_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','knox_untrusted_app')
G.edge['s_system_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['s_system_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('s_system_app','llk_untrusted_app')
G.edge['s_system_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['s_system_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('s_system_app','location_app')
G.edge['s_system_app']['location_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['location_app']['fill'] = 'red'
G.add_edge('s_system_app','location_app')
G.edge['s_system_app']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','mediaserver')
G.edge['s_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['s_system_app']['mediaserver']['fill'] = 'red'
G.add_edge('s_system_app','mediaserver')
G.edge['s_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','mediaserver')
G.edge['s_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['s_system_app']['mediaserver']['fill'] = 'red'
G.add_edge('s_system_app','mediaserver')
G.edge['s_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('s_system_app','platformappdomain')
G.edge['s_system_app']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['s_system_app']['platformappdomain']['fill'] = 'red'
G.add_edge('s_system_app','rild')
G.edge['s_system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['rild']['fill'] = 'red'
G.add_edge('s_system_app','rild')
G.edge['s_system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','syscope_app')
G.edge['s_system_app']['syscope_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['syscope_app']['fill'] = 'red'
G.add_edge('s_system_app','syscope_app')
G.edge['s_system_app']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['system_app']['fill'] = 'red'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['system_server']['fill'] = 'red'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read]'
G.edge['s_system_app']['system_server']['fill'] = 'red'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read]'
G.add_edge('s_system_app','trustonicpartner_app')
G.edge['s_system_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['s_system_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('s_system_app','umcagent_app')
G.edge['s_system_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['s_system_app']['umcagent_app']['fill'] = 'red'
G.add_edge('s_system_app','untrusted_app')
G.edge['s_system_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['s_system_app']['untrusted_app']['fill'] = 'red'
G.add_edge('s_system_app','vpn_untrusted_app')
G.edge['s_system_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['s_system_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('s_system_app','epmd')
G.edge['s_system_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('s_system_app','installd')
G.edge['s_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('s_system_app','knox_system_app')
G.edge['s_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('s_system_app','location_app')
G.edge['s_system_app']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('s_system_app','mediaserver')
G.edge['s_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr]'
G.add_edge('s_system_app','radio')
G.edge['s_system_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr]'
G.add_edge('s_system_app','rild')
G.edge['s_system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('s_system_app','syscope_app')
G.edge['s_system_app']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr]'
G.add_edge('syscope_app','debuggerd')
G.edge['syscope_app']['debuggerd']['write-read'] = '[open open]'
G.add_edge('syscope_app','epmd')
G.edge['syscope_app']['epmd']['write-read'] = '[open open]'
G.add_edge('syscope_app','ime_app')
G.edge['syscope_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('syscope_app','knox_system_app')
G.edge['syscope_app']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('syscope_app','location_app')
G.edge['syscope_app']['location_app']['write-read'] = '[open open]'
G.add_edge('syscope_app','mediaserver')
G.edge['syscope_app']['mediaserver']['write-read'] = '[open open]'
G.add_edge('syscope_app','mediaserver')
G.edge['syscope_app']['mediaserver']['write-read'] = '[open open][open open]'
G.add_edge('syscope_app','rild')
G.edge['syscope_app']['rild']['write-read'] = '[open open]'
G.add_edge('syscope_app','s_system_app')
G.edge['syscope_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('syscope_app','syscope_app')
G.edge['syscope_app']['syscope_app']['write-read'] = '[open open]'
G.add_edge('syscope_app','system_app')
G.edge['syscope_app']['system_app']['write-read'] = '[open open]'
G.add_edge('syscope_app','system_server')
G.edge['syscope_app']['system_server']['write-read'] = '[open open]'
G.add_edge('syscope_app','debuggerd')
G.edge['syscope_app']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('syscope_app','epmd')
G.edge['syscope_app']['epmd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('syscope_app','ime_app')
G.edge['syscope_app']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('syscope_app','installd')
G.edge['syscope_app']['installd']['write-read'] = '[setattr getattr]'
G.add_edge('syscope_app','knox_system_app')
G.edge['syscope_app']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('syscope_app','location_app')
G.edge['syscope_app']['location_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('syscope_app','mediaserver')
G.edge['syscope_app']['mediaserver']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('syscope_app','radio')
G.edge['syscope_app']['radio']['write-read'] = '[setattr getattr]'
G.add_edge('syscope_app','rild')
G.edge['syscope_app']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('syscope_app','s_system_app')
G.edge['syscope_app']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('syscope_app','syscope_app')
G.edge['syscope_app']['syscope_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('syscope_app','system_app')
G.edge['syscope_app']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('syscope_app','system_server')
G.edge['syscope_app']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('syscope_app','carrier_app')
G.edge['syscope_app']['carrier_app']['write-read'] = '[write read]'
G.edge['syscope_app']['carrier_app']['fill'] = 'red'
G.add_edge('syscope_app','debuggerd')
G.edge['syscope_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['syscope_app']['debuggerd']['fill'] = 'red'
G.add_edge('syscope_app','debuggerd')
G.edge['syscope_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('syscope_app','epmd')
G.edge['syscope_app']['epmd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['syscope_app']['epmd']['fill'] = 'red'
G.add_edge('syscope_app','epmd')
G.edge['syscope_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('syscope_app','filtered_google_app')
G.edge['syscope_app']['filtered_google_app']['write-read'] = '[write read]'
G.edge['syscope_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('syscope_app','filtered_untrusted_app')
G.edge['syscope_app']['filtered_untrusted_app']['write-read'] = '[write read]'
G.edge['syscope_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('syscope_app','gad_untrusted_app')
G.edge['syscope_app']['gad_untrusted_app']['write-read'] = '[write read]'
G.edge['syscope_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('syscope_app','ime_app')
G.edge['syscope_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['syscope_app']['ime_app']['fill'] = 'red'
G.add_edge('syscope_app','ime_app')
G.edge['syscope_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('syscope_app','irm_app')
G.edge['syscope_app']['irm_app']['write-read'] = '[write read]'
G.edge['syscope_app']['irm_app']['fill'] = 'red'
G.add_edge('syscope_app','knox_system_app')
G.edge['syscope_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['syscope_app']['knox_system_app']['fill'] = 'red'
G.add_edge('syscope_app','knox_system_app')
G.edge['syscope_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('syscope_app','knox_untrusted_app')
G.edge['syscope_app']['knox_untrusted_app']['write-read'] = '[write read]'
G.edge['syscope_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('syscope_app','llk_untrusted_app')
G.edge['syscope_app']['llk_untrusted_app']['write-read'] = '[write read]'
G.edge['syscope_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('syscope_app','location_app')
G.edge['syscope_app']['location_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['syscope_app']['location_app']['fill'] = 'red'
G.add_edge('syscope_app','location_app')
G.edge['syscope_app']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('syscope_app','mediaserver')
G.edge['syscope_app']['mediaserver']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['syscope_app']['mediaserver']['fill'] = 'red'
G.add_edge('syscope_app','mediaserver')
G.edge['syscope_app']['mediaserver']['write-read'] = '[open open][open open][setattr getattr][write read][append read]'
G.add_edge('syscope_app','mediaserver')
G.edge['syscope_app']['mediaserver']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read]'
G.edge['syscope_app']['mediaserver']['fill'] = 'red'
G.add_edge('syscope_app','mediaserver')
G.edge['syscope_app']['mediaserver']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('syscope_app','platformappdomain')
G.edge['syscope_app']['platformappdomain']['write-read'] = '[write read]'
G.edge['syscope_app']['platformappdomain']['fill'] = 'red'
G.add_edge('syscope_app','rild')
G.edge['syscope_app']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['syscope_app']['rild']['fill'] = 'red'
G.add_edge('syscope_app','rild')
G.edge['syscope_app']['rild']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('syscope_app','s_system_app')
G.edge['syscope_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['syscope_app']['s_system_app']['fill'] = 'red'
G.add_edge('syscope_app','s_system_app')
G.edge['syscope_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('syscope_app','syscope_app')
G.edge['syscope_app']['syscope_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['syscope_app']['syscope_app']['fill'] = 'red'
G.add_edge('syscope_app','syscope_app')
G.edge['syscope_app']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('syscope_app','system_app')
G.edge['syscope_app']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['syscope_app']['system_app']['fill'] = 'red'
G.add_edge('syscope_app','system_app')
G.edge['syscope_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('syscope_app','system_server')
G.edge['syscope_app']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['syscope_app']['system_server']['fill'] = 'red'
G.add_edge('syscope_app','system_server')
G.edge['syscope_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][write read]'
G.edge['syscope_app']['system_server']['fill'] = 'red'
G.add_edge('syscope_app','system_server')
G.edge['syscope_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][write read][append read]'
G.add_edge('syscope_app','trustonicpartner_app')
G.edge['syscope_app']['trustonicpartner_app']['write-read'] = '[write read]'
G.edge['syscope_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('syscope_app','umcagent_app')
G.edge['syscope_app']['umcagent_app']['write-read'] = '[write read]'
G.edge['syscope_app']['umcagent_app']['fill'] = 'red'
G.add_edge('syscope_app','untrusted_app')
G.edge['syscope_app']['untrusted_app']['write-read'] = '[write read]'
G.edge['syscope_app']['untrusted_app']['fill'] = 'red'
G.add_edge('syscope_app','vpn_untrusted_app')
G.edge['syscope_app']['vpn_untrusted_app']['write-read'] = '[write read]'
G.edge['syscope_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('syscope_app','debuggerd')
G.edge['syscope_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('syscope_app','epmd')
G.edge['syscope_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('syscope_app','ime_app')
G.edge['syscope_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('syscope_app','installd')
G.edge['syscope_app']['installd']['write-read'] = '[setattr getattr][setattr getattr]'
G.add_edge('syscope_app','knox_system_app')
G.edge['syscope_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('syscope_app','location_app')
G.edge['syscope_app']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('syscope_app','mediaserver')
G.edge['syscope_app']['mediaserver']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr]'
G.add_edge('syscope_app','radio')
G.edge['syscope_app']['radio']['write-read'] = '[setattr getattr][setattr getattr]'
G.add_edge('syscope_app','rild')
G.edge['syscope_app']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('syscope_app','s_system_app')
G.edge['syscope_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('syscope_app','syscope_app')
G.edge['syscope_app']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('syscope_app','system_app')
G.edge['syscope_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('syscope_app','system_server')
G.edge['syscope_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][write read][append read][setattr getattr]'
G.add_edge('system_app','debuggerd')
G.edge['system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','epmd')
G.edge['system_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','knox_system_app')
G.edge['system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','location_app')
G.edge['system_app']['location_app']['write-read'] = '[open open]'
G.add_edge('system_app','mediaserver')
G.edge['system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','mediaserver')
G.edge['system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('system_app','rild')
G.edge['system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','syscope_app')
G.edge['system_app']['syscope_app']['write-read'] = '[open open]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','debuggerd')
G.edge['system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_app','epmd')
G.edge['system_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','installd')
G.edge['system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('system_app','knox_system_app')
G.edge['system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','location_app')
G.edge['system_app']['location_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','mediaserver')
G.edge['system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('system_app','radio')
G.edge['system_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('system_app','rild')
G.edge['system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','syscope_app')
G.edge['system_app']['syscope_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','carrier_app')
G.edge['system_app']['carrier_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['system_app']['carrier_app']['fill'] = 'red'
G.add_edge('system_app','debuggerd')
G.edge['system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_app']['debuggerd']['fill'] = 'red'
G.add_edge('system_app','debuggerd')
G.edge['system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','epmd')
G.edge['system_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['epmd']['fill'] = 'red'
G.add_edge('system_app','epmd')
G.edge['system_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','filtered_google_app')
G.edge['system_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['system_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('system_app','filtered_untrusted_app')
G.edge['system_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['system_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('system_app','gad_untrusted_app')
G.edge['system_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['system_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['ime_app']['fill'] = 'red'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','irm_app')
G.edge['system_app']['irm_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['system_app']['irm_app']['fill'] = 'red'
G.add_edge('system_app','knox_system_app')
G.edge['system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['knox_system_app']['fill'] = 'red'
G.add_edge('system_app','knox_system_app')
G.edge['system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','knox_untrusted_app')
G.edge['system_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['system_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('system_app','llk_untrusted_app')
G.edge['system_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['system_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('system_app','location_app')
G.edge['system_app']['location_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['location_app']['fill'] = 'red'
G.add_edge('system_app','location_app')
G.edge['system_app']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_app','mediaserver')
G.edge['system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['system_app']['mediaserver']['fill'] = 'red'
G.add_edge('system_app','mediaserver')
G.edge['system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','mediaserver')
G.edge['system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['system_app']['mediaserver']['fill'] = 'red'
G.add_edge('system_app','mediaserver')
G.edge['system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('system_app','platformappdomain')
G.edge['system_app']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['system_app']['platformappdomain']['fill'] = 'red'
G.add_edge('system_app','rild')
G.edge['system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['rild']['fill'] = 'red'
G.add_edge('system_app','rild')
G.edge['system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['s_system_app']['fill'] = 'red'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','syscope_app')
G.edge['system_app']['syscope_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['syscope_app']['fill'] = 'red'
G.add_edge('system_app','syscope_app')
G.edge['system_app']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['system_app']['fill'] = 'red'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['system_server']['fill'] = 'red'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read]'
G.edge['system_app']['system_server']['fill'] = 'red'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read]'
G.add_edge('system_app','trustonicpartner_app')
G.edge['system_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['system_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('system_app','umcagent_app')
G.edge['system_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['system_app']['umcagent_app']['fill'] = 'red'
G.add_edge('system_app','untrusted_app')
G.edge['system_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['system_app']['untrusted_app']['fill'] = 'red'
G.add_edge('system_app','vpn_untrusted_app')
G.edge['system_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['system_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('system_app','debuggerd')
G.edge['system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('system_app','epmd')
G.edge['system_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('system_app','installd')
G.edge['system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('system_app','knox_system_app')
G.edge['system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('system_app','location_app')
G.edge['system_app']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('system_app','mediaserver')
G.edge['system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr]'
G.add_edge('system_app','radio')
G.edge['system_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr]'
G.add_edge('system_app','rild')
G.edge['system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('system_app','syscope_app')
G.edge['system_app']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr]'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][setattr getattr][open open][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('system_server','knox_system_app')
G.edge['system_server']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('system_server','location_app')
G.edge['system_server']['location_app']['write-read'] = '[setattr getattr]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('system_server','syscope_app')
G.edge['system_server']['syscope_app']['write-read'] = '[setattr getattr]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('system_server','carrier_app')
G.edge['system_server']['carrier_app']['write-read'] = '[write read]'
G.edge['system_server']['carrier_app']['fill'] = 'red'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['system_server']['debuggerd']['fill'] = 'red'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read]'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['system_server']['epmd']['fill'] = 'red'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read]'
G.add_edge('system_server','filtered_google_app')
G.edge['system_server']['filtered_google_app']['write-read'] = '[write read]'
G.edge['system_server']['filtered_google_app']['fill'] = 'red'
G.add_edge('system_server','filtered_untrusted_app')
G.edge['system_server']['filtered_untrusted_app']['write-read'] = '[write read]'
G.edge['system_server']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('system_server','gad_untrusted_app')
G.edge['system_server']['gad_untrusted_app']['write-read'] = '[write read]'
G.edge['system_server']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['system_server']['ime_app']['fill'] = 'red'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read]'
G.add_edge('system_server','irm_app')
G.edge['system_server']['irm_app']['write-read'] = '[write read]'
G.edge['system_server']['irm_app']['fill'] = 'red'
G.add_edge('system_server','knox_system_app')
G.edge['system_server']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['system_server']['knox_system_app']['fill'] = 'red'
G.add_edge('system_server','knox_system_app')
G.edge['system_server']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read]'
G.add_edge('system_server','knox_untrusted_app')
G.edge['system_server']['knox_untrusted_app']['write-read'] = '[write read]'
G.edge['system_server']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('system_server','llk_untrusted_app')
G.edge['system_server']['llk_untrusted_app']['write-read'] = '[write read]'
G.edge['system_server']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('system_server','location_app')
G.edge['system_server']['location_app']['write-read'] = '[setattr getattr][write read]'
G.edge['system_server']['location_app']['fill'] = 'red'
G.add_edge('system_server','location_app')
G.edge['system_server']['location_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['system_server']['mediaserver']['fill'] = 'red'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read]'
G.edge['system_server']['mediaserver']['fill'] = 'red'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read]'
G.add_edge('system_server','platformappdomain')
G.edge['system_server']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['system_server']['platformappdomain']['fill'] = 'red'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['system_server']['rild']['fill'] = 'red'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['system_server']['s_system_app']['fill'] = 'red'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read]'
G.add_edge('system_server','syscope_app')
G.edge['system_server']['syscope_app']['write-read'] = '[setattr getattr][write read]'
G.edge['system_server']['syscope_app']['fill'] = 'red'
G.add_edge('system_server','syscope_app')
G.edge['system_server']['syscope_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['system_server']['system_app']['fill'] = 'red'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read]'
G.add_edge('system_server','trustonicpartner_app')
G.edge['system_server']['trustonicpartner_app']['write-read'] = '[write read]'
G.edge['system_server']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('system_server','umcagent_app')
G.edge['system_server']['umcagent_app']['write-read'] = '[write read]'
G.edge['system_server']['umcagent_app']['fill'] = 'red'
G.add_edge('system_server','untrusted_app')
G.edge['system_server']['untrusted_app']['write-read'] = '[write read]'
G.edge['system_server']['untrusted_app']['fill'] = 'red'
G.add_edge('system_server','vpn_untrusted_app')
G.edge['system_server']['vpn_untrusted_app']['write-read'] = '[write read]'
G.edge['system_server']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','knox_system_app')
G.edge['system_server']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','location_app')
G.edge['system_server']['location_app']['write-read'] = '[setattr getattr][write read][append read][open open]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','syscope_app')
G.edge['system_server']['syscope_app']['write-read'] = '[setattr getattr][write read][append read][open open]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open]'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][setattr getattr][open open][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('system_server','knox_system_app')
G.edge['system_server']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','location_app')
G.edge['system_server']['location_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr]'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','syscope_app')
G.edge['system_server']['syscope_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','carrier_app')
G.edge['system_server']['carrier_app']['write-read'] = '[write read][write read]'
G.edge['system_server']['carrier_app']['fill'] = 'red'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['debuggerd']['fill'] = 'red'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['epmd']['fill'] = 'red'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','filtered_google_app')
G.edge['system_server']['filtered_google_app']['write-read'] = '[write read][write read]'
G.edge['system_server']['filtered_google_app']['fill'] = 'red'
G.add_edge('system_server','filtered_untrusted_app')
G.edge['system_server']['filtered_untrusted_app']['write-read'] = '[write read][write read]'
G.edge['system_server']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('system_server','gad_untrusted_app')
G.edge['system_server']['gad_untrusted_app']['write-read'] = '[write read][write read]'
G.edge['system_server']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['ime_app']['fill'] = 'red'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','irm_app')
G.edge['system_server']['irm_app']['write-read'] = '[write read][write read]'
G.edge['system_server']['irm_app']['fill'] = 'red'
G.add_edge('system_server','knox_system_app')
G.edge['system_server']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['knox_system_app']['fill'] = 'red'
G.add_edge('system_server','knox_system_app')
G.edge['system_server']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','knox_untrusted_app')
G.edge['system_server']['knox_untrusted_app']['write-read'] = '[write read][write read]'
G.edge['system_server']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('system_server','llk_untrusted_app')
G.edge['system_server']['llk_untrusted_app']['write-read'] = '[write read][write read]'
G.edge['system_server']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('system_server','location_app')
G.edge['system_server']['location_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['location_app']['fill'] = 'red'
G.add_edge('system_server','location_app')
G.edge['system_server']['location_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['system_server']['mediaserver']['fill'] = 'red'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['system_server']['mediaserver']['fill'] = 'red'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('system_server','platformappdomain')
G.edge['system_server']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][write read][write read]'
G.edge['system_server']['platformappdomain']['fill'] = 'red'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['rild']['fill'] = 'red'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['s_system_app']['fill'] = 'red'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','syscope_app')
G.edge['system_server']['syscope_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['syscope_app']['fill'] = 'red'
G.add_edge('system_server','syscope_app')
G.edge['system_server']['syscope_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['system_app']['fill'] = 'red'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read]'
G.add_edge('system_server','trustonicpartner_app')
G.edge['system_server']['trustonicpartner_app']['write-read'] = '[write read][write read]'
G.edge['system_server']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('system_server','umcagent_app')
G.edge['system_server']['umcagent_app']['write-read'] = '[write read][write read]'
G.edge['system_server']['umcagent_app']['fill'] = 'red'
G.add_edge('system_server','untrusted_app')
G.edge['system_server']['untrusted_app']['write-read'] = '[write read][write read]'
G.edge['system_server']['untrusted_app']['fill'] = 'red'
G.add_edge('system_server','vpn_untrusted_app')
G.edge['system_server']['vpn_untrusted_app']['write-read'] = '[write read][write read]'
G.edge['system_server']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','debuggerd')
G.edge['trustonicpartner_app']['debuggerd']['write-read'] = '[setattr getattr]'
G.add_edge('trustonicpartner_app','epmd')
G.edge['trustonicpartner_app']['epmd']['write-read'] = '[setattr getattr]'
G.add_edge('trustonicpartner_app','ime_app')
G.edge['trustonicpartner_app']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','installd')
G.edge['trustonicpartner_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('trustonicpartner_app','knox_system_app')
G.edge['trustonicpartner_app']['knox_system_app']['write-read'] = '[setattr getattr]'
G.add_edge('trustonicpartner_app','location_app')
G.edge['trustonicpartner_app']['location_app']['write-read'] = '[setattr getattr]'
G.add_edge('trustonicpartner_app','mediaserver')
G.edge['trustonicpartner_app']['mediaserver']['write-read'] = '[setattr getattr]'
G.add_edge('trustonicpartner_app','radio')
G.edge['trustonicpartner_app']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','rild')
G.edge['trustonicpartner_app']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('trustonicpartner_app','s_system_app')
G.edge['trustonicpartner_app']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','syscope_app')
G.edge['trustonicpartner_app']['syscope_app']['write-read'] = '[setattr getattr]'
G.add_edge('trustonicpartner_app','system_app')
G.edge['trustonicpartner_app']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','system_server')
G.edge['trustonicpartner_app']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('trustonicpartner_app','carrier_app')
G.edge['trustonicpartner_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['carrier_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','debuggerd')
G.edge['trustonicpartner_app']['debuggerd']['write-read'] = '[setattr getattr][write read]'
G.edge['trustonicpartner_app']['debuggerd']['fill'] = 'red'
G.add_edge('trustonicpartner_app','debuggerd')
G.edge['trustonicpartner_app']['debuggerd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','epmd')
G.edge['trustonicpartner_app']['epmd']['write-read'] = '[setattr getattr][write read]'
G.edge['trustonicpartner_app']['epmd']['fill'] = 'red'
G.add_edge('trustonicpartner_app','epmd')
G.edge['trustonicpartner_app']['epmd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','filtered_google_app')
G.edge['trustonicpartner_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','filtered_untrusted_app')
G.edge['trustonicpartner_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','gad_untrusted_app')
G.edge['trustonicpartner_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','ime_app')
G.edge['trustonicpartner_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['ime_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','ime_app')
G.edge['trustonicpartner_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','irm_app')
G.edge['trustonicpartner_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['irm_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','knox_system_app')
G.edge['trustonicpartner_app']['knox_system_app']['write-read'] = '[setattr getattr][write read]'
G.edge['trustonicpartner_app']['knox_system_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','knox_system_app')
G.edge['trustonicpartner_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','knox_untrusted_app')
G.edge['trustonicpartner_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','llk_untrusted_app')
G.edge['trustonicpartner_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','location_app')
G.edge['trustonicpartner_app']['location_app']['write-read'] = '[setattr getattr][write read]'
G.edge['trustonicpartner_app']['location_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','location_app')
G.edge['trustonicpartner_app']['location_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','mediaserver')
G.edge['trustonicpartner_app']['mediaserver']['write-read'] = '[setattr getattr][write read]'
G.edge['trustonicpartner_app']['mediaserver']['fill'] = 'red'
G.add_edge('trustonicpartner_app','mediaserver')
G.edge['trustonicpartner_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','mediaserver')
G.edge['trustonicpartner_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read]'
G.edge['trustonicpartner_app']['mediaserver']['fill'] = 'red'
G.add_edge('trustonicpartner_app','mediaserver')
G.edge['trustonicpartner_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read]'
G.add_edge('trustonicpartner_app','platformappdomain')
G.edge['trustonicpartner_app']['platformappdomain']['write-read'] = '[write read]'
G.edge['trustonicpartner_app']['platformappdomain']['fill'] = 'red'
G.add_edge('trustonicpartner_app','rild')
G.edge['trustonicpartner_app']['rild']['write-read'] = '[setattr getattr][write read]'
G.edge['trustonicpartner_app']['rild']['fill'] = 'red'
G.add_edge('trustonicpartner_app','rild')
G.edge['trustonicpartner_app']['rild']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','s_system_app')
G.edge['trustonicpartner_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['s_system_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','s_system_app')
G.edge['trustonicpartner_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','syscope_app')
G.edge['trustonicpartner_app']['syscope_app']['write-read'] = '[setattr getattr][write read]'
G.edge['trustonicpartner_app']['syscope_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','syscope_app')
G.edge['trustonicpartner_app']['syscope_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','system_app')
G.edge['trustonicpartner_app']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['system_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','system_app')
G.edge['trustonicpartner_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','system_server')
G.edge['trustonicpartner_app']['system_server']['write-read'] = '[setattr getattr][write read]'
G.edge['trustonicpartner_app']['system_server']['fill'] = 'red'
G.add_edge('trustonicpartner_app','system_server')
G.edge['trustonicpartner_app']['system_server']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['trustonicpartner_app']['system_server']['fill'] = 'red'
G.add_edge('trustonicpartner_app','system_server')
G.edge['trustonicpartner_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read]'
G.add_edge('trustonicpartner_app','trustonicpartner_app')
G.edge['trustonicpartner_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','umcagent_app')
G.edge['trustonicpartner_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['umcagent_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','untrusted_app')
G.edge['trustonicpartner_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['untrusted_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','vpn_untrusted_app')
G.edge['trustonicpartner_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('umcagent_app','debuggerd')
G.edge['umcagent_app']['debuggerd']['write-read'] = '[setattr getattr]'
G.add_edge('umcagent_app','epmd')
G.edge['umcagent_app']['epmd']['write-read'] = '[setattr getattr]'
G.add_edge('umcagent_app','ime_app')
G.edge['umcagent_app']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','installd')
G.edge['umcagent_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('umcagent_app','knox_system_app')
G.edge['umcagent_app']['knox_system_app']['write-read'] = '[setattr getattr]'
G.add_edge('umcagent_app','location_app')
G.edge['umcagent_app']['location_app']['write-read'] = '[setattr getattr]'
G.add_edge('umcagent_app','mediaserver')
G.edge['umcagent_app']['mediaserver']['write-read'] = '[setattr getattr]'
G.add_edge('umcagent_app','radio')
G.edge['umcagent_app']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','rild')
G.edge['umcagent_app']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('umcagent_app','s_system_app')
G.edge['umcagent_app']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','syscope_app')
G.edge['umcagent_app']['syscope_app']['write-read'] = '[setattr getattr]'
G.add_edge('umcagent_app','system_app')
G.edge['umcagent_app']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','system_server')
G.edge['umcagent_app']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('umcagent_app','carrier_app')
G.edge['umcagent_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['umcagent_app']['carrier_app']['fill'] = 'red'
G.add_edge('umcagent_app','debuggerd')
G.edge['umcagent_app']['debuggerd']['write-read'] = '[setattr getattr][write read]'
G.edge['umcagent_app']['debuggerd']['fill'] = 'red'
G.add_edge('umcagent_app','debuggerd')
G.edge['umcagent_app']['debuggerd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('umcagent_app','epmd')
G.edge['umcagent_app']['epmd']['write-read'] = '[setattr getattr][write read]'
G.edge['umcagent_app']['epmd']['fill'] = 'red'
G.add_edge('umcagent_app','epmd')
G.edge['umcagent_app']['epmd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('umcagent_app','filtered_google_app')
G.edge['umcagent_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['umcagent_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('umcagent_app','filtered_untrusted_app')
G.edge['umcagent_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['umcagent_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('umcagent_app','gad_untrusted_app')
G.edge['umcagent_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['umcagent_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('umcagent_app','ime_app')
G.edge['umcagent_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['umcagent_app']['ime_app']['fill'] = 'red'
G.add_edge('umcagent_app','ime_app')
G.edge['umcagent_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','irm_app')
G.edge['umcagent_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['umcagent_app']['irm_app']['fill'] = 'red'
G.add_edge('umcagent_app','knox_system_app')
G.edge['umcagent_app']['knox_system_app']['write-read'] = '[setattr getattr][write read]'
G.edge['umcagent_app']['knox_system_app']['fill'] = 'red'
G.add_edge('umcagent_app','knox_system_app')
G.edge['umcagent_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('umcagent_app','knox_untrusted_app')
G.edge['umcagent_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['umcagent_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('umcagent_app','llk_untrusted_app')
G.edge['umcagent_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['umcagent_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('umcagent_app','location_app')
G.edge['umcagent_app']['location_app']['write-read'] = '[setattr getattr][write read]'
G.edge['umcagent_app']['location_app']['fill'] = 'red'
G.add_edge('umcagent_app','location_app')
G.edge['umcagent_app']['location_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('umcagent_app','mediaserver')
G.edge['umcagent_app']['mediaserver']['write-read'] = '[setattr getattr][write read]'
G.edge['umcagent_app']['mediaserver']['fill'] = 'red'
G.add_edge('umcagent_app','mediaserver')
G.edge['umcagent_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('umcagent_app','mediaserver')
G.edge['umcagent_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read]'
G.edge['umcagent_app']['mediaserver']['fill'] = 'red'
G.add_edge('umcagent_app','mediaserver')
G.edge['umcagent_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read]'
G.add_edge('umcagent_app','platformappdomain')
G.edge['umcagent_app']['platformappdomain']['write-read'] = '[write read]'
G.edge['umcagent_app']['platformappdomain']['fill'] = 'red'
G.add_edge('umcagent_app','rild')
G.edge['umcagent_app']['rild']['write-read'] = '[setattr getattr][write read]'
G.edge['umcagent_app']['rild']['fill'] = 'red'
G.add_edge('umcagent_app','rild')
G.edge['umcagent_app']['rild']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('umcagent_app','s_system_app')
G.edge['umcagent_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['umcagent_app']['s_system_app']['fill'] = 'red'
G.add_edge('umcagent_app','s_system_app')
G.edge['umcagent_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','syscope_app')
G.edge['umcagent_app']['syscope_app']['write-read'] = '[setattr getattr][write read]'
G.edge['umcagent_app']['syscope_app']['fill'] = 'red'
G.add_edge('umcagent_app','syscope_app')
G.edge['umcagent_app']['syscope_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('umcagent_app','system_app')
G.edge['umcagent_app']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['umcagent_app']['system_app']['fill'] = 'red'
G.add_edge('umcagent_app','system_app')
G.edge['umcagent_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','system_server')
G.edge['umcagent_app']['system_server']['write-read'] = '[setattr getattr][write read]'
G.edge['umcagent_app']['system_server']['fill'] = 'red'
G.add_edge('umcagent_app','system_server')
G.edge['umcagent_app']['system_server']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['umcagent_app']['system_server']['fill'] = 'red'
G.add_edge('umcagent_app','system_server')
G.edge['umcagent_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read]'
G.add_edge('umcagent_app','trustonicpartner_app')
G.edge['umcagent_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['umcagent_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('umcagent_app','umcagent_app')
G.edge['umcagent_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['umcagent_app']['umcagent_app']['fill'] = 'red'
G.add_edge('umcagent_app','untrusted_app')
G.edge['umcagent_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['umcagent_app']['untrusted_app']['fill'] = 'red'
G.add_edge('umcagent_app','vpn_untrusted_app')
G.edge['umcagent_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['umcagent_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('untrusted_app','debuggerd')
G.edge['untrusted_app']['debuggerd']['write-read'] = '[setattr getattr]'
G.add_edge('untrusted_app','epmd')
G.edge['untrusted_app']['epmd']['write-read'] = '[setattr getattr]'
G.add_edge('untrusted_app','ime_app')
G.edge['untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','installd')
G.edge['untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('untrusted_app','knox_system_app')
G.edge['untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr]'
G.add_edge('untrusted_app','location_app')
G.edge['untrusted_app']['location_app']['write-read'] = '[setattr getattr]'
G.add_edge('untrusted_app','mediaserver')
G.edge['untrusted_app']['mediaserver']['write-read'] = '[setattr getattr]'
G.add_edge('untrusted_app','radio')
G.edge['untrusted_app']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','rild')
G.edge['untrusted_app']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('untrusted_app','s_system_app')
G.edge['untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','syscope_app')
G.edge['untrusted_app']['syscope_app']['write-read'] = '[setattr getattr]'
G.add_edge('untrusted_app','system_app')
G.edge['untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','system_server')
G.edge['untrusted_app']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('untrusted_app','carrier_app')
G.edge['untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusted_app']['carrier_app']['fill'] = 'red'
G.add_edge('untrusted_app','debuggerd')
G.edge['untrusted_app']['debuggerd']['write-read'] = '[setattr getattr][write read]'
G.edge['untrusted_app']['debuggerd']['fill'] = 'red'
G.add_edge('untrusted_app','debuggerd')
G.edge['untrusted_app']['debuggerd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('untrusted_app','epmd')
G.edge['untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read]'
G.edge['untrusted_app']['epmd']['fill'] = 'red'
G.add_edge('untrusted_app','epmd')
G.edge['untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('untrusted_app','filtered_google_app')
G.edge['untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusted_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('untrusted_app','filtered_untrusted_app')
G.edge['untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusted_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('untrusted_app','gad_untrusted_app')
G.edge['untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusted_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('untrusted_app','ime_app')
G.edge['untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusted_app']['ime_app']['fill'] = 'red'
G.add_edge('untrusted_app','ime_app')
G.edge['untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','irm_app')
G.edge['untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusted_app']['irm_app']['fill'] = 'red'
G.add_edge('untrusted_app','knox_system_app')
G.edge['untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr][write read]'
G.edge['untrusted_app']['knox_system_app']['fill'] = 'red'
G.add_edge('untrusted_app','knox_system_app')
G.edge['untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('untrusted_app','knox_untrusted_app')
G.edge['untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusted_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('untrusted_app','llk_untrusted_app')
G.edge['untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusted_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('untrusted_app','location_app')
G.edge['untrusted_app']['location_app']['write-read'] = '[setattr getattr][write read]'
G.edge['untrusted_app']['location_app']['fill'] = 'red'
G.add_edge('untrusted_app','location_app')
G.edge['untrusted_app']['location_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('untrusted_app','mediaserver')
G.edge['untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read]'
G.edge['untrusted_app']['mediaserver']['fill'] = 'red'
G.add_edge('untrusted_app','mediaserver')
G.edge['untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('untrusted_app','mediaserver')
G.edge['untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read]'
G.edge['untrusted_app']['mediaserver']['fill'] = 'red'
G.add_edge('untrusted_app','mediaserver')
G.edge['untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read]'
G.add_edge('untrusted_app','platformappdomain')
G.edge['untrusted_app']['platformappdomain']['write-read'] = '[write read]'
G.edge['untrusted_app']['platformappdomain']['fill'] = 'red'
G.add_edge('untrusted_app','rild')
G.edge['untrusted_app']['rild']['write-read'] = '[setattr getattr][write read]'
G.edge['untrusted_app']['rild']['fill'] = 'red'
G.add_edge('untrusted_app','rild')
G.edge['untrusted_app']['rild']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('untrusted_app','s_system_app')
G.edge['untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusted_app']['s_system_app']['fill'] = 'red'
G.add_edge('untrusted_app','s_system_app')
G.edge['untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','syscope_app')
G.edge['untrusted_app']['syscope_app']['write-read'] = '[setattr getattr][write read]'
G.edge['untrusted_app']['syscope_app']['fill'] = 'red'
G.add_edge('untrusted_app','syscope_app')
G.edge['untrusted_app']['syscope_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('untrusted_app','system_app')
G.edge['untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusted_app']['system_app']['fill'] = 'red'
G.add_edge('untrusted_app','system_app')
G.edge['untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','system_server')
G.edge['untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read]'
G.edge['untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('untrusted_app','system_server')
G.edge['untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('untrusted_app','system_server')
G.edge['untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read]'
G.add_edge('untrusted_app','trustonicpartner_app')
G.edge['untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusted_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('untrusted_app','umcagent_app')
G.edge['untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusted_app']['umcagent_app']['fill'] = 'red'
G.add_edge('untrusted_app','untrusted_app')
G.edge['untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusted_app']['untrusted_app']['fill'] = 'red'
G.add_edge('untrusted_app','vpn_untrusted_app')
G.edge['untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusted_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('untrusteddomain','debuggerd')
G.edge['untrusteddomain']['debuggerd']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','epmd')
G.edge['untrusteddomain']['epmd']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','ime_app')
G.edge['untrusteddomain']['ime_app']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','knox_system_app')
G.edge['untrusteddomain']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','location_app')
G.edge['untrusteddomain']['location_app']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','mediaserver')
G.edge['untrusteddomain']['mediaserver']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','mediaserver')
G.edge['untrusteddomain']['mediaserver']['write-read'] = '[open open][open open]'
G.add_edge('untrusteddomain','rild')
G.edge['untrusteddomain']['rild']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','s_system_app')
G.edge['untrusteddomain']['s_system_app']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','syscope_app')
G.edge['untrusteddomain']['syscope_app']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','system_app')
G.edge['untrusteddomain']['system_app']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusteddomain','debuggerd')
G.edge['untrusteddomain']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusteddomain','epmd')
G.edge['untrusteddomain']['epmd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusteddomain','ime_app')
G.edge['untrusteddomain']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusteddomain','installd')
G.edge['untrusteddomain']['installd']['write-read'] = '[setattr getattr]'
G.add_edge('untrusteddomain','knox_system_app')
G.edge['untrusteddomain']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusteddomain','location_app')
G.edge['untrusteddomain']['location_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusteddomain','mediaserver')
G.edge['untrusteddomain']['mediaserver']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('untrusteddomain','radio')
G.edge['untrusteddomain']['radio']['write-read'] = '[setattr getattr]'
G.add_edge('untrusteddomain','rild')
G.edge['untrusteddomain']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusteddomain','s_system_app')
G.edge['untrusteddomain']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusteddomain','syscope_app')
G.edge['untrusteddomain']['syscope_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusteddomain','system_app')
G.edge['untrusteddomain']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('untrusteddomain','carrier_app')
G.edge['untrusteddomain']['carrier_app']['write-read'] = '[write read]'
G.edge['untrusteddomain']['carrier_app']['fill'] = 'red'
G.add_edge('untrusteddomain','debuggerd')
G.edge['untrusteddomain']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusteddomain']['debuggerd']['fill'] = 'red'
G.add_edge('untrusteddomain','debuggerd')
G.edge['untrusteddomain']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','epmd')
G.edge['untrusteddomain']['epmd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusteddomain']['epmd']['fill'] = 'red'
G.add_edge('untrusteddomain','epmd')
G.edge['untrusteddomain']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','filtered_google_app')
G.edge['untrusteddomain']['filtered_google_app']['write-read'] = '[write read]'
G.edge['untrusteddomain']['filtered_google_app']['fill'] = 'red'
G.add_edge('untrusteddomain','filtered_untrusted_app')
G.edge['untrusteddomain']['filtered_untrusted_app']['write-read'] = '[write read]'
G.edge['untrusteddomain']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('untrusteddomain','gad_untrusted_app')
G.edge['untrusteddomain']['gad_untrusted_app']['write-read'] = '[write read]'
G.edge['untrusteddomain']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('untrusteddomain','ime_app')
G.edge['untrusteddomain']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusteddomain']['ime_app']['fill'] = 'red'
G.add_edge('untrusteddomain','ime_app')
G.edge['untrusteddomain']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','irm_app')
G.edge['untrusteddomain']['irm_app']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['untrusteddomain']['irm_app']['fill'] = 'red'
G.add_edge('untrusteddomain','knox_system_app')
G.edge['untrusteddomain']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusteddomain']['knox_system_app']['fill'] = 'red'
G.add_edge('untrusteddomain','knox_system_app')
G.edge['untrusteddomain']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','knox_untrusted_app')
G.edge['untrusteddomain']['knox_untrusted_app']['write-read'] = '[write read]'
G.edge['untrusteddomain']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('untrusteddomain','llk_untrusted_app')
G.edge['untrusteddomain']['llk_untrusted_app']['write-read'] = '[write read]'
G.edge['untrusteddomain']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('untrusteddomain','location_app')
G.edge['untrusteddomain']['location_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusteddomain']['location_app']['fill'] = 'red'
G.add_edge('untrusteddomain','location_app')
G.edge['untrusteddomain']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','mediaserver')
G.edge['untrusteddomain']['mediaserver']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['mediaserver']['fill'] = 'red'
G.add_edge('untrusteddomain','mediaserver')
G.edge['untrusteddomain']['mediaserver']['write-read'] = '[open open][open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','mediaserver')
G.edge['untrusteddomain']['mediaserver']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read]'
G.edge['untrusteddomain']['mediaserver']['fill'] = 'red'
G.add_edge('untrusteddomain','mediaserver')
G.edge['untrusteddomain']['mediaserver']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('untrusteddomain','platformappdomain')
G.edge['untrusteddomain']['platformappdomain']['write-read'] = '[write read]'
G.edge['untrusteddomain']['platformappdomain']['fill'] = 'red'
G.add_edge('untrusteddomain','rild')
G.edge['untrusteddomain']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusteddomain']['rild']['fill'] = 'red'
G.add_edge('untrusteddomain','rild')
G.edge['untrusteddomain']['rild']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','s_system_app')
G.edge['untrusteddomain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusteddomain']['s_system_app']['fill'] = 'red'
G.add_edge('untrusteddomain','s_system_app')
G.edge['untrusteddomain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','syscope_app')
G.edge['untrusteddomain']['syscope_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusteddomain']['syscope_app']['fill'] = 'red'
G.add_edge('untrusteddomain','syscope_app')
G.edge['untrusteddomain']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','system_app')
G.edge['untrusteddomain']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusteddomain']['system_app']['fill'] = 'red'
G.add_edge('untrusteddomain','system_app')
G.edge['untrusteddomain']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['system_server']['fill'] = 'red'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read]'
G.edge['untrusteddomain']['system_server']['fill'] = 'red'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read]'
G.add_edge('untrusteddomain','trustonicpartner_app')
G.edge['untrusteddomain']['trustonicpartner_app']['write-read'] = '[write read]'
G.edge['untrusteddomain']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('untrusteddomain','umcagent_app')
G.edge['untrusteddomain']['umcagent_app']['write-read'] = '[write read]'
G.edge['untrusteddomain']['umcagent_app']['fill'] = 'red'
G.add_edge('untrusteddomain','untrusted_app')
G.edge['untrusteddomain']['untrusted_app']['write-read'] = '[write read]'
G.edge['untrusteddomain']['untrusted_app']['fill'] = 'red'
G.add_edge('untrusteddomain','vpn_untrusted_app')
G.edge['untrusteddomain']['vpn_untrusted_app']['write-read'] = '[write read]'
G.edge['untrusteddomain']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','debuggerd')
G.edge['vpn_untrusted_app']['debuggerd']['write-read'] = '[setattr getattr]'
G.add_edge('vpn_untrusted_app','epmd')
G.edge['vpn_untrusted_app']['epmd']['write-read'] = '[setattr getattr]'
G.add_edge('vpn_untrusted_app','ime_app')
G.edge['vpn_untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','installd')
G.edge['vpn_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('vpn_untrusted_app','knox_system_app')
G.edge['vpn_untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr]'
G.add_edge('vpn_untrusted_app','location_app')
G.edge['vpn_untrusted_app']['location_app']['write-read'] = '[setattr getattr]'
G.add_edge('vpn_untrusted_app','mediaserver')
G.edge['vpn_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr]'
G.add_edge('vpn_untrusted_app','radio')
G.edge['vpn_untrusted_app']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','rild')
G.edge['vpn_untrusted_app']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('vpn_untrusted_app','s_system_app')
G.edge['vpn_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','syscope_app')
G.edge['vpn_untrusted_app']['syscope_app']['write-read'] = '[setattr getattr]'
G.add_edge('vpn_untrusted_app','system_app')
G.edge['vpn_untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','system_server')
G.edge['vpn_untrusted_app']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('vpn_untrusted_app','carrier_app')
G.edge['vpn_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['carrier_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','debuggerd')
G.edge['vpn_untrusted_app']['debuggerd']['write-read'] = '[setattr getattr][write read]'
G.edge['vpn_untrusted_app']['debuggerd']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','debuggerd')
G.edge['vpn_untrusted_app']['debuggerd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','epmd')
G.edge['vpn_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read]'
G.edge['vpn_untrusted_app']['epmd']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','epmd')
G.edge['vpn_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','filtered_google_app')
G.edge['vpn_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','filtered_untrusted_app')
G.edge['vpn_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','gad_untrusted_app')
G.edge['vpn_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','ime_app')
G.edge['vpn_untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['ime_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','ime_app')
G.edge['vpn_untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','irm_app')
G.edge['vpn_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['irm_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','knox_system_app')
G.edge['vpn_untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr][write read]'
G.edge['vpn_untrusted_app']['knox_system_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','knox_system_app')
G.edge['vpn_untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','knox_untrusted_app')
G.edge['vpn_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','llk_untrusted_app')
G.edge['vpn_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','location_app')
G.edge['vpn_untrusted_app']['location_app']['write-read'] = '[setattr getattr][write read]'
G.edge['vpn_untrusted_app']['location_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','location_app')
G.edge['vpn_untrusted_app']['location_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','mediaserver')
G.edge['vpn_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read]'
G.edge['vpn_untrusted_app']['mediaserver']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','mediaserver')
G.edge['vpn_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','mediaserver')
G.edge['vpn_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read]'
G.edge['vpn_untrusted_app']['mediaserver']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','mediaserver')
G.edge['vpn_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read]'
G.add_edge('vpn_untrusted_app','platformappdomain')
G.edge['vpn_untrusted_app']['platformappdomain']['write-read'] = '[write read]'
G.edge['vpn_untrusted_app']['platformappdomain']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','rild')
G.edge['vpn_untrusted_app']['rild']['write-read'] = '[setattr getattr][write read]'
G.edge['vpn_untrusted_app']['rild']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','rild')
G.edge['vpn_untrusted_app']['rild']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','s_system_app')
G.edge['vpn_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['s_system_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','s_system_app')
G.edge['vpn_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','syscope_app')
G.edge['vpn_untrusted_app']['syscope_app']['write-read'] = '[setattr getattr][write read]'
G.edge['vpn_untrusted_app']['syscope_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','syscope_app')
G.edge['vpn_untrusted_app']['syscope_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','system_app')
G.edge['vpn_untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['system_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','system_app')
G.edge['vpn_untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','system_server')
G.edge['vpn_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read]'
G.edge['vpn_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','system_server')
G.edge['vpn_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['vpn_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','system_server')
G.edge['vpn_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read]'
G.add_edge('vpn_untrusted_app','trustonicpartner_app')
G.edge['vpn_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','umcagent_app')
G.edge['vpn_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['umcagent_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','untrusted_app')
G.edge['vpn_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['untrusted_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','vpn_untrusted_app')
G.edge['vpn_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['vpn_untrusted_app']['fill'] = 'red'
app = Viewer(G)
app.mainloop()