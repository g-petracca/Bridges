import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('lpm','lpm')
G.edge['lpm']['lpm']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('lpm','platformappdomain')
G.edge['lpm']['platformappdomain']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('lpm','surfaceflinger')
G.edge['lpm']['surfaceflinger']['write-read'] = '[write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open]'
G.add_edge('lpm','wfdservice')
G.edge['lpm']['wfdservice']['write-read'] = '[write read][append read][open open][write read][append read][open open]'
G.add_edge('lpm','lpm')
G.edge['lpm']['lpm']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['lpm']['lpm']['fill'] = 'red'
G.add_edge('lpm','lpm')
G.edge['lpm']['lpm']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('lpm','platformappdomain')
G.edge['lpm']['platformappdomain']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['lpm']['platformappdomain']['fill'] = 'red'
G.add_edge('lpm','platformappdomain')
G.edge['lpm']['platformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('lpm','surfaceflinger')
G.edge['lpm']['surfaceflinger']['write-read'] = '[write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read]'
G.edge['lpm']['surfaceflinger']['fill'] = 'red'
G.add_edge('lpm','surfaceflinger')
G.edge['lpm']['surfaceflinger']['write-read'] = '[write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read]'
G.add_edge('lpm','surfaceflinger')
G.edge['lpm']['surfaceflinger']['write-read'] = '[write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['lpm']['surfaceflinger']['fill'] = 'red'
G.add_edge('lpm','wfdservice')
G.edge['lpm']['wfdservice']['write-read'] = '[write read][append read][open open][write read][append read][open open][write read]'
G.edge['lpm']['wfdservice']['fill'] = 'red'
G.add_edge('lpm','wfdservice')
G.edge['lpm']['wfdservice']['write-read'] = '[write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('platformappdomain','lpm')
G.edge['platformappdomain']['lpm']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('platformappdomain','platformappdomain')
G.edge['platformappdomain']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('platformappdomain','surfaceflinger')
G.edge['platformappdomain']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('platformappdomain','wfdservice')
G.edge['platformappdomain']['wfdservice']['write-read'] = '[open open]'
G.add_edge('platformappdomain','lpm')
G.edge['platformappdomain']['lpm']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['platformappdomain']['lpm']['fill'] = 'red'
G.add_edge('platformappdomain','lpm')
G.edge['platformappdomain']['lpm']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('platformappdomain','platformappdomain')
G.edge['platformappdomain']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['platformappdomain']['platformappdomain']['fill'] = 'red'
G.add_edge('platformappdomain','platformappdomain')
G.edge['platformappdomain']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('platformappdomain','surfaceflinger')
G.edge['platformappdomain']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['platformappdomain']['surfaceflinger']['fill'] = 'red'
G.add_edge('platformappdomain','surfaceflinger')
G.edge['platformappdomain']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('platformappdomain','surfaceflinger')
G.edge['platformappdomain']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['platformappdomain']['surfaceflinger']['fill'] = 'red'
G.add_edge('platformappdomain','wfdservice')
G.edge['platformappdomain']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['platformappdomain']['wfdservice']['fill'] = 'red'
G.add_edge('platformappdomain','wfdservice')
G.edge['platformappdomain']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','lpm')
G.edge['surfaceflinger']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('surfaceflinger','platformappdomain')
G.edge['surfaceflinger']['platformappdomain']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('surfaceflinger','wfdservice')
G.edge['surfaceflinger']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('surfaceflinger','lpm')
G.edge['surfaceflinger']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['surfaceflinger']['lpm']['fill'] = 'red'
G.add_edge('surfaceflinger','lpm')
G.edge['surfaceflinger']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('surfaceflinger','platformappdomain')
G.edge['surfaceflinger']['platformappdomain']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['surfaceflinger']['platformappdomain']['fill'] = 'red'
G.add_edge('surfaceflinger','platformappdomain')
G.edge['surfaceflinger']['platformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['surfaceflinger']['surfaceflinger']['fill'] = 'red'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['surfaceflinger']['surfaceflinger']['fill'] = 'red'
G.add_edge('surfaceflinger','wfdservice')
G.edge['surfaceflinger']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['surfaceflinger']['wfdservice']['fill'] = 'red'
G.add_edge('surfaceflinger','wfdservice')
G.edge['surfaceflinger']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('wfdservice','lpm')
G.edge['wfdservice']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open]'
G.add_edge('wfdservice','platformappdomain')
G.edge['wfdservice']['platformappdomain']['write-read'] = '[open open]'
G.add_edge('wfdservice','surfaceflinger')
G.edge['wfdservice']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('wfdservice','wfdservice')
G.edge['wfdservice']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('wfdservice','lpm')
G.edge['wfdservice']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read]'
G.edge['wfdservice']['lpm']['fill'] = 'red'
G.add_edge('wfdservice','lpm')
G.edge['wfdservice']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read][append read]'
G.add_edge('wfdservice','platformappdomain')
G.edge['wfdservice']['platformappdomain']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['platformappdomain']['fill'] = 'red'
G.add_edge('wfdservice','platformappdomain')
G.edge['wfdservice']['platformappdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','surfaceflinger')
G.edge['wfdservice']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['wfdservice']['surfaceflinger']['fill'] = 'red'
G.add_edge('wfdservice','surfaceflinger')
G.edge['wfdservice']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('wfdservice','surfaceflinger')
G.edge['wfdservice']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['wfdservice']['surfaceflinger']['fill'] = 'red'
G.add_edge('wfdservice','wfdservice')
G.edge['wfdservice']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['wfdservice']['wfdservice']['fill'] = 'red'
G.add_edge('wfdservice','wfdservice')
G.edge['wfdservice']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()