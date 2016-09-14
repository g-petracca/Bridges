import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('connfwexe','connfwexe')
G.edge['connfwexe']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['connfwexe']['connfwexe']['fill'] = 'red'
app = Viewer(G)
app.mainloop()