import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('epmd','flash_recovery')
G.edge['epmd']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('epmd','prepare_param')
G.edge['epmd']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('epmd','prepare_param')
G.edge['epmd']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('epmd','flash_recovery')
G.edge['epmd']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['epmd']['flash_recovery']['fill'] = 'red'
G.add_edge('epmd','flash_recovery')
G.edge['epmd']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('epmd','prepare_param')
G.edge['epmd']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['epmd']['prepare_param']['fill'] = 'red'
G.add_edge('epmd','prepare_param')
G.edge['epmd']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('flash_recovery','flash_recovery')
G.edge['flash_recovery']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('flash_recovery','prepare_param')
G.edge['flash_recovery']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('flash_recovery','prepare_param')
G.edge['flash_recovery']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('flash_recovery','flash_recovery')
G.edge['flash_recovery']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['flash_recovery']['flash_recovery']['fill'] = 'red'
G.add_edge('flash_recovery','flash_recovery')
G.edge['flash_recovery']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('flash_recovery','prepare_param')
G.edge['flash_recovery']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['flash_recovery']['prepare_param']['fill'] = 'red'
G.add_edge('flash_recovery','prepare_param')
G.edge['flash_recovery']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('prepare_param','flash_recovery')
G.edge['prepare_param']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('prepare_param','prepare_param')
G.edge['prepare_param']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('prepare_param','prepare_param')
G.edge['prepare_param']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('prepare_param','flash_recovery')
G.edge['prepare_param']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['prepare_param']['flash_recovery']['fill'] = 'red'
G.add_edge('prepare_param','flash_recovery')
G.edge['prepare_param']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('prepare_param','prepare_param')
G.edge['prepare_param']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['prepare_param']['prepare_param']['fill'] = 'red'
G.add_edge('prepare_param','prepare_param')
G.edge['prepare_param']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()