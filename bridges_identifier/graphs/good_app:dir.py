import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('bridged_platform_app','bridged_platform_app')
G.edge['bridged_platform_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('bridged_platform_app','lmkd')
G.edge['bridged_platform_app']['lmkd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('bridged_platform_app','bridged_platform_app')
G.edge['bridged_platform_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['bridged_platform_app']['bridged_platform_app']['fill'] = 'red'
G.add_edge('bridged_platform_app','lmkd')
G.edge['bridged_platform_app']['lmkd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['bridged_platform_app']['lmkd']['fill'] = 'red'
G.add_edge('bridged_platform_app','bridged_platform_app')
G.edge['bridged_platform_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('bridged_platform_app','bridged_platform_app')
G.edge['bridged_platform_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('bridged_platform_app','lmkd')
G.edge['bridged_platform_app']['lmkd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('bridged_platform_app','lmkd')
G.edge['bridged_platform_app']['lmkd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('lmkd','bridged_platform_app')
G.edge['lmkd']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('lmkd','lmkd')
G.edge['lmkd']['lmkd']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('lmkd','bridged_platform_app')
G.edge['lmkd']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['lmkd']['bridged_platform_app']['fill'] = 'red'
G.add_edge('lmkd','lmkd')
G.edge['lmkd']['lmkd']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read]'
G.edge['lmkd']['lmkd']['fill'] = 'red'
G.add_edge('lmkd','bridged_platform_app')
G.edge['lmkd']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('lmkd','bridged_platform_app')
G.edge['lmkd']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('lmkd','lmkd')
G.edge['lmkd']['lmkd']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search]'
G.add_edge('lmkd','lmkd')
G.edge['lmkd']['lmkd']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search]'
G.add_edge('servicemanager','bridged_platform_app')
G.edge['servicemanager']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][add_name search][remove_name search][add_name search]'
G.add_edge('servicemanager','bridged_platform_app')
G.edge['servicemanager']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('servicemanager','lmkd')
G.edge['servicemanager']['lmkd']['write-read'] = '[open open][write read][append read][open open][write read][append read][add_name search][remove_name search][add_name search]'
G.add_edge('servicemanager','lmkd')
G.edge['servicemanager']['lmkd']['write-read'] = '[open open][write read][append read][open open][write read][append read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('system','bridged_platform_app')
G.edge['system']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system','lmkd')
G.edge['system']['lmkd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system','bridged_platform_app')
G.edge['system']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['system']['bridged_platform_app']['fill'] = 'red'
G.add_edge('system','lmkd')
G.edge['system']['lmkd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['system']['lmkd']['fill'] = 'red'
G.add_edge('system','bridged_platform_app')
G.edge['system']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('system','bridged_platform_app')
G.edge['system']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('system','lmkd')
G.edge['system']['lmkd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('system','lmkd')
G.edge['system']['lmkd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('system_app','bridged_platform_app')
G.edge['system_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','lmkd')
G.edge['system_app']['lmkd']['write-read'] = '[remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','bridged_platform_app')
G.edge['system_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_app']['bridged_platform_app']['fill'] = 'red'
G.add_edge('system_app','lmkd')
G.edge['system_app']['lmkd']['write-read'] = '[remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_app']['lmkd']['fill'] = 'red'
G.add_edge('system_app','bridged_platform_app')
G.edge['system_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('system_app','bridged_platform_app')
G.edge['system_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('system_app','lmkd')
G.edge['system_app']['lmkd']['write-read'] = '[remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('system_app','lmkd')
G.edge['system_app']['lmkd']['write-read'] = '[remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','bridged_platform_app')
G.edge['s_system_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','lmkd')
G.edge['s_system_app']['lmkd']['write-read'] = '[remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','bridged_platform_app')
G.edge['s_system_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['s_system_app']['bridged_platform_app']['fill'] = 'red'
G.add_edge('s_system_app','lmkd')
G.edge['s_system_app']['lmkd']['write-read'] = '[remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['s_system_app']['lmkd']['fill'] = 'red'
G.add_edge('s_system_app','bridged_platform_app')
G.edge['s_system_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('s_system_app','bridged_platform_app')
G.edge['s_system_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','lmkd')
G.edge['s_system_app']['lmkd']['write-read'] = '[remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('s_system_app','lmkd')
G.edge['s_system_app']['lmkd']['write-read'] = '[remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()