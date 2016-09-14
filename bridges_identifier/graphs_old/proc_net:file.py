import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('charon','clatd')
G.edge['charon']['clatd']['write-read'] = '[add_name search][open open]'
G.add_edge('charon','init_shell')
G.edge['charon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('charon','netmgrd')
G.edge['charon']['netmgrd']['write-read'] = '[open open]'
G.add_edge('charon','rild')
G.edge['charon']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['charon']['charon']['fill'] = 'red'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('charon','clatd')
G.edge['charon']['clatd']['write-read'] = '[add_name search][open open][write read]'
G.edge['charon']['clatd']['fill'] = 'red'
G.add_edge('charon','clatd')
G.edge['charon']['clatd']['write-read'] = '[add_name search][open open][write read][append read]'
G.add_edge('charon','dhcp')
G.edge['charon']['dhcp']['write-read'] = '[write read][add_name search][write read]'
G.edge['charon']['dhcp']['fill'] = 'red'
G.add_edge('charon','init_shell')
G.edge['charon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['charon']['init_shell']['fill'] = 'red'
G.add_edge('charon','init_shell')
G.edge['charon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('charon','netd')
G.edge['charon']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['charon']['netd']['fill'] = 'red'
G.add_edge('charon','netmgrd')
G.edge['charon']['netmgrd']['write-read'] = '[open open][write read]'
G.edge['charon']['netmgrd']['fill'] = 'red'
G.add_edge('charon','netmgrd')
G.edge['charon']['netmgrd']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','netmgrd')
G.edge['charon']['netmgrd']['write-read'] = '[open open][write read][append read][write read]'
G.edge['charon']['netmgrd']['fill'] = 'red'
G.add_edge('charon','olsrd')
G.edge['charon']['olsrd']['write-read'] = '[write read]'
G.edge['charon']['olsrd']['fill'] = 'red'
G.add_edge('charon','rild')
G.edge['charon']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['charon']['rild']['fill'] = 'red'
G.add_edge('charon','rild')
G.edge['charon']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('charon','s_system_app')
G.edge['charon']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['charon']['s_system_app']['fill'] = 'red'
G.add_edge('charon','system_app')
G.edge['charon']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['charon']['system_app']['fill'] = 'red'
G.add_edge('charon','wcnss_service')
G.edge['charon']['wcnss_service']['write-read'] = '[write read]'
G.edge['charon']['wcnss_service']['fill'] = 'red'
G.add_edge('charon','wpa')
G.edge['charon']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['charon']['wpa']['fill'] = 'red'
G.add_edge('domain','charon')
G.edge['domain']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('domain','clatd')
G.edge['domain']['clatd']['write-read'] = '[add_name search][add_name search][open open]'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('domain','netmgrd')
G.edge['domain']['netmgrd']['write-read'] = '[add_name search][add_name search][remove_name search][open open]'
G.add_edge('domain','rild')
G.edge['domain']['rild']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('domain','charon')
G.edge['domain']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['domain']['charon']['fill'] = 'red'
G.add_edge('domain','charon')
G.edge['domain']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('domain','clatd')
G.edge['domain']['clatd']['write-read'] = '[add_name search][add_name search][open open][write read]'
G.edge['domain']['clatd']['fill'] = 'red'
G.add_edge('domain','clatd')
G.edge['domain']['clatd']['write-read'] = '[add_name search][add_name search][open open][write read][append read]'
G.add_edge('domain','dhcp')
G.edge['domain']['dhcp']['write-read'] = '[write read][add_name search][add_name search][write read]'
G.edge['domain']['dhcp']['fill'] = 'red'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['domain']['init_shell']['fill'] = 'red'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('domain','netd')
G.edge['domain']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][write read]'
G.edge['domain']['netd']['fill'] = 'red'
G.add_edge('domain','netmgrd')
G.edge['domain']['netmgrd']['write-read'] = '[add_name search][add_name search][remove_name search][open open][write read]'
G.edge['domain']['netmgrd']['fill'] = 'red'
G.add_edge('domain','netmgrd')
G.edge['domain']['netmgrd']['write-read'] = '[add_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','netmgrd')
G.edge['domain']['netmgrd']['write-read'] = '[add_name search][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['domain']['netmgrd']['fill'] = 'red'
G.add_edge('domain','olsrd')
G.edge['domain']['olsrd']['write-read'] = '[setattr getattr][add_name search][remove_name search][write read]'
G.edge['domain']['olsrd']['fill'] = 'red'
G.add_edge('domain','rild')
G.edge['domain']['rild']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['domain']['rild']['fill'] = 'red'
G.add_edge('domain','rild')
G.edge['domain']['rild']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','s_system_app')
G.edge['domain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][add_name search][remove_name search][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['domain']['s_system_app']['fill'] = 'red'
G.add_edge('domain','system_app')
G.edge['domain']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][add_name search][remove_name search][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['domain']['system_app']['fill'] = 'red'
G.add_edge('domain','wcnss_service')
G.edge['domain']['wcnss_service']['write-read'] = '[write read]'
G.edge['domain']['wcnss_service']['fill'] = 'red'
G.add_edge('domain','wpa')
G.edge['domain']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][write read]'
G.edge['domain']['wpa']['fill'] = 'red'
app = Viewer(G)
app.mainloop()