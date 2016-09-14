import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('cnd','trusted_app_domain')
G.edge['cnd']['trusted_app_domain']['write-read'] = '[open open]'
G.add_edge('cnd','trusted_app_domain')
G.edge['cnd']['trusted_app_domain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cnd','trusted_app_domain')
G.edge['cnd']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cnd']['trusted_app_domain']['fill'] = 'red'
G.add_edge('cnd','trusted_app_domain')
G.edge['cnd']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cnd','trusted_app_domain')
G.edge['cnd']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('lmkd','trusted_app_domain')
G.edge['lmkd']['trusted_app_domain']['write-read'] = '[open open]'
G.add_edge('lmkd','trusted_app_domain')
G.edge['lmkd']['trusted_app_domain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('lmkd','trusted_app_domain')
G.edge['lmkd']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['lmkd']['trusted_app_domain']['fill'] = 'red'
G.add_edge('lmkd','trusted_app_domain')
G.edge['lmkd']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('lmkd','trusted_app_domain')
G.edge['lmkd']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('surfaceflinger','trusted_app_domain')
G.edge['surfaceflinger']['trusted_app_domain']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','trusted_app_domain')
G.edge['surfaceflinger']['trusted_app_domain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('surfaceflinger','trusted_app_domain')
G.edge['surfaceflinger']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['surfaceflinger']['trusted_app_domain']['fill'] = 'red'
G.add_edge('surfaceflinger','trusted_app_domain')
G.edge['surfaceflinger']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('surfaceflinger','trusted_app_domain')
G.edge['surfaceflinger']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('trusted_app_domain','trusted_app_domain')
G.edge['trusted_app_domain']['trusted_app_domain']['write-read'] = '[open open]'
G.add_edge('trusted_app_domain','trusted_app_domain')
G.edge['trusted_app_domain']['trusted_app_domain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trusted_app_domain','trusted_app_domain')
G.edge['trusted_app_domain']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['trusted_app_domain']['trusted_app_domain']['fill'] = 'red'
G.add_edge('trusted_app_domain','trusted_app_domain')
G.edge['trusted_app_domain']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('trusted_app_domain','trusted_app_domain')
G.edge['trusted_app_domain']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','trusted_app_domain')
G.edge['zygote']['trusted_app_domain']['write-read'] = '[setattr getattr]'
G.add_edge('zygote','trusted_app_domain')
G.edge['zygote']['trusted_app_domain']['write-read'] = '[setattr getattr][add_name search]'
G.add_edge('zygote','trusted_app_domain')
G.edge['zygote']['trusted_app_domain']['write-read'] = '[setattr getattr][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()