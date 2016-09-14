import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open]'
G.add_edge('domain','qrngd')
G.edge['domain']['qrngd']['write-read'] = '[open open]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][write read]'
G.edge['domain']['domain']['fill'] = 'red'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][write read][append read]'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][write read][append read][write read]'
G.edge['domain']['domain']['fill'] = 'red'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][write read][append read][write read][append read]'
G.add_edge('domain','qrngd')
G.edge['domain']['qrngd']['write-read'] = '[open open][write read]'
G.edge['domain']['qrngd']['fill'] = 'red'
G.add_edge('domain','qrngd')
G.edge['domain']['qrngd']['write-read'] = '[open open][write read][append read]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read]'
G.edge['domain']['system_server']['fill'] = 'red'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read]'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open]'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open]'
G.add_edge('domain','qrngd')
G.edge['domain']['qrngd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open]'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read]'
G.edge['domain']['domain']['fill'] = 'red'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read]'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read]'
G.edge['domain']['domain']['fill'] = 'red'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read]'
G.add_edge('domain','qrngd')
G.edge['domain']['qrngd']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['domain']['qrngd']['fill'] = 'red'
G.add_edge('domain','qrngd')
G.edge['domain']['qrngd']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read]'
G.edge['domain']['system_server']['fill'] = 'red'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('netd','domain')
G.edge['netd']['domain']['write-read'] = '[write read][open open]'
G.add_edge('netd','domain')
G.edge['netd']['domain']['write-read'] = '[write read][open open][open open]'
G.add_edge('netd','qrngd')
G.edge['netd']['qrngd']['write-read'] = '[open open]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('netd','domain')
G.edge['netd']['domain']['write-read'] = '[write read][open open][open open][write read]'
G.edge['netd']['domain']['fill'] = 'red'
G.add_edge('netd','domain')
G.edge['netd']['domain']['write-read'] = '[write read][open open][open open][write read][append read]'
G.add_edge('netd','domain')
G.edge['netd']['domain']['write-read'] = '[write read][open open][open open][write read][append read][write read]'
G.edge['netd']['domain']['fill'] = 'red'
G.add_edge('netd','domain')
G.edge['netd']['domain']['write-read'] = '[write read][open open][open open][write read][append read][write read][append read]'
G.add_edge('netd','qrngd')
G.edge['netd']['qrngd']['write-read'] = '[open open][write read]'
G.edge['netd']['qrngd']['fill'] = 'red'
G.add_edge('netd','qrngd')
G.edge['netd']['qrngd']['write-read'] = '[open open][write read][append read]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['netd']['system_server']['fill'] = 'red'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('oneseg_mw','domain')
G.edge['oneseg_mw']['domain']['write-read'] = '[open open]'
G.add_edge('oneseg_mw','domain')
G.edge['oneseg_mw']['domain']['write-read'] = '[open open][open open]'
G.add_edge('oneseg_mw','qrngd')
G.edge['oneseg_mw']['qrngd']['write-read'] = '[open open]'
G.add_edge('oneseg_mw','system_server')
G.edge['oneseg_mw']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('oneseg_mw','domain')
G.edge['oneseg_mw']['domain']['write-read'] = '[open open][open open][write read]'
G.edge['oneseg_mw']['domain']['fill'] = 'red'
G.add_edge('oneseg_mw','domain')
G.edge['oneseg_mw']['domain']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('oneseg_mw','domain')
G.edge['oneseg_mw']['domain']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['oneseg_mw']['domain']['fill'] = 'red'
G.add_edge('oneseg_mw','domain')
G.edge['oneseg_mw']['domain']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('oneseg_mw','qrngd')
G.edge['oneseg_mw']['qrngd']['write-read'] = '[open open][write read]'
G.edge['oneseg_mw']['qrngd']['fill'] = 'red'
G.add_edge('oneseg_mw','qrngd')
G.edge['oneseg_mw']['qrngd']['write-read'] = '[open open][write read][append read]'
G.add_edge('oneseg_mw','system_server')
G.edge['oneseg_mw']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['oneseg_mw']['system_server']['fill'] = 'red'
G.add_edge('oneseg_mw','system_server')
G.edge['oneseg_mw']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('p2p_supplicant','domain')
G.edge['p2p_supplicant']['domain']['write-read'] = '[open open]'
G.add_edge('p2p_supplicant','domain')
G.edge['p2p_supplicant']['domain']['write-read'] = '[open open][open open]'
G.add_edge('p2p_supplicant','qrngd')
G.edge['p2p_supplicant']['qrngd']['write-read'] = '[open open]'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('p2p_supplicant','domain')
G.edge['p2p_supplicant']['domain']['write-read'] = '[open open][open open][write read]'
G.edge['p2p_supplicant']['domain']['fill'] = 'red'
G.add_edge('p2p_supplicant','domain')
G.edge['p2p_supplicant']['domain']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('p2p_supplicant','domain')
G.edge['p2p_supplicant']['domain']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['p2p_supplicant']['domain']['fill'] = 'red'
G.add_edge('p2p_supplicant','domain')
G.edge['p2p_supplicant']['domain']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('p2p_supplicant','qrngd')
G.edge['p2p_supplicant']['qrngd']['write-read'] = '[open open][write read]'
G.edge['p2p_supplicant']['qrngd']['fill'] = 'red'
G.add_edge('p2p_supplicant','qrngd')
G.edge['p2p_supplicant']['qrngd']['write-read'] = '[open open][write read][append read]'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['p2p_supplicant']['system_server']['fill'] = 'red'
G.add_edge('p2p_supplicant','system_server')
G.edge['p2p_supplicant']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qrngd','domain')
G.edge['qrngd']['domain']['write-read'] = '[open open]'
G.add_edge('qrngd','domain')
G.edge['qrngd']['domain']['write-read'] = '[open open][open open]'
G.add_edge('qrngd','qrngd')
G.edge['qrngd']['qrngd']['write-read'] = '[open open]'
G.add_edge('qrngd','system_server')
G.edge['qrngd']['system_server']['write-read'] = '[open open]'
G.add_edge('qrngd','domain')
G.edge['qrngd']['domain']['write-read'] = '[open open][open open][write read]'
G.edge['qrngd']['domain']['fill'] = 'red'
G.add_edge('qrngd','domain')
G.edge['qrngd']['domain']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('qrngd','domain')
G.edge['qrngd']['domain']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['qrngd']['domain']['fill'] = 'red'
G.add_edge('qrngd','domain')
G.edge['qrngd']['domain']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('qrngd','qrngd')
G.edge['qrngd']['qrngd']['write-read'] = '[open open][write read]'
G.edge['qrngd']['qrngd']['fill'] = 'red'
G.add_edge('qrngd','qrngd')
G.edge['qrngd']['qrngd']['write-read'] = '[open open][write read][append read]'
G.add_edge('qrngd','system_server')
G.edge['qrngd']['system_server']['write-read'] = '[open open][write read]'
G.edge['qrngd']['system_server']['fill'] = 'red'
G.add_edge('qrngd','system_server')
G.edge['qrngd']['system_server']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','domain')
G.edge['system_server']['domain']['write-read'] = '[write read][open open][write read][append read][write read][append read][open open]'
G.add_edge('system_server','domain')
G.edge['system_server']['domain']['write-read'] = '[write read][open open][write read][append read][write read][append read][open open][open open]'
G.add_edge('system_server','qrngd')
G.edge['system_server']['qrngd']['write-read'] = '[open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','domain')
G.edge['system_server']['domain']['write-read'] = '[write read][open open][write read][append read][write read][append read][open open][open open][write read]'
G.edge['system_server']['domain']['fill'] = 'red'
G.add_edge('system_server','domain')
G.edge['system_server']['domain']['write-read'] = '[write read][open open][write read][append read][write read][append read][open open][open open][write read][append read]'
G.add_edge('system_server','domain')
G.edge['system_server']['domain']['write-read'] = '[write read][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read]'
G.edge['system_server']['domain']['fill'] = 'red'
G.add_edge('system_server','domain')
G.edge['system_server']['domain']['write-read'] = '[write read][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read]'
G.add_edge('system_server','qrngd')
G.edge['system_server']['qrngd']['write-read'] = '[open open][write read]'
G.edge['system_server']['qrngd']['fill'] = 'red'
G.add_edge('system_server','qrngd')
G.edge['system_server']['qrngd']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('vold','domain')
G.edge['vold']['domain']['write-read'] = '[open open]'
G.add_edge('vold','domain')
G.edge['vold']['domain']['write-read'] = '[open open][open open]'
G.add_edge('vold','qrngd')
G.edge['vold']['qrngd']['write-read'] = '[open open]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vold','domain')
G.edge['vold']['domain']['write-read'] = '[open open][open open][write read]'
G.edge['vold']['domain']['fill'] = 'red'
G.add_edge('vold','domain')
G.edge['vold']['domain']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('vold','domain')
G.edge['vold']['domain']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['vold']['domain']['fill'] = 'red'
G.add_edge('vold','domain')
G.edge['vold']['domain']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('vold','qrngd')
G.edge['vold']['qrngd']['write-read'] = '[open open][write read]'
G.edge['vold']['qrngd']['fill'] = 'red'
G.add_edge('vold','qrngd')
G.edge['vold']['qrngd']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['vold']['system_server']['fill'] = 'red'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()