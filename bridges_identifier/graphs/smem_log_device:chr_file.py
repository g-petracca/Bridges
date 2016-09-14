import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][append read][setopt getopt][setattr getattr][write read][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][setattr getattr][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][write read][setopt getopt][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('cnd','dpmd')
G.edge['cnd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][write read][setopt getopt][write read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('cnd','netmgrd')
G.edge['cnd']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('cnd','qcomsysd')
G.edge['cnd']['qcomsysd']['write-read'] = '[open open]'
G.add_edge('cnd','qlogd')
G.edge['cnd']['qlogd']['write-read'] = '[write read][add_name search][open open][write read][open open]'
G.add_edge('cnd','qti')
G.edge['cnd']['qti']['write-read'] = '[write read][setattr getattr][write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('cnd','rfs_access')
G.edge['cnd']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('cnd','rmt_storage')
G.edge['cnd']['rmt_storage']['write-read'] = '[setattr getattr][write read][append read][write read][setopt getopt][setopt getopt][open open]'
G.add_edge('cnd','sensors')
G.edge['cnd']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('cnd','thermal-engine')
G.edge['cnd']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('cnd','time_daemon')
G.edge['cnd']['time_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('cnd','wcnss_service')
G.edge['cnd']['wcnss_service']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('cnd','wpa')
G.edge['cnd']['wpa']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][nlmsg_write nlmsg_read][open open]'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][append read][setopt getopt][setattr getattr][write read][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][setattr getattr][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][write read][setopt getopt][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['cnd']['cnd']['fill'] = 'red'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][append read][setopt getopt][setattr getattr][write read][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][setattr getattr][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][write read][setopt getopt][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('cnd','dpmd')
G.edge['cnd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][write read][setopt getopt][write read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['cnd']['dpmd']['fill'] = 'red'
G.add_edge('cnd','dpmd')
G.edge['cnd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][write read][setopt getopt][write read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('cnd','netmgrd')
G.edge['cnd']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['cnd']['netmgrd']['fill'] = 'red'
G.add_edge('cnd','netmgrd')
G.edge['cnd']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('cnd','qcomsysd')
G.edge['cnd']['qcomsysd']['write-read'] = '[open open][write read]'
G.edge['cnd']['qcomsysd']['fill'] = 'red'
G.add_edge('cnd','qlogd')
G.edge['cnd']['qlogd']['write-read'] = '[write read][add_name search][open open][write read][open open][write read]'
G.edge['cnd']['qlogd']['fill'] = 'red'
G.add_edge('cnd','qlogd')
G.edge['cnd']['qlogd']['write-read'] = '[write read][add_name search][open open][write read][open open][write read][append read]'
G.add_edge('cnd','qti')
G.edge['cnd']['qti']['write-read'] = '[write read][setattr getattr][write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['cnd']['qti']['fill'] = 'red'
G.add_edge('cnd','qti')
G.edge['cnd']['qti']['write-read'] = '[write read][setattr getattr][write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('cnd','rfs_access')
G.edge['cnd']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['cnd']['rfs_access']['fill'] = 'red'
G.add_edge('cnd','rfs_access')
G.edge['cnd']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('cnd','rmt_storage')
G.edge['cnd']['rmt_storage']['write-read'] = '[setattr getattr][write read][append read][write read][setopt getopt][setopt getopt][open open][write read]'
G.edge['cnd']['rmt_storage']['fill'] = 'red'
G.add_edge('cnd','rmt_storage')
G.edge['cnd']['rmt_storage']['write-read'] = '[setattr getattr][write read][append read][write read][setopt getopt][setopt getopt][open open][write read][append read]'
G.add_edge('cnd','sensors')
G.edge['cnd']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['cnd']['sensors']['fill'] = 'red'
G.add_edge('cnd','sensors')
G.edge['cnd']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('cnd','thermal-engine')
G.edge['cnd']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['cnd']['thermal-engine']['fill'] = 'red'
G.add_edge('cnd','thermal-engine')
G.edge['cnd']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('cnd','time_daemon')
G.edge['cnd']['time_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][open open][write read]'
G.edge['cnd']['time_daemon']['fill'] = 'red'
G.add_edge('cnd','time_daemon')
G.edge['cnd']['time_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][open open][write read][append read]'
G.add_edge('cnd','wcnss_service')
G.edge['cnd']['wcnss_service']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['cnd']['wcnss_service']['fill'] = 'red'
G.add_edge('cnd','wcnss_service')
G.edge['cnd']['wcnss_service']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('cnd','wpa')
G.edge['cnd']['wpa']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][nlmsg_write nlmsg_read][open open][write read]'
G.edge['cnd']['wpa']['fill'] = 'red'
G.add_edge('cnd','wpa')
G.edge['cnd']['wpa']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][nlmsg_write nlmsg_read][open open][write read][append read]'
G.add_edge('dpmd','cnd')
G.edge['dpmd']['cnd']['write-read'] = '[open open][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dpmd','dpmd')
G.edge['dpmd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dpmd','netmgrd')
G.edge['dpmd']['netmgrd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dpmd','qcomsysd')
G.edge['dpmd']['qcomsysd']['write-read'] = '[open open]'
G.add_edge('dpmd','qlogd')
G.edge['dpmd']['qlogd']['write-read'] = '[open open][append read][open open]'
G.add_edge('dpmd','qti')
G.edge['dpmd']['qti']['write-read'] = '[write read][setattr getattr][write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dpmd','rfs_access')
G.edge['dpmd']['rfs_access']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('dpmd','rmt_storage')
G.edge['dpmd']['rmt_storage']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][write read][setopt getopt][setopt getopt][open open]'
G.add_edge('dpmd','sensors')
G.edge['dpmd']['sensors']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('dpmd','thermal-engine')
G.edge['dpmd']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dpmd','time_daemon')
G.edge['dpmd']['time_daemon']['write-read'] = '[write read][open open]'
G.add_edge('dpmd','wcnss_service')
G.edge['dpmd']['wcnss_service']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dpmd','wpa')
G.edge['dpmd']['wpa']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dpmd','cnd')
G.edge['dpmd']['cnd']['write-read'] = '[open open][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['dpmd']['cnd']['fill'] = 'red'
G.add_edge('dpmd','cnd')
G.edge['dpmd']['cnd']['write-read'] = '[open open][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('dpmd','dpmd')
G.edge['dpmd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['dpmd']['dpmd']['fill'] = 'red'
G.add_edge('dpmd','dpmd')
G.edge['dpmd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('dpmd','netmgrd')
G.edge['dpmd']['netmgrd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['dpmd']['netmgrd']['fill'] = 'red'
G.add_edge('dpmd','netmgrd')
G.edge['dpmd']['netmgrd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('dpmd','qcomsysd')
G.edge['dpmd']['qcomsysd']['write-read'] = '[open open][write read]'
G.edge['dpmd']['qcomsysd']['fill'] = 'red'
G.add_edge('dpmd','qlogd')
G.edge['dpmd']['qlogd']['write-read'] = '[open open][append read][open open][write read]'
G.edge['dpmd']['qlogd']['fill'] = 'red'
G.add_edge('dpmd','qlogd')
G.edge['dpmd']['qlogd']['write-read'] = '[open open][append read][open open][write read][append read]'
G.add_edge('dpmd','qti')
G.edge['dpmd']['qti']['write-read'] = '[write read][setattr getattr][write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['dpmd']['qti']['fill'] = 'red'
G.add_edge('dpmd','qti')
G.edge['dpmd']['qti']['write-read'] = '[write read][setattr getattr][write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('dpmd','rfs_access')
G.edge['dpmd']['rfs_access']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['dpmd']['rfs_access']['fill'] = 'red'
G.add_edge('dpmd','rfs_access')
G.edge['dpmd']['rfs_access']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('dpmd','rmt_storage')
G.edge['dpmd']['rmt_storage']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][write read][setopt getopt][setopt getopt][open open][write read]'
G.edge['dpmd']['rmt_storage']['fill'] = 'red'
G.add_edge('dpmd','rmt_storage')
G.edge['dpmd']['rmt_storage']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][write read][setopt getopt][setopt getopt][open open][write read][append read]'
G.add_edge('dpmd','sensors')
G.edge['dpmd']['sensors']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['dpmd']['sensors']['fill'] = 'red'
G.add_edge('dpmd','sensors')
G.edge['dpmd']['sensors']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('dpmd','thermal-engine')
G.edge['dpmd']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['dpmd']['thermal-engine']['fill'] = 'red'
G.add_edge('dpmd','thermal-engine')
G.edge['dpmd']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('dpmd','time_daemon')
G.edge['dpmd']['time_daemon']['write-read'] = '[write read][open open][write read]'
G.edge['dpmd']['time_daemon']['fill'] = 'red'
G.add_edge('dpmd','time_daemon')
G.edge['dpmd']['time_daemon']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('dpmd','wcnss_service')
G.edge['dpmd']['wcnss_service']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['dpmd']['wcnss_service']['fill'] = 'red'
G.add_edge('dpmd','wcnss_service')
G.edge['dpmd']['wcnss_service']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('dpmd','wpa')
G.edge['dpmd']['wpa']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['dpmd']['wpa']['fill'] = 'red'
G.add_edge('dpmd','wpa')
G.edge['dpmd']['wpa']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('netmgrd','cnd')
G.edge['netmgrd']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netmgrd','dpmd')
G.edge['netmgrd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netmgrd','netmgrd')
G.edge['netmgrd']['netmgrd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read][nlmsg_write nlmsg_read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('netmgrd','qcomsysd')
G.edge['netmgrd']['qcomsysd']['write-read'] = '[open open]'
G.add_edge('netmgrd','qlogd')
G.edge['netmgrd']['qlogd']['write-read'] = '[write read][add_name search][write read][add_name search][open open][write read][open open]'
G.add_edge('netmgrd','qti')
G.edge['netmgrd']['qti']['write-read'] = '[setattr getattr][write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netmgrd','rfs_access')
G.edge['netmgrd']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('netmgrd','rmt_storage')
G.edge['netmgrd']['rmt_storage']['write-read'] = '[setattr getattr][write read][append read][write read][setopt getopt][setopt getopt][open open]'
G.add_edge('netmgrd','sensors')
G.edge['netmgrd']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netmgrd','thermal-engine')
G.edge['netmgrd']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netmgrd','time_daemon')
G.edge['netmgrd']['time_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('netmgrd','wcnss_service')
G.edge['netmgrd']['wcnss_service']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netmgrd','wpa')
G.edge['netmgrd']['wpa']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netmgrd','cnd')
G.edge['netmgrd']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['netmgrd']['cnd']['fill'] = 'red'
G.add_edge('netmgrd','cnd')
G.edge['netmgrd']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('netmgrd','dpmd')
G.edge['netmgrd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['netmgrd']['dpmd']['fill'] = 'red'
G.add_edge('netmgrd','dpmd')
G.edge['netmgrd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('netmgrd','netmgrd')
G.edge['netmgrd']['netmgrd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read][nlmsg_write nlmsg_read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['netmgrd']['netmgrd']['fill'] = 'red'
G.add_edge('netmgrd','netmgrd')
G.edge['netmgrd']['netmgrd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read][nlmsg_write nlmsg_read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('netmgrd','qcomsysd')
G.edge['netmgrd']['qcomsysd']['write-read'] = '[open open][write read]'
G.edge['netmgrd']['qcomsysd']['fill'] = 'red'
G.add_edge('netmgrd','qlogd')
G.edge['netmgrd']['qlogd']['write-read'] = '[write read][add_name search][write read][add_name search][open open][write read][open open][write read]'
G.edge['netmgrd']['qlogd']['fill'] = 'red'
G.add_edge('netmgrd','qlogd')
G.edge['netmgrd']['qlogd']['write-read'] = '[write read][add_name search][write read][add_name search][open open][write read][open open][write read][append read]'
G.add_edge('netmgrd','qti')
G.edge['netmgrd']['qti']['write-read'] = '[setattr getattr][write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['netmgrd']['qti']['fill'] = 'red'
G.add_edge('netmgrd','qti')
G.edge['netmgrd']['qti']['write-read'] = '[setattr getattr][write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('netmgrd','rfs_access')
G.edge['netmgrd']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['netmgrd']['rfs_access']['fill'] = 'red'
G.add_edge('netmgrd','rfs_access')
G.edge['netmgrd']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('netmgrd','rmt_storage')
G.edge['netmgrd']['rmt_storage']['write-read'] = '[setattr getattr][write read][append read][write read][setopt getopt][setopt getopt][open open][write read]'
G.edge['netmgrd']['rmt_storage']['fill'] = 'red'
G.add_edge('netmgrd','rmt_storage')
G.edge['netmgrd']['rmt_storage']['write-read'] = '[setattr getattr][write read][append read][write read][setopt getopt][setopt getopt][open open][write read][append read]'
G.add_edge('netmgrd','sensors')
G.edge['netmgrd']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['netmgrd']['sensors']['fill'] = 'red'
G.add_edge('netmgrd','sensors')
G.edge['netmgrd']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('netmgrd','thermal-engine')
G.edge['netmgrd']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['netmgrd']['thermal-engine']['fill'] = 'red'
G.add_edge('netmgrd','thermal-engine')
G.edge['netmgrd']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('netmgrd','time_daemon')
G.edge['netmgrd']['time_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][open open][write read]'
G.edge['netmgrd']['time_daemon']['fill'] = 'red'
G.add_edge('netmgrd','time_daemon')
G.edge['netmgrd']['time_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][open open][write read][append read]'
G.add_edge('netmgrd','wcnss_service')
G.edge['netmgrd']['wcnss_service']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['netmgrd']['wcnss_service']['fill'] = 'red'
G.add_edge('netmgrd','wcnss_service')
G.edge['netmgrd']['wcnss_service']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('netmgrd','wpa')
G.edge['netmgrd']['wpa']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['netmgrd']['wpa']['fill'] = 'red'
G.add_edge('netmgrd','wpa')
G.edge['netmgrd']['wpa']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qcomsysd','cnd')
G.edge['qcomsysd']['cnd']['write-read'] = '[open open]'
G.add_edge('qcomsysd','dpmd')
G.edge['qcomsysd']['dpmd']['write-read'] = '[open open]'
G.add_edge('qcomsysd','netmgrd')
G.edge['qcomsysd']['netmgrd']['write-read'] = '[open open]'
G.add_edge('qcomsysd','qcomsysd')
G.edge['qcomsysd']['qcomsysd']['write-read'] = '[open open][write read][open open][write read][write read][open open][write read][open open]'
G.add_edge('qcomsysd','qlogd')
G.edge['qcomsysd']['qlogd']['write-read'] = '[open open]'
G.add_edge('qcomsysd','qti')
G.edge['qcomsysd']['qti']['write-read'] = '[open open]'
G.add_edge('qcomsysd','rfs_access')
G.edge['qcomsysd']['rfs_access']['write-read'] = '[open open]'
G.add_edge('qcomsysd','rmt_storage')
G.edge['qcomsysd']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('qcomsysd','sensors')
G.edge['qcomsysd']['sensors']['write-read'] = '[open open]'
G.add_edge('qcomsysd','thermal-engine')
G.edge['qcomsysd']['thermal-engine']['write-read'] = '[open open]'
G.add_edge('qcomsysd','time_daemon')
G.edge['qcomsysd']['time_daemon']['write-read'] = '[open open]'
G.add_edge('qcomsysd','wcnss_service')
G.edge['qcomsysd']['wcnss_service']['write-read'] = '[open open]'
G.add_edge('qcomsysd','wpa')
G.edge['qcomsysd']['wpa']['write-read'] = '[open open]'
G.add_edge('qcomsysd','cnd')
G.edge['qcomsysd']['cnd']['write-read'] = '[open open][write read]'
G.edge['qcomsysd']['cnd']['fill'] = 'red'
G.add_edge('qcomsysd','cnd')
G.edge['qcomsysd']['cnd']['write-read'] = '[open open][write read][append read]'
G.add_edge('qcomsysd','dpmd')
G.edge['qcomsysd']['dpmd']['write-read'] = '[open open][write read]'
G.edge['qcomsysd']['dpmd']['fill'] = 'red'
G.add_edge('qcomsysd','dpmd')
G.edge['qcomsysd']['dpmd']['write-read'] = '[open open][write read][append read]'
G.add_edge('qcomsysd','netmgrd')
G.edge['qcomsysd']['netmgrd']['write-read'] = '[open open][write read]'
G.edge['qcomsysd']['netmgrd']['fill'] = 'red'
G.add_edge('qcomsysd','netmgrd')
G.edge['qcomsysd']['netmgrd']['write-read'] = '[open open][write read][append read]'
G.add_edge('qcomsysd','qcomsysd')
G.edge['qcomsysd']['qcomsysd']['write-read'] = '[open open][write read][open open][write read][write read][open open][write read][open open][write read]'
G.edge['qcomsysd']['qcomsysd']['fill'] = 'red'
G.add_edge('qcomsysd','qlogd')
G.edge['qcomsysd']['qlogd']['write-read'] = '[open open][write read]'
G.edge['qcomsysd']['qlogd']['fill'] = 'red'
G.add_edge('qcomsysd','qlogd')
G.edge['qcomsysd']['qlogd']['write-read'] = '[open open][write read][append read]'
G.add_edge('qcomsysd','qti')
G.edge['qcomsysd']['qti']['write-read'] = '[open open][write read]'
G.edge['qcomsysd']['qti']['fill'] = 'red'
G.add_edge('qcomsysd','qti')
G.edge['qcomsysd']['qti']['write-read'] = '[open open][write read][append read]'
G.add_edge('qcomsysd','rfs_access')
G.edge['qcomsysd']['rfs_access']['write-read'] = '[open open][write read]'
G.edge['qcomsysd']['rfs_access']['fill'] = 'red'
G.add_edge('qcomsysd','rfs_access')
G.edge['qcomsysd']['rfs_access']['write-read'] = '[open open][write read][append read]'
G.add_edge('qcomsysd','rmt_storage')
G.edge['qcomsysd']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['qcomsysd']['rmt_storage']['fill'] = 'red'
G.add_edge('qcomsysd','rmt_storage')
G.edge['qcomsysd']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('qcomsysd','sensors')
G.edge['qcomsysd']['sensors']['write-read'] = '[open open][write read]'
G.edge['qcomsysd']['sensors']['fill'] = 'red'
G.add_edge('qcomsysd','sensors')
G.edge['qcomsysd']['sensors']['write-read'] = '[open open][write read][append read]'
G.add_edge('qcomsysd','thermal-engine')
G.edge['qcomsysd']['thermal-engine']['write-read'] = '[open open][write read]'
G.edge['qcomsysd']['thermal-engine']['fill'] = 'red'
G.add_edge('qcomsysd','thermal-engine')
G.edge['qcomsysd']['thermal-engine']['write-read'] = '[open open][write read][append read]'
G.add_edge('qcomsysd','time_daemon')
G.edge['qcomsysd']['time_daemon']['write-read'] = '[open open][write read]'
G.edge['qcomsysd']['time_daemon']['fill'] = 'red'
G.add_edge('qcomsysd','time_daemon')
G.edge['qcomsysd']['time_daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('qcomsysd','wcnss_service')
G.edge['qcomsysd']['wcnss_service']['write-read'] = '[open open][write read]'
G.edge['qcomsysd']['wcnss_service']['fill'] = 'red'
G.add_edge('qcomsysd','wcnss_service')
G.edge['qcomsysd']['wcnss_service']['write-read'] = '[open open][write read][append read]'
G.add_edge('qcomsysd','wpa')
G.edge['qcomsysd']['wpa']['write-read'] = '[open open][write read]'
G.edge['qcomsysd']['wpa']['fill'] = 'red'
G.add_edge('qcomsysd','wpa')
G.edge['qcomsysd']['wpa']['write-read'] = '[open open][write read][append read]'
G.add_edge('qlogd','cnd')
G.edge['qlogd']['cnd']['write-read'] = '[open open][append read][open open][write read][append read][open open]'
G.add_edge('qlogd','dpmd')
G.edge['qlogd']['dpmd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('qlogd','netmgrd')
G.edge['qlogd']['netmgrd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('qlogd','qcomsysd')
G.edge['qlogd']['qcomsysd']['write-read'] = '[open open]'
G.add_edge('qlogd','qlogd')
G.edge['qlogd']['qlogd']['write-read'] = '[open open][setattr getattr][write read][append read][setopt getopt][write read][open open][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('qlogd','qti')
G.edge['qlogd']['qti']['write-read'] = '[open open]'
G.add_edge('qlogd','rfs_access')
G.edge['qlogd']['rfs_access']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('qlogd','rmt_storage')
G.edge['qlogd']['rmt_storage']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('qlogd','sensors')
G.edge['qlogd']['sensors']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('qlogd','thermal-engine')
G.edge['qlogd']['thermal-engine']['write-read'] = '[open open]'
G.add_edge('qlogd','time_daemon')
G.edge['qlogd']['time_daemon']['write-read'] = '[open open]'
G.add_edge('qlogd','wcnss_service')
G.edge['qlogd']['wcnss_service']['write-read'] = '[open open]'
G.add_edge('qlogd','wpa')
G.edge['qlogd']['wpa']['write-read'] = '[setopt getopt][open open][write read][append read][open open]'
G.add_edge('qlogd','cnd')
G.edge['qlogd']['cnd']['write-read'] = '[open open][append read][open open][write read][append read][open open][write read]'
G.edge['qlogd']['cnd']['fill'] = 'red'
G.add_edge('qlogd','cnd')
G.edge['qlogd']['cnd']['write-read'] = '[open open][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('qlogd','dpmd')
G.edge['qlogd']['dpmd']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['qlogd']['dpmd']['fill'] = 'red'
G.add_edge('qlogd','dpmd')
G.edge['qlogd']['dpmd']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('qlogd','netmgrd')
G.edge['qlogd']['netmgrd']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['qlogd']['netmgrd']['fill'] = 'red'
G.add_edge('qlogd','netmgrd')
G.edge['qlogd']['netmgrd']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('qlogd','qcomsysd')
G.edge['qlogd']['qcomsysd']['write-read'] = '[open open][write read]'
G.edge['qlogd']['qcomsysd']['fill'] = 'red'
G.add_edge('qlogd','qlogd')
G.edge['qlogd']['qlogd']['write-read'] = '[open open][setattr getattr][write read][append read][setopt getopt][write read][open open][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['qlogd']['qlogd']['fill'] = 'red'
G.add_edge('qlogd','qlogd')
G.edge['qlogd']['qlogd']['write-read'] = '[open open][setattr getattr][write read][append read][setopt getopt][write read][open open][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('qlogd','qti')
G.edge['qlogd']['qti']['write-read'] = '[open open][write read]'
G.edge['qlogd']['qti']['fill'] = 'red'
G.add_edge('qlogd','qti')
G.edge['qlogd']['qti']['write-read'] = '[open open][write read][append read]'
G.add_edge('qlogd','rfs_access')
G.edge['qlogd']['rfs_access']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['qlogd']['rfs_access']['fill'] = 'red'
G.add_edge('qlogd','rfs_access')
G.edge['qlogd']['rfs_access']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('qlogd','rmt_storage')
G.edge['qlogd']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['qlogd']['rmt_storage']['fill'] = 'red'
G.add_edge('qlogd','rmt_storage')
G.edge['qlogd']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('qlogd','sensors')
G.edge['qlogd']['sensors']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['qlogd']['sensors']['fill'] = 'red'
G.add_edge('qlogd','sensors')
G.edge['qlogd']['sensors']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('qlogd','thermal-engine')
G.edge['qlogd']['thermal-engine']['write-read'] = '[open open][write read]'
G.edge['qlogd']['thermal-engine']['fill'] = 'red'
G.add_edge('qlogd','thermal-engine')
G.edge['qlogd']['thermal-engine']['write-read'] = '[open open][write read][append read]'
G.add_edge('qlogd','time_daemon')
G.edge['qlogd']['time_daemon']['write-read'] = '[open open][write read]'
G.edge['qlogd']['time_daemon']['fill'] = 'red'
G.add_edge('qlogd','time_daemon')
G.edge['qlogd']['time_daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('qlogd','wcnss_service')
G.edge['qlogd']['wcnss_service']['write-read'] = '[open open][write read]'
G.edge['qlogd']['wcnss_service']['fill'] = 'red'
G.add_edge('qlogd','wcnss_service')
G.edge['qlogd']['wcnss_service']['write-read'] = '[open open][write read][append read]'
G.add_edge('qlogd','wpa')
G.edge['qlogd']['wpa']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read]'
G.edge['qlogd']['wpa']['fill'] = 'red'
G.add_edge('qlogd','wpa')
G.edge['qlogd']['wpa']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read][append read]'
G.add_edge('qti','cnd')
G.edge['qti']['cnd']['write-read'] = '[write read][setattr getattr][write read][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qti','dpmd')
G.edge['qti']['dpmd']['write-read'] = '[write read][append read][setattr getattr][write read][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qti','netmgrd')
G.edge['qti']['netmgrd']['write-read'] = '[setattr getattr][write read][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qti','qcomsysd')
G.edge['qti']['qcomsysd']['write-read'] = '[open open]'
G.add_edge('qti','qlogd')
G.edge['qti']['qlogd']['write-read'] = '[open open]'
G.add_edge('qti','qti')
G.edge['qti']['qti']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][write read][setattr getattr][write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qti','rfs_access')
G.edge['qti']['rfs_access']['write-read'] = '[write read][append read][open open]'
G.add_edge('qti','rmt_storage')
G.edge['qti']['rmt_storage']['write-read'] = '[write read][append read][write read][open open]'
G.add_edge('qti','sensors')
G.edge['qti']['sensors']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('qti','thermal-engine')
G.edge['qti']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qti','time_daemon')
G.edge['qti']['time_daemon']['write-read'] = '[write read][open open]'
G.add_edge('qti','wcnss_service')
G.edge['qti']['wcnss_service']['write-read'] = '[write read][append read][setattr getattr][write read][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qti','wpa')
G.edge['qti']['wpa']['write-read'] = '[write read][append read][setattr getattr][write read][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qti','cnd')
G.edge['qti']['cnd']['write-read'] = '[write read][setattr getattr][write read][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['qti']['cnd']['fill'] = 'red'
G.add_edge('qti','cnd')
G.edge['qti']['cnd']['write-read'] = '[write read][setattr getattr][write read][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qti','dpmd')
G.edge['qti']['dpmd']['write-read'] = '[write read][append read][setattr getattr][write read][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['qti']['dpmd']['fill'] = 'red'
G.add_edge('qti','dpmd')
G.edge['qti']['dpmd']['write-read'] = '[write read][append read][setattr getattr][write read][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qti','netmgrd')
G.edge['qti']['netmgrd']['write-read'] = '[setattr getattr][write read][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['qti']['netmgrd']['fill'] = 'red'
G.add_edge('qti','netmgrd')
G.edge['qti']['netmgrd']['write-read'] = '[setattr getattr][write read][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qti','qcomsysd')
G.edge['qti']['qcomsysd']['write-read'] = '[open open][write read]'
G.edge['qti']['qcomsysd']['fill'] = 'red'
G.add_edge('qti','qlogd')
G.edge['qti']['qlogd']['write-read'] = '[open open][write read]'
G.edge['qti']['qlogd']['fill'] = 'red'
G.add_edge('qti','qlogd')
G.edge['qti']['qlogd']['write-read'] = '[open open][write read][append read]'
G.add_edge('qti','qti')
G.edge['qti']['qti']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][write read][setattr getattr][write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['qti']['qti']['fill'] = 'red'
G.add_edge('qti','qti')
G.edge['qti']['qti']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][write read][setattr getattr][write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qti','rfs_access')
G.edge['qti']['rfs_access']['write-read'] = '[write read][append read][open open][write read]'
G.edge['qti']['rfs_access']['fill'] = 'red'
G.add_edge('qti','rfs_access')
G.edge['qti']['rfs_access']['write-read'] = '[write read][append read][open open][write read][append read]'
G.add_edge('qti','rmt_storage')
G.edge['qti']['rmt_storage']['write-read'] = '[write read][append read][write read][open open][write read]'
G.edge['qti']['rmt_storage']['fill'] = 'red'
G.add_edge('qti','rmt_storage')
G.edge['qti']['rmt_storage']['write-read'] = '[write read][append read][write read][open open][write read][append read]'
G.add_edge('qti','sensors')
G.edge['qti']['sensors']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['qti']['sensors']['fill'] = 'red'
G.add_edge('qti','sensors')
G.edge['qti']['sensors']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('qti','thermal-engine')
G.edge['qti']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['qti']['thermal-engine']['fill'] = 'red'
G.add_edge('qti','thermal-engine')
G.edge['qti']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qti','time_daemon')
G.edge['qti']['time_daemon']['write-read'] = '[write read][open open][write read]'
G.edge['qti']['time_daemon']['fill'] = 'red'
G.add_edge('qti','time_daemon')
G.edge['qti']['time_daemon']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('qti','wcnss_service')
G.edge['qti']['wcnss_service']['write-read'] = '[write read][append read][setattr getattr][write read][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['qti']['wcnss_service']['fill'] = 'red'
G.add_edge('qti','wcnss_service')
G.edge['qti']['wcnss_service']['write-read'] = '[write read][append read][setattr getattr][write read][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qti','wpa')
G.edge['qti']['wpa']['write-read'] = '[write read][append read][setattr getattr][write read][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['qti']['wpa']['fill'] = 'red'
G.add_edge('qti','wpa')
G.edge['qti']['wpa']['write-read'] = '[write read][append read][setattr getattr][write read][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rfs_access','cnd')
G.edge['rfs_access']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('rfs_access','dpmd')
G.edge['rfs_access']['dpmd']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('rfs_access','netmgrd')
G.edge['rfs_access']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('rfs_access','qcomsysd')
G.edge['rfs_access']['qcomsysd']['write-read'] = '[open open]'
G.add_edge('rfs_access','qlogd')
G.edge['rfs_access']['qlogd']['write-read'] = '[write read][add_name search][open open][append read][open open]'
G.add_edge('rfs_access','qti')
G.edge['rfs_access']['qti']['write-read'] = '[write read][open open]'
G.add_edge('rfs_access','rfs_access')
G.edge['rfs_access']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('rfs_access','rmt_storage')
G.edge['rfs_access']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][write read][setopt getopt][setopt getopt][open open]'
G.add_edge('rfs_access','sensors')
G.edge['rfs_access']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('rfs_access','thermal-engine')
G.edge['rfs_access']['thermal-engine']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('rfs_access','time_daemon')
G.edge['rfs_access']['time_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('rfs_access','wcnss_service')
G.edge['rfs_access']['wcnss_service']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('rfs_access','wpa')
G.edge['rfs_access']['wpa']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('rfs_access','cnd')
G.edge['rfs_access']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['rfs_access']['cnd']['fill'] = 'red'
G.add_edge('rfs_access','cnd')
G.edge['rfs_access']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('rfs_access','dpmd')
G.edge['rfs_access']['dpmd']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['rfs_access']['dpmd']['fill'] = 'red'
G.add_edge('rfs_access','dpmd')
G.edge['rfs_access']['dpmd']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('rfs_access','netmgrd')
G.edge['rfs_access']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['rfs_access']['netmgrd']['fill'] = 'red'
G.add_edge('rfs_access','netmgrd')
G.edge['rfs_access']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('rfs_access','qcomsysd')
G.edge['rfs_access']['qcomsysd']['write-read'] = '[open open][write read]'
G.edge['rfs_access']['qcomsysd']['fill'] = 'red'
G.add_edge('rfs_access','qlogd')
G.edge['rfs_access']['qlogd']['write-read'] = '[write read][add_name search][open open][append read][open open][write read]'
G.edge['rfs_access']['qlogd']['fill'] = 'red'
G.add_edge('rfs_access','qlogd')
G.edge['rfs_access']['qlogd']['write-read'] = '[write read][add_name search][open open][append read][open open][write read][append read]'
G.add_edge('rfs_access','qti')
G.edge['rfs_access']['qti']['write-read'] = '[write read][open open][write read]'
G.edge['rfs_access']['qti']['fill'] = 'red'
G.add_edge('rfs_access','qti')
G.edge['rfs_access']['qti']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('rfs_access','rfs_access')
G.edge['rfs_access']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['rfs_access']['rfs_access']['fill'] = 'red'
G.add_edge('rfs_access','rfs_access')
G.edge['rfs_access']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('rfs_access','rmt_storage')
G.edge['rfs_access']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][write read][setopt getopt][setopt getopt][open open][write read]'
G.edge['rfs_access']['rmt_storage']['fill'] = 'red'
G.add_edge('rfs_access','rmt_storage')
G.edge['rfs_access']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][write read][setopt getopt][setopt getopt][open open][write read][append read]'
G.add_edge('rfs_access','sensors')
G.edge['rfs_access']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['rfs_access']['sensors']['fill'] = 'red'
G.add_edge('rfs_access','sensors')
G.edge['rfs_access']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('rfs_access','thermal-engine')
G.edge['rfs_access']['thermal-engine']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['rfs_access']['thermal-engine']['fill'] = 'red'
G.add_edge('rfs_access','thermal-engine')
G.edge['rfs_access']['thermal-engine']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('rfs_access','time_daemon')
G.edge['rfs_access']['time_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][open open][write read]'
G.edge['rfs_access']['time_daemon']['fill'] = 'red'
G.add_edge('rfs_access','time_daemon')
G.edge['rfs_access']['time_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][open open][write read][append read]'
G.add_edge('rfs_access','wcnss_service')
G.edge['rfs_access']['wcnss_service']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['rfs_access']['wcnss_service']['fill'] = 'red'
G.add_edge('rfs_access','wcnss_service')
G.edge['rfs_access']['wcnss_service']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('rfs_access','wpa')
G.edge['rfs_access']['wpa']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['rfs_access']['wpa']['fill'] = 'red'
G.add_edge('rfs_access','wpa')
G.edge['rfs_access']['wpa']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('rmt_storage','cnd')
G.edge['rmt_storage']['cnd']['write-read'] = '[open open][append read][setattr getattr][write read][append read][setopt getopt][write read][append read][open open]'
G.add_edge('rmt_storage','dpmd')
G.edge['rmt_storage']['dpmd']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][append read][open open]'
G.add_edge('rmt_storage','netmgrd')
G.edge['rmt_storage']['netmgrd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open]'
G.add_edge('rmt_storage','qcomsysd')
G.edge['rmt_storage']['qcomsysd']['write-read'] = '[open open]'
G.add_edge('rmt_storage','qlogd')
G.edge['rmt_storage']['qlogd']['write-read'] = '[open open][append read][open open]'
G.add_edge('rmt_storage','qti')
G.edge['rmt_storage']['qti']['write-read'] = '[write read][write read][open open]'
G.add_edge('rmt_storage','rfs_access')
G.edge['rmt_storage']['rfs_access']['write-read'] = '[open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][append read][open open]'
G.add_edge('rmt_storage','rmt_storage')
G.edge['rmt_storage']['rmt_storage']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][write read][setopt getopt][setopt getopt][write read][append read][write read][open open]'
G.add_edge('rmt_storage','sensors')
G.edge['rmt_storage']['sensors']['write-read'] = '[add_name search][open open][write read][append read][open open]'
G.add_edge('rmt_storage','thermal-engine')
G.edge['rmt_storage']['thermal-engine']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][append read][open open]'
G.add_edge('rmt_storage','time_daemon')
G.edge['rmt_storage']['time_daemon']['write-read'] = '[write read][write read][open open]'
G.add_edge('rmt_storage','wcnss_service')
G.edge['rmt_storage']['wcnss_service']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open]'
G.add_edge('rmt_storage','wpa')
G.edge['rmt_storage']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open]'
G.add_edge('rmt_storage','cnd')
G.edge['rmt_storage']['cnd']['write-read'] = '[open open][append read][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read]'
G.edge['rmt_storage']['cnd']['fill'] = 'red'
G.add_edge('rmt_storage','cnd')
G.edge['rmt_storage']['cnd']['write-read'] = '[open open][append read][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read]'
G.add_edge('rmt_storage','dpmd')
G.edge['rmt_storage']['dpmd']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read]'
G.edge['rmt_storage']['dpmd']['fill'] = 'red'
G.add_edge('rmt_storage','dpmd')
G.edge['rmt_storage']['dpmd']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read]'
G.add_edge('rmt_storage','netmgrd')
G.edge['rmt_storage']['netmgrd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read]'
G.edge['rmt_storage']['netmgrd']['fill'] = 'red'
G.add_edge('rmt_storage','netmgrd')
G.edge['rmt_storage']['netmgrd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read]'
G.add_edge('rmt_storage','qcomsysd')
G.edge['rmt_storage']['qcomsysd']['write-read'] = '[open open][write read]'
G.edge['rmt_storage']['qcomsysd']['fill'] = 'red'
G.add_edge('rmt_storage','qlogd')
G.edge['rmt_storage']['qlogd']['write-read'] = '[open open][append read][open open][write read]'
G.edge['rmt_storage']['qlogd']['fill'] = 'red'
G.add_edge('rmt_storage','qlogd')
G.edge['rmt_storage']['qlogd']['write-read'] = '[open open][append read][open open][write read][append read]'
G.add_edge('rmt_storage','qti')
G.edge['rmt_storage']['qti']['write-read'] = '[write read][write read][open open][write read]'
G.edge['rmt_storage']['qti']['fill'] = 'red'
G.add_edge('rmt_storage','qti')
G.edge['rmt_storage']['qti']['write-read'] = '[write read][write read][open open][write read][append read]'
G.add_edge('rmt_storage','rfs_access')
G.edge['rmt_storage']['rfs_access']['write-read'] = '[open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read]'
G.edge['rmt_storage']['rfs_access']['fill'] = 'red'
G.add_edge('rmt_storage','rfs_access')
G.edge['rmt_storage']['rfs_access']['write-read'] = '[open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read]'
G.add_edge('rmt_storage','rmt_storage')
G.edge['rmt_storage']['rmt_storage']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][write read][setopt getopt][setopt getopt][write read][append read][write read][open open][write read]'
G.edge['rmt_storage']['rmt_storage']['fill'] = 'red'
G.add_edge('rmt_storage','rmt_storage')
G.edge['rmt_storage']['rmt_storage']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][write read][setopt getopt][setopt getopt][write read][append read][write read][open open][write read][append read]'
G.add_edge('rmt_storage','sensors')
G.edge['rmt_storage']['sensors']['write-read'] = '[add_name search][open open][write read][append read][open open][write read]'
G.edge['rmt_storage']['sensors']['fill'] = 'red'
G.add_edge('rmt_storage','sensors')
G.edge['rmt_storage']['sensors']['write-read'] = '[add_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('rmt_storage','thermal-engine')
G.edge['rmt_storage']['thermal-engine']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read]'
G.edge['rmt_storage']['thermal-engine']['fill'] = 'red'
G.add_edge('rmt_storage','thermal-engine')
G.edge['rmt_storage']['thermal-engine']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read]'
G.add_edge('rmt_storage','time_daemon')
G.edge['rmt_storage']['time_daemon']['write-read'] = '[write read][write read][open open][write read]'
G.edge['rmt_storage']['time_daemon']['fill'] = 'red'
G.add_edge('rmt_storage','time_daemon')
G.edge['rmt_storage']['time_daemon']['write-read'] = '[write read][write read][open open][write read][append read]'
G.add_edge('rmt_storage','wcnss_service')
G.edge['rmt_storage']['wcnss_service']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read]'
G.edge['rmt_storage']['wcnss_service']['fill'] = 'red'
G.add_edge('rmt_storage','wcnss_service')
G.edge['rmt_storage']['wcnss_service']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read]'
G.add_edge('rmt_storage','wpa')
G.edge['rmt_storage']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read]'
G.edge['rmt_storage']['wpa']['fill'] = 'red'
G.add_edge('rmt_storage','wpa')
G.edge['rmt_storage']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read]'
G.add_edge('sensors','cnd')
G.edge['sensors']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open]'
G.add_edge('sensors','dpmd')
G.edge['sensors']['dpmd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('sensors','netmgrd')
G.edge['sensors']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open]'
G.add_edge('sensors','qcomsysd')
G.edge['sensors']['qcomsysd']['write-read'] = '[open open]'
G.add_edge('sensors','qlogd')
G.edge['sensors']['qlogd']['write-read'] = '[write read][add_name search][open open][append read][open open]'
G.add_edge('sensors','qti')
G.edge['sensors']['qti']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('sensors','rfs_access')
G.edge['sensors']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('sensors','rmt_storage')
G.edge['sensors']['rmt_storage']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('sensors','sensors')
G.edge['sensors']['sensors']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('sensors','thermal-engine')
G.edge['sensors']['thermal-engine']['write-read'] = '[open open]'
G.add_edge('sensors','time_daemon')
G.edge['sensors']['time_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('sensors','wcnss_service')
G.edge['sensors']['wcnss_service']['write-read'] = '[open open]'
G.add_edge('sensors','wpa')
G.edge['sensors']['wpa']['write-read'] = '[open open]'
G.add_edge('sensors','cnd')
G.edge['sensors']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read]'
G.edge['sensors']['cnd']['fill'] = 'red'
G.add_edge('sensors','cnd')
G.edge['sensors']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read]'
G.add_edge('sensors','dpmd')
G.edge['sensors']['dpmd']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['sensors']['dpmd']['fill'] = 'red'
G.add_edge('sensors','dpmd')
G.edge['sensors']['dpmd']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('sensors','netmgrd')
G.edge['sensors']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read]'
G.edge['sensors']['netmgrd']['fill'] = 'red'
G.add_edge('sensors','netmgrd')
G.edge['sensors']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sensors','qcomsysd')
G.edge['sensors']['qcomsysd']['write-read'] = '[open open][write read]'
G.edge['sensors']['qcomsysd']['fill'] = 'red'
G.add_edge('sensors','qlogd')
G.edge['sensors']['qlogd']['write-read'] = '[write read][add_name search][open open][append read][open open][write read]'
G.edge['sensors']['qlogd']['fill'] = 'red'
G.add_edge('sensors','qlogd')
G.edge['sensors']['qlogd']['write-read'] = '[write read][add_name search][open open][append read][open open][write read][append read]'
G.add_edge('sensors','qti')
G.edge['sensors']['qti']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['sensors']['qti']['fill'] = 'red'
G.add_edge('sensors','qti')
G.edge['sensors']['qti']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('sensors','rfs_access')
G.edge['sensors']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['sensors']['rfs_access']['fill'] = 'red'
G.add_edge('sensors','rfs_access')
G.edge['sensors']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('sensors','rmt_storage')
G.edge['sensors']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['sensors']['rmt_storage']['fill'] = 'red'
G.add_edge('sensors','rmt_storage')
G.edge['sensors']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('sensors','sensors')
G.edge['sensors']['sensors']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['sensors']['sensors']['fill'] = 'red'
G.add_edge('sensors','sensors')
G.edge['sensors']['sensors']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('sensors','thermal-engine')
G.edge['sensors']['thermal-engine']['write-read'] = '[open open][write read]'
G.edge['sensors']['thermal-engine']['fill'] = 'red'
G.add_edge('sensors','thermal-engine')
G.edge['sensors']['thermal-engine']['write-read'] = '[open open][write read][append read]'
G.add_edge('sensors','time_daemon')
G.edge['sensors']['time_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['sensors']['time_daemon']['fill'] = 'red'
G.add_edge('sensors','time_daemon')
G.edge['sensors']['time_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sensors','wcnss_service')
G.edge['sensors']['wcnss_service']['write-read'] = '[open open][write read]'
G.edge['sensors']['wcnss_service']['fill'] = 'red'
G.add_edge('sensors','wcnss_service')
G.edge['sensors']['wcnss_service']['write-read'] = '[open open][write read][append read]'
G.add_edge('sensors','wpa')
G.edge['sensors']['wpa']['write-read'] = '[open open][write read]'
G.edge['sensors']['wpa']['fill'] = 'red'
G.add_edge('sensors','wpa')
G.edge['sensors']['wpa']['write-read'] = '[open open][write read][append read]'
G.add_edge('thermal-engine','cnd')
G.edge['thermal-engine']['cnd']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('thermal-engine','dpmd')
G.edge['thermal-engine']['dpmd']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('thermal-engine','netmgrd')
G.edge['thermal-engine']['netmgrd']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('thermal-engine','qcomsysd')
G.edge['thermal-engine']['qcomsysd']['write-read'] = '[open open]'
G.add_edge('thermal-engine','qlogd')
G.edge['thermal-engine']['qlogd']['write-read'] = '[open open]'
G.add_edge('thermal-engine','qti')
G.edge['thermal-engine']['qti']['write-read'] = '[setattr getattr][write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('thermal-engine','rfs_access')
G.edge['thermal-engine']['rfs_access']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('thermal-engine','rmt_storage')
G.edge['thermal-engine']['rmt_storage']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][write read][setopt getopt][setopt getopt][open open]'
G.add_edge('thermal-engine','sensors')
G.edge['thermal-engine']['sensors']['write-read'] = '[open open]'
G.add_edge('thermal-engine','thermal-engine')
G.edge['thermal-engine']['thermal-engine']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('thermal-engine','time_daemon')
G.edge['thermal-engine']['time_daemon']['write-read'] = '[write read][open open]'
G.add_edge('thermal-engine','wcnss_service')
G.edge['thermal-engine']['wcnss_service']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('thermal-engine','wpa')
G.edge['thermal-engine']['wpa']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('thermal-engine','cnd')
G.edge['thermal-engine']['cnd']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['thermal-engine']['cnd']['fill'] = 'red'
G.add_edge('thermal-engine','cnd')
G.edge['thermal-engine']['cnd']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('thermal-engine','dpmd')
G.edge['thermal-engine']['dpmd']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['thermal-engine']['dpmd']['fill'] = 'red'
G.add_edge('thermal-engine','dpmd')
G.edge['thermal-engine']['dpmd']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('thermal-engine','netmgrd')
G.edge['thermal-engine']['netmgrd']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['thermal-engine']['netmgrd']['fill'] = 'red'
G.add_edge('thermal-engine','netmgrd')
G.edge['thermal-engine']['netmgrd']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('thermal-engine','qcomsysd')
G.edge['thermal-engine']['qcomsysd']['write-read'] = '[open open][write read]'
G.edge['thermal-engine']['qcomsysd']['fill'] = 'red'
G.add_edge('thermal-engine','qlogd')
G.edge['thermal-engine']['qlogd']['write-read'] = '[open open][write read]'
G.edge['thermal-engine']['qlogd']['fill'] = 'red'
G.add_edge('thermal-engine','qlogd')
G.edge['thermal-engine']['qlogd']['write-read'] = '[open open][write read][append read]'
G.add_edge('thermal-engine','qti')
G.edge['thermal-engine']['qti']['write-read'] = '[setattr getattr][write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['thermal-engine']['qti']['fill'] = 'red'
G.add_edge('thermal-engine','qti')
G.edge['thermal-engine']['qti']['write-read'] = '[setattr getattr][write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('thermal-engine','rfs_access')
G.edge['thermal-engine']['rfs_access']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['thermal-engine']['rfs_access']['fill'] = 'red'
G.add_edge('thermal-engine','rfs_access')
G.edge['thermal-engine']['rfs_access']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('thermal-engine','rmt_storage')
G.edge['thermal-engine']['rmt_storage']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][write read][setopt getopt][setopt getopt][open open][write read]'
G.edge['thermal-engine']['rmt_storage']['fill'] = 'red'
G.add_edge('thermal-engine','rmt_storage')
G.edge['thermal-engine']['rmt_storage']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][write read][setopt getopt][setopt getopt][open open][write read][append read]'
G.add_edge('thermal-engine','sensors')
G.edge['thermal-engine']['sensors']['write-read'] = '[open open][write read]'
G.edge['thermal-engine']['sensors']['fill'] = 'red'
G.add_edge('thermal-engine','sensors')
G.edge['thermal-engine']['sensors']['write-read'] = '[open open][write read][append read]'
G.add_edge('thermal-engine','thermal-engine')
G.edge['thermal-engine']['thermal-engine']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['thermal-engine']['thermal-engine']['fill'] = 'red'
G.add_edge('thermal-engine','thermal-engine')
G.edge['thermal-engine']['thermal-engine']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('thermal-engine','time_daemon')
G.edge['thermal-engine']['time_daemon']['write-read'] = '[write read][open open][write read]'
G.edge['thermal-engine']['time_daemon']['fill'] = 'red'
G.add_edge('thermal-engine','time_daemon')
G.edge['thermal-engine']['time_daemon']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('thermal-engine','wcnss_service')
G.edge['thermal-engine']['wcnss_service']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['thermal-engine']['wcnss_service']['fill'] = 'red'
G.add_edge('thermal-engine','wcnss_service')
G.edge['thermal-engine']['wcnss_service']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('thermal-engine','wpa')
G.edge['thermal-engine']['wpa']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['thermal-engine']['wpa']['fill'] = 'red'
G.add_edge('thermal-engine','wpa')
G.edge['thermal-engine']['wpa']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('time_daemon','cnd')
G.edge['time_daemon']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][append read][open open]'
G.add_edge('time_daemon','dpmd')
G.edge['time_daemon']['dpmd']['write-read'] = '[write read][append read][open open]'
G.add_edge('time_daemon','netmgrd')
G.edge['time_daemon']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read][append read][open open]'
G.add_edge('time_daemon','qcomsysd')
G.edge['time_daemon']['qcomsysd']['write-read'] = '[open open]'
G.add_edge('time_daemon','qlogd')
G.edge['time_daemon']['qlogd']['write-read'] = '[write read][add_name search][open open]'
G.add_edge('time_daemon','qti')
G.edge['time_daemon']['qti']['write-read'] = '[write read][open open]'
G.add_edge('time_daemon','rfs_access')
G.edge['time_daemon']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open]'
G.add_edge('time_daemon','rmt_storage')
G.edge['time_daemon']['rmt_storage']['write-read'] = '[write read][append read][write read][open open]'
G.add_edge('time_daemon','sensors')
G.edge['time_daemon']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('time_daemon','thermal-engine')
G.edge['time_daemon']['thermal-engine']['write-read'] = '[write read][append read][open open]'
G.add_edge('time_daemon','time_daemon')
G.edge['time_daemon']['time_daemon']['write-read'] = '[open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][add_name search][remove_name search][add_name search][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][write read][open open]'
G.add_edge('time_daemon','wcnss_service')
G.edge['time_daemon']['wcnss_service']['write-read'] = '[write read][append read][open open]'
G.add_edge('time_daemon','wpa')
G.edge['time_daemon']['wpa']['write-read'] = '[write read][append read][open open]'
G.add_edge('time_daemon','cnd')
G.edge['time_daemon']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][append read][open open][write read]'
G.edge['time_daemon']['cnd']['fill'] = 'red'
G.add_edge('time_daemon','cnd')
G.edge['time_daemon']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][append read][open open][write read][append read]'
G.add_edge('time_daemon','dpmd')
G.edge['time_daemon']['dpmd']['write-read'] = '[write read][append read][open open][write read]'
G.edge['time_daemon']['dpmd']['fill'] = 'red'
G.add_edge('time_daemon','dpmd')
G.edge['time_daemon']['dpmd']['write-read'] = '[write read][append read][open open][write read][append read]'
G.add_edge('time_daemon','netmgrd')
G.edge['time_daemon']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read][append read][open open][write read]'
G.edge['time_daemon']['netmgrd']['fill'] = 'red'
G.add_edge('time_daemon','netmgrd')
G.edge['time_daemon']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read][append read][open open][write read][append read]'
G.add_edge('time_daemon','qcomsysd')
G.edge['time_daemon']['qcomsysd']['write-read'] = '[open open][write read]'
G.edge['time_daemon']['qcomsysd']['fill'] = 'red'
G.add_edge('time_daemon','qlogd')
G.edge['time_daemon']['qlogd']['write-read'] = '[write read][add_name search][open open][write read]'
G.edge['time_daemon']['qlogd']['fill'] = 'red'
G.add_edge('time_daemon','qlogd')
G.edge['time_daemon']['qlogd']['write-read'] = '[write read][add_name search][open open][write read][append read]'
G.add_edge('time_daemon','qti')
G.edge['time_daemon']['qti']['write-read'] = '[write read][open open][write read]'
G.edge['time_daemon']['qti']['fill'] = 'red'
G.add_edge('time_daemon','qti')
G.edge['time_daemon']['qti']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('time_daemon','rfs_access')
G.edge['time_daemon']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read]'
G.edge['time_daemon']['rfs_access']['fill'] = 'red'
G.add_edge('time_daemon','rfs_access')
G.edge['time_daemon']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read]'
G.add_edge('time_daemon','rmt_storage')
G.edge['time_daemon']['rmt_storage']['write-read'] = '[write read][append read][write read][open open][write read]'
G.edge['time_daemon']['rmt_storage']['fill'] = 'red'
G.add_edge('time_daemon','rmt_storage')
G.edge['time_daemon']['rmt_storage']['write-read'] = '[write read][append read][write read][open open][write read][append read]'
G.add_edge('time_daemon','sensors')
G.edge['time_daemon']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['time_daemon']['sensors']['fill'] = 'red'
G.add_edge('time_daemon','sensors')
G.edge['time_daemon']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('time_daemon','thermal-engine')
G.edge['time_daemon']['thermal-engine']['write-read'] = '[write read][append read][open open][write read]'
G.edge['time_daemon']['thermal-engine']['fill'] = 'red'
G.add_edge('time_daemon','thermal-engine')
G.edge['time_daemon']['thermal-engine']['write-read'] = '[write read][append read][open open][write read][append read]'
G.add_edge('time_daemon','time_daemon')
G.edge['time_daemon']['time_daemon']['write-read'] = '[open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][add_name search][remove_name search][add_name search][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][write read][open open][write read]'
G.edge['time_daemon']['time_daemon']['fill'] = 'red'
G.add_edge('time_daemon','time_daemon')
G.edge['time_daemon']['time_daemon']['write-read'] = '[open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][add_name search][remove_name search][add_name search][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][write read][open open][write read][append read]'
G.add_edge('time_daemon','wcnss_service')
G.edge['time_daemon']['wcnss_service']['write-read'] = '[write read][append read][open open][write read]'
G.edge['time_daemon']['wcnss_service']['fill'] = 'red'
G.add_edge('time_daemon','wcnss_service')
G.edge['time_daemon']['wcnss_service']['write-read'] = '[write read][append read][open open][write read][append read]'
G.add_edge('time_daemon','wpa')
G.edge['time_daemon']['wpa']['write-read'] = '[write read][append read][open open][write read]'
G.edge['time_daemon']['wpa']['fill'] = 'red'
G.add_edge('time_daemon','wpa')
G.edge['time_daemon']['wpa']['write-read'] = '[write read][append read][open open][write read][append read]'
G.add_edge('wcnss_service','cnd')
G.edge['wcnss_service']['cnd']['write-read'] = '[write read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('wcnss_service','dpmd')
G.edge['wcnss_service']['dpmd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('wcnss_service','netmgrd')
G.edge['wcnss_service']['netmgrd']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('wcnss_service','qcomsysd')
G.edge['wcnss_service']['qcomsysd']['write-read'] = '[open open]'
G.add_edge('wcnss_service','qlogd')
G.edge['wcnss_service']['qlogd']['write-read'] = '[open open]'
G.add_edge('wcnss_service','qti')
G.edge['wcnss_service']['qti']['write-read'] = '[write read][setattr getattr][write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('wcnss_service','rfs_access')
G.edge['wcnss_service']['rfs_access']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('wcnss_service','rmt_storage')
G.edge['wcnss_service']['rmt_storage']['write-read'] = '[setattr getattr][write read][append read][write read][setopt getopt][setopt getopt][open open]'
G.add_edge('wcnss_service','sensors')
G.edge['wcnss_service']['sensors']['write-read'] = '[open open]'
G.add_edge('wcnss_service','thermal-engine')
G.edge['wcnss_service']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('wcnss_service','time_daemon')
G.edge['wcnss_service']['time_daemon']['write-read'] = '[write read][open open]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('wcnss_service','wpa')
G.edge['wcnss_service']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('wcnss_service','cnd')
G.edge['wcnss_service']['cnd']['write-read'] = '[write read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['wcnss_service']['cnd']['fill'] = 'red'
G.add_edge('wcnss_service','cnd')
G.edge['wcnss_service']['cnd']['write-read'] = '[write read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('wcnss_service','dpmd')
G.edge['wcnss_service']['dpmd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['wcnss_service']['dpmd']['fill'] = 'red'
G.add_edge('wcnss_service','dpmd')
G.edge['wcnss_service']['dpmd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('wcnss_service','netmgrd')
G.edge['wcnss_service']['netmgrd']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['wcnss_service']['netmgrd']['fill'] = 'red'
G.add_edge('wcnss_service','netmgrd')
G.edge['wcnss_service']['netmgrd']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('wcnss_service','qcomsysd')
G.edge['wcnss_service']['qcomsysd']['write-read'] = '[open open][write read]'
G.edge['wcnss_service']['qcomsysd']['fill'] = 'red'
G.add_edge('wcnss_service','qlogd')
G.edge['wcnss_service']['qlogd']['write-read'] = '[open open][write read]'
G.edge['wcnss_service']['qlogd']['fill'] = 'red'
G.add_edge('wcnss_service','qlogd')
G.edge['wcnss_service']['qlogd']['write-read'] = '[open open][write read][append read]'
G.add_edge('wcnss_service','qti')
G.edge['wcnss_service']['qti']['write-read'] = '[write read][setattr getattr][write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['wcnss_service']['qti']['fill'] = 'red'
G.add_edge('wcnss_service','qti')
G.edge['wcnss_service']['qti']['write-read'] = '[write read][setattr getattr][write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('wcnss_service','rfs_access')
G.edge['wcnss_service']['rfs_access']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['wcnss_service']['rfs_access']['fill'] = 'red'
G.add_edge('wcnss_service','rfs_access')
G.edge['wcnss_service']['rfs_access']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('wcnss_service','rmt_storage')
G.edge['wcnss_service']['rmt_storage']['write-read'] = '[setattr getattr][write read][append read][write read][setopt getopt][setopt getopt][open open][write read]'
G.edge['wcnss_service']['rmt_storage']['fill'] = 'red'
G.add_edge('wcnss_service','rmt_storage')
G.edge['wcnss_service']['rmt_storage']['write-read'] = '[setattr getattr][write read][append read][write read][setopt getopt][setopt getopt][open open][write read][append read]'
G.add_edge('wcnss_service','sensors')
G.edge['wcnss_service']['sensors']['write-read'] = '[open open][write read]'
G.edge['wcnss_service']['sensors']['fill'] = 'red'
G.add_edge('wcnss_service','sensors')
G.edge['wcnss_service']['sensors']['write-read'] = '[open open][write read][append read]'
G.add_edge('wcnss_service','thermal-engine')
G.edge['wcnss_service']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['wcnss_service']['thermal-engine']['fill'] = 'red'
G.add_edge('wcnss_service','thermal-engine')
G.edge['wcnss_service']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('wcnss_service','time_daemon')
G.edge['wcnss_service']['time_daemon']['write-read'] = '[write read][open open][write read]'
G.edge['wcnss_service']['time_daemon']['fill'] = 'red'
G.add_edge('wcnss_service','time_daemon')
G.edge['wcnss_service']['time_daemon']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['wcnss_service']['wcnss_service']['fill'] = 'red'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('wcnss_service','wpa')
G.edge['wcnss_service']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['wcnss_service']['wpa']['fill'] = 'red'
G.add_edge('wcnss_service','wpa')
G.edge['wcnss_service']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('wpa','cnd')
G.edge['wpa']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][write read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('wpa','dpmd')
G.edge['wpa']['dpmd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('wpa','netmgrd')
G.edge['wpa']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('wpa','qcomsysd')
G.edge['wpa']['qcomsysd']['write-read'] = '[open open]'
G.add_edge('wpa','qlogd')
G.edge['wpa']['qlogd']['write-read'] = '[setopt getopt][write read][add_name search][open open]'
G.add_edge('wpa','qti')
G.edge['wpa']['qti']['write-read'] = '[write read][setattr getattr][write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('wpa','rfs_access')
G.edge['wpa']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('wpa','rmt_storage')
G.edge['wpa']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][write read][setopt getopt][setopt getopt][open open]'
G.add_edge('wpa','sensors')
G.edge['wpa']['sensors']['write-read'] = '[add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('wpa','thermal-engine')
G.edge['wpa']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('wpa','time_daemon')
G.edge['wpa']['time_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('wpa','wcnss_service')
G.edge['wpa']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('wpa','wpa')
G.edge['wpa']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('wpa','cnd')
G.edge['wpa']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][write read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['wpa']['cnd']['fill'] = 'red'
G.add_edge('wpa','cnd')
G.edge['wpa']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][write read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('wpa','dpmd')
G.edge['wpa']['dpmd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['wpa']['dpmd']['fill'] = 'red'
G.add_edge('wpa','dpmd')
G.edge['wpa']['dpmd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('wpa','netmgrd')
G.edge['wpa']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['wpa']['netmgrd']['fill'] = 'red'
G.add_edge('wpa','netmgrd')
G.edge['wpa']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('wpa','qcomsysd')
G.edge['wpa']['qcomsysd']['write-read'] = '[open open][write read]'
G.edge['wpa']['qcomsysd']['fill'] = 'red'
G.add_edge('wpa','qlogd')
G.edge['wpa']['qlogd']['write-read'] = '[setopt getopt][write read][add_name search][open open][write read]'
G.edge['wpa']['qlogd']['fill'] = 'red'
G.add_edge('wpa','qlogd')
G.edge['wpa']['qlogd']['write-read'] = '[setopt getopt][write read][add_name search][open open][write read][append read]'
G.add_edge('wpa','qti')
G.edge['wpa']['qti']['write-read'] = '[write read][setattr getattr][write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['wpa']['qti']['fill'] = 'red'
G.add_edge('wpa','qti')
G.edge['wpa']['qti']['write-read'] = '[write read][setattr getattr][write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('wpa','rfs_access')
G.edge['wpa']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['wpa']['rfs_access']['fill'] = 'red'
G.add_edge('wpa','rfs_access')
G.edge['wpa']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('wpa','rmt_storage')
G.edge['wpa']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][write read][setopt getopt][setopt getopt][open open][write read]'
G.edge['wpa']['rmt_storage']['fill'] = 'red'
G.add_edge('wpa','rmt_storage')
G.edge['wpa']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][write read][setopt getopt][setopt getopt][open open][write read][append read]'
G.add_edge('wpa','sensors')
G.edge['wpa']['sensors']['write-read'] = '[add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['wpa']['sensors']['fill'] = 'red'
G.add_edge('wpa','sensors')
G.edge['wpa']['sensors']['write-read'] = '[add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('wpa','thermal-engine')
G.edge['wpa']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['wpa']['thermal-engine']['fill'] = 'red'
G.add_edge('wpa','thermal-engine')
G.edge['wpa']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('wpa','time_daemon')
G.edge['wpa']['time_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][open open][write read]'
G.edge['wpa']['time_daemon']['fill'] = 'red'
G.add_edge('wpa','time_daemon')
G.edge['wpa']['time_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][open open][write read][append read]'
G.add_edge('wpa','wcnss_service')
G.edge['wpa']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['wpa']['wcnss_service']['fill'] = 'red'
G.add_edge('wpa','wcnss_service')
G.edge['wpa']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('wpa','wpa')
G.edge['wpa']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['wpa']['wpa']['fill'] = 'red'
G.add_edge('wpa','wpa')
G.edge['wpa']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
app = Viewer(G)
app.mainloop()