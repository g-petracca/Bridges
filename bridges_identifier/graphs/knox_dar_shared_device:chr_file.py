import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][open open][write read][append read][open open][add_name search][remove_name search][open open]'
G.add_edge('commonplatformappdomain','epmd')
G.edge['commonplatformappdomain']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('commonplatformappdomain','system_server')
G.edge['commonplatformappdomain']['system_server']['write-read'] = '[write read][append read][open open][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('commonplatformappdomain','vold')
G.edge['commonplatformappdomain']['vold']['write-read'] = '[write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open]'
G.add_edge('commonplatformappdomain','carrier_app')
G.edge['commonplatformappdomain']['carrier_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['commonplatformappdomain']['carrier_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][open open][write read][append read][open open][add_name search][remove_name search][open open][write read]'
G.edge['commonplatformappdomain']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('commonplatformappdomain','epmd')
G.edge['commonplatformappdomain']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['commonplatformappdomain']['epmd']['fill'] = 'red'
G.add_edge('commonplatformappdomain','epmd')
G.edge['commonplatformappdomain']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('commonplatformappdomain','filtered_google_app')
G.edge['commonplatformappdomain']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['commonplatformappdomain']['filtered_google_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','filtered_untrusted_app')
G.edge['commonplatformappdomain']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['commonplatformappdomain']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','gad_untrusted_app')
G.edge['commonplatformappdomain']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['commonplatformappdomain']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','irm_app')
G.edge['commonplatformappdomain']['irm_app']['write-read'] = '[open open][setattr getattr][append read][setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['commonplatformappdomain']['irm_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','knox_untrusted_app')
G.edge['commonplatformappdomain']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['commonplatformappdomain']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','llk_untrusted_app')
G.edge['commonplatformappdomain']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['commonplatformappdomain']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','system_server')
G.edge['commonplatformappdomain']['system_server']['write-read'] = '[write read][append read][open open][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['commonplatformappdomain']['system_server']['fill'] = 'red'
G.add_edge('commonplatformappdomain','system_server')
G.edge['commonplatformappdomain']['system_server']['write-read'] = '[write read][append read][open open][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('commonplatformappdomain','trustonicpartner_app')
G.edge['commonplatformappdomain']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['commonplatformappdomain']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','umcagent_app')
G.edge['commonplatformappdomain']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['commonplatformappdomain']['umcagent_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','untrusted_app')
G.edge['commonplatformappdomain']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['commonplatformappdomain']['untrusted_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','vold')
G.edge['commonplatformappdomain']['vold']['write-read'] = '[write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][write read]'
G.edge['commonplatformappdomain']['vold']['fill'] = 'red'
G.add_edge('commonplatformappdomain','vold')
G.edge['commonplatformappdomain']['vold']['write-read'] = '[write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('commonplatformappdomain','vpn_untrusted_app')
G.edge['commonplatformappdomain']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['commonplatformappdomain']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('epmd','commonplatformappdomain')
G.edge['epmd']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('epmd','carrier_app')
G.edge['epmd']['carrier_app']['write-read'] = '[write read][write read]'
G.edge['epmd']['carrier_app']['fill'] = 'red'
G.add_edge('epmd','commonplatformappdomain')
G.edge['epmd']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['epmd']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('epmd','commonplatformappdomain')
G.edge['epmd']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['epmd']['epmd']['fill'] = 'red'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('epmd','filtered_google_app')
G.edge['epmd']['filtered_google_app']['write-read'] = '[write read][write read]'
G.edge['epmd']['filtered_google_app']['fill'] = 'red'
G.add_edge('epmd','filtered_untrusted_app')
G.edge['epmd']['filtered_untrusted_app']['write-read'] = '[write read][write read]'
G.edge['epmd']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('epmd','gad_untrusted_app')
G.edge['epmd']['gad_untrusted_app']['write-read'] = '[write read][write read]'
G.edge['epmd']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('epmd','irm_app')
G.edge['epmd']['irm_app']['write-read'] = '[write read][write read]'
G.edge['epmd']['irm_app']['fill'] = 'red'
G.add_edge('epmd','knox_untrusted_app')
G.edge['epmd']['knox_untrusted_app']['write-read'] = '[write read][write read]'
G.edge['epmd']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('epmd','llk_untrusted_app')
G.edge['epmd']['llk_untrusted_app']['write-read'] = '[write read][write read]'
G.edge['epmd']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['epmd']['system_server']['fill'] = 'red'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('epmd','trustonicpartner_app')
G.edge['epmd']['trustonicpartner_app']['write-read'] = '[write read][write read]'
G.edge['epmd']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('epmd','umcagent_app')
G.edge['epmd']['umcagent_app']['write-read'] = '[write read][write read]'
G.edge['epmd']['umcagent_app']['fill'] = 'red'
G.add_edge('epmd','untrusted_app')
G.edge['epmd']['untrusted_app']['write-read'] = '[write read][write read]'
G.edge['epmd']['untrusted_app']['fill'] = 'red'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['epmd']['vold']['fill'] = 'red'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('epmd','vpn_untrusted_app')
G.edge['epmd']['vpn_untrusted_app']['write-read'] = '[write read][write read]'
G.edge['epmd']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('system_server','commonplatformappdomain')
G.edge['system_server']['commonplatformappdomain']['write-read'] = '[setopt getopt][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('system_server','carrier_app')
G.edge['system_server']['carrier_app']['write-read'] = '[write read][write read][write read]'
G.edge['system_server']['carrier_app']['fill'] = 'red'
G.add_edge('system_server','commonplatformappdomain')
G.edge['system_server']['commonplatformappdomain']['write-read'] = '[setopt getopt][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('system_server','commonplatformappdomain')
G.edge['system_server']['commonplatformappdomain']['write-read'] = '[setopt getopt][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['epmd']['fill'] = 'red'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','filtered_google_app')
G.edge['system_server']['filtered_google_app']['write-read'] = '[write read][write read][write read]'
G.edge['system_server']['filtered_google_app']['fill'] = 'red'
G.add_edge('system_server','filtered_untrusted_app')
G.edge['system_server']['filtered_untrusted_app']['write-read'] = '[write read][write read][write read]'
G.edge['system_server']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('system_server','gad_untrusted_app')
G.edge['system_server']['gad_untrusted_app']['write-read'] = '[write read][write read][write read]'
G.edge['system_server']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('system_server','irm_app')
G.edge['system_server']['irm_app']['write-read'] = '[write read][write read][write read]'
G.edge['system_server']['irm_app']['fill'] = 'red'
G.add_edge('system_server','knox_untrusted_app')
G.edge['system_server']['knox_untrusted_app']['write-read'] = '[write read][write read][write read]'
G.edge['system_server']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('system_server','llk_untrusted_app')
G.edge['system_server']['llk_untrusted_app']['write-read'] = '[write read][write read][write read]'
G.edge['system_server']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','trustonicpartner_app')
G.edge['system_server']['trustonicpartner_app']['write-read'] = '[write read][write read][write read]'
G.edge['system_server']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('system_server','umcagent_app')
G.edge['system_server']['umcagent_app']['write-read'] = '[write read][write read][write read]'
G.edge['system_server']['umcagent_app']['fill'] = 'red'
G.add_edge('system_server','untrusted_app')
G.edge['system_server']['untrusted_app']['write-read'] = '[write read][write read][write read]'
G.edge['system_server']['untrusted_app']['fill'] = 'red'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['vold']['fill'] = 'red'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','vpn_untrusted_app')
G.edge['system_server']['vpn_untrusted_app']['write-read'] = '[write read][write read][write read]'
G.edge['system_server']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('vold','commonplatformappdomain')
G.edge['vold']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','carrier_app')
G.edge['vold']['carrier_app']['write-read'] = '[write read]'
G.edge['vold']['carrier_app']['fill'] = 'red'
G.add_edge('vold','commonplatformappdomain')
G.edge['vold']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['vold']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('vold','commonplatformappdomain')
G.edge['vold']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['vold']['epmd']['fill'] = 'red'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','filtered_google_app')
G.edge['vold']['filtered_google_app']['write-read'] = '[write read]'
G.edge['vold']['filtered_google_app']['fill'] = 'red'
G.add_edge('vold','filtered_untrusted_app')
G.edge['vold']['filtered_untrusted_app']['write-read'] = '[write read]'
G.edge['vold']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('vold','gad_untrusted_app')
G.edge['vold']['gad_untrusted_app']['write-read'] = '[write read]'
G.edge['vold']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('vold','irm_app')
G.edge['vold']['irm_app']['write-read'] = '[write read]'
G.edge['vold']['irm_app']['fill'] = 'red'
G.add_edge('vold','knox_untrusted_app')
G.edge['vold']['knox_untrusted_app']['write-read'] = '[write read]'
G.edge['vold']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('vold','llk_untrusted_app')
G.edge['vold']['llk_untrusted_app']['write-read'] = '[write read]'
G.edge['vold']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['vold']['system_server']['fill'] = 'red'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('vold','trustonicpartner_app')
G.edge['vold']['trustonicpartner_app']['write-read'] = '[write read]'
G.edge['vold']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('vold','umcagent_app')
G.edge['vold']['umcagent_app']['write-read'] = '[write read]'
G.edge['vold']['umcagent_app']['fill'] = 'red'
G.add_edge('vold','untrusted_app')
G.edge['vold']['untrusted_app']['write-read'] = '[write read]'
G.edge['vold']['untrusted_app']['fill'] = 'red'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['vold']['fill'] = 'red'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','vpn_untrusted_app')
G.edge['vold']['vpn_untrusted_app']['write-read'] = '[write read]'
G.edge['vold']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('vold','commonplatformappdomain')
G.edge['vold']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('vold','carrier_app')
G.edge['vold']['carrier_app']['write-read'] = '[write read][write read]'
G.edge['vold']['carrier_app']['fill'] = 'red'
G.add_edge('vold','commonplatformappdomain')
G.edge['vold']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['vold']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('vold','commonplatformappdomain')
G.edge['vold']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['vold']['epmd']['fill'] = 'red'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('vold','filtered_google_app')
G.edge['vold']['filtered_google_app']['write-read'] = '[write read][write read]'
G.edge['vold']['filtered_google_app']['fill'] = 'red'
G.add_edge('vold','filtered_untrusted_app')
G.edge['vold']['filtered_untrusted_app']['write-read'] = '[write read][write read]'
G.edge['vold']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('vold','gad_untrusted_app')
G.edge['vold']['gad_untrusted_app']['write-read'] = '[write read][write read]'
G.edge['vold']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('vold','irm_app')
G.edge['vold']['irm_app']['write-read'] = '[write read][write read]'
G.edge['vold']['irm_app']['fill'] = 'red'
G.add_edge('vold','knox_untrusted_app')
G.edge['vold']['knox_untrusted_app']['write-read'] = '[write read][write read]'
G.edge['vold']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('vold','llk_untrusted_app')
G.edge['vold']['llk_untrusted_app']['write-read'] = '[write read][write read]'
G.edge['vold']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['vold']['system_server']['fill'] = 'red'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('vold','trustonicpartner_app')
G.edge['vold']['trustonicpartner_app']['write-read'] = '[write read][write read]'
G.edge['vold']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('vold','umcagent_app')
G.edge['vold']['umcagent_app']['write-read'] = '[write read][write read]'
G.edge['vold']['umcagent_app']['fill'] = 'red'
G.add_edge('vold','untrusted_app')
G.edge['vold']['untrusted_app']['write-read'] = '[write read][write read]'
G.edge['vold']['untrusted_app']['fill'] = 'red'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['vold']['vold']['fill'] = 'red'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('vold','vpn_untrusted_app')
G.edge['vold']['vpn_untrusted_app']['write-read'] = '[write read][write read]'
G.edge['vold']['vpn_untrusted_app']['fill'] = 'red'
app = Viewer(G)
app.mainloop()