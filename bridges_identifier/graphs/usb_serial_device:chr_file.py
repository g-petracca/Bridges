import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('ddexe','ddexe')
G.edge['ddexe']['ddexe']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('ddexe','diagexe')
G.edge['ddexe']['diagexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ddexe','ddexe')
G.edge['ddexe']['ddexe']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['ddexe']['ddexe']['fill'] = 'red'
G.add_edge('ddexe','ddexe')
G.edge['ddexe']['ddexe']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('ddexe','diagexe')
G.edge['ddexe']['diagexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['ddexe']['diagexe']['fill'] = 'red'
G.add_edge('diagexe','ddexe')
G.edge['diagexe']['ddexe']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('diagexe','diagexe')
G.edge['diagexe']['diagexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('diagexe','ddexe')
G.edge['diagexe']['ddexe']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['diagexe']['ddexe']['fill'] = 'red'
G.add_edge('diagexe','ddexe')
G.edge['diagexe']['ddexe']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('diagexe','diagexe')
G.edge['diagexe']['diagexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['diagexe']['diagexe']['fill'] = 'red'
app = Viewer(G)
app.mainloop()