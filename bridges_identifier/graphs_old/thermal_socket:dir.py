import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('thermal-engine','thermal-engine')
G.edge['thermal-engine']['thermal-engine']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][open open][write read][append read][open open]'
G.add_edge('thermal-engine','thermal-engine')
G.edge['thermal-engine']['thermal-engine']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][open open][write read][append read][open open][add_name search]'
G.add_edge('thermal-engine','thermal-engine')
G.edge['thermal-engine']['thermal-engine']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][open open][write read][append read][open open][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()