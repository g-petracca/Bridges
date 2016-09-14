import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('debuggerd','debug_interface_proxy')
G.edge['debuggerd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('debuggerd','init_shell')
G.edge['debuggerd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('debuggerd','installd')
G.edge['debuggerd']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('debuggerd','kernel')
G.edge['debuggerd']['kernel']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('debuggerd','mobexdaemon')
G.edge['debuggerd']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('debuggerd','qcks')
G.edge['debuggerd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('debuggerd','sdcardd')
G.edge['debuggerd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('debuggerd','ueventd')
G.edge['debuggerd']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('debuggerd','untrusteddomain')
G.edge['debuggerd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('debuggerd','debug_interface_proxy')
G.edge['debuggerd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('debuggerd','init_shell')
G.edge['debuggerd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('debuggerd','installd')
G.edge['debuggerd']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('debuggerd','mobexdaemon')
G.edge['debuggerd']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('debuggerd','qcks')
G.edge['debuggerd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('debuggerd','sdcardd')
G.edge['debuggerd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('debuggerd','ueventd')
G.edge['debuggerd']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('debuggerd','untrusteddomain')
G.edge['debuggerd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('debuggerd','debug_interface_proxy')
G.edge['debuggerd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['debuggerd']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('debuggerd','init_shell')
G.edge['debuggerd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['debuggerd']['init_shell']['fill'] = 'red'
G.add_edge('debuggerd','installd')
G.edge['debuggerd']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['debuggerd']['installd']['fill'] = 'red'
G.add_edge('debuggerd','kernel')
G.edge['debuggerd']['kernel']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['debuggerd']['kernel']['fill'] = 'red'
G.add_edge('debuggerd','mobexdaemon')
G.edge['debuggerd']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['debuggerd']['mobexdaemon']['fill'] = 'red'
G.add_edge('debuggerd','qcks')
G.edge['debuggerd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['debuggerd']['qcks']['fill'] = 'red'
G.add_edge('debuggerd','sdcardd')
G.edge['debuggerd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['debuggerd']['sdcardd']['fill'] = 'red'
G.add_edge('debuggerd','ueventd')
G.edge['debuggerd']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['debuggerd']['ueventd']['fill'] = 'red'
G.add_edge('debuggerd','untrusteddomain')
G.edge['debuggerd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['debuggerd']['untrusteddomain']['fill'] = 'red'
G.add_edge('debuggerd','debug_interface_proxy')
G.edge['debuggerd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','debug_interface_proxy')
G.edge['debuggerd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','init_shell')
G.edge['debuggerd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','init_shell')
G.edge['debuggerd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','installd')
G.edge['debuggerd']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','installd')
G.edge['debuggerd']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','kernel')
G.edge['debuggerd']['kernel']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('debuggerd','kernel')
G.edge['debuggerd']['kernel']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','mobexdaemon')
G.edge['debuggerd']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','mobexdaemon')
G.edge['debuggerd']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','qcks')
G.edge['debuggerd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','qcks')
G.edge['debuggerd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','sdcardd')
G.edge['debuggerd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','sdcardd')
G.edge['debuggerd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','ueventd')
G.edge['debuggerd']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','ueventd')
G.edge['debuggerd']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','untrusteddomain')
G.edge['debuggerd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','untrusteddomain')
G.edge['debuggerd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debug_interface_proxy','debug_interface_proxy')
G.edge['debug_interface_proxy']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('debug_interface_proxy','init_shell')
G.edge['debug_interface_proxy']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('debug_interface_proxy','installd')
G.edge['debug_interface_proxy']['installd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('debug_interface_proxy','kernel')
G.edge['debug_interface_proxy']['kernel']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('debug_interface_proxy','mobexdaemon')
G.edge['debug_interface_proxy']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('debug_interface_proxy','qcks')
G.edge['debug_interface_proxy']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('debug_interface_proxy','sdcardd')
G.edge['debug_interface_proxy']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('debug_interface_proxy','ueventd')
G.edge['debug_interface_proxy']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('debug_interface_proxy','untrusteddomain')
G.edge['debug_interface_proxy']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('debug_interface_proxy','debug_interface_proxy')
G.edge['debug_interface_proxy']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('debug_interface_proxy','init_shell')
G.edge['debug_interface_proxy']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('debug_interface_proxy','installd')
G.edge['debug_interface_proxy']['installd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('debug_interface_proxy','mobexdaemon')
G.edge['debug_interface_proxy']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('debug_interface_proxy','qcks')
G.edge['debug_interface_proxy']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('debug_interface_proxy','sdcardd')
G.edge['debug_interface_proxy']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('debug_interface_proxy','ueventd')
G.edge['debug_interface_proxy']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('debug_interface_proxy','untrusteddomain')
G.edge['debug_interface_proxy']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('debug_interface_proxy','debug_interface_proxy')
G.edge['debug_interface_proxy']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['debug_interface_proxy']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('debug_interface_proxy','init_shell')
G.edge['debug_interface_proxy']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['debug_interface_proxy']['init_shell']['fill'] = 'red'
G.add_edge('debug_interface_proxy','installd')
G.edge['debug_interface_proxy']['installd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['debug_interface_proxy']['installd']['fill'] = 'red'
G.add_edge('debug_interface_proxy','kernel')
G.edge['debug_interface_proxy']['kernel']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['debug_interface_proxy']['kernel']['fill'] = 'red'
G.add_edge('debug_interface_proxy','mobexdaemon')
G.edge['debug_interface_proxy']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['debug_interface_proxy']['mobexdaemon']['fill'] = 'red'
G.add_edge('debug_interface_proxy','qcks')
G.edge['debug_interface_proxy']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['debug_interface_proxy']['qcks']['fill'] = 'red'
G.add_edge('debug_interface_proxy','sdcardd')
G.edge['debug_interface_proxy']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['debug_interface_proxy']['sdcardd']['fill'] = 'red'
G.add_edge('debug_interface_proxy','ueventd')
G.edge['debug_interface_proxy']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['debug_interface_proxy']['ueventd']['fill'] = 'red'
G.add_edge('debug_interface_proxy','untrusteddomain')
G.edge['debug_interface_proxy']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['debug_interface_proxy']['untrusteddomain']['fill'] = 'red'
G.add_edge('debug_interface_proxy','debug_interface_proxy')
G.edge['debug_interface_proxy']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('debug_interface_proxy','debug_interface_proxy')
G.edge['debug_interface_proxy']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debug_interface_proxy','init_shell')
G.edge['debug_interface_proxy']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('debug_interface_proxy','init_shell')
G.edge['debug_interface_proxy']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debug_interface_proxy','installd')
G.edge['debug_interface_proxy']['installd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('debug_interface_proxy','installd')
G.edge['debug_interface_proxy']['installd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debug_interface_proxy','kernel')
G.edge['debug_interface_proxy']['kernel']['write-read'] = '[open open][write read][append read][open open][write read][add_name search]'
G.add_edge('debug_interface_proxy','kernel')
G.edge['debug_interface_proxy']['kernel']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('debug_interface_proxy','mobexdaemon')
G.edge['debug_interface_proxy']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('debug_interface_proxy','mobexdaemon')
G.edge['debug_interface_proxy']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debug_interface_proxy','qcks')
G.edge['debug_interface_proxy']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('debug_interface_proxy','qcks')
G.edge['debug_interface_proxy']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debug_interface_proxy','sdcardd')
G.edge['debug_interface_proxy']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('debug_interface_proxy','sdcardd')
G.edge['debug_interface_proxy']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debug_interface_proxy','ueventd')
G.edge['debug_interface_proxy']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('debug_interface_proxy','ueventd')
G.edge['debug_interface_proxy']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debug_interface_proxy','untrusteddomain')
G.edge['debug_interface_proxy']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('debug_interface_proxy','untrusteddomain')
G.edge['debug_interface_proxy']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','debug_interface_proxy')
G.edge['init_shell']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','installd')
G.edge['init_shell']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','kernel')
G.edge['init_shell']['kernel']['write-read'] = '[relabelto relabelfrom][relabelto relabelfrom][open open][write read][append read][open open]'
G.add_edge('init_shell','mobexdaemon')
G.edge['init_shell']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','qcks')
G.edge['init_shell']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('init_shell','sdcardd')
G.edge['init_shell']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','ueventd')
G.edge['init_shell']['ueventd']['write-read'] = '[setattr getattr][open open][write read][append read][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('init_shell','untrusteddomain')
G.edge['init_shell']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open]'
G.add_edge('init_shell','debug_interface_proxy')
G.edge['init_shell']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','installd')
G.edge['init_shell']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','mobexdaemon')
G.edge['init_shell']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','qcks')
G.edge['init_shell']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','sdcardd')
G.edge['init_shell']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','ueventd')
G.edge['init_shell']['ueventd']['write-read'] = '[setattr getattr][open open][write read][append read][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','untrusteddomain')
G.edge['init_shell']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr]'
G.add_edge('init_shell','debug_interface_proxy')
G.edge['init_shell']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read]'
G.edge['init_shell']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['init_shell']['fill'] = 'red'
G.add_edge('init_shell','installd')
G.edge['init_shell']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['installd']['fill'] = 'red'
G.add_edge('init_shell','kernel')
G.edge['init_shell']['kernel']['write-read'] = '[relabelto relabelfrom][relabelto relabelfrom][open open][write read][append read][open open][write read]'
G.edge['init_shell']['kernel']['fill'] = 'red'
G.add_edge('init_shell','mobexdaemon')
G.edge['init_shell']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['mobexdaemon']['fill'] = 'red'
G.add_edge('init_shell','qcks')
G.edge['init_shell']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['qcks']['fill'] = 'red'
G.add_edge('init_shell','sdcardd')
G.edge['init_shell']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['sdcardd']['fill'] = 'red'
G.add_edge('init_shell','ueventd')
G.edge['init_shell']['ueventd']['write-read'] = '[setattr getattr][open open][write read][append read][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['ueventd']['fill'] = 'red'
G.add_edge('init_shell','untrusteddomain')
G.edge['init_shell']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read]'
G.edge['init_shell']['untrusteddomain']['fill'] = 'red'
G.add_edge('init_shell','debug_interface_proxy')
G.edge['init_shell']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','debug_interface_proxy')
G.edge['init_shell']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','installd')
G.edge['init_shell']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','installd')
G.edge['init_shell']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','kernel')
G.edge['init_shell']['kernel']['write-read'] = '[relabelto relabelfrom][relabelto relabelfrom][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('init_shell','kernel')
G.edge['init_shell']['kernel']['write-read'] = '[relabelto relabelfrom][relabelto relabelfrom][open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('init_shell','mobexdaemon')
G.edge['init_shell']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','mobexdaemon')
G.edge['init_shell']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','qcks')
G.edge['init_shell']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','qcks')
G.edge['init_shell']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','sdcardd')
G.edge['init_shell']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','sdcardd')
G.edge['init_shell']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','ueventd')
G.edge['init_shell']['ueventd']['write-read'] = '[setattr getattr][open open][write read][append read][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','ueventd')
G.edge['init_shell']['ueventd']['write-read'] = '[setattr getattr][open open][write read][append read][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','untrusteddomain')
G.edge['init_shell']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','untrusteddomain')
G.edge['init_shell']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','debug_interface_proxy')
G.edge['installd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('installd','init_shell')
G.edge['installd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open]'
G.add_edge('installd','kernel')
G.edge['installd']['kernel']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('installd','mobexdaemon')
G.edge['installd']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('installd','qcks')
G.edge['installd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('installd','sdcardd')
G.edge['installd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('installd','ueventd')
G.edge['installd']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('installd','untrusteddomain')
G.edge['installd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('installd','debug_interface_proxy')
G.edge['installd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('installd','init_shell')
G.edge['installd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr]'
G.add_edge('installd','mobexdaemon')
G.edge['installd']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('installd','qcks')
G.edge['installd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('installd','sdcardd')
G.edge['installd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('installd','ueventd')
G.edge['installd']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('installd','untrusteddomain')
G.edge['installd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('installd','debug_interface_proxy')
G.edge['installd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['installd']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('installd','init_shell')
G.edge['installd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['installd']['init_shell']['fill'] = 'red'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read]'
G.edge['installd']['installd']['fill'] = 'red'
G.add_edge('installd','kernel')
G.edge['installd']['kernel']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['installd']['kernel']['fill'] = 'red'
G.add_edge('installd','mobexdaemon')
G.edge['installd']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['installd']['mobexdaemon']['fill'] = 'red'
G.add_edge('installd','qcks')
G.edge['installd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['installd']['qcks']['fill'] = 'red'
G.add_edge('installd','sdcardd')
G.edge['installd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['installd']['sdcardd']['fill'] = 'red'
G.add_edge('installd','ueventd')
G.edge['installd']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['installd']['ueventd']['fill'] = 'red'
G.add_edge('installd','untrusteddomain')
G.edge['installd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['installd']['untrusteddomain']['fill'] = 'red'
G.add_edge('installd','debug_interface_proxy')
G.edge['installd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','debug_interface_proxy')
G.edge['installd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','init_shell')
G.edge['installd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','init_shell')
G.edge['installd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','kernel')
G.edge['installd']['kernel']['write-read'] = '[open open][write read][append read][open open][write read][add_name search]'
G.add_edge('installd','kernel')
G.edge['installd']['kernel']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('installd','mobexdaemon')
G.edge['installd']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','mobexdaemon')
G.edge['installd']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','qcks')
G.edge['installd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','qcks')
G.edge['installd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','sdcardd')
G.edge['installd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','sdcardd')
G.edge['installd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','ueventd')
G.edge['installd']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','ueventd')
G.edge['installd']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','untrusteddomain')
G.edge['installd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','untrusteddomain')
G.edge['installd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('kernel','debug_interface_proxy')
G.edge['kernel']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('kernel','init_shell')
G.edge['kernel']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('kernel','installd')
G.edge['kernel']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open]'
G.add_edge('kernel','mobexdaemon')
G.edge['kernel']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('kernel','qcks')
G.edge['kernel']['qcks']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('kernel','sdcardd')
G.edge['kernel']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('kernel','ueventd')
G.edge['kernel']['ueventd']['write-read'] = '[relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open]'
G.add_edge('kernel','untrusteddomain')
G.edge['kernel']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('kernel','debug_interface_proxy')
G.edge['kernel']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('kernel','init_shell')
G.edge['kernel']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('kernel','installd')
G.edge['kernel']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('kernel','mobexdaemon')
G.edge['kernel']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('kernel','qcks')
G.edge['kernel']['qcks']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('kernel','sdcardd')
G.edge['kernel']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('kernel','ueventd')
G.edge['kernel']['ueventd']['write-read'] = '[relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr]'
G.add_edge('kernel','untrusteddomain')
G.edge['kernel']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('kernel','debug_interface_proxy')
G.edge['kernel']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['kernel']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('kernel','init_shell')
G.edge['kernel']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['kernel']['init_shell']['fill'] = 'red'
G.add_edge('kernel','installd')
G.edge['kernel']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['kernel']['installd']['fill'] = 'red'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read]'
G.edge['kernel']['kernel']['fill'] = 'red'
G.add_edge('kernel','mobexdaemon')
G.edge['kernel']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['kernel']['mobexdaemon']['fill'] = 'red'
G.add_edge('kernel','qcks')
G.edge['kernel']['qcks']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['kernel']['qcks']['fill'] = 'red'
G.add_edge('kernel','sdcardd')
G.edge['kernel']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['kernel']['sdcardd']['fill'] = 'red'
G.add_edge('kernel','ueventd')
G.edge['kernel']['ueventd']['write-read'] = '[relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read]'
G.edge['kernel']['ueventd']['fill'] = 'red'
G.add_edge('kernel','untrusteddomain')
G.edge['kernel']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['kernel']['untrusteddomain']['fill'] = 'red'
G.add_edge('kernel','debug_interface_proxy')
G.edge['kernel']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('kernel','debug_interface_proxy')
G.edge['kernel']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('kernel','init_shell')
G.edge['kernel']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('kernel','init_shell')
G.edge['kernel']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('kernel','installd')
G.edge['kernel']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('kernel','installd')
G.edge['kernel']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('kernel','mobexdaemon')
G.edge['kernel']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('kernel','mobexdaemon')
G.edge['kernel']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('kernel','qcks')
G.edge['kernel']['qcks']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('kernel','qcks')
G.edge['kernel']['qcks']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('kernel','sdcardd')
G.edge['kernel']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('kernel','sdcardd')
G.edge['kernel']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('kernel','ueventd')
G.edge['kernel']['ueventd']['write-read'] = '[relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search]'
G.add_edge('kernel','ueventd')
G.edge['kernel']['ueventd']['write-read'] = '[relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('kernel','untrusteddomain')
G.edge['kernel']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('kernel','untrusteddomain')
G.edge['kernel']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mobexdaemon','debug_interface_proxy')
G.edge['mobexdaemon']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mobexdaemon','init_shell')
G.edge['mobexdaemon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mobexdaemon','installd')
G.edge['mobexdaemon']['installd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mobexdaemon','kernel')
G.edge['mobexdaemon']['kernel']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('mobexdaemon','mobexdaemon')
G.edge['mobexdaemon']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mobexdaemon','qcks')
G.edge['mobexdaemon']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mobexdaemon','sdcardd')
G.edge['mobexdaemon']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mobexdaemon','ueventd')
G.edge['mobexdaemon']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('mobexdaemon','untrusteddomain')
G.edge['mobexdaemon']['untrusteddomain']['write-read'] = '[write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mobexdaemon','debug_interface_proxy')
G.edge['mobexdaemon']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mobexdaemon','init_shell')
G.edge['mobexdaemon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mobexdaemon','installd')
G.edge['mobexdaemon']['installd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mobexdaemon','mobexdaemon')
G.edge['mobexdaemon']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mobexdaemon','qcks')
G.edge['mobexdaemon']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mobexdaemon','sdcardd')
G.edge['mobexdaemon']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mobexdaemon','ueventd')
G.edge['mobexdaemon']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mobexdaemon','untrusteddomain')
G.edge['mobexdaemon']['untrusteddomain']['write-read'] = '[write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mobexdaemon','debug_interface_proxy')
G.edge['mobexdaemon']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mobexdaemon']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('mobexdaemon','init_shell')
G.edge['mobexdaemon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mobexdaemon']['init_shell']['fill'] = 'red'
G.add_edge('mobexdaemon','installd')
G.edge['mobexdaemon']['installd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mobexdaemon']['installd']['fill'] = 'red'
G.add_edge('mobexdaemon','kernel')
G.edge['mobexdaemon']['kernel']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['mobexdaemon']['kernel']['fill'] = 'red'
G.add_edge('mobexdaemon','mobexdaemon')
G.edge['mobexdaemon']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mobexdaemon']['mobexdaemon']['fill'] = 'red'
G.add_edge('mobexdaemon','qcks')
G.edge['mobexdaemon']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mobexdaemon']['qcks']['fill'] = 'red'
G.add_edge('mobexdaemon','sdcardd')
G.edge['mobexdaemon']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mobexdaemon']['sdcardd']['fill'] = 'red'
G.add_edge('mobexdaemon','ueventd')
G.edge['mobexdaemon']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mobexdaemon']['ueventd']['fill'] = 'red'
G.add_edge('mobexdaemon','untrusteddomain')
G.edge['mobexdaemon']['untrusteddomain']['write-read'] = '[write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mobexdaemon']['untrusteddomain']['fill'] = 'red'
G.add_edge('mobexdaemon','debug_interface_proxy')
G.edge['mobexdaemon']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('mobexdaemon','debug_interface_proxy')
G.edge['mobexdaemon']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mobexdaemon','init_shell')
G.edge['mobexdaemon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('mobexdaemon','init_shell')
G.edge['mobexdaemon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mobexdaemon','installd')
G.edge['mobexdaemon']['installd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('mobexdaemon','installd')
G.edge['mobexdaemon']['installd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mobexdaemon','kernel')
G.edge['mobexdaemon']['kernel']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('mobexdaemon','kernel')
G.edge['mobexdaemon']['kernel']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('mobexdaemon','mobexdaemon')
G.edge['mobexdaemon']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('mobexdaemon','mobexdaemon')
G.edge['mobexdaemon']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mobexdaemon','qcks')
G.edge['mobexdaemon']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('mobexdaemon','qcks')
G.edge['mobexdaemon']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mobexdaemon','sdcardd')
G.edge['mobexdaemon']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('mobexdaemon','sdcardd')
G.edge['mobexdaemon']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mobexdaemon','ueventd')
G.edge['mobexdaemon']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('mobexdaemon','ueventd')
G.edge['mobexdaemon']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mobexdaemon','untrusteddomain')
G.edge['mobexdaemon']['untrusteddomain']['write-read'] = '[write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('mobexdaemon','untrusteddomain')
G.edge['mobexdaemon']['untrusteddomain']['write-read'] = '[write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qcks','debug_interface_proxy')
G.edge['qcks']['debug_interface_proxy']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('qcks','init_shell')
G.edge['qcks']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('qcks','installd')
G.edge['qcks']['installd']['write-read'] = '[open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('qcks','kernel')
G.edge['qcks']['kernel']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('qcks','mobexdaemon')
G.edge['qcks']['mobexdaemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open][write read][add_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('qcks','sdcardd')
G.edge['qcks']['sdcardd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('qcks','ueventd')
G.edge['qcks']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('qcks','untrusteddomain')
G.edge['qcks']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('qcks','debug_interface_proxy')
G.edge['qcks']['debug_interface_proxy']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('qcks','init_shell')
G.edge['qcks']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('qcks','installd')
G.edge['qcks']['installd']['write-read'] = '[open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('qcks','mobexdaemon')
G.edge['qcks']['mobexdaemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open][write read][add_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('qcks','sdcardd')
G.edge['qcks']['sdcardd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('qcks','ueventd')
G.edge['qcks']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('qcks','untrusteddomain')
G.edge['qcks']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('qcks','debug_interface_proxy')
G.edge['qcks']['debug_interface_proxy']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['qcks']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('qcks','init_shell')
G.edge['qcks']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['qcks']['init_shell']['fill'] = 'red'
G.add_edge('qcks','installd')
G.edge['qcks']['installd']['write-read'] = '[open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['qcks']['installd']['fill'] = 'red'
G.add_edge('qcks','kernel')
G.edge['qcks']['kernel']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['qcks']['kernel']['fill'] = 'red'
G.add_edge('qcks','mobexdaemon')
G.edge['qcks']['mobexdaemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['qcks']['mobexdaemon']['fill'] = 'red'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open][write read][add_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['qcks']['qcks']['fill'] = 'red'
G.add_edge('qcks','sdcardd')
G.edge['qcks']['sdcardd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['qcks']['sdcardd']['fill'] = 'red'
G.add_edge('qcks','ueventd')
G.edge['qcks']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['qcks']['ueventd']['fill'] = 'red'
G.add_edge('qcks','untrusteddomain')
G.edge['qcks']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['qcks']['untrusteddomain']['fill'] = 'red'
G.add_edge('qcks','debug_interface_proxy')
G.edge['qcks']['debug_interface_proxy']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('qcks','debug_interface_proxy')
G.edge['qcks']['debug_interface_proxy']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qcks','init_shell')
G.edge['qcks']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('qcks','init_shell')
G.edge['qcks']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qcks','installd')
G.edge['qcks']['installd']['write-read'] = '[open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('qcks','installd')
G.edge['qcks']['installd']['write-read'] = '[open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qcks','kernel')
G.edge['qcks']['kernel']['write-read'] = '[open open][write read][append read][open open][write read][add_name search]'
G.add_edge('qcks','kernel')
G.edge['qcks']['kernel']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('qcks','mobexdaemon')
G.edge['qcks']['mobexdaemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('qcks','mobexdaemon')
G.edge['qcks']['mobexdaemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open][write read][add_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open][write read][add_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qcks','sdcardd')
G.edge['qcks']['sdcardd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('qcks','sdcardd')
G.edge['qcks']['sdcardd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qcks','ueventd')
G.edge['qcks']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('qcks','ueventd')
G.edge['qcks']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qcks','untrusteddomain')
G.edge['qcks']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('qcks','untrusteddomain')
G.edge['qcks']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','debug_interface_proxy')
G.edge['sdcardd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('sdcardd','init_shell')
G.edge['sdcardd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('sdcardd','installd')
G.edge['sdcardd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('sdcardd','kernel')
G.edge['sdcardd']['kernel']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('sdcardd','mobexdaemon')
G.edge['sdcardd']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('sdcardd','qcks')
G.edge['sdcardd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('sdcardd','sdcardd')
G.edge['sdcardd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('sdcardd','ueventd')
G.edge['sdcardd']['ueventd']['write-read'] = '[write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][open open]'
G.add_edge('sdcardd','untrusteddomain')
G.edge['sdcardd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('sdcardd','debug_interface_proxy')
G.edge['sdcardd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('sdcardd','init_shell')
G.edge['sdcardd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('sdcardd','installd')
G.edge['sdcardd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('sdcardd','mobexdaemon')
G.edge['sdcardd']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('sdcardd','qcks')
G.edge['sdcardd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('sdcardd','sdcardd')
G.edge['sdcardd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('sdcardd','ueventd')
G.edge['sdcardd']['ueventd']['write-read'] = '[write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr]'
G.add_edge('sdcardd','untrusteddomain')
G.edge['sdcardd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('sdcardd','debug_interface_proxy')
G.edge['sdcardd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['sdcardd']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('sdcardd','init_shell')
G.edge['sdcardd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['sdcardd']['init_shell']['fill'] = 'red'
G.add_edge('sdcardd','installd')
G.edge['sdcardd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['sdcardd']['installd']['fill'] = 'red'
G.add_edge('sdcardd','kernel')
G.edge['sdcardd']['kernel']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['sdcardd']['kernel']['fill'] = 'red'
G.add_edge('sdcardd','mobexdaemon')
G.edge['sdcardd']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['sdcardd']['mobexdaemon']['fill'] = 'red'
G.add_edge('sdcardd','qcks')
G.edge['sdcardd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['sdcardd']['qcks']['fill'] = 'red'
G.add_edge('sdcardd','sdcardd')
G.edge['sdcardd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['sdcardd']['sdcardd']['fill'] = 'red'
G.add_edge('sdcardd','ueventd')
G.edge['sdcardd']['ueventd']['write-read'] = '[write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read]'
G.edge['sdcardd']['ueventd']['fill'] = 'red'
G.add_edge('sdcardd','untrusteddomain')
G.edge['sdcardd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['sdcardd']['untrusteddomain']['fill'] = 'red'
G.add_edge('sdcardd','debug_interface_proxy')
G.edge['sdcardd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','debug_interface_proxy')
G.edge['sdcardd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','init_shell')
G.edge['sdcardd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','init_shell')
G.edge['sdcardd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','installd')
G.edge['sdcardd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','installd')
G.edge['sdcardd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','kernel')
G.edge['sdcardd']['kernel']['write-read'] = '[open open][write read][append read][open open][write read][add_name search]'
G.add_edge('sdcardd','kernel')
G.edge['sdcardd']['kernel']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','mobexdaemon')
G.edge['sdcardd']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','mobexdaemon')
G.edge['sdcardd']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','qcks')
G.edge['sdcardd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','qcks')
G.edge['sdcardd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','sdcardd')
G.edge['sdcardd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','sdcardd')
G.edge['sdcardd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','ueventd')
G.edge['sdcardd']['ueventd']['write-read'] = '[write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','ueventd')
G.edge['sdcardd']['ueventd']['write-read'] = '[write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','untrusteddomain')
G.edge['sdcardd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','untrusteddomain')
G.edge['sdcardd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ueventd','debug_interface_proxy')
G.edge['ueventd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ueventd','init_shell')
G.edge['ueventd']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ueventd','installd')
G.edge['ueventd']['installd']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ueventd','kernel')
G.edge['ueventd']['kernel']['write-read'] = '[relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][open open][write read][append read][open open]'
G.add_edge('ueventd','mobexdaemon')
G.edge['ueventd']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ueventd','qcks')
G.edge['ueventd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('ueventd','sdcardd')
G.edge['ueventd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][relabelto relabelfrom][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][write read][append read][open open]'
G.add_edge('ueventd','untrusteddomain')
G.edge['ueventd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('ueventd','debug_interface_proxy')
G.edge['ueventd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ueventd','init_shell')
G.edge['ueventd']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ueventd','installd')
G.edge['ueventd']['installd']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ueventd','mobexdaemon')
G.edge['ueventd']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ueventd','qcks')
G.edge['ueventd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('ueventd','sdcardd')
G.edge['ueventd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][relabelto relabelfrom][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr]'
G.add_edge('ueventd','untrusteddomain')
G.edge['ueventd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ueventd','debug_interface_proxy')
G.edge['ueventd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ueventd']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('ueventd','init_shell')
G.edge['ueventd']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ueventd']['init_shell']['fill'] = 'red'
G.add_edge('ueventd','installd')
G.edge['ueventd']['installd']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ueventd']['installd']['fill'] = 'red'
G.add_edge('ueventd','kernel')
G.edge['ueventd']['kernel']['write-read'] = '[relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][open open][write read][append read][open open][write read]'
G.edge['ueventd']['kernel']['fill'] = 'red'
G.add_edge('ueventd','mobexdaemon')
G.edge['ueventd']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ueventd']['mobexdaemon']['fill'] = 'red'
G.add_edge('ueventd','qcks')
G.edge['ueventd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['ueventd']['qcks']['fill'] = 'red'
G.add_edge('ueventd','sdcardd')
G.edge['ueventd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ueventd']['sdcardd']['fill'] = 'red'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][relabelto relabelfrom][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['ueventd']['ueventd']['fill'] = 'red'
G.add_edge('ueventd','untrusteddomain')
G.edge['ueventd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ueventd']['untrusteddomain']['fill'] = 'red'
G.add_edge('ueventd','debug_interface_proxy')
G.edge['ueventd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('ueventd','debug_interface_proxy')
G.edge['ueventd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ueventd','init_shell')
G.edge['ueventd']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('ueventd','init_shell')
G.edge['ueventd']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ueventd','installd')
G.edge['ueventd']['installd']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('ueventd','installd')
G.edge['ueventd']['installd']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ueventd','kernel')
G.edge['ueventd']['kernel']['write-read'] = '[relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('ueventd','kernel')
G.edge['ueventd']['kernel']['write-read'] = '[relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('ueventd','mobexdaemon')
G.edge['ueventd']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('ueventd','mobexdaemon')
G.edge['ueventd']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ueventd','qcks')
G.edge['ueventd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('ueventd','qcks')
G.edge['ueventd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ueventd','sdcardd')
G.edge['ueventd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('ueventd','sdcardd')
G.edge['ueventd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][relabelto relabelfrom][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][relabelto relabelfrom][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ueventd','untrusteddomain')
G.edge['ueventd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('ueventd','untrusteddomain')
G.edge['ueventd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('untrusteddomain','debug_interface_proxy')
G.edge['untrusteddomain']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusteddomain','init_shell')
G.edge['untrusteddomain']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusteddomain','installd')
G.edge['untrusteddomain']['installd']['write-read'] = '[setattr getattr][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusteddomain','kernel')
G.edge['untrusteddomain']['kernel']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('untrusteddomain','mobexdaemon')
G.edge['untrusteddomain']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusteddomain','qcks')
G.edge['untrusteddomain']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusteddomain','sdcardd')
G.edge['untrusteddomain']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusteddomain','ueventd')
G.edge['untrusteddomain']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('untrusteddomain','debug_interface_proxy')
G.edge['untrusteddomain']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('untrusteddomain','init_shell')
G.edge['untrusteddomain']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('untrusteddomain','installd')
G.edge['untrusteddomain']['installd']['write-read'] = '[setattr getattr][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('untrusteddomain','mobexdaemon')
G.edge['untrusteddomain']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('untrusteddomain','qcks')
G.edge['untrusteddomain']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('untrusteddomain','sdcardd')
G.edge['untrusteddomain']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('untrusteddomain','ueventd')
G.edge['untrusteddomain']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('untrusteddomain','debug_interface_proxy')
G.edge['untrusteddomain']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('untrusteddomain','init_shell')
G.edge['untrusteddomain']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['init_shell']['fill'] = 'red'
G.add_edge('untrusteddomain','installd')
G.edge['untrusteddomain']['installd']['write-read'] = '[setattr getattr][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['installd']['fill'] = 'red'
G.add_edge('untrusteddomain','kernel')
G.edge['untrusteddomain']['kernel']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['untrusteddomain']['kernel']['fill'] = 'red'
G.add_edge('untrusteddomain','mobexdaemon')
G.edge['untrusteddomain']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['mobexdaemon']['fill'] = 'red'
G.add_edge('untrusteddomain','qcks')
G.edge['untrusteddomain']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['qcks']['fill'] = 'red'
G.add_edge('untrusteddomain','sdcardd')
G.edge['untrusteddomain']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['sdcardd']['fill'] = 'red'
G.add_edge('untrusteddomain','ueventd')
G.edge['untrusteddomain']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['ueventd']['fill'] = 'red'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['untrusteddomain']['fill'] = 'red'
G.add_edge('untrusteddomain','debug_interface_proxy')
G.edge['untrusteddomain']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('untrusteddomain','debug_interface_proxy')
G.edge['untrusteddomain']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('untrusteddomain','init_shell')
G.edge['untrusteddomain']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('untrusteddomain','init_shell')
G.edge['untrusteddomain']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('untrusteddomain','installd')
G.edge['untrusteddomain']['installd']['write-read'] = '[setattr getattr][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('untrusteddomain','installd')
G.edge['untrusteddomain']['installd']['write-read'] = '[setattr getattr][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('untrusteddomain','kernel')
G.edge['untrusteddomain']['kernel']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('untrusteddomain','kernel')
G.edge['untrusteddomain']['kernel']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('untrusteddomain','mobexdaemon')
G.edge['untrusteddomain']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('untrusteddomain','mobexdaemon')
G.edge['untrusteddomain']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('untrusteddomain','qcks')
G.edge['untrusteddomain']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('untrusteddomain','qcks')
G.edge['untrusteddomain']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('untrusteddomain','sdcardd')
G.edge['untrusteddomain']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('untrusteddomain','sdcardd')
G.edge['untrusteddomain']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('untrusteddomain','ueventd')
G.edge['untrusteddomain']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('untrusteddomain','ueventd')
G.edge['untrusteddomain']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()