import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('bridged_platform_app','bridged_platform_app')
G.edge['bridged_platform_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bridged_platform_app','bridged_platform_app')
G.edge['bridged_platform_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['bridged_platform_app']['bridged_platform_app']['fill'] = 'red'
G.add_edge('bridged_platform_app','bridged_platform_app')
G.edge['bridged_platform_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('epmd','bridged_platform_app')
G.edge['epmd']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('epmd','bridged_platform_app')
G.edge['epmd']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['epmd']['bridged_platform_app']['fill'] = 'red'
G.add_edge('epmd','bridged_platform_app')
G.edge['epmd']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('mediaserver','bridged_platform_app')
G.edge['mediaserver']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mediaserver','bridged_platform_app')
G.edge['mediaserver']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['mediaserver']['bridged_platform_app']['fill'] = 'red'
G.add_edge('mediaserver','bridged_platform_app')
G.edge['mediaserver']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()