import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][write read][write read][write read]'
G.edge['dumpstate']['dumpstate']['fill'] = 'red'
G.add_edge('dumpstate','dumpsys')
G.edge['dumpstate']['dumpsys']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][write read][write read][append read][write read]'
G.edge['dumpstate']['dumpsys']['fill'] = 'red'
G.add_edge('dumpstate','vdc')
G.edge['dumpstate']['vdc']['write-read'] = '[write read][write read][write read][write read]'
G.edge['dumpstate']['vdc']['fill'] = 'red'
G.add_edge('dumpsys','dumpstate')
G.edge['dumpsys']['dumpstate']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][write read][open open][write read][append read][write read][write read][write read]'
G.edge['dumpsys']['dumpstate']['fill'] = 'red'
G.add_edge('dumpsys','dumpsys')
G.edge['dumpsys']['dumpsys']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][write read][open open][write read][append read][write read]'
G.edge['dumpsys']['dumpsys']['fill'] = 'red'
G.add_edge('dumpsys','vdc')
G.edge['dumpsys']['vdc']['write-read'] = '[write read][write read][write read]'
G.edge['dumpsys']['vdc']['fill'] = 'red'
G.add_edge('vdc','dumpstate')
G.edge['vdc']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['vdc']['dumpstate']['fill'] = 'red'
G.add_edge('vdc','dumpsys')
G.edge['vdc']['dumpsys']['write-read'] = '[write read]'
G.edge['vdc']['dumpsys']['fill'] = 'red'
G.add_edge('vdc','vdc')
G.edge['vdc']['vdc']['write-read'] = '[write read][write read][write read]'
G.edge['vdc']['vdc']['fill'] = 'red'
app = Viewer(G)
app.mainloop()