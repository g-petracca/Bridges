import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('cnd','debuggerd')
G.edge['cnd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('cnd','debuggerd')
G.edge['cnd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('cnd','dumpstate')
G.edge['cnd']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('cnd','dumpstate')
G.edge['cnd']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('cnd','hostapd')
G.edge['cnd']['hostapd']['write-read'] = '[open open][write read][add_name search][remove_name search][add_name search]'
G.add_edge('cnd','hostapd')
G.edge['cnd']['hostapd']['write-read'] = '[open open][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('cnd','init_shell')
G.edge['cnd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('cnd','init_shell')
G.edge['cnd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('cnd','logwrapper')
G.edge['cnd']['logwrapper']['write-read'] = '[add_name search]'
G.add_edge('cnd','logwrapper')
G.edge['cnd']['logwrapper']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('cnd','netd')
G.edge['cnd']['netd']['write-read'] = '[add_name search]'
G.add_edge('cnd','netd')
G.edge['cnd']['netd']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('cnd','netd')
G.edge['cnd']['netd']['write-read'] = '[add_name search][remove_name search][add_name search]'
G.add_edge('cnd','netd')
G.edge['cnd']['netd']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('cnd','p2p_supplicant')
G.edge['cnd']['p2p_supplicant']['write-read'] = '[add_name search][remove_name search][add_name search]'
G.add_edge('cnd','p2p_supplicant')
G.edge['cnd']['p2p_supplicant']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('cnd','p2p_supplicant')
G.edge['cnd']['p2p_supplicant']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('cnd','p2p_supplicant')
G.edge['cnd']['p2p_supplicant']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('cnd','p2p_supplicant')
G.edge['cnd']['p2p_supplicant']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('cnd','p2p_supplicant')
G.edge['cnd']['p2p_supplicant']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('cnd','s_system_app')
G.edge['cnd']['s_system_app']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][add_name search]'
G.add_edge('cnd','s_system_app')
G.edge['cnd']['s_system_app']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][add_name search][remove_name search]'
G.add_edge('cnd','system_server')
G.edge['cnd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search]'
G.add_edge('cnd','system_server')
G.edge['cnd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('cnd','vold')
G.edge['cnd']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('cnd','vold')
G.edge['cnd']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('cnd','wcnss_service')
G.edge['cnd']['wcnss_service']['write-read'] = '[add_name search]'
G.add_edge('cnd','wcnss_service')
G.edge['cnd']['wcnss_service']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('cnd','wcnss_service')
G.edge['cnd']['wcnss_service']['write-read'] = '[add_name search][remove_name search][add_name search]'
G.add_edge('cnd','wcnss_service')
G.edge['cnd']['wcnss_service']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('cnd','wpa')
G.edge['cnd']['wpa']['write-read'] = '[add_name search]'
G.add_edge('cnd','wpa')
G.edge['cnd']['wpa']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('debuggerd','debuggerd')
G.edge['debuggerd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('debuggerd','dumpstate')
G.edge['debuggerd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('debuggerd','hostapd')
G.edge['debuggerd']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('debuggerd','init_shell')
G.edge['debuggerd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('debuggerd','logwrapper')
G.edge['debuggerd']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('debuggerd','netd')
G.edge['debuggerd']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('debuggerd','netd')
G.edge['debuggerd']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('debuggerd','p2p_supplicant')
G.edge['debuggerd']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open]'
G.add_edge('debuggerd','p2p_supplicant')
G.edge['debuggerd']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('debuggerd','s_system_app')
G.edge['debuggerd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open]'
G.add_edge('debuggerd','system_server')
G.edge['debuggerd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('debuggerd','vold')
G.edge['debuggerd']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('debuggerd','wcnss_service')
G.edge['debuggerd']['wcnss_service']['write-read'] = '[open open]'
G.add_edge('debuggerd','wcnss_service')
G.edge['debuggerd']['wcnss_service']['write-read'] = '[open open][open open]'
G.add_edge('debuggerd','wpa')
G.edge['debuggerd']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('debuggerd','hostapd')
G.edge['debuggerd']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('debuggerd','init_shell')
G.edge['debuggerd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('debuggerd','netd')
G.edge['debuggerd']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('debuggerd','p2p_supplicant')
G.edge['debuggerd']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('debuggerd','system_server')
G.edge['debuggerd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('debuggerd','wpa')
G.edge['debuggerd']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('debuggerd','debuggerd')
G.edge['debuggerd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['debuggerd']['debuggerd']['fill'] = 'red'
G.add_edge('debuggerd','dumpstate')
G.edge['debuggerd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['debuggerd']['dumpstate']['fill'] = 'red'
G.add_edge('debuggerd','hostapd')
G.edge['debuggerd']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['debuggerd']['hostapd']['fill'] = 'red'
G.add_edge('debuggerd','init_shell')
G.edge['debuggerd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['debuggerd']['init_shell']['fill'] = 'red'
G.add_edge('debuggerd','logwrapper')
G.edge['debuggerd']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['debuggerd']['logwrapper']['fill'] = 'red'
G.add_edge('debuggerd','netd')
G.edge['debuggerd']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['debuggerd']['netd']['fill'] = 'red'
G.add_edge('debuggerd','netd')
G.edge['debuggerd']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read]'
G.edge['debuggerd']['netd']['fill'] = 'red'
G.add_edge('debuggerd','p2p_supplicant')
G.edge['debuggerd']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['debuggerd']['p2p_supplicant']['fill'] = 'red'
G.add_edge('debuggerd','p2p_supplicant')
G.edge['debuggerd']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read]'
G.edge['debuggerd']['p2p_supplicant']['fill'] = 'red'
G.add_edge('debuggerd','p2p_supplicant')
G.edge['debuggerd']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read]'
G.edge['debuggerd']['p2p_supplicant']['fill'] = 'red'
G.add_edge('debuggerd','s_system_app')
G.edge['debuggerd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read]'
G.edge['debuggerd']['s_system_app']['fill'] = 'red'
G.add_edge('debuggerd','system_server')
G.edge['debuggerd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['debuggerd']['system_server']['fill'] = 'red'
G.add_edge('debuggerd','vold')
G.edge['debuggerd']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['debuggerd']['vold']['fill'] = 'red'
G.add_edge('debuggerd','wcnss_service')
G.edge['debuggerd']['wcnss_service']['write-read'] = '[open open][open open][write read]'
G.edge['debuggerd']['wcnss_service']['fill'] = 'red'
G.add_edge('debuggerd','wcnss_service')
G.edge['debuggerd']['wcnss_service']['write-read'] = '[open open][open open][write read][write read]'
G.edge['debuggerd']['wcnss_service']['fill'] = 'red'
G.add_edge('debuggerd','wpa')
G.edge['debuggerd']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['debuggerd']['wpa']['fill'] = 'red'
G.add_edge('debuggerd','debuggerd')
G.edge['debuggerd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('debuggerd','debuggerd')
G.edge['debuggerd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','dumpstate')
G.edge['debuggerd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('debuggerd','dumpstate')
G.edge['debuggerd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','hostapd')
G.edge['debuggerd']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','hostapd')
G.edge['debuggerd']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','init_shell')
G.edge['debuggerd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','init_shell')
G.edge['debuggerd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','logwrapper')
G.edge['debuggerd']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('debuggerd','logwrapper')
G.edge['debuggerd']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','netd')
G.edge['debuggerd']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search]'
G.add_edge('debuggerd','netd')
G.edge['debuggerd']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','netd')
G.edge['debuggerd']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('debuggerd','netd')
G.edge['debuggerd']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('debuggerd','p2p_supplicant')
G.edge['debuggerd']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('debuggerd','p2p_supplicant')
G.edge['debuggerd']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','p2p_supplicant')
G.edge['debuggerd']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('debuggerd','p2p_supplicant')
G.edge['debuggerd']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('debuggerd','p2p_supplicant')
G.edge['debuggerd']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('debuggerd','p2p_supplicant')
G.edge['debuggerd']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('debuggerd','s_system_app')
G.edge['debuggerd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][add_name search]'
G.add_edge('debuggerd','s_system_app')
G.edge['debuggerd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','system_server')
G.edge['debuggerd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','system_server')
G.edge['debuggerd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','vold')
G.edge['debuggerd']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('debuggerd','vold')
G.edge['debuggerd']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','wcnss_service')
G.edge['debuggerd']['wcnss_service']['write-read'] = '[open open][open open][write read][write read][add_name search]'
G.add_edge('debuggerd','wcnss_service')
G.edge['debuggerd']['wcnss_service']['write-read'] = '[open open][open open][write read][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','wcnss_service')
G.edge['debuggerd']['wcnss_service']['write-read'] = '[open open][open open][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('debuggerd','wcnss_service')
G.edge['debuggerd']['wcnss_service']['write-read'] = '[open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('debuggerd','wpa')
G.edge['debuggerd']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','wpa')
G.edge['debuggerd']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','debuggerd')
G.edge['dumpstate']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','hostapd')
G.edge['dumpstate']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','init_shell')
G.edge['dumpstate']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','logwrapper')
G.edge['dumpstate']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('dumpstate','netd')
G.edge['dumpstate']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','netd')
G.edge['dumpstate']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][open open]'
G.add_edge('dumpstate','p2p_supplicant')
G.edge['dumpstate']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','p2p_supplicant')
G.edge['dumpstate']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open]'
G.add_edge('dumpstate','s_system_app')
G.edge['dumpstate']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','system_server')
G.edge['dumpstate']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','vold')
G.edge['dumpstate']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','wcnss_service')
G.edge['dumpstate']['wcnss_service']['write-read'] = '[open open]'
G.add_edge('dumpstate','wcnss_service')
G.edge['dumpstate']['wcnss_service']['write-read'] = '[open open][open open]'
G.add_edge('dumpstate','wpa')
G.edge['dumpstate']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('dumpstate','hostapd')
G.edge['dumpstate']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('dumpstate','init_shell')
G.edge['dumpstate']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('dumpstate','netd')
G.edge['dumpstate']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('dumpstate','p2p_supplicant')
G.edge['dumpstate']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('dumpstate','system_server')
G.edge['dumpstate']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('dumpstate','wpa')
G.edge['dumpstate']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('dumpstate','debuggerd')
G.edge['dumpstate']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['dumpstate']['debuggerd']['fill'] = 'red'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['dumpstate']['dumpstate']['fill'] = 'red'
G.add_edge('dumpstate','hostapd')
G.edge['dumpstate']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['dumpstate']['hostapd']['fill'] = 'red'
G.add_edge('dumpstate','init_shell')
G.edge['dumpstate']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['dumpstate']['init_shell']['fill'] = 'red'
G.add_edge('dumpstate','logwrapper')
G.edge['dumpstate']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['dumpstate']['logwrapper']['fill'] = 'red'
G.add_edge('dumpstate','netd')
G.edge['dumpstate']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['dumpstate']['netd']['fill'] = 'red'
G.add_edge('dumpstate','netd')
G.edge['dumpstate']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read]'
G.edge['dumpstate']['netd']['fill'] = 'red'
G.add_edge('dumpstate','p2p_supplicant')
G.edge['dumpstate']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['dumpstate']['p2p_supplicant']['fill'] = 'red'
G.add_edge('dumpstate','p2p_supplicant')
G.edge['dumpstate']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read]'
G.edge['dumpstate']['p2p_supplicant']['fill'] = 'red'
G.add_edge('dumpstate','p2p_supplicant')
G.edge['dumpstate']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read]'
G.edge['dumpstate']['p2p_supplicant']['fill'] = 'red'
G.add_edge('dumpstate','s_system_app')
G.edge['dumpstate']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['dumpstate']['s_system_app']['fill'] = 'red'
G.add_edge('dumpstate','system_server')
G.edge['dumpstate']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['dumpstate']['system_server']['fill'] = 'red'
G.add_edge('dumpstate','vold')
G.edge['dumpstate']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['dumpstate']['vold']['fill'] = 'red'
G.add_edge('dumpstate','wcnss_service')
G.edge['dumpstate']['wcnss_service']['write-read'] = '[open open][open open][write read]'
G.edge['dumpstate']['wcnss_service']['fill'] = 'red'
G.add_edge('dumpstate','wcnss_service')
G.edge['dumpstate']['wcnss_service']['write-read'] = '[open open][open open][write read][write read]'
G.edge['dumpstate']['wcnss_service']['fill'] = 'red'
G.add_edge('dumpstate','wpa')
G.edge['dumpstate']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['dumpstate']['wpa']['fill'] = 'red'
G.add_edge('dumpstate','debuggerd')
G.edge['dumpstate']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('dumpstate','debuggerd')
G.edge['dumpstate']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','hostapd')
G.edge['dumpstate']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','hostapd')
G.edge['dumpstate']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','init_shell')
G.edge['dumpstate']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','init_shell')
G.edge['dumpstate']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','logwrapper')
G.edge['dumpstate']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('dumpstate','logwrapper')
G.edge['dumpstate']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','netd')
G.edge['dumpstate']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search]'
G.add_edge('dumpstate','netd')
G.edge['dumpstate']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','netd')
G.edge['dumpstate']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('dumpstate','netd')
G.edge['dumpstate']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('dumpstate','p2p_supplicant')
G.edge['dumpstate']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('dumpstate','p2p_supplicant')
G.edge['dumpstate']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','p2p_supplicant')
G.edge['dumpstate']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('dumpstate','p2p_supplicant')
G.edge['dumpstate']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('dumpstate','p2p_supplicant')
G.edge['dumpstate']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('dumpstate','p2p_supplicant')
G.edge['dumpstate']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('dumpstate','s_system_app')
G.edge['dumpstate']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('dumpstate','s_system_app')
G.edge['dumpstate']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','system_server')
G.edge['dumpstate']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','system_server')
G.edge['dumpstate']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','vold')
G.edge['dumpstate']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('dumpstate','vold')
G.edge['dumpstate']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','wcnss_service')
G.edge['dumpstate']['wcnss_service']['write-read'] = '[open open][open open][write read][write read][add_name search]'
G.add_edge('dumpstate','wcnss_service')
G.edge['dumpstate']['wcnss_service']['write-read'] = '[open open][open open][write read][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','wcnss_service')
G.edge['dumpstate']['wcnss_service']['write-read'] = '[open open][open open][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('dumpstate','wcnss_service')
G.edge['dumpstate']['wcnss_service']['write-read'] = '[open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('dumpstate','wpa')
G.edge['dumpstate']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','wpa')
G.edge['dumpstate']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','debuggerd')
G.edge['hostapd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('hostapd','dumpstate')
G.edge['hostapd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('hostapd','hostapd')
G.edge['hostapd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('hostapd','init_shell')
G.edge['hostapd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('hostapd','logwrapper')
G.edge['hostapd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('hostapd','netd')
G.edge['hostapd']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('hostapd','netd')
G.edge['hostapd']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('hostapd','p2p_supplicant')
G.edge['hostapd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][add_name search][remove_name search][open open]'
G.add_edge('hostapd','p2p_supplicant')
G.edge['hostapd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('hostapd','s_system_app')
G.edge['hostapd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('hostapd','system_server')
G.edge['hostapd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('hostapd','vold')
G.edge['hostapd']['vold']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('hostapd','wcnss_service')
G.edge['hostapd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('hostapd','wcnss_service')
G.edge['hostapd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open]'
G.add_edge('hostapd','wpa')
G.edge['hostapd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('hostapd','hostapd')
G.edge['hostapd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('hostapd','init_shell')
G.edge['hostapd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('hostapd','netd')
G.edge['hostapd']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('hostapd','p2p_supplicant')
G.edge['hostapd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('hostapd','system_server')
G.edge['hostapd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('hostapd','wpa')
G.edge['hostapd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('hostapd','debuggerd')
G.edge['hostapd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['hostapd']['debuggerd']['fill'] = 'red'
G.add_edge('hostapd','dumpstate')
G.edge['hostapd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['hostapd']['dumpstate']['fill'] = 'red'
G.add_edge('hostapd','hostapd')
G.edge['hostapd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['hostapd']['hostapd']['fill'] = 'red'
G.add_edge('hostapd','init_shell')
G.edge['hostapd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['hostapd']['init_shell']['fill'] = 'red'
G.add_edge('hostapd','logwrapper')
G.edge['hostapd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['hostapd']['logwrapper']['fill'] = 'red'
G.add_edge('hostapd','netd')
G.edge['hostapd']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['hostapd']['netd']['fill'] = 'red'
G.add_edge('hostapd','netd')
G.edge['hostapd']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read]'
G.edge['hostapd']['netd']['fill'] = 'red'
G.add_edge('hostapd','p2p_supplicant')
G.edge['hostapd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['hostapd']['p2p_supplicant']['fill'] = 'red'
G.add_edge('hostapd','p2p_supplicant')
G.edge['hostapd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read]'
G.edge['hostapd']['p2p_supplicant']['fill'] = 'red'
G.add_edge('hostapd','p2p_supplicant')
G.edge['hostapd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read]'
G.edge['hostapd']['p2p_supplicant']['fill'] = 'red'
G.add_edge('hostapd','s_system_app')
G.edge['hostapd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['hostapd']['s_system_app']['fill'] = 'red'
G.add_edge('hostapd','system_server')
G.edge['hostapd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['hostapd']['system_server']['fill'] = 'red'
G.add_edge('hostapd','vold')
G.edge['hostapd']['vold']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['hostapd']['vold']['fill'] = 'red'
G.add_edge('hostapd','wcnss_service')
G.edge['hostapd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read]'
G.edge['hostapd']['wcnss_service']['fill'] = 'red'
G.add_edge('hostapd','wcnss_service')
G.edge['hostapd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read]'
G.edge['hostapd']['wcnss_service']['fill'] = 'red'
G.add_edge('hostapd','wpa')
G.edge['hostapd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['hostapd']['wpa']['fill'] = 'red'
G.add_edge('hostapd','debuggerd')
G.edge['hostapd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('hostapd','debuggerd')
G.edge['hostapd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('hostapd','dumpstate')
G.edge['hostapd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('hostapd','dumpstate')
G.edge['hostapd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('hostapd','hostapd')
G.edge['hostapd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','hostapd')
G.edge['hostapd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','init_shell')
G.edge['hostapd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','init_shell')
G.edge['hostapd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','logwrapper')
G.edge['hostapd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('hostapd','logwrapper')
G.edge['hostapd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('hostapd','netd')
G.edge['hostapd']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search]'
G.add_edge('hostapd','netd')
G.edge['hostapd']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search]'
G.add_edge('hostapd','netd')
G.edge['hostapd']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('hostapd','netd')
G.edge['hostapd']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('hostapd','p2p_supplicant')
G.edge['hostapd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('hostapd','p2p_supplicant')
G.edge['hostapd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('hostapd','p2p_supplicant')
G.edge['hostapd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('hostapd','p2p_supplicant')
G.edge['hostapd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('hostapd','p2p_supplicant')
G.edge['hostapd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('hostapd','p2p_supplicant')
G.edge['hostapd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('hostapd','s_system_app')
G.edge['hostapd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('hostapd','s_system_app')
G.edge['hostapd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('hostapd','system_server')
G.edge['hostapd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','system_server')
G.edge['hostapd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','vold')
G.edge['hostapd']['vold']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('hostapd','vold')
G.edge['hostapd']['vold']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('hostapd','wcnss_service')
G.edge['hostapd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search]'
G.add_edge('hostapd','wcnss_service')
G.edge['hostapd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search]'
G.add_edge('hostapd','wcnss_service')
G.edge['hostapd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('hostapd','wcnss_service')
G.edge['hostapd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('hostapd','wpa')
G.edge['hostapd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','wpa')
G.edge['hostapd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','debuggerd')
G.edge['ime_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','dumpstate')
G.edge['ime_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','hostapd')
G.edge['ime_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('ime_app','logwrapper')
G.edge['ime_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('ime_app','p2p_supplicant')
G.edge['ime_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','p2p_supplicant')
G.edge['ime_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','vold')
G.edge['ime_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open]'
G.add_edge('ime_app','wcnss_service')
G.edge['ime_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('ime_app','wcnss_service')
G.edge['ime_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open]'
G.add_edge('ime_app','wpa')
G.edge['ime_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read][open open]'
G.add_edge('ime_app','hostapd')
G.edge['ime_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('ime_app','p2p_supplicant')
G.edge['ime_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ime_app','wpa')
G.edge['ime_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','debuggerd')
G.edge['ime_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['ime_app']['debuggerd']['fill'] = 'red'
G.add_edge('ime_app','dumpstate')
G.edge['ime_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['ime_app']['dumpstate']['fill'] = 'red'
G.add_edge('ime_app','hostapd')
G.edge['ime_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['hostapd']['fill'] = 'red'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['ime_app']['init_shell']['fill'] = 'red'
G.add_edge('ime_app','logwrapper')
G.edge['ime_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['ime_app']['logwrapper']['fill'] = 'red'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['ime_app']['netd']['fill'] = 'red'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read]'
G.edge['ime_app']['netd']['fill'] = 'red'
G.add_edge('ime_app','p2p_supplicant')
G.edge['ime_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['ime_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('ime_app','p2p_supplicant')
G.edge['ime_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read]'
G.edge['ime_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('ime_app','p2p_supplicant')
G.edge['ime_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read]'
G.edge['ime_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['ime_app']['s_system_app']['fill'] = 'red'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ime_app']['system_server']['fill'] = 'red'
G.add_edge('ime_app','vold')
G.edge['ime_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][write read]'
G.edge['ime_app']['vold']['fill'] = 'red'
G.add_edge('ime_app','wcnss_service')
G.edge['ime_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read]'
G.edge['ime_app']['wcnss_service']['fill'] = 'red'
G.add_edge('ime_app','wcnss_service')
G.edge['ime_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read]'
G.edge['ime_app']['wcnss_service']['fill'] = 'red'
G.add_edge('ime_app','wpa')
G.edge['ime_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['wpa']['fill'] = 'red'
G.add_edge('ime_app','debuggerd')
G.edge['ime_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('ime_app','debuggerd')
G.edge['ime_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('ime_app','dumpstate')
G.edge['ime_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('ime_app','dumpstate')
G.edge['ime_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('ime_app','hostapd')
G.edge['ime_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','hostapd')
G.edge['ime_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','logwrapper')
G.edge['ime_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('ime_app','logwrapper')
G.edge['ime_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search]'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search]'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('ime_app','p2p_supplicant')
G.edge['ime_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('ime_app','p2p_supplicant')
G.edge['ime_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('ime_app','p2p_supplicant')
G.edge['ime_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('ime_app','p2p_supplicant')
G.edge['ime_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('ime_app','p2p_supplicant')
G.edge['ime_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('ime_app','p2p_supplicant')
G.edge['ime_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','vold')
G.edge['ime_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search]'
G.add_edge('ime_app','vold')
G.edge['ime_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search]'
G.add_edge('ime_app','wcnss_service')
G.edge['ime_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search]'
G.add_edge('ime_app','wcnss_service')
G.edge['ime_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search]'
G.add_edge('ime_app','wcnss_service')
G.edge['ime_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('ime_app','wcnss_service')
G.edge['ime_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('ime_app','wpa')
G.edge['ime_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','wpa')
G.edge['ime_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ims','debuggerd')
G.edge['ims']['debuggerd']['write-read'] = '[open open]'
G.add_edge('ims','dumpstate')
G.edge['ims']['dumpstate']['write-read'] = '[open open]'
G.add_edge('ims','hostapd')
G.edge['ims']['hostapd']['write-read'] = '[open open]'
G.add_edge('ims','init_shell')
G.edge['ims']['init_shell']['write-read'] = '[open open]'
G.add_edge('ims','logwrapper')
G.edge['ims']['logwrapper']['write-read'] = '[open open]'
G.add_edge('ims','netd')
G.edge['ims']['netd']['write-read'] = '[open open]'
G.add_edge('ims','netd')
G.edge['ims']['netd']['write-read'] = '[open open][open open]'
G.add_edge('ims','p2p_supplicant')
G.edge['ims']['p2p_supplicant']['write-read'] = '[open open]'
G.add_edge('ims','p2p_supplicant')
G.edge['ims']['p2p_supplicant']['write-read'] = '[open open][open open]'
G.add_edge('ims','s_system_app')
G.edge['ims']['s_system_app']['write-read'] = '[open open]'
G.add_edge('ims','system_server')
G.edge['ims']['system_server']['write-read'] = '[open open]'
G.add_edge('ims','vold')
G.edge['ims']['vold']['write-read'] = '[open open]'
G.add_edge('ims','wcnss_service')
G.edge['ims']['wcnss_service']['write-read'] = '[open open]'
G.add_edge('ims','wcnss_service')
G.edge['ims']['wcnss_service']['write-read'] = '[open open][open open]'
G.add_edge('ims','wpa')
G.edge['ims']['wpa']['write-read'] = '[open open]'
G.add_edge('ims','hostapd')
G.edge['ims']['hostapd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ims','init_shell')
G.edge['ims']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ims','netd')
G.edge['ims']['netd']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('ims','p2p_supplicant')
G.edge['ims']['p2p_supplicant']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('ims','system_server')
G.edge['ims']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ims','wpa')
G.edge['ims']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ims','debuggerd')
G.edge['ims']['debuggerd']['write-read'] = '[open open][write read]'
G.edge['ims']['debuggerd']['fill'] = 'red'
G.add_edge('ims','dumpstate')
G.edge['ims']['dumpstate']['write-read'] = '[open open][write read]'
G.edge['ims']['dumpstate']['fill'] = 'red'
G.add_edge('ims','hostapd')
G.edge['ims']['hostapd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ims']['hostapd']['fill'] = 'red'
G.add_edge('ims','init_shell')
G.edge['ims']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ims']['init_shell']['fill'] = 'red'
G.add_edge('ims','logwrapper')
G.edge['ims']['logwrapper']['write-read'] = '[open open][write read]'
G.edge['ims']['logwrapper']['fill'] = 'red'
G.add_edge('ims','netd')
G.edge['ims']['netd']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['ims']['netd']['fill'] = 'red'
G.add_edge('ims','netd')
G.edge['ims']['netd']['write-read'] = '[open open][open open][setattr getattr][write read][write read]'
G.edge['ims']['netd']['fill'] = 'red'
G.add_edge('ims','p2p_supplicant')
G.edge['ims']['p2p_supplicant']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['ims']['p2p_supplicant']['fill'] = 'red'
G.add_edge('ims','p2p_supplicant')
G.edge['ims']['p2p_supplicant']['write-read'] = '[open open][open open][setattr getattr][write read][write read]'
G.edge['ims']['p2p_supplicant']['fill'] = 'red'
G.add_edge('ims','p2p_supplicant')
G.edge['ims']['p2p_supplicant']['write-read'] = '[open open][open open][setattr getattr][write read][write read][write read]'
G.edge['ims']['p2p_supplicant']['fill'] = 'red'
G.add_edge('ims','s_system_app')
G.edge['ims']['s_system_app']['write-read'] = '[open open][write read]'
G.edge['ims']['s_system_app']['fill'] = 'red'
G.add_edge('ims','system_server')
G.edge['ims']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ims']['system_server']['fill'] = 'red'
G.add_edge('ims','vold')
G.edge['ims']['vold']['write-read'] = '[open open][write read]'
G.edge['ims']['vold']['fill'] = 'red'
G.add_edge('ims','wcnss_service')
G.edge['ims']['wcnss_service']['write-read'] = '[open open][open open][write read]'
G.edge['ims']['wcnss_service']['fill'] = 'red'
G.add_edge('ims','wcnss_service')
G.edge['ims']['wcnss_service']['write-read'] = '[open open][open open][write read][write read]'
G.edge['ims']['wcnss_service']['fill'] = 'red'
G.add_edge('ims','wpa')
G.edge['ims']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ims']['wpa']['fill'] = 'red'
G.add_edge('ims','debuggerd')
G.edge['ims']['debuggerd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('ims','debuggerd')
G.edge['ims']['debuggerd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('ims','dumpstate')
G.edge['ims']['dumpstate']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('ims','dumpstate')
G.edge['ims']['dumpstate']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('ims','hostapd')
G.edge['ims']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('ims','hostapd')
G.edge['ims']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ims','init_shell')
G.edge['ims']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('ims','init_shell')
G.edge['ims']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ims','logwrapper')
G.edge['ims']['logwrapper']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('ims','logwrapper')
G.edge['ims']['logwrapper']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('ims','netd')
G.edge['ims']['netd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search]'
G.add_edge('ims','netd')
G.edge['ims']['netd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search]'
G.add_edge('ims','netd')
G.edge['ims']['netd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('ims','netd')
G.edge['ims']['netd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('ims','p2p_supplicant')
G.edge['ims']['p2p_supplicant']['write-read'] = '[open open][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('ims','p2p_supplicant')
G.edge['ims']['p2p_supplicant']['write-read'] = '[open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('ims','p2p_supplicant')
G.edge['ims']['p2p_supplicant']['write-read'] = '[open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('ims','p2p_supplicant')
G.edge['ims']['p2p_supplicant']['write-read'] = '[open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('ims','p2p_supplicant')
G.edge['ims']['p2p_supplicant']['write-read'] = '[open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('ims','p2p_supplicant')
G.edge['ims']['p2p_supplicant']['write-read'] = '[open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('ims','s_system_app')
G.edge['ims']['s_system_app']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('ims','s_system_app')
G.edge['ims']['s_system_app']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('ims','system_server')
G.edge['ims']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('ims','system_server')
G.edge['ims']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ims','vold')
G.edge['ims']['vold']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('ims','vold')
G.edge['ims']['vold']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('ims','wcnss_service')
G.edge['ims']['wcnss_service']['write-read'] = '[open open][open open][write read][write read][add_name search]'
G.add_edge('ims','wcnss_service')
G.edge['ims']['wcnss_service']['write-read'] = '[open open][open open][write read][write read][add_name search][remove_name search]'
G.add_edge('ims','wcnss_service')
G.edge['ims']['wcnss_service']['write-read'] = '[open open][open open][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('ims','wcnss_service')
G.edge['ims']['wcnss_service']['write-read'] = '[open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('ims','wpa')
G.edge['ims']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('ims','wpa')
G.edge['ims']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','debuggerd')
G.edge['init_shell']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','dumpstate')
G.edge['init_shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','hostapd')
G.edge['init_shell']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','logwrapper')
G.edge['init_shell']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','netd')
G.edge['init_shell']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','netd')
G.edge['init_shell']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('init_shell','p2p_supplicant')
G.edge['init_shell']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','p2p_supplicant')
G.edge['init_shell']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('init_shell','s_system_app')
G.edge['init_shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open]'
G.add_edge('init_shell','wcnss_service')
G.edge['init_shell']['wcnss_service']['write-read'] = '[open open]'
G.add_edge('init_shell','wcnss_service')
G.edge['init_shell']['wcnss_service']['write-read'] = '[open open][open open]'
G.add_edge('init_shell','wpa')
G.edge['init_shell']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('init_shell','hostapd')
G.edge['init_shell']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','netd')
G.edge['init_shell']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('init_shell','p2p_supplicant')
G.edge['init_shell']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('init_shell','wpa')
G.edge['init_shell']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','debuggerd')
G.edge['init_shell']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['debuggerd']['fill'] = 'red'
G.add_edge('init_shell','dumpstate')
G.edge['init_shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['dumpstate']['fill'] = 'red'
G.add_edge('init_shell','hostapd')
G.edge['init_shell']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['hostapd']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['init_shell']['fill'] = 'red'
G.add_edge('init_shell','logwrapper')
G.edge['init_shell']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['init_shell']['logwrapper']['fill'] = 'red'
G.add_edge('init_shell','netd')
G.edge['init_shell']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['init_shell']['netd']['fill'] = 'red'
G.add_edge('init_shell','netd')
G.edge['init_shell']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read]'
G.edge['init_shell']['netd']['fill'] = 'red'
G.add_edge('init_shell','p2p_supplicant')
G.edge['init_shell']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['init_shell']['p2p_supplicant']['fill'] = 'red'
G.add_edge('init_shell','p2p_supplicant')
G.edge['init_shell']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read]'
G.edge['init_shell']['p2p_supplicant']['fill'] = 'red'
G.add_edge('init_shell','p2p_supplicant')
G.edge['init_shell']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read]'
G.edge['init_shell']['p2p_supplicant']['fill'] = 'red'
G.add_edge('init_shell','s_system_app')
G.edge['init_shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['s_system_app']['fill'] = 'red'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['init_shell']['system_server']['fill'] = 'red'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][write read]'
G.edge['init_shell']['vold']['fill'] = 'red'
G.add_edge('init_shell','wcnss_service')
G.edge['init_shell']['wcnss_service']['write-read'] = '[open open][open open][write read]'
G.edge['init_shell']['wcnss_service']['fill'] = 'red'
G.add_edge('init_shell','wcnss_service')
G.edge['init_shell']['wcnss_service']['write-read'] = '[open open][open open][write read][write read]'
G.edge['init_shell']['wcnss_service']['fill'] = 'red'
G.add_edge('init_shell','wpa')
G.edge['init_shell']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['wpa']['fill'] = 'red'
G.add_edge('init_shell','debuggerd')
G.edge['init_shell']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('init_shell','debuggerd')
G.edge['init_shell']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('init_shell','dumpstate')
G.edge['init_shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('init_shell','dumpstate')
G.edge['init_shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('init_shell','hostapd')
G.edge['init_shell']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','hostapd')
G.edge['init_shell']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','logwrapper')
G.edge['init_shell']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('init_shell','logwrapper')
G.edge['init_shell']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('init_shell','netd')
G.edge['init_shell']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search]'
G.add_edge('init_shell','netd')
G.edge['init_shell']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search]'
G.add_edge('init_shell','netd')
G.edge['init_shell']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('init_shell','netd')
G.edge['init_shell']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('init_shell','p2p_supplicant')
G.edge['init_shell']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('init_shell','p2p_supplicant')
G.edge['init_shell']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('init_shell','p2p_supplicant')
G.edge['init_shell']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('init_shell','p2p_supplicant')
G.edge['init_shell']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('init_shell','p2p_supplicant')
G.edge['init_shell']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('init_shell','p2p_supplicant')
G.edge['init_shell']['p2p_supplicant']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('init_shell','s_system_app')
G.edge['init_shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('init_shell','s_system_app')
G.edge['init_shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][write read][add_name search]'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][write read][add_name search][remove_name search]'
G.add_edge('init_shell','wcnss_service')
G.edge['init_shell']['wcnss_service']['write-read'] = '[open open][open open][write read][write read][add_name search]'
G.add_edge('init_shell','wcnss_service')
G.edge['init_shell']['wcnss_service']['write-read'] = '[open open][open open][write read][write read][add_name search][remove_name search]'
G.add_edge('init_shell','wcnss_service')
G.edge['init_shell']['wcnss_service']['write-read'] = '[open open][open open][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('init_shell','wcnss_service')
G.edge['init_shell']['wcnss_service']['write-read'] = '[open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('init_shell','wpa')
G.edge['init_shell']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','wpa')
G.edge['init_shell']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('knox_system_app','debuggerd')
G.edge['knox_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open]'
G.add_edge('knox_system_app','dumpstate')
G.edge['knox_system_app']['dumpstate']['write-read'] = '[open open]'
G.add_edge('knox_system_app','hostapd')
G.edge['knox_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('knox_system_app','init_shell')
G.edge['knox_system_app']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_system_app','logwrapper')
G.edge['knox_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('knox_system_app','netd')
G.edge['knox_system_app']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('knox_system_app','netd')
G.edge['knox_system_app']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][open open]'
G.add_edge('knox_system_app','p2p_supplicant')
G.edge['knox_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open]'
G.add_edge('knox_system_app','p2p_supplicant')
G.edge['knox_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open]'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_system_app','vold')
G.edge['knox_system_app']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_system_app','wcnss_service')
G.edge['knox_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('knox_system_app','wcnss_service')
G.edge['knox_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open]'
G.add_edge('knox_system_app','wpa')
G.edge['knox_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_system_app','hostapd')
G.edge['knox_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('knox_system_app','init_shell')
G.edge['knox_system_app']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('knox_system_app','netd')
G.edge['knox_system_app']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][open open][setattr getattr]'
G.add_edge('knox_system_app','p2p_supplicant')
G.edge['knox_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][setattr getattr]'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('knox_system_app','wpa')
G.edge['knox_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('knox_system_app','debuggerd')
G.edge['knox_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][write read]'
G.edge['knox_system_app']['debuggerd']['fill'] = 'red'
G.add_edge('knox_system_app','dumpstate')
G.edge['knox_system_app']['dumpstate']['write-read'] = '[open open][write read]'
G.edge['knox_system_app']['dumpstate']['fill'] = 'red'
G.add_edge('knox_system_app','hostapd')
G.edge['knox_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_system_app']['hostapd']['fill'] = 'red'
G.add_edge('knox_system_app','init_shell')
G.edge['knox_system_app']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['knox_system_app']['init_shell']['fill'] = 'red'
G.add_edge('knox_system_app','logwrapper')
G.edge['knox_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['knox_system_app']['logwrapper']['fill'] = 'red'
G.add_edge('knox_system_app','netd')
G.edge['knox_system_app']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['knox_system_app']['netd']['fill'] = 'red'
G.add_edge('knox_system_app','netd')
G.edge['knox_system_app']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][write read]'
G.edge['knox_system_app']['netd']['fill'] = 'red'
G.add_edge('knox_system_app','p2p_supplicant')
G.edge['knox_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read]'
G.edge['knox_system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('knox_system_app','p2p_supplicant')
G.edge['knox_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read][write read]'
G.edge['knox_system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('knox_system_app','p2p_supplicant')
G.edge['knox_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read]'
G.edge['knox_system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['knox_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['knox_system_app']['system_server']['fill'] = 'red'
G.add_edge('knox_system_app','vold')
G.edge['knox_system_app']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['knox_system_app']['vold']['fill'] = 'red'
G.add_edge('knox_system_app','wcnss_service')
G.edge['knox_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read]'
G.edge['knox_system_app']['wcnss_service']['fill'] = 'red'
G.add_edge('knox_system_app','wcnss_service')
G.edge['knox_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read]'
G.edge['knox_system_app']['wcnss_service']['fill'] = 'red'
G.add_edge('knox_system_app','wpa')
G.edge['knox_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_system_app']['wpa']['fill'] = 'red'
G.add_edge('knox_system_app','debuggerd')
G.edge['knox_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search]'
G.add_edge('knox_system_app','debuggerd')
G.edge['knox_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search]'
G.add_edge('knox_system_app','dumpstate')
G.edge['knox_system_app']['dumpstate']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('knox_system_app','dumpstate')
G.edge['knox_system_app']['dumpstate']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('knox_system_app','hostapd')
G.edge['knox_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('knox_system_app','hostapd')
G.edge['knox_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('knox_system_app','init_shell')
G.edge['knox_system_app']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('knox_system_app','init_shell')
G.edge['knox_system_app']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('knox_system_app','logwrapper')
G.edge['knox_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][add_name search]'
G.add_edge('knox_system_app','logwrapper')
G.edge['knox_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('knox_system_app','netd')
G.edge['knox_system_app']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search]'
G.add_edge('knox_system_app','netd')
G.edge['knox_system_app']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search]'
G.add_edge('knox_system_app','netd')
G.edge['knox_system_app']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('knox_system_app','netd')
G.edge['knox_system_app']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('knox_system_app','p2p_supplicant')
G.edge['knox_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('knox_system_app','p2p_supplicant')
G.edge['knox_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('knox_system_app','p2p_supplicant')
G.edge['knox_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('knox_system_app','p2p_supplicant')
G.edge['knox_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('knox_system_app','p2p_supplicant')
G.edge['knox_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('knox_system_app','p2p_supplicant')
G.edge['knox_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('knox_system_app','vold')
G.edge['knox_system_app']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('knox_system_app','vold')
G.edge['knox_system_app']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('knox_system_app','wcnss_service')
G.edge['knox_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search]'
G.add_edge('knox_system_app','wcnss_service')
G.edge['knox_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search]'
G.add_edge('knox_system_app','wcnss_service')
G.edge['knox_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('knox_system_app','wcnss_service')
G.edge['knox_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('knox_system_app','wpa')
G.edge['knox_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('knox_system_app','wpa')
G.edge['knox_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','debuggerd')
G.edge['logwrapper']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('logwrapper','dumpstate')
G.edge['logwrapper']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('logwrapper','hostapd')
G.edge['logwrapper']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open]'
G.add_edge('logwrapper','init_shell')
G.edge['logwrapper']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('logwrapper','logwrapper')
G.edge['logwrapper']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('logwrapper','netd')
G.edge['logwrapper']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('logwrapper','netd')
G.edge['logwrapper']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('logwrapper','p2p_supplicant')
G.edge['logwrapper']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open]'
G.add_edge('logwrapper','p2p_supplicant')
G.edge['logwrapper']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open]'
G.add_edge('logwrapper','s_system_app')
G.edge['logwrapper']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('logwrapper','system_server')
G.edge['logwrapper']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('logwrapper','vold')
G.edge['logwrapper']['vold']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('logwrapper','wcnss_service')
G.edge['logwrapper']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('logwrapper','wcnss_service')
G.edge['logwrapper']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open]'
G.add_edge('logwrapper','wpa')
G.edge['logwrapper']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('logwrapper','hostapd')
G.edge['logwrapper']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][setattr getattr]'
G.add_edge('logwrapper','init_shell')
G.edge['logwrapper']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('logwrapper','netd')
G.edge['logwrapper']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('logwrapper','p2p_supplicant')
G.edge['logwrapper']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr]'
G.add_edge('logwrapper','system_server')
G.edge['logwrapper']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('logwrapper','wpa')
G.edge['logwrapper']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('logwrapper','debuggerd')
G.edge['logwrapper']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['logwrapper']['debuggerd']['fill'] = 'red'
G.add_edge('logwrapper','dumpstate')
G.edge['logwrapper']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['logwrapper']['dumpstate']['fill'] = 'red'
G.add_edge('logwrapper','hostapd')
G.edge['logwrapper']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][setattr getattr][write read]'
G.edge['logwrapper']['hostapd']['fill'] = 'red'
G.add_edge('logwrapper','init_shell')
G.edge['logwrapper']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['logwrapper']['init_shell']['fill'] = 'red'
G.add_edge('logwrapper','logwrapper')
G.edge['logwrapper']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['logwrapper']['logwrapper']['fill'] = 'red'
G.add_edge('logwrapper','netd')
G.edge['logwrapper']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['logwrapper']['netd']['fill'] = 'red'
G.add_edge('logwrapper','netd')
G.edge['logwrapper']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read]'
G.edge['logwrapper']['netd']['fill'] = 'red'
G.add_edge('logwrapper','p2p_supplicant')
G.edge['logwrapper']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read]'
G.edge['logwrapper']['p2p_supplicant']['fill'] = 'red'
G.add_edge('logwrapper','p2p_supplicant')
G.edge['logwrapper']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read]'
G.edge['logwrapper']['p2p_supplicant']['fill'] = 'red'
G.add_edge('logwrapper','p2p_supplicant')
G.edge['logwrapper']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read]'
G.edge['logwrapper']['p2p_supplicant']['fill'] = 'red'
G.add_edge('logwrapper','s_system_app')
G.edge['logwrapper']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['logwrapper']['s_system_app']['fill'] = 'red'
G.add_edge('logwrapper','system_server')
G.edge['logwrapper']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['logwrapper']['system_server']['fill'] = 'red'
G.add_edge('logwrapper','vold')
G.edge['logwrapper']['vold']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['logwrapper']['vold']['fill'] = 'red'
G.add_edge('logwrapper','wcnss_service')
G.edge['logwrapper']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read]'
G.edge['logwrapper']['wcnss_service']['fill'] = 'red'
G.add_edge('logwrapper','wcnss_service')
G.edge['logwrapper']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read]'
G.edge['logwrapper']['wcnss_service']['fill'] = 'red'
G.add_edge('logwrapper','wpa')
G.edge['logwrapper']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['logwrapper']['wpa']['fill'] = 'red'
G.add_edge('logwrapper','debuggerd')
G.edge['logwrapper']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('logwrapper','debuggerd')
G.edge['logwrapper']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','dumpstate')
G.edge['logwrapper']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('logwrapper','dumpstate')
G.edge['logwrapper']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','hostapd')
G.edge['logwrapper']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','hostapd')
G.edge['logwrapper']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','init_shell')
G.edge['logwrapper']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','init_shell')
G.edge['logwrapper']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','logwrapper')
G.edge['logwrapper']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('logwrapper','logwrapper')
G.edge['logwrapper']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','netd')
G.edge['logwrapper']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search]'
G.add_edge('logwrapper','netd')
G.edge['logwrapper']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','netd')
G.edge['logwrapper']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('logwrapper','netd')
G.edge['logwrapper']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('logwrapper','p2p_supplicant')
G.edge['logwrapper']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('logwrapper','p2p_supplicant')
G.edge['logwrapper']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','p2p_supplicant')
G.edge['logwrapper']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('logwrapper','p2p_supplicant')
G.edge['logwrapper']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('logwrapper','p2p_supplicant')
G.edge['logwrapper']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('logwrapper','p2p_supplicant')
G.edge['logwrapper']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('logwrapper','s_system_app')
G.edge['logwrapper']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('logwrapper','s_system_app')
G.edge['logwrapper']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','system_server')
G.edge['logwrapper']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','system_server')
G.edge['logwrapper']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','vold')
G.edge['logwrapper']['vold']['write-read'] = '[open open][write read][append read][open open][write read][add_name search]'
G.add_edge('logwrapper','vold')
G.edge['logwrapper']['vold']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','wcnss_service')
G.edge['logwrapper']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search]'
G.add_edge('logwrapper','wcnss_service')
G.edge['logwrapper']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','wcnss_service')
G.edge['logwrapper']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('logwrapper','wcnss_service')
G.edge['logwrapper']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('logwrapper','wpa')
G.edge['logwrapper']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','wpa')
G.edge['logwrapper']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','debuggerd')
G.edge['netd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('netd','dumpstate')
G.edge['netd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','hostapd')
G.edge['netd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open]'
G.add_edge('netd','init_shell')
G.edge['netd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','logwrapper')
G.edge['netd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open]'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('netd','vold')
G.edge['netd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','wcnss_service')
G.edge['netd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('netd','wcnss_service')
G.edge['netd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open]'
G.add_edge('netd','wpa')
G.edge['netd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('netd','hostapd')
G.edge['netd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][setattr getattr]'
G.add_edge('netd','init_shell')
G.edge['netd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('netd','wpa')
G.edge['netd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('netd','debuggerd')
G.edge['netd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['netd']['debuggerd']['fill'] = 'red'
G.add_edge('netd','dumpstate')
G.edge['netd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['netd']['dumpstate']['fill'] = 'red'
G.add_edge('netd','hostapd')
G.edge['netd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][setattr getattr][write read]'
G.edge['netd']['hostapd']['fill'] = 'red'
G.add_edge('netd','init_shell')
G.edge['netd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['netd']['init_shell']['fill'] = 'red'
G.add_edge('netd','logwrapper')
G.edge['netd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['netd']['logwrapper']['fill'] = 'red'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['netd']['netd']['fill'] = 'red'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read]'
G.edge['netd']['netd']['fill'] = 'red'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read]'
G.edge['netd']['p2p_supplicant']['fill'] = 'red'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read]'
G.edge['netd']['p2p_supplicant']['fill'] = 'red'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read]'
G.edge['netd']['p2p_supplicant']['fill'] = 'red'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['netd']['s_system_app']['fill'] = 'red'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['netd']['system_server']['fill'] = 'red'
G.add_edge('netd','vold')
G.edge['netd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['netd']['vold']['fill'] = 'red'
G.add_edge('netd','wcnss_service')
G.edge['netd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read]'
G.edge['netd']['wcnss_service']['fill'] = 'red'
G.add_edge('netd','wcnss_service')
G.edge['netd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read]'
G.edge['netd']['wcnss_service']['fill'] = 'red'
G.add_edge('netd','wpa')
G.edge['netd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['netd']['wpa']['fill'] = 'red'
G.add_edge('netd','debuggerd')
G.edge['netd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('netd','debuggerd')
G.edge['netd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('netd','dumpstate')
G.edge['netd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('netd','dumpstate')
G.edge['netd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('netd','hostapd')
G.edge['netd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','hostapd')
G.edge['netd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','init_shell')
G.edge['netd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','init_shell')
G.edge['netd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','logwrapper')
G.edge['netd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('netd','logwrapper')
G.edge['netd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','vold')
G.edge['netd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('netd','vold')
G.edge['netd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('netd','wcnss_service')
G.edge['netd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search]'
G.add_edge('netd','wcnss_service')
G.edge['netd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search]'
G.add_edge('netd','wcnss_service')
G.edge['netd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('netd','wcnss_service')
G.edge['netd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('netd','wpa')
G.edge['netd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','wpa')
G.edge['netd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','debuggerd')
G.edge['netd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','dumpstate')
G.edge['netd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','hostapd')
G.edge['netd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','init_shell')
G.edge['netd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','logwrapper')
G.edge['netd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open]'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','vold')
G.edge['netd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','wcnss_service')
G.edge['netd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('netd','wcnss_service')
G.edge['netd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open]'
G.add_edge('netd','wpa')
G.edge['netd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','hostapd')
G.edge['netd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('netd','init_shell')
G.edge['netd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('netd','wpa')
G.edge['netd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('netd','debuggerd')
G.edge['netd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['netd']['debuggerd']['fill'] = 'red'
G.add_edge('netd','dumpstate')
G.edge['netd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['netd']['dumpstate']['fill'] = 'red'
G.add_edge('netd','hostapd')
G.edge['netd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['netd']['hostapd']['fill'] = 'red'
G.add_edge('netd','init_shell')
G.edge['netd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['netd']['init_shell']['fill'] = 'red'
G.add_edge('netd','logwrapper')
G.edge['netd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['netd']['logwrapper']['fill'] = 'red'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['netd']['netd']['fill'] = 'red'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read]'
G.edge['netd']['netd']['fill'] = 'red'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['netd']['p2p_supplicant']['fill'] = 'red'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read]'
G.edge['netd']['p2p_supplicant']['fill'] = 'red'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read]'
G.edge['netd']['p2p_supplicant']['fill'] = 'red'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['netd']['s_system_app']['fill'] = 'red'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['netd']['system_server']['fill'] = 'red'
G.add_edge('netd','vold')
G.edge['netd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['netd']['vold']['fill'] = 'red'
G.add_edge('netd','wcnss_service')
G.edge['netd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read]'
G.edge['netd']['wcnss_service']['fill'] = 'red'
G.add_edge('netd','wcnss_service')
G.edge['netd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read]'
G.edge['netd']['wcnss_service']['fill'] = 'red'
G.add_edge('netd','wpa')
G.edge['netd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['netd']['wpa']['fill'] = 'red'
G.add_edge('netd','debuggerd')
G.edge['netd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('netd','debuggerd')
G.edge['netd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('netd','dumpstate')
G.edge['netd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('netd','dumpstate')
G.edge['netd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('netd','hostapd')
G.edge['netd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','hostapd')
G.edge['netd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','init_shell')
G.edge['netd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','init_shell')
G.edge['netd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','logwrapper')
G.edge['netd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('netd','logwrapper')
G.edge['netd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','vold')
G.edge['netd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('netd','vold')
G.edge['netd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('netd','wcnss_service')
G.edge['netd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search]'
G.add_edge('netd','wcnss_service')
G.edge['netd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][remove_name search]'
G.add_edge('netd','wcnss_service')
G.edge['netd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('netd','wcnss_service')
G.edge['netd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('netd','wpa')
G.edge['netd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','wpa')
G.edge['netd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','debuggerd')
G.edge['p2p_supplicant']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('p2p_supplicant','dumpstate')
G.edge['p2p_supplicant']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('p2p_supplicant','hostapd')
G.edge['p2p_supplicant']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][open open]'
G.add_edge('p2p_supplicant','init_shell')
G.edge['p2p_supplicant']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('p2p_supplicant','logwrapper')
G.edge['p2p_supplicant']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open]'
G.add_edge('p2p_supplicant','s_system_app')
G.edge['p2p_supplicant']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('p2p_supplicant','vold')
G.edge['p2p_supplicant']['vold']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open]'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open]'
G.add_edge('p2p_supplicant','hostapd')
G.edge['p2p_supplicant']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][open open][setattr getattr]'
G.add_edge('p2p_supplicant','init_shell')
G.edge['p2p_supplicant']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr]'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('p2p_supplicant','debuggerd')
G.edge['p2p_supplicant']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['p2p_supplicant']['debuggerd']['fill'] = 'red'
G.add_edge('p2p_supplicant','dumpstate')
G.edge['p2p_supplicant']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['p2p_supplicant']['dumpstate']['fill'] = 'red'
G.add_edge('p2p_supplicant','hostapd')
G.edge['p2p_supplicant']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['hostapd']['fill'] = 'red'
G.add_edge('p2p_supplicant','init_shell')
G.edge['p2p_supplicant']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['init_shell']['fill'] = 'red'
G.add_edge('p2p_supplicant','logwrapper')
G.edge['p2p_supplicant']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['p2p_supplicant']['logwrapper']['fill'] = 'red'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['netd']['fill'] = 'red'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read]'
G.edge['p2p_supplicant']['netd']['fill'] = 'red'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['p2p_supplicant']['fill'] = 'red'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read]'
G.edge['p2p_supplicant']['p2p_supplicant']['fill'] = 'red'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read]'
G.edge['p2p_supplicant']['p2p_supplicant']['fill'] = 'red'
G.add_edge('p2p_supplicant','s_system_app')
G.edge['p2p_supplicant']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['p2p_supplicant']['s_system_app']['fill'] = 'red'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['system_server']['fill'] = 'red'
G.add_edge('p2p_supplicant','vold')
G.edge['p2p_supplicant']['vold']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['p2p_supplicant']['vold']['fill'] = 'red'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read]'
G.edge['p2p_supplicant']['wcnss_service']['fill'] = 'red'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read]'
G.edge['p2p_supplicant']['wcnss_service']['fill'] = 'red'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['wpa']['fill'] = 'red'
G.add_edge('p2p_supplicant','debuggerd')
G.edge['p2p_supplicant']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('p2p_supplicant','debuggerd')
G.edge['p2p_supplicant']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','dumpstate')
G.edge['p2p_supplicant']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('p2p_supplicant','dumpstate')
G.edge['p2p_supplicant']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','hostapd')
G.edge['p2p_supplicant']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('p2p_supplicant','hostapd')
G.edge['p2p_supplicant']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','init_shell')
G.edge['p2p_supplicant']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('p2p_supplicant','init_shell')
G.edge['p2p_supplicant']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','logwrapper')
G.edge['p2p_supplicant']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('p2p_supplicant','logwrapper')
G.edge['p2p_supplicant']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','s_system_app')
G.edge['p2p_supplicant']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('p2p_supplicant','s_system_app')
G.edge['p2p_supplicant']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','vold')
G.edge['p2p_supplicant']['vold']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('p2p_supplicant','vold')
G.edge['p2p_supplicant']['vold']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','debuggerd')
G.edge['p2p_supplicant']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('p2p_supplicant','dumpstate')
G.edge['p2p_supplicant']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('p2p_supplicant','hostapd')
G.edge['p2p_supplicant']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('p2p_supplicant','init_shell')
G.edge['p2p_supplicant']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('p2p_supplicant','logwrapper')
G.edge['p2p_supplicant']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open]'
G.add_edge('p2p_supplicant','s_system_app')
G.edge['p2p_supplicant']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('p2p_supplicant','vold')
G.edge['p2p_supplicant']['vold']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open]'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('p2p_supplicant','hostapd')
G.edge['p2p_supplicant']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('p2p_supplicant','init_shell')
G.edge['p2p_supplicant']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('p2p_supplicant','debuggerd')
G.edge['p2p_supplicant']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['p2p_supplicant']['debuggerd']['fill'] = 'red'
G.add_edge('p2p_supplicant','dumpstate')
G.edge['p2p_supplicant']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['p2p_supplicant']['dumpstate']['fill'] = 'red'
G.add_edge('p2p_supplicant','hostapd')
G.edge['p2p_supplicant']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['hostapd']['fill'] = 'red'
G.add_edge('p2p_supplicant','init_shell')
G.edge['p2p_supplicant']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['init_shell']['fill'] = 'red'
G.add_edge('p2p_supplicant','logwrapper')
G.edge['p2p_supplicant']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['p2p_supplicant']['logwrapper']['fill'] = 'red'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['netd']['fill'] = 'red'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read]'
G.edge['p2p_supplicant']['netd']['fill'] = 'red'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['p2p_supplicant']['fill'] = 'red'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read]'
G.edge['p2p_supplicant']['p2p_supplicant']['fill'] = 'red'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read]'
G.edge['p2p_supplicant']['p2p_supplicant']['fill'] = 'red'
G.add_edge('p2p_supplicant','s_system_app')
G.edge['p2p_supplicant']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['p2p_supplicant']['s_system_app']['fill'] = 'red'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['system_server']['fill'] = 'red'
G.add_edge('p2p_supplicant','vold')
G.edge['p2p_supplicant']['vold']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['p2p_supplicant']['vold']['fill'] = 'red'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read]'
G.edge['p2p_supplicant']['wcnss_service']['fill'] = 'red'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read]'
G.edge['p2p_supplicant']['wcnss_service']['fill'] = 'red'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['wpa']['fill'] = 'red'
G.add_edge('p2p_supplicant','debuggerd')
G.edge['p2p_supplicant']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('p2p_supplicant','debuggerd')
G.edge['p2p_supplicant']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','dumpstate')
G.edge['p2p_supplicant']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('p2p_supplicant','dumpstate')
G.edge['p2p_supplicant']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','hostapd')
G.edge['p2p_supplicant']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('p2p_supplicant','hostapd')
G.edge['p2p_supplicant']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','init_shell')
G.edge['p2p_supplicant']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('p2p_supplicant','init_shell')
G.edge['p2p_supplicant']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','logwrapper')
G.edge['p2p_supplicant']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('p2p_supplicant','logwrapper')
G.edge['p2p_supplicant']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','s_system_app')
G.edge['p2p_supplicant']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('p2p_supplicant','s_system_app')
G.edge['p2p_supplicant']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','vold')
G.edge['p2p_supplicant']['vold']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('p2p_supplicant','vold')
G.edge['p2p_supplicant']['vold']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','debuggerd')
G.edge['p2p_supplicant']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('p2p_supplicant','dumpstate')
G.edge['p2p_supplicant']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('p2p_supplicant','hostapd')
G.edge['p2p_supplicant']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('p2p_supplicant','init_shell')
G.edge['p2p_supplicant']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('p2p_supplicant','logwrapper')
G.edge['p2p_supplicant']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open]'
G.add_edge('p2p_supplicant','s_system_app')
G.edge['p2p_supplicant']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('p2p_supplicant','vold')
G.edge['p2p_supplicant']['vold']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open]'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('p2p_supplicant','hostapd')
G.edge['p2p_supplicant']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('p2p_supplicant','init_shell')
G.edge['p2p_supplicant']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('p2p_supplicant','debuggerd')
G.edge['p2p_supplicant']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['p2p_supplicant']['debuggerd']['fill'] = 'red'
G.add_edge('p2p_supplicant','dumpstate')
G.edge['p2p_supplicant']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['p2p_supplicant']['dumpstate']['fill'] = 'red'
G.add_edge('p2p_supplicant','hostapd')
G.edge['p2p_supplicant']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['hostapd']['fill'] = 'red'
G.add_edge('p2p_supplicant','init_shell')
G.edge['p2p_supplicant']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['init_shell']['fill'] = 'red'
G.add_edge('p2p_supplicant','logwrapper')
G.edge['p2p_supplicant']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['p2p_supplicant']['logwrapper']['fill'] = 'red'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['netd']['fill'] = 'red'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read]'
G.edge['p2p_supplicant']['netd']['fill'] = 'red'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['p2p_supplicant']['fill'] = 'red'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read]'
G.edge['p2p_supplicant']['p2p_supplicant']['fill'] = 'red'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read]'
G.edge['p2p_supplicant']['p2p_supplicant']['fill'] = 'red'
G.add_edge('p2p_supplicant','s_system_app')
G.edge['p2p_supplicant']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['p2p_supplicant']['s_system_app']['fill'] = 'red'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['system_server']['fill'] = 'red'
G.add_edge('p2p_supplicant','vold')
G.edge['p2p_supplicant']['vold']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['p2p_supplicant']['vold']['fill'] = 'red'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read]'
G.edge['p2p_supplicant']['wcnss_service']['fill'] = 'red'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read]'
G.edge['p2p_supplicant']['wcnss_service']['fill'] = 'red'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['wpa']['fill'] = 'red'
G.add_edge('p2p_supplicant','debuggerd')
G.edge['p2p_supplicant']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('p2p_supplicant','debuggerd')
G.edge['p2p_supplicant']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','dumpstate')
G.edge['p2p_supplicant']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('p2p_supplicant','dumpstate')
G.edge['p2p_supplicant']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','hostapd')
G.edge['p2p_supplicant']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('p2p_supplicant','hostapd')
G.edge['p2p_supplicant']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','init_shell')
G.edge['p2p_supplicant']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('p2p_supplicant','init_shell')
G.edge['p2p_supplicant']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','logwrapper')
G.edge['p2p_supplicant']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('p2p_supplicant','logwrapper')
G.edge['p2p_supplicant']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','s_system_app')
G.edge['p2p_supplicant']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('p2p_supplicant','s_system_app')
G.edge['p2p_supplicant']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','vold')
G.edge['p2p_supplicant']['vold']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('p2p_supplicant','vold')
G.edge['p2p_supplicant']['vold']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','dumpstate')
G.edge['s_system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][append read][write read][append read][open open]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open]'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open]'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr]'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['s_system_app']['debuggerd']['fill'] = 'red'
G.add_edge('s_system_app','dumpstate')
G.edge['s_system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['s_system_app']['dumpstate']['fill'] = 'red'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['hostapd']['fill'] = 'red'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['s_system_app']['init_shell']['fill'] = 'red'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['s_system_app']['logwrapper']['fill'] = 'red'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['s_system_app']['netd']['fill'] = 'red'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read]'
G.edge['s_system_app']['netd']['fill'] = 'red'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['s_system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read]'
G.edge['s_system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read]'
G.edge['s_system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][append read][write read][append read][open open][write read]'
G.edge['s_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read]'
G.edge['s_system_app']['system_server']['fill'] = 'red'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['s_system_app']['vold']['fill'] = 'red'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read]'
G.edge['s_system_app']['wcnss_service']['fill'] = 'red'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read]'
G.edge['s_system_app']['wcnss_service']['fill'] = 'red'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['wpa']['fill'] = 'red'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','dumpstate')
G.edge['s_system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('s_system_app','dumpstate')
G.edge['s_system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][append read][write read][append read][open open][write read][add_name search]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][append read][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search]'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','dumpstate')
G.edge['s_system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][append read][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open]'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['s_system_app']['debuggerd']['fill'] = 'red'
G.add_edge('s_system_app','dumpstate')
G.edge['s_system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['s_system_app']['dumpstate']['fill'] = 'red'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['hostapd']['fill'] = 'red'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['init_shell']['fill'] = 'red'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['s_system_app']['logwrapper']['fill'] = 'red'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['s_system_app']['netd']['fill'] = 'red'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read]'
G.edge['s_system_app']['netd']['fill'] = 'red'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['s_system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read]'
G.edge['s_system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read]'
G.edge['s_system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['s_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['system_server']['fill'] = 'red'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['s_system_app']['vold']['fill'] = 'red'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read]'
G.edge['s_system_app']['wcnss_service']['fill'] = 'red'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read]'
G.edge['s_system_app']['wcnss_service']['fill'] = 'red'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['wpa']['fill'] = 'red'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','dumpstate')
G.edge['s_system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('s_system_app','dumpstate')
G.edge['s_system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search]'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','debuggerd')
G.edge['system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','dumpstate')
G.edge['system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','hostapd')
G.edge['system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('system_app','logwrapper')
G.edge['system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('system_app','p2p_supplicant')
G.edge['system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','p2p_supplicant')
G.edge['system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open]'
G.add_edge('system_app','vold')
G.edge['system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open]'
G.add_edge('system_app','wcnss_service')
G.edge['system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('system_app','wcnss_service')
G.edge['system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open]'
G.add_edge('system_app','wpa')
G.edge['system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_app','hostapd')
G.edge['system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('system_app','p2p_supplicant')
G.edge['system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr]'
G.add_edge('system_app','wpa')
G.edge['system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','debuggerd')
G.edge['system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_app']['debuggerd']['fill'] = 'red'
G.add_edge('system_app','dumpstate')
G.edge['system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_app']['dumpstate']['fill'] = 'red'
G.add_edge('system_app','hostapd')
G.edge['system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['hostapd']['fill'] = 'red'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['system_app']['init_shell']['fill'] = 'red'
G.add_edge('system_app','logwrapper')
G.edge['system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['system_app']['logwrapper']['fill'] = 'red'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['system_app']['netd']['fill'] = 'red'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read]'
G.edge['system_app']['netd']['fill'] = 'red'
G.add_edge('system_app','p2p_supplicant')
G.edge['system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('system_app','p2p_supplicant')
G.edge['system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read]'
G.edge['system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('system_app','p2p_supplicant')
G.edge['system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read]'
G.edge['system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['system_app']['s_system_app']['fill'] = 'red'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read]'
G.edge['system_app']['system_server']['fill'] = 'red'
G.add_edge('system_app','vold')
G.edge['system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][write read]'
G.edge['system_app']['vold']['fill'] = 'red'
G.add_edge('system_app','wcnss_service')
G.edge['system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read]'
G.edge['system_app']['wcnss_service']['fill'] = 'red'
G.add_edge('system_app','wcnss_service')
G.edge['system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read]'
G.edge['system_app']['wcnss_service']['fill'] = 'red'
G.add_edge('system_app','wpa')
G.edge['system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['wpa']['fill'] = 'red'
G.add_edge('system_app','debuggerd')
G.edge['system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('system_app','debuggerd')
G.edge['system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('system_app','dumpstate')
G.edge['system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('system_app','dumpstate')
G.edge['system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('system_app','hostapd')
G.edge['system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','hostapd')
G.edge['system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','logwrapper')
G.edge['system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('system_app','logwrapper')
G.edge['system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search]'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search]'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('system_app','p2p_supplicant')
G.edge['system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('system_app','p2p_supplicant')
G.edge['system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('system_app','p2p_supplicant')
G.edge['system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('system_app','p2p_supplicant')
G.edge['system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('system_app','p2p_supplicant')
G.edge['system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('system_app','p2p_supplicant')
G.edge['system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','vold')
G.edge['system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search]'
G.add_edge('system_app','vold')
G.edge['system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search]'
G.add_edge('system_app','wcnss_service')
G.edge['system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search]'
G.add_edge('system_app','wcnss_service')
G.edge['system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search]'
G.add_edge('system_app','wcnss_service')
G.edge['system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('system_app','wcnss_service')
G.edge['system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('system_app','wpa')
G.edge['system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','wpa')
G.edge['system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('system_server','hostapd')
G.edge['system_server']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','logwrapper')
G.edge['system_server']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('system_server','p2p_supplicant')
G.edge['system_server']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','p2p_supplicant')
G.edge['system_server']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','wcnss_service')
G.edge['system_server']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('system_server','wcnss_service')
G.edge['system_server']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open]'
G.add_edge('system_server','wpa')
G.edge['system_server']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open]'
G.add_edge('system_server','hostapd')
G.edge['system_server']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('system_server','p2p_supplicant')
G.edge['system_server']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('system_server','wpa')
G.edge['system_server']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['debuggerd']['fill'] = 'red'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['dumpstate']['fill'] = 'red'
G.add_edge('system_server','hostapd')
G.edge['system_server']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['hostapd']['fill'] = 'red'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['init_shell']['fill'] = 'red'
G.add_edge('system_server','logwrapper')
G.edge['system_server']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['system_server']['logwrapper']['fill'] = 'red'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['system_server']['netd']['fill'] = 'red'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read]'
G.edge['system_server']['netd']['fill'] = 'red'
G.add_edge('system_server','p2p_supplicant')
G.edge['system_server']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['system_server']['p2p_supplicant']['fill'] = 'red'
G.add_edge('system_server','p2p_supplicant')
G.edge['system_server']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read]'
G.edge['system_server']['p2p_supplicant']['fill'] = 'red'
G.add_edge('system_server','p2p_supplicant')
G.edge['system_server']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read]'
G.edge['system_server']['p2p_supplicant']['fill'] = 'red'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['system_server']['s_system_app']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['vold']['fill'] = 'red'
G.add_edge('system_server','wcnss_service')
G.edge['system_server']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read]'
G.edge['system_server']['wcnss_service']['fill'] = 'red'
G.add_edge('system_server','wcnss_service')
G.edge['system_server']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read]'
G.edge['system_server']['wcnss_service']['fill'] = 'red'
G.add_edge('system_server','wpa')
G.edge['system_server']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['wpa']['fill'] = 'red'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('system_server','hostapd')
G.edge['system_server']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','hostapd')
G.edge['system_server']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','logwrapper')
G.edge['system_server']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('system_server','logwrapper')
G.edge['system_server']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search]'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search]'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('system_server','p2p_supplicant')
G.edge['system_server']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('system_server','p2p_supplicant')
G.edge['system_server']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('system_server','p2p_supplicant')
G.edge['system_server']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('system_server','p2p_supplicant')
G.edge['system_server']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('system_server','p2p_supplicant')
G.edge['system_server']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('system_server','p2p_supplicant')
G.edge['system_server']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('system_server','wcnss_service')
G.edge['system_server']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search]'
G.add_edge('system_server','wcnss_service')
G.edge['system_server']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search]'
G.add_edge('system_server','wcnss_service')
G.edge['system_server']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('system_server','wcnss_service')
G.edge['system_server']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('system_server','wpa')
G.edge['system_server']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','wpa')
G.edge['system_server']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ueventd','debuggerd')
G.edge['ueventd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('ueventd','debuggerd')
G.edge['ueventd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('ueventd','dumpstate')
G.edge['ueventd']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('ueventd','dumpstate')
G.edge['ueventd']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('ueventd','hostapd')
G.edge['ueventd']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][add_name search]'
G.add_edge('ueventd','hostapd')
G.edge['ueventd']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('ueventd','init_shell')
G.edge['ueventd']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search]'
G.add_edge('ueventd','init_shell')
G.edge['ueventd']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search]'
G.add_edge('ueventd','logwrapper')
G.edge['ueventd']['logwrapper']['write-read'] = '[open open][write read][append read][add_name search]'
G.add_edge('ueventd','logwrapper')
G.edge['ueventd']['logwrapper']['write-read'] = '[open open][write read][append read][add_name search][remove_name search]'
G.add_edge('ueventd','netd')
G.edge['ueventd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][add_name search]'
G.add_edge('ueventd','netd')
G.edge['ueventd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][add_name search][remove_name search]'
G.add_edge('ueventd','netd')
G.edge['ueventd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][add_name search][remove_name search][add_name search]'
G.add_edge('ueventd','netd')
G.edge['ueventd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('ueventd','p2p_supplicant')
G.edge['ueventd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('ueventd','p2p_supplicant')
G.edge['ueventd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('ueventd','p2p_supplicant')
G.edge['ueventd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('ueventd','p2p_supplicant')
G.edge['ueventd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('ueventd','p2p_supplicant')
G.edge['ueventd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('ueventd','p2p_supplicant')
G.edge['ueventd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('ueventd','s_system_app')
G.edge['ueventd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][add_name search]'
G.add_edge('ueventd','s_system_app')
G.edge['ueventd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][add_name search][remove_name search]'
G.add_edge('ueventd','system_server')
G.edge['ueventd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('ueventd','system_server')
G.edge['ueventd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('ueventd','vold')
G.edge['ueventd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][append read][add_name search]'
G.add_edge('ueventd','vold')
G.edge['ueventd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][append read][add_name search][remove_name search]'
G.add_edge('ueventd','wcnss_service')
G.edge['ueventd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][add_name search]'
G.add_edge('ueventd','wcnss_service')
G.edge['ueventd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][add_name search][remove_name search]'
G.add_edge('ueventd','wcnss_service')
G.edge['ueventd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][add_name search][remove_name search][add_name search]'
G.add_edge('ueventd','wcnss_service')
G.edge['ueventd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('ueventd','wpa')
G.edge['ueventd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][add_name search]'
G.add_edge('ueventd','wpa')
G.edge['ueventd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][add_name search][remove_name search]'
G.add_edge('vold','debuggerd')
G.edge['vold']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','dumpstate')
G.edge['vold']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','hostapd')
G.edge['vold']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','logwrapper')
G.edge['vold']['logwrapper']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('vold','netd')
G.edge['vold']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vold','netd')
G.edge['vold']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('vold','p2p_supplicant')
G.edge['vold']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('vold','p2p_supplicant')
G.edge['vold']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open]'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][append read][write read][append read][open open]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vold','wcnss_service')
G.edge['vold']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('vold','wcnss_service')
G.edge['vold']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open]'
G.add_edge('vold','wpa')
G.edge['vold']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('vold','hostapd')
G.edge['vold']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('vold','netd')
G.edge['vold']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('vold','p2p_supplicant')
G.edge['vold']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('vold','wpa')
G.edge['vold']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('vold','debuggerd')
G.edge['vold']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['debuggerd']['fill'] = 'red'
G.add_edge('vold','dumpstate')
G.edge['vold']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['dumpstate']['fill'] = 'red'
G.add_edge('vold','hostapd')
G.edge['vold']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['vold']['hostapd']['fill'] = 'red'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['vold']['init_shell']['fill'] = 'red'
G.add_edge('vold','logwrapper')
G.edge['vold']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['vold']['logwrapper']['fill'] = 'red'
G.add_edge('vold','netd')
G.edge['vold']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['vold']['netd']['fill'] = 'red'
G.add_edge('vold','netd')
G.edge['vold']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read]'
G.edge['vold']['netd']['fill'] = 'red'
G.add_edge('vold','p2p_supplicant')
G.edge['vold']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['vold']['p2p_supplicant']['fill'] = 'red'
G.add_edge('vold','p2p_supplicant')
G.edge['vold']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read]'
G.edge['vold']['p2p_supplicant']['fill'] = 'red'
G.add_edge('vold','p2p_supplicant')
G.edge['vold']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read]'
G.edge['vold']['p2p_supplicant']['fill'] = 'red'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][append read][write read][append read][open open][write read]'
G.edge['vold']['s_system_app']['fill'] = 'red'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['vold']['system_server']['fill'] = 'red'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['vold']['vold']['fill'] = 'red'
G.add_edge('vold','wcnss_service')
G.edge['vold']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read]'
G.edge['vold']['wcnss_service']['fill'] = 'red'
G.add_edge('vold','wcnss_service')
G.edge['vold']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read]'
G.edge['vold']['wcnss_service']['fill'] = 'red'
G.add_edge('vold','wpa')
G.edge['vold']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['vold']['wpa']['fill'] = 'red'
G.add_edge('vold','debuggerd')
G.edge['vold']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('vold','debuggerd')
G.edge['vold']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('vold','dumpstate')
G.edge['vold']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('vold','dumpstate')
G.edge['vold']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('vold','hostapd')
G.edge['vold']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('vold','hostapd')
G.edge['vold']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vold','logwrapper')
G.edge['vold']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][add_name search]'
G.add_edge('vold','logwrapper')
G.edge['vold']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('vold','netd')
G.edge['vold']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search]'
G.add_edge('vold','netd')
G.edge['vold']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search]'
G.add_edge('vold','netd')
G.edge['vold']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('vold','netd')
G.edge['vold']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('vold','p2p_supplicant')
G.edge['vold']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('vold','p2p_supplicant')
G.edge['vold']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('vold','p2p_supplicant')
G.edge['vold']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('vold','p2p_supplicant')
G.edge['vold']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('vold','p2p_supplicant')
G.edge['vold']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('vold','p2p_supplicant')
G.edge['vold']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][append read][write read][append read][open open][write read][add_name search]'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][append read][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('vold','wcnss_service')
G.edge['vold']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search]'
G.add_edge('vold','wcnss_service')
G.edge['vold']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search]'
G.add_edge('vold','wcnss_service')
G.edge['vold']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('vold','wcnss_service')
G.edge['vold']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('vold','wpa')
G.edge['vold']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('vold','wpa')
G.edge['vold']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wcnss_service','debuggerd')
G.edge['wcnss_service']['debuggerd']['write-read'] = '[open open]'
G.add_edge('wcnss_service','dumpstate')
G.edge['wcnss_service']['dumpstate']['write-read'] = '[open open]'
G.add_edge('wcnss_service','hostapd')
G.edge['wcnss_service']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('wcnss_service','init_shell')
G.edge['wcnss_service']['init_shell']['write-read'] = '[open open]'
G.add_edge('wcnss_service','logwrapper')
G.edge['wcnss_service']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('wcnss_service','netd')
G.edge['wcnss_service']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('wcnss_service','netd')
G.edge['wcnss_service']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open]'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][open open]'
G.add_edge('wcnss_service','s_system_app')
G.edge['wcnss_service']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('wcnss_service','system_server')
G.edge['wcnss_service']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('wcnss_service','vold')
G.edge['wcnss_service']['vold']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][open open]'
G.add_edge('wcnss_service','wpa')
G.edge['wcnss_service']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('wcnss_service','hostapd')
G.edge['wcnss_service']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('wcnss_service','init_shell')
G.edge['wcnss_service']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wcnss_service','netd')
G.edge['wcnss_service']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][open open][setattr getattr]'
G.add_edge('wcnss_service','system_server')
G.edge['wcnss_service']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('wcnss_service','wpa')
G.edge['wcnss_service']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('wcnss_service','debuggerd')
G.edge['wcnss_service']['debuggerd']['write-read'] = '[open open][write read]'
G.edge['wcnss_service']['debuggerd']['fill'] = 'red'
G.add_edge('wcnss_service','dumpstate')
G.edge['wcnss_service']['dumpstate']['write-read'] = '[open open][write read]'
G.edge['wcnss_service']['dumpstate']['fill'] = 'red'
G.add_edge('wcnss_service','hostapd')
G.edge['wcnss_service']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['wcnss_service']['hostapd']['fill'] = 'red'
G.add_edge('wcnss_service','init_shell')
G.edge['wcnss_service']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wcnss_service']['init_shell']['fill'] = 'red'
G.add_edge('wcnss_service','logwrapper')
G.edge['wcnss_service']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['wcnss_service']['logwrapper']['fill'] = 'red'
G.add_edge('wcnss_service','netd')
G.edge['wcnss_service']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['wcnss_service']['netd']['fill'] = 'red'
G.add_edge('wcnss_service','netd')
G.edge['wcnss_service']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read]'
G.edge['wcnss_service']['netd']['fill'] = 'red'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read]'
G.edge['wcnss_service']['p2p_supplicant']['fill'] = 'red'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read][write read]'
G.edge['wcnss_service']['p2p_supplicant']['fill'] = 'red'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read]'
G.edge['wcnss_service']['p2p_supplicant']['fill'] = 'red'
G.add_edge('wcnss_service','s_system_app')
G.edge['wcnss_service']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['wcnss_service']['s_system_app']['fill'] = 'red'
G.add_edge('wcnss_service','system_server')
G.edge['wcnss_service']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['wcnss_service']['system_server']['fill'] = 'red'
G.add_edge('wcnss_service','vold')
G.edge['wcnss_service']['vold']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['wcnss_service']['vold']['fill'] = 'red'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][open open][write read]'
G.edge['wcnss_service']['wcnss_service']['fill'] = 'red'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][open open][write read][write read]'
G.edge['wcnss_service']['wcnss_service']['fill'] = 'red'
G.add_edge('wcnss_service','wpa')
G.edge['wcnss_service']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['wcnss_service']['wpa']['fill'] = 'red'
G.add_edge('wcnss_service','debuggerd')
G.edge['wcnss_service']['debuggerd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('wcnss_service','debuggerd')
G.edge['wcnss_service']['debuggerd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('wcnss_service','dumpstate')
G.edge['wcnss_service']['dumpstate']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('wcnss_service','dumpstate')
G.edge['wcnss_service']['dumpstate']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('wcnss_service','hostapd')
G.edge['wcnss_service']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('wcnss_service','hostapd')
G.edge['wcnss_service']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wcnss_service','init_shell')
G.edge['wcnss_service']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('wcnss_service','init_shell')
G.edge['wcnss_service']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wcnss_service','logwrapper')
G.edge['wcnss_service']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('wcnss_service','logwrapper')
G.edge['wcnss_service']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('wcnss_service','netd')
G.edge['wcnss_service']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search]'
G.add_edge('wcnss_service','netd')
G.edge['wcnss_service']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search]'
G.add_edge('wcnss_service','netd')
G.edge['wcnss_service']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('wcnss_service','netd')
G.edge['wcnss_service']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('wcnss_service','s_system_app')
G.edge['wcnss_service']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('wcnss_service','s_system_app')
G.edge['wcnss_service']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('wcnss_service','system_server')
G.edge['wcnss_service']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('wcnss_service','system_server')
G.edge['wcnss_service']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wcnss_service','vold')
G.edge['wcnss_service']['vold']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('wcnss_service','vold')
G.edge['wcnss_service']['vold']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][open open][write read][write read][add_name search]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][open open][write read][write read][add_name search][remove_name search]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][open open][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('wcnss_service','wpa')
G.edge['wcnss_service']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('wcnss_service','wpa')
G.edge['wcnss_service']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wcnss_service','debuggerd')
G.edge['wcnss_service']['debuggerd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('wcnss_service','dumpstate')
G.edge['wcnss_service']['dumpstate']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('wcnss_service','hostapd')
G.edge['wcnss_service']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('wcnss_service','init_shell')
G.edge['wcnss_service']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('wcnss_service','logwrapper')
G.edge['wcnss_service']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('wcnss_service','netd')
G.edge['wcnss_service']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('wcnss_service','netd')
G.edge['wcnss_service']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open]'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open]'
G.add_edge('wcnss_service','s_system_app')
G.edge['wcnss_service']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('wcnss_service','system_server')
G.edge['wcnss_service']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('wcnss_service','vold')
G.edge['wcnss_service']['vold']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open]'
G.add_edge('wcnss_service','wpa')
G.edge['wcnss_service']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('wcnss_service','debuggerd')
G.edge['wcnss_service']['debuggerd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search]'
G.add_edge('wcnss_service','debuggerd')
G.edge['wcnss_service']['debuggerd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search]'
G.add_edge('wcnss_service','dumpstate')
G.edge['wcnss_service']['dumpstate']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search]'
G.add_edge('wcnss_service','dumpstate')
G.edge['wcnss_service']['dumpstate']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search]'
G.add_edge('wcnss_service','hostapd')
G.edge['wcnss_service']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search]'
G.add_edge('wcnss_service','hostapd')
G.edge['wcnss_service']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search]'
G.add_edge('wcnss_service','init_shell')
G.edge['wcnss_service']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search]'
G.add_edge('wcnss_service','init_shell')
G.edge['wcnss_service']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search]'
G.add_edge('wcnss_service','logwrapper')
G.edge['wcnss_service']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][add_name search]'
G.add_edge('wcnss_service','logwrapper')
G.edge['wcnss_service']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search]'
G.add_edge('wcnss_service','netd')
G.edge['wcnss_service']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search]'
G.add_edge('wcnss_service','netd')
G.edge['wcnss_service']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search]'
G.add_edge('wcnss_service','netd')
G.edge['wcnss_service']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search]'
G.add_edge('wcnss_service','netd')
G.edge['wcnss_service']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search]'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search]'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search]'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('wcnss_service','s_system_app')
G.edge['wcnss_service']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][add_name search]'
G.add_edge('wcnss_service','s_system_app')
G.edge['wcnss_service']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search]'
G.add_edge('wcnss_service','system_server')
G.edge['wcnss_service']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search]'
G.add_edge('wcnss_service','system_server')
G.edge['wcnss_service']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search]'
G.add_edge('wcnss_service','vold')
G.edge['wcnss_service']['vold']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][add_name search]'
G.add_edge('wcnss_service','vold')
G.edge['wcnss_service']['vold']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('wcnss_service','wpa')
G.edge['wcnss_service']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search]'
G.add_edge('wcnss_service','wpa')
G.edge['wcnss_service']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search]'
G.add_edge('wpa','debuggerd')
G.edge['wpa']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('wpa','dumpstate')
G.edge['wpa']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open]'
G.add_edge('wpa','hostapd')
G.edge['wpa']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('wpa','init_shell')
G.edge['wpa']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open]'
G.add_edge('wpa','logwrapper')
G.edge['wpa']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('wpa','netd')
G.edge['wpa']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('wpa','netd')
G.edge['wpa']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('wpa','p2p_supplicant')
G.edge['wpa']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][add_name search][remove_name search][open open]'
G.add_edge('wpa','p2p_supplicant')
G.edge['wpa']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('wpa','s_system_app')
G.edge['wpa']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open]'
G.add_edge('wpa','system_server')
G.edge['wpa']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('wpa','vold')
G.edge['wpa']['vold']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open]'
G.add_edge('wpa','wcnss_service')
G.edge['wpa']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('wpa','wcnss_service')
G.edge['wpa']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open]'
G.add_edge('wpa','wpa')
G.edge['wpa']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('wpa','hostapd')
G.edge['wpa']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('wpa','init_shell')
G.edge['wpa']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr]'
G.add_edge('wpa','netd')
G.edge['wpa']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('wpa','p2p_supplicant')
G.edge['wpa']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('wpa','system_server')
G.edge['wpa']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('wpa','wpa')
G.edge['wpa']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('wpa','debuggerd')
G.edge['wpa']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['wpa']['debuggerd']['fill'] = 'red'
G.add_edge('wpa','dumpstate')
G.edge['wpa']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][write read]'
G.edge['wpa']['dumpstate']['fill'] = 'red'
G.add_edge('wpa','hostapd')
G.edge['wpa']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['wpa']['hostapd']['fill'] = 'red'
G.add_edge('wpa','init_shell')
G.edge['wpa']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read]'
G.edge['wpa']['init_shell']['fill'] = 'red'
G.add_edge('wpa','logwrapper')
G.edge['wpa']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['wpa']['logwrapper']['fill'] = 'red'
G.add_edge('wpa','netd')
G.edge['wpa']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['wpa']['netd']['fill'] = 'red'
G.add_edge('wpa','netd')
G.edge['wpa']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read]'
G.edge['wpa']['netd']['fill'] = 'red'
G.add_edge('wpa','p2p_supplicant')
G.edge['wpa']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['wpa']['p2p_supplicant']['fill'] = 'red'
G.add_edge('wpa','p2p_supplicant')
G.edge['wpa']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read]'
G.edge['wpa']['p2p_supplicant']['fill'] = 'red'
G.add_edge('wpa','p2p_supplicant')
G.edge['wpa']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read]'
G.edge['wpa']['p2p_supplicant']['fill'] = 'red'
G.add_edge('wpa','s_system_app')
G.edge['wpa']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][write read]'
G.edge['wpa']['s_system_app']['fill'] = 'red'
G.add_edge('wpa','system_server')
G.edge['wpa']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['wpa']['system_server']['fill'] = 'red'
G.add_edge('wpa','vold')
G.edge['wpa']['vold']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][write read]'
G.edge['wpa']['vold']['fill'] = 'red'
G.add_edge('wpa','wcnss_service')
G.edge['wpa']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read]'
G.edge['wpa']['wcnss_service']['fill'] = 'red'
G.add_edge('wpa','wcnss_service')
G.edge['wpa']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read]'
G.edge['wpa']['wcnss_service']['fill'] = 'red'
G.add_edge('wpa','wpa')
G.edge['wpa']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['wpa']['wpa']['fill'] = 'red'
G.add_edge('wpa','debuggerd')
G.edge['wpa']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('wpa','debuggerd')
G.edge['wpa']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('wpa','dumpstate')
G.edge['wpa']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][write read][add_name search]'
G.add_edge('wpa','dumpstate')
G.edge['wpa']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][write read][add_name search][remove_name search]'
G.add_edge('wpa','hostapd')
G.edge['wpa']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','hostapd')
G.edge['wpa']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','init_shell')
G.edge['wpa']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','init_shell')
G.edge['wpa']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','logwrapper')
G.edge['wpa']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('wpa','logwrapper')
G.edge['wpa']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('wpa','netd')
G.edge['wpa']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search]'
G.add_edge('wpa','netd')
G.edge['wpa']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search]'
G.add_edge('wpa','netd')
G.edge['wpa']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('wpa','netd')
G.edge['wpa']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('wpa','p2p_supplicant')
G.edge['wpa']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('wpa','p2p_supplicant')
G.edge['wpa']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('wpa','p2p_supplicant')
G.edge['wpa']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('wpa','p2p_supplicant')
G.edge['wpa']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('wpa','p2p_supplicant')
G.edge['wpa']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('wpa','p2p_supplicant')
G.edge['wpa']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('wpa','s_system_app')
G.edge['wpa']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][write read][add_name search]'
G.add_edge('wpa','s_system_app')
G.edge['wpa']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][write read][add_name search][remove_name search]'
G.add_edge('wpa','system_server')
G.edge['wpa']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','system_server')
G.edge['wpa']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','vold')
G.edge['wpa']['vold']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][write read][add_name search]'
G.add_edge('wpa','vold')
G.edge['wpa']['vold']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][write read][add_name search][remove_name search]'
G.add_edge('wpa','wcnss_service')
G.edge['wpa']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search]'
G.add_edge('wpa','wcnss_service')
G.edge['wpa']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search]'
G.add_edge('wpa','wcnss_service')
G.edge['wpa']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('wpa','wcnss_service')
G.edge['wpa']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('wpa','wpa')
G.edge['wpa']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','wpa')
G.edge['wpa']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()