import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('clatd','clatd')
G.edge['clatd']['clatd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['clatd']['clatd']['fill'] = 'red'
G.add_edge('clatd','dhcp')
G.edge['clatd']['dhcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['clatd']['dhcp']['fill'] = 'red'
G.add_edge('clatd','dnsmasq')
G.edge['clatd']['dnsmasq']['write-read'] = '[write read]'
G.edge['clatd']['dnsmasq']['fill'] = 'red'
G.add_edge('clatd','hostapd')
G.edge['clatd']['hostapd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['clatd']['hostapd']['fill'] = 'red'
G.add_edge('dhcp','clatd')
G.edge['dhcp']['clatd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['dhcp']['clatd']['fill'] = 'red'
G.add_edge('dhcp','dhcp')
G.edge['dhcp']['dhcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['dhcp']['dhcp']['fill'] = 'red'
G.add_edge('dhcp','dnsmasq')
G.edge['dhcp']['dnsmasq']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read]'
G.edge['dhcp']['dnsmasq']['fill'] = 'red'
G.add_edge('dhcp','hostapd')
G.edge['dhcp']['hostapd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['dhcp']['hostapd']['fill'] = 'red'
G.add_edge('dnsmasq','clatd')
G.edge['dnsmasq']['clatd']['write-read'] = '[write read]'
G.edge['dnsmasq']['clatd']['fill'] = 'red'
G.add_edge('dnsmasq','dhcp')
G.edge['dnsmasq']['dhcp']['write-read'] = '[open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][write read]'
G.edge['dnsmasq']['dhcp']['fill'] = 'red'
G.add_edge('dnsmasq','dnsmasq')
G.edge['dnsmasq']['dnsmasq']['write-read'] = '[open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][write read]'
G.edge['dnsmasq']['dnsmasq']['fill'] = 'red'
G.add_edge('dnsmasq','hostapd')
G.edge['dnsmasq']['hostapd']['write-read'] = '[write read]'
G.edge['dnsmasq']['hostapd']['fill'] = 'red'
G.add_edge('hostapd','clatd')
G.edge['hostapd']['clatd']['write-read'] = '[add_name search][setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['hostapd']['clatd']['fill'] = 'red'
G.add_edge('hostapd','dhcp')
G.edge['hostapd']['dhcp']['write-read'] = '[write read][add_name search][setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['hostapd']['dhcp']['fill'] = 'red'
G.add_edge('hostapd','dnsmasq')
G.edge['hostapd']['dnsmasq']['write-read'] = '[write read]'
G.edge['hostapd']['dnsmasq']['fill'] = 'red'
G.add_edge('hostapd','hostapd')
G.edge['hostapd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['hostapd']['hostapd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()