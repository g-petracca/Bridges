import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('appdomain','mpdecision')
G.edge['appdomain']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][open execmod][open open]'
G.add_edge('appdomain','perfd')
G.edge['appdomain']['perfd']['write-read'] = '[open open]'
G.add_edge('appdomain','mpdecision')
G.edge['appdomain']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][open execmod][open open][write read]'
G.edge['appdomain']['mpdecision']['fill'] = 'red'
G.add_edge('appdomain','perfd')
G.edge['appdomain']['perfd']['write-read'] = '[open open][write read]'
G.edge['appdomain']['perfd']['fill'] = 'red'
G.add_edge('appdomain','mpdecision')
G.edge['appdomain']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][open execmod][open open][write read][add_name search]'
G.add_edge('appdomain','mpdecision')
G.edge['appdomain']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][open execmod][open open][write read][add_name search][remove_name search]'
G.add_edge('appdomain','perfd')
G.edge['appdomain']['perfd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('appdomain','perfd')
G.edge['appdomain']['perfd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('mediaserver','mpdecision')
G.edge['mediaserver']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','perfd')
G.edge['mediaserver']['perfd']['write-read'] = '[write read][open open]'
G.add_edge('mediaserver','mpdecision')
G.edge['mediaserver']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['mediaserver']['mpdecision']['fill'] = 'red'
G.add_edge('mediaserver','perfd')
G.edge['mediaserver']['perfd']['write-read'] = '[write read][open open][write read]'
G.edge['mediaserver']['perfd']['fill'] = 'red'
G.add_edge('mediaserver','mpdecision')
G.edge['mediaserver']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('mediaserver','mpdecision')
G.edge['mediaserver']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('mediaserver','perfd')
G.edge['mediaserver']['perfd']['write-read'] = '[write read][open open][write read][add_name search]'
G.add_edge('mediaserver','perfd')
G.edge['mediaserver']['perfd']['write-read'] = '[write read][open open][write read][add_name search][remove_name search]'
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mpdecision','perfd')
G.edge['mpdecision']['perfd']['write-read'] = '[write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['mpdecision']['mpdecision']['fill'] = 'red'
G.add_edge('mpdecision','perfd')
G.edge['mpdecision']['perfd']['write-read'] = '[write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['mpdecision']['perfd']['fill'] = 'red'
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('mpdecision','perfd')
G.edge['mpdecision']['perfd']['write-read'] = '[write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('mpdecision','perfd')
G.edge['mpdecision']['perfd']['write-read'] = '[write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('perfd','mpdecision')
G.edge['perfd']['mpdecision']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('perfd','perfd')
G.edge['perfd']['perfd']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('perfd','mpdecision')
G.edge['perfd']['mpdecision']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['perfd']['mpdecision']['fill'] = 'red'
G.add_edge('perfd','perfd')
G.edge['perfd']['perfd']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['perfd']['perfd']['fill'] = 'red'
G.add_edge('perfd','mpdecision')
G.edge['perfd']['mpdecision']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('perfd','mpdecision')
G.edge['perfd']['mpdecision']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('perfd','perfd')
G.edge['perfd']['perfd']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('perfd','perfd')
G.edge['perfd']['perfd']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','mpdecision')
G.edge['s_system_app']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','perfd')
G.edge['s_system_app']['perfd']['write-read'] = '[setopt getopt][open open]'
G.add_edge('s_system_app','mpdecision')
G.edge['s_system_app']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['s_system_app']['mpdecision']['fill'] = 'red'
G.add_edge('s_system_app','perfd')
G.edge['s_system_app']['perfd']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['s_system_app']['perfd']['fill'] = 'red'
G.add_edge('s_system_app','mpdecision')
G.edge['s_system_app']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('s_system_app','mpdecision')
G.edge['s_system_app']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','perfd')
G.edge['s_system_app']['perfd']['write-read'] = '[setopt getopt][open open][write read][add_name search]'
G.add_edge('s_system_app','perfd')
G.edge['s_system_app']['perfd']['write-read'] = '[setopt getopt][open open][write read][add_name search][remove_name search]'
G.add_edge('surfaceflinger','mpdecision')
G.edge['surfaceflinger']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][append read][write read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('surfaceflinger','perfd')
G.edge['surfaceflinger']['perfd']['write-read'] = '[setopt getopt][write read][open open]'
G.add_edge('surfaceflinger','mpdecision')
G.edge['surfaceflinger']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][append read][write read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['surfaceflinger']['mpdecision']['fill'] = 'red'
G.add_edge('surfaceflinger','perfd')
G.edge['surfaceflinger']['perfd']['write-read'] = '[setopt getopt][write read][open open][write read]'
G.edge['surfaceflinger']['perfd']['fill'] = 'red'
G.add_edge('surfaceflinger','mpdecision')
G.edge['surfaceflinger']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][append read][write read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('surfaceflinger','mpdecision')
G.edge['surfaceflinger']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][append read][write read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('surfaceflinger','perfd')
G.edge['surfaceflinger']['perfd']['write-read'] = '[setopt getopt][write read][open open][write read][add_name search]'
G.add_edge('surfaceflinger','perfd')
G.edge['surfaceflinger']['perfd']['write-read'] = '[setopt getopt][write read][open open][write read][add_name search][remove_name search]'
G.add_edge('system_app','mpdecision')
G.edge['system_app']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','perfd')
G.edge['system_app']['perfd']['write-read'] = '[setopt getopt][open open]'
G.add_edge('system_app','mpdecision')
G.edge['system_app']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['system_app']['mpdecision']['fill'] = 'red'
G.add_edge('system_app','perfd')
G.edge['system_app']['perfd']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['system_app']['perfd']['fill'] = 'red'
G.add_edge('system_app','mpdecision')
G.edge['system_app']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('system_app','mpdecision')
G.edge['system_app']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('system_app','perfd')
G.edge['system_app']['perfd']['write-read'] = '[setopt getopt][open open][write read][add_name search]'
G.add_edge('system_app','perfd')
G.edge['system_app']['perfd']['write-read'] = '[setopt getopt][open open][write read][add_name search][remove_name search]'
G.add_edge('system_server','mpdecision')
G.edge['system_server']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][write read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','perfd')
G.edge['system_server']['perfd']['write-read'] = '[setopt getopt][write read][write read][write read][open open][write read][open open]'
G.add_edge('system_server','mpdecision')
G.edge['system_server']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][write read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['system_server']['mpdecision']['fill'] = 'red'
G.add_edge('system_server','perfd')
G.edge['system_server']['perfd']['write-read'] = '[setopt getopt][write read][write read][write read][open open][write read][open open][write read]'
G.edge['system_server']['perfd']['fill'] = 'red'
G.add_edge('system_server','mpdecision')
G.edge['system_server']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][write read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('system_server','mpdecision')
G.edge['system_server']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][write read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('system_server','perfd')
G.edge['system_server']['perfd']['write-read'] = '[setopt getopt][write read][write read][write read][open open][write read][open open][write read][add_name search]'
G.add_edge('system_server','perfd')
G.edge['system_server']['perfd']['write-read'] = '[setopt getopt][write read][write read][write read][open open][write read][open open][write read][add_name search][remove_name search]'
G.add_edge('thermal-engine','mpdecision')
G.edge['thermal-engine']['mpdecision']['write-read'] = '[open open][write read][append read][open open][write read][append read][add_name search]'
G.add_edge('thermal-engine','mpdecision')
G.edge['thermal-engine']['mpdecision']['write-read'] = '[open open][write read][append read][open open][write read][append read][add_name search][remove_name search]'
G.add_edge('thermal-engine','perfd')
G.edge['thermal-engine']['perfd']['write-read'] = '[write read][open open][write read][add_name search]'
G.add_edge('thermal-engine','perfd')
G.edge['thermal-engine']['perfd']['write-read'] = '[write read][open open][write read][add_name search][remove_name search]'
G.add_edge('wfd_app','mpdecision')
G.edge['wfd_app']['mpdecision']['write-read'] = '[open open]'
G.add_edge('wfd_app','perfd')
G.edge['wfd_app']['perfd']['write-read'] = '[open open]'
G.add_edge('wfd_app','mpdecision')
G.edge['wfd_app']['mpdecision']['write-read'] = '[open open][write read]'
G.edge['wfd_app']['mpdecision']['fill'] = 'red'
G.add_edge('wfd_app','perfd')
G.edge['wfd_app']['perfd']['write-read'] = '[open open][write read]'
G.edge['wfd_app']['perfd']['fill'] = 'red'
G.add_edge('wfd_app','mpdecision')
G.edge['wfd_app']['mpdecision']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('wfd_app','mpdecision')
G.edge['wfd_app']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('wfd_app','perfd')
G.edge['wfd_app']['perfd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('wfd_app','perfd')
G.edge['wfd_app']['perfd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()