import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('energy-awareness','energy-awareness')
G.edge['energy-awareness']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open]'
G.add_edge('energy-awareness','energyawareness')
G.edge['energy-awareness']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open]'
G.add_edge('energy-awareness','rfs_access')
G.edge['energy-awareness']['rfs_access']['write-read'] = '[open open]'
G.add_edge('energy-awareness','rmt_storage')
G.edge['energy-awareness']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('energy-awareness','energy-awareness')
G.edge['energy-awareness']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read]'
G.edge['energy-awareness']['energy-awareness']['fill'] = 'red'
G.add_edge('energy-awareness','energy-awareness')
G.edge['energy-awareness']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read]'
G.add_edge('energy-awareness','energyawareness')
G.edge['energy-awareness']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read]'
G.edge['energy-awareness']['energyawareness']['fill'] = 'red'
G.add_edge('energy-awareness','energyawareness')
G.edge['energy-awareness']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read]'
G.add_edge('energy-awareness','rfs_access')
G.edge['energy-awareness']['rfs_access']['write-read'] = '[open open][write read]'
G.edge['energy-awareness']['rfs_access']['fill'] = 'red'
G.add_edge('energy-awareness','rfs_access')
G.edge['energy-awareness']['rfs_access']['write-read'] = '[open open][write read][append read]'
G.add_edge('energy-awareness','rmt_storage')
G.edge['energy-awareness']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['energy-awareness']['rmt_storage']['fill'] = 'red'
G.add_edge('energy-awareness','rmt_storage')
G.edge['energy-awareness']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('energyawareness','energy-awareness')
G.edge['energyawareness']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open]'
G.add_edge('energyawareness','energyawareness')
G.edge['energyawareness']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open]'
G.add_edge('energyawareness','rfs_access')
G.edge['energyawareness']['rfs_access']['write-read'] = '[open open]'
G.add_edge('energyawareness','rmt_storage')
G.edge['energyawareness']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('energyawareness','energy-awareness')
G.edge['energyawareness']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read]'
G.edge['energyawareness']['energy-awareness']['fill'] = 'red'
G.add_edge('energyawareness','energy-awareness')
G.edge['energyawareness']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read]'
G.add_edge('energyawareness','energyawareness')
G.edge['energyawareness']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read]'
G.edge['energyawareness']['energyawareness']['fill'] = 'red'
G.add_edge('energyawareness','energyawareness')
G.edge['energyawareness']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read]'
G.add_edge('energyawareness','rfs_access')
G.edge['energyawareness']['rfs_access']['write-read'] = '[open open][write read]'
G.edge['energyawareness']['rfs_access']['fill'] = 'red'
G.add_edge('energyawareness','rfs_access')
G.edge['energyawareness']['rfs_access']['write-read'] = '[open open][write read][append read]'
G.add_edge('energyawareness','rmt_storage')
G.edge['energyawareness']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['energyawareness']['rmt_storage']['fill'] = 'red'
G.add_edge('energyawareness','rmt_storage')
G.edge['energyawareness']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('rfs_access','energy-awareness')
G.edge['rfs_access']['energy-awareness']['write-read'] = '[open open]'
G.add_edge('rfs_access','energyawareness')
G.edge['rfs_access']['energyawareness']['write-read'] = '[open open]'
G.add_edge('rfs_access','rfs_access')
G.edge['rfs_access']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('rfs_access','rmt_storage')
G.edge['rfs_access']['rmt_storage']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('rfs_access','energy-awareness')
G.edge['rfs_access']['energy-awareness']['write-read'] = '[open open][write read]'
G.edge['rfs_access']['energy-awareness']['fill'] = 'red'
G.add_edge('rfs_access','energy-awareness')
G.edge['rfs_access']['energy-awareness']['write-read'] = '[open open][write read][append read]'
G.add_edge('rfs_access','energyawareness')
G.edge['rfs_access']['energyawareness']['write-read'] = '[open open][write read]'
G.edge['rfs_access']['energyawareness']['fill'] = 'red'
G.add_edge('rfs_access','energyawareness')
G.edge['rfs_access']['energyawareness']['write-read'] = '[open open][write read][append read]'
G.add_edge('rfs_access','rfs_access')
G.edge['rfs_access']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['rfs_access']['rfs_access']['fill'] = 'red'
G.add_edge('rfs_access','rfs_access')
G.edge['rfs_access']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('rfs_access','rmt_storage')
G.edge['rfs_access']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['rfs_access']['rmt_storage']['fill'] = 'red'
G.add_edge('rfs_access','rmt_storage')
G.edge['rfs_access']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('rmt_storage','energy-awareness')
G.edge['rmt_storage']['energy-awareness']['write-read'] = '[open open]'
G.add_edge('rmt_storage','energyawareness')
G.edge['rmt_storage']['energyawareness']['write-read'] = '[open open]'
G.add_edge('rmt_storage','rfs_access')
G.edge['rmt_storage']['rfs_access']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('rmt_storage','rmt_storage')
G.edge['rmt_storage']['rmt_storage']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('rmt_storage','energy-awareness')
G.edge['rmt_storage']['energy-awareness']['write-read'] = '[open open][write read]'
G.edge['rmt_storage']['energy-awareness']['fill'] = 'red'
G.add_edge('rmt_storage','energy-awareness')
G.edge['rmt_storage']['energy-awareness']['write-read'] = '[open open][write read][append read]'
G.add_edge('rmt_storage','energyawareness')
G.edge['rmt_storage']['energyawareness']['write-read'] = '[open open][write read]'
G.edge['rmt_storage']['energyawareness']['fill'] = 'red'
G.add_edge('rmt_storage','energyawareness')
G.edge['rmt_storage']['energyawareness']['write-read'] = '[open open][write read][append read]'
G.add_edge('rmt_storage','rfs_access')
G.edge['rmt_storage']['rfs_access']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['rmt_storage']['rfs_access']['fill'] = 'red'
G.add_edge('rmt_storage','rfs_access')
G.edge['rmt_storage']['rfs_access']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('rmt_storage','rmt_storage')
G.edge['rmt_storage']['rmt_storage']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['rmt_storage']['rmt_storage']['fill'] = 'red'
G.add_edge('rmt_storage','rmt_storage')
G.edge['rmt_storage']['rmt_storage']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()