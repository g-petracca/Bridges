import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('mdm_helper','mdm_helper')
G.edge['mdm_helper']['mdm_helper']['write-read'] = '[open open][setattr getattr][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][open open][write read][append read][open open][write read][add_name search][open open][write read][open open][write read][open open][write read][open open]'
G.add_edge('mdm_helper','mdm_helper')
G.edge['mdm_helper']['mdm_helper']['write-read'] = '[open open][setattr getattr][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][open open][write read][append read][open open][write read][add_name search][open open][write read][open open][write read][open open][write read][open open][write read]'
G.edge['mdm_helper']['mdm_helper']['fill'] = 'red'
app = Viewer(G)
app.mainloop()