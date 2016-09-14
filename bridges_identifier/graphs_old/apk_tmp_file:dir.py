import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('carrier_app','platform_app')
G.edge['carrier_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('carrier_app','s_platform_app')
G.edge['carrier_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('carrier_app','system_server')
G.edge['carrier_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('carrier_app','system_server')
G.edge['carrier_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('carrier_app','platform_app')
G.edge['carrier_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['carrier_app']['platform_app']['fill'] = 'red'
G.add_edge('carrier_app','s_platform_app')
G.edge['carrier_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['carrier_app']['s_platform_app']['fill'] = 'red'
G.add_edge('carrier_app','system_server')
G.edge['carrier_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['carrier_app']['system_server']['fill'] = 'red'
G.add_edge('carrier_app','platform_app')
G.edge['carrier_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('carrier_app','platform_app')
G.edge['carrier_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('carrier_app','s_platform_app')
G.edge['carrier_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('carrier_app','s_platform_app')
G.edge['carrier_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('carrier_app','system_server')
G.edge['carrier_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('carrier_app','system_server')
G.edge['carrier_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('filtered_google_app','platform_app')
G.edge['filtered_google_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_google_app','s_platform_app')
G.edge['filtered_google_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_google_app','system_server')
G.edge['filtered_google_app']['system_server']['write-read'] = '[setattr getattr][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_google_app','system_server')
G.edge['filtered_google_app']['system_server']['write-read'] = '[setattr getattr][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('filtered_google_app','platform_app')
G.edge['filtered_google_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_google_app']['platform_app']['fill'] = 'red'
G.add_edge('filtered_google_app','s_platform_app')
G.edge['filtered_google_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_google_app']['s_platform_app']['fill'] = 'red'
G.add_edge('filtered_google_app','system_server')
G.edge['filtered_google_app']['system_server']['write-read'] = '[setattr getattr][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['filtered_google_app']['system_server']['fill'] = 'red'
G.add_edge('filtered_google_app','platform_app')
G.edge['filtered_google_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('filtered_google_app','platform_app')
G.edge['filtered_google_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('filtered_google_app','s_platform_app')
G.edge['filtered_google_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('filtered_google_app','s_platform_app')
G.edge['filtered_google_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('filtered_google_app','system_server')
G.edge['filtered_google_app']['system_server']['write-read'] = '[setattr getattr][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('filtered_google_app','system_server')
G.edge['filtered_google_app']['system_server']['write-read'] = '[setattr getattr][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('filtered_untrusted_app','platform_app')
G.edge['filtered_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_untrusted_app','s_platform_app')
G.edge['filtered_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_untrusted_app','system_server')
G.edge['filtered_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_untrusted_app','system_server')
G.edge['filtered_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','platform_app')
G.edge['filtered_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_untrusted_app']['platform_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','s_platform_app')
G.edge['filtered_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_untrusted_app']['s_platform_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','system_server')
G.edge['filtered_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','platform_app')
G.edge['filtered_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('filtered_untrusted_app','platform_app')
G.edge['filtered_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('filtered_untrusted_app','s_platform_app')
G.edge['filtered_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('filtered_untrusted_app','s_platform_app')
G.edge['filtered_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('filtered_untrusted_app','system_server')
G.edge['filtered_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('filtered_untrusted_app','system_server')
G.edge['filtered_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('gad_untrusted_app','platform_app')
G.edge['gad_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('gad_untrusted_app','s_platform_app')
G.edge['gad_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('gad_untrusted_app','system_server')
G.edge['gad_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('gad_untrusted_app','system_server')
G.edge['gad_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('gad_untrusted_app','platform_app')
G.edge['gad_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['gad_untrusted_app']['platform_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','s_platform_app')
G.edge['gad_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['gad_untrusted_app']['s_platform_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','system_server')
G.edge['gad_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('gad_untrusted_app','platform_app')
G.edge['gad_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('gad_untrusted_app','platform_app')
G.edge['gad_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('gad_untrusted_app','s_platform_app')
G.edge['gad_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('gad_untrusted_app','s_platform_app')
G.edge['gad_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('gad_untrusted_app','system_server')
G.edge['gad_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('gad_untrusted_app','system_server')
G.edge['gad_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('irm_app','platform_app')
G.edge['irm_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('irm_app','s_platform_app')
G.edge['irm_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('irm_app','system_server')
G.edge['irm_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('irm_app','system_server')
G.edge['irm_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('irm_app','platform_app')
G.edge['irm_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['irm_app']['platform_app']['fill'] = 'red'
G.add_edge('irm_app','s_platform_app')
G.edge['irm_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['irm_app']['s_platform_app']['fill'] = 'red'
G.add_edge('irm_app','system_server')
G.edge['irm_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['irm_app']['system_server']['fill'] = 'red'
G.add_edge('irm_app','platform_app')
G.edge['irm_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('irm_app','platform_app')
G.edge['irm_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('irm_app','s_platform_app')
G.edge['irm_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('irm_app','s_platform_app')
G.edge['irm_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('irm_app','system_server')
G.edge['irm_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('irm_app','system_server')
G.edge['irm_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('knox_untrusted_app','platform_app')
G.edge['knox_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_untrusted_app','s_platform_app')
G.edge['knox_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_untrusted_app','system_server')
G.edge['knox_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_untrusted_app','system_server')
G.edge['knox_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('knox_untrusted_app','platform_app')
G.edge['knox_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['knox_untrusted_app']['platform_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','s_platform_app')
G.edge['knox_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['knox_untrusted_app']['s_platform_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','system_server')
G.edge['knox_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('knox_untrusted_app','platform_app')
G.edge['knox_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('knox_untrusted_app','platform_app')
G.edge['knox_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('knox_untrusted_app','s_platform_app')
G.edge['knox_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('knox_untrusted_app','s_platform_app')
G.edge['knox_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('knox_untrusted_app','system_server')
G.edge['knox_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('knox_untrusted_app','system_server')
G.edge['knox_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('llk_untrusted_app','platform_app')
G.edge['llk_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('llk_untrusted_app','s_platform_app')
G.edge['llk_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('llk_untrusted_app','system_server')
G.edge['llk_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('llk_untrusted_app','system_server')
G.edge['llk_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('llk_untrusted_app','platform_app')
G.edge['llk_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['llk_untrusted_app']['platform_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','s_platform_app')
G.edge['llk_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['llk_untrusted_app']['s_platform_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','system_server')
G.edge['llk_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('llk_untrusted_app','platform_app')
G.edge['llk_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('llk_untrusted_app','platform_app')
G.edge['llk_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('llk_untrusted_app','s_platform_app')
G.edge['llk_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('llk_untrusted_app','s_platform_app')
G.edge['llk_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('llk_untrusted_app','system_server')
G.edge['llk_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('llk_untrusted_app','system_server')
G.edge['llk_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('platform_app','platform_app')
G.edge['platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('platform_app','s_platform_app')
G.edge['platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('platform_app','system_server')
G.edge['platform_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('platform_app','system_server')
G.edge['platform_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('platform_app','platform_app')
G.edge['platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['platform_app']['platform_app']['fill'] = 'red'
G.add_edge('platform_app','s_platform_app')
G.edge['platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['platform_app']['s_platform_app']['fill'] = 'red'
G.add_edge('platform_app','system_server')
G.edge['platform_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['platform_app']['system_server']['fill'] = 'red'
G.add_edge('platform_app','platform_app')
G.edge['platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('platform_app','platform_app')
G.edge['platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('platform_app','s_platform_app')
G.edge['platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('platform_app','s_platform_app')
G.edge['platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('platform_app','system_server')
G.edge['platform_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('platform_app','system_server')
G.edge['platform_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_platform_app','platform_app')
G.edge['s_platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_platform_app','s_platform_app')
G.edge['s_platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_platform_app','system_server')
G.edge['s_platform_app']['system_server']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_platform_app','system_server')
G.edge['s_platform_app']['system_server']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_platform_app','platform_app')
G.edge['s_platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['s_platform_app']['platform_app']['fill'] = 'red'
G.add_edge('s_platform_app','s_platform_app')
G.edge['s_platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['s_platform_app']['s_platform_app']['fill'] = 'red'
G.add_edge('s_platform_app','system_server')
G.edge['s_platform_app']['system_server']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_platform_app']['system_server']['fill'] = 'red'
G.add_edge('s_platform_app','platform_app')
G.edge['s_platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('s_platform_app','platform_app')
G.edge['s_platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('s_platform_app','s_platform_app')
G.edge['s_platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('s_platform_app','s_platform_app')
G.edge['s_platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('s_platform_app','system_server')
G.edge['s_platform_app']['system_server']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_platform_app','system_server')
G.edge['s_platform_app']['system_server']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom]'
G.add_edge('system_server','platform_app')
G.edge['system_server']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','s_platform_app')
G.edge['system_server']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr]'
G.add_edge('system_server','platform_app')
G.edge['system_server']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['system_server']['platform_app']['fill'] = 'red'
G.add_edge('system_server','s_platform_app')
G.edge['system_server']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['system_server']['s_platform_app']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','platform_app')
G.edge['system_server']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('system_server','platform_app')
G.edge['system_server']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('system_server','s_platform_app')
G.edge['system_server']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('system_server','s_platform_app')
G.edge['system_server']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('trustonicpartner_app','platform_app')
G.edge['trustonicpartner_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('trustonicpartner_app','s_platform_app')
G.edge['trustonicpartner_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('trustonicpartner_app','system_server')
G.edge['trustonicpartner_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('trustonicpartner_app','system_server')
G.edge['trustonicpartner_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('trustonicpartner_app','platform_app')
G.edge['trustonicpartner_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['trustonicpartner_app']['platform_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','s_platform_app')
G.edge['trustonicpartner_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['trustonicpartner_app']['s_platform_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','system_server')
G.edge['trustonicpartner_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['system_server']['fill'] = 'red'
G.add_edge('trustonicpartner_app','platform_app')
G.edge['trustonicpartner_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('trustonicpartner_app','platform_app')
G.edge['trustonicpartner_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('trustonicpartner_app','s_platform_app')
G.edge['trustonicpartner_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('trustonicpartner_app','s_platform_app')
G.edge['trustonicpartner_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('trustonicpartner_app','system_server')
G.edge['trustonicpartner_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('trustonicpartner_app','system_server')
G.edge['trustonicpartner_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('umcagent_app','platform_app')
G.edge['umcagent_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('umcagent_app','s_platform_app')
G.edge['umcagent_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('umcagent_app','system_server')
G.edge['umcagent_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('umcagent_app','system_server')
G.edge['umcagent_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('umcagent_app','platform_app')
G.edge['umcagent_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['umcagent_app']['platform_app']['fill'] = 'red'
G.add_edge('umcagent_app','s_platform_app')
G.edge['umcagent_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['umcagent_app']['s_platform_app']['fill'] = 'red'
G.add_edge('umcagent_app','system_server')
G.edge['umcagent_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['umcagent_app']['system_server']['fill'] = 'red'
G.add_edge('umcagent_app','platform_app')
G.edge['umcagent_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('umcagent_app','platform_app')
G.edge['umcagent_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('umcagent_app','s_platform_app')
G.edge['umcagent_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('umcagent_app','s_platform_app')
G.edge['umcagent_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('umcagent_app','system_server')
G.edge['umcagent_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('umcagent_app','system_server')
G.edge['umcagent_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('untrusted_app','platform_app')
G.edge['untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusted_app','s_platform_app')
G.edge['untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusted_app','system_server')
G.edge['untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusted_app','system_server')
G.edge['untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('untrusted_app','platform_app')
G.edge['untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['untrusted_app']['platform_app']['fill'] = 'red'
G.add_edge('untrusted_app','s_platform_app')
G.edge['untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['untrusted_app']['s_platform_app']['fill'] = 'red'
G.add_edge('untrusted_app','system_server')
G.edge['untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('untrusted_app','platform_app')
G.edge['untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('untrusted_app','platform_app')
G.edge['untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('untrusted_app','s_platform_app')
G.edge['untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('untrusted_app','s_platform_app')
G.edge['untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('untrusted_app','system_server')
G.edge['untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('untrusted_app','system_server')
G.edge['untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vpn_untrusted_app','platform_app')
G.edge['vpn_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('vpn_untrusted_app','s_platform_app')
G.edge['vpn_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('vpn_untrusted_app','system_server')
G.edge['vpn_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vpn_untrusted_app','system_server')
G.edge['vpn_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','platform_app')
G.edge['vpn_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['vpn_untrusted_app']['platform_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','s_platform_app')
G.edge['vpn_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['vpn_untrusted_app']['s_platform_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','system_server')
G.edge['vpn_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','platform_app')
G.edge['vpn_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('vpn_untrusted_app','platform_app')
G.edge['vpn_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('vpn_untrusted_app','s_platform_app')
G.edge['vpn_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('vpn_untrusted_app','s_platform_app')
G.edge['vpn_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('vpn_untrusted_app','system_server')
G.edge['vpn_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('vpn_untrusted_app','system_server')
G.edge['vpn_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()