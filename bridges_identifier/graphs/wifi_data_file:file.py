import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('hostapd','hostapd')
G.edge['hostapd']['hostapd']['write-read'] = '[open open]'
G.add_edge('hostapd','logwrapper')
G.edge['hostapd']['logwrapper']['write-read'] = '[open open]'
G.add_edge('hostapd','netd')
G.edge['hostapd']['netd']['write-read'] = '[open open]'
G.add_edge('hostapd','p2p_supplicant')
G.edge['hostapd']['p2p_supplicant']['write-read'] = '[open open]'
G.add_edge('hostapd','p2p_supplicant')
G.edge['hostapd']['p2p_supplicant']['write-read'] = '[open open][open open]'
G.add_edge('hostapd','s_system_app')
G.edge['hostapd']['s_system_app']['write-read'] = '[open open]'
G.add_edge('hostapd','system_server')
G.edge['hostapd']['system_server']['write-read'] = '[open open]'
G.add_edge('hostapd','vold')
G.edge['hostapd']['vold']['write-read'] = '[open open]'
G.add_edge('hostapd','wcnss_service')
G.edge['hostapd']['wcnss_service']['write-read'] = '[open open]'
G.add_edge('hostapd','wcnss_service')
G.edge['hostapd']['wcnss_service']['write-read'] = '[open open][open open]'
G.add_edge('hostapd','wpa')
G.edge['hostapd']['wpa']['write-read'] = '[open open]'
G.add_edge('hostapd','netd')
G.edge['hostapd']['netd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('hostapd','s_system_app')
G.edge['hostapd']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('hostapd','system_server')
G.edge['hostapd']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('hostapd','wcnss_service')
G.edge['hostapd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('hostapd','wcnss_service')
G.edge['hostapd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('hostapd','wpa')
G.edge['hostapd']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('hostapd','hostapd')
G.edge['hostapd']['hostapd']['write-read'] = '[open open][write read]'
G.edge['hostapd']['hostapd']['fill'] = 'red'
G.add_edge('hostapd','hostapd')
G.edge['hostapd']['hostapd']['write-read'] = '[open open][write read][append read]'
G.add_edge('hostapd','logwrapper')
G.edge['hostapd']['logwrapper']['write-read'] = '[open open][write read]'
G.edge['hostapd']['logwrapper']['fill'] = 'red'
G.add_edge('hostapd','logwrapper')
G.edge['hostapd']['logwrapper']['write-read'] = '[open open][write read][append read]'
G.add_edge('hostapd','netd')
G.edge['hostapd']['netd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['hostapd']['netd']['fill'] = 'red'
G.add_edge('hostapd','netd')
G.edge['hostapd']['netd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('hostapd','p2p_supplicant')
G.edge['hostapd']['p2p_supplicant']['write-read'] = '[open open][open open][write read]'
G.edge['hostapd']['p2p_supplicant']['fill'] = 'red'
G.add_edge('hostapd','p2p_supplicant')
G.edge['hostapd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('hostapd','p2p_supplicant')
G.edge['hostapd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['hostapd']['p2p_supplicant']['fill'] = 'red'
G.add_edge('hostapd','s_system_app')
G.edge['hostapd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['hostapd']['s_system_app']['fill'] = 'red'
G.add_edge('hostapd','s_system_app')
G.edge['hostapd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('hostapd','system_server')
G.edge['hostapd']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['hostapd']['system_server']['fill'] = 'red'
G.add_edge('hostapd','system_server')
G.edge['hostapd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('hostapd','vold')
G.edge['hostapd']['vold']['write-read'] = '[open open][write read]'
G.edge['hostapd']['vold']['fill'] = 'red'
G.add_edge('hostapd','vold')
G.edge['hostapd']['vold']['write-read'] = '[open open][write read][append read]'
G.add_edge('hostapd','wcnss_service')
G.edge['hostapd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['hostapd']['wcnss_service']['fill'] = 'red'
G.add_edge('hostapd','wcnss_service')
G.edge['hostapd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('hostapd','wcnss_service')
G.edge['hostapd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['hostapd']['wcnss_service']['fill'] = 'red'
G.add_edge('hostapd','wcnss_service')
G.edge['hostapd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('hostapd','wpa')
G.edge['hostapd']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['hostapd']['wpa']['fill'] = 'red'
G.add_edge('hostapd','wpa')
G.edge['hostapd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','hostapd')
G.edge['ime_app']['hostapd']['write-read'] = '[open open]'
G.add_edge('ime_app','logwrapper')
G.edge['ime_app']['logwrapper']['write-read'] = '[open open]'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('ime_app','p2p_supplicant')
G.edge['ime_app']['p2p_supplicant']['write-read'] = '[open open]'
G.add_edge('ime_app','p2p_supplicant')
G.edge['ime_app']['p2p_supplicant']['write-read'] = '[open open][open open]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('ime_app','vold')
G.edge['ime_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('ime_app','wcnss_service')
G.edge['ime_app']['wcnss_service']['write-read'] = '[open open]'
G.add_edge('ime_app','wcnss_service')
G.edge['ime_app']['wcnss_service']['write-read'] = '[open open][open open]'
G.add_edge('ime_app','wpa')
G.edge['ime_app']['wpa']['write-read'] = '[open open]'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('ime_app','wcnss_service')
G.edge['ime_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('ime_app','wcnss_service')
G.edge['ime_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('ime_app','wpa')
G.edge['ime_app']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','hostapd')
G.edge['ime_app']['hostapd']['write-read'] = '[open open][write read]'
G.edge['ime_app']['hostapd']['fill'] = 'red'
G.add_edge('ime_app','hostapd')
G.edge['ime_app']['hostapd']['write-read'] = '[open open][write read][append read]'
G.add_edge('ime_app','logwrapper')
G.edge['ime_app']['logwrapper']['write-read'] = '[open open][write read]'
G.edge['ime_app']['logwrapper']['fill'] = 'red'
G.add_edge('ime_app','logwrapper')
G.edge['ime_app']['logwrapper']['write-read'] = '[open open][write read][append read]'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['ime_app']['netd']['fill'] = 'red'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','p2p_supplicant')
G.edge['ime_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read]'
G.edge['ime_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('ime_app','p2p_supplicant')
G.edge['ime_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('ime_app','p2p_supplicant')
G.edge['ime_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['ime_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read]'
G.edge['ime_app']['s_system_app']['fill'] = 'red'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['ime_app']['system_server']['fill'] = 'red'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','vold')
G.edge['ime_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['ime_app']['vold']['fill'] = 'red'
G.add_edge('ime_app','vold')
G.edge['ime_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('ime_app','wcnss_service')
G.edge['ime_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['ime_app']['wcnss_service']['fill'] = 'red'
G.add_edge('ime_app','wcnss_service')
G.edge['ime_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('ime_app','wcnss_service')
G.edge['ime_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['ime_app']['wcnss_service']['fill'] = 'red'
G.add_edge('ime_app','wcnss_service')
G.edge['ime_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('ime_app','wpa')
G.edge['ime_app']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['wpa']['fill'] = 'red'
G.add_edge('ime_app','wpa')
G.edge['ime_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','hostapd')
G.edge['knox_system_app']['hostapd']['write-read'] = '[open open]'
G.add_edge('knox_system_app','logwrapper')
G.edge['knox_system_app']['logwrapper']['write-read'] = '[open open]'
G.add_edge('knox_system_app','netd')
G.edge['knox_system_app']['netd']['write-read'] = '[open open]'
G.add_edge('knox_system_app','p2p_supplicant')
G.edge['knox_system_app']['p2p_supplicant']['write-read'] = '[open open]'
G.add_edge('knox_system_app','p2p_supplicant')
G.edge['knox_system_app']['p2p_supplicant']['write-read'] = '[open open][open open]'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_system_app','vold')
G.edge['knox_system_app']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_system_app','wcnss_service')
G.edge['knox_system_app']['wcnss_service']['write-read'] = '[open open]'
G.add_edge('knox_system_app','wcnss_service')
G.edge['knox_system_app']['wcnss_service']['write-read'] = '[open open][open open]'
G.add_edge('knox_system_app','wpa')
G.edge['knox_system_app']['wpa']['write-read'] = '[open open]'
G.add_edge('knox_system_app','netd')
G.edge['knox_system_app']['netd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('knox_system_app','wcnss_service')
G.edge['knox_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('knox_system_app','wcnss_service')
G.edge['knox_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('knox_system_app','wpa')
G.edge['knox_system_app']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','hostapd')
G.edge['knox_system_app']['hostapd']['write-read'] = '[open open][write read]'
G.edge['knox_system_app']['hostapd']['fill'] = 'red'
G.add_edge('knox_system_app','hostapd')
G.edge['knox_system_app']['hostapd']['write-read'] = '[open open][write read][append read]'
G.add_edge('knox_system_app','logwrapper')
G.edge['knox_system_app']['logwrapper']['write-read'] = '[open open][write read]'
G.edge['knox_system_app']['logwrapper']['fill'] = 'red'
G.add_edge('knox_system_app','logwrapper')
G.edge['knox_system_app']['logwrapper']['write-read'] = '[open open][write read][append read]'
G.add_edge('knox_system_app','netd')
G.edge['knox_system_app']['netd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['netd']['fill'] = 'red'
G.add_edge('knox_system_app','netd')
G.edge['knox_system_app']['netd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','p2p_supplicant')
G.edge['knox_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read]'
G.edge['knox_system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('knox_system_app','p2p_supplicant')
G.edge['knox_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('knox_system_app','p2p_supplicant')
G.edge['knox_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['knox_system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_system_app']['system_server']['fill'] = 'red'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','vold')
G.edge['knox_system_app']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['knox_system_app']['vold']['fill'] = 'red'
G.add_edge('knox_system_app','vold')
G.edge['knox_system_app']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('knox_system_app','wcnss_service')
G.edge['knox_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['knox_system_app']['wcnss_service']['fill'] = 'red'
G.add_edge('knox_system_app','wcnss_service')
G.edge['knox_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','wcnss_service')
G.edge['knox_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['knox_system_app']['wcnss_service']['fill'] = 'red'
G.add_edge('knox_system_app','wcnss_service')
G.edge['knox_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('knox_system_app','wpa')
G.edge['knox_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['wpa']['fill'] = 'red'
G.add_edge('knox_system_app','wpa')
G.edge['knox_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('logwrapper','hostapd')
G.edge['logwrapper']['hostapd']['write-read'] = '[open open]'
G.add_edge('logwrapper','logwrapper')
G.edge['logwrapper']['logwrapper']['write-read'] = '[open open]'
G.add_edge('logwrapper','netd')
G.edge['logwrapper']['netd']['write-read'] = '[open open]'
G.add_edge('logwrapper','p2p_supplicant')
G.edge['logwrapper']['p2p_supplicant']['write-read'] = '[open open]'
G.add_edge('logwrapper','p2p_supplicant')
G.edge['logwrapper']['p2p_supplicant']['write-read'] = '[open open][open open]'
G.add_edge('logwrapper','s_system_app')
G.edge['logwrapper']['s_system_app']['write-read'] = '[open open]'
G.add_edge('logwrapper','system_server')
G.edge['logwrapper']['system_server']['write-read'] = '[open open]'
G.add_edge('logwrapper','vold')
G.edge['logwrapper']['vold']['write-read'] = '[open open]'
G.add_edge('logwrapper','wcnss_service')
G.edge['logwrapper']['wcnss_service']['write-read'] = '[open open]'
G.add_edge('logwrapper','wcnss_service')
G.edge['logwrapper']['wcnss_service']['write-read'] = '[open open][open open]'
G.add_edge('logwrapper','wpa')
G.edge['logwrapper']['wpa']['write-read'] = '[open open]'
G.add_edge('logwrapper','netd')
G.edge['logwrapper']['netd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('logwrapper','s_system_app')
G.edge['logwrapper']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('logwrapper','system_server')
G.edge['logwrapper']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('logwrapper','wcnss_service')
G.edge['logwrapper']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('logwrapper','wcnss_service')
G.edge['logwrapper']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('logwrapper','wpa')
G.edge['logwrapper']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('logwrapper','hostapd')
G.edge['logwrapper']['hostapd']['write-read'] = '[open open][write read]'
G.edge['logwrapper']['hostapd']['fill'] = 'red'
G.add_edge('logwrapper','hostapd')
G.edge['logwrapper']['hostapd']['write-read'] = '[open open][write read][append read]'
G.add_edge('logwrapper','logwrapper')
G.edge['logwrapper']['logwrapper']['write-read'] = '[open open][write read]'
G.edge['logwrapper']['logwrapper']['fill'] = 'red'
G.add_edge('logwrapper','logwrapper')
G.edge['logwrapper']['logwrapper']['write-read'] = '[open open][write read][append read]'
G.add_edge('logwrapper','netd')
G.edge['logwrapper']['netd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['logwrapper']['netd']['fill'] = 'red'
G.add_edge('logwrapper','netd')
G.edge['logwrapper']['netd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('logwrapper','p2p_supplicant')
G.edge['logwrapper']['p2p_supplicant']['write-read'] = '[open open][open open][write read]'
G.edge['logwrapper']['p2p_supplicant']['fill'] = 'red'
G.add_edge('logwrapper','p2p_supplicant')
G.edge['logwrapper']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('logwrapper','p2p_supplicant')
G.edge['logwrapper']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['logwrapper']['p2p_supplicant']['fill'] = 'red'
G.add_edge('logwrapper','s_system_app')
G.edge['logwrapper']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['logwrapper']['s_system_app']['fill'] = 'red'
G.add_edge('logwrapper','s_system_app')
G.edge['logwrapper']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('logwrapper','system_server')
G.edge['logwrapper']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['logwrapper']['system_server']['fill'] = 'red'
G.add_edge('logwrapper','system_server')
G.edge['logwrapper']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('logwrapper','vold')
G.edge['logwrapper']['vold']['write-read'] = '[open open][write read]'
G.edge['logwrapper']['vold']['fill'] = 'red'
G.add_edge('logwrapper','vold')
G.edge['logwrapper']['vold']['write-read'] = '[open open][write read][append read]'
G.add_edge('logwrapper','wcnss_service')
G.edge['logwrapper']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['logwrapper']['wcnss_service']['fill'] = 'red'
G.add_edge('logwrapper','wcnss_service')
G.edge['logwrapper']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('logwrapper','wcnss_service')
G.edge['logwrapper']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['logwrapper']['wcnss_service']['fill'] = 'red'
G.add_edge('logwrapper','wcnss_service')
G.edge['logwrapper']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('logwrapper','wpa')
G.edge['logwrapper']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['logwrapper']['wpa']['fill'] = 'red'
G.add_edge('logwrapper','wpa')
G.edge['logwrapper']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('netd','hostapd')
G.edge['netd']['hostapd']['write-read'] = '[open open]'
G.add_edge('netd','logwrapper')
G.edge['netd']['logwrapper']['write-read'] = '[open open]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open]'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('netd','vold')
G.edge['netd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('netd','wcnss_service')
G.edge['netd']['wcnss_service']['write-read'] = '[open open]'
G.add_edge('netd','wcnss_service')
G.edge['netd']['wcnss_service']['write-read'] = '[open open][open open]'
G.add_edge('netd','wpa')
G.edge['netd']['wpa']['write-read'] = '[open open]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('netd','wcnss_service')
G.edge['netd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('netd','wcnss_service')
G.edge['netd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('netd','wpa')
G.edge['netd']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('netd','hostapd')
G.edge['netd']['hostapd']['write-read'] = '[open open][write read]'
G.edge['netd']['hostapd']['fill'] = 'red'
G.add_edge('netd','hostapd')
G.edge['netd']['hostapd']['write-read'] = '[open open][write read][append read]'
G.add_edge('netd','logwrapper')
G.edge['netd']['logwrapper']['write-read'] = '[open open][write read]'
G.edge['netd']['logwrapper']['fill'] = 'red'
G.add_edge('netd','logwrapper')
G.edge['netd']['logwrapper']['write-read'] = '[open open][write read][append read]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['netd']['netd']['fill'] = 'red'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read]'
G.edge['netd']['p2p_supplicant']['fill'] = 'red'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('netd','p2p_supplicant')
G.edge['netd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['netd']['p2p_supplicant']['fill'] = 'red'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read]'
G.edge['netd']['s_system_app']['fill'] = 'red'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['netd']['system_server']['fill'] = 'red'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('netd','vold')
G.edge['netd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['netd']['vold']['fill'] = 'red'
G.add_edge('netd','vold')
G.edge['netd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('netd','wcnss_service')
G.edge['netd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['netd']['wcnss_service']['fill'] = 'red'
G.add_edge('netd','wcnss_service')
G.edge['netd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('netd','wcnss_service')
G.edge['netd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['netd']['wcnss_service']['fill'] = 'red'
G.add_edge('netd','wcnss_service')
G.edge['netd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('netd','wpa')
G.edge['netd']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['netd']['wpa']['fill'] = 'red'
G.add_edge('netd','wpa')
G.edge['netd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('p2p_supplicant','hostapd')
G.edge['p2p_supplicant']['hostapd']['write-read'] = '[open open]'
G.add_edge('p2p_supplicant','logwrapper')
G.edge['p2p_supplicant']['logwrapper']['write-read'] = '[open open]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open]'
G.add_edge('p2p_supplicant','s_system_app')
G.edge['p2p_supplicant']['s_system_app']['write-read'] = '[open open]'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open]'
G.add_edge('p2p_supplicant','vold')
G.edge['p2p_supplicant']['vold']['write-read'] = '[open open]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open]'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('p2p_supplicant','s_system_app')
G.edge['p2p_supplicant']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('p2p_supplicant','hostapd')
G.edge['p2p_supplicant']['hostapd']['write-read'] = '[open open][write read]'
G.edge['p2p_supplicant']['hostapd']['fill'] = 'red'
G.add_edge('p2p_supplicant','hostapd')
G.edge['p2p_supplicant']['hostapd']['write-read'] = '[open open][write read][append read]'
G.add_edge('p2p_supplicant','logwrapper')
G.edge['p2p_supplicant']['logwrapper']['write-read'] = '[open open][write read]'
G.edge['p2p_supplicant']['logwrapper']['fill'] = 'red'
G.add_edge('p2p_supplicant','logwrapper')
G.edge['p2p_supplicant']['logwrapper']['write-read'] = '[open open][write read][append read]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['netd']['fill'] = 'red'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read]'
G.edge['p2p_supplicant']['p2p_supplicant']['fill'] = 'red'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['p2p_supplicant']['p2p_supplicant']['fill'] = 'red'
G.add_edge('p2p_supplicant','s_system_app')
G.edge['p2p_supplicant']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['s_system_app']['fill'] = 'red'
G.add_edge('p2p_supplicant','s_system_app')
G.edge['p2p_supplicant']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['system_server']['fill'] = 'red'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('p2p_supplicant','vold')
G.edge['p2p_supplicant']['vold']['write-read'] = '[open open][write read]'
G.edge['p2p_supplicant']['vold']['fill'] = 'red'
G.add_edge('p2p_supplicant','vold')
G.edge['p2p_supplicant']['vold']['write-read'] = '[open open][write read][append read]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['p2p_supplicant']['wcnss_service']['fill'] = 'red'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['p2p_supplicant']['wcnss_service']['fill'] = 'red'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['wpa']['fill'] = 'red'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('p2p_supplicant','hostapd')
G.edge['p2p_supplicant']['hostapd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('p2p_supplicant','logwrapper')
G.edge['p2p_supplicant']['logwrapper']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open]'
G.add_edge('p2p_supplicant','s_system_app')
G.edge['p2p_supplicant']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('p2p_supplicant','vold')
G.edge['p2p_supplicant']['vold']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open]'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('p2p_supplicant','s_system_app')
G.edge['p2p_supplicant']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr]'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('p2p_supplicant','hostapd')
G.edge['p2p_supplicant']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['p2p_supplicant']['hostapd']['fill'] = 'red'
G.add_edge('p2p_supplicant','hostapd')
G.edge['p2p_supplicant']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('p2p_supplicant','logwrapper')
G.edge['p2p_supplicant']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['p2p_supplicant']['logwrapper']['fill'] = 'red'
G.add_edge('p2p_supplicant','logwrapper')
G.edge['p2p_supplicant']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['netd']['fill'] = 'red'
G.add_edge('p2p_supplicant','netd')
G.edge['p2p_supplicant']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read]'
G.edge['p2p_supplicant']['p2p_supplicant']['fill'] = 'red'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read]'
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read]'
G.edge['p2p_supplicant']['p2p_supplicant']['fill'] = 'red'
G.add_edge('p2p_supplicant','s_system_app')
G.edge['p2p_supplicant']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['s_system_app']['fill'] = 'red'
G.add_edge('p2p_supplicant','s_system_app')
G.edge['p2p_supplicant']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['system_server']['fill'] = 'red'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('p2p_supplicant','vold')
G.edge['p2p_supplicant']['vold']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['p2p_supplicant']['vold']['fill'] = 'red'
G.add_edge('p2p_supplicant','vold')
G.edge['p2p_supplicant']['vold']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['p2p_supplicant']['wcnss_service']['fill'] = 'red'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['p2p_supplicant']['wcnss_service']['fill'] = 'red'
G.add_edge('p2p_supplicant','wcnss_service')
G.edge['p2p_supplicant']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['wpa']['fill'] = 'red'
G.add_edge('p2p_supplicant','wpa')
G.edge['p2p_supplicant']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open]'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open]'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open]'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['hostapd']['fill'] = 'red'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['logwrapper']['fill'] = 'red'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['s_system_app']['netd']['fill'] = 'red'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read]'
G.edge['s_system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['s_system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read]'
G.edge['s_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['s_system_app']['system_server']['fill'] = 'red'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['s_system_app']['vold']['fill'] = 'red'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['s_system_app']['wcnss_service']['fill'] = 'red'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['s_system_app']['wcnss_service']['fill'] = 'red'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['wpa']['fill'] = 'red'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open]'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open]'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr]'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr]'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['s_system_app']['hostapd']['fill'] = 'red'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['s_system_app']['logwrapper']['fill'] = 'red'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['netd']['fill'] = 'red'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read]'
G.edge['s_system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read]'
G.add_edge('s_system_app','p2p_supplicant')
G.edge['s_system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read]'
G.edge['s_system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['system_server']['fill'] = 'red'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read]'
G.edge['s_system_app']['vold']['fill'] = 'red'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read]'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['s_system_app']['wcnss_service']['fill'] = 'red'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['s_system_app']['wcnss_service']['fill'] = 'red'
G.add_edge('s_system_app','wcnss_service')
G.edge['s_system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['wpa']['fill'] = 'red'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','hostapd')
G.edge['system_app']['hostapd']['write-read'] = '[open open]'
G.add_edge('system_app','logwrapper')
G.edge['system_app']['logwrapper']['write-read'] = '[open open]'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('system_app','p2p_supplicant')
G.edge['system_app']['p2p_supplicant']['write-read'] = '[open open]'
G.add_edge('system_app','p2p_supplicant')
G.edge['system_app']['p2p_supplicant']['write-read'] = '[open open][open open]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('system_app','vold')
G.edge['system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('system_app','wcnss_service')
G.edge['system_app']['wcnss_service']['write-read'] = '[open open]'
G.add_edge('system_app','wcnss_service')
G.edge['system_app']['wcnss_service']['write-read'] = '[open open][open open]'
G.add_edge('system_app','wpa')
G.edge['system_app']['wpa']['write-read'] = '[open open]'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('system_app','wcnss_service')
G.edge['system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('system_app','wcnss_service')
G.edge['system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('system_app','wpa')
G.edge['system_app']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','hostapd')
G.edge['system_app']['hostapd']['write-read'] = '[open open][write read]'
G.edge['system_app']['hostapd']['fill'] = 'red'
G.add_edge('system_app','hostapd')
G.edge['system_app']['hostapd']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_app','logwrapper')
G.edge['system_app']['logwrapper']['write-read'] = '[open open][write read]'
G.edge['system_app']['logwrapper']['fill'] = 'red'
G.add_edge('system_app','logwrapper')
G.edge['system_app']['logwrapper']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['system_app']['netd']['fill'] = 'red'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','p2p_supplicant')
G.edge['system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read]'
G.edge['system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('system_app','p2p_supplicant')
G.edge['system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('system_app','p2p_supplicant')
G.edge['system_app']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['system_app']['p2p_supplicant']['fill'] = 'red'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read]'
G.edge['system_app']['s_system_app']['fill'] = 'red'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['system_app']['system_server']['fill'] = 'red'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','vold')
G.edge['system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['system_app']['vold']['fill'] = 'red'
G.add_edge('system_app','vold')
G.edge['system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('system_app','wcnss_service')
G.edge['system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['system_app']['wcnss_service']['fill'] = 'red'
G.add_edge('system_app','wcnss_service')
G.edge['system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('system_app','wcnss_service')
G.edge['system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['system_app']['wcnss_service']['fill'] = 'red'
G.add_edge('system_app','wcnss_service')
G.edge['system_app']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('system_app','wpa')
G.edge['system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['wpa']['fill'] = 'red'
G.add_edge('system_app','wpa')
G.edge['system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_server','hostapd')
G.edge['system_server']['hostapd']['write-read'] = '[open open]'
G.add_edge('system_server','logwrapper')
G.edge['system_server']['logwrapper']['write-read'] = '[open open]'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('system_server','p2p_supplicant')
G.edge['system_server']['p2p_supplicant']['write-read'] = '[open open]'
G.add_edge('system_server','p2p_supplicant')
G.edge['system_server']['p2p_supplicant']['write-read'] = '[open open][open open]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','wcnss_service')
G.edge['system_server']['wcnss_service']['write-read'] = '[open open]'
G.add_edge('system_server','wcnss_service')
G.edge['system_server']['wcnss_service']['write-read'] = '[open open][open open]'
G.add_edge('system_server','wpa')
G.edge['system_server']['wpa']['write-read'] = '[open open]'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','wcnss_service')
G.edge['system_server']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('system_server','wcnss_service')
G.edge['system_server']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('system_server','wpa')
G.edge['system_server']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','hostapd')
G.edge['system_server']['hostapd']['write-read'] = '[open open][write read]'
G.edge['system_server']['hostapd']['fill'] = 'red'
G.add_edge('system_server','hostapd')
G.edge['system_server']['hostapd']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','logwrapper')
G.edge['system_server']['logwrapper']['write-read'] = '[open open][write read]'
G.edge['system_server']['logwrapper']['fill'] = 'red'
G.add_edge('system_server','logwrapper')
G.edge['system_server']['logwrapper']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['system_server']['netd']['fill'] = 'red'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','p2p_supplicant')
G.edge['system_server']['p2p_supplicant']['write-read'] = '[open open][open open][write read]'
G.edge['system_server']['p2p_supplicant']['fill'] = 'red'
G.add_edge('system_server','p2p_supplicant')
G.edge['system_server']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('system_server','p2p_supplicant')
G.edge['system_server']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['system_server']['p2p_supplicant']['fill'] = 'red'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read]'
G.edge['system_server']['s_system_app']['fill'] = 'red'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['system_server']['vold']['fill'] = 'red'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('system_server','wcnss_service')
G.edge['system_server']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['system_server']['wcnss_service']['fill'] = 'red'
G.add_edge('system_server','wcnss_service')
G.edge['system_server']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('system_server','wcnss_service')
G.edge['system_server']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['system_server']['wcnss_service']['fill'] = 'red'
G.add_edge('system_server','wcnss_service')
G.edge['system_server']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('system_server','wpa')
G.edge['system_server']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['wpa']['fill'] = 'red'
G.add_edge('system_server','wpa')
G.edge['system_server']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('ueventd','hostapd')
G.edge['ueventd']['hostapd']['write-read'] = '[open open]'
G.add_edge('ueventd','logwrapper')
G.edge['ueventd']['logwrapper']['write-read'] = '[open open]'
G.add_edge('ueventd','netd')
G.edge['ueventd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('ueventd','p2p_supplicant')
G.edge['ueventd']['p2p_supplicant']['write-read'] = '[open open]'
G.add_edge('ueventd','p2p_supplicant')
G.edge['ueventd']['p2p_supplicant']['write-read'] = '[open open][open open]'
G.add_edge('ueventd','s_system_app')
G.edge['ueventd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open]'
G.add_edge('ueventd','system_server')
G.edge['ueventd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('ueventd','vold')
G.edge['ueventd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('ueventd','wcnss_service')
G.edge['ueventd']['wcnss_service']['write-read'] = '[open open]'
G.add_edge('ueventd','wcnss_service')
G.edge['ueventd']['wcnss_service']['write-read'] = '[open open][open open]'
G.add_edge('ueventd','wpa')
G.edge['ueventd']['wpa']['write-read'] = '[open open]'
G.add_edge('ueventd','netd')
G.edge['ueventd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('ueventd','s_system_app')
G.edge['ueventd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr]'
G.add_edge('ueventd','system_server')
G.edge['ueventd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('ueventd','wcnss_service')
G.edge['ueventd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('ueventd','wcnss_service')
G.edge['ueventd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('ueventd','wpa')
G.edge['ueventd']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ueventd','hostapd')
G.edge['ueventd']['hostapd']['write-read'] = '[open open][write read]'
G.edge['ueventd']['hostapd']['fill'] = 'red'
G.add_edge('ueventd','hostapd')
G.edge['ueventd']['hostapd']['write-read'] = '[open open][write read][append read]'
G.add_edge('ueventd','logwrapper')
G.edge['ueventd']['logwrapper']['write-read'] = '[open open][write read]'
G.edge['ueventd']['logwrapper']['fill'] = 'red'
G.add_edge('ueventd','logwrapper')
G.edge['ueventd']['logwrapper']['write-read'] = '[open open][write read][append read]'
G.add_edge('ueventd','netd')
G.edge['ueventd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['ueventd']['netd']['fill'] = 'red'
G.add_edge('ueventd','netd')
G.edge['ueventd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('ueventd','p2p_supplicant')
G.edge['ueventd']['p2p_supplicant']['write-read'] = '[open open][open open][write read]'
G.edge['ueventd']['p2p_supplicant']['fill'] = 'red'
G.add_edge('ueventd','p2p_supplicant')
G.edge['ueventd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('ueventd','p2p_supplicant')
G.edge['ueventd']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['ueventd']['p2p_supplicant']['fill'] = 'red'
G.add_edge('ueventd','s_system_app')
G.edge['ueventd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read]'
G.edge['ueventd']['s_system_app']['fill'] = 'red'
G.add_edge('ueventd','s_system_app')
G.edge['ueventd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('ueventd','system_server')
G.edge['ueventd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['ueventd']['system_server']['fill'] = 'red'
G.add_edge('ueventd','system_server')
G.edge['ueventd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('ueventd','vold')
G.edge['ueventd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['ueventd']['vold']['fill'] = 'red'
G.add_edge('ueventd','vold')
G.edge['ueventd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('ueventd','wcnss_service')
G.edge['ueventd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['ueventd']['wcnss_service']['fill'] = 'red'
G.add_edge('ueventd','wcnss_service')
G.edge['ueventd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('ueventd','wcnss_service')
G.edge['ueventd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['ueventd']['wcnss_service']['fill'] = 'red'
G.add_edge('ueventd','wcnss_service')
G.edge['ueventd']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('ueventd','wpa')
G.edge['ueventd']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ueventd']['wpa']['fill'] = 'red'
G.add_edge('ueventd','wpa')
G.edge['ueventd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('vold','hostapd')
G.edge['vold']['hostapd']['write-read'] = '[open open]'
G.add_edge('vold','logwrapper')
G.edge['vold']['logwrapper']['write-read'] = '[open open]'
G.add_edge('vold','netd')
G.edge['vold']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('vold','p2p_supplicant')
G.edge['vold']['p2p_supplicant']['write-read'] = '[open open]'
G.add_edge('vold','p2p_supplicant')
G.edge['vold']['p2p_supplicant']['write-read'] = '[open open][open open]'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vold','wcnss_service')
G.edge['vold']['wcnss_service']['write-read'] = '[open open]'
G.add_edge('vold','wcnss_service')
G.edge['vold']['wcnss_service']['write-read'] = '[open open][open open]'
G.add_edge('vold','wpa')
G.edge['vold']['wpa']['write-read'] = '[open open]'
G.add_edge('vold','netd')
G.edge['vold']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('vold','wcnss_service')
G.edge['vold']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('vold','wcnss_service')
G.edge['vold']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('vold','wpa')
G.edge['vold']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vold','hostapd')
G.edge['vold']['hostapd']['write-read'] = '[open open][write read]'
G.edge['vold']['hostapd']['fill'] = 'red'
G.add_edge('vold','hostapd')
G.edge['vold']['hostapd']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','logwrapper')
G.edge['vold']['logwrapper']['write-read'] = '[open open][write read]'
G.edge['vold']['logwrapper']['fill'] = 'red'
G.add_edge('vold','logwrapper')
G.edge['vold']['logwrapper']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','netd')
G.edge['vold']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['vold']['netd']['fill'] = 'red'
G.add_edge('vold','netd')
G.edge['vold']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('vold','p2p_supplicant')
G.edge['vold']['p2p_supplicant']['write-read'] = '[open open][open open][write read]'
G.edge['vold']['p2p_supplicant']['fill'] = 'red'
G.add_edge('vold','p2p_supplicant')
G.edge['vold']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('vold','p2p_supplicant')
G.edge['vold']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['vold']['p2p_supplicant']['fill'] = 'red'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read]'
G.edge['vold']['s_system_app']['fill'] = 'red'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['vold']['system_server']['fill'] = 'red'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['vold']['vold']['fill'] = 'red'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('vold','wcnss_service')
G.edge['vold']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['vold']['wcnss_service']['fill'] = 'red'
G.add_edge('vold','wcnss_service')
G.edge['vold']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('vold','wcnss_service')
G.edge['vold']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['vold']['wcnss_service']['fill'] = 'red'
G.add_edge('vold','wcnss_service')
G.edge['vold']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('vold','wpa')
G.edge['vold']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vold']['wpa']['fill'] = 'red'
G.add_edge('vold','wpa')
G.edge['vold']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('wcnss_service','hostapd')
G.edge['wcnss_service']['hostapd']['write-read'] = '[open open]'
G.add_edge('wcnss_service','logwrapper')
G.edge['wcnss_service']['logwrapper']['write-read'] = '[open open]'
G.add_edge('wcnss_service','netd')
G.edge['wcnss_service']['netd']['write-read'] = '[open open]'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open]'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open]'
G.add_edge('wcnss_service','s_system_app')
G.edge['wcnss_service']['s_system_app']['write-read'] = '[open open]'
G.add_edge('wcnss_service','system_server')
G.edge['wcnss_service']['system_server']['write-read'] = '[open open]'
G.add_edge('wcnss_service','vold')
G.edge['wcnss_service']['vold']['write-read'] = '[open open]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open]'
G.add_edge('wcnss_service','wpa')
G.edge['wcnss_service']['wpa']['write-read'] = '[open open]'
G.add_edge('wcnss_service','netd')
G.edge['wcnss_service']['netd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wcnss_service','s_system_app')
G.edge['wcnss_service']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wcnss_service','system_server')
G.edge['wcnss_service']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('wcnss_service','wpa')
G.edge['wcnss_service']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wcnss_service','hostapd')
G.edge['wcnss_service']['hostapd']['write-read'] = '[open open][write read]'
G.edge['wcnss_service']['hostapd']['fill'] = 'red'
G.add_edge('wcnss_service','hostapd')
G.edge['wcnss_service']['hostapd']['write-read'] = '[open open][write read][append read]'
G.add_edge('wcnss_service','logwrapper')
G.edge['wcnss_service']['logwrapper']['write-read'] = '[open open][write read]'
G.edge['wcnss_service']['logwrapper']['fill'] = 'red'
G.add_edge('wcnss_service','logwrapper')
G.edge['wcnss_service']['logwrapper']['write-read'] = '[open open][write read][append read]'
G.add_edge('wcnss_service','netd')
G.edge['wcnss_service']['netd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wcnss_service']['netd']['fill'] = 'red'
G.add_edge('wcnss_service','netd')
G.edge['wcnss_service']['netd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read]'
G.edge['wcnss_service']['p2p_supplicant']['fill'] = 'red'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['wcnss_service']['p2p_supplicant']['fill'] = 'red'
G.add_edge('wcnss_service','s_system_app')
G.edge['wcnss_service']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wcnss_service']['s_system_app']['fill'] = 'red'
G.add_edge('wcnss_service','s_system_app')
G.edge['wcnss_service']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('wcnss_service','system_server')
G.edge['wcnss_service']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wcnss_service']['system_server']['fill'] = 'red'
G.add_edge('wcnss_service','system_server')
G.edge['wcnss_service']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('wcnss_service','vold')
G.edge['wcnss_service']['vold']['write-read'] = '[open open][write read]'
G.edge['wcnss_service']['vold']['fill'] = 'red'
G.add_edge('wcnss_service','vold')
G.edge['wcnss_service']['vold']['write-read'] = '[open open][write read][append read]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['wcnss_service']['wcnss_service']['fill'] = 'red'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['wcnss_service']['wcnss_service']['fill'] = 'red'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('wcnss_service','wpa')
G.edge['wcnss_service']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wcnss_service']['wpa']['fill'] = 'red'
G.add_edge('wcnss_service','wpa')
G.edge['wcnss_service']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('wcnss_service','hostapd')
G.edge['wcnss_service']['hostapd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('wcnss_service','logwrapper')
G.edge['wcnss_service']['logwrapper']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('wcnss_service','netd')
G.edge['wcnss_service']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open]'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open]'
G.add_edge('wcnss_service','s_system_app')
G.edge['wcnss_service']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('wcnss_service','system_server')
G.edge['wcnss_service']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('wcnss_service','vold')
G.edge['wcnss_service']['vold']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open]'
G.add_edge('wcnss_service','wpa')
G.edge['wcnss_service']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('wcnss_service','netd')
G.edge['wcnss_service']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('wcnss_service','s_system_app')
G.edge['wcnss_service']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('wcnss_service','system_server')
G.edge['wcnss_service']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr]'
G.add_edge('wcnss_service','wpa')
G.edge['wcnss_service']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('wcnss_service','hostapd')
G.edge['wcnss_service']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['wcnss_service']['hostapd']['fill'] = 'red'
G.add_edge('wcnss_service','hostapd')
G.edge['wcnss_service']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('wcnss_service','logwrapper')
G.edge['wcnss_service']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['wcnss_service']['logwrapper']['fill'] = 'red'
G.add_edge('wcnss_service','logwrapper')
G.edge['wcnss_service']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('wcnss_service','netd')
G.edge['wcnss_service']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['wcnss_service']['netd']['fill'] = 'red'
G.add_edge('wcnss_service','netd')
G.edge['wcnss_service']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read]'
G.edge['wcnss_service']['p2p_supplicant']['fill'] = 'red'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read]'
G.add_edge('wcnss_service','p2p_supplicant')
G.edge['wcnss_service']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read]'
G.edge['wcnss_service']['p2p_supplicant']['fill'] = 'red'
G.add_edge('wcnss_service','s_system_app')
G.edge['wcnss_service']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['wcnss_service']['s_system_app']['fill'] = 'red'
G.add_edge('wcnss_service','s_system_app')
G.edge['wcnss_service']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('wcnss_service','system_server')
G.edge['wcnss_service']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['wcnss_service']['system_server']['fill'] = 'red'
G.add_edge('wcnss_service','system_server')
G.edge['wcnss_service']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('wcnss_service','vold')
G.edge['wcnss_service']['vold']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['wcnss_service']['vold']['fill'] = 'red'
G.add_edge('wcnss_service','vold')
G.edge['wcnss_service']['vold']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['wcnss_service']['wcnss_service']['fill'] = 'red'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['wcnss_service']['wcnss_service']['fill'] = 'red'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('wcnss_service','wpa')
G.edge['wcnss_service']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['wcnss_service']['wpa']['fill'] = 'red'
G.add_edge('wcnss_service','wpa')
G.edge['wcnss_service']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('wpa','hostapd')
G.edge['wpa']['hostapd']['write-read'] = '[open open]'
G.add_edge('wpa','logwrapper')
G.edge['wpa']['logwrapper']['write-read'] = '[open open]'
G.add_edge('wpa','netd')
G.edge['wpa']['netd']['write-read'] = '[open open]'
G.add_edge('wpa','p2p_supplicant')
G.edge['wpa']['p2p_supplicant']['write-read'] = '[open open]'
G.add_edge('wpa','p2p_supplicant')
G.edge['wpa']['p2p_supplicant']['write-read'] = '[open open][open open]'
G.add_edge('wpa','s_system_app')
G.edge['wpa']['s_system_app']['write-read'] = '[open open]'
G.add_edge('wpa','system_server')
G.edge['wpa']['system_server']['write-read'] = '[open open]'
G.add_edge('wpa','vold')
G.edge['wpa']['vold']['write-read'] = '[open open]'
G.add_edge('wpa','wcnss_service')
G.edge['wpa']['wcnss_service']['write-read'] = '[open open]'
G.add_edge('wpa','wcnss_service')
G.edge['wpa']['wcnss_service']['write-read'] = '[open open][open open]'
G.add_edge('wpa','wpa')
G.edge['wpa']['wpa']['write-read'] = '[open open]'
G.add_edge('wpa','netd')
G.edge['wpa']['netd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wpa','s_system_app')
G.edge['wpa']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wpa','system_server')
G.edge['wpa']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wpa','wcnss_service')
G.edge['wpa']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('wpa','wcnss_service')
G.edge['wpa']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('wpa','wpa')
G.edge['wpa']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wpa','hostapd')
G.edge['wpa']['hostapd']['write-read'] = '[open open][write read]'
G.edge['wpa']['hostapd']['fill'] = 'red'
G.add_edge('wpa','hostapd')
G.edge['wpa']['hostapd']['write-read'] = '[open open][write read][append read]'
G.add_edge('wpa','logwrapper')
G.edge['wpa']['logwrapper']['write-read'] = '[open open][write read]'
G.edge['wpa']['logwrapper']['fill'] = 'red'
G.add_edge('wpa','logwrapper')
G.edge['wpa']['logwrapper']['write-read'] = '[open open][write read][append read]'
G.add_edge('wpa','netd')
G.edge['wpa']['netd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wpa']['netd']['fill'] = 'red'
G.add_edge('wpa','netd')
G.edge['wpa']['netd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('wpa','p2p_supplicant')
G.edge['wpa']['p2p_supplicant']['write-read'] = '[open open][open open][write read]'
G.edge['wpa']['p2p_supplicant']['fill'] = 'red'
G.add_edge('wpa','p2p_supplicant')
G.edge['wpa']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('wpa','p2p_supplicant')
G.edge['wpa']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['wpa']['p2p_supplicant']['fill'] = 'red'
G.add_edge('wpa','s_system_app')
G.edge['wpa']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wpa']['s_system_app']['fill'] = 'red'
G.add_edge('wpa','s_system_app')
G.edge['wpa']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('wpa','system_server')
G.edge['wpa']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wpa']['system_server']['fill'] = 'red'
G.add_edge('wpa','system_server')
G.edge['wpa']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('wpa','vold')
G.edge['wpa']['vold']['write-read'] = '[open open][write read]'
G.edge['wpa']['vold']['fill'] = 'red'
G.add_edge('wpa','vold')
G.edge['wpa']['vold']['write-read'] = '[open open][write read][append read]'
G.add_edge('wpa','wcnss_service')
G.edge['wpa']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['wpa']['wcnss_service']['fill'] = 'red'
G.add_edge('wpa','wcnss_service')
G.edge['wpa']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('wpa','wcnss_service')
G.edge['wpa']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['wpa']['wcnss_service']['fill'] = 'red'
G.add_edge('wpa','wcnss_service')
G.edge['wpa']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('wpa','wpa')
G.edge['wpa']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wpa']['wpa']['fill'] = 'red'
G.add_edge('wpa','wpa')
G.edge['wpa']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()