import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('cnd','trusted_app_domain')
G.edge['cnd']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('cnd','trusted_app_domain')
G.edge['cnd']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('cnd','lmkd')
G.edge['cnd']['lmkd']['write-read'] = '[write read]'
G.edge['cnd']['lmkd']['fill'] = 'red'
G.add_edge('cnd','system_server')
G.edge['cnd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['cnd']['system_server']['fill'] = 'red'
G.add_edge('cnd','trusted_app_domain')
G.edge['cnd']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['cnd']['trusted_app_domain']['fill'] = 'red'
G.add_edge('cnd','trusted_app_domain')
G.edge['cnd']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('lmkd','trusted_app_domain')
G.edge['lmkd']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('lmkd','trusted_app_domain')
G.edge['lmkd']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('lmkd','lmkd')
G.edge['lmkd']['lmkd']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][write read]'
G.edge['lmkd']['lmkd']['fill'] = 'red'
G.add_edge('lmkd','system_server')
G.edge['lmkd']['system_server']['write-read'] = '[open open][write read][append read][write read]'
G.edge['lmkd']['system_server']['fill'] = 'red'
G.add_edge('lmkd','trusted_app_domain')
G.edge['lmkd']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['lmkd']['trusted_app_domain']['fill'] = 'red'
G.add_edge('lmkd','trusted_app_domain')
G.edge['lmkd']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('surfaceflinger','trusted_app_domain')
G.edge['surfaceflinger']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('surfaceflinger','trusted_app_domain')
G.edge['surfaceflinger']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('surfaceflinger','lmkd')
G.edge['surfaceflinger']['lmkd']['write-read'] = '[write read][open open][write read][append read][write read]'
G.edge['surfaceflinger']['lmkd']['fill'] = 'red'
G.add_edge('surfaceflinger','system_server')
G.edge['surfaceflinger']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][write read]'
G.edge['surfaceflinger']['system_server']['fill'] = 'red'
G.add_edge('surfaceflinger','trusted_app_domain')
G.edge['surfaceflinger']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['surfaceflinger']['trusted_app_domain']['fill'] = 'red'
G.add_edge('surfaceflinger','trusted_app_domain')
G.edge['surfaceflinger']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('trusted_app_domain','trusted_app_domain')
G.edge['trusted_app_domain']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('trusted_app_domain','trusted_app_domain')
G.edge['trusted_app_domain']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('trusted_app_domain','lmkd')
G.edge['trusted_app_domain']['lmkd']['write-read'] = '[write read]'
G.edge['trusted_app_domain']['lmkd']['fill'] = 'red'
G.add_edge('trusted_app_domain','system_server')
G.edge['trusted_app_domain']['system_server']['write-read'] = '[open open][write read][append read][write read][write read]'
G.edge['trusted_app_domain']['system_server']['fill'] = 'red'
G.add_edge('trusted_app_domain','trusted_app_domain')
G.edge['trusted_app_domain']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['trusted_app_domain']['trusted_app_domain']['fill'] = 'red'
G.add_edge('trusted_app_domain','trusted_app_domain')
G.edge['trusted_app_domain']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('zygote','trusted_app_domain')
G.edge['zygote']['trusted_app_domain']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open]'
G.add_edge('zygote','trusted_app_domain')
G.edge['zygote']['trusted_app_domain']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('zygote','lmkd')
G.edge['zygote']['lmkd']['write-read'] = '[remove_name search][write read]'
G.edge['zygote']['lmkd']['fill'] = 'red'
G.add_edge('zygote','system_server')
G.edge['zygote']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read][write read]'
G.edge['zygote']['system_server']['fill'] = 'red'
G.add_edge('zygote','trusted_app_domain')
G.edge['zygote']['trusted_app_domain']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['zygote']['trusted_app_domain']['fill'] = 'red'
G.add_edge('zygote','trusted_app_domain')
G.edge['zygote']['trusted_app_domain']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()