import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('commonplatformappdomain','ime_app')
G.edge['commonplatformappdomain']['ime_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('commonplatformappdomain','macloader')
G.edge['commonplatformappdomain']['macloader']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','mfgloader')
G.edge['commonplatformappdomain']['mfgloader']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','radio')
G.edge['commonplatformappdomain']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('commonplatformappdomain','s_system_app')
G.edge['commonplatformappdomain']['s_system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('commonplatformappdomain','system_app')
G.edge['commonplatformappdomain']['system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('commonplatformappdomain','untrusteddomain')
G.edge['commonplatformappdomain']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('commonplatformappdomain','ime_app')
G.edge['commonplatformappdomain']['ime_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','mfgloader')
G.edge['commonplatformappdomain']['mfgloader']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','radio')
G.edge['commonplatformappdomain']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','s_system_app')
G.edge['commonplatformappdomain']['s_system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','system_app')
G.edge['commonplatformappdomain']['system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','ime_app')
G.edge['commonplatformappdomain']['ime_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['ime_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','ime_app')
G.edge['commonplatformappdomain']['ime_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','macloader')
G.edge['commonplatformappdomain']['macloader']['write-read'] = '[open open][write read]'
G.edge['commonplatformappdomain']['macloader']['fill'] = 'red'
G.add_edge('commonplatformappdomain','macloader')
G.edge['commonplatformappdomain']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('commonplatformappdomain','mfgloader')
G.edge['commonplatformappdomain']['mfgloader']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['mfgloader']['fill'] = 'red'
G.add_edge('commonplatformappdomain','mfgloader')
G.edge['commonplatformappdomain']['mfgloader']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','radio')
G.edge['commonplatformappdomain']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['radio']['fill'] = 'red'
G.add_edge('commonplatformappdomain','radio')
G.edge['commonplatformappdomain']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','s_system_app')
G.edge['commonplatformappdomain']['s_system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['s_system_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','s_system_app')
G.edge['commonplatformappdomain']['s_system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','system_app')
G.edge['commonplatformappdomain']['system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['system_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','system_app')
G.edge['commonplatformappdomain']['system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','untrusteddomain')
G.edge['commonplatformappdomain']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['commonplatformappdomain']['untrusteddomain']['fill'] = 'red'
G.add_edge('commonplatformappdomain','untrusteddomain')
G.edge['commonplatformappdomain']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('hostapd','ime_app')
G.edge['hostapd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('hostapd','macloader')
G.edge['hostapd']['macloader']['write-read'] = '[open open]'
G.add_edge('hostapd','mfgloader')
G.edge['hostapd']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('hostapd','radio')
G.edge['hostapd']['radio']['write-read'] = '[open open]'
G.add_edge('hostapd','s_system_app')
G.edge['hostapd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('hostapd','system_app')
G.edge['hostapd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('hostapd','untrusteddomain')
G.edge['hostapd']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('hostapd','ime_app')
G.edge['hostapd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('hostapd','mfgloader')
G.edge['hostapd']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('hostapd','radio')
G.edge['hostapd']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('hostapd','s_system_app')
G.edge['hostapd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('hostapd','system_app')
G.edge['hostapd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('hostapd','ime_app')
G.edge['hostapd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['hostapd']['ime_app']['fill'] = 'red'
G.add_edge('hostapd','ime_app')
G.edge['hostapd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('hostapd','macloader')
G.edge['hostapd']['macloader']['write-read'] = '[open open][write read]'
G.edge['hostapd']['macloader']['fill'] = 'red'
G.add_edge('hostapd','macloader')
G.edge['hostapd']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('hostapd','mfgloader')
G.edge['hostapd']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['hostapd']['mfgloader']['fill'] = 'red'
G.add_edge('hostapd','mfgloader')
G.edge['hostapd']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('hostapd','radio')
G.edge['hostapd']['radio']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['hostapd']['radio']['fill'] = 'red'
G.add_edge('hostapd','radio')
G.edge['hostapd']['radio']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('hostapd','s_system_app')
G.edge['hostapd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['hostapd']['s_system_app']['fill'] = 'red'
G.add_edge('hostapd','s_system_app')
G.edge['hostapd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('hostapd','system_app')
G.edge['hostapd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['hostapd']['system_app']['fill'] = 'red'
G.add_edge('hostapd','system_app')
G.edge['hostapd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('hostapd','untrusteddomain')
G.edge['hostapd']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['hostapd']['untrusteddomain']['fill'] = 'red'
G.add_edge('hostapd','untrusteddomain')
G.edge['hostapd']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','macloader')
G.edge['ime_app']['macloader']['write-read'] = '[open open]'
G.add_edge('ime_app','mfgloader')
G.edge['ime_app']['mfgloader']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','radio')
G.edge['ime_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','untrusteddomain')
G.edge['ime_app']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','mfgloader')
G.edge['ime_app']['mfgloader']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ime_app','radio')
G.edge['ime_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['ime_app']['fill'] = 'red'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','macloader')
G.edge['ime_app']['macloader']['write-read'] = '[open open][write read]'
G.edge['ime_app']['macloader']['fill'] = 'red'
G.add_edge('ime_app','macloader')
G.edge['ime_app']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('ime_app','mfgloader')
G.edge['ime_app']['mfgloader']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ime_app']['mfgloader']['fill'] = 'red'
G.add_edge('ime_app','mfgloader')
G.edge['ime_app']['mfgloader']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','radio')
G.edge['ime_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ime_app']['radio']['fill'] = 'red'
G.add_edge('ime_app','radio')
G.edge['ime_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['s_system_app']['fill'] = 'red'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['system_app']['fill'] = 'red'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','untrusteddomain')
G.edge['ime_app']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['ime_app']['untrusteddomain']['fill'] = 'red'
G.add_edge('ime_app','untrusteddomain')
G.edge['ime_app']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','ime_app')
G.edge['macloader']['ime_app']['write-read'] = '[open open]'
G.add_edge('macloader','macloader')
G.edge['macloader']['macloader']['write-read'] = '[open open]'
G.add_edge('macloader','mfgloader')
G.edge['macloader']['mfgloader']['write-read'] = '[open open]'
G.add_edge('macloader','radio')
G.edge['macloader']['radio']['write-read'] = '[open open]'
G.add_edge('macloader','s_system_app')
G.edge['macloader']['s_system_app']['write-read'] = '[open open]'
G.add_edge('macloader','system_app')
G.edge['macloader']['system_app']['write-read'] = '[open open]'
G.add_edge('macloader','untrusteddomain')
G.edge['macloader']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('macloader','ime_app')
G.edge['macloader']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('macloader','mfgloader')
G.edge['macloader']['mfgloader']['write-read'] = '[open open][setattr getattr]'
G.add_edge('macloader','radio')
G.edge['macloader']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('macloader','s_system_app')
G.edge['macloader']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('macloader','system_app')
G.edge['macloader']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('macloader','ime_app')
G.edge['macloader']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['macloader']['ime_app']['fill'] = 'red'
G.add_edge('macloader','ime_app')
G.edge['macloader']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('macloader','macloader')
G.edge['macloader']['macloader']['write-read'] = '[open open][write read]'
G.edge['macloader']['macloader']['fill'] = 'red'
G.add_edge('macloader','macloader')
G.edge['macloader']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','mfgloader')
G.edge['macloader']['mfgloader']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['macloader']['mfgloader']['fill'] = 'red'
G.add_edge('macloader','mfgloader')
G.edge['macloader']['mfgloader']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('macloader','radio')
G.edge['macloader']['radio']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['macloader']['radio']['fill'] = 'red'
G.add_edge('macloader','radio')
G.edge['macloader']['radio']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('macloader','s_system_app')
G.edge['macloader']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['macloader']['s_system_app']['fill'] = 'red'
G.add_edge('macloader','s_system_app')
G.edge['macloader']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('macloader','system_app')
G.edge['macloader']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['macloader']['system_app']['fill'] = 'red'
G.add_edge('macloader','system_app')
G.edge['macloader']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('macloader','untrusteddomain')
G.edge['macloader']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['macloader']['untrusteddomain']['fill'] = 'red'
G.add_edge('macloader','untrusteddomain')
G.edge['macloader']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('mfgloader','ime_app')
G.edge['mfgloader']['ime_app']['write-read'] = '[open open]'
G.add_edge('mfgloader','macloader')
G.edge['mfgloader']['macloader']['write-read'] = '[open open]'
G.add_edge('mfgloader','mfgloader')
G.edge['mfgloader']['mfgloader']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('mfgloader','radio')
G.edge['mfgloader']['radio']['write-read'] = '[open open]'
G.add_edge('mfgloader','s_system_app')
G.edge['mfgloader']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mfgloader','system_app')
G.edge['mfgloader']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mfgloader','untrusteddomain')
G.edge['mfgloader']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('mfgloader','ime_app')
G.edge['mfgloader']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mfgloader','mfgloader')
G.edge['mfgloader']['mfgloader']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('mfgloader','radio')
G.edge['mfgloader']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mfgloader','s_system_app')
G.edge['mfgloader']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('mfgloader','system_app')
G.edge['mfgloader']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('mfgloader','ime_app')
G.edge['mfgloader']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mfgloader']['ime_app']['fill'] = 'red'
G.add_edge('mfgloader','ime_app')
G.edge['mfgloader']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mfgloader','macloader')
G.edge['mfgloader']['macloader']['write-read'] = '[open open][write read]'
G.edge['mfgloader']['macloader']['fill'] = 'red'
G.add_edge('mfgloader','macloader')
G.edge['mfgloader']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('mfgloader','mfgloader')
G.edge['mfgloader']['mfgloader']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['mfgloader']['mfgloader']['fill'] = 'red'
G.add_edge('mfgloader','mfgloader')
G.edge['mfgloader']['mfgloader']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('mfgloader','radio')
G.edge['mfgloader']['radio']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mfgloader']['radio']['fill'] = 'red'
G.add_edge('mfgloader','radio')
G.edge['mfgloader']['radio']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mfgloader','s_system_app')
G.edge['mfgloader']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['mfgloader']['s_system_app']['fill'] = 'red'
G.add_edge('mfgloader','s_system_app')
G.edge['mfgloader']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('mfgloader','system_app')
G.edge['mfgloader']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['mfgloader']['system_app']['fill'] = 'red'
G.add_edge('mfgloader','system_app')
G.edge['mfgloader']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('mfgloader','untrusteddomain')
G.edge['mfgloader']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['mfgloader']['untrusteddomain']['fill'] = 'red'
G.add_edge('mfgloader','untrusteddomain')
G.edge['mfgloader']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('otp_server','ime_app')
G.edge['otp_server']['ime_app']['write-read'] = '[open open]'
G.add_edge('otp_server','macloader')
G.edge['otp_server']['macloader']['write-read'] = '[open open]'
G.add_edge('otp_server','mfgloader')
G.edge['otp_server']['mfgloader']['write-read'] = '[open open]'
G.add_edge('otp_server','radio')
G.edge['otp_server']['radio']['write-read'] = '[open open]'
G.add_edge('otp_server','s_system_app')
G.edge['otp_server']['s_system_app']['write-read'] = '[open open]'
G.add_edge('otp_server','system_app')
G.edge['otp_server']['system_app']['write-read'] = '[open open]'
G.add_edge('otp_server','untrusteddomain')
G.edge['otp_server']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('otp_server','ime_app')
G.edge['otp_server']['ime_app']['write-read'] = '[open open][write read]'
G.edge['otp_server']['ime_app']['fill'] = 'red'
G.add_edge('otp_server','ime_app')
G.edge['otp_server']['ime_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('otp_server','macloader')
G.edge['otp_server']['macloader']['write-read'] = '[open open][write read]'
G.edge['otp_server']['macloader']['fill'] = 'red'
G.add_edge('otp_server','macloader')
G.edge['otp_server']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('otp_server','mfgloader')
G.edge['otp_server']['mfgloader']['write-read'] = '[open open][write read]'
G.edge['otp_server']['mfgloader']['fill'] = 'red'
G.add_edge('otp_server','mfgloader')
G.edge['otp_server']['mfgloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('otp_server','radio')
G.edge['otp_server']['radio']['write-read'] = '[open open][write read]'
G.edge['otp_server']['radio']['fill'] = 'red'
G.add_edge('otp_server','radio')
G.edge['otp_server']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('otp_server','s_system_app')
G.edge['otp_server']['s_system_app']['write-read'] = '[open open][write read]'
G.edge['otp_server']['s_system_app']['fill'] = 'red'
G.add_edge('otp_server','s_system_app')
G.edge['otp_server']['s_system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('otp_server','system_app')
G.edge['otp_server']['system_app']['write-read'] = '[open open][write read]'
G.edge['otp_server']['system_app']['fill'] = 'red'
G.add_edge('otp_server','system_app')
G.edge['otp_server']['system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('otp_server','untrusteddomain')
G.edge['otp_server']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['otp_server']['untrusteddomain']['fill'] = 'red'
G.add_edge('otp_server','untrusteddomain')
G.edge['otp_server']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','ime_app')
G.edge['radio']['ime_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('radio','macloader')
G.edge['radio']['macloader']['write-read'] = '[open open]'
G.add_edge('radio','mfgloader')
G.edge['radio']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][open open]'
G.add_edge('radio','s_system_app')
G.edge['radio']['s_system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][open open]'
G.add_edge('radio','system_app')
G.edge['radio']['system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('radio','untrusteddomain')
G.edge['radio']['untrusteddomain']['write-read'] = '[write read][append read][open open]'
G.add_edge('radio','ime_app')
G.edge['radio']['ime_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('radio','mfgloader')
G.edge['radio']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr]'
G.add_edge('radio','s_system_app')
G.edge['radio']['s_system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][open open][setattr getattr]'
G.add_edge('radio','system_app')
G.edge['radio']['system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('radio','ime_app')
G.edge['radio']['ime_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['radio']['ime_app']['fill'] = 'red'
G.add_edge('radio','ime_app')
G.edge['radio']['ime_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read]'
G.add_edge('radio','macloader')
G.edge['radio']['macloader']['write-read'] = '[open open][write read]'
G.edge['radio']['macloader']['fill'] = 'red'
G.add_edge('radio','macloader')
G.edge['radio']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','mfgloader')
G.edge['radio']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['radio']['mfgloader']['fill'] = 'red'
G.add_edge('radio','mfgloader')
G.edge['radio']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read]'
G.edge['radio']['radio']['fill'] = 'red'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read]'
G.add_edge('radio','s_system_app')
G.edge['radio']['s_system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][open open][setattr getattr][write read]'
G.edge['radio']['s_system_app']['fill'] = 'red'
G.add_edge('radio','s_system_app')
G.edge['radio']['s_system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][open open][setattr getattr][write read][append read]'
G.add_edge('radio','system_app')
G.edge['radio']['system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['radio']['system_app']['fill'] = 'red'
G.add_edge('radio','system_app')
G.edge['radio']['system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read]'
G.add_edge('radio','untrusteddomain')
G.edge['radio']['untrusteddomain']['write-read'] = '[write read][append read][open open][write read]'
G.edge['radio']['untrusteddomain']['fill'] = 'red'
G.add_edge('radio','untrusteddomain')
G.edge['radio']['untrusteddomain']['write-read'] = '[write read][append read][open open][write read][append read]'
G.add_edge('samsung_app','ime_app')
G.edge['samsung_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('samsung_app','macloader')
G.edge['samsung_app']['macloader']['write-read'] = '[open open]'
G.add_edge('samsung_app','mfgloader')
G.edge['samsung_app']['mfgloader']['write-read'] = '[open open]'
G.add_edge('samsung_app','radio')
G.edge['samsung_app']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('samsung_app','s_system_app')
G.edge['samsung_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('samsung_app','system_app')
G.edge['samsung_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('samsung_app','untrusteddomain')
G.edge['samsung_app']['untrusteddomain']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('samsung_app','ime_app')
G.edge['samsung_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('samsung_app','mfgloader')
G.edge['samsung_app']['mfgloader']['write-read'] = '[open open][setattr getattr]'
G.add_edge('samsung_app','radio')
G.edge['samsung_app']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('samsung_app','s_system_app')
G.edge['samsung_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('samsung_app','system_app')
G.edge['samsung_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('samsung_app','ime_app')
G.edge['samsung_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['samsung_app']['ime_app']['fill'] = 'red'
G.add_edge('samsung_app','ime_app')
G.edge['samsung_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('samsung_app','macloader')
G.edge['samsung_app']['macloader']['write-read'] = '[open open][write read]'
G.edge['samsung_app']['macloader']['fill'] = 'red'
G.add_edge('samsung_app','macloader')
G.edge['samsung_app']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('samsung_app','mfgloader')
G.edge['samsung_app']['mfgloader']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['samsung_app']['mfgloader']['fill'] = 'red'
G.add_edge('samsung_app','mfgloader')
G.edge['samsung_app']['mfgloader']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('samsung_app','radio')
G.edge['samsung_app']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['samsung_app']['radio']['fill'] = 'red'
G.add_edge('samsung_app','radio')
G.edge['samsung_app']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('samsung_app','s_system_app')
G.edge['samsung_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['samsung_app']['s_system_app']['fill'] = 'red'
G.add_edge('samsung_app','s_system_app')
G.edge['samsung_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('samsung_app','system_app')
G.edge['samsung_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['samsung_app']['system_app']['fill'] = 'red'
G.add_edge('samsung_app','system_app')
G.edge['samsung_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('samsung_app','untrusteddomain')
G.edge['samsung_app']['untrusteddomain']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['samsung_app']['untrusteddomain']['fill'] = 'red'
G.add_edge('samsung_app','untrusteddomain')
G.edge['samsung_app']['untrusteddomain']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][append read][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','macloader')
G.edge['s_system_app']['macloader']['write-read'] = '[open open]'
G.add_edge('s_system_app','mfgloader')
G.edge['s_system_app']['mfgloader']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','radio')
G.edge['s_system_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','untrusteddomain')
G.edge['s_system_app']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][append read][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','mfgloader')
G.edge['s_system_app']['mfgloader']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','radio')
G.edge['s_system_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][append read][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['ime_app']['fill'] = 'red'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][append read][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','macloader')
G.edge['s_system_app']['macloader']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['macloader']['fill'] = 'red'
G.add_edge('s_system_app','macloader')
G.edge['s_system_app']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','mfgloader')
G.edge['s_system_app']['mfgloader']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['mfgloader']['fill'] = 'red'
G.add_edge('s_system_app','mfgloader')
G.edge['s_system_app']['mfgloader']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','radio')
G.edge['s_system_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['radio']['fill'] = 'red'
G.add_edge('s_system_app','radio')
G.edge['s_system_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['system_app']['fill'] = 'red'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','untrusteddomain')
G.edge['s_system_app']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['untrusteddomain']['fill'] = 'red'
G.add_edge('s_system_app','untrusteddomain')
G.edge['s_system_app']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','macloader')
G.edge['system_app']['macloader']['write-read'] = '[open open]'
G.add_edge('system_app','mfgloader')
G.edge['system_app']['mfgloader']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','radio')
G.edge['system_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','untrusteddomain')
G.edge['system_app']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','mfgloader')
G.edge['system_app']['mfgloader']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_app','radio')
G.edge['system_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['ime_app']['fill'] = 'red'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','macloader')
G.edge['system_app']['macloader']['write-read'] = '[open open][write read]'
G.edge['system_app']['macloader']['fill'] = 'red'
G.add_edge('system_app','macloader')
G.edge['system_app']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_app','mfgloader')
G.edge['system_app']['mfgloader']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_app']['mfgloader']['fill'] = 'red'
G.add_edge('system_app','mfgloader')
G.edge['system_app']['mfgloader']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','radio')
G.edge['system_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_app']['radio']['fill'] = 'red'
G.add_edge('system_app','radio')
G.edge['system_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['s_system_app']['fill'] = 'red'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['system_app']['fill'] = 'red'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','untrusteddomain')
G.edge['system_app']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['system_app']['untrusteddomain']['fill'] = 'red'
G.add_edge('system_app','untrusteddomain')
G.edge['system_app']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][add_name search][open open]'
G.add_edge('system_server','macloader')
G.edge['system_server']['macloader']['write-read'] = '[open open]'
G.add_edge('system_server','mfgloader')
G.edge['system_server']['mfgloader']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][open open]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','untrusteddomain')
G.edge['system_server']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][add_name search][open open][setattr getattr]'
G.add_edge('system_server','mfgloader')
G.edge['system_server']['mfgloader']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][open open][setattr getattr]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][add_name search][open open][setattr getattr][write read]'
G.edge['system_server']['ime_app']['fill'] = 'red'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][add_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','macloader')
G.edge['system_server']['macloader']['write-read'] = '[open open][write read]'
G.edge['system_server']['macloader']['fill'] = 'red'
G.add_edge('system_server','macloader')
G.edge['system_server']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','mfgloader')
G.edge['system_server']['mfgloader']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['mfgloader']['fill'] = 'red'
G.add_edge('system_server','mfgloader')
G.edge['system_server']['mfgloader']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][open open][setattr getattr][write read]'
G.edge['system_server']['radio']['fill'] = 'red'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['s_system_app']['fill'] = 'red'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['system_app']['fill'] = 'red'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','untrusteddomain')
G.edge['system_server']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['system_server']['untrusteddomain']['fill'] = 'red'
G.add_edge('system_server','untrusteddomain')
G.edge['system_server']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('tlc_server','ime_app')
G.edge['tlc_server']['ime_app']['write-read'] = '[open open]'
G.add_edge('tlc_server','macloader')
G.edge['tlc_server']['macloader']['write-read'] = '[open open]'
G.add_edge('tlc_server','mfgloader')
G.edge['tlc_server']['mfgloader']['write-read'] = '[open open]'
G.add_edge('tlc_server','radio')
G.edge['tlc_server']['radio']['write-read'] = '[open open]'
G.add_edge('tlc_server','s_system_app')
G.edge['tlc_server']['s_system_app']['write-read'] = '[open open]'
G.add_edge('tlc_server','system_app')
G.edge['tlc_server']['system_app']['write-read'] = '[open open]'
G.add_edge('tlc_server','untrusteddomain')
G.edge['tlc_server']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('tlc_server','ime_app')
G.edge['tlc_server']['ime_app']['write-read'] = '[open open][write read]'
G.edge['tlc_server']['ime_app']['fill'] = 'red'
G.add_edge('tlc_server','ime_app')
G.edge['tlc_server']['ime_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('tlc_server','macloader')
G.edge['tlc_server']['macloader']['write-read'] = '[open open][write read]'
G.edge['tlc_server']['macloader']['fill'] = 'red'
G.add_edge('tlc_server','macloader')
G.edge['tlc_server']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('tlc_server','mfgloader')
G.edge['tlc_server']['mfgloader']['write-read'] = '[open open][write read]'
G.edge['tlc_server']['mfgloader']['fill'] = 'red'
G.add_edge('tlc_server','mfgloader')
G.edge['tlc_server']['mfgloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('tlc_server','radio')
G.edge['tlc_server']['radio']['write-read'] = '[open open][write read]'
G.edge['tlc_server']['radio']['fill'] = 'red'
G.add_edge('tlc_server','radio')
G.edge['tlc_server']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('tlc_server','s_system_app')
G.edge['tlc_server']['s_system_app']['write-read'] = '[open open][write read]'
G.edge['tlc_server']['s_system_app']['fill'] = 'red'
G.add_edge('tlc_server','s_system_app')
G.edge['tlc_server']['s_system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('tlc_server','system_app')
G.edge['tlc_server']['system_app']['write-read'] = '[open open][write read]'
G.edge['tlc_server']['system_app']['fill'] = 'red'
G.add_edge('tlc_server','system_app')
G.edge['tlc_server']['system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('tlc_server','untrusteddomain')
G.edge['tlc_server']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['tlc_server']['untrusteddomain']['fill'] = 'red'
G.add_edge('tlc_server','untrusteddomain')
G.edge['tlc_server']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrusteddomain','ime_app')
G.edge['untrusteddomain']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][write read][add_name search][open open]'
G.add_edge('untrusteddomain','macloader')
G.edge['untrusteddomain']['macloader']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','mfgloader')
G.edge['untrusteddomain']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusteddomain','radio')
G.edge['untrusteddomain']['radio']['write-read'] = '[setattr getattr][write read][write read][open open]'
G.add_edge('untrusteddomain','s_system_app')
G.edge['untrusteddomain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open]'
G.add_edge('untrusteddomain','system_app')
G.edge['untrusteddomain']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open]'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusteddomain','ime_app')
G.edge['untrusteddomain']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][write read][add_name search][open open][setattr getattr]'
G.add_edge('untrusteddomain','mfgloader')
G.edge['untrusteddomain']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('untrusteddomain','radio')
G.edge['untrusteddomain']['radio']['write-read'] = '[setattr getattr][write read][write read][open open][setattr getattr]'
G.add_edge('untrusteddomain','s_system_app')
G.edge['untrusteddomain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr]'
G.add_edge('untrusteddomain','system_app')
G.edge['untrusteddomain']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr]'
G.add_edge('untrusteddomain','ime_app')
G.edge['untrusteddomain']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][write read][add_name search][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['ime_app']['fill'] = 'red'
G.add_edge('untrusteddomain','ime_app')
G.edge['untrusteddomain']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][write read][add_name search][open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','macloader')
G.edge['untrusteddomain']['macloader']['write-read'] = '[open open][write read]'
G.edge['untrusteddomain']['macloader']['fill'] = 'red'
G.add_edge('untrusteddomain','macloader')
G.edge['untrusteddomain']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrusteddomain','mfgloader')
G.edge['untrusteddomain']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['mfgloader']['fill'] = 'red'
G.add_edge('untrusteddomain','mfgloader')
G.edge['untrusteddomain']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','radio')
G.edge['untrusteddomain']['radio']['write-read'] = '[setattr getattr][write read][write read][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['radio']['fill'] = 'red'
G.add_edge('untrusteddomain','radio')
G.edge['untrusteddomain']['radio']['write-read'] = '[setattr getattr][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','s_system_app')
G.edge['untrusteddomain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['s_system_app']['fill'] = 'red'
G.add_edge('untrusteddomain','s_system_app')
G.edge['untrusteddomain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','system_app')
G.edge['untrusteddomain']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['system_app']['fill'] = 'red'
G.add_edge('untrusteddomain','system_app')
G.edge['untrusteddomain']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['untrusteddomain']['untrusteddomain']['fill'] = 'red'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('untrusteddomain','ime_app')
G.edge['untrusteddomain']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][write read][add_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusteddomain','macloader')
G.edge['untrusteddomain']['macloader']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('untrusteddomain','mfgloader')
G.edge['untrusteddomain']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusteddomain','radio')
G.edge['untrusteddomain']['radio']['write-read'] = '[setattr getattr][write read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusteddomain','s_system_app')
G.edge['untrusteddomain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusteddomain','system_app')
G.edge['untrusteddomain']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('untrusteddomain','ime_app')
G.edge['untrusteddomain']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][write read][add_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('untrusteddomain','mfgloader')
G.edge['untrusteddomain']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('untrusteddomain','radio')
G.edge['untrusteddomain']['radio']['write-read'] = '[setattr getattr][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('untrusteddomain','s_system_app')
G.edge['untrusteddomain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('untrusteddomain','system_app')
G.edge['untrusteddomain']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('untrusteddomain','ime_app')
G.edge['untrusteddomain']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][write read][add_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['ime_app']['fill'] = 'red'
G.add_edge('untrusteddomain','ime_app')
G.edge['untrusteddomain']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][write read][add_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','macloader')
G.edge['untrusteddomain']['macloader']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['untrusteddomain']['macloader']['fill'] = 'red'
G.add_edge('untrusteddomain','macloader')
G.edge['untrusteddomain']['macloader']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('untrusteddomain','mfgloader')
G.edge['untrusteddomain']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['mfgloader']['fill'] = 'red'
G.add_edge('untrusteddomain','mfgloader')
G.edge['untrusteddomain']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','radio')
G.edge['untrusteddomain']['radio']['write-read'] = '[setattr getattr][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['radio']['fill'] = 'red'
G.add_edge('untrusteddomain','radio')
G.edge['untrusteddomain']['radio']['write-read'] = '[setattr getattr][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','s_system_app')
G.edge['untrusteddomain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['s_system_app']['fill'] = 'red'
G.add_edge('untrusteddomain','s_system_app')
G.edge['untrusteddomain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','system_app')
G.edge['untrusteddomain']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['system_app']['fill'] = 'red'
G.add_edge('untrusteddomain','system_app')
G.edge['untrusteddomain']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['untrusteddomain']['untrusteddomain']['fill'] = 'red'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()