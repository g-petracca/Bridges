import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('bridged_platform_app','bridged_platform_app')
G.edge['bridged_platform_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('bridged_platform_app','lmkd')
G.edge['bridged_platform_app']['lmkd']['write-read'] = '[open open]'
G.add_edge('bridged_platform_app','system')
G.edge['bridged_platform_app']['system']['write-read'] = '[open open]'
G.add_edge('bridged_platform_app','system_app')
G.edge['bridged_platform_app']['system_app']['write-read'] = '[open open]'
G.add_edge('bridged_platform_app','s_system_app')
G.edge['bridged_platform_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('bridged_platform_app','bridged_platform_app')
G.edge['bridged_platform_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['bridged_platform_app']['bridged_platform_app']['fill'] = 'red'
G.add_edge('bridged_platform_app','bridged_platform_app')
G.edge['bridged_platform_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('bridged_platform_app','lmkd')
G.edge['bridged_platform_app']['lmkd']['write-read'] = '[open open][write read]'
G.edge['bridged_platform_app']['lmkd']['fill'] = 'red'
G.add_edge('bridged_platform_app','lmkd')
G.edge['bridged_platform_app']['lmkd']['write-read'] = '[open open][write read][append read]'
G.add_edge('bridged_platform_app','system')
G.edge['bridged_platform_app']['system']['write-read'] = '[open open][write read]'
G.edge['bridged_platform_app']['system']['fill'] = 'red'
G.add_edge('bridged_platform_app','system')
G.edge['bridged_platform_app']['system']['write-read'] = '[open open][write read][append read]'
G.add_edge('bridged_platform_app','system_app')
G.edge['bridged_platform_app']['system_app']['write-read'] = '[open open][write read]'
G.edge['bridged_platform_app']['system_app']['fill'] = 'red'
G.add_edge('bridged_platform_app','system_app')
G.edge['bridged_platform_app']['system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('bridged_platform_app','s_system_app')
G.edge['bridged_platform_app']['s_system_app']['write-read'] = '[open open][write read]'
G.edge['bridged_platform_app']['s_system_app']['fill'] = 'red'
G.add_edge('bridged_platform_app','s_system_app')
G.edge['bridged_platform_app']['s_system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('lmkd','bridged_platform_app')
G.edge['lmkd']['bridged_platform_app']['write-read'] = '[open open]'
G.add_edge('lmkd','lmkd')
G.edge['lmkd']['lmkd']['write-read'] = '[open open]'
G.add_edge('lmkd','system')
G.edge['lmkd']['system']['write-read'] = '[open open]'
G.add_edge('lmkd','system_app')
G.edge['lmkd']['system_app']['write-read'] = '[open open]'
G.add_edge('lmkd','s_system_app')
G.edge['lmkd']['s_system_app']['write-read'] = '[open open]'
G.add_edge('lmkd','bridged_platform_app')
G.edge['lmkd']['bridged_platform_app']['write-read'] = '[open open][write read]'
G.edge['lmkd']['bridged_platform_app']['fill'] = 'red'
G.add_edge('lmkd','bridged_platform_app')
G.edge['lmkd']['bridged_platform_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('lmkd','lmkd')
G.edge['lmkd']['lmkd']['write-read'] = '[open open][write read]'
G.edge['lmkd']['lmkd']['fill'] = 'red'
G.add_edge('lmkd','lmkd')
G.edge['lmkd']['lmkd']['write-read'] = '[open open][write read][append read]'
G.add_edge('lmkd','system')
G.edge['lmkd']['system']['write-read'] = '[open open][write read]'
G.edge['lmkd']['system']['fill'] = 'red'
G.add_edge('lmkd','system')
G.edge['lmkd']['system']['write-read'] = '[open open][write read][append read]'
G.add_edge('lmkd','system_app')
G.edge['lmkd']['system_app']['write-read'] = '[open open][write read]'
G.edge['lmkd']['system_app']['fill'] = 'red'
G.add_edge('lmkd','system_app')
G.edge['lmkd']['system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('lmkd','s_system_app')
G.edge['lmkd']['s_system_app']['write-read'] = '[open open][write read]'
G.edge['lmkd']['s_system_app']['fill'] = 'red'
G.add_edge('lmkd','s_system_app')
G.edge['lmkd']['s_system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('servicemanager','bridged_platform_app')
G.edge['servicemanager']['bridged_platform_app']['write-read'] = '[open open]'
G.add_edge('servicemanager','lmkd')
G.edge['servicemanager']['lmkd']['write-read'] = '[open open]'
G.add_edge('servicemanager','system')
G.edge['servicemanager']['system']['write-read'] = '[open open]'
G.add_edge('servicemanager','system_app')
G.edge['servicemanager']['system_app']['write-read'] = '[open open]'
G.add_edge('servicemanager','s_system_app')
G.edge['servicemanager']['s_system_app']['write-read'] = '[open open]'
G.add_edge('servicemanager','bridged_platform_app')
G.edge['servicemanager']['bridged_platform_app']['write-read'] = '[open open][write read]'
G.edge['servicemanager']['bridged_platform_app']['fill'] = 'red'
G.add_edge('servicemanager','bridged_platform_app')
G.edge['servicemanager']['bridged_platform_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('servicemanager','lmkd')
G.edge['servicemanager']['lmkd']['write-read'] = '[open open][write read]'
G.edge['servicemanager']['lmkd']['fill'] = 'red'
G.add_edge('servicemanager','lmkd')
G.edge['servicemanager']['lmkd']['write-read'] = '[open open][write read][append read]'
G.add_edge('servicemanager','system')
G.edge['servicemanager']['system']['write-read'] = '[open open][write read]'
G.edge['servicemanager']['system']['fill'] = 'red'
G.add_edge('servicemanager','system')
G.edge['servicemanager']['system']['write-read'] = '[open open][write read][append read]'
G.add_edge('servicemanager','system_app')
G.edge['servicemanager']['system_app']['write-read'] = '[open open][write read]'
G.edge['servicemanager']['system_app']['fill'] = 'red'
G.add_edge('servicemanager','system_app')
G.edge['servicemanager']['system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('servicemanager','s_system_app')
G.edge['servicemanager']['s_system_app']['write-read'] = '[open open][write read]'
G.edge['servicemanager']['s_system_app']['fill'] = 'red'
G.add_edge('servicemanager','s_system_app')
G.edge['servicemanager']['s_system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('system','bridged_platform_app')
G.edge['system']['bridged_platform_app']['write-read'] = '[open open]'
G.add_edge('system','lmkd')
G.edge['system']['lmkd']['write-read'] = '[open open]'
G.add_edge('system','system')
G.edge['system']['system']['write-read'] = '[open open]'
G.add_edge('system','system_app')
G.edge['system']['system_app']['write-read'] = '[open open]'
G.add_edge('system','s_system_app')
G.edge['system']['s_system_app']['write-read'] = '[open open]'
G.add_edge('system','bridged_platform_app')
G.edge['system']['bridged_platform_app']['write-read'] = '[open open][write read]'
G.edge['system']['bridged_platform_app']['fill'] = 'red'
G.add_edge('system','bridged_platform_app')
G.edge['system']['bridged_platform_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('system','lmkd')
G.edge['system']['lmkd']['write-read'] = '[open open][write read]'
G.edge['system']['lmkd']['fill'] = 'red'
G.add_edge('system','lmkd')
G.edge['system']['lmkd']['write-read'] = '[open open][write read][append read]'
G.add_edge('system','system')
G.edge['system']['system']['write-read'] = '[open open][write read]'
G.edge['system']['system']['fill'] = 'red'
G.add_edge('system','system')
G.edge['system']['system']['write-read'] = '[open open][write read][append read]'
G.add_edge('system','system_app')
G.edge['system']['system_app']['write-read'] = '[open open][write read]'
G.edge['system']['system_app']['fill'] = 'red'
G.add_edge('system','system_app')
G.edge['system']['system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('system','s_system_app')
G.edge['system']['s_system_app']['write-read'] = '[open open][write read]'
G.edge['system']['s_system_app']['fill'] = 'red'
G.add_edge('system','s_system_app')
G.edge['system']['s_system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_app','bridged_platform_app')
G.edge['system_app']['bridged_platform_app']['write-read'] = '[open open]'
G.add_edge('system_app','lmkd')
G.edge['system_app']['lmkd']['write-read'] = '[remove_name search][open open]'
G.add_edge('system_app','system')
G.edge['system_app']['system']['write-read'] = '[open open]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','bridged_platform_app')
G.edge['system_app']['bridged_platform_app']['write-read'] = '[open open][write read]'
G.edge['system_app']['bridged_platform_app']['fill'] = 'red'
G.add_edge('system_app','bridged_platform_app')
G.edge['system_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_app','lmkd')
G.edge['system_app']['lmkd']['write-read'] = '[remove_name search][open open][write read]'
G.edge['system_app']['lmkd']['fill'] = 'red'
G.add_edge('system_app','lmkd')
G.edge['system_app']['lmkd']['write-read'] = '[remove_name search][open open][write read][append read]'
G.add_edge('system_app','system')
G.edge['system_app']['system']['write-read'] = '[open open][write read]'
G.edge['system_app']['system']['fill'] = 'red'
G.add_edge('system_app','system')
G.edge['system_app']['system']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_app']['system_app']['fill'] = 'red'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_app']['s_system_app']['fill'] = 'red'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('s_system_app','bridged_platform_app')
G.edge['s_system_app']['bridged_platform_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','lmkd')
G.edge['s_system_app']['lmkd']['write-read'] = '[remove_name search][open open]'
G.add_edge('s_system_app','system')
G.edge['s_system_app']['system']['write-read'] = '[open open]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','bridged_platform_app')
G.edge['s_system_app']['bridged_platform_app']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['bridged_platform_app']['fill'] = 'red'
G.add_edge('s_system_app','bridged_platform_app')
G.edge['s_system_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','lmkd')
G.edge['s_system_app']['lmkd']['write-read'] = '[remove_name search][open open][write read]'
G.edge['s_system_app']['lmkd']['fill'] = 'red'
G.add_edge('s_system_app','lmkd')
G.edge['s_system_app']['lmkd']['write-read'] = '[remove_name search][open open][write read][append read]'
G.add_edge('s_system_app','system')
G.edge['s_system_app']['system']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['system']['fill'] = 'red'
G.add_edge('s_system_app','system')
G.edge['s_system_app']['system']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['s_system_app']['system_app']['fill'] = 'red'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['s_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
app = Viewer(G)
app.mainloop()