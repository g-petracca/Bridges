import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('dhcp','dhcp')
G.edge['dhcp']['dhcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('dhcp','dnsmasq')
G.edge['dhcp']['dnsmasq']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('dhcp','netd')
G.edge['dhcp']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('dhcp','dhcp')
G.edge['dhcp']['dhcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('dhcp','dhcp')
G.edge['dhcp']['dhcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['dhcp']['dhcp']['fill'] = 'red'
G.add_edge('dhcp','dnsmasq')
G.edge['dhcp']['dnsmasq']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['dhcp']['dnsmasq']['fill'] = 'red'
G.add_edge('dhcp','netd')
G.edge['dhcp']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['dhcp']['netd']['fill'] = 'red'
G.add_edge('dhcp','dhcp')
G.edge['dhcp']['dhcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('dhcp','dhcp')
G.edge['dhcp']['dhcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dhcp','dnsmasq')
G.edge['dhcp']['dnsmasq']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('dhcp','dnsmasq')
G.edge['dhcp']['dnsmasq']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('dhcp','netd')
G.edge['dhcp']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('dhcp','netd')
G.edge['dhcp']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('dnsmasq','dhcp')
G.edge['dnsmasq']['dhcp']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('dnsmasq','dnsmasq')
G.edge['dnsmasq']['dnsmasq']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('dnsmasq','netd')
G.edge['dnsmasq']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('dnsmasq','dhcp')
G.edge['dnsmasq']['dhcp']['write-read'] = '[open open][setattr getattr][write read][append read][open open][add_name search]'
G.add_edge('dnsmasq','dhcp')
G.edge['dnsmasq']['dhcp']['write-read'] = '[open open][setattr getattr][write read][append read][open open][add_name search][remove_name search]'
G.add_edge('dnsmasq','dnsmasq')
G.edge['dnsmasq']['dnsmasq']['write-read'] = '[open open][setattr getattr][write read][append read][open open][add_name search]'
G.add_edge('dnsmasq','dnsmasq')
G.edge['dnsmasq']['dnsmasq']['write-read'] = '[open open][setattr getattr][write read][append read][open open][add_name search][remove_name search]'
G.add_edge('dnsmasq','netd')
G.edge['dnsmasq']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][add_name search]'
G.add_edge('dnsmasq','netd')
G.edge['dnsmasq']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][add_name search][remove_name search]'
G.add_edge('netd','dhcp')
G.edge['netd']['dhcp']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('netd','dnsmasq')
G.edge['netd']['dnsmasq']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][setopt getopt][open open]'
G.add_edge('netd','dhcp')
G.edge['netd']['dhcp']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('netd','dhcp')
G.edge['netd']['dhcp']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['netd']['dhcp']['fill'] = 'red'
G.add_edge('netd','dnsmasq')
G.edge['netd']['dnsmasq']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['netd']['dnsmasq']['fill'] = 'red'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][setopt getopt][open open][write read]'
G.edge['netd']['netd']['fill'] = 'red'
G.add_edge('netd','dhcp')
G.edge['netd']['dhcp']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','dhcp')
G.edge['netd']['dhcp']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','dnsmasq')
G.edge['netd']['dnsmasq']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('netd','dnsmasq')
G.edge['netd']['dnsmasq']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][setopt getopt][open open][write read][add_name search]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][setopt getopt][open open][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()