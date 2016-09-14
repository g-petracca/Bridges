import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('lptcpgc','lptcpgc')
G.edge['lptcpgc']['lptcpgc']['write-read'] = '[open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][write read]'
G.edge['lptcpgc']['lptcpgc']['fill'] = 'red'
app = Viewer(G)
app.mainloop()