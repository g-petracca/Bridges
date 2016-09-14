import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('at_distributor','at_distributor')
G.edge['at_distributor']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','charon')
G.edge['at_distributor']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','domain')
G.edge['at_distributor']['domain']['write-read'] = '[write read][open open]'
G.add_edge('at_distributor','hostapd')
G.edge['at_distributor']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','ime_app')
G.edge['at_distributor']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('at_distributor','init_shell')
G.edge['at_distributor']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','shell')
G.edge['at_distributor']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','s_system_app')
G.edge['at_distributor']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','system_app')
G.edge['at_distributor']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','vmwared')
G.edge['at_distributor']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','at_distributor')
G.edge['at_distributor']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('at_distributor','charon')
G.edge['at_distributor']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('at_distributor','hostapd')
G.edge['at_distributor']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('at_distributor','ime_app')
G.edge['at_distributor']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('at_distributor','init_shell')
G.edge['at_distributor']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('at_distributor','shell')
G.edge['at_distributor']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('at_distributor','s_system_app')
G.edge['at_distributor']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('at_distributor','system_app')
G.edge['at_distributor']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('at_distributor','vmwared')
G.edge['at_distributor']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('at_distributor','at_distributor')
G.edge['at_distributor']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['at_distributor']['at_distributor']['fill'] = 'red'
G.add_edge('at_distributor','at_distributor')
G.edge['at_distributor']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('at_distributor','charon')
G.edge['at_distributor']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['at_distributor']['charon']['fill'] = 'red'
G.add_edge('at_distributor','charon')
G.edge['at_distributor']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('at_distributor','domain')
G.edge['at_distributor']['domain']['write-read'] = '[write read][open open][write read]'
G.edge['at_distributor']['domain']['fill'] = 'red'
G.add_edge('at_distributor','domain')
G.edge['at_distributor']['domain']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('at_distributor','hostapd')
G.edge['at_distributor']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['at_distributor']['hostapd']['fill'] = 'red'
G.add_edge('at_distributor','hostapd')
G.edge['at_distributor']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('at_distributor','ime_app')
G.edge['at_distributor']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['at_distributor']['ime_app']['fill'] = 'red'
G.add_edge('at_distributor','ime_app')
G.edge['at_distributor']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('at_distributor','init_shell')
G.edge['at_distributor']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['at_distributor']['init_shell']['fill'] = 'red'
G.add_edge('at_distributor','init_shell')
G.edge['at_distributor']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('at_distributor','shell')
G.edge['at_distributor']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['at_distributor']['shell']['fill'] = 'red'
G.add_edge('at_distributor','shell')
G.edge['at_distributor']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('at_distributor','s_system_app')
G.edge['at_distributor']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['at_distributor']['s_system_app']['fill'] = 'red'
G.add_edge('at_distributor','s_system_app')
G.edge['at_distributor']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('at_distributor','system_app')
G.edge['at_distributor']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['at_distributor']['system_app']['fill'] = 'red'
G.add_edge('at_distributor','system_app')
G.edge['at_distributor']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('at_distributor','vmwared')
G.edge['at_distributor']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['at_distributor']['vmwared']['fill'] = 'red'
G.add_edge('at_distributor','vmwared')
G.edge['at_distributor']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('charon','at_distributor')
G.edge['charon']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('charon','domain')
G.edge['charon']['domain']['write-read'] = '[write read][open open]'
G.add_edge('charon','hostapd')
G.edge['charon']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('charon','ime_app')
G.edge['charon']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('charon','init_shell')
G.edge['charon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('charon','shell')
G.edge['charon']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('charon','s_system_app')
G.edge['charon']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('charon','system_app')
G.edge['charon']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('charon','vmwared')
G.edge['charon']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('charon','at_distributor')
G.edge['charon']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('charon','hostapd')
G.edge['charon']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('charon','ime_app')
G.edge['charon']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('charon','init_shell')
G.edge['charon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('charon','shell')
G.edge['charon']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('charon','s_system_app')
G.edge['charon']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('charon','system_app')
G.edge['charon']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('charon','vmwared')
G.edge['charon']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('charon','at_distributor')
G.edge['charon']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['charon']['at_distributor']['fill'] = 'red'
G.add_edge('charon','at_distributor')
G.edge['charon']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['charon']['charon']['fill'] = 'red'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('charon','domain')
G.edge['charon']['domain']['write-read'] = '[write read][open open][write read]'
G.edge['charon']['domain']['fill'] = 'red'
G.add_edge('charon','domain')
G.edge['charon']['domain']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('charon','hostapd')
G.edge['charon']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['charon']['hostapd']['fill'] = 'red'
G.add_edge('charon','hostapd')
G.edge['charon']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('charon','ime_app')
G.edge['charon']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['charon']['ime_app']['fill'] = 'red'
G.add_edge('charon','ime_app')
G.edge['charon']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('charon','init_shell')
G.edge['charon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['charon']['init_shell']['fill'] = 'red'
G.add_edge('charon','init_shell')
G.edge['charon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('charon','shell')
G.edge['charon']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['charon']['shell']['fill'] = 'red'
G.add_edge('charon','shell')
G.edge['charon']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('charon','s_system_app')
G.edge['charon']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['charon']['s_system_app']['fill'] = 'red'
G.add_edge('charon','s_system_app')
G.edge['charon']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('charon','system_app')
G.edge['charon']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['charon']['system_app']['fill'] = 'red'
G.add_edge('charon','system_app')
G.edge['charon']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('charon','vmwared')
G.edge['charon']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['charon']['vmwared']['fill'] = 'red'
G.add_edge('charon','vmwared')
G.edge['charon']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('domain','at_distributor')
G.edge['domain']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][open open]'
G.add_edge('domain','charon')
G.edge['domain']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('domain','hostapd')
G.edge['domain']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('domain','ime_app')
G.edge['domain']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][write read][append read][open open]'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open]'
G.add_edge('domain','shell')
G.edge['domain']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('domain','s_system_app')
G.edge['domain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][add_name search][remove_name search][open open][write read][append read][write read][append read][open open]'
G.add_edge('domain','system_app')
G.edge['domain']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][add_name search][remove_name search][open open][write read][append read][write read][append read][open open]'
G.add_edge('domain','vmwared')
G.edge['domain']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('domain','at_distributor')
G.edge['domain']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('domain','charon')
G.edge['domain']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('domain','hostapd')
G.edge['domain']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('domain','ime_app')
G.edge['domain']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][write read][append read][open open][setattr getattr]'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('domain','shell')
G.edge['domain']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('domain','s_system_app')
G.edge['domain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][add_name search][remove_name search][open open][write read][append read][write read][append read][open open][setattr getattr]'
G.add_edge('domain','system_app')
G.edge['domain']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][add_name search][remove_name search][open open][write read][append read][write read][append read][open open][setattr getattr]'
G.add_edge('domain','vmwared')
G.edge['domain']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('domain','at_distributor')
G.edge['domain']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['domain']['at_distributor']['fill'] = 'red'
G.add_edge('domain','at_distributor')
G.edge['domain']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('domain','charon')
G.edge['domain']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['domain']['charon']['fill'] = 'red'
G.add_edge('domain','charon')
G.edge['domain']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['domain']['domain']['fill'] = 'red'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('domain','hostapd')
G.edge['domain']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['domain']['hostapd']['fill'] = 'red'
G.add_edge('domain','hostapd')
G.edge['domain']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('domain','ime_app')
G.edge['domain']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read]'
G.edge['domain']['ime_app']['fill'] = 'red'
G.add_edge('domain','ime_app')
G.edge['domain']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['domain']['init_shell']['fill'] = 'red'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('domain','shell')
G.edge['domain']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['domain']['shell']['fill'] = 'red'
G.add_edge('domain','shell')
G.edge['domain']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('domain','s_system_app')
G.edge['domain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][add_name search][remove_name search][open open][write read][append read][write read][append read][open open][setattr getattr][write read]'
G.edge['domain']['s_system_app']['fill'] = 'red'
G.add_edge('domain','s_system_app')
G.edge['domain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][add_name search][remove_name search][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('domain','system_app')
G.edge['domain']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][add_name search][remove_name search][open open][write read][append read][write read][append read][open open][setattr getattr][write read]'
G.edge['domain']['system_app']['fill'] = 'red'
G.add_edge('domain','system_app')
G.edge['domain']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][add_name search][remove_name search][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('domain','vmwared')
G.edge['domain']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['domain']['vmwared']['fill'] = 'red'
G.add_edge('domain','vmwared')
G.edge['domain']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('hostapd','at_distributor')
G.edge['hostapd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('hostapd','charon')
G.edge['hostapd']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('hostapd','domain')
G.edge['hostapd']['domain']['write-read'] = '[write read][open open]'
G.add_edge('hostapd','hostapd')
G.edge['hostapd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('hostapd','ime_app')
G.edge['hostapd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open]'
G.add_edge('hostapd','init_shell')
G.edge['hostapd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('hostapd','shell')
G.edge['hostapd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('hostapd','s_system_app')
G.edge['hostapd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('hostapd','system_app')
G.edge['hostapd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('hostapd','vmwared')
G.edge['hostapd']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('hostapd','at_distributor')
G.edge['hostapd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('hostapd','charon')
G.edge['hostapd']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('hostapd','hostapd')
G.edge['hostapd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('hostapd','ime_app')
G.edge['hostapd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr]'
G.add_edge('hostapd','init_shell')
G.edge['hostapd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('hostapd','shell')
G.edge['hostapd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('hostapd','s_system_app')
G.edge['hostapd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('hostapd','system_app')
G.edge['hostapd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('hostapd','vmwared')
G.edge['hostapd']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('hostapd','at_distributor')
G.edge['hostapd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['hostapd']['at_distributor']['fill'] = 'red'
G.add_edge('hostapd','at_distributor')
G.edge['hostapd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('hostapd','charon')
G.edge['hostapd']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['hostapd']['charon']['fill'] = 'red'
G.add_edge('hostapd','charon')
G.edge['hostapd']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('hostapd','domain')
G.edge['hostapd']['domain']['write-read'] = '[write read][open open][write read]'
G.edge['hostapd']['domain']['fill'] = 'red'
G.add_edge('hostapd','domain')
G.edge['hostapd']['domain']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('hostapd','hostapd')
G.edge['hostapd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['hostapd']['hostapd']['fill'] = 'red'
G.add_edge('hostapd','hostapd')
G.edge['hostapd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('hostapd','ime_app')
G.edge['hostapd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read]'
G.edge['hostapd']['ime_app']['fill'] = 'red'
G.add_edge('hostapd','ime_app')
G.edge['hostapd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('hostapd','init_shell')
G.edge['hostapd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['hostapd']['init_shell']['fill'] = 'red'
G.add_edge('hostapd','init_shell')
G.edge['hostapd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('hostapd','shell')
G.edge['hostapd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['hostapd']['shell']['fill'] = 'red'
G.add_edge('hostapd','shell')
G.edge['hostapd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('hostapd','s_system_app')
G.edge['hostapd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['hostapd']['s_system_app']['fill'] = 'red'
G.add_edge('hostapd','s_system_app')
G.edge['hostapd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('hostapd','system_app')
G.edge['hostapd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['hostapd']['system_app']['fill'] = 'red'
G.add_edge('hostapd','system_app')
G.edge['hostapd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('hostapd','vmwared')
G.edge['hostapd']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['hostapd']['vmwared']['fill'] = 'red'
G.add_edge('hostapd','vmwared')
G.edge['hostapd']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','at_distributor')
G.edge['ime_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','charon')
G.edge['ime_app']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','domain')
G.edge['ime_app']['domain']['write-read'] = '[write read][write read][append read][open open]'
G.add_edge('ime_app','hostapd')
G.edge['ime_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','shell')
G.edge['ime_app']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('ime_app','vmwared')
G.edge['ime_app']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','at_distributor')
G.edge['ime_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ime_app','charon')
G.edge['ime_app']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ime_app','hostapd')
G.edge['ime_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','shell')
G.edge['ime_app']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','vmwared')
G.edge['ime_app']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ime_app','at_distributor')
G.edge['ime_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ime_app']['at_distributor']['fill'] = 'red'
G.add_edge('ime_app','at_distributor')
G.edge['ime_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','charon')
G.edge['ime_app']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ime_app']['charon']['fill'] = 'red'
G.add_edge('ime_app','charon')
G.edge['ime_app']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','domain')
G.edge['ime_app']['domain']['write-read'] = '[write read][write read][append read][open open][write read]'
G.edge['ime_app']['domain']['fill'] = 'red'
G.add_edge('ime_app','domain')
G.edge['ime_app']['domain']['write-read'] = '[write read][write read][append read][open open][write read][append read]'
G.add_edge('ime_app','hostapd')
G.edge['ime_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ime_app']['hostapd']['fill'] = 'red'
G.add_edge('ime_app','hostapd')
G.edge['ime_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['ime_app']['fill'] = 'red'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['init_shell']['fill'] = 'red'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','shell')
G.edge['ime_app']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ime_app']['shell']['fill'] = 'red'
G.add_edge('ime_app','shell')
G.edge['ime_app']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['s_system_app']['fill'] = 'red'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['system_app']['fill'] = 'red'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','vmwared')
G.edge['ime_app']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ime_app']['vmwared']['fill'] = 'red'
G.add_edge('ime_app','vmwared')
G.edge['ime_app']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','at_distributor')
G.edge['init_shell']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','charon')
G.edge['init_shell']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','domain')
G.edge['init_shell']['domain']['write-read'] = '[write read][open open]'
G.add_edge('init_shell','hostapd')
G.edge['init_shell']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','ime_app')
G.edge['init_shell']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open]'
G.add_edge('init_shell','shell')
G.edge['init_shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','s_system_app')
G.edge['init_shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('init_shell','system_app')
G.edge['init_shell']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('init_shell','vmwared')
G.edge['init_shell']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','at_distributor')
G.edge['init_shell']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('init_shell','charon')
G.edge['init_shell']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('init_shell','hostapd')
G.edge['init_shell']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('init_shell','ime_app')
G.edge['init_shell']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr]'
G.add_edge('init_shell','shell')
G.edge['init_shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('init_shell','s_system_app')
G.edge['init_shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','system_app')
G.edge['init_shell']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','vmwared')
G.edge['init_shell']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('init_shell','at_distributor')
G.edge['init_shell']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['init_shell']['at_distributor']['fill'] = 'red'
G.add_edge('init_shell','at_distributor')
G.edge['init_shell']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','charon')
G.edge['init_shell']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['init_shell']['charon']['fill'] = 'red'
G.add_edge('init_shell','charon')
G.edge['init_shell']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','domain')
G.edge['init_shell']['domain']['write-read'] = '[write read][open open][write read]'
G.edge['init_shell']['domain']['fill'] = 'red'
G.add_edge('init_shell','domain')
G.edge['init_shell']['domain']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('init_shell','hostapd')
G.edge['init_shell']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['init_shell']['hostapd']['fill'] = 'red'
G.add_edge('init_shell','hostapd')
G.edge['init_shell']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','ime_app')
G.edge['init_shell']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['ime_app']['fill'] = 'red'
G.add_edge('init_shell','ime_app')
G.edge['init_shell']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read]'
G.edge['init_shell']['init_shell']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','shell')
G.edge['init_shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['init_shell']['shell']['fill'] = 'red'
G.add_edge('init_shell','shell')
G.edge['init_shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','s_system_app')
G.edge['init_shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['s_system_app']['fill'] = 'red'
G.add_edge('init_shell','s_system_app')
G.edge['init_shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','system_app')
G.edge['init_shell']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['system_app']['fill'] = 'red'
G.add_edge('init_shell','system_app')
G.edge['init_shell']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','vmwared')
G.edge['init_shell']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['init_shell']['vmwared']['fill'] = 'red'
G.add_edge('init_shell','vmwared')
G.edge['init_shell']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('shell','at_distributor')
G.edge['shell']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('shell','charon')
G.edge['shell']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('shell','domain')
G.edge['shell']['domain']['write-read'] = '[write read][open open][write read][append read][write read][append read][open open]'
G.add_edge('shell','hostapd')
G.edge['shell']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open]'
G.add_edge('shell','ime_app')
G.edge['shell']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('shell','init_shell')
G.edge['shell']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('shell','shell')
G.edge['shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open]'
G.add_edge('shell','s_system_app')
G.edge['shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('shell','system_app')
G.edge['shell']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('shell','vmwared')
G.edge['shell']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('shell','at_distributor')
G.edge['shell']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('shell','charon')
G.edge['shell']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('shell','hostapd')
G.edge['shell']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][setattr getattr]'
G.add_edge('shell','ime_app')
G.edge['shell']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('shell','init_shell')
G.edge['shell']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('shell','shell')
G.edge['shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr]'
G.add_edge('shell','s_system_app')
G.edge['shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('shell','system_app')
G.edge['shell']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('shell','vmwared')
G.edge['shell']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('shell','at_distributor')
G.edge['shell']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['shell']['at_distributor']['fill'] = 'red'
G.add_edge('shell','at_distributor')
G.edge['shell']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('shell','charon')
G.edge['shell']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['shell']['charon']['fill'] = 'red'
G.add_edge('shell','charon')
G.edge['shell']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('shell','domain')
G.edge['shell']['domain']['write-read'] = '[write read][open open][write read][append read][write read][append read][open open][write read]'
G.edge['shell']['domain']['fill'] = 'red'
G.add_edge('shell','domain')
G.edge['shell']['domain']['write-read'] = '[write read][open open][write read][append read][write read][append read][open open][write read][append read]'
G.add_edge('shell','hostapd')
G.edge['shell']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][setattr getattr][write read]'
G.edge['shell']['hostapd']['fill'] = 'red'
G.add_edge('shell','hostapd')
G.edge['shell']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][setattr getattr][write read][append read]'
G.add_edge('shell','ime_app')
G.edge['shell']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['shell']['ime_app']['fill'] = 'red'
G.add_edge('shell','ime_app')
G.edge['shell']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('shell','init_shell')
G.edge['shell']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['shell']['init_shell']['fill'] = 'red'
G.add_edge('shell','init_shell')
G.edge['shell']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('shell','shell')
G.edge['shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read]'
G.edge['shell']['shell']['fill'] = 'red'
G.add_edge('shell','shell')
G.edge['shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('shell','s_system_app')
G.edge['shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['shell']['s_system_app']['fill'] = 'red'
G.add_edge('shell','s_system_app')
G.edge['shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('shell','system_app')
G.edge['shell']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['shell']['system_app']['fill'] = 'red'
G.add_edge('shell','system_app')
G.edge['shell']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('shell','vmwared')
G.edge['shell']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['shell']['vmwared']['fill'] = 'red'
G.add_edge('shell','vmwared')
G.edge['shell']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','at_distributor')
G.edge['s_system_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','charon')
G.edge['s_system_app']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','domain')
G.edge['s_system_app']['domain']['write-read'] = '[write read][write read][append read][open open]'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','shell')
G.edge['s_system_app']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','vmwared')
G.edge['s_system_app']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','at_distributor')
G.edge['s_system_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','charon')
G.edge['s_system_app']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','shell')
G.edge['s_system_app']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','vmwared')
G.edge['s_system_app']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','at_distributor')
G.edge['s_system_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['at_distributor']['fill'] = 'red'
G.add_edge('s_system_app','at_distributor')
G.edge['s_system_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','charon')
G.edge['s_system_app']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['charon']['fill'] = 'red'
G.add_edge('s_system_app','charon')
G.edge['s_system_app']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','domain')
G.edge['s_system_app']['domain']['write-read'] = '[write read][write read][append read][open open][write read]'
G.edge['s_system_app']['domain']['fill'] = 'red'
G.add_edge('s_system_app','domain')
G.edge['s_system_app']['domain']['write-read'] = '[write read][write read][append read][open open][write read][append read]'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['hostapd']['fill'] = 'red'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['ime_app']['fill'] = 'red'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['init_shell']['fill'] = 'red'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','shell')
G.edge['s_system_app']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['shell']['fill'] = 'red'
G.add_edge('s_system_app','shell')
G.edge['s_system_app']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['system_app']['fill'] = 'red'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','vmwared')
G.edge['s_system_app']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['vmwared']['fill'] = 'red'
G.add_edge('s_system_app','vmwared')
G.edge['s_system_app']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','at_distributor')
G.edge['system_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','charon')
G.edge['system_app']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','domain')
G.edge['system_app']['domain']['write-read'] = '[write read][write read][append read][open open]'
G.add_edge('system_app','hostapd')
G.edge['system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','shell')
G.edge['system_app']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','vmwared')
G.edge['system_app']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','at_distributor')
G.edge['system_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_app','charon')
G.edge['system_app']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_app','hostapd')
G.edge['system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','shell')
G.edge['system_app']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','vmwared')
G.edge['system_app']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_app','at_distributor')
G.edge['system_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_app']['at_distributor']['fill'] = 'red'
G.add_edge('system_app','at_distributor')
G.edge['system_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','charon')
G.edge['system_app']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_app']['charon']['fill'] = 'red'
G.add_edge('system_app','charon')
G.edge['system_app']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','domain')
G.edge['system_app']['domain']['write-read'] = '[write read][write read][append read][open open][write read]'
G.edge['system_app']['domain']['fill'] = 'red'
G.add_edge('system_app','domain')
G.edge['system_app']['domain']['write-read'] = '[write read][write read][append read][open open][write read][append read]'
G.add_edge('system_app','hostapd')
G.edge['system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_app']['hostapd']['fill'] = 'red'
G.add_edge('system_app','hostapd')
G.edge['system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['ime_app']['fill'] = 'red'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['init_shell']['fill'] = 'red'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','shell')
G.edge['system_app']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_app']['shell']['fill'] = 'red'
G.add_edge('system_app','shell')
G.edge['system_app']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['s_system_app']['fill'] = 'red'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['system_app']['fill'] = 'red'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','vmwared')
G.edge['system_app']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_app']['vmwared']['fill'] = 'red'
G.add_edge('system_app','vmwared')
G.edge['system_app']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('vmwared','at_distributor')
G.edge['vmwared']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vmwared','charon')
G.edge['vmwared']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vmwared','domain')
G.edge['vmwared']['domain']['write-read'] = '[write read][open open]'
G.add_edge('vmwared','hostapd')
G.edge['vmwared']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vmwared','ime_app')
G.edge['vmwared']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vmwared','init_shell')
G.edge['vmwared']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vmwared','shell')
G.edge['vmwared']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vmwared','s_system_app')
G.edge['vmwared']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vmwared','system_app')
G.edge['vmwared']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vmwared','vmwared')
G.edge['vmwared']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vmwared','at_distributor')
G.edge['vmwared']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('vmwared','charon')
G.edge['vmwared']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('vmwared','hostapd')
G.edge['vmwared']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('vmwared','ime_app')
G.edge['vmwared']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('vmwared','init_shell')
G.edge['vmwared']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('vmwared','shell')
G.edge['vmwared']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('vmwared','s_system_app')
G.edge['vmwared']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('vmwared','system_app')
G.edge['vmwared']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('vmwared','vmwared')
G.edge['vmwared']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('vmwared','at_distributor')
G.edge['vmwared']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['vmwared']['at_distributor']['fill'] = 'red'
G.add_edge('vmwared','at_distributor')
G.edge['vmwared']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('vmwared','charon')
G.edge['vmwared']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['vmwared']['charon']['fill'] = 'red'
G.add_edge('vmwared','charon')
G.edge['vmwared']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('vmwared','domain')
G.edge['vmwared']['domain']['write-read'] = '[write read][open open][write read]'
G.edge['vmwared']['domain']['fill'] = 'red'
G.add_edge('vmwared','domain')
G.edge['vmwared']['domain']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('vmwared','hostapd')
G.edge['vmwared']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['vmwared']['hostapd']['fill'] = 'red'
G.add_edge('vmwared','hostapd')
G.edge['vmwared']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('vmwared','ime_app')
G.edge['vmwared']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['vmwared']['ime_app']['fill'] = 'red'
G.add_edge('vmwared','ime_app')
G.edge['vmwared']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('vmwared','init_shell')
G.edge['vmwared']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['vmwared']['init_shell']['fill'] = 'red'
G.add_edge('vmwared','init_shell')
G.edge['vmwared']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('vmwared','shell')
G.edge['vmwared']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['vmwared']['shell']['fill'] = 'red'
G.add_edge('vmwared','shell')
G.edge['vmwared']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('vmwared','s_system_app')
G.edge['vmwared']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['vmwared']['s_system_app']['fill'] = 'red'
G.add_edge('vmwared','s_system_app')
G.edge['vmwared']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('vmwared','system_app')
G.edge['vmwared']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['vmwared']['system_app']['fill'] = 'red'
G.add_edge('vmwared','system_app')
G.edge['vmwared']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('vmwared','vmwared')
G.edge['vmwared']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['vmwared']['vmwared']['fill'] = 'red'
G.add_edge('vmwared','vmwared')
G.edge['vmwared']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()