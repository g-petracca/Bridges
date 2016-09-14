import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('logwrapper','logwrapper')
G.edge['logwrapper']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['logwrapper']['logwrapper']['fill'] = 'red'
app = Viewer(G)
app.mainloop()