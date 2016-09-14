import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('daemon_app_process','daemon_app_process')
G.edge['daemon_app_process']['daemon_app_process']['write-read'] = '[open open]'
G.add_edge('daemon_app_process','dumpstate')
G.edge['daemon_app_process']['dumpstate']['write-read'] = '[open open]'
G.add_edge('daemon_app_process','dumpsys')
G.edge['daemon_app_process']['dumpsys']['write-read'] = '[open open]'
G.add_edge('daemon_app_process','daemon_app_process')
G.edge['daemon_app_process']['daemon_app_process']['write-read'] = '[open open][write read]'
G.edge['daemon_app_process']['daemon_app_process']['fill'] = 'red'
G.add_edge('daemon_app_process','daemon_app_process')
G.edge['daemon_app_process']['daemon_app_process']['write-read'] = '[open open][write read][append read]'
G.add_edge('daemon_app_process','dumpstate')
G.edge['daemon_app_process']['dumpstate']['write-read'] = '[open open][write read]'
G.edge['daemon_app_process']['dumpstate']['fill'] = 'red'
G.add_edge('daemon_app_process','dumpstate')
G.edge['daemon_app_process']['dumpstate']['write-read'] = '[open open][write read][append read]'
G.add_edge('daemon_app_process','dumpsys')
G.edge['daemon_app_process']['dumpsys']['write-read'] = '[open open][write read]'
G.edge['daemon_app_process']['dumpsys']['fill'] = 'red'
G.add_edge('daemon_app_process','dumpsys')
G.edge['daemon_app_process']['dumpsys']['write-read'] = '[open open][write read][append read]'
G.add_edge('daemon_app_process','vdc')
G.edge['daemon_app_process']['vdc']['write-read'] = '[write read]'
G.edge['daemon_app_process']['vdc']['fill'] = 'red'
G.add_edge('dumpstate','daemon_app_process')
G.edge['dumpstate']['daemon_app_process']['write-read'] = '[open open]'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('dumpstate','dumpsys')
G.edge['dumpstate']['dumpsys']['write-read'] = '[open open]'
G.add_edge('dumpstate','daemon_app_process')
G.edge['dumpstate']['daemon_app_process']['write-read'] = '[open open][write read]'
G.edge['dumpstate']['daemon_app_process']['fill'] = 'red'
G.add_edge('dumpstate','daemon_app_process')
G.edge['dumpstate']['daemon_app_process']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['dumpstate']['dumpstate']['fill'] = 'red'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('dumpstate','dumpsys')
G.edge['dumpstate']['dumpsys']['write-read'] = '[open open][write read]'
G.edge['dumpstate']['dumpsys']['fill'] = 'red'
G.add_edge('dumpstate','dumpsys')
G.edge['dumpstate']['dumpsys']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpstate','vdc')
G.edge['dumpstate']['vdc']['write-read'] = '[write read]'
G.edge['dumpstate']['vdc']['fill'] = 'red'
G.add_edge('dumpsys','daemon_app_process')
G.edge['dumpsys']['daemon_app_process']['write-read'] = '[open open]'
G.add_edge('dumpsys','dumpstate')
G.edge['dumpsys']['dumpstate']['write-read'] = '[open open]'
G.add_edge('dumpsys','dumpsys')
G.edge['dumpsys']['dumpsys']['write-read'] = '[open open]'
G.add_edge('dumpsys','daemon_app_process')
G.edge['dumpsys']['daemon_app_process']['write-read'] = '[open open][write read]'
G.edge['dumpsys']['daemon_app_process']['fill'] = 'red'
G.add_edge('dumpsys','daemon_app_process')
G.edge['dumpsys']['daemon_app_process']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpsys','dumpstate')
G.edge['dumpsys']['dumpstate']['write-read'] = '[open open][write read]'
G.edge['dumpsys']['dumpstate']['fill'] = 'red'
G.add_edge('dumpsys','dumpstate')
G.edge['dumpsys']['dumpstate']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpsys','dumpsys')
G.edge['dumpsys']['dumpsys']['write-read'] = '[open open][write read]'
G.edge['dumpsys']['dumpsys']['fill'] = 'red'
G.add_edge('dumpsys','dumpsys')
G.edge['dumpsys']['dumpsys']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpsys','vdc')
G.edge['dumpsys']['vdc']['write-read'] = '[write read]'
G.edge['dumpsys']['vdc']['fill'] = 'red'
app = Viewer(G)
app.mainloop()