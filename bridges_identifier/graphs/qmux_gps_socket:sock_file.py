import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('commonplatformappdomain','gpsone_daemon')
G.edge['commonplatformappdomain']['gpsone_daemon']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('commonplatformappdomain','gsiff_daemon')
G.edge['commonplatformappdomain']['gsiff_daemon']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('commonplatformappdomain','qmuxd')
G.edge['commonplatformappdomain']['qmuxd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('commonplatformappdomain','wiperiface')
G.edge['commonplatformappdomain']['wiperiface']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','gpsone_daemon')
G.edge['commonplatformappdomain']['gpsone_daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','gsiff_daemon')
G.edge['commonplatformappdomain']['gsiff_daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','qmuxd')
G.edge['commonplatformappdomain']['qmuxd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','wiperiface')
G.edge['commonplatformappdomain']['wiperiface']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','gpsone_daemon')
G.edge['commonplatformappdomain']['gpsone_daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['gpsone_daemon']['fill'] = 'red'
G.add_edge('commonplatformappdomain','gpsone_daemon')
G.edge['commonplatformappdomain']['gpsone_daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','gsiff_daemon')
G.edge['commonplatformappdomain']['gsiff_daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['gsiff_daemon']['fill'] = 'red'
G.add_edge('commonplatformappdomain','gsiff_daemon')
G.edge['commonplatformappdomain']['gsiff_daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','qmuxd')
G.edge['commonplatformappdomain']['qmuxd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['qmuxd']['fill'] = 'red'
G.add_edge('commonplatformappdomain','qmuxd')
G.edge['commonplatformappdomain']['qmuxd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','wiperiface')
G.edge['commonplatformappdomain']['wiperiface']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['wiperiface']['fill'] = 'red'
G.add_edge('commonplatformappdomain','wiperiface')
G.edge['commonplatformappdomain']['wiperiface']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('gpsone_daemon','commonplatformappdomain')
G.edge['gpsone_daemon']['commonplatformappdomain']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('gpsone_daemon','gpsone_daemon')
G.edge['gpsone_daemon']['gpsone_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('gpsone_daemon','gsiff_daemon')
G.edge['gpsone_daemon']['gsiff_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('gpsone_daemon','qmuxd')
G.edge['gpsone_daemon']['qmuxd']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('gpsone_daemon','wiperiface')
G.edge['gpsone_daemon']['wiperiface']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('gpsone_daemon','commonplatformappdomain')
G.edge['gpsone_daemon']['commonplatformappdomain']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('gpsone_daemon','gpsone_daemon')
G.edge['gpsone_daemon']['gpsone_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('gpsone_daemon','gsiff_daemon')
G.edge['gpsone_daemon']['gsiff_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('gpsone_daemon','qmuxd')
G.edge['gpsone_daemon']['qmuxd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('gpsone_daemon','wiperiface')
G.edge['gpsone_daemon']['wiperiface']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('gpsone_daemon','commonplatformappdomain')
G.edge['gpsone_daemon']['commonplatformappdomain']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['gpsone_daemon']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('gpsone_daemon','commonplatformappdomain')
G.edge['gpsone_daemon']['commonplatformappdomain']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('gpsone_daemon','gpsone_daemon')
G.edge['gpsone_daemon']['gpsone_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['gpsone_daemon']['gpsone_daemon']['fill'] = 'red'
G.add_edge('gpsone_daemon','gpsone_daemon')
G.edge['gpsone_daemon']['gpsone_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('gpsone_daemon','gsiff_daemon')
G.edge['gpsone_daemon']['gsiff_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['gpsone_daemon']['gsiff_daemon']['fill'] = 'red'
G.add_edge('gpsone_daemon','gsiff_daemon')
G.edge['gpsone_daemon']['gsiff_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('gpsone_daemon','qmuxd')
G.edge['gpsone_daemon']['qmuxd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['gpsone_daemon']['qmuxd']['fill'] = 'red'
G.add_edge('gpsone_daemon','qmuxd')
G.edge['gpsone_daemon']['qmuxd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('gpsone_daemon','wiperiface')
G.edge['gpsone_daemon']['wiperiface']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['gpsone_daemon']['wiperiface']['fill'] = 'red'
G.add_edge('gpsone_daemon','wiperiface')
G.edge['gpsone_daemon']['wiperiface']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('gsiff_daemon','commonplatformappdomain')
G.edge['gsiff_daemon']['commonplatformappdomain']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('gsiff_daemon','gpsone_daemon')
G.edge['gsiff_daemon']['gpsone_daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('gsiff_daemon','gsiff_daemon')
G.edge['gsiff_daemon']['gsiff_daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('gsiff_daemon','qmuxd')
G.edge['gsiff_daemon']['qmuxd']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('gsiff_daemon','wiperiface')
G.edge['gsiff_daemon']['wiperiface']['write-read'] = '[open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('gsiff_daemon','commonplatformappdomain')
G.edge['gsiff_daemon']['commonplatformappdomain']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('gsiff_daemon','gpsone_daemon')
G.edge['gsiff_daemon']['gpsone_daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('gsiff_daemon','gsiff_daemon')
G.edge['gsiff_daemon']['gsiff_daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('gsiff_daemon','qmuxd')
G.edge['gsiff_daemon']['qmuxd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('gsiff_daemon','wiperiface')
G.edge['gsiff_daemon']['wiperiface']['write-read'] = '[open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('gsiff_daemon','commonplatformappdomain')
G.edge['gsiff_daemon']['commonplatformappdomain']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['gsiff_daemon']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('gsiff_daemon','commonplatformappdomain')
G.edge['gsiff_daemon']['commonplatformappdomain']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('gsiff_daemon','gpsone_daemon')
G.edge['gsiff_daemon']['gpsone_daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['gsiff_daemon']['gpsone_daemon']['fill'] = 'red'
G.add_edge('gsiff_daemon','gpsone_daemon')
G.edge['gsiff_daemon']['gpsone_daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('gsiff_daemon','gsiff_daemon')
G.edge['gsiff_daemon']['gsiff_daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['gsiff_daemon']['gsiff_daemon']['fill'] = 'red'
G.add_edge('gsiff_daemon','gsiff_daemon')
G.edge['gsiff_daemon']['gsiff_daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('gsiff_daemon','qmuxd')
G.edge['gsiff_daemon']['qmuxd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['gsiff_daemon']['qmuxd']['fill'] = 'red'
G.add_edge('gsiff_daemon','qmuxd')
G.edge['gsiff_daemon']['qmuxd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('gsiff_daemon','wiperiface')
G.edge['gsiff_daemon']['wiperiface']['write-read'] = '[open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['gsiff_daemon']['wiperiface']['fill'] = 'red'
G.add_edge('gsiff_daemon','wiperiface')
G.edge['gsiff_daemon']['wiperiface']['write-read'] = '[open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('qmuxd','commonplatformappdomain')
G.edge['qmuxd']['commonplatformappdomain']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('qmuxd','gpsone_daemon')
G.edge['qmuxd']['gpsone_daemon']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('qmuxd','gsiff_daemon')
G.edge['qmuxd']['gsiff_daemon']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][append read][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('qmuxd','wiperiface')
G.edge['qmuxd']['wiperiface']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('qmuxd','commonplatformappdomain')
G.edge['qmuxd']['commonplatformappdomain']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('qmuxd','gpsone_daemon')
G.edge['qmuxd']['gpsone_daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('qmuxd','gsiff_daemon')
G.edge['qmuxd']['gsiff_daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('qmuxd','wiperiface')
G.edge['qmuxd']['wiperiface']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('qmuxd','commonplatformappdomain')
G.edge['qmuxd']['commonplatformappdomain']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['qmuxd']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('qmuxd','commonplatformappdomain')
G.edge['qmuxd']['commonplatformappdomain']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('qmuxd','gpsone_daemon')
G.edge['qmuxd']['gpsone_daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['qmuxd']['gpsone_daemon']['fill'] = 'red'
G.add_edge('qmuxd','gpsone_daemon')
G.edge['qmuxd']['gpsone_daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('qmuxd','gsiff_daemon')
G.edge['qmuxd']['gsiff_daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['qmuxd']['gsiff_daemon']['fill'] = 'red'
G.add_edge('qmuxd','gsiff_daemon')
G.edge['qmuxd']['gsiff_daemon']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['qmuxd']['qmuxd']['fill'] = 'red'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('qmuxd','wiperiface')
G.edge['qmuxd']['wiperiface']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['qmuxd']['wiperiface']['fill'] = 'red'
G.add_edge('qmuxd','wiperiface')
G.edge['qmuxd']['wiperiface']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('wiperiface','commonplatformappdomain')
G.edge['wiperiface']['commonplatformappdomain']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('wiperiface','gpsone_daemon')
G.edge['wiperiface']['gpsone_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('wiperiface','gsiff_daemon')
G.edge['wiperiface']['gsiff_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('wiperiface','qmuxd')
G.edge['wiperiface']['qmuxd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('wiperiface','wiperiface')
G.edge['wiperiface']['wiperiface']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('wiperiface','commonplatformappdomain')
G.edge['wiperiface']['commonplatformappdomain']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('wiperiface','gpsone_daemon')
G.edge['wiperiface']['gpsone_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('wiperiface','gsiff_daemon')
G.edge['wiperiface']['gsiff_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('wiperiface','qmuxd')
G.edge['wiperiface']['qmuxd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('wiperiface','wiperiface')
G.edge['wiperiface']['wiperiface']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('wiperiface','commonplatformappdomain')
G.edge['wiperiface']['commonplatformappdomain']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['wiperiface']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('wiperiface','commonplatformappdomain')
G.edge['wiperiface']['commonplatformappdomain']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('wiperiface','gpsone_daemon')
G.edge['wiperiface']['gpsone_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['wiperiface']['gpsone_daemon']['fill'] = 'red'
G.add_edge('wiperiface','gpsone_daemon')
G.edge['wiperiface']['gpsone_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('wiperiface','gsiff_daemon')
G.edge['wiperiface']['gsiff_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['wiperiface']['gsiff_daemon']['fill'] = 'red'
G.add_edge('wiperiface','gsiff_daemon')
G.edge['wiperiface']['gsiff_daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('wiperiface','qmuxd')
G.edge['wiperiface']['qmuxd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['wiperiface']['qmuxd']['fill'] = 'red'
G.add_edge('wiperiface','qmuxd')
G.edge['wiperiface']['qmuxd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('wiperiface','wiperiface')
G.edge['wiperiface']['wiperiface']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['wiperiface']['wiperiface']['fill'] = 'red'
G.add_edge('wiperiface','wiperiface')
G.edge['wiperiface']['wiperiface']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()