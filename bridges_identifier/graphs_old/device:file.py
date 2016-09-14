import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('ddexe','icd')
G.edge['ddexe']['icd']['write-read'] = '[open open]'
G.add_edge('ddexe','rild')
G.edge['ddexe']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('ddexe','ueventd')
G.edge['ddexe']['ueventd']['write-read'] = '[open open]'
G.add_edge('ddexe','rild')
G.edge['ddexe']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ddexe','ueventd')
G.edge['ddexe']['ueventd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ddexe','icd')
G.edge['ddexe']['icd']['write-read'] = '[open open][write read]'
G.edge['ddexe']['icd']['fill'] = 'red'
G.add_edge('ddexe','icd')
G.edge['ddexe']['icd']['write-read'] = '[open open][write read][append read]'
G.add_edge('ddexe','rild')
G.edge['ddexe']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ddexe']['rild']['fill'] = 'red'
G.add_edge('ddexe','rild')
G.edge['ddexe']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ddexe','ueventd')
G.edge['ddexe']['ueventd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ddexe']['ueventd']['fill'] = 'red'
G.add_edge('ddexe','ueventd')
G.edge['ddexe']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('dhcp','icd')
G.edge['dhcp']['icd']['write-read'] = '[open open]'
G.add_edge('dhcp','rild')
G.edge['dhcp']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('dhcp','ueventd')
G.edge['dhcp']['ueventd']['write-read'] = '[open open]'
G.add_edge('dhcp','rild')
G.edge['dhcp']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('dhcp','ueventd')
G.edge['dhcp']['ueventd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dhcp','icd')
G.edge['dhcp']['icd']['write-read'] = '[open open][write read]'
G.edge['dhcp']['icd']['fill'] = 'red'
G.add_edge('dhcp','icd')
G.edge['dhcp']['icd']['write-read'] = '[open open][write read][append read]'
G.add_edge('dhcp','rild')
G.edge['dhcp']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['dhcp']['rild']['fill'] = 'red'
G.add_edge('dhcp','rild')
G.edge['dhcp']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('dhcp','ueventd')
G.edge['dhcp']['ueventd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dhcp']['ueventd']['fill'] = 'red'
G.add_edge('dhcp','ueventd')
G.edge['dhcp']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('domain','icd')
G.edge['domain']['icd']['write-read'] = '[write read]'
G.edge['domain']['icd']['fill'] = 'red'
G.add_edge('domain','icd')
G.edge['domain']['icd']['write-read'] = '[write read][append read]'
G.add_edge('domain','rild')
G.edge['domain']['rild']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['domain']['rild']['fill'] = 'red'
G.add_edge('domain','rild')
G.edge['domain']['rild']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('domain','ueventd')
G.edge['domain']['ueventd']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['domain']['ueventd']['fill'] = 'red'
G.add_edge('domain','ueventd')
G.edge['domain']['ueventd']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][write read][append read][write read][append read]'
G.add_edge('ime_app','icd')
G.edge['ime_app']['icd']['write-read'] = '[open open]'
G.add_edge('ime_app','rild')
G.edge['ime_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','ueventd')
G.edge['ime_app']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','rild')
G.edge['ime_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ime_app','ueventd')
G.edge['ime_app']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ime_app','icd')
G.edge['ime_app']['icd']['write-read'] = '[open open][write read]'
G.edge['ime_app']['icd']['fill'] = 'red'
G.add_edge('ime_app','icd')
G.edge['ime_app']['icd']['write-read'] = '[open open][write read][append read]'
G.add_edge('ime_app','rild')
G.edge['ime_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ime_app']['rild']['fill'] = 'red'
G.add_edge('ime_app','rild')
G.edge['ime_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','ueventd')
G.edge['ime_app']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ime_app']['ueventd']['fill'] = 'red'
G.add_edge('ime_app','ueventd')
G.edge['ime_app']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('immvibed','icd')
G.edge['immvibed']['icd']['write-read'] = '[open open]'
G.add_edge('immvibed','rild')
G.edge['immvibed']['rild']['write-read'] = '[open open]'
G.add_edge('immvibed','ueventd')
G.edge['immvibed']['ueventd']['write-read'] = '[open open]'
G.add_edge('immvibed','rild')
G.edge['immvibed']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('immvibed','ueventd')
G.edge['immvibed']['ueventd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('immvibed','icd')
G.edge['immvibed']['icd']['write-read'] = '[open open][write read]'
G.edge['immvibed']['icd']['fill'] = 'red'
G.add_edge('immvibed','icd')
G.edge['immvibed']['icd']['write-read'] = '[open open][write read][append read]'
G.add_edge('immvibed','rild')
G.edge['immvibed']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['immvibed']['rild']['fill'] = 'red'
G.add_edge('immvibed','rild')
G.edge['immvibed']['rild']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('immvibed','ueventd')
G.edge['immvibed']['ueventd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['immvibed']['ueventd']['fill'] = 'red'
G.add_edge('immvibed','ueventd')
G.edge['immvibed']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('kiesexe','icd')
G.edge['kiesexe']['icd']['write-read'] = '[open open]'
G.add_edge('kiesexe','rild')
G.edge['kiesexe']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('kiesexe','ueventd')
G.edge['kiesexe']['ueventd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('kiesexe','rild')
G.edge['kiesexe']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('kiesexe','ueventd')
G.edge['kiesexe']['ueventd']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('kiesexe','icd')
G.edge['kiesexe']['icd']['write-read'] = '[open open][write read]'
G.edge['kiesexe']['icd']['fill'] = 'red'
G.add_edge('kiesexe','icd')
G.edge['kiesexe']['icd']['write-read'] = '[open open][write read][append read]'
G.add_edge('kiesexe','rild')
G.edge['kiesexe']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['kiesexe']['rild']['fill'] = 'red'
G.add_edge('kiesexe','rild')
G.edge['kiesexe']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('kiesexe','ueventd')
G.edge['kiesexe']['ueventd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['kiesexe']['ueventd']['fill'] = 'red'
G.add_edge('kiesexe','ueventd')
G.edge['kiesexe']['ueventd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('p2p_supplicant','icd')
G.edge['p2p_supplicant']['icd']['write-read'] = '[open open]'
G.add_edge('p2p_supplicant','rild')
G.edge['p2p_supplicant']['rild']['write-read'] = '[write read][append read][open open]'
G.add_edge('p2p_supplicant','ueventd')
G.edge['p2p_supplicant']['ueventd']['write-read'] = '[open open]'
G.add_edge('p2p_supplicant','rild')
G.edge['p2p_supplicant']['rild']['write-read'] = '[write read][append read][open open][setattr getattr]'
G.add_edge('p2p_supplicant','ueventd')
G.edge['p2p_supplicant']['ueventd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('p2p_supplicant','icd')
G.edge['p2p_supplicant']['icd']['write-read'] = '[open open][write read]'
G.edge['p2p_supplicant']['icd']['fill'] = 'red'
G.add_edge('p2p_supplicant','icd')
G.edge['p2p_supplicant']['icd']['write-read'] = '[open open][write read][append read]'
G.add_edge('p2p_supplicant','rild')
G.edge['p2p_supplicant']['rild']['write-read'] = '[write read][append read][open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['rild']['fill'] = 'red'
G.add_edge('p2p_supplicant','rild')
G.edge['p2p_supplicant']['rild']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('p2p_supplicant','ueventd')
G.edge['p2p_supplicant']['ueventd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['p2p_supplicant']['ueventd']['fill'] = 'red'
G.add_edge('p2p_supplicant','ueventd')
G.edge['p2p_supplicant']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('rild','icd')
G.edge['rild']['icd']['write-read'] = '[open open]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read][append read][write read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','ueventd')
G.edge['rild']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('rild','ueventd')
G.edge['rild']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('rild','icd')
G.edge['rild']['icd']['write-read'] = '[open open][write read]'
G.edge['rild']['icd']['fill'] = 'red'
G.add_edge('rild','icd')
G.edge['rild']['icd']['write-read'] = '[open open][write read][append read]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['rild']['rild']['fill'] = 'red'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('rild','ueventd')
G.edge['rild']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['rild']['ueventd']['fill'] = 'red'
G.add_edge('rild','ueventd')
G.edge['rild']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('servicemanager','icd')
G.edge['servicemanager']['icd']['write-read'] = '[open open]'
G.add_edge('servicemanager','rild')
G.edge['servicemanager']['rild']['write-read'] = '[open open]'
G.add_edge('servicemanager','ueventd')
G.edge['servicemanager']['ueventd']['write-read'] = '[open open]'
G.add_edge('servicemanager','rild')
G.edge['servicemanager']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('servicemanager','ueventd')
G.edge['servicemanager']['ueventd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('servicemanager','icd')
G.edge['servicemanager']['icd']['write-read'] = '[open open][write read]'
G.edge['servicemanager']['icd']['fill'] = 'red'
G.add_edge('servicemanager','icd')
G.edge['servicemanager']['icd']['write-read'] = '[open open][write read][append read]'
G.add_edge('servicemanager','rild')
G.edge['servicemanager']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['servicemanager']['rild']['fill'] = 'red'
G.add_edge('servicemanager','rild')
G.edge['servicemanager']['rild']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('servicemanager','ueventd')
G.edge['servicemanager']['ueventd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['servicemanager']['ueventd']['fill'] = 'red'
G.add_edge('servicemanager','ueventd')
G.edge['servicemanager']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','icd')
G.edge['s_system_app']['icd']['write-read'] = '[open open]'
G.add_edge('s_system_app','rild')
G.edge['s_system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','ueventd')
G.edge['s_system_app']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','rild')
G.edge['s_system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','ueventd')
G.edge['s_system_app']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','icd')
G.edge['s_system_app']['icd']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['icd']['fill'] = 'red'
G.add_edge('s_system_app','icd')
G.edge['s_system_app']['icd']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','rild')
G.edge['s_system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['rild']['fill'] = 'red'
G.add_edge('s_system_app','rild')
G.edge['s_system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','ueventd')
G.edge['s_system_app']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['ueventd']['fill'] = 'red'
G.add_edge('s_system_app','ueventd')
G.edge['s_system_app']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','icd')
G.edge['system_app']['icd']['write-read'] = '[open open]'
G.add_edge('system_app','rild')
G.edge['system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','ueventd')
G.edge['system_app']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','rild')
G.edge['system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_app','ueventd')
G.edge['system_app']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_app','icd')
G.edge['system_app']['icd']['write-read'] = '[open open][write read]'
G.edge['system_app']['icd']['fill'] = 'red'
G.add_edge('system_app','icd')
G.edge['system_app']['icd']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_app','rild')
G.edge['system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_app']['rild']['fill'] = 'red'
G.add_edge('system_app','rild')
G.edge['system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','ueventd')
G.edge['system_app']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_app']['ueventd']['fill'] = 'red'
G.add_edge('system_app','ueventd')
G.edge['system_app']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ueventd','icd')
G.edge['ueventd']['icd']['write-read'] = '[open open]'
G.add_edge('ueventd','rild')
G.edge['ueventd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][relabelto relabelfrom][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('ueventd','rild')
G.edge['ueventd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][relabelto relabelfrom][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ueventd','icd')
G.edge['ueventd']['icd']['write-read'] = '[open open][write read]'
G.edge['ueventd']['icd']['fill'] = 'red'
G.add_edge('ueventd','icd')
G.edge['ueventd']['icd']['write-read'] = '[open open][write read][append read]'
G.add_edge('ueventd','rild')
G.edge['ueventd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ueventd']['rild']['fill'] = 'red'
G.add_edge('ueventd','rild')
G.edge['ueventd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][relabelto relabelfrom][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ueventd']['ueventd']['fill'] = 'red'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][relabelto relabelfrom][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('wpa','icd')
G.edge['wpa']['icd']['write-read'] = '[open open]'
G.add_edge('wpa','rild')
G.edge['wpa']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('wpa','ueventd')
G.edge['wpa']['ueventd']['write-read'] = '[open open]'
G.add_edge('wpa','rild')
G.edge['wpa']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('wpa','ueventd')
G.edge['wpa']['ueventd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wpa','icd')
G.edge['wpa']['icd']['write-read'] = '[open open][write read]'
G.edge['wpa']['icd']['fill'] = 'red'
G.add_edge('wpa','icd')
G.edge['wpa']['icd']['write-read'] = '[open open][write read][append read]'
G.add_edge('wpa','rild')
G.edge['wpa']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['wpa']['rild']['fill'] = 'red'
G.add_edge('wpa','rild')
G.edge['wpa']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('wpa','ueventd')
G.edge['wpa']['ueventd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wpa']['ueventd']['fill'] = 'red'
G.add_edge('wpa','ueventd')
G.edge['wpa']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()