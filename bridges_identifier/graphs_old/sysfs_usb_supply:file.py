import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('charger_monitor','hvdcp')
G.edge['charger_monitor']['hvdcp']['write-read'] = '[write read][append read][open open][write read][append read][open open]'
G.add_edge('charger_monitor','ueventd')
G.edge['charger_monitor']['ueventd']['write-read'] = '[write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('charger_monitor','hvdcp')
G.edge['charger_monitor']['hvdcp']['write-read'] = '[write read][append read][open open][write read][append read][open open][write read]'
G.edge['charger_monitor']['hvdcp']['fill'] = 'red'
G.add_edge('charger_monitor','hvdcp')
G.edge['charger_monitor']['hvdcp']['write-read'] = '[write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('charger_monitor','ueventd')
G.edge['charger_monitor']['ueventd']['write-read'] = '[write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['charger_monitor']['ueventd']['fill'] = 'red'
G.add_edge('charger_monitor','ueventd')
G.edge['charger_monitor']['ueventd']['write-read'] = '[write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('healthd','hvdcp')
G.edge['healthd']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open]'
G.add_edge('healthd','ueventd')
G.edge['healthd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('healthd','hvdcp')
G.edge['healthd']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read]'
G.edge['healthd']['hvdcp']['fill'] = 'red'
G.add_edge('healthd','hvdcp')
G.edge['healthd']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read]'
G.add_edge('healthd','ueventd')
G.edge['healthd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['healthd']['ueventd']['fill'] = 'red'
G.add_edge('healthd','ueventd')
G.edge['healthd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('hvdcp','hvdcp')
G.edge['hvdcp']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('hvdcp','ueventd')
G.edge['hvdcp']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open]'
G.add_edge('hvdcp','hvdcp')
G.edge['hvdcp']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['hvdcp']['hvdcp']['fill'] = 'red'
G.add_edge('hvdcp','hvdcp')
G.edge['hvdcp']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('hvdcp','ueventd')
G.edge['hvdcp']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read]'
G.edge['hvdcp']['ueventd']['fill'] = 'red'
G.add_edge('hvdcp','ueventd')
G.edge['hvdcp']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()