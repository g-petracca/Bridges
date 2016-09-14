import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('ATFWD-daemon','ATFWD-daemon')
G.edge['ATFWD-daemon']['ATFWD-daemon']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('ATFWD-daemon','cnd')
G.edge['ATFWD-daemon']['cnd']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('ATFWD-daemon','dpmd')
G.edge['ATFWD-daemon']['dpmd']['write-read'] = '[open open]'
G.add_edge('ATFWD-daemon','netmgrd')
G.edge['ATFWD-daemon']['netmgrd']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('ATFWD-daemon','qmiproxy')
G.edge['ATFWD-daemon']['qmiproxy']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('ATFWD-daemon','qmuxd')
G.edge['ATFWD-daemon']['qmuxd']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('ATFWD-daemon','radio')
G.edge['ATFWD-daemon']['radio']['write-read'] = '[open open]'
G.add_edge('ATFWD-daemon','rild')
G.edge['ATFWD-daemon']['rild']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('ATFWD-daemon','system_server')
G.edge['ATFWD-daemon']['system_server']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('ATFWD-daemon','thermald')
G.edge['ATFWD-daemon']['thermald']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('ATFWD-daemon','untrusteddomain')
G.edge['ATFWD-daemon']['untrusteddomain']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('ATFWD-daemon','ATFWD-daemon')
G.edge['ATFWD-daemon']['ATFWD-daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ATFWD-daemon','cnd')
G.edge['ATFWD-daemon']['cnd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ATFWD-daemon','dpmd')
G.edge['ATFWD-daemon']['dpmd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ATFWD-daemon','ime_app')
G.edge['ATFWD-daemon']['ime_app']['write-read'] = '[add_name search][setattr getattr]'
G.add_edge('ATFWD-daemon','netmgrd')
G.edge['ATFWD-daemon']['netmgrd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ATFWD-daemon','qmiproxy')
G.edge['ATFWD-daemon']['qmiproxy']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ATFWD-daemon','qmuxd')
G.edge['ATFWD-daemon']['qmuxd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ATFWD-daemon','radio')
G.edge['ATFWD-daemon']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ATFWD-daemon','rild')
G.edge['ATFWD-daemon']['rild']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ATFWD-daemon','sec-ril')
G.edge['ATFWD-daemon']['sec-ril']['write-read'] = '[add_name search][setattr getattr]'
G.add_edge('ATFWD-daemon','s_system_app')
G.edge['ATFWD-daemon']['s_system_app']['write-read'] = '[add_name search][setattr getattr]'
G.add_edge('ATFWD-daemon','system_app')
G.edge['ATFWD-daemon']['system_app']['write-read'] = '[add_name search][setattr getattr]'
G.add_edge('ATFWD-daemon','system_server')
G.edge['ATFWD-daemon']['system_server']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ATFWD-daemon','thermald')
G.edge['ATFWD-daemon']['thermald']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ATFWD-daemon','untrusteddomain')
G.edge['ATFWD-daemon']['untrusteddomain']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ATFWD-daemon','ATFWD-daemon')
G.edge['ATFWD-daemon']['ATFWD-daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ATFWD-daemon']['ATFWD-daemon']['fill'] = 'red'
G.add_edge('ATFWD-daemon','ATFWD-daemon')
G.edge['ATFWD-daemon']['ATFWD-daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ATFWD-daemon','cnd')
G.edge['ATFWD-daemon']['cnd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ATFWD-daemon']['cnd']['fill'] = 'red'
G.add_edge('ATFWD-daemon','cnd')
G.edge['ATFWD-daemon']['cnd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ATFWD-daemon','dpmd')
G.edge['ATFWD-daemon']['dpmd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ATFWD-daemon']['dpmd']['fill'] = 'red'
G.add_edge('ATFWD-daemon','dpmd')
G.edge['ATFWD-daemon']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('ATFWD-daemon','ime_app')
G.edge['ATFWD-daemon']['ime_app']['write-read'] = '[add_name search][setattr getattr][write read]'
G.edge['ATFWD-daemon']['ime_app']['fill'] = 'red'
G.add_edge('ATFWD-daemon','netmgrd')
G.edge['ATFWD-daemon']['netmgrd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ATFWD-daemon']['netmgrd']['fill'] = 'red'
G.add_edge('ATFWD-daemon','netmgrd')
G.edge['ATFWD-daemon']['netmgrd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ATFWD-daemon','qmiproxy')
G.edge['ATFWD-daemon']['qmiproxy']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ATFWD-daemon']['qmiproxy']['fill'] = 'red'
G.add_edge('ATFWD-daemon','qmiproxy')
G.edge['ATFWD-daemon']['qmiproxy']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ATFWD-daemon','qmuxd')
G.edge['ATFWD-daemon']['qmuxd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ATFWD-daemon']['qmuxd']['fill'] = 'red'
G.add_edge('ATFWD-daemon','qmuxd')
G.edge['ATFWD-daemon']['qmuxd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ATFWD-daemon','radio')
G.edge['ATFWD-daemon']['radio']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ATFWD-daemon']['radio']['fill'] = 'red'
G.add_edge('ATFWD-daemon','radio')
G.edge['ATFWD-daemon']['radio']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('ATFWD-daemon','rild')
G.edge['ATFWD-daemon']['rild']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ATFWD-daemon']['rild']['fill'] = 'red'
G.add_edge('ATFWD-daemon','rild')
G.edge['ATFWD-daemon']['rild']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ATFWD-daemon','sec-ril')
G.edge['ATFWD-daemon']['sec-ril']['write-read'] = '[add_name search][setattr getattr][write read]'
G.edge['ATFWD-daemon']['sec-ril']['fill'] = 'red'
G.add_edge('ATFWD-daemon','s_system_app')
G.edge['ATFWD-daemon']['s_system_app']['write-read'] = '[add_name search][setattr getattr][write read]'
G.edge['ATFWD-daemon']['s_system_app']['fill'] = 'red'
G.add_edge('ATFWD-daemon','system_app')
G.edge['ATFWD-daemon']['system_app']['write-read'] = '[add_name search][setattr getattr][write read]'
G.edge['ATFWD-daemon']['system_app']['fill'] = 'red'
G.add_edge('ATFWD-daemon','system_server')
G.edge['ATFWD-daemon']['system_server']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ATFWD-daemon']['system_server']['fill'] = 'red'
G.add_edge('ATFWD-daemon','system_server')
G.edge['ATFWD-daemon']['system_server']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ATFWD-daemon','thermald')
G.edge['ATFWD-daemon']['thermald']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ATFWD-daemon']['thermald']['fill'] = 'red'
G.add_edge('ATFWD-daemon','thermald')
G.edge['ATFWD-daemon']['thermald']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ATFWD-daemon','untrusteddomain')
G.edge['ATFWD-daemon']['untrusteddomain']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ATFWD-daemon']['untrusteddomain']['fill'] = 'red'
G.add_edge('ATFWD-daemon','untrusteddomain')
G.edge['ATFWD-daemon']['untrusteddomain']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('cnd','ATFWD-daemon')
G.edge['cnd']['ATFWD-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][append read][setopt getopt][setattr getattr][write read][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('cnd','dpmd')
G.edge['cnd']['dpmd']['write-read'] = '[open open]'
G.add_edge('cnd','netmgrd')
G.edge['cnd']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('cnd','qmiproxy')
G.edge['cnd']['qmiproxy']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('cnd','qmuxd')
G.edge['cnd']['qmuxd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('cnd','radio')
G.edge['cnd']['radio']['write-read'] = '[open open]'
G.add_edge('cnd','rild')
G.edge['cnd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('cnd','system_server')
G.edge['cnd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('cnd','thermald')
G.edge['cnd']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('cnd','untrusteddomain')
G.edge['cnd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('cnd','ATFWD-daemon')
G.edge['cnd']['ATFWD-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][append read][setopt getopt][setattr getattr][write read][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('cnd','dpmd')
G.edge['cnd']['dpmd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cnd','ime_app')
G.edge['cnd']['ime_app']['write-read'] = '[write read][add_name search][setattr getattr]'
G.add_edge('cnd','netmgrd')
G.edge['cnd']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('cnd','qmiproxy')
G.edge['cnd']['qmiproxy']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('cnd','qmuxd')
G.edge['cnd']['qmuxd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('cnd','radio')
G.edge['cnd']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cnd','rild')
G.edge['cnd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('cnd','sec-ril')
G.edge['cnd']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][setattr getattr]'
G.add_edge('cnd','s_system_app')
G.edge['cnd']['s_system_app']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][add_name search][remove_name search][setattr getattr]'
G.add_edge('cnd','system_app')
G.edge['cnd']['system_app']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][setattr getattr]'
G.add_edge('cnd','system_server')
G.edge['cnd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('cnd','thermald')
G.edge['cnd']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('cnd','untrusteddomain')
G.edge['cnd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('cnd','ATFWD-daemon')
G.edge['cnd']['ATFWD-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['cnd']['ATFWD-daemon']['fill'] = 'red'
G.add_edge('cnd','ATFWD-daemon')
G.edge['cnd']['ATFWD-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][append read][setopt getopt][setattr getattr][write read][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['cnd']['cnd']['fill'] = 'red'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][append read][setopt getopt][setattr getattr][write read][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('cnd','dpmd')
G.edge['cnd']['dpmd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cnd']['dpmd']['fill'] = 'red'
G.add_edge('cnd','dpmd')
G.edge['cnd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('cnd','ime_app')
G.edge['cnd']['ime_app']['write-read'] = '[write read][add_name search][setattr getattr][write read]'
G.edge['cnd']['ime_app']['fill'] = 'red'
G.add_edge('cnd','netmgrd')
G.edge['cnd']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['cnd']['netmgrd']['fill'] = 'red'
G.add_edge('cnd','netmgrd')
G.edge['cnd']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('cnd','qmiproxy')
G.edge['cnd']['qmiproxy']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['cnd']['qmiproxy']['fill'] = 'red'
G.add_edge('cnd','qmiproxy')
G.edge['cnd']['qmiproxy']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('cnd','qmuxd')
G.edge['cnd']['qmuxd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['cnd']['qmuxd']['fill'] = 'red'
G.add_edge('cnd','qmuxd')
G.edge['cnd']['qmuxd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('cnd','radio')
G.edge['cnd']['radio']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cnd']['radio']['fill'] = 'red'
G.add_edge('cnd','radio')
G.edge['cnd']['radio']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('cnd','rild')
G.edge['cnd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['cnd']['rild']['fill'] = 'red'
G.add_edge('cnd','rild')
G.edge['cnd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('cnd','sec-ril')
G.edge['cnd']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][setattr getattr][write read]'
G.edge['cnd']['sec-ril']['fill'] = 'red'
G.add_edge('cnd','s_system_app')
G.edge['cnd']['s_system_app']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][add_name search][remove_name search][setattr getattr][write read]'
G.edge['cnd']['s_system_app']['fill'] = 'red'
G.add_edge('cnd','system_app')
G.edge['cnd']['system_app']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][setattr getattr][write read]'
G.edge['cnd']['system_app']['fill'] = 'red'
G.add_edge('cnd','system_server')
G.edge['cnd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['cnd']['system_server']['fill'] = 'red'
G.add_edge('cnd','system_server')
G.edge['cnd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('cnd','thermald')
G.edge['cnd']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['cnd']['thermald']['fill'] = 'red'
G.add_edge('cnd','thermald')
G.edge['cnd']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('cnd','untrusteddomain')
G.edge['cnd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['cnd']['untrusteddomain']['fill'] = 'red'
G.add_edge('cnd','untrusteddomain')
G.edge['cnd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('dpmd','ATFWD-daemon')
G.edge['dpmd']['ATFWD-daemon']['write-read'] = '[open open]'
G.add_edge('dpmd','cnd')
G.edge['dpmd']['cnd']['write-read'] = '[open open][append read][open open]'
G.add_edge('dpmd','dpmd')
G.edge['dpmd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('dpmd','netmgrd')
G.edge['dpmd']['netmgrd']['write-read'] = '[open open]'
G.add_edge('dpmd','qmiproxy')
G.edge['dpmd']['qmiproxy']['write-read'] = '[open open]'
G.add_edge('dpmd','qmuxd')
G.edge['dpmd']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open]'
G.add_edge('dpmd','radio')
G.edge['dpmd']['radio']['write-read'] = '[open open]'
G.add_edge('dpmd','rild')
G.edge['dpmd']['rild']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('dpmd','system_server')
G.edge['dpmd']['system_server']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('dpmd','thermald')
G.edge['dpmd']['thermald']['write-read'] = '[open open]'
G.add_edge('dpmd','untrusteddomain')
G.edge['dpmd']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('dpmd','ATFWD-daemon')
G.edge['dpmd']['ATFWD-daemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dpmd','cnd')
G.edge['dpmd']['cnd']['write-read'] = '[open open][append read][open open][setattr getattr]'
G.add_edge('dpmd','dpmd')
G.edge['dpmd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('dpmd','ime_app')
G.edge['dpmd']['ime_app']['write-read'] = '[setattr getattr]'
G.add_edge('dpmd','netmgrd')
G.edge['dpmd']['netmgrd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dpmd','qmiproxy')
G.edge['dpmd']['qmiproxy']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dpmd','qmuxd')
G.edge['dpmd']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open][setattr getattr]'
G.add_edge('dpmd','radio')
G.edge['dpmd']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dpmd','rild')
G.edge['dpmd']['rild']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('dpmd','sec-ril')
G.edge['dpmd']['sec-ril']['write-read'] = '[open open][write read][setattr getattr]'
G.add_edge('dpmd','s_system_app')
G.edge['dpmd']['s_system_app']['write-read'] = '[setattr getattr]'
G.add_edge('dpmd','system_app')
G.edge['dpmd']['system_app']['write-read'] = '[setattr getattr]'
G.add_edge('dpmd','system_server')
G.edge['dpmd']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('dpmd','thermald')
G.edge['dpmd']['thermald']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dpmd','untrusteddomain')
G.edge['dpmd']['untrusteddomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dpmd','ATFWD-daemon')
G.edge['dpmd']['ATFWD-daemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dpmd']['ATFWD-daemon']['fill'] = 'red'
G.add_edge('dpmd','ATFWD-daemon')
G.edge['dpmd']['ATFWD-daemon']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('dpmd','cnd')
G.edge['dpmd']['cnd']['write-read'] = '[open open][append read][open open][setattr getattr][write read]'
G.edge['dpmd']['cnd']['fill'] = 'red'
G.add_edge('dpmd','cnd')
G.edge['dpmd']['cnd']['write-read'] = '[open open][append read][open open][setattr getattr][write read][append read]'
G.add_edge('dpmd','dpmd')
G.edge['dpmd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['dpmd']['dpmd']['fill'] = 'red'
G.add_edge('dpmd','dpmd')
G.edge['dpmd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('dpmd','ime_app')
G.edge['dpmd']['ime_app']['write-read'] = '[setattr getattr][write read]'
G.edge['dpmd']['ime_app']['fill'] = 'red'
G.add_edge('dpmd','netmgrd')
G.edge['dpmd']['netmgrd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dpmd']['netmgrd']['fill'] = 'red'
G.add_edge('dpmd','netmgrd')
G.edge['dpmd']['netmgrd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('dpmd','qmiproxy')
G.edge['dpmd']['qmiproxy']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dpmd']['qmiproxy']['fill'] = 'red'
G.add_edge('dpmd','qmiproxy')
G.edge['dpmd']['qmiproxy']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('dpmd','qmuxd')
G.edge['dpmd']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open][setattr getattr][write read]'
G.edge['dpmd']['qmuxd']['fill'] = 'red'
G.add_edge('dpmd','qmuxd')
G.edge['dpmd']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('dpmd','radio')
G.edge['dpmd']['radio']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dpmd']['radio']['fill'] = 'red'
G.add_edge('dpmd','radio')
G.edge['dpmd']['radio']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('dpmd','rild')
G.edge['dpmd']['rild']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['dpmd']['rild']['fill'] = 'red'
G.add_edge('dpmd','rild')
G.edge['dpmd']['rild']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('dpmd','sec-ril')
G.edge['dpmd']['sec-ril']['write-read'] = '[open open][write read][setattr getattr][write read]'
G.edge['dpmd']['sec-ril']['fill'] = 'red'
G.add_edge('dpmd','s_system_app')
G.edge['dpmd']['s_system_app']['write-read'] = '[setattr getattr][write read]'
G.edge['dpmd']['s_system_app']['fill'] = 'red'
G.add_edge('dpmd','system_app')
G.edge['dpmd']['system_app']['write-read'] = '[setattr getattr][write read]'
G.edge['dpmd']['system_app']['fill'] = 'red'
G.add_edge('dpmd','system_server')
G.edge['dpmd']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['dpmd']['system_server']['fill'] = 'red'
G.add_edge('dpmd','system_server')
G.edge['dpmd']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('dpmd','thermald')
G.edge['dpmd']['thermald']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dpmd']['thermald']['fill'] = 'red'
G.add_edge('dpmd','thermald')
G.edge['dpmd']['thermald']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('dpmd','untrusteddomain')
G.edge['dpmd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dpmd']['untrusteddomain']['fill'] = 'red'
G.add_edge('dpmd','untrusteddomain')
G.edge['dpmd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('netmgrd','ATFWD-daemon')
G.edge['netmgrd']['ATFWD-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('netmgrd','cnd')
G.edge['netmgrd']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('netmgrd','dpmd')
G.edge['netmgrd']['dpmd']['write-read'] = '[open open]'
G.add_edge('netmgrd','netmgrd')
G.edge['netmgrd']['netmgrd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('netmgrd','qmiproxy')
G.edge['netmgrd']['qmiproxy']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('netmgrd','qmuxd')
G.edge['netmgrd']['qmuxd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('netmgrd','radio')
G.edge['netmgrd']['radio']['write-read'] = '[open open]'
G.add_edge('netmgrd','rild')
G.edge['netmgrd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netmgrd','system_server')
G.edge['netmgrd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netmgrd','thermald')
G.edge['netmgrd']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('netmgrd','untrusteddomain')
G.edge['netmgrd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netmgrd','ATFWD-daemon')
G.edge['netmgrd']['ATFWD-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('netmgrd','cnd')
G.edge['netmgrd']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('netmgrd','dpmd')
G.edge['netmgrd']['dpmd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('netmgrd','ime_app')
G.edge['netmgrd']['ime_app']['write-read'] = '[write read][add_name search][setattr getattr]'
G.add_edge('netmgrd','netmgrd')
G.edge['netmgrd']['netmgrd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('netmgrd','qmiproxy')
G.edge['netmgrd']['qmiproxy']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('netmgrd','qmuxd')
G.edge['netmgrd']['qmuxd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('netmgrd','radio')
G.edge['netmgrd']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('netmgrd','rild')
G.edge['netmgrd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('netmgrd','sec-ril')
G.edge['netmgrd']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('netmgrd','s_system_app')
G.edge['netmgrd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('netmgrd','system_app')
G.edge['netmgrd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][setattr getattr]'
G.add_edge('netmgrd','system_server')
G.edge['netmgrd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('netmgrd','thermald')
G.edge['netmgrd']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('netmgrd','untrusteddomain')
G.edge['netmgrd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('netmgrd','ATFWD-daemon')
G.edge['netmgrd']['ATFWD-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['netmgrd']['ATFWD-daemon']['fill'] = 'red'
G.add_edge('netmgrd','ATFWD-daemon')
G.edge['netmgrd']['ATFWD-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('netmgrd','cnd')
G.edge['netmgrd']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['netmgrd']['cnd']['fill'] = 'red'
G.add_edge('netmgrd','cnd')
G.edge['netmgrd']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('netmgrd','dpmd')
G.edge['netmgrd']['dpmd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['netmgrd']['dpmd']['fill'] = 'red'
G.add_edge('netmgrd','dpmd')
G.edge['netmgrd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('netmgrd','ime_app')
G.edge['netmgrd']['ime_app']['write-read'] = '[write read][add_name search][setattr getattr][write read]'
G.edge['netmgrd']['ime_app']['fill'] = 'red'
G.add_edge('netmgrd','netmgrd')
G.edge['netmgrd']['netmgrd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['netmgrd']['netmgrd']['fill'] = 'red'
G.add_edge('netmgrd','netmgrd')
G.edge['netmgrd']['netmgrd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('netmgrd','qmiproxy')
G.edge['netmgrd']['qmiproxy']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['netmgrd']['qmiproxy']['fill'] = 'red'
G.add_edge('netmgrd','qmiproxy')
G.edge['netmgrd']['qmiproxy']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('netmgrd','qmuxd')
G.edge['netmgrd']['qmuxd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['netmgrd']['qmuxd']['fill'] = 'red'
G.add_edge('netmgrd','qmuxd')
G.edge['netmgrd']['qmuxd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('netmgrd','radio')
G.edge['netmgrd']['radio']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['netmgrd']['radio']['fill'] = 'red'
G.add_edge('netmgrd','radio')
G.edge['netmgrd']['radio']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('netmgrd','rild')
G.edge['netmgrd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['netmgrd']['rild']['fill'] = 'red'
G.add_edge('netmgrd','rild')
G.edge['netmgrd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('netmgrd','sec-ril')
G.edge['netmgrd']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['netmgrd']['sec-ril']['fill'] = 'red'
G.add_edge('netmgrd','s_system_app')
G.edge['netmgrd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][setattr getattr][setattr getattr][setattr getattr][write read]'
G.edge['netmgrd']['s_system_app']['fill'] = 'red'
G.add_edge('netmgrd','system_app')
G.edge['netmgrd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][setattr getattr][write read]'
G.edge['netmgrd']['system_app']['fill'] = 'red'
G.add_edge('netmgrd','system_server')
G.edge['netmgrd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['netmgrd']['system_server']['fill'] = 'red'
G.add_edge('netmgrd','system_server')
G.edge['netmgrd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('netmgrd','thermald')
G.edge['netmgrd']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['netmgrd']['thermald']['fill'] = 'red'
G.add_edge('netmgrd','thermald')
G.edge['netmgrd']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('netmgrd','untrusteddomain')
G.edge['netmgrd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['netmgrd']['untrusteddomain']['fill'] = 'red'
G.add_edge('netmgrd','untrusteddomain')
G.edge['netmgrd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('qmiproxy','ATFWD-daemon')
G.edge['qmiproxy']['ATFWD-daemon']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('qmiproxy','cnd')
G.edge['qmiproxy']['cnd']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('qmiproxy','dpmd')
G.edge['qmiproxy']['dpmd']['write-read'] = '[open open]'
G.add_edge('qmiproxy','netmgrd')
G.edge['qmiproxy']['netmgrd']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('qmiproxy','qmiproxy')
G.edge['qmiproxy']['qmiproxy']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('qmiproxy','qmuxd')
G.edge['qmiproxy']['qmuxd']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('qmiproxy','radio')
G.edge['qmiproxy']['radio']['write-read'] = '[open open]'
G.add_edge('qmiproxy','rild')
G.edge['qmiproxy']['rild']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('qmiproxy','system_server')
G.edge['qmiproxy']['system_server']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('qmiproxy','thermald')
G.edge['qmiproxy']['thermald']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('qmiproxy','untrusteddomain')
G.edge['qmiproxy']['untrusteddomain']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('qmiproxy','ATFWD-daemon')
G.edge['qmiproxy']['ATFWD-daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('qmiproxy','cnd')
G.edge['qmiproxy']['cnd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('qmiproxy','dpmd')
G.edge['qmiproxy']['dpmd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmiproxy','ime_app')
G.edge['qmiproxy']['ime_app']['write-read'] = '[add_name search][setattr getattr]'
G.add_edge('qmiproxy','netmgrd')
G.edge['qmiproxy']['netmgrd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('qmiproxy','qmiproxy')
G.edge['qmiproxy']['qmiproxy']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('qmiproxy','qmuxd')
G.edge['qmiproxy']['qmuxd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('qmiproxy','radio')
G.edge['qmiproxy']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmiproxy','rild')
G.edge['qmiproxy']['rild']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('qmiproxy','sec-ril')
G.edge['qmiproxy']['sec-ril']['write-read'] = '[add_name search][setattr getattr]'
G.add_edge('qmiproxy','s_system_app')
G.edge['qmiproxy']['s_system_app']['write-read'] = '[add_name search][setattr getattr]'
G.add_edge('qmiproxy','system_app')
G.edge['qmiproxy']['system_app']['write-read'] = '[add_name search][setattr getattr]'
G.add_edge('qmiproxy','system_server')
G.edge['qmiproxy']['system_server']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('qmiproxy','thermald')
G.edge['qmiproxy']['thermald']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('qmiproxy','untrusteddomain')
G.edge['qmiproxy']['untrusteddomain']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('qmiproxy','ATFWD-daemon')
G.edge['qmiproxy']['ATFWD-daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['qmiproxy']['ATFWD-daemon']['fill'] = 'red'
G.add_edge('qmiproxy','ATFWD-daemon')
G.edge['qmiproxy']['ATFWD-daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('qmiproxy','cnd')
G.edge['qmiproxy']['cnd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['qmiproxy']['cnd']['fill'] = 'red'
G.add_edge('qmiproxy','cnd')
G.edge['qmiproxy']['cnd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('qmiproxy','dpmd')
G.edge['qmiproxy']['dpmd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmiproxy']['dpmd']['fill'] = 'red'
G.add_edge('qmiproxy','dpmd')
G.edge['qmiproxy']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('qmiproxy','ime_app')
G.edge['qmiproxy']['ime_app']['write-read'] = '[add_name search][setattr getattr][write read]'
G.edge['qmiproxy']['ime_app']['fill'] = 'red'
G.add_edge('qmiproxy','netmgrd')
G.edge['qmiproxy']['netmgrd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['qmiproxy']['netmgrd']['fill'] = 'red'
G.add_edge('qmiproxy','netmgrd')
G.edge['qmiproxy']['netmgrd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('qmiproxy','qmiproxy')
G.edge['qmiproxy']['qmiproxy']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['qmiproxy']['qmiproxy']['fill'] = 'red'
G.add_edge('qmiproxy','qmiproxy')
G.edge['qmiproxy']['qmiproxy']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('qmiproxy','qmuxd')
G.edge['qmiproxy']['qmuxd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['qmiproxy']['qmuxd']['fill'] = 'red'
G.add_edge('qmiproxy','qmuxd')
G.edge['qmiproxy']['qmuxd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('qmiproxy','radio')
G.edge['qmiproxy']['radio']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmiproxy']['radio']['fill'] = 'red'
G.add_edge('qmiproxy','radio')
G.edge['qmiproxy']['radio']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('qmiproxy','rild')
G.edge['qmiproxy']['rild']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['qmiproxy']['rild']['fill'] = 'red'
G.add_edge('qmiproxy','rild')
G.edge['qmiproxy']['rild']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('qmiproxy','sec-ril')
G.edge['qmiproxy']['sec-ril']['write-read'] = '[add_name search][setattr getattr][write read]'
G.edge['qmiproxy']['sec-ril']['fill'] = 'red'
G.add_edge('qmiproxy','s_system_app')
G.edge['qmiproxy']['s_system_app']['write-read'] = '[add_name search][setattr getattr][write read]'
G.edge['qmiproxy']['s_system_app']['fill'] = 'red'
G.add_edge('qmiproxy','system_app')
G.edge['qmiproxy']['system_app']['write-read'] = '[add_name search][setattr getattr][write read]'
G.edge['qmiproxy']['system_app']['fill'] = 'red'
G.add_edge('qmiproxy','system_server')
G.edge['qmiproxy']['system_server']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['qmiproxy']['system_server']['fill'] = 'red'
G.add_edge('qmiproxy','system_server')
G.edge['qmiproxy']['system_server']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('qmiproxy','thermald')
G.edge['qmiproxy']['thermald']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['qmiproxy']['thermald']['fill'] = 'red'
G.add_edge('qmiproxy','thermald')
G.edge['qmiproxy']['thermald']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('qmiproxy','untrusteddomain')
G.edge['qmiproxy']['untrusteddomain']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['qmiproxy']['untrusteddomain']['fill'] = 'red'
G.add_edge('qmiproxy','untrusteddomain')
G.edge['qmiproxy']['untrusteddomain']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('qmuxd','ATFWD-daemon')
G.edge['qmuxd']['ATFWD-daemon']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('qmuxd','cnd')
G.edge['qmuxd']['cnd']['write-read'] = '[open open][add_name search][remove_name search][open open][append read][open open]'
G.add_edge('qmuxd','dpmd')
G.edge['qmuxd']['dpmd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('qmuxd','netmgrd')
G.edge['qmuxd']['netmgrd']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('qmuxd','qmiproxy')
G.edge['qmuxd']['qmiproxy']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('qmuxd','radio')
G.edge['qmuxd']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('qmuxd','rild')
G.edge['qmuxd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('qmuxd','system_server')
G.edge['qmuxd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('qmuxd','thermald')
G.edge['qmuxd']['thermald']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('qmuxd','untrusteddomain')
G.edge['qmuxd']['untrusteddomain']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('qmuxd','ATFWD-daemon')
G.edge['qmuxd']['ATFWD-daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('qmuxd','cnd')
G.edge['qmuxd']['cnd']['write-read'] = '[open open][add_name search][remove_name search][open open][append read][open open][setattr getattr]'
G.add_edge('qmuxd','dpmd')
G.edge['qmuxd']['dpmd']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('qmuxd','ime_app')
G.edge['qmuxd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('qmuxd','netmgrd')
G.edge['qmuxd']['netmgrd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('qmuxd','qmiproxy')
G.edge['qmuxd']['qmiproxy']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('qmuxd','radio')
G.edge['qmuxd']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('qmuxd','rild')
G.edge['qmuxd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('qmuxd','sec-ril')
G.edge['qmuxd']['sec-ril']['write-read'] = '[add_name search][open open][write read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('qmuxd','s_system_app')
G.edge['qmuxd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('qmuxd','system_app')
G.edge['qmuxd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('qmuxd','system_server')
G.edge['qmuxd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('qmuxd','thermald')
G.edge['qmuxd']['thermald']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('qmuxd','untrusteddomain')
G.edge['qmuxd']['untrusteddomain']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('qmuxd','ATFWD-daemon')
G.edge['qmuxd']['ATFWD-daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['qmuxd']['ATFWD-daemon']['fill'] = 'red'
G.add_edge('qmuxd','ATFWD-daemon')
G.edge['qmuxd']['ATFWD-daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('qmuxd','cnd')
G.edge['qmuxd']['cnd']['write-read'] = '[open open][add_name search][remove_name search][open open][append read][open open][setattr getattr][write read]'
G.edge['qmuxd']['cnd']['fill'] = 'red'
G.add_edge('qmuxd','cnd')
G.edge['qmuxd']['cnd']['write-read'] = '[open open][add_name search][remove_name search][open open][append read][open open][setattr getattr][write read][append read]'
G.add_edge('qmuxd','dpmd')
G.edge['qmuxd']['dpmd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['qmuxd']['dpmd']['fill'] = 'red'
G.add_edge('qmuxd','dpmd')
G.edge['qmuxd']['dpmd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('qmuxd','ime_app')
G.edge['qmuxd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['qmuxd']['ime_app']['fill'] = 'red'
G.add_edge('qmuxd','netmgrd')
G.edge['qmuxd']['netmgrd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['qmuxd']['netmgrd']['fill'] = 'red'
G.add_edge('qmuxd','netmgrd')
G.edge['qmuxd']['netmgrd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('qmuxd','qmiproxy')
G.edge['qmuxd']['qmiproxy']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['qmuxd']['qmiproxy']['fill'] = 'red'
G.add_edge('qmuxd','qmiproxy')
G.edge['qmuxd']['qmiproxy']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['qmuxd']['qmuxd']['fill'] = 'red'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('qmuxd','radio')
G.edge['qmuxd']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['qmuxd']['radio']['fill'] = 'red'
G.add_edge('qmuxd','radio')
G.edge['qmuxd']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('qmuxd','rild')
G.edge['qmuxd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['qmuxd']['rild']['fill'] = 'red'
G.add_edge('qmuxd','rild')
G.edge['qmuxd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('qmuxd','sec-ril')
G.edge['qmuxd']['sec-ril']['write-read'] = '[add_name search][open open][write read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['qmuxd']['sec-ril']['fill'] = 'red'
G.add_edge('qmuxd','s_system_app')
G.edge['qmuxd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][setattr getattr][write read]'
G.edge['qmuxd']['s_system_app']['fill'] = 'red'
G.add_edge('qmuxd','system_app')
G.edge['qmuxd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['qmuxd']['system_app']['fill'] = 'red'
G.add_edge('qmuxd','system_server')
G.edge['qmuxd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['qmuxd']['system_server']['fill'] = 'red'
G.add_edge('qmuxd','system_server')
G.edge['qmuxd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('qmuxd','thermald')
G.edge['qmuxd']['thermald']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['qmuxd']['thermald']['fill'] = 'red'
G.add_edge('qmuxd','thermald')
G.edge['qmuxd']['thermald']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('qmuxd','untrusteddomain')
G.edge['qmuxd']['untrusteddomain']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['qmuxd']['untrusteddomain']['fill'] = 'red'
G.add_edge('qmuxd','untrusteddomain')
G.edge['qmuxd']['untrusteddomain']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('radio','ATFWD-daemon')
G.edge['radio']['ATFWD-daemon']['write-read'] = '[open open]'
G.add_edge('radio','cnd')
G.edge['radio']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('radio','dpmd')
G.edge['radio']['dpmd']['write-read'] = '[open open]'
G.add_edge('radio','netmgrd')
G.edge['radio']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('radio','qmiproxy')
G.edge['radio']['qmiproxy']['write-read'] = '[open open]'
G.add_edge('radio','qmuxd')
G.edge['radio']['qmuxd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('radio','rild')
G.edge['radio']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('radio','system_server')
G.edge['radio']['system_server']['write-read'] = '[add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('radio','thermald')
G.edge['radio']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('radio','untrusteddomain')
G.edge['radio']['untrusteddomain']['write-read'] = '[write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('radio','ATFWD-daemon')
G.edge['radio']['ATFWD-daemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','cnd')
G.edge['radio']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('radio','dpmd')
G.edge['radio']['dpmd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','ime_app')
G.edge['radio']['ime_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr]'
G.add_edge('radio','netmgrd')
G.edge['radio']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('radio','qmiproxy')
G.edge['radio']['qmiproxy']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','qmuxd')
G.edge['radio']['qmuxd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('radio','rild')
G.edge['radio']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('radio','sec-ril')
G.edge['radio']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr]'
G.add_edge('radio','s_system_app')
G.edge['radio']['s_system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr]'
G.add_edge('radio','system_app')
G.edge['radio']['system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr]'
G.add_edge('radio','system_server')
G.edge['radio']['system_server']['write-read'] = '[add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('radio','thermald')
G.edge['radio']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('radio','untrusteddomain')
G.edge['radio']['untrusteddomain']['write-read'] = '[write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('radio','ATFWD-daemon')
G.edge['radio']['ATFWD-daemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['radio']['ATFWD-daemon']['fill'] = 'red'
G.add_edge('radio','ATFWD-daemon')
G.edge['radio']['ATFWD-daemon']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('radio','cnd')
G.edge['radio']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['radio']['cnd']['fill'] = 'red'
G.add_edge('radio','cnd')
G.edge['radio']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('radio','dpmd')
G.edge['radio']['dpmd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['radio']['dpmd']['fill'] = 'red'
G.add_edge('radio','dpmd')
G.edge['radio']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('radio','ime_app')
G.edge['radio']['ime_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read]'
G.edge['radio']['ime_app']['fill'] = 'red'
G.add_edge('radio','netmgrd')
G.edge['radio']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['radio']['netmgrd']['fill'] = 'red'
G.add_edge('radio','netmgrd')
G.edge['radio']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('radio','qmiproxy')
G.edge['radio']['qmiproxy']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['radio']['qmiproxy']['fill'] = 'red'
G.add_edge('radio','qmiproxy')
G.edge['radio']['qmiproxy']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('radio','qmuxd')
G.edge['radio']['qmuxd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['radio']['qmuxd']['fill'] = 'red'
G.add_edge('radio','qmuxd')
G.edge['radio']['qmuxd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['radio']['radio']['fill'] = 'red'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('radio','rild')
G.edge['radio']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['radio']['rild']['fill'] = 'red'
G.add_edge('radio','rild')
G.edge['radio']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('radio','sec-ril')
G.edge['radio']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read]'
G.edge['radio']['sec-ril']['fill'] = 'red'
G.add_edge('radio','s_system_app')
G.edge['radio']['s_system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read]'
G.edge['radio']['s_system_app']['fill'] = 'red'
G.add_edge('radio','system_app')
G.edge['radio']['system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read]'
G.edge['radio']['system_app']['fill'] = 'red'
G.add_edge('radio','system_server')
G.edge['radio']['system_server']['write-read'] = '[add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['radio']['system_server']['fill'] = 'red'
G.add_edge('radio','system_server')
G.edge['radio']['system_server']['write-read'] = '[add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('radio','thermald')
G.edge['radio']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['radio']['thermald']['fill'] = 'red'
G.add_edge('radio','thermald')
G.edge['radio']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('radio','untrusteddomain')
G.edge['radio']['untrusteddomain']['write-read'] = '[write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['radio']['untrusteddomain']['fill'] = 'red'
G.add_edge('radio','untrusteddomain')
G.edge['radio']['untrusteddomain']['write-read'] = '[write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('rild','ATFWD-daemon')
G.edge['rild']['ATFWD-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','cnd')
G.edge['rild']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open]'
G.add_edge('rild','dpmd')
G.edge['rild']['dpmd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('rild','netmgrd')
G.edge['rild']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('rild','qmiproxy')
G.edge['rild']['qmiproxy']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','qmuxd')
G.edge['rild']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][open open][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('rild','radio')
G.edge['rild']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('rild','thermald')
G.edge['rild']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('rild','untrusteddomain')
G.edge['rild']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('rild','ATFWD-daemon')
G.edge['rild']['ATFWD-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('rild','cnd')
G.edge['rild']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('rild','dpmd')
G.edge['rild']['dpmd']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('rild','ime_app')
G.edge['rild']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr]'
G.add_edge('rild','netmgrd')
G.edge['rild']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('rild','qmiproxy')
G.edge['rild']['qmiproxy']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('rild','qmuxd')
G.edge['rild']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][open open][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('rild','radio')
G.edge['rild']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('rild','sec-ril')
G.edge['rild']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr]'
G.add_edge('rild','s_system_app')
G.edge['rild']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr]'
G.add_edge('rild','system_app')
G.edge['rild']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('rild','thermald')
G.edge['rild']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('rild','untrusteddomain')
G.edge['rild']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('rild','ATFWD-daemon')
G.edge['rild']['ATFWD-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['rild']['ATFWD-daemon']['fill'] = 'red'
G.add_edge('rild','ATFWD-daemon')
G.edge['rild']['ATFWD-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('rild','cnd')
G.edge['rild']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['cnd']['fill'] = 'red'
G.add_edge('rild','cnd')
G.edge['rild']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('rild','dpmd')
G.edge['rild']['dpmd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['dpmd']['fill'] = 'red'
G.add_edge('rild','dpmd')
G.edge['rild']['dpmd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('rild','ime_app')
G.edge['rild']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read]'
G.edge['rild']['ime_app']['fill'] = 'red'
G.add_edge('rild','netmgrd')
G.edge['rild']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['rild']['netmgrd']['fill'] = 'red'
G.add_edge('rild','netmgrd')
G.edge['rild']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('rild','qmiproxy')
G.edge['rild']['qmiproxy']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['rild']['qmiproxy']['fill'] = 'red'
G.add_edge('rild','qmiproxy')
G.edge['rild']['qmiproxy']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('rild','qmuxd')
G.edge['rild']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][open open][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['qmuxd']['fill'] = 'red'
G.add_edge('rild','qmuxd')
G.edge['rild']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][open open][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('rild','radio')
G.edge['rild']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['radio']['fill'] = 'red'
G.add_edge('rild','radio')
G.edge['rild']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['rild']['fill'] = 'red'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('rild','sec-ril')
G.edge['rild']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read]'
G.edge['rild']['sec-ril']['fill'] = 'red'
G.add_edge('rild','s_system_app')
G.edge['rild']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read]'
G.edge['rild']['s_system_app']['fill'] = 'red'
G.add_edge('rild','system_app')
G.edge['rild']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read]'
G.edge['rild']['system_app']['fill'] = 'red'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['system_server']['fill'] = 'red'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('rild','thermald')
G.edge['rild']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['rild']['thermald']['fill'] = 'red'
G.add_edge('rild','thermald')
G.edge['rild']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('rild','untrusteddomain')
G.edge['rild']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['untrusteddomain']['fill'] = 'red'
G.add_edge('rild','untrusteddomain')
G.edge['rild']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','ATFWD-daemon')
G.edge['system_server']['ATFWD-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','cnd')
G.edge['system_server']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','dpmd')
G.edge['system_server']['dpmd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('system_server','netmgrd')
G.edge['system_server']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open]'
G.add_edge('system_server','qmiproxy')
G.edge['system_server']['qmiproxy']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][open open][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][append read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','thermald')
G.edge['system_server']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][write read][open open]'
G.add_edge('system_server','untrusteddomain')
G.edge['system_server']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','ATFWD-daemon')
G.edge['system_server']['ATFWD-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','cnd')
G.edge['system_server']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','dpmd')
G.edge['system_server']['dpmd']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][add_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setattr getattr]'
G.add_edge('system_server','netmgrd')
G.edge['system_server']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr]'
G.add_edge('system_server','qmiproxy')
G.edge['system_server']['qmiproxy']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][open open][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][append read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','sec-ril')
G.edge['system_server']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setattr getattr]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setattr getattr]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','thermald')
G.edge['system_server']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr]'
G.add_edge('system_server','untrusteddomain')
G.edge['system_server']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','ATFWD-daemon')
G.edge['system_server']['ATFWD-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['ATFWD-daemon']['fill'] = 'red'
G.add_edge('system_server','ATFWD-daemon')
G.edge['system_server']['ATFWD-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','cnd')
G.edge['system_server']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['cnd']['fill'] = 'red'
G.add_edge('system_server','cnd')
G.edge['system_server']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','dpmd')
G.edge['system_server']['dpmd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['dpmd']['fill'] = 'red'
G.add_edge('system_server','dpmd')
G.edge['system_server']['dpmd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][add_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setattr getattr][write read]'
G.edge['system_server']['ime_app']['fill'] = 'red'
G.add_edge('system_server','netmgrd')
G.edge['system_server']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read]'
G.edge['system_server']['netmgrd']['fill'] = 'red'
G.add_edge('system_server','netmgrd')
G.edge['system_server']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','qmiproxy')
G.edge['system_server']['qmiproxy']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['qmiproxy']['fill'] = 'red'
G.add_edge('system_server','qmiproxy')
G.edge['system_server']['qmiproxy']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][open open][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['qmuxd']['fill'] = 'red'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][open open][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][append read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['radio']['fill'] = 'red'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][append read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['rild']['fill'] = 'red'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','sec-ril')
G.edge['system_server']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read]'
G.edge['system_server']['sec-ril']['fill'] = 'red'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setattr getattr][write read]'
G.edge['system_server']['s_system_app']['fill'] = 'red'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setattr getattr][write read]'
G.edge['system_server']['system_app']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','thermald')
G.edge['system_server']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read]'
G.edge['system_server']['thermald']['fill'] = 'red'
G.add_edge('system_server','thermald')
G.edge['system_server']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','untrusteddomain')
G.edge['system_server']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['untrusteddomain']['fill'] = 'red'
G.add_edge('system_server','untrusteddomain')
G.edge['system_server']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('thermald','ATFWD-daemon')
G.edge['thermald']['ATFWD-daemon']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('thermald','cnd')
G.edge['thermald']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('thermald','dpmd')
G.edge['thermald']['dpmd']['write-read'] = '[open open]'
G.add_edge('thermald','netmgrd')
G.edge['thermald']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('thermald','qmiproxy')
G.edge['thermald']['qmiproxy']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('thermald','qmuxd')
G.edge['thermald']['qmuxd']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('thermald','radio')
G.edge['thermald']['radio']['write-read'] = '[open open]'
G.add_edge('thermald','rild')
G.edge['thermald']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('thermald','system_server')
G.edge['thermald']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('thermald','thermald')
G.edge['thermald']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('thermald','untrusteddomain')
G.edge['thermald']['untrusteddomain']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('thermald','ATFWD-daemon')
G.edge['thermald']['ATFWD-daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('thermald','cnd')
G.edge['thermald']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('thermald','dpmd')
G.edge['thermald']['dpmd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('thermald','ime_app')
G.edge['thermald']['ime_app']['write-read'] = '[add_name search][setattr getattr]'
G.add_edge('thermald','netmgrd')
G.edge['thermald']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('thermald','qmiproxy')
G.edge['thermald']['qmiproxy']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('thermald','qmuxd')
G.edge['thermald']['qmuxd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('thermald','radio')
G.edge['thermald']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('thermald','rild')
G.edge['thermald']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('thermald','sec-ril')
G.edge['thermald']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][setattr getattr]'
G.add_edge('thermald','s_system_app')
G.edge['thermald']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][setattr getattr]'
G.add_edge('thermald','system_app')
G.edge['thermald']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][setattr getattr]'
G.add_edge('thermald','system_server')
G.edge['thermald']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('thermald','thermald')
G.edge['thermald']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('thermald','untrusteddomain')
G.edge['thermald']['untrusteddomain']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('thermald','ATFWD-daemon')
G.edge['thermald']['ATFWD-daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['thermald']['ATFWD-daemon']['fill'] = 'red'
G.add_edge('thermald','ATFWD-daemon')
G.edge['thermald']['ATFWD-daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('thermald','cnd')
G.edge['thermald']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['thermald']['cnd']['fill'] = 'red'
G.add_edge('thermald','cnd')
G.edge['thermald']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('thermald','dpmd')
G.edge['thermald']['dpmd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['thermald']['dpmd']['fill'] = 'red'
G.add_edge('thermald','dpmd')
G.edge['thermald']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('thermald','ime_app')
G.edge['thermald']['ime_app']['write-read'] = '[add_name search][setattr getattr][write read]'
G.edge['thermald']['ime_app']['fill'] = 'red'
G.add_edge('thermald','netmgrd')
G.edge['thermald']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['thermald']['netmgrd']['fill'] = 'red'
G.add_edge('thermald','netmgrd')
G.edge['thermald']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('thermald','qmiproxy')
G.edge['thermald']['qmiproxy']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['thermald']['qmiproxy']['fill'] = 'red'
G.add_edge('thermald','qmiproxy')
G.edge['thermald']['qmiproxy']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('thermald','qmuxd')
G.edge['thermald']['qmuxd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['thermald']['qmuxd']['fill'] = 'red'
G.add_edge('thermald','qmuxd')
G.edge['thermald']['qmuxd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('thermald','radio')
G.edge['thermald']['radio']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['thermald']['radio']['fill'] = 'red'
G.add_edge('thermald','radio')
G.edge['thermald']['radio']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('thermald','rild')
G.edge['thermald']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['thermald']['rild']['fill'] = 'red'
G.add_edge('thermald','rild')
G.edge['thermald']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('thermald','sec-ril')
G.edge['thermald']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][setattr getattr][write read]'
G.edge['thermald']['sec-ril']['fill'] = 'red'
G.add_edge('thermald','s_system_app')
G.edge['thermald']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][setattr getattr][write read]'
G.edge['thermald']['s_system_app']['fill'] = 'red'
G.add_edge('thermald','system_app')
G.edge['thermald']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][setattr getattr][write read]'
G.edge['thermald']['system_app']['fill'] = 'red'
G.add_edge('thermald','system_server')
G.edge['thermald']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['thermald']['system_server']['fill'] = 'red'
G.add_edge('thermald','system_server')
G.edge['thermald']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('thermald','thermald')
G.edge['thermald']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['thermald']['thermald']['fill'] = 'red'
G.add_edge('thermald','thermald')
G.edge['thermald']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('thermald','untrusteddomain')
G.edge['thermald']['untrusteddomain']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['thermald']['untrusteddomain']['fill'] = 'red'
G.add_edge('thermald','untrusteddomain')
G.edge['thermald']['untrusteddomain']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','ATFWD-daemon')
G.edge['untrusteddomain']['ATFWD-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusteddomain','cnd')
G.edge['untrusteddomain']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusteddomain','dpmd')
G.edge['untrusteddomain']['dpmd']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','netmgrd')
G.edge['untrusteddomain']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusteddomain','qmiproxy')
G.edge['untrusteddomain']['qmiproxy']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusteddomain','qmuxd')
G.edge['untrusteddomain']['qmuxd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusteddomain','radio')
G.edge['untrusteddomain']['radio']['write-read'] = '[setattr getattr][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusteddomain','rild')
G.edge['untrusteddomain']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('untrusteddomain','thermald')
G.edge['untrusteddomain']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusteddomain','ATFWD-daemon')
G.edge['untrusteddomain']['ATFWD-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('untrusteddomain','cnd')
G.edge['untrusteddomain']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('untrusteddomain','dpmd')
G.edge['untrusteddomain']['dpmd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusteddomain','ime_app')
G.edge['untrusteddomain']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][write read][add_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('untrusteddomain','netmgrd')
G.edge['untrusteddomain']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('untrusteddomain','qmiproxy')
G.edge['untrusteddomain']['qmiproxy']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('untrusteddomain','qmuxd')
G.edge['untrusteddomain']['qmuxd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('untrusteddomain','radio')
G.edge['untrusteddomain']['radio']['write-read'] = '[setattr getattr][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('untrusteddomain','rild')
G.edge['untrusteddomain']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('untrusteddomain','sec-ril')
G.edge['untrusteddomain']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('untrusteddomain','s_system_app')
G.edge['untrusteddomain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('untrusteddomain','system_app')
G.edge['untrusteddomain']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('untrusteddomain','thermald')
G.edge['untrusteddomain']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('untrusteddomain','ATFWD-daemon')
G.edge['untrusteddomain']['ATFWD-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['ATFWD-daemon']['fill'] = 'red'
G.add_edge('untrusteddomain','ATFWD-daemon')
G.edge['untrusteddomain']['ATFWD-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','cnd')
G.edge['untrusteddomain']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['cnd']['fill'] = 'red'
G.add_edge('untrusteddomain','cnd')
G.edge['untrusteddomain']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','dpmd')
G.edge['untrusteddomain']['dpmd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusteddomain']['dpmd']['fill'] = 'red'
G.add_edge('untrusteddomain','dpmd')
G.edge['untrusteddomain']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','ime_app')
G.edge['untrusteddomain']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][write read][add_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['untrusteddomain']['ime_app']['fill'] = 'red'
G.add_edge('untrusteddomain','netmgrd')
G.edge['untrusteddomain']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['netmgrd']['fill'] = 'red'
G.add_edge('untrusteddomain','netmgrd')
G.edge['untrusteddomain']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','qmiproxy')
G.edge['untrusteddomain']['qmiproxy']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['qmiproxy']['fill'] = 'red'
G.add_edge('untrusteddomain','qmiproxy')
G.edge['untrusteddomain']['qmiproxy']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','qmuxd')
G.edge['untrusteddomain']['qmuxd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['qmuxd']['fill'] = 'red'
G.add_edge('untrusteddomain','qmuxd')
G.edge['untrusteddomain']['qmuxd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','radio')
G.edge['untrusteddomain']['radio']['write-read'] = '[setattr getattr][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['radio']['fill'] = 'red'
G.add_edge('untrusteddomain','radio')
G.edge['untrusteddomain']['radio']['write-read'] = '[setattr getattr][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','rild')
G.edge['untrusteddomain']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['rild']['fill'] = 'red'
G.add_edge('untrusteddomain','rild')
G.edge['untrusteddomain']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','sec-ril')
G.edge['untrusteddomain']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['untrusteddomain']['sec-ril']['fill'] = 'red'
G.add_edge('untrusteddomain','s_system_app')
G.edge['untrusteddomain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['untrusteddomain']['s_system_app']['fill'] = 'red'
G.add_edge('untrusteddomain','system_app')
G.edge['untrusteddomain']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['untrusteddomain']['system_app']['fill'] = 'red'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['system_server']['fill'] = 'red'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','thermald')
G.edge['untrusteddomain']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['thermald']['fill'] = 'red'
G.add_edge('untrusteddomain','thermald')
G.edge['untrusteddomain']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['untrusteddomain']['fill'] = 'red'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()