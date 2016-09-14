import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('debuggerd','debuggerd')
G.edge['debuggerd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('debuggerd','dumpstate')
G.edge['debuggerd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('debuggerd','init_shell')
G.edge['debuggerd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('debuggerd','logwrapper')
G.edge['debuggerd']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('debuggerd','netd')
G.edge['debuggerd']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('debuggerd','p2p_supplicant')
G.edge['debuggerd']['p2p_supplicant']['write-read'] = '[open open]'
G.add_edge('debuggerd','s_system_app')
G.edge['debuggerd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('debuggerd','system_server')
G.edge['debuggerd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('debuggerd','wpa')
G.edge['debuggerd']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('debuggerd','debuggerd')
G.edge['debuggerd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('debuggerd','dumpstate')
G.edge['debuggerd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('debuggerd','hostapd')
G.edge['debuggerd']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('debuggerd','init_shell')
G.edge['debuggerd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('debuggerd','logwrapper')
G.edge['debuggerd']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('debuggerd','netd')
G.edge['debuggerd']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('debuggerd','p2p_supplicant')
G.edge['debuggerd']['p2p_supplicant']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','p2p_supplicant')
G.edge['debuggerd']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr]'
G.add_edge('debuggerd','s_system_app')
G.edge['debuggerd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('debuggerd','system_server')
G.edge['debuggerd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('debuggerd','debuggerd')
G.edge['debuggerd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['debuggerd']['debuggerd']['fill'] = 'red'
G.add_edge('debuggerd','debuggerd')
G.edge['debuggerd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('debuggerd','dumpstate')
G.edge['debuggerd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['debuggerd']['dumpstate']['fill'] = 'red'
G.add_edge('debuggerd','dumpstate')
G.edge['debuggerd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('debuggerd','hostapd')
G.edge['debuggerd']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['debuggerd']['hostapd']['fill'] = 'red'
G.add_edge('debuggerd','init_shell')
G.edge['debuggerd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['debuggerd']['init_shell']['fill'] = 'red'
G.add_edge('debuggerd','init_shell')
G.edge['debuggerd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('debuggerd','logwrapper')
G.edge['debuggerd']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['debuggerd']['logwrapper']['fill'] = 'red'
G.add_edge('debuggerd','logwrapper')
G.edge['debuggerd']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('debuggerd','netd')
G.edge['debuggerd']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['debuggerd']['netd']['fill'] = 'red'
G.add_edge('debuggerd','netd')
G.edge['debuggerd']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('debuggerd','p2p_supplicant')
G.edge['debuggerd']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read]'
G.edge['debuggerd']['p2p_supplicant']['fill'] = 'red'
G.add_edge('debuggerd','p2p_supplicant')
G.edge['debuggerd']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('debuggerd','p2p_supplicant')
G.edge['debuggerd']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['debuggerd']['p2p_supplicant']['fill'] = 'red'
G.add_edge('debuggerd','s_system_app')
G.edge['debuggerd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['debuggerd']['s_system_app']['fill'] = 'red'
G.add_edge('debuggerd','s_system_app')
G.edge['debuggerd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('debuggerd','system_server')
G.edge['debuggerd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['debuggerd']['system_server']['fill'] = 'red'
G.add_edge('debuggerd','system_server')
G.edge['debuggerd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('debuggerd','wpa')
G.edge['debuggerd']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['debuggerd']['wpa']['fill'] = 'red'
G.add_edge('debuggerd','wpa')
G.edge['debuggerd']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('dumpstate','debuggerd')
G.edge['dumpstate']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('dumpstate','init_shell')
G.edge['dumpstate']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','logwrapper')
G.edge['dumpstate']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','netd')
G.edge['dumpstate']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','p2p_supplicant')
G.edge['dumpstate']['p2p_supplicant']['write-read'] = '[open open]'
G.add_edge('dumpstate','s_system_app')
G.edge['dumpstate']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','system_server')
G.edge['dumpstate']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('dumpstate','wpa')
G.edge['dumpstate']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','debuggerd')
G.edge['dumpstate']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('dumpstate','hostapd')
G.edge['dumpstate']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('dumpstate','init_shell')
G.edge['dumpstate']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('dumpstate','logwrapper')
G.edge['dumpstate']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('dumpstate','netd')
G.edge['dumpstate']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('dumpstate','p2p_supplicant')
G.edge['dumpstate']['p2p_supplicant']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','p2p_supplicant')
G.edge['dumpstate']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr]'
G.add_edge('dumpstate','s_system_app')
G.edge['dumpstate']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('dumpstate','system_server')
G.edge['dumpstate']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('dumpstate','debuggerd')
G.edge['dumpstate']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['dumpstate']['debuggerd']['fill'] = 'red'
G.add_edge('dumpstate','debuggerd')
G.edge['dumpstate']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['dumpstate']['dumpstate']['fill'] = 'red'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('dumpstate','hostapd')
G.edge['dumpstate']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['dumpstate']['hostapd']['fill'] = 'red'
G.add_edge('dumpstate','init_shell')
G.edge['dumpstate']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['dumpstate']['init_shell']['fill'] = 'red'
G.add_edge('dumpstate','init_shell')
G.edge['dumpstate']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('dumpstate','logwrapper')
G.edge['dumpstate']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['dumpstate']['logwrapper']['fill'] = 'red'
G.add_edge('dumpstate','logwrapper')
G.edge['dumpstate']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('dumpstate','netd')
G.edge['dumpstate']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['dumpstate']['netd']['fill'] = 'red'
G.add_edge('dumpstate','netd')
G.edge['dumpstate']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('dumpstate','p2p_supplicant')
G.edge['dumpstate']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read]'
G.edge['dumpstate']['p2p_supplicant']['fill'] = 'red'
G.add_edge('dumpstate','p2p_supplicant')
G.edge['dumpstate']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('dumpstate','p2p_supplicant')
G.edge['dumpstate']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['dumpstate']['p2p_supplicant']['fill'] = 'red'
G.add_edge('dumpstate','s_system_app')
G.edge['dumpstate']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['dumpstate']['s_system_app']['fill'] = 'red'
G.add_edge('dumpstate','s_system_app')
G.edge['dumpstate']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('dumpstate','system_server')
G.edge['dumpstate']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['dumpstate']['system_server']['fill'] = 'red'
G.add_edge('dumpstate','system_server')
G.edge['dumpstate']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('dumpstate','wpa')
G.edge['dumpstate']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['dumpstate']['wpa']['fill'] = 'red'
G.add_edge('dumpstate','wpa')
G.edge['dumpstate']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('ime_app','debuggerd')
G.edge['ime_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open]'
G.add_edge('ime_app','dumpstate')
G.edge['ime_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('ime_app','logwrapper')
G.edge['ime_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','p2p_supplicant')
G.edge['ime_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','wpa')
G.edge['ime_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open]'
G.add_edge('ime_app','debuggerd')
G.edge['ime_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr]'
G.add_edge('ime_app','dumpstate')
G.edge['ime_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ime_app','hostapd')
G.edge['ime_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr]'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','logwrapper')
G.edge['ime_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ime_app','p2p_supplicant')
G.edge['ime_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr]'
G.add_edge('ime_app','p2p_supplicant')
G.edge['ime_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','debuggerd')
G.edge['ime_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read]'
G.edge['ime_app']['debuggerd']['fill'] = 'red'
G.add_edge('ime_app','debuggerd')
G.edge['ime_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','dumpstate')
G.edge['ime_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ime_app']['dumpstate']['fill'] = 'red'
G.add_edge('ime_app','dumpstate')
G.edge['ime_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','hostapd')
G.edge['ime_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read]'
G.edge['ime_app']['hostapd']['fill'] = 'red'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['init_shell']['fill'] = 'red'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','logwrapper')
G.edge['ime_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ime_app']['logwrapper']['fill'] = 'red'
G.add_edge('ime_app','logwrapper')
G.edge['ime_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ime_app']['netd']['fill'] = 'red'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','p2p_supplicant')
G.edge['ime_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read]'
G.edge['ime_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('ime_app','p2p_supplicant')
G.edge['ime_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('ime_app','p2p_supplicant')
G.edge['ime_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['ime_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ime_app']['s_system_app']['fill'] = 'red'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['system_server']['fill'] = 'red'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','wpa')
G.edge['ime_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read]'
G.edge['ime_app']['wpa']['fill'] = 'red'
G.add_edge('ime_app','wpa')
G.edge['ime_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read]'
G.add_edge('init_shell','debuggerd')
G.edge['init_shell']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','dumpstate')
G.edge['init_shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('init_shell','logwrapper')
G.edge['init_shell']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','netd')
G.edge['init_shell']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','p2p_supplicant')
G.edge['init_shell']['p2p_supplicant']['write-read'] = '[open open]'
G.add_edge('init_shell','s_system_app')
G.edge['init_shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('init_shell','wpa')
G.edge['init_shell']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','debuggerd')
G.edge['init_shell']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('init_shell','dumpstate')
G.edge['init_shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('init_shell','hostapd')
G.edge['init_shell']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','logwrapper')
G.edge['init_shell']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('init_shell','netd')
G.edge['init_shell']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('init_shell','p2p_supplicant')
G.edge['init_shell']['p2p_supplicant']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','p2p_supplicant')
G.edge['init_shell']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr]'
G.add_edge('init_shell','s_system_app')
G.edge['init_shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','debuggerd')
G.edge['init_shell']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['init_shell']['debuggerd']['fill'] = 'red'
G.add_edge('init_shell','debuggerd')
G.edge['init_shell']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','dumpstate')
G.edge['init_shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['init_shell']['dumpstate']['fill'] = 'red'
G.add_edge('init_shell','dumpstate')
G.edge['init_shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','hostapd')
G.edge['init_shell']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['init_shell']['hostapd']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['init_shell']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','logwrapper')
G.edge['init_shell']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['init_shell']['logwrapper']['fill'] = 'red'
G.add_edge('init_shell','logwrapper')
G.edge['init_shell']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','netd')
G.edge['init_shell']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['init_shell']['netd']['fill'] = 'red'
G.add_edge('init_shell','netd')
G.edge['init_shell']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','p2p_supplicant')
G.edge['init_shell']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read]'
G.edge['init_shell']['p2p_supplicant']['fill'] = 'red'
G.add_edge('init_shell','p2p_supplicant')
G.edge['init_shell']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('init_shell','p2p_supplicant')
G.edge['init_shell']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['init_shell']['p2p_supplicant']['fill'] = 'red'
G.add_edge('init_shell','s_system_app')
G.edge['init_shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['s_system_app']['fill'] = 'red'
G.add_edge('init_shell','s_system_app')
G.edge['init_shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['system_server']['fill'] = 'red'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','wpa')
G.edge['init_shell']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['wpa']['fill'] = 'red'
G.add_edge('init_shell','wpa')
G.edge['init_shell']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('logwrapper','debuggerd')
G.edge['logwrapper']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('logwrapper','dumpstate')
G.edge['logwrapper']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('logwrapper','init_shell')
G.edge['logwrapper']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('logwrapper','logwrapper')
G.edge['logwrapper']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('logwrapper','netd')
G.edge['logwrapper']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('logwrapper','p2p_supplicant')
G.edge['logwrapper']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open]'
G.add_edge('logwrapper','s_system_app')
G.edge['logwrapper']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('logwrapper','system_server')
G.edge['logwrapper']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open]'
G.add_edge('logwrapper','wpa')
G.edge['logwrapper']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('logwrapper','debuggerd')
G.edge['logwrapper']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('logwrapper','dumpstate')
G.edge['logwrapper']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('logwrapper','hostapd')
G.edge['logwrapper']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('logwrapper','init_shell')
G.edge['logwrapper']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('logwrapper','logwrapper')
G.edge['logwrapper']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('logwrapper','netd')
G.edge['logwrapper']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('logwrapper','p2p_supplicant')
G.edge['logwrapper']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr]'
G.add_edge('logwrapper','p2p_supplicant')
G.edge['logwrapper']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr]'
G.add_edge('logwrapper','s_system_app')
G.edge['logwrapper']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('logwrapper','system_server')
G.edge['logwrapper']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr]'
G.add_edge('logwrapper','debuggerd')
G.edge['logwrapper']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['logwrapper']['debuggerd']['fill'] = 'red'
G.add_edge('logwrapper','debuggerd')
G.edge['logwrapper']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('logwrapper','dumpstate')
G.edge['logwrapper']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['logwrapper']['dumpstate']['fill'] = 'red'
G.add_edge('logwrapper','dumpstate')
G.edge['logwrapper']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('logwrapper','hostapd')
G.edge['logwrapper']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['logwrapper']['hostapd']['fill'] = 'red'
G.add_edge('logwrapper','init_shell')
G.edge['logwrapper']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['logwrapper']['init_shell']['fill'] = 'red'
G.add_edge('logwrapper','init_shell')
G.edge['logwrapper']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('logwrapper','logwrapper')
G.edge['logwrapper']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['logwrapper']['logwrapper']['fill'] = 'red'
G.add_edge('logwrapper','logwrapper')
G.edge['logwrapper']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('logwrapper','netd')
G.edge['logwrapper']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['logwrapper']['netd']['fill'] = 'red'
G.add_edge('logwrapper','netd')
G.edge['logwrapper']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('logwrapper','p2p_supplicant')
G.edge['logwrapper']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read]'
G.edge['logwrapper']['p2p_supplicant']['fill'] = 'red'
G.add_edge('logwrapper','p2p_supplicant')
G.edge['logwrapper']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('logwrapper','p2p_supplicant')
G.edge['logwrapper']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['logwrapper']['p2p_supplicant']['fill'] = 'red'
G.add_edge('logwrapper','s_system_app')
G.edge['logwrapper']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['logwrapper']['s_system_app']['fill'] = 'red'
G.add_edge('logwrapper','s_system_app')
G.edge['logwrapper']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('logwrapper','system_server')
G.edge['logwrapper']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['logwrapper']['system_server']['fill'] = 'red'
G.add_edge('logwrapper','system_server')
G.edge['logwrapper']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('logwrapper','wpa')
G.edge['logwrapper']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['logwrapper']['wpa']['fill'] = 'red'
G.add_edge('logwrapper','wpa')
G.edge['logwrapper']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('netd','debuggerd')
G.edge['netd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','dumpstate')
G.edge['netd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','init_shell')
G.edge['netd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','logwrapper')
G.edge['netd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open]'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open]'
G.add_edge('netd','wpa')
G.edge['netd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','debuggerd')
G.edge['netd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('netd','dumpstate')
G.edge['netd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('netd','hostapd')
G.edge['netd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('netd','init_shell')
G.edge['netd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('netd','logwrapper')
G.edge['netd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr]'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr]'
G.add_edge('netd','debuggerd')
G.edge['netd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['netd']['debuggerd']['fill'] = 'red'
G.add_edge('netd','debuggerd')
G.edge['netd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('netd','dumpstate')
G.edge['netd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['netd']['dumpstate']['fill'] = 'red'
G.add_edge('netd','dumpstate')
G.edge['netd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('netd','hostapd')
G.edge['netd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['netd']['hostapd']['fill'] = 'red'
G.add_edge('netd','init_shell')
G.edge['netd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['netd']['init_shell']['fill'] = 'red'
G.add_edge('netd','init_shell')
G.edge['netd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('netd','logwrapper')
G.edge['netd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['netd']['logwrapper']['fill'] = 'red'
G.add_edge('netd','logwrapper')
G.edge['netd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read]'
G.edge['netd']['netd']['fill'] = 'red'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read]'
G.edge['netd']['p2p_supplicant']['fill'] = 'red'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['netd']['p2p_supplicant']['fill'] = 'red'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['netd']['s_system_app']['fill'] = 'red'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['netd']['system_server']['fill'] = 'red'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('netd','wpa')
G.edge['netd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['netd']['wpa']['fill'] = 'red'
G.add_edge('netd','wpa')
G.edge['netd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('p2p_supplicant','debuggerd')
G.edge['p2p_supplicant']['debuggerd']['write-read'] = '[open open]'
G.add_edge('p2p_supplicant','dumpstate')
G.edge['p2p_supplicant']['dumpstate']['write-read'] = '[open open]'
G.add_edge('p2p_supplicant','init_shell')
G.edge['p2p_supplicant']['init_shell']['write-read'] = '[open open]'
G.add_edge('p2p_supplicant','logwrapper')
G.edge['p2p_supplicant']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open]'
G.add_edge('p2p_supplicant','s_system_app')
G.edge['p2p_supplicant']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open]'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('p2p_supplicant','debuggerd')
G.edge['p2p_supplicant']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('p2p_supplicant','dumpstate')
G.edge['p2p_supplicant']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('p2p_supplicant','hostapd')
G.edge['p2p_supplicant']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr]'
G.add_edge('p2p_supplicant','init_shell')
G.edge['p2p_supplicant']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('p2p_supplicant','logwrapper')
G.edge['p2p_supplicant']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr]'
G.add_edge('p2p_supplicant','s_system_app')
G.edge['p2p_supplicant']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr]'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr]'
G.add_edge('p2p_supplicant','debuggerd')
G.edge['p2p_supplicant']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['debuggerd']['fill'] = 'red'
G.add_edge('p2p_supplicant','debuggerd')
G.edge['p2p_supplicant']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('p2p_supplicant','dumpstate')
G.edge['p2p_supplicant']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['dumpstate']['fill'] = 'red'
G.add_edge('p2p_supplicant','dumpstate')
G.edge['p2p_supplicant']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('p2p_supplicant','hostapd')
G.edge['p2p_supplicant']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read]'
G.edge['p2p_supplicant']['hostapd']['fill'] = 'red'
G.add_edge('p2p_supplicant','init_shell')
G.edge['p2p_supplicant']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['init_shell']['fill'] = 'red'
G.add_edge('p2p_supplicant','init_shell')
G.edge['p2p_supplicant']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('p2p_supplicant','logwrapper')
G.edge['p2p_supplicant']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['logwrapper']['fill'] = 'red'
G.add_edge('p2p_supplicant','logwrapper')
G.edge['p2p_supplicant']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['netd']['fill'] = 'red'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read]'
G.edge['p2p_supplicant']['p2p_supplicant']['fill'] = 'red'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['p2p_supplicant']['p2p_supplicant']['fill'] = 'red'
G.add_edge('p2p_supplicant','s_system_app')
G.edge['p2p_supplicant']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['s_system_app']['fill'] = 'red'
G.add_edge('p2p_supplicant','s_system_app')
G.edge['p2p_supplicant']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['system_server']['fill'] = 'red'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][write read]'
G.edge['p2p_supplicant']['wpa']['fill'] = 'red'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read]'
G.add_edge('shell','debuggerd')
G.edge['shell']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('shell','dumpstate')
G.edge['shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('shell','init_shell')
G.edge['shell']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('shell','logwrapper')
G.edge['shell']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('shell','netd')
G.edge['shell']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('shell','p2p_supplicant')
G.edge['shell']['p2p_supplicant']['write-read'] = '[open open]'
G.add_edge('shell','s_system_app')
G.edge['shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('shell','system_server')
G.edge['shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][open open]'
G.add_edge('shell','wpa')
G.edge['shell']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('shell','debuggerd')
G.edge['shell']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('shell','dumpstate')
G.edge['shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('shell','hostapd')
G.edge['shell']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('shell','init_shell')
G.edge['shell']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('shell','logwrapper')
G.edge['shell']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('shell','netd')
G.edge['shell']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('shell','p2p_supplicant')
G.edge['shell']['p2p_supplicant']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','p2p_supplicant')
G.edge['shell']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr]'
G.add_edge('shell','s_system_app')
G.edge['shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('shell','system_server')
G.edge['shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('shell','debuggerd')
G.edge['shell']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['shell']['debuggerd']['fill'] = 'red'
G.add_edge('shell','debuggerd')
G.edge['shell']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('shell','dumpstate')
G.edge['shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['shell']['dumpstate']['fill'] = 'red'
G.add_edge('shell','dumpstate')
G.edge['shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('shell','hostapd')
G.edge['shell']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['shell']['hostapd']['fill'] = 'red'
G.add_edge('shell','init_shell')
G.edge['shell']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['shell']['init_shell']['fill'] = 'red'
G.add_edge('shell','init_shell')
G.edge['shell']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('shell','logwrapper')
G.edge['shell']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['shell']['logwrapper']['fill'] = 'red'
G.add_edge('shell','logwrapper')
G.edge['shell']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('shell','netd')
G.edge['shell']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['shell']['netd']['fill'] = 'red'
G.add_edge('shell','netd')
G.edge['shell']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('shell','p2p_supplicant')
G.edge['shell']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read]'
G.edge['shell']['p2p_supplicant']['fill'] = 'red'
G.add_edge('shell','p2p_supplicant')
G.edge['shell']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('shell','p2p_supplicant')
G.edge['shell']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['shell']['p2p_supplicant']['fill'] = 'red'
G.add_edge('shell','s_system_app')
G.edge['shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['shell']['s_system_app']['fill'] = 'red'
G.add_edge('shell','s_system_app')
G.edge['shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('shell','system_server')
G.edge['shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['shell']['system_server']['fill'] = 'red'
G.add_edge('shell','system_server')
G.edge['shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('shell','wpa')
G.edge['shell']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['shell']['wpa']['fill'] = 'red'
G.add_edge('shell','wpa')
G.edge['shell']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open]'
G.add_edge('s_system_app','dumpstate')
G.edge['s_system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open]'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr]'
G.add_edge('s_system_app','dumpstate')
G.edge['s_system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr]'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read]'
G.edge['s_system_app']['debuggerd']['fill'] = 'red'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','dumpstate')
G.edge['s_system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['dumpstate']['fill'] = 'red'
G.add_edge('s_system_app','dumpstate')
G.edge['s_system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read]'
G.edge['s_system_app']['hostapd']['fill'] = 'red'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['init_shell']['fill'] = 'red'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['logwrapper']['fill'] = 'red'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['netd']['fill'] = 'red'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read]'
G.edge['s_system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['s_system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['system_server']['fill'] = 'red'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read]'
G.edge['s_system_app']['wpa']['fill'] = 'red'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read]'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','dumpstate')
G.edge['s_system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read][open open]'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','dumpstate')
G.edge['s_system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][setattr getattr]'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['debuggerd']['fill'] = 'red'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','dumpstate')
G.edge['s_system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['dumpstate']['fill'] = 'red'
G.add_edge('s_system_app','dumpstate')
G.edge['s_system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][setattr getattr][write read]'
G.edge['s_system_app']['hostapd']['fill'] = 'red'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['init_shell']['fill'] = 'red'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['logwrapper']['fill'] = 'red'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['netd']['fill'] = 'red'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read]'
G.edge['s_system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['s_system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['system_server']['fill'] = 'red'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read][open open][write read]'
G.edge['s_system_app']['wpa']['fill'] = 'red'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_app','debuggerd')
G.edge['system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open]'
G.add_edge('system_app','dumpstate')
G.edge['system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_app','logwrapper')
G.edge['system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','p2p_supplicant')
G.edge['system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','wpa')
G.edge['system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open]'
G.add_edge('system_app','debuggerd')
G.edge['system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr]'
G.add_edge('system_app','dumpstate')
G.edge['system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_app','hostapd')
G.edge['system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr]'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','logwrapper')
G.edge['system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_app','p2p_supplicant')
G.edge['system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr]'
G.add_edge('system_app','p2p_supplicant')
G.edge['system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','debuggerd')
G.edge['system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read]'
G.edge['system_app']['debuggerd']['fill'] = 'red'
G.add_edge('system_app','debuggerd')
G.edge['system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','dumpstate')
G.edge['system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_app']['dumpstate']['fill'] = 'red'
G.add_edge('system_app','dumpstate')
G.edge['system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','hostapd')
G.edge['system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read]'
G.edge['system_app']['hostapd']['fill'] = 'red'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['init_shell']['fill'] = 'red'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','logwrapper')
G.edge['system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_app']['logwrapper']['fill'] = 'red'
G.add_edge('system_app','logwrapper')
G.edge['system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_app']['netd']['fill'] = 'red'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','p2p_supplicant')
G.edge['system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read]'
G.edge['system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('system_app','p2p_supplicant')
G.edge['system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('system_app','p2p_supplicant')
G.edge['system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_app']['s_system_app']['fill'] = 'red'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['system_server']['fill'] = 'red'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','wpa')
G.edge['system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read]'
G.edge['system_app']['wpa']['fill'] = 'red'
G.add_edge('system_app','wpa')
G.edge['system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read]'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','logwrapper')
G.edge['system_server']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','p2p_supplicant')
G.edge['system_server']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','wpa')
G.edge['system_server']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','hostapd')
G.edge['system_server']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','logwrapper')
G.edge['system_server']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','p2p_supplicant')
G.edge['system_server']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr]'
G.add_edge('system_server','p2p_supplicant')
G.edge['system_server']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['debuggerd']['fill'] = 'red'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['dumpstate']['fill'] = 'red'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','hostapd')
G.edge['system_server']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['system_server']['hostapd']['fill'] = 'red'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['init_shell']['fill'] = 'red'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','logwrapper')
G.edge['system_server']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['logwrapper']['fill'] = 'red'
G.add_edge('system_server','logwrapper')
G.edge['system_server']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['netd']['fill'] = 'red'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','p2p_supplicant')
G.edge['system_server']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read]'
G.edge['system_server']['p2p_supplicant']['fill'] = 'red'
G.add_edge('system_server','p2p_supplicant')
G.edge['system_server']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('system_server','p2p_supplicant')
G.edge['system_server']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['system_server']['p2p_supplicant']['fill'] = 'red'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['s_system_app']['fill'] = 'red'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','wpa')
G.edge['system_server']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['system_server']['wpa']['fill'] = 'red'
G.add_edge('system_server','wpa')
G.edge['system_server']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
app = Viewer(G)
app.mainloop()