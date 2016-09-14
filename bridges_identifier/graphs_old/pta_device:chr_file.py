import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('energy-awareness','energy-awareness')
G.edge['energy-awareness']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('energy-awareness','energyawareness')
G.edge['energy-awareness']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('energy-awareness','energy-awareness')
G.edge['energy-awareness']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['energy-awareness']['energy-awareness']['fill'] = 'red'
G.add_edge('energy-awareness','energy-awareness')
G.edge['energy-awareness']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('energy-awareness','energyawareness')
G.edge['energy-awareness']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['energy-awareness']['energyawareness']['fill'] = 'red'
G.add_edge('energy-awareness','energyawareness')
G.edge['energy-awareness']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('energyawareness','energy-awareness')
G.edge['energyawareness']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('energyawareness','energyawareness')
G.edge['energyawareness']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('energyawareness','energy-awareness')
G.edge['energyawareness']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['energyawareness']['energy-awareness']['fill'] = 'red'
G.add_edge('energyawareness','energy-awareness')
G.edge['energyawareness']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('energyawareness','energyawareness')
G.edge['energyawareness']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['energyawareness']['energyawareness']['fill'] = 'red'
G.add_edge('energyawareness','energyawareness')
G.edge['energyawareness']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
app = Viewer(G)
app.mainloop()