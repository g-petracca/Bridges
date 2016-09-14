import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('at_distributor','at_distributor')
G.edge['at_distributor']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','ime_app')
G.edge['at_distributor']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','knox_system_app')
G.edge['at_distributor']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('at_distributor','mediaserver')
G.edge['at_distributor']['mediaserver']['write-read'] = '[open open]'
G.add_edge('at_distributor','nfc')
G.edge['at_distributor']['nfc']['write-read'] = '[open open]'
G.add_edge('at_distributor','platformappdomain')
G.edge['at_distributor']['platformappdomain']['write-read'] = '[open open]'
G.add_edge('at_distributor','radio')
G.edge['at_distributor']['radio']['write-read'] = '[open open]'
G.add_edge('at_distributor','rild')
G.edge['at_distributor']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','sec-ril')
G.edge['at_distributor']['sec-ril']['write-read'] = '[open open]'
G.add_edge('at_distributor','sem')
G.edge['at_distributor']['sem']['write-read'] = '[open open]'
G.add_edge('at_distributor','s_system_app')
G.edge['at_distributor']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','system_app')
G.edge['at_distributor']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','system_server')
G.edge['at_distributor']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open]'
G.add_edge('at_distributor','at_distributor')
G.edge['at_distributor']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('at_distributor','ime_app')
G.edge['at_distributor']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('at_distributor','knox_system_app')
G.edge['at_distributor']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','mediaserver')
G.edge['at_distributor']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','nfc')
G.edge['at_distributor']['nfc']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','platformappdomain')
G.edge['at_distributor']['platformappdomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','radio')
G.edge['at_distributor']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','rild')
G.edge['at_distributor']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('at_distributor','sec-ril')
G.edge['at_distributor']['sec-ril']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','sem')
G.edge['at_distributor']['sem']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','s_system_app')
G.edge['at_distributor']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('at_distributor','system_app')
G.edge['at_distributor']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('at_distributor','system_server')
G.edge['at_distributor']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr]'
G.add_edge('at_distributor','at_distributor')
G.edge['at_distributor']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['at_distributor']['at_distributor']['fill'] = 'red'
G.add_edge('at_distributor','at_distributor')
G.edge['at_distributor']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('at_distributor','ime_app')
G.edge['at_distributor']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['at_distributor']['ime_app']['fill'] = 'red'
G.add_edge('at_distributor','ime_app')
G.edge['at_distributor']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('at_distributor','knox_system_app')
G.edge['at_distributor']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['knox_system_app']['fill'] = 'red'
G.add_edge('at_distributor','knox_system_app')
G.edge['at_distributor']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('at_distributor','mediaserver')
G.edge['at_distributor']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['mediaserver']['fill'] = 'red'
G.add_edge('at_distributor','mediaserver')
G.edge['at_distributor']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('at_distributor','nfc')
G.edge['at_distributor']['nfc']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['nfc']['fill'] = 'red'
G.add_edge('at_distributor','nfc')
G.edge['at_distributor']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('at_distributor','platformappdomain')
G.edge['at_distributor']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['platformappdomain']['fill'] = 'red'
G.add_edge('at_distributor','platformappdomain')
G.edge['at_distributor']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('at_distributor','radio')
G.edge['at_distributor']['radio']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['radio']['fill'] = 'red'
G.add_edge('at_distributor','radio')
G.edge['at_distributor']['radio']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('at_distributor','rild')
G.edge['at_distributor']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['at_distributor']['rild']['fill'] = 'red'
G.add_edge('at_distributor','rild')
G.edge['at_distributor']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('at_distributor','sec-ril')
G.edge['at_distributor']['sec-ril']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['sec-ril']['fill'] = 'red'
G.add_edge('at_distributor','sec-ril')
G.edge['at_distributor']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('at_distributor','sem')
G.edge['at_distributor']['sem']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['sem']['fill'] = 'red'
G.add_edge('at_distributor','sem')
G.edge['at_distributor']['sem']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('at_distributor','s_system_app')
G.edge['at_distributor']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['at_distributor']['s_system_app']['fill'] = 'red'
G.add_edge('at_distributor','s_system_app')
G.edge['at_distributor']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('at_distributor','system_app')
G.edge['at_distributor']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['at_distributor']['system_app']['fill'] = 'red'
G.add_edge('at_distributor','system_app')
G.edge['at_distributor']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('at_distributor','system_server')
G.edge['at_distributor']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['at_distributor']['system_server']['fill'] = 'red'
G.add_edge('at_distributor','system_server')
G.edge['at_distributor']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','at_distributor')
G.edge['ime_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','knox_system_app')
G.edge['ime_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','mediaserver')
G.edge['ime_app']['mediaserver']['write-read'] = '[open open]'
G.add_edge('ime_app','nfc')
G.edge['ime_app']['nfc']['write-read'] = '[open open]'
G.add_edge('ime_app','platformappdomain')
G.edge['ime_app']['platformappdomain']['write-read'] = '[open open]'
G.add_edge('ime_app','radio')
G.edge['ime_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('ime_app','rild')
G.edge['ime_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open]'
G.add_edge('ime_app','sec-ril')
G.edge['ime_app']['sec-ril']['write-read'] = '[open open]'
G.add_edge('ime_app','sem')
G.edge['ime_app']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','at_distributor')
G.edge['ime_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','knox_system_app')
G.edge['ime_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','mediaserver')
G.edge['ime_app']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','nfc')
G.edge['ime_app']['nfc']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','platformappdomain')
G.edge['ime_app']['platformappdomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','radio')
G.edge['ime_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','rild')
G.edge['ime_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','sec-ril')
G.edge['ime_app']['sec-ril']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','sem')
G.edge['ime_app']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','at_distributor')
G.edge['ime_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ime_app']['at_distributor']['fill'] = 'red'
G.add_edge('ime_app','at_distributor')
G.edge['ime_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['ime_app']['fill'] = 'red'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','knox_system_app')
G.edge['ime_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['knox_system_app']['fill'] = 'red'
G.add_edge('ime_app','knox_system_app')
G.edge['ime_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','mediaserver')
G.edge['ime_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['mediaserver']['fill'] = 'red'
G.add_edge('ime_app','mediaserver')
G.edge['ime_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','nfc')
G.edge['ime_app']['nfc']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['nfc']['fill'] = 'red'
G.add_edge('ime_app','nfc')
G.edge['ime_app']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','platformappdomain')
G.edge['ime_app']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['platformappdomain']['fill'] = 'red'
G.add_edge('ime_app','platformappdomain')
G.edge['ime_app']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','radio')
G.edge['ime_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['radio']['fill'] = 'red'
G.add_edge('ime_app','radio')
G.edge['ime_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','rild')
G.edge['ime_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['rild']['fill'] = 'red'
G.add_edge('ime_app','rild')
G.edge['ime_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','sec-ril')
G.edge['ime_app']['sec-ril']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['sec-ril']['fill'] = 'red'
G.add_edge('ime_app','sec-ril')
G.edge['ime_app']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','sem')
G.edge['ime_app']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ime_app']['sem']['fill'] = 'red'
G.add_edge('ime_app','sem')
G.edge['ime_app']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['s_system_app']['fill'] = 'red'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['system_app']['fill'] = 'red'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['system_server']['fill'] = 'red'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','at_distributor')
G.edge['knox_system_app']['at_distributor']['write-read'] = '[open open]'
G.add_edge('knox_system_app','ime_app')
G.edge['knox_system_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_system_app','mediaserver')
G.edge['knox_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_system_app','nfc')
G.edge['knox_system_app']['nfc']['write-read'] = '[open open]'
G.add_edge('knox_system_app','platformappdomain')
G.edge['knox_system_app']['platformappdomain']['write-read'] = '[open open]'
G.add_edge('knox_system_app','radio')
G.edge['knox_system_app']['radio']['write-read'] = '[open open]'
G.add_edge('knox_system_app','rild')
G.edge['knox_system_app']['rild']['write-read'] = '[open open]'
G.add_edge('knox_system_app','sec-ril')
G.edge['knox_system_app']['sec-ril']['write-read'] = '[open open]'
G.add_edge('knox_system_app','sem')
G.edge['knox_system_app']['sem']['write-read'] = '[open open]'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_system_app','system_app')
G.edge['knox_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_system_app','at_distributor')
G.edge['knox_system_app']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','ime_app')
G.edge['knox_system_app']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('knox_system_app','mediaserver')
G.edge['knox_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('knox_system_app','nfc')
G.edge['knox_system_app']['nfc']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','platformappdomain')
G.edge['knox_system_app']['platformappdomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','radio')
G.edge['knox_system_app']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','rild')
G.edge['knox_system_app']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','sec-ril')
G.edge['knox_system_app']['sec-ril']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','sem')
G.edge['knox_system_app']['sem']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('knox_system_app','system_app')
G.edge['knox_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('knox_system_app','at_distributor')
G.edge['knox_system_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['at_distributor']['fill'] = 'red'
G.add_edge('knox_system_app','at_distributor')
G.edge['knox_system_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','ime_app')
G.edge['knox_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['ime_app']['fill'] = 'red'
G.add_edge('knox_system_app','ime_app')
G.edge['knox_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_system_app']['knox_system_app']['fill'] = 'red'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','mediaserver')
G.edge['knox_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['knox_system_app']['mediaserver']['fill'] = 'red'
G.add_edge('knox_system_app','mediaserver')
G.edge['knox_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','nfc')
G.edge['knox_system_app']['nfc']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['nfc']['fill'] = 'red'
G.add_edge('knox_system_app','nfc')
G.edge['knox_system_app']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','platformappdomain')
G.edge['knox_system_app']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['platformappdomain']['fill'] = 'red'
G.add_edge('knox_system_app','platformappdomain')
G.edge['knox_system_app']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','radio')
G.edge['knox_system_app']['radio']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['radio']['fill'] = 'red'
G.add_edge('knox_system_app','radio')
G.edge['knox_system_app']['radio']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','rild')
G.edge['knox_system_app']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['rild']['fill'] = 'red'
G.add_edge('knox_system_app','rild')
G.edge['knox_system_app']['rild']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','sec-ril')
G.edge['knox_system_app']['sec-ril']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['sec-ril']['fill'] = 'red'
G.add_edge('knox_system_app','sec-ril')
G.edge['knox_system_app']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','sem')
G.edge['knox_system_app']['sem']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['sem']['fill'] = 'red'
G.add_edge('knox_system_app','sem')
G.edge['knox_system_app']['sem']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','system_app')
G.edge['knox_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_system_app']['system_app']['fill'] = 'red'
G.add_edge('knox_system_app','system_app')
G.edge['knox_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_system_app']['system_server']['fill'] = 'red'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','at_distributor')
G.edge['mediaserver']['at_distributor']['write-read'] = '[open open]'
G.add_edge('mediaserver','ime_app')
G.edge['mediaserver']['ime_app']['write-read'] = '[open open]'
G.add_edge('mediaserver','knox_system_app')
G.edge['mediaserver']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','nfc')
G.edge['mediaserver']['nfc']['write-read'] = '[open open]'
G.add_edge('mediaserver','platformappdomain')
G.edge['mediaserver']['platformappdomain']['write-read'] = '[open open]'
G.add_edge('mediaserver','radio')
G.edge['mediaserver']['radio']['write-read'] = '[open open]'
G.add_edge('mediaserver','rild')
G.edge['mediaserver']['rild']['write-read'] = '[open open]'
G.add_edge('mediaserver','sec-ril')
G.edge['mediaserver']['sec-ril']['write-read'] = '[open open]'
G.add_edge('mediaserver','sem')
G.edge['mediaserver']['sem']['write-read'] = '[open open]'
G.add_edge('mediaserver','s_system_app')
G.edge['mediaserver']['s_system_app']['write-read'] = '[open open]'
G.add_edge('mediaserver','system_app')
G.edge['mediaserver']['system_app']['write-read'] = '[open open]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','at_distributor')
G.edge['mediaserver']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','ime_app')
G.edge['mediaserver']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','knox_system_app')
G.edge['mediaserver']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('mediaserver','nfc')
G.edge['mediaserver']['nfc']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','platformappdomain')
G.edge['mediaserver']['platformappdomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','radio')
G.edge['mediaserver']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','rild')
G.edge['mediaserver']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','sec-ril')
G.edge['mediaserver']['sec-ril']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','sem')
G.edge['mediaserver']['sem']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','s_system_app')
G.edge['mediaserver']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','system_app')
G.edge['mediaserver']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('mediaserver','at_distributor')
G.edge['mediaserver']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['at_distributor']['fill'] = 'red'
G.add_edge('mediaserver','at_distributor')
G.edge['mediaserver']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','ime_app')
G.edge['mediaserver']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['ime_app']['fill'] = 'red'
G.add_edge('mediaserver','ime_app')
G.edge['mediaserver']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','knox_system_app')
G.edge['mediaserver']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['mediaserver']['knox_system_app']['fill'] = 'red'
G.add_edge('mediaserver','knox_system_app')
G.edge['mediaserver']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['mediaserver']['mediaserver']['fill'] = 'red'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','nfc')
G.edge['mediaserver']['nfc']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['nfc']['fill'] = 'red'
G.add_edge('mediaserver','nfc')
G.edge['mediaserver']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','platformappdomain')
G.edge['mediaserver']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['platformappdomain']['fill'] = 'red'
G.add_edge('mediaserver','platformappdomain')
G.edge['mediaserver']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','radio')
G.edge['mediaserver']['radio']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['radio']['fill'] = 'red'
G.add_edge('mediaserver','radio')
G.edge['mediaserver']['radio']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','rild')
G.edge['mediaserver']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['rild']['fill'] = 'red'
G.add_edge('mediaserver','rild')
G.edge['mediaserver']['rild']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','sec-ril')
G.edge['mediaserver']['sec-ril']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['sec-ril']['fill'] = 'red'
G.add_edge('mediaserver','sec-ril')
G.edge['mediaserver']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','sem')
G.edge['mediaserver']['sem']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['sem']['fill'] = 'red'
G.add_edge('mediaserver','sem')
G.edge['mediaserver']['sem']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','s_system_app')
G.edge['mediaserver']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['s_system_app']['fill'] = 'red'
G.add_edge('mediaserver','s_system_app')
G.edge['mediaserver']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','system_app')
G.edge['mediaserver']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['system_app']['fill'] = 'red'
G.add_edge('mediaserver','system_app')
G.edge['mediaserver']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['mediaserver']['system_server']['fill'] = 'red'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr15','at_distributor')
G.edge['newAttr15']['at_distributor']['write-read'] = '[open open]'
G.add_edge('newAttr15','ime_app')
G.edge['newAttr15']['ime_app']['write-read'] = '[open open]'
G.add_edge('newAttr15','knox_system_app')
G.edge['newAttr15']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('newAttr15','mediaserver')
G.edge['newAttr15']['mediaserver']['write-read'] = '[open open]'
G.add_edge('newAttr15','nfc')
G.edge['newAttr15']['nfc']['write-read'] = '[open open]'
G.add_edge('newAttr15','platformappdomain')
G.edge['newAttr15']['platformappdomain']['write-read'] = '[open open]'
G.add_edge('newAttr15','radio')
G.edge['newAttr15']['radio']['write-read'] = '[open open]'
G.add_edge('newAttr15','rild')
G.edge['newAttr15']['rild']['write-read'] = '[open open]'
G.add_edge('newAttr15','sec-ril')
G.edge['newAttr15']['sec-ril']['write-read'] = '[open open]'
G.add_edge('newAttr15','sem')
G.edge['newAttr15']['sem']['write-read'] = '[open open]'
G.add_edge('newAttr15','s_system_app')
G.edge['newAttr15']['s_system_app']['write-read'] = '[open open]'
G.add_edge('newAttr15','system_app')
G.edge['newAttr15']['system_app']['write-read'] = '[open open]'
G.add_edge('newAttr15','system_server')
G.edge['newAttr15']['system_server']['write-read'] = '[open open]'
G.add_edge('newAttr15','at_distributor')
G.edge['newAttr15']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr15','ime_app')
G.edge['newAttr15']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr15','knox_system_app')
G.edge['newAttr15']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr15','mediaserver')
G.edge['newAttr15']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr15','nfc')
G.edge['newAttr15']['nfc']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr15','platformappdomain')
G.edge['newAttr15']['platformappdomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr15','radio')
G.edge['newAttr15']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr15','rild')
G.edge['newAttr15']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr15','sec-ril')
G.edge['newAttr15']['sec-ril']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr15','sem')
G.edge['newAttr15']['sem']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr15','s_system_app')
G.edge['newAttr15']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr15','system_app')
G.edge['newAttr15']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr15','system_server')
G.edge['newAttr15']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr15','at_distributor')
G.edge['newAttr15']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr15']['at_distributor']['fill'] = 'red'
G.add_edge('newAttr15','at_distributor')
G.edge['newAttr15']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr15','ime_app')
G.edge['newAttr15']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr15']['ime_app']['fill'] = 'red'
G.add_edge('newAttr15','ime_app')
G.edge['newAttr15']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr15','knox_system_app')
G.edge['newAttr15']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr15']['knox_system_app']['fill'] = 'red'
G.add_edge('newAttr15','knox_system_app')
G.edge['newAttr15']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr15','mediaserver')
G.edge['newAttr15']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr15']['mediaserver']['fill'] = 'red'
G.add_edge('newAttr15','mediaserver')
G.edge['newAttr15']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr15','nfc')
G.edge['newAttr15']['nfc']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr15']['nfc']['fill'] = 'red'
G.add_edge('newAttr15','nfc')
G.edge['newAttr15']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr15','platformappdomain')
G.edge['newAttr15']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr15']['platformappdomain']['fill'] = 'red'
G.add_edge('newAttr15','platformappdomain')
G.edge['newAttr15']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr15','radio')
G.edge['newAttr15']['radio']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr15']['radio']['fill'] = 'red'
G.add_edge('newAttr15','radio')
G.edge['newAttr15']['radio']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr15','rild')
G.edge['newAttr15']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr15']['rild']['fill'] = 'red'
G.add_edge('newAttr15','rild')
G.edge['newAttr15']['rild']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr15','sec-ril')
G.edge['newAttr15']['sec-ril']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr15']['sec-ril']['fill'] = 'red'
G.add_edge('newAttr15','sec-ril')
G.edge['newAttr15']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr15','sem')
G.edge['newAttr15']['sem']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr15']['sem']['fill'] = 'red'
G.add_edge('newAttr15','sem')
G.edge['newAttr15']['sem']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr15','s_system_app')
G.edge['newAttr15']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr15']['s_system_app']['fill'] = 'red'
G.add_edge('newAttr15','s_system_app')
G.edge['newAttr15']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr15','system_app')
G.edge['newAttr15']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr15']['system_app']['fill'] = 'red'
G.add_edge('newAttr15','system_app')
G.edge['newAttr15']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr15','system_server')
G.edge['newAttr15']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr15']['system_server']['fill'] = 'red'
G.add_edge('newAttr15','system_server')
G.edge['newAttr15']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('nfc','at_distributor')
G.edge['nfc']['at_distributor']['write-read'] = '[open open]'
G.add_edge('nfc','ime_app')
G.edge['nfc']['ime_app']['write-read'] = '[open open]'
G.add_edge('nfc','knox_system_app')
G.edge['nfc']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('nfc','mediaserver')
G.edge['nfc']['mediaserver']['write-read'] = '[open open]'
G.add_edge('nfc','nfc')
G.edge['nfc']['nfc']['write-read'] = '[open open]'
G.add_edge('nfc','platformappdomain')
G.edge['nfc']['platformappdomain']['write-read'] = '[open open]'
G.add_edge('nfc','radio')
G.edge['nfc']['radio']['write-read'] = '[open open]'
G.add_edge('nfc','rild')
G.edge['nfc']['rild']['write-read'] = '[open open]'
G.add_edge('nfc','sec-ril')
G.edge['nfc']['sec-ril']['write-read'] = '[open open]'
G.add_edge('nfc','sem')
G.edge['nfc']['sem']['write-read'] = '[open open]'
G.add_edge('nfc','s_system_app')
G.edge['nfc']['s_system_app']['write-read'] = '[open open]'
G.add_edge('nfc','system_app')
G.edge['nfc']['system_app']['write-read'] = '[open open]'
G.add_edge('nfc','system_server')
G.edge['nfc']['system_server']['write-read'] = '[open open]'
G.add_edge('nfc','at_distributor')
G.edge['nfc']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('nfc','ime_app')
G.edge['nfc']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('nfc','knox_system_app')
G.edge['nfc']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('nfc','mediaserver')
G.edge['nfc']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('nfc','nfc')
G.edge['nfc']['nfc']['write-read'] = '[open open][setattr getattr]'
G.add_edge('nfc','platformappdomain')
G.edge['nfc']['platformappdomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('nfc','radio')
G.edge['nfc']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('nfc','rild')
G.edge['nfc']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('nfc','sec-ril')
G.edge['nfc']['sec-ril']['write-read'] = '[open open][setattr getattr]'
G.add_edge('nfc','sem')
G.edge['nfc']['sem']['write-read'] = '[open open][setattr getattr]'
G.add_edge('nfc','s_system_app')
G.edge['nfc']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('nfc','system_app')
G.edge['nfc']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('nfc','system_server')
G.edge['nfc']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('nfc','at_distributor')
G.edge['nfc']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['nfc']['at_distributor']['fill'] = 'red'
G.add_edge('nfc','at_distributor')
G.edge['nfc']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('nfc','ime_app')
G.edge['nfc']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['nfc']['ime_app']['fill'] = 'red'
G.add_edge('nfc','ime_app')
G.edge['nfc']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('nfc','knox_system_app')
G.edge['nfc']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['nfc']['knox_system_app']['fill'] = 'red'
G.add_edge('nfc','knox_system_app')
G.edge['nfc']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('nfc','mediaserver')
G.edge['nfc']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['nfc']['mediaserver']['fill'] = 'red'
G.add_edge('nfc','mediaserver')
G.edge['nfc']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('nfc','nfc')
G.edge['nfc']['nfc']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['nfc']['nfc']['fill'] = 'red'
G.add_edge('nfc','nfc')
G.edge['nfc']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('nfc','platformappdomain')
G.edge['nfc']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['nfc']['platformappdomain']['fill'] = 'red'
G.add_edge('nfc','platformappdomain')
G.edge['nfc']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('nfc','radio')
G.edge['nfc']['radio']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['nfc']['radio']['fill'] = 'red'
G.add_edge('nfc','radio')
G.edge['nfc']['radio']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('nfc','rild')
G.edge['nfc']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['nfc']['rild']['fill'] = 'red'
G.add_edge('nfc','rild')
G.edge['nfc']['rild']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('nfc','sec-ril')
G.edge['nfc']['sec-ril']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['nfc']['sec-ril']['fill'] = 'red'
G.add_edge('nfc','sec-ril')
G.edge['nfc']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('nfc','sem')
G.edge['nfc']['sem']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['nfc']['sem']['fill'] = 'red'
G.add_edge('nfc','sem')
G.edge['nfc']['sem']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('nfc','s_system_app')
G.edge['nfc']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['nfc']['s_system_app']['fill'] = 'red'
G.add_edge('nfc','s_system_app')
G.edge['nfc']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('nfc','system_app')
G.edge['nfc']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['nfc']['system_app']['fill'] = 'red'
G.add_edge('nfc','system_app')
G.edge['nfc']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('nfc','system_server')
G.edge['nfc']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['nfc']['system_server']['fill'] = 'red'
G.add_edge('nfc','system_server')
G.edge['nfc']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('platformappdomain','at_distributor')
G.edge['platformappdomain']['at_distributor']['write-read'] = '[open open]'
G.add_edge('platformappdomain','ime_app')
G.edge['platformappdomain']['ime_app']['write-read'] = '[open open]'
G.add_edge('platformappdomain','knox_system_app')
G.edge['platformappdomain']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('platformappdomain','mediaserver')
G.edge['platformappdomain']['mediaserver']['write-read'] = '[open open]'
G.add_edge('platformappdomain','nfc')
G.edge['platformappdomain']['nfc']['write-read'] = '[open open]'
G.add_edge('platformappdomain','platformappdomain')
G.edge['platformappdomain']['platformappdomain']['write-read'] = '[open open]'
G.add_edge('platformappdomain','radio')
G.edge['platformappdomain']['radio']['write-read'] = '[open open]'
G.add_edge('platformappdomain','rild')
G.edge['platformappdomain']['rild']['write-read'] = '[open open]'
G.add_edge('platformappdomain','sec-ril')
G.edge['platformappdomain']['sec-ril']['write-read'] = '[open open]'
G.add_edge('platformappdomain','sem')
G.edge['platformappdomain']['sem']['write-read'] = '[open open]'
G.add_edge('platformappdomain','s_system_app')
G.edge['platformappdomain']['s_system_app']['write-read'] = '[open open]'
G.add_edge('platformappdomain','system_app')
G.edge['platformappdomain']['system_app']['write-read'] = '[open open]'
G.add_edge('platformappdomain','system_server')
G.edge['platformappdomain']['system_server']['write-read'] = '[open open]'
G.add_edge('platformappdomain','at_distributor')
G.edge['platformappdomain']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platformappdomain','ime_app')
G.edge['platformappdomain']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platformappdomain','knox_system_app')
G.edge['platformappdomain']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platformappdomain','mediaserver')
G.edge['platformappdomain']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platformappdomain','nfc')
G.edge['platformappdomain']['nfc']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platformappdomain','platformappdomain')
G.edge['platformappdomain']['platformappdomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platformappdomain','radio')
G.edge['platformappdomain']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platformappdomain','rild')
G.edge['platformappdomain']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platformappdomain','sec-ril')
G.edge['platformappdomain']['sec-ril']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platformappdomain','sem')
G.edge['platformappdomain']['sem']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platformappdomain','s_system_app')
G.edge['platformappdomain']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platformappdomain','system_app')
G.edge['platformappdomain']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platformappdomain','system_server')
G.edge['platformappdomain']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platformappdomain','at_distributor')
G.edge['platformappdomain']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platformappdomain']['at_distributor']['fill'] = 'red'
G.add_edge('platformappdomain','at_distributor')
G.edge['platformappdomain']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('platformappdomain','ime_app')
G.edge['platformappdomain']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platformappdomain']['ime_app']['fill'] = 'red'
G.add_edge('platformappdomain','ime_app')
G.edge['platformappdomain']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('platformappdomain','knox_system_app')
G.edge['platformappdomain']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platformappdomain']['knox_system_app']['fill'] = 'red'
G.add_edge('platformappdomain','knox_system_app')
G.edge['platformappdomain']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('platformappdomain','mediaserver')
G.edge['platformappdomain']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platformappdomain']['mediaserver']['fill'] = 'red'
G.add_edge('platformappdomain','mediaserver')
G.edge['platformappdomain']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('platformappdomain','nfc')
G.edge['platformappdomain']['nfc']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platformappdomain']['nfc']['fill'] = 'red'
G.add_edge('platformappdomain','nfc')
G.edge['platformappdomain']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('platformappdomain','platformappdomain')
G.edge['platformappdomain']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platformappdomain']['platformappdomain']['fill'] = 'red'
G.add_edge('platformappdomain','platformappdomain')
G.edge['platformappdomain']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('platformappdomain','radio')
G.edge['platformappdomain']['radio']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platformappdomain']['radio']['fill'] = 'red'
G.add_edge('platformappdomain','radio')
G.edge['platformappdomain']['radio']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('platformappdomain','rild')
G.edge['platformappdomain']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platformappdomain']['rild']['fill'] = 'red'
G.add_edge('platformappdomain','rild')
G.edge['platformappdomain']['rild']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('platformappdomain','sec-ril')
G.edge['platformappdomain']['sec-ril']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platformappdomain']['sec-ril']['fill'] = 'red'
G.add_edge('platformappdomain','sec-ril')
G.edge['platformappdomain']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('platformappdomain','sem')
G.edge['platformappdomain']['sem']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platformappdomain']['sem']['fill'] = 'red'
G.add_edge('platformappdomain','sem')
G.edge['platformappdomain']['sem']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('platformappdomain','s_system_app')
G.edge['platformappdomain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platformappdomain']['s_system_app']['fill'] = 'red'
G.add_edge('platformappdomain','s_system_app')
G.edge['platformappdomain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('platformappdomain','system_app')
G.edge['platformappdomain']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platformappdomain']['system_app']['fill'] = 'red'
G.add_edge('platformappdomain','system_app')
G.edge['platformappdomain']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('platformappdomain','system_server')
G.edge['platformappdomain']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platformappdomain']['system_server']['fill'] = 'red'
G.add_edge('platformappdomain','system_server')
G.edge['platformappdomain']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('radio','at_distributor')
G.edge['radio']['at_distributor']['write-read'] = '[open open]'
G.add_edge('radio','ime_app')
G.edge['radio']['ime_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('radio','knox_system_app')
G.edge['radio']['knox_system_app']['write-read'] = '[add_name search][remove_name search][open open]'
G.add_edge('radio','mediaserver')
G.edge['radio']['mediaserver']['write-read'] = '[add_name search][remove_name search][open open]'
G.add_edge('radio','nfc')
G.edge['radio']['nfc']['write-read'] = '[open open]'
G.add_edge('radio','platformappdomain')
G.edge['radio']['platformappdomain']['write-read'] = '[open open]'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('radio','rild')
G.edge['radio']['rild']['write-read'] = '[open open]'
G.add_edge('radio','sec-ril')
G.edge['radio']['sec-ril']['write-read'] = '[open open]'
G.add_edge('radio','sem')
G.edge['radio']['sem']['write-read'] = '[open open]'
G.add_edge('radio','s_system_app')
G.edge['radio']['s_system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('radio','system_app')
G.edge['radio']['system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('radio','system_server')
G.edge['radio']['system_server']['write-read'] = '[add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('radio','at_distributor')
G.edge['radio']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','ime_app')
G.edge['radio']['ime_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('radio','knox_system_app')
G.edge['radio']['knox_system_app']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('radio','mediaserver')
G.edge['radio']['mediaserver']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('radio','nfc')
G.edge['radio']['nfc']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','platformappdomain')
G.edge['radio']['platformappdomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('radio','rild')
G.edge['radio']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','sec-ril')
G.edge['radio']['sec-ril']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','sem')
G.edge['radio']['sem']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','s_system_app')
G.edge['radio']['s_system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('radio','system_app')
G.edge['radio']['system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('radio','system_server')
G.edge['radio']['system_server']['write-read'] = '[add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('radio','at_distributor')
G.edge['radio']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['radio']['at_distributor']['fill'] = 'red'
G.add_edge('radio','at_distributor')
G.edge['radio']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('radio','ime_app')
G.edge['radio']['ime_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['radio']['ime_app']['fill'] = 'red'
G.add_edge('radio','ime_app')
G.edge['radio']['ime_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('radio','knox_system_app')
G.edge['radio']['knox_system_app']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['radio']['knox_system_app']['fill'] = 'red'
G.add_edge('radio','knox_system_app')
G.edge['radio']['knox_system_app']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('radio','mediaserver')
G.edge['radio']['mediaserver']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['radio']['mediaserver']['fill'] = 'red'
G.add_edge('radio','mediaserver')
G.edge['radio']['mediaserver']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('radio','nfc')
G.edge['radio']['nfc']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['radio']['nfc']['fill'] = 'red'
G.add_edge('radio','nfc')
G.edge['radio']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('radio','platformappdomain')
G.edge['radio']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['radio']['platformappdomain']['fill'] = 'red'
G.add_edge('radio','platformappdomain')
G.edge['radio']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['radio']['radio']['fill'] = 'red'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('radio','rild')
G.edge['radio']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['radio']['rild']['fill'] = 'red'
G.add_edge('radio','rild')
G.edge['radio']['rild']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('radio','sec-ril')
G.edge['radio']['sec-ril']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['radio']['sec-ril']['fill'] = 'red'
G.add_edge('radio','sec-ril')
G.edge['radio']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('radio','sem')
G.edge['radio']['sem']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['radio']['sem']['fill'] = 'red'
G.add_edge('radio','sem')
G.edge['radio']['sem']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('radio','s_system_app')
G.edge['radio']['s_system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['radio']['s_system_app']['fill'] = 'red'
G.add_edge('radio','s_system_app')
G.edge['radio']['s_system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('radio','system_app')
G.edge['radio']['system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['radio']['system_app']['fill'] = 'red'
G.add_edge('radio','system_app')
G.edge['radio']['system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('radio','system_server')
G.edge['radio']['system_server']['write-read'] = '[add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['radio']['system_server']['fill'] = 'red'
G.add_edge('radio','system_server')
G.edge['radio']['system_server']['write-read'] = '[add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('rild','at_distributor')
G.edge['rild']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','ime_app')
G.edge['rild']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open]'
G.add_edge('rild','knox_system_app')
G.edge['rild']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('rild','mediaserver')
G.edge['rild']['mediaserver']['write-read'] = '[open open]'
G.add_edge('rild','nfc')
G.edge['rild']['nfc']['write-read'] = '[open open]'
G.add_edge('rild','platformappdomain')
G.edge['rild']['platformappdomain']['write-read'] = '[open open]'
G.add_edge('rild','radio')
G.edge['rild']['radio']['write-read'] = '[open open]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open]'
G.add_edge('rild','sec-ril')
G.edge['rild']['sec-ril']['write-read'] = '[open open]'
G.add_edge('rild','sem')
G.edge['rild']['sem']['write-read'] = '[open open]'
G.add_edge('rild','s_system_app')
G.edge['rild']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open]'
G.add_edge('rild','system_app')
G.edge['rild']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open]'
G.add_edge('rild','at_distributor')
G.edge['rild']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('rild','ime_app')
G.edge['rild']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr]'
G.add_edge('rild','knox_system_app')
G.edge['rild']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','mediaserver')
G.edge['rild']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','nfc')
G.edge['rild']['nfc']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','platformappdomain')
G.edge['rild']['platformappdomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','radio')
G.edge['rild']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('rild','sec-ril')
G.edge['rild']['sec-ril']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','sem')
G.edge['rild']['sem']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','s_system_app')
G.edge['rild']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr]'
G.add_edge('rild','system_app')
G.edge['rild']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr]'
G.add_edge('rild','at_distributor')
G.edge['rild']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['rild']['at_distributor']['fill'] = 'red'
G.add_edge('rild','at_distributor')
G.edge['rild']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('rild','ime_app')
G.edge['rild']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr][write read]'
G.edge['rild']['ime_app']['fill'] = 'red'
G.add_edge('rild','ime_app')
G.edge['rild']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr][write read][append read]'
G.add_edge('rild','knox_system_app')
G.edge['rild']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['knox_system_app']['fill'] = 'red'
G.add_edge('rild','knox_system_app')
G.edge['rild']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('rild','mediaserver')
G.edge['rild']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['mediaserver']['fill'] = 'red'
G.add_edge('rild','mediaserver')
G.edge['rild']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('rild','nfc')
G.edge['rild']['nfc']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['nfc']['fill'] = 'red'
G.add_edge('rild','nfc')
G.edge['rild']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('rild','platformappdomain')
G.edge['rild']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['platformappdomain']['fill'] = 'red'
G.add_edge('rild','platformappdomain')
G.edge['rild']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('rild','radio')
G.edge['rild']['radio']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['radio']['fill'] = 'red'
G.add_edge('rild','radio')
G.edge['rild']['radio']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['rild']['fill'] = 'red'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('rild','sec-ril')
G.edge['rild']['sec-ril']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['sec-ril']['fill'] = 'red'
G.add_edge('rild','sec-ril')
G.edge['rild']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('rild','sem')
G.edge['rild']['sem']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['sem']['fill'] = 'red'
G.add_edge('rild','sem')
G.edge['rild']['sem']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('rild','s_system_app')
G.edge['rild']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr][write read]'
G.edge['rild']['s_system_app']['fill'] = 'red'
G.add_edge('rild','s_system_app')
G.edge['rild']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr][write read][append read]'
G.add_edge('rild','system_app')
G.edge['rild']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr][write read]'
G.edge['rild']['system_app']['fill'] = 'red'
G.add_edge('rild','system_app')
G.edge['rild']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr][write read][append read]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['system_server']['fill'] = 'red'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('sec-ril','at_distributor')
G.edge['sec-ril']['at_distributor']['write-read'] = '[open open]'
G.add_edge('sec-ril','ime_app')
G.edge['sec-ril']['ime_app']['write-read'] = '[write read][open open]'
G.add_edge('sec-ril','knox_system_app')
G.edge['sec-ril']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('sec-ril','mediaserver')
G.edge['sec-ril']['mediaserver']['write-read'] = '[open open]'
G.add_edge('sec-ril','nfc')
G.edge['sec-ril']['nfc']['write-read'] = '[open open]'
G.add_edge('sec-ril','platformappdomain')
G.edge['sec-ril']['platformappdomain']['write-read'] = '[open open]'
G.add_edge('sec-ril','radio')
G.edge['sec-ril']['radio']['write-read'] = '[open open]'
G.add_edge('sec-ril','rild')
G.edge['sec-ril']['rild']['write-read'] = '[write read][append read][open open]'
G.add_edge('sec-ril','sec-ril')
G.edge['sec-ril']['sec-ril']['write-read'] = '[open open]'
G.add_edge('sec-ril','sem')
G.edge['sec-ril']['sem']['write-read'] = '[open open]'
G.add_edge('sec-ril','s_system_app')
G.edge['sec-ril']['s_system_app']['write-read'] = '[write read][open open]'
G.add_edge('sec-ril','system_app')
G.edge['sec-ril']['system_app']['write-read'] = '[write read][open open]'
G.add_edge('sec-ril','system_server')
G.edge['sec-ril']['system_server']['write-read'] = '[write read][append read][open open]'
G.add_edge('sec-ril','at_distributor')
G.edge['sec-ril']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sec-ril','ime_app')
G.edge['sec-ril']['ime_app']['write-read'] = '[write read][open open][setattr getattr]'
G.add_edge('sec-ril','knox_system_app')
G.edge['sec-ril']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sec-ril','mediaserver')
G.edge['sec-ril']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sec-ril','nfc')
G.edge['sec-ril']['nfc']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sec-ril','platformappdomain')
G.edge['sec-ril']['platformappdomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sec-ril','radio')
G.edge['sec-ril']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sec-ril','rild')
G.edge['sec-ril']['rild']['write-read'] = '[write read][append read][open open][setattr getattr]'
G.add_edge('sec-ril','sec-ril')
G.edge['sec-ril']['sec-ril']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sec-ril','sem')
G.edge['sec-ril']['sem']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sec-ril','s_system_app')
G.edge['sec-ril']['s_system_app']['write-read'] = '[write read][open open][setattr getattr]'
G.add_edge('sec-ril','system_app')
G.edge['sec-ril']['system_app']['write-read'] = '[write read][open open][setattr getattr]'
G.add_edge('sec-ril','system_server')
G.edge['sec-ril']['system_server']['write-read'] = '[write read][append read][open open][setattr getattr]'
G.add_edge('sec-ril','at_distributor')
G.edge['sec-ril']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sec-ril']['at_distributor']['fill'] = 'red'
G.add_edge('sec-ril','at_distributor')
G.edge['sec-ril']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sec-ril','ime_app')
G.edge['sec-ril']['ime_app']['write-read'] = '[write read][open open][setattr getattr][write read]'
G.edge['sec-ril']['ime_app']['fill'] = 'red'
G.add_edge('sec-ril','ime_app')
G.edge['sec-ril']['ime_app']['write-read'] = '[write read][open open][setattr getattr][write read][append read]'
G.add_edge('sec-ril','knox_system_app')
G.edge['sec-ril']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sec-ril']['knox_system_app']['fill'] = 'red'
G.add_edge('sec-ril','knox_system_app')
G.edge['sec-ril']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sec-ril','mediaserver')
G.edge['sec-ril']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sec-ril']['mediaserver']['fill'] = 'red'
G.add_edge('sec-ril','mediaserver')
G.edge['sec-ril']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sec-ril','nfc')
G.edge['sec-ril']['nfc']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sec-ril']['nfc']['fill'] = 'red'
G.add_edge('sec-ril','nfc')
G.edge['sec-ril']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sec-ril','platformappdomain')
G.edge['sec-ril']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sec-ril']['platformappdomain']['fill'] = 'red'
G.add_edge('sec-ril','platformappdomain')
G.edge['sec-ril']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sec-ril','radio')
G.edge['sec-ril']['radio']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sec-ril']['radio']['fill'] = 'red'
G.add_edge('sec-ril','radio')
G.edge['sec-ril']['radio']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sec-ril','rild')
G.edge['sec-ril']['rild']['write-read'] = '[write read][append read][open open][setattr getattr][write read]'
G.edge['sec-ril']['rild']['fill'] = 'red'
G.add_edge('sec-ril','rild')
G.edge['sec-ril']['rild']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('sec-ril','sec-ril')
G.edge['sec-ril']['sec-ril']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sec-ril']['sec-ril']['fill'] = 'red'
G.add_edge('sec-ril','sec-ril')
G.edge['sec-ril']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sec-ril','sem')
G.edge['sec-ril']['sem']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sec-ril']['sem']['fill'] = 'red'
G.add_edge('sec-ril','sem')
G.edge['sec-ril']['sem']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sec-ril','s_system_app')
G.edge['sec-ril']['s_system_app']['write-read'] = '[write read][open open][setattr getattr][write read]'
G.edge['sec-ril']['s_system_app']['fill'] = 'red'
G.add_edge('sec-ril','s_system_app')
G.edge['sec-ril']['s_system_app']['write-read'] = '[write read][open open][setattr getattr][write read][append read]'
G.add_edge('sec-ril','system_app')
G.edge['sec-ril']['system_app']['write-read'] = '[write read][open open][setattr getattr][write read]'
G.edge['sec-ril']['system_app']['fill'] = 'red'
G.add_edge('sec-ril','system_app')
G.edge['sec-ril']['system_app']['write-read'] = '[write read][open open][setattr getattr][write read][append read]'
G.add_edge('sec-ril','system_server')
G.edge['sec-ril']['system_server']['write-read'] = '[write read][append read][open open][setattr getattr][write read]'
G.edge['sec-ril']['system_server']['fill'] = 'red'
G.add_edge('sec-ril','system_server')
G.edge['sec-ril']['system_server']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('sem','at_distributor')
G.edge['sem']['at_distributor']['write-read'] = '[open open]'
G.add_edge('sem','ime_app')
G.edge['sem']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sem','knox_system_app')
G.edge['sem']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('sem','mediaserver')
G.edge['sem']['mediaserver']['write-read'] = '[open open]'
G.add_edge('sem','nfc')
G.edge['sem']['nfc']['write-read'] = '[open open]'
G.add_edge('sem','platformappdomain')
G.edge['sem']['platformappdomain']['write-read'] = '[open open]'
G.add_edge('sem','radio')
G.edge['sem']['radio']['write-read'] = '[open open]'
G.add_edge('sem','rild')
G.edge['sem']['rild']['write-read'] = '[open open]'
G.add_edge('sem','sec-ril')
G.edge['sem']['sec-ril']['write-read'] = '[open open]'
G.add_edge('sem','sem')
G.edge['sem']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sem','s_system_app')
G.edge['sem']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sem','system_app')
G.edge['sem']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sem','system_server')
G.edge['sem']['system_server']['write-read'] = '[open open]'
G.add_edge('sem','at_distributor')
G.edge['sem']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sem','ime_app')
G.edge['sem']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('sem','knox_system_app')
G.edge['sem']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sem','mediaserver')
G.edge['sem']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sem','nfc')
G.edge['sem']['nfc']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sem','platformappdomain')
G.edge['sem']['platformappdomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sem','radio')
G.edge['sem']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sem','rild')
G.edge['sem']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sem','sec-ril')
G.edge['sem']['sec-ril']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sem','sem')
G.edge['sem']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('sem','s_system_app')
G.edge['sem']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('sem','system_app')
G.edge['sem']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('sem','system_server')
G.edge['sem']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sem','at_distributor')
G.edge['sem']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sem']['at_distributor']['fill'] = 'red'
G.add_edge('sem','at_distributor')
G.edge['sem']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sem','ime_app')
G.edge['sem']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['sem']['ime_app']['fill'] = 'red'
G.add_edge('sem','ime_app')
G.edge['sem']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('sem','knox_system_app')
G.edge['sem']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sem']['knox_system_app']['fill'] = 'red'
G.add_edge('sem','knox_system_app')
G.edge['sem']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sem','mediaserver')
G.edge['sem']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sem']['mediaserver']['fill'] = 'red'
G.add_edge('sem','mediaserver')
G.edge['sem']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sem','nfc')
G.edge['sem']['nfc']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sem']['nfc']['fill'] = 'red'
G.add_edge('sem','nfc')
G.edge['sem']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sem','platformappdomain')
G.edge['sem']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sem']['platformappdomain']['fill'] = 'red'
G.add_edge('sem','platformappdomain')
G.edge['sem']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sem','radio')
G.edge['sem']['radio']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sem']['radio']['fill'] = 'red'
G.add_edge('sem','radio')
G.edge['sem']['radio']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sem','rild')
G.edge['sem']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sem']['rild']['fill'] = 'red'
G.add_edge('sem','rild')
G.edge['sem']['rild']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sem','sec-ril')
G.edge['sem']['sec-ril']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sem']['sec-ril']['fill'] = 'red'
G.add_edge('sem','sec-ril')
G.edge['sem']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sem','sem')
G.edge['sem']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['sem']['sem']['fill'] = 'red'
G.add_edge('sem','sem')
G.edge['sem']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('sem','s_system_app')
G.edge['sem']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['sem']['s_system_app']['fill'] = 'red'
G.add_edge('sem','s_system_app')
G.edge['sem']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('sem','system_app')
G.edge['sem']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['sem']['system_app']['fill'] = 'red'
G.add_edge('sem','system_app')
G.edge['sem']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('sem','system_server')
G.edge['sem']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sem']['system_server']['fill'] = 'red'
G.add_edge('sem','system_server')
G.edge['sem']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','at_distributor')
G.edge['s_system_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','knox_system_app')
G.edge['s_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','mediaserver')
G.edge['s_system_app']['mediaserver']['write-read'] = '[open open]'
G.add_edge('s_system_app','nfc')
G.edge['s_system_app']['nfc']['write-read'] = '[open open]'
G.add_edge('s_system_app','platformappdomain')
G.edge['s_system_app']['platformappdomain']['write-read'] = '[open open]'
G.add_edge('s_system_app','radio')
G.edge['s_system_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('s_system_app','rild')
G.edge['s_system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open]'
G.add_edge('s_system_app','sec-ril')
G.edge['s_system_app']['sec-ril']['write-read'] = '[open open]'
G.add_edge('s_system_app','sem')
G.edge['s_system_app']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','at_distributor')
G.edge['s_system_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','knox_system_app')
G.edge['s_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','mediaserver')
G.edge['s_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','nfc')
G.edge['s_system_app']['nfc']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','platformappdomain')
G.edge['s_system_app']['platformappdomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','radio')
G.edge['s_system_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','rild')
G.edge['s_system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','sec-ril')
G.edge['s_system_app']['sec-ril']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','sem')
G.edge['s_system_app']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','at_distributor')
G.edge['s_system_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['at_distributor']['fill'] = 'red'
G.add_edge('s_system_app','at_distributor')
G.edge['s_system_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['ime_app']['fill'] = 'red'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','knox_system_app')
G.edge['s_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['knox_system_app']['fill'] = 'red'
G.add_edge('s_system_app','knox_system_app')
G.edge['s_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','mediaserver')
G.edge['s_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['mediaserver']['fill'] = 'red'
G.add_edge('s_system_app','mediaserver')
G.edge['s_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','nfc')
G.edge['s_system_app']['nfc']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['nfc']['fill'] = 'red'
G.add_edge('s_system_app','nfc')
G.edge['s_system_app']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','platformappdomain')
G.edge['s_system_app']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['platformappdomain']['fill'] = 'red'
G.add_edge('s_system_app','platformappdomain')
G.edge['s_system_app']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','radio')
G.edge['s_system_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['radio']['fill'] = 'red'
G.add_edge('s_system_app','radio')
G.edge['s_system_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','rild')
G.edge['s_system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['rild']['fill'] = 'red'
G.add_edge('s_system_app','rild')
G.edge['s_system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','sec-ril')
G.edge['s_system_app']['sec-ril']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['sec-ril']['fill'] = 'red'
G.add_edge('s_system_app','sec-ril')
G.edge['s_system_app']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','sem')
G.edge['s_system_app']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['sem']['fill'] = 'red'
G.add_edge('s_system_app','sem')
G.edge['s_system_app']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['system_app']['fill'] = 'red'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['system_server']['fill'] = 'red'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','at_distributor')
G.edge['system_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','knox_system_app')
G.edge['system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','mediaserver')
G.edge['system_app']['mediaserver']['write-read'] = '[open open]'
G.add_edge('system_app','nfc')
G.edge['system_app']['nfc']['write-read'] = '[open open]'
G.add_edge('system_app','platformappdomain')
G.edge['system_app']['platformappdomain']['write-read'] = '[open open]'
G.add_edge('system_app','radio')
G.edge['system_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_app','rild')
G.edge['system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open]'
G.add_edge('system_app','sec-ril')
G.edge['system_app']['sec-ril']['write-read'] = '[open open]'
G.add_edge('system_app','sem')
G.edge['system_app']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','at_distributor')
G.edge['system_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','knox_system_app')
G.edge['system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','mediaserver')
G.edge['system_app']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','nfc')
G.edge['system_app']['nfc']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','platformappdomain')
G.edge['system_app']['platformappdomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','radio')
G.edge['system_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','rild')
G.edge['system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','sec-ril')
G.edge['system_app']['sec-ril']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','sem')
G.edge['system_app']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','at_distributor')
G.edge['system_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_app']['at_distributor']['fill'] = 'red'
G.add_edge('system_app','at_distributor')
G.edge['system_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['ime_app']['fill'] = 'red'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','knox_system_app')
G.edge['system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['knox_system_app']['fill'] = 'red'
G.add_edge('system_app','knox_system_app')
G.edge['system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','mediaserver')
G.edge['system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['mediaserver']['fill'] = 'red'
G.add_edge('system_app','mediaserver')
G.edge['system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_app','nfc')
G.edge['system_app']['nfc']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['nfc']['fill'] = 'red'
G.add_edge('system_app','nfc')
G.edge['system_app']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_app','platformappdomain')
G.edge['system_app']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['platformappdomain']['fill'] = 'red'
G.add_edge('system_app','platformappdomain')
G.edge['system_app']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_app','radio')
G.edge['system_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['radio']['fill'] = 'red'
G.add_edge('system_app','radio')
G.edge['system_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','rild')
G.edge['system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['rild']['fill'] = 'red'
G.add_edge('system_app','rild')
G.edge['system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','sec-ril')
G.edge['system_app']['sec-ril']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['sec-ril']['fill'] = 'red'
G.add_edge('system_app','sec-ril')
G.edge['system_app']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_app','sem')
G.edge['system_app']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_app']['sem']['fill'] = 'red'
G.add_edge('system_app','sem')
G.edge['system_app']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['s_system_app']['fill'] = 'red'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['system_app']['fill'] = 'red'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['system_server']['fill'] = 'red'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','at_distributor')
G.edge['system_server']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open]'
G.add_edge('system_server','knox_system_app')
G.edge['system_server']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','nfc')
G.edge['system_server']['nfc']['write-read'] = '[open open]'
G.add_edge('system_server','platformappdomain')
G.edge['system_server']['platformappdomain']['write-read'] = '[open open]'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('system_server','sec-ril')
G.edge['system_server']['sec-ril']['write-read'] = '[open open]'
G.add_edge('system_server','sem')
G.edge['system_server']['sem']['write-read'] = '[open open]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','at_distributor')
G.edge['system_server']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr]'
G.add_edge('system_server','knox_system_app')
G.edge['system_server']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','nfc')
G.edge['system_server']['nfc']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','platformappdomain')
G.edge['system_server']['platformappdomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('system_server','sec-ril')
G.edge['system_server']['sec-ril']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','sem')
G.edge['system_server']['sem']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','at_distributor')
G.edge['system_server']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['at_distributor']['fill'] = 'red'
G.add_edge('system_server','at_distributor')
G.edge['system_server']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read]'
G.edge['system_server']['ime_app']['fill'] = 'red'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','knox_system_app')
G.edge['system_server']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['knox_system_app']['fill'] = 'red'
G.add_edge('system_server','knox_system_app')
G.edge['system_server']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['mediaserver']['fill'] = 'red'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','nfc')
G.edge['system_server']['nfc']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['nfc']['fill'] = 'red'
G.add_edge('system_server','nfc')
G.edge['system_server']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_server','platformappdomain')
G.edge['system_server']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['platformappdomain']['fill'] = 'red'
G.add_edge('system_server','platformappdomain')
G.edge['system_server']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['radio']['fill'] = 'red'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['system_server']['rild']['fill'] = 'red'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','sec-ril')
G.edge['system_server']['sec-ril']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['sec-ril']['fill'] = 'red'
G.add_edge('system_server','sec-ril')
G.edge['system_server']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_server','sem')
G.edge['system_server']['sem']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['sem']['fill'] = 'red'
G.add_edge('system_server','sem')
G.edge['system_server']['sem']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['s_system_app']['fill'] = 'red'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['system_app']['fill'] = 'red'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()