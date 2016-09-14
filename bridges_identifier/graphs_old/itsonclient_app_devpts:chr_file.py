import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('itsonclient_app','itsonclient_app')
G.edge['itsonclient_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('itsonclient_app','itsonclient_app')
G.edge['itsonclient_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['itsonclient_app']['itsonclient_app']['fill'] = 'red'
app = Viewer(G)
app.mainloop()