import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('bridged_platform_app','bridged_platform_app')
G.edge['bridged_platform_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][write read]'
G.edge['bridged_platform_app']['bridged_platform_app']['fill'] = 'red'
app = Viewer(G)
app.mainloop()