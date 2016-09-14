import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('ime_app','platform_app')
G.edge['ime_app']['platform_app']['write-read'] = '[open open]'
G.add_edge('ime_app','sem')
G.edge['ime_app']['sem']['write-read'] = '[open open]'
G.add_edge('ime_app','s_platform_app')
G.edge['ime_app']['s_platform_app']['write-read'] = '[open open]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','platform_app')
G.edge['ime_app']['platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','sem')
G.edge['ime_app']['sem']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','s_platform_app')
G.edge['ime_app']['s_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['ime_app']['fill'] = 'red'
G.add_edge('ime_app','platform_app')
G.edge['ime_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['platform_app']['fill'] = 'red'
G.add_edge('ime_app','sem')
G.edge['ime_app']['sem']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['sem']['fill'] = 'red'
G.add_edge('ime_app','s_platform_app')
G.edge['ime_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['s_platform_app']['fill'] = 'red'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['s_system_app']['fill'] = 'red'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['system_app']['fill'] = 'red'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','platform_app')
G.edge['ime_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','platform_app')
G.edge['ime_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','sem')
G.edge['ime_app']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','sem')
G.edge['ime_app']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','s_platform_app')
G.edge['ime_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','s_platform_app')
G.edge['ime_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('platform_app','ime_app')
G.edge['platform_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('platform_app','platform_app')
G.edge['platform_app']['platform_app']['write-read'] = '[open open]'
G.add_edge('platform_app','sem')
G.edge['platform_app']['sem']['write-read'] = '[open open]'
G.add_edge('platform_app','s_platform_app')
G.edge['platform_app']['s_platform_app']['write-read'] = '[open open]'
G.add_edge('platform_app','s_system_app')
G.edge['platform_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('platform_app','system_app')
G.edge['platform_app']['system_app']['write-read'] = '[open open]'
G.add_edge('platform_app','ime_app')
G.edge['platform_app']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platform_app','platform_app')
G.edge['platform_app']['platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platform_app','sem')
G.edge['platform_app']['sem']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platform_app','s_platform_app')
G.edge['platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platform_app','s_system_app')
G.edge['platform_app']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platform_app','system_app')
G.edge['platform_app']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platform_app','ime_app')
G.edge['platform_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platform_app']['ime_app']['fill'] = 'red'
G.add_edge('platform_app','platform_app')
G.edge['platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platform_app']['platform_app']['fill'] = 'red'
G.add_edge('platform_app','sem')
G.edge['platform_app']['sem']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platform_app']['sem']['fill'] = 'red'
G.add_edge('platform_app','s_platform_app')
G.edge['platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platform_app']['s_platform_app']['fill'] = 'red'
G.add_edge('platform_app','s_system_app')
G.edge['platform_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platform_app']['s_system_app']['fill'] = 'red'
G.add_edge('platform_app','system_app')
G.edge['platform_app']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platform_app']['system_app']['fill'] = 'red'
G.add_edge('platform_app','ime_app')
G.edge['platform_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('platform_app','ime_app')
G.edge['platform_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('platform_app','platform_app')
G.edge['platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('platform_app','platform_app')
G.edge['platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('platform_app','sem')
G.edge['platform_app']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('platform_app','sem')
G.edge['platform_app']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('platform_app','s_platform_app')
G.edge['platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('platform_app','s_platform_app')
G.edge['platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('platform_app','s_system_app')
G.edge['platform_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('platform_app','s_system_app')
G.edge['platform_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('platform_app','system_app')
G.edge['platform_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('platform_app','system_app')
G.edge['platform_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sem','ime_app')
G.edge['sem']['ime_app']['write-read'] = '[open open]'
G.add_edge('sem','platform_app')
G.edge['sem']['platform_app']['write-read'] = '[open open]'
G.add_edge('sem','sem')
G.edge['sem']['sem']['write-read'] = '[open open]'
G.add_edge('sem','s_platform_app')
G.edge['sem']['s_platform_app']['write-read'] = '[open open]'
G.add_edge('sem','s_system_app')
G.edge['sem']['s_system_app']['write-read'] = '[open open]'
G.add_edge('sem','system_app')
G.edge['sem']['system_app']['write-read'] = '[open open]'
G.add_edge('sem','ime_app')
G.edge['sem']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sem','platform_app')
G.edge['sem']['platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sem','sem')
G.edge['sem']['sem']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sem','s_platform_app')
G.edge['sem']['s_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sem','s_system_app')
G.edge['sem']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sem','system_app')
G.edge['sem']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sem','ime_app')
G.edge['sem']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sem']['ime_app']['fill'] = 'red'
G.add_edge('sem','platform_app')
G.edge['sem']['platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sem']['platform_app']['fill'] = 'red'
G.add_edge('sem','sem')
G.edge['sem']['sem']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sem']['sem']['fill'] = 'red'
G.add_edge('sem','s_platform_app')
G.edge['sem']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sem']['s_platform_app']['fill'] = 'red'
G.add_edge('sem','s_system_app')
G.edge['sem']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sem']['s_system_app']['fill'] = 'red'
G.add_edge('sem','system_app')
G.edge['sem']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sem']['system_app']['fill'] = 'red'
G.add_edge('sem','ime_app')
G.edge['sem']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sem','ime_app')
G.edge['sem']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sem','platform_app')
G.edge['sem']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sem','platform_app')
G.edge['sem']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sem','sem')
G.edge['sem']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sem','sem')
G.edge['sem']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sem','s_platform_app')
G.edge['sem']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sem','s_platform_app')
G.edge['sem']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sem','s_system_app')
G.edge['sem']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sem','s_system_app')
G.edge['sem']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sem','system_app')
G.edge['sem']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sem','system_app')
G.edge['sem']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_platform_app','ime_app')
G.edge['s_platform_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('s_platform_app','platform_app')
G.edge['s_platform_app']['platform_app']['write-read'] = '[open open]'
G.add_edge('s_platform_app','sem')
G.edge['s_platform_app']['sem']['write-read'] = '[open open]'
G.add_edge('s_platform_app','s_platform_app')
G.edge['s_platform_app']['s_platform_app']['write-read'] = '[open open]'
G.add_edge('s_platform_app','s_system_app')
G.edge['s_platform_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('s_platform_app','system_app')
G.edge['s_platform_app']['system_app']['write-read'] = '[open open]'
G.add_edge('s_platform_app','ime_app')
G.edge['s_platform_app']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_platform_app','platform_app')
G.edge['s_platform_app']['platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_platform_app','sem')
G.edge['s_platform_app']['sem']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_platform_app','s_platform_app')
G.edge['s_platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_platform_app','s_system_app')
G.edge['s_platform_app']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_platform_app','system_app')
G.edge['s_platform_app']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_platform_app','ime_app')
G.edge['s_platform_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_platform_app']['ime_app']['fill'] = 'red'
G.add_edge('s_platform_app','platform_app')
G.edge['s_platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_platform_app']['platform_app']['fill'] = 'red'
G.add_edge('s_platform_app','sem')
G.edge['s_platform_app']['sem']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_platform_app']['sem']['fill'] = 'red'
G.add_edge('s_platform_app','s_platform_app')
G.edge['s_platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_platform_app']['s_platform_app']['fill'] = 'red'
G.add_edge('s_platform_app','s_system_app')
G.edge['s_platform_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_platform_app']['s_system_app']['fill'] = 'red'
G.add_edge('s_platform_app','system_app')
G.edge['s_platform_app']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_platform_app']['system_app']['fill'] = 'red'
G.add_edge('s_platform_app','ime_app')
G.edge['s_platform_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_platform_app','ime_app')
G.edge['s_platform_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_platform_app','platform_app')
G.edge['s_platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_platform_app','platform_app')
G.edge['s_platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_platform_app','sem')
G.edge['s_platform_app']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_platform_app','sem')
G.edge['s_platform_app']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_platform_app','s_platform_app')
G.edge['s_platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_platform_app','s_platform_app')
G.edge['s_platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_platform_app','s_system_app')
G.edge['s_platform_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_platform_app','s_system_app')
G.edge['s_platform_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_platform_app','system_app')
G.edge['s_platform_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_platform_app','system_app')
G.edge['s_platform_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('s_system_app','platform_app')
G.edge['s_system_app']['platform_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','sem')
G.edge['s_system_app']['sem']['write-read'] = '[open open]'
G.add_edge('s_system_app','s_platform_app')
G.edge['s_system_app']['s_platform_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','platform_app')
G.edge['s_system_app']['platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','sem')
G.edge['s_system_app']['sem']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','s_platform_app')
G.edge['s_system_app']['s_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['ime_app']['fill'] = 'red'
G.add_edge('s_system_app','platform_app')
G.edge['s_system_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['platform_app']['fill'] = 'red'
G.add_edge('s_system_app','sem')
G.edge['s_system_app']['sem']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['sem']['fill'] = 'red'
G.add_edge('s_system_app','s_platform_app')
G.edge['s_system_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['s_platform_app']['fill'] = 'red'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['system_app']['fill'] = 'red'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','platform_app')
G.edge['s_system_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','platform_app')
G.edge['s_system_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','sem')
G.edge['s_system_app']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','sem')
G.edge['s_system_app']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','s_platform_app')
G.edge['s_system_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','s_platform_app')
G.edge['s_system_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_app','platform_app')
G.edge['system_app']['platform_app']['write-read'] = '[open open]'
G.add_edge('system_app','sem')
G.edge['system_app']['sem']['write-read'] = '[open open]'
G.add_edge('system_app','s_platform_app')
G.edge['system_app']['s_platform_app']['write-read'] = '[open open]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','platform_app')
G.edge['system_app']['platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','sem')
G.edge['system_app']['sem']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','s_platform_app')
G.edge['system_app']['s_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['ime_app']['fill'] = 'red'
G.add_edge('system_app','platform_app')
G.edge['system_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['platform_app']['fill'] = 'red'
G.add_edge('system_app','sem')
G.edge['system_app']['sem']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['sem']['fill'] = 'red'
G.add_edge('system_app','s_platform_app')
G.edge['system_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['s_platform_app']['fill'] = 'red'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['s_system_app']['fill'] = 'red'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['system_app']['fill'] = 'red'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','platform_app')
G.edge['system_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','platform_app')
G.edge['system_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','sem')
G.edge['system_app']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','sem')
G.edge['system_app']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','s_platform_app')
G.edge['system_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','s_platform_app')
G.edge['system_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()