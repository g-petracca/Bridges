import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('auditd','auditd')
G.edge['auditd']['auditd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][open open][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['auditd']['auditd']['fill'] = 'red'
G.add_edge('auditd','logd')
G.edge['auditd']['logd']['write-read'] = '[write read]'
G.edge['auditd']['logd']['fill'] = 'red'
G.add_edge('auditd','logd')
G.edge['auditd']['logd']['write-read'] = '[write read][append read]'
G.add_edge('logd','logd')
G.edge['logd']['logd']['write-read'] = '[setattr getattr]'
G.add_edge('logd','auditd')
G.edge['logd']['auditd']['write-read'] = '[write read]'
G.edge['logd']['auditd']['fill'] = 'red'
G.add_edge('logd','logd')
G.edge['logd']['logd']['write-read'] = '[setattr getattr][write read]'
G.edge['logd']['logd']['fill'] = 'red'
G.add_edge('logd','logd')
G.edge['logd']['logd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('logd','logd')
G.edge['logd']['logd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
app = Viewer(G)
app.mainloop()