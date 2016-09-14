import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][write read]'
G.edge['charon']['charon']['fill'] = 'red'
G.add_edge('charon','clatd')
G.edge['charon']['clatd']['write-read'] = '[add_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read]'
G.edge['charon']['clatd']['fill'] = 'red'
G.add_edge('charon','dhcp')
G.edge['charon']['dhcp']['write-read'] = '[write read][add_name search][write read][write read][write read][write read]'
G.edge['charon']['dhcp']['fill'] = 'red'
G.add_edge('charon','dnsmasq')
G.edge['charon']['dnsmasq']['write-read'] = '[write read]'
G.edge['charon']['dnsmasq']['fill'] = 'red'
G.add_edge('charon','fixmo_app')
G.edge['charon']['fixmo_app']['write-read'] = '[open open][write read][append read][write read][write read]'
G.edge['charon']['fixmo_app']['fill'] = 'red'
G.add_edge('charon','good_app')
G.edge['charon']['good_app']['write-read'] = '[open open][write read][append read][write read][write read]'
G.edge['charon']['good_app']['fill'] = 'red'
G.add_edge('charon','hostapd')
G.edge['charon']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['charon']['hostapd']['fill'] = 'red'
G.add_edge('clatd','charon')
G.edge['clatd']['charon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read]'
G.edge['clatd']['charon']['fill'] = 'red'
G.add_edge('clatd','clatd')
G.edge['clatd']['clatd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][write read][write read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][write read]'
G.edge['clatd']['clatd']['fill'] = 'red'
G.add_edge('clatd','dhcp')
G.edge['clatd']['dhcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][write read][setopt getopt][write read][write read][write read][write read][write read][append read][write read]'
G.edge['clatd']['dhcp']['fill'] = 'red'
G.add_edge('clatd','dnsmasq')
G.edge['clatd']['dnsmasq']['write-read'] = '[write read][write read][write read][write read][write read][append read][write read][write read]'
G.edge['clatd']['dnsmasq']['fill'] = 'red'
G.add_edge('clatd','fixmo_app')
G.edge['clatd']['fixmo_app']['write-read'] = '[write read]'
G.edge['clatd']['fixmo_app']['fill'] = 'red'
G.add_edge('clatd','good_app')
G.edge['clatd']['good_app']['write-read'] = '[write read]'
G.edge['clatd']['good_app']['fill'] = 'red'
G.add_edge('clatd','hostapd')
G.edge['clatd']['hostapd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][write read][write read][write read][write read][write read]'
G.edge['clatd']['hostapd']['fill'] = 'red'
G.add_edge('dhcp','charon')
G.edge['dhcp']['charon']['write-read'] = '[write read]'
G.edge['dhcp']['charon']['fill'] = 'red'
G.add_edge('dhcp','clatd')
G.edge['dhcp']['clatd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][write read][append read][write read][write read][write read][write read][write read]'
G.edge['dhcp']['clatd']['fill'] = 'red'
G.add_edge('dhcp','dhcp')
G.edge['dhcp']['dhcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read][write read][write read][write read][write read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read]'
G.edge['dhcp']['dhcp']['fill'] = 'red'
G.add_edge('dhcp','dnsmasq')
G.edge['dhcp']['dnsmasq']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][write read][write read][write read][open open][write read][append read][write read][write read]'
G.edge['dhcp']['dnsmasq']['fill'] = 'red'
G.add_edge('dhcp','fixmo_app')
G.edge['dhcp']['fixmo_app']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['dhcp']['fixmo_app']['fill'] = 'red'
G.add_edge('dhcp','good_app')
G.edge['dhcp']['good_app']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['dhcp']['good_app']['fill'] = 'red'
G.add_edge('dhcp','hostapd')
G.edge['dhcp']['hostapd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][write read][write read][write read][write read][write read]'
G.edge['dhcp']['hostapd']['fill'] = 'red'
G.add_edge('dnsmasq','charon')
G.edge['dnsmasq']['charon']['write-read'] = '[write read]'
G.edge['dnsmasq']['charon']['fill'] = 'red'
G.add_edge('dnsmasq','clatd')
G.edge['dnsmasq']['clatd']['write-read'] = '[write read][write read][write read][write read][write read][write read][write read]'
G.edge['dnsmasq']['clatd']['fill'] = 'red'
G.add_edge('dnsmasq','dhcp')
G.edge['dnsmasq']['dhcp']['write-read'] = '[open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][write read][write read][write read][write read][open open][write read][append read][write read][append read][write read]'
G.edge['dnsmasq']['dhcp']['fill'] = 'red'
G.add_edge('dnsmasq','dnsmasq')
G.edge['dnsmasq']['dnsmasq']['write-read'] = '[open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][write read][write read][write read][write read][open open][write read][append read][write read][write read][append read][write read][write read]'
G.edge['dnsmasq']['dnsmasq']['fill'] = 'red'
G.add_edge('dnsmasq','fixmo_app')
G.edge['dnsmasq']['fixmo_app']['write-read'] = '[write read]'
G.edge['dnsmasq']['fixmo_app']['fill'] = 'red'
G.add_edge('dnsmasq','good_app')
G.edge['dnsmasq']['good_app']['write-read'] = '[write read]'
G.edge['dnsmasq']['good_app']['fill'] = 'red'
G.add_edge('dnsmasq','hostapd')
G.edge['dnsmasq']['hostapd']['write-read'] = '[write read][write read][write read][write read][write read][write read][write read]'
G.edge['dnsmasq']['hostapd']['fill'] = 'red'
G.add_edge('fixmo_app','charon')
G.edge['fixmo_app']['charon']['write-read'] = '[open open][write read][append read][write read][write read]'
G.edge['fixmo_app']['charon']['fill'] = 'red'
G.add_edge('fixmo_app','clatd')
G.edge['fixmo_app']['clatd']['write-read'] = '[write read]'
G.edge['fixmo_app']['clatd']['fill'] = 'red'
G.add_edge('fixmo_app','dhcp')
G.edge['fixmo_app']['dhcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['fixmo_app']['dhcp']['fill'] = 'red'
G.add_edge('fixmo_app','dnsmasq')
G.edge['fixmo_app']['dnsmasq']['write-read'] = '[setopt getopt][write read]'
G.edge['fixmo_app']['dnsmasq']['fill'] = 'red'
G.add_edge('fixmo_app','fixmo_app')
G.edge['fixmo_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read][setopt getopt][open open][setattr getattr][open execmod][write read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['fixmo_app']['fixmo_app']['fill'] = 'red'
G.add_edge('fixmo_app','good_app')
G.edge['fixmo_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read][setopt getopt][open open][setattr getattr][open execmod][write read][setopt getopt][open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][write read]'
G.edge['fixmo_app']['good_app']['fill'] = 'red'
G.add_edge('fixmo_app','hostapd')
G.edge['fixmo_app']['hostapd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['fixmo_app']['hostapd']['fill'] = 'red'
G.add_edge('fixmo_app','fixmo_app')
G.edge['fixmo_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read][setopt getopt][open open][setattr getattr][open execmod][write read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt]'
G.add_edge('fixmo_app','good_app')
G.edge['fixmo_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read][setopt getopt][open open][setattr getattr][open execmod][write read][setopt getopt][open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][write read][setopt getopt]'
G.add_edge('good_app','charon')
G.edge['good_app']['charon']['write-read'] = '[open open][write read][append read][write read][write read]'
G.edge['good_app']['charon']['fill'] = 'red'
G.add_edge('good_app','clatd')
G.edge['good_app']['clatd']['write-read'] = '[write read]'
G.edge['good_app']['clatd']['fill'] = 'red'
G.add_edge('good_app','dhcp')
G.edge['good_app']['dhcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['good_app']['dhcp']['fill'] = 'red'
G.add_edge('good_app','dnsmasq')
G.edge['good_app']['dnsmasq']['write-read'] = '[setopt getopt][write read]'
G.edge['good_app']['dnsmasq']['fill'] = 'red'
G.add_edge('good_app','fixmo_app')
G.edge['good_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read][setopt getopt][open open][setattr getattr][open execmod][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['good_app']['fixmo_app']['fill'] = 'red'
G.add_edge('good_app','good_app')
G.edge['good_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read][setopt getopt][open open][setattr getattr][open execmod][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][write read][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][write read]'
G.edge['good_app']['good_app']['fill'] = 'red'
G.add_edge('good_app','hostapd')
G.edge['good_app']['hostapd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['good_app']['hostapd']['fill'] = 'red'
G.add_edge('good_app','fixmo_app')
G.edge['good_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read][setopt getopt][open open][setattr getattr][open execmod][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt]'
G.add_edge('good_app','good_app')
G.edge['good_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read][setopt getopt][open open][setattr getattr][open execmod][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][write read][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][write read][setopt getopt]'
G.add_edge('hostapd','charon')
G.edge['hostapd']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['hostapd']['charon']['fill'] = 'red'
G.add_edge('hostapd','clatd')
G.edge['hostapd']['clatd']['write-read'] = '[add_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][write read][write read][write read][write read]'
G.edge['hostapd']['clatd']['fill'] = 'red'
G.add_edge('hostapd','dhcp')
G.edge['hostapd']['dhcp']['write-read'] = '[write read][add_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][write read][write read][write read][append read][write read]'
G.edge['hostapd']['dhcp']['fill'] = 'red'
G.add_edge('hostapd','dnsmasq')
G.edge['hostapd']['dnsmasq']['write-read'] = '[write read][write read][write read][write read][write read][append read][write read][write read]'
G.edge['hostapd']['dnsmasq']['fill'] = 'red'
G.add_edge('hostapd','fixmo_app')
G.edge['hostapd']['fixmo_app']['write-read'] = '[write read]'
G.edge['hostapd']['fixmo_app']['fill'] = 'red'
G.add_edge('hostapd','good_app')
G.edge['hostapd']['good_app']['write-read'] = '[write read]'
G.edge['hostapd']['good_app']['fill'] = 'red'
G.add_edge('hostapd','hostapd')
G.edge['hostapd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['hostapd']['hostapd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()