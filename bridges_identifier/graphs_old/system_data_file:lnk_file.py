import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('appdomain','init_shell')
G.edge['appdomain']['init_shell']['write-read'] = '[setattr getattr]'
G.add_edge('appdomain','installd')
G.edge['appdomain']['installd']['write-read'] = '[setattr getattr]'
G.add_edge('appdomain','installd')
G.edge['appdomain']['installd']['write-read'] = '[setattr getattr][setattr getattr]'
G.add_edge('appdomain','s_system_app')
G.edge['appdomain']['s_system_app']['write-read'] = '[setattr getattr]'
G.add_edge('appdomain','system_app')
G.edge['appdomain']['system_app']['write-read'] = '[setattr getattr]'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('domain','mfgloader')
G.edge['domain']['mfgloader']['write-read'] = '[open open]'
G.add_edge('domain','s_system_app')
G.edge['domain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('domain','system_app')
G.edge['domain']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('domain','installd')
G.edge['domain']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr]'
G.add_edge('domain','installd')
G.edge['domain']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('domain','s_system_app')
G.edge['domain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('domain','system_app')
G.edge['domain']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['domain']['init_shell']['fill'] = 'red'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('domain','mfgloader')
G.edge['domain']['mfgloader']['write-read'] = '[open open][write read]'
G.edge['domain']['mfgloader']['fill'] = 'red'
G.add_edge('domain','mfgloader')
G.edge['domain']['mfgloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('domain','s_system_app')
G.edge['domain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['domain']['s_system_app']['fill'] = 'red'
G.add_edge('domain','s_system_app')
G.edge['domain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('domain','system_app')
G.edge['domain']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['domain']['system_app']['fill'] = 'red'
G.add_edge('domain','system_app')
G.edge['domain']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['domain']['system_server']['fill'] = 'red'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('epmd','init_shell')
G.edge['epmd']['init_shell']['write-read'] = '[open open][open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('epmd','installd')
G.edge['epmd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('epmd','installd')
G.edge['epmd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('epmd','s_system_app')
G.edge['epmd']['s_system_app']['write-read'] = '[setattr getattr]'
G.add_edge('epmd','system_app')
G.edge['epmd']['system_app']['write-read'] = '[setattr getattr]'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('fixmo_app','init_shell')
G.edge['fixmo_app']['init_shell']['write-read'] = '[open open]'
G.add_edge('fixmo_app','mfgloader')
G.edge['fixmo_app']['mfgloader']['write-read'] = '[open open]'
G.add_edge('fixmo_app','s_system_app')
G.edge['fixmo_app']['s_system_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('fixmo_app','system_app')
G.edge['fixmo_app']['system_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('fixmo_app','system_server')
G.edge['fixmo_app']['system_server']['write-read'] = '[open open]'
G.add_edge('fixmo_app','init_shell')
G.edge['fixmo_app']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('fixmo_app','installd')
G.edge['fixmo_app']['installd']['write-read'] = '[setattr getattr]'
G.add_edge('fixmo_app','installd')
G.edge['fixmo_app']['installd']['write-read'] = '[setattr getattr][setattr getattr]'
G.add_edge('fixmo_app','s_system_app')
G.edge['fixmo_app']['s_system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('fixmo_app','system_app')
G.edge['fixmo_app']['system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('fixmo_app','system_server')
G.edge['fixmo_app']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('fixmo_app','init_shell')
G.edge['fixmo_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['fixmo_app']['init_shell']['fill'] = 'red'
G.add_edge('fixmo_app','init_shell')
G.edge['fixmo_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('fixmo_app','mfgloader')
G.edge['fixmo_app']['mfgloader']['write-read'] = '[open open][write read]'
G.edge['fixmo_app']['mfgloader']['fill'] = 'red'
G.add_edge('fixmo_app','mfgloader')
G.edge['fixmo_app']['mfgloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('fixmo_app','s_system_app')
G.edge['fixmo_app']['s_system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['fixmo_app']['s_system_app']['fill'] = 'red'
G.add_edge('fixmo_app','s_system_app')
G.edge['fixmo_app']['s_system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('fixmo_app','system_app')
G.edge['fixmo_app']['system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['fixmo_app']['system_app']['fill'] = 'red'
G.add_edge('fixmo_app','system_app')
G.edge['fixmo_app']['system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('fixmo_app','system_server')
G.edge['fixmo_app']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['fixmo_app']['system_server']['fill'] = 'red'
G.add_edge('fixmo_app','system_server')
G.edge['fixmo_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('good_app','init_shell')
G.edge['good_app']['init_shell']['write-read'] = '[open open]'
G.add_edge('good_app','mfgloader')
G.edge['good_app']['mfgloader']['write-read'] = '[open open]'
G.add_edge('good_app','s_system_app')
G.edge['good_app']['s_system_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('good_app','system_app')
G.edge['good_app']['system_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('good_app','system_server')
G.edge['good_app']['system_server']['write-read'] = '[open open]'
G.add_edge('good_app','init_shell')
G.edge['good_app']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('good_app','installd')
G.edge['good_app']['installd']['write-read'] = '[setattr getattr]'
G.add_edge('good_app','installd')
G.edge['good_app']['installd']['write-read'] = '[setattr getattr][setattr getattr]'
G.add_edge('good_app','s_system_app')
G.edge['good_app']['s_system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('good_app','system_app')
G.edge['good_app']['system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('good_app','system_server')
G.edge['good_app']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('good_app','init_shell')
G.edge['good_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['good_app']['init_shell']['fill'] = 'red'
G.add_edge('good_app','init_shell')
G.edge['good_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('good_app','mfgloader')
G.edge['good_app']['mfgloader']['write-read'] = '[open open][write read]'
G.edge['good_app']['mfgloader']['fill'] = 'red'
G.add_edge('good_app','mfgloader')
G.edge['good_app']['mfgloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('good_app','s_system_app')
G.edge['good_app']['s_system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['good_app']['s_system_app']['fill'] = 'red'
G.add_edge('good_app','s_system_app')
G.edge['good_app']['s_system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('good_app','system_app')
G.edge['good_app']['system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['good_app']['system_app']['fill'] = 'red'
G.add_edge('good_app','system_app')
G.edge['good_app']['system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('good_app','system_server')
G.edge['good_app']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['good_app']['system_server']['fill'] = 'red'
G.add_edge('good_app','system_server')
G.edge['good_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','mfgloader')
G.edge['ime_app']['mfgloader']['write-read'] = '[open open]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open]'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ime_app','installd')
G.edge['ime_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('ime_app','installd')
G.edge['ime_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ime_app']['init_shell']['fill'] = 'red'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','mfgloader')
G.edge['ime_app']['mfgloader']['write-read'] = '[open open][write read]'
G.edge['ime_app']['mfgloader']['fill'] = 'red'
G.add_edge('ime_app','mfgloader')
G.edge['ime_app']['mfgloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ime_app']['s_system_app']['fill'] = 'red'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ime_app']['system_app']['fill'] = 'red'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['system_server']['fill'] = 'red'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','mfgloader')
G.edge['init_shell']['mfgloader']['write-read'] = '[open open]'
G.add_edge('init_shell','s_system_app')
G.edge['init_shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','system_app')
G.edge['init_shell']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('init_shell','installd')
G.edge['init_shell']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('init_shell','installd')
G.edge['init_shell']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('init_shell','s_system_app')
G.edge['init_shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('init_shell','system_app')
G.edge['init_shell']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['init_shell']['init_shell']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','mfgloader')
G.edge['init_shell']['mfgloader']['write-read'] = '[open open][write read]'
G.edge['init_shell']['mfgloader']['fill'] = 'red'
G.add_edge('init_shell','mfgloader')
G.edge['init_shell']['mfgloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('init_shell','s_system_app')
G.edge['init_shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['init_shell']['s_system_app']['fill'] = 'red'
G.add_edge('init_shell','s_system_app')
G.edge['init_shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','system_app')
G.edge['init_shell']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['init_shell']['system_app']['fill'] = 'red'
G.add_edge('init_shell','system_app')
G.edge['init_shell']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['init_shell']['system_server']['fill'] = 'red'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('installd','init_shell')
G.edge['installd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('installd','s_system_app')
G.edge['installd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','system_app')
G.edge['installd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom]'
G.add_edge('installd','init_shell')
G.edge['installd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr][setattr getattr]'
G.add_edge('installd','s_system_app')
G.edge['installd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('installd','system_app')
G.edge['installd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom]'
G.add_edge('mfgloader','init_shell')
G.edge['mfgloader']['init_shell']['write-read'] = '[open open]'
G.add_edge('mfgloader','mfgloader')
G.edge['mfgloader']['mfgloader']['write-read'] = '[open open]'
G.add_edge('mfgloader','s_system_app')
G.edge['mfgloader']['s_system_app']['write-read'] = '[open open]'
G.add_edge('mfgloader','system_app')
G.edge['mfgloader']['system_app']['write-read'] = '[open open]'
G.add_edge('mfgloader','system_server')
G.edge['mfgloader']['system_server']['write-read'] = '[open open]'
G.add_edge('mfgloader','init_shell')
G.edge['mfgloader']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mfgloader','installd')
G.edge['mfgloader']['installd']['write-read'] = '[setattr getattr]'
G.add_edge('mfgloader','installd')
G.edge['mfgloader']['installd']['write-read'] = '[setattr getattr][setattr getattr]'
G.add_edge('mfgloader','s_system_app')
G.edge['mfgloader']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mfgloader','system_app')
G.edge['mfgloader']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mfgloader','system_server')
G.edge['mfgloader']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mfgloader','init_shell')
G.edge['mfgloader']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mfgloader']['init_shell']['fill'] = 'red'
G.add_edge('mfgloader','init_shell')
G.edge['mfgloader']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mfgloader','mfgloader')
G.edge['mfgloader']['mfgloader']['write-read'] = '[open open][write read]'
G.edge['mfgloader']['mfgloader']['fill'] = 'red'
G.add_edge('mfgloader','mfgloader')
G.edge['mfgloader']['mfgloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('mfgloader','s_system_app')
G.edge['mfgloader']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mfgloader']['s_system_app']['fill'] = 'red'
G.add_edge('mfgloader','s_system_app')
G.edge['mfgloader']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mfgloader','system_app')
G.edge['mfgloader']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mfgloader']['system_app']['fill'] = 'red'
G.add_edge('mfgloader','system_app')
G.edge['mfgloader']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mfgloader','system_server')
G.edge['mfgloader']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mfgloader']['system_server']['fill'] = 'red'
G.add_edge('mfgloader','system_server')
G.edge['mfgloader']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_platform_app','init_shell')
G.edge['s_platform_app']['init_shell']['write-read'] = '[setattr getattr]'
G.add_edge('s_platform_app','installd')
G.edge['s_platform_app']['installd']['write-read'] = '[setattr getattr]'
G.add_edge('s_platform_app','installd')
G.edge['s_platform_app']['installd']['write-read'] = '[setattr getattr][setattr getattr]'
G.add_edge('s_platform_app','s_system_app')
G.edge['s_platform_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('s_platform_app','system_app')
G.edge['s_platform_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('s_platform_app','system_server')
G.edge['s_platform_app']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','mfgloader')
G.edge['s_system_app']['mfgloader']['write-read'] = '[open open]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open]'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','installd')
G.edge['s_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('s_system_app','installd')
G.edge['s_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['init_shell']['fill'] = 'red'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','mfgloader')
G.edge['s_system_app']['mfgloader']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['mfgloader']['fill'] = 'red'
G.add_edge('s_system_app','mfgloader')
G.edge['s_system_app']['mfgloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['system_app']['fill'] = 'red'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['system_server']['fill'] = 'red'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','mfgloader')
G.edge['system_app']['mfgloader']['write-read'] = '[open open]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open]'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_app','installd')
G.edge['system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('system_app','installd')
G.edge['system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_app']['init_shell']['fill'] = 'red'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','mfgloader')
G.edge['system_app']['mfgloader']['write-read'] = '[open open][write read]'
G.edge['system_app']['mfgloader']['fill'] = 'red'
G.add_edge('system_app','mfgloader')
G.edge['system_app']['mfgloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['s_system_app']['fill'] = 'red'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['system_app']['fill'] = 'red'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['system_server']['fill'] = 'red'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','mfgloader')
G.edge['system_server']['mfgloader']['write-read'] = '[open open]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][setattr getattr]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['init_shell']['fill'] = 'red'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','mfgloader')
G.edge['system_server']['mfgloader']['write-read'] = '[open open][write read]'
G.edge['system_server']['mfgloader']['fill'] = 'red'
G.add_edge('system_server','mfgloader')
G.edge['system_server']['mfgloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read]'
G.edge['system_server']['s_system_app']['fill'] = 'red'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read]'
G.edge['system_server']['system_app']['fill'] = 'red'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('vold','installd')
G.edge['vold']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('vold','installd')
G.edge['vold']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('vold','system_app')
G.edge['vold']['system_app']['write-read'] = '[setattr getattr][setopt getopt][setattr getattr]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open]'
G.add_edge('vold','mfgloader')
G.edge['vold']['mfgloader']['write-read'] = '[open open]'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][open open]'
G.add_edge('vold','system_app')
G.edge['vold']['system_app']['write-read'] = '[setattr getattr][setopt getopt][setattr getattr][open open]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open]'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr]'
G.add_edge('vold','installd')
G.edge['vold']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('vold','installd')
G.edge['vold']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr]'
G.add_edge('vold','system_app')
G.edge['vold']['system_app']['write-read'] = '[setattr getattr][setopt getopt][setattr getattr][open open][setattr getattr]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr]'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read]'
G.edge['vold']['init_shell']['fill'] = 'red'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read]'
G.add_edge('vold','mfgloader')
G.edge['vold']['mfgloader']['write-read'] = '[open open][write read]'
G.edge['vold']['mfgloader']['fill'] = 'red'
G.add_edge('vold','mfgloader')
G.edge['vold']['mfgloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read]'
G.edge['vold']['s_system_app']['fill'] = 'red'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read]'
G.add_edge('vold','system_app')
G.edge['vold']['system_app']['write-read'] = '[setattr getattr][setopt getopt][setattr getattr][open open][setattr getattr][write read]'
G.edge['vold']['system_app']['fill'] = 'red'
G.add_edge('vold','system_app')
G.edge['vold']['system_app']['write-read'] = '[setattr getattr][setopt getopt][setattr getattr][open open][setattr getattr][write read][append read]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read]'
G.edge['vold']['system_server']['fill'] = 'red'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()