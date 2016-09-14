import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open]'
G.add_edge('commonplatformappdomain','ime_app')
G.edge['commonplatformappdomain']['ime_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open]'
G.add_edge('commonplatformappdomain','installd')
G.edge['commonplatformappdomain']['installd']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','s_system_app')
G.edge['commonplatformappdomain']['s_system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open]'
G.add_edge('commonplatformappdomain','store_app')
G.edge['commonplatformappdomain']['store_app']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','system_app')
G.edge['commonplatformappdomain']['system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open]'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','ime_app')
G.edge['commonplatformappdomain']['ime_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','installd')
G.edge['commonplatformappdomain']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','s_system_app')
G.edge['commonplatformappdomain']['s_system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','store_app')
G.edge['commonplatformappdomain']['store_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','system_app')
G.edge['commonplatformappdomain']['system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('commonplatformappdomain','ime_app')
G.edge['commonplatformappdomain']['ime_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['ime_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','installd')
G.edge['commonplatformappdomain']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['installd']['fill'] = 'red'
G.add_edge('commonplatformappdomain','s_system_app')
G.edge['commonplatformappdomain']['s_system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['s_system_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','store_app')
G.edge['commonplatformappdomain']['store_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['store_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','system_app')
G.edge['commonplatformappdomain']['system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['system_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('commonplatformappdomain','ime_app')
G.edge['commonplatformappdomain']['ime_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('commonplatformappdomain','ime_app')
G.edge['commonplatformappdomain']['ime_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('commonplatformappdomain','installd')
G.edge['commonplatformappdomain']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('commonplatformappdomain','installd')
G.edge['commonplatformappdomain']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('commonplatformappdomain','s_system_app')
G.edge['commonplatformappdomain']['s_system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('commonplatformappdomain','s_system_app')
G.edge['commonplatformappdomain']['s_system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('commonplatformappdomain','store_app')
G.edge['commonplatformappdomain']['store_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('commonplatformappdomain','store_app')
G.edge['commonplatformappdomain']['store_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('commonplatformappdomain','system_app')
G.edge['commonplatformappdomain']['system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('commonplatformappdomain','system_app')
G.edge['commonplatformappdomain']['system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','commonplatformappdomain')
G.edge['ime_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('ime_app','installd')
G.edge['ime_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('ime_app','store_app')
G.edge['ime_app']['store_app']['write-read'] = '[open open]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('ime_app','commonplatformappdomain')
G.edge['ime_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('ime_app','installd')
G.edge['ime_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('ime_app','store_app')
G.edge['ime_app']['store_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('ime_app','commonplatformappdomain')
G.edge['ime_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['ime_app']['ime_app']['fill'] = 'red'
G.add_edge('ime_app','installd')
G.edge['ime_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ime_app']['installd']['fill'] = 'red'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['ime_app']['s_system_app']['fill'] = 'red'
G.add_edge('ime_app','store_app')
G.edge['ime_app']['store_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['store_app']['fill'] = 'red'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['ime_app']['system_app']['fill'] = 'red'
G.add_edge('ime_app','commonplatformappdomain')
G.edge['ime_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','commonplatformappdomain')
G.edge['ime_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','installd')
G.edge['ime_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','installd')
G.edge['ime_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','store_app')
G.edge['ime_app']['store_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','store_app')
G.edge['ime_app']['store_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','commonplatformappdomain')
G.edge['installd']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('installd','ime_app')
G.edge['installd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open]'
G.add_edge('installd','s_system_app')
G.edge['installd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('installd','store_app')
G.edge['installd']['store_app']['write-read'] = '[open open]'
G.add_edge('installd','system_app')
G.edge['installd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('installd','commonplatformappdomain')
G.edge['installd']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','ime_app')
G.edge['installd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr]'
G.add_edge('installd','s_system_app')
G.edge['installd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('installd','store_app')
G.edge['installd']['store_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','system_app')
G.edge['installd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('installd','commonplatformappdomain')
G.edge['installd']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('installd','ime_app')
G.edge['installd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['installd']['ime_app']['fill'] = 'red'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read]'
G.edge['installd']['installd']['fill'] = 'red'
G.add_edge('installd','s_system_app')
G.edge['installd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['installd']['s_system_app']['fill'] = 'red'
G.add_edge('installd','store_app')
G.edge['installd']['store_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['store_app']['fill'] = 'red'
G.add_edge('installd','system_app')
G.edge['installd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['installd']['system_app']['fill'] = 'red'
G.add_edge('installd','commonplatformappdomain')
G.edge['installd']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','commonplatformappdomain')
G.edge['installd']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','ime_app')
G.edge['installd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','ime_app')
G.edge['installd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','s_system_app')
G.edge['installd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','s_system_app')
G.edge['installd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','store_app')
G.edge['installd']['store_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','store_app')
G.edge['installd']['store_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','system_app')
G.edge['installd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','system_app')
G.edge['installd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','commonplatformappdomain')
G.edge['s_system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('s_system_app','installd')
G.edge['s_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open]'
G.add_edge('s_system_app','store_app')
G.edge['s_system_app']['store_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open]'
G.add_edge('s_system_app','commonplatformappdomain')
G.edge['s_system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('s_system_app','installd')
G.edge['s_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('s_system_app','store_app')
G.edge['s_system_app']['store_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('s_system_app','commonplatformappdomain')
G.edge['s_system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['s_system_app']['ime_app']['fill'] = 'red'
G.add_edge('s_system_app','installd')
G.edge['s_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['installd']['fill'] = 'red'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['s_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('s_system_app','store_app')
G.edge['s_system_app']['store_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['store_app']['fill'] = 'red'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['s_system_app']['system_app']['fill'] = 'red'
G.add_edge('s_system_app','commonplatformappdomain')
G.edge['s_system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','commonplatformappdomain')
G.edge['s_system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','installd')
G.edge['s_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','installd')
G.edge['s_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','store_app')
G.edge['s_system_app']['store_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','store_app')
G.edge['s_system_app']['store_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('store_app','commonplatformappdomain')
G.edge['store_app']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('store_app','ime_app')
G.edge['store_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('store_app','installd')
G.edge['store_app']['installd']['write-read'] = '[open open]'
G.add_edge('store_app','s_system_app')
G.edge['store_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('store_app','store_app')
G.edge['store_app']['store_app']['write-read'] = '[open open]'
G.add_edge('store_app','system_app')
G.edge['store_app']['system_app']['write-read'] = '[open open]'
G.add_edge('store_app','commonplatformappdomain')
G.edge['store_app']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('store_app','ime_app')
G.edge['store_app']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('store_app','installd')
G.edge['store_app']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('store_app','s_system_app')
G.edge['store_app']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('store_app','store_app')
G.edge['store_app']['store_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('store_app','system_app')
G.edge['store_app']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('store_app','commonplatformappdomain')
G.edge['store_app']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['store_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('store_app','ime_app')
G.edge['store_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['store_app']['ime_app']['fill'] = 'red'
G.add_edge('store_app','installd')
G.edge['store_app']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['store_app']['installd']['fill'] = 'red'
G.add_edge('store_app','s_system_app')
G.edge['store_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['store_app']['s_system_app']['fill'] = 'red'
G.add_edge('store_app','store_app')
G.edge['store_app']['store_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['store_app']['store_app']['fill'] = 'red'
G.add_edge('store_app','system_app')
G.edge['store_app']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['store_app']['system_app']['fill'] = 'red'
G.add_edge('store_app','commonplatformappdomain')
G.edge['store_app']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('store_app','commonplatformappdomain')
G.edge['store_app']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('store_app','ime_app')
G.edge['store_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('store_app','ime_app')
G.edge['store_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('store_app','installd')
G.edge['store_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('store_app','installd')
G.edge['store_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('store_app','s_system_app')
G.edge['store_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('store_app','s_system_app')
G.edge['store_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('store_app','store_app')
G.edge['store_app']['store_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('store_app','store_app')
G.edge['store_app']['store_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('store_app','system_app')
G.edge['store_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('store_app','system_app')
G.edge['store_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','commonplatformappdomain')
G.edge['system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('system_app','installd')
G.edge['system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open]'
G.add_edge('system_app','store_app')
G.edge['system_app']['store_app']['write-read'] = '[open open]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open]'
G.add_edge('system_app','commonplatformappdomain')
G.edge['system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('system_app','installd')
G.edge['system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('system_app','store_app')
G.edge['system_app']['store_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('system_app','commonplatformappdomain')
G.edge['system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['system_app']['ime_app']['fill'] = 'red'
G.add_edge('system_app','installd')
G.edge['system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_app']['installd']['fill'] = 'red'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['system_app']['s_system_app']['fill'] = 'red'
G.add_edge('system_app','store_app')
G.edge['system_app']['store_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['store_app']['fill'] = 'red'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['system_app']['system_app']['fill'] = 'red'
G.add_edge('system_app','commonplatformappdomain')
G.edge['system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','commonplatformappdomain')
G.edge['system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','installd')
G.edge['system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','installd')
G.edge['system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','store_app')
G.edge['system_app']['store_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','store_app')
G.edge['system_app']['store_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()