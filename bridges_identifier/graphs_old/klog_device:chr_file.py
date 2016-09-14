import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('sdcardd','healthd')
G.edge['sdcardd']['healthd']['write-read'] = '[write read][add_name search][remove_name search][open open]'
G.add_edge('sdcardd','sdcardd')
G.edge['sdcardd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('sdcardd','ueventd')
G.edge['sdcardd']['ueventd']['write-read'] = '[write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('sdcardd','vold')
G.edge['sdcardd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sdcardd','watchdogd')
G.edge['sdcardd']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('sdcardd','sdcardd')
G.edge['sdcardd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('sdcardd','healthd')
G.edge['sdcardd']['healthd']['write-read'] = '[write read][add_name search][remove_name search][open open][write read]'
G.edge['sdcardd']['healthd']['fill'] = 'red'
G.add_edge('sdcardd','sdcardd')
G.edge['sdcardd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['sdcardd']['sdcardd']['fill'] = 'red'
G.add_edge('sdcardd','sdcardd')
G.edge['sdcardd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('sdcardd','ueventd')
G.edge['sdcardd']['ueventd']['write-read'] = '[write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['sdcardd']['ueventd']['fill'] = 'red'
G.add_edge('sdcardd','vold')
G.edge['sdcardd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['sdcardd']['vold']['fill'] = 'red'
G.add_edge('sdcardd','watchdogd')
G.edge['sdcardd']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['sdcardd']['watchdogd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()