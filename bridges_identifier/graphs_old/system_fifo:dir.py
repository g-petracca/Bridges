import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('immvibed','immvibed')
G.edge['immvibed']['immvibed']['write-read'] = '[open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('immvibed','init')
G.edge['immvibed']['init']['write-read'] = '[open open]'
G.add_edge('immvibed','init')
G.edge['immvibed']['init']['write-read'] = '[open open][setattr getattr]'
G.add_edge('immvibed','immvibed')
G.edge['immvibed']['immvibed']['write-read'] = '[open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['immvibed']['immvibed']['fill'] = 'red'
G.add_edge('immvibed','init')
G.edge['immvibed']['init']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['immvibed']['init']['fill'] = 'red'
G.add_edge('immvibed','immvibed')
G.edge['immvibed']['immvibed']['write-read'] = '[open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('immvibed','immvibed')
G.edge['immvibed']['immvibed']['write-read'] = '[open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('immvibed','init')
G.edge['immvibed']['init']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('immvibed','init')
G.edge['immvibed']['init']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init','immvibed')
G.edge['init']['immvibed']['write-read'] = '[open open]'
G.add_edge('init','init')
G.edge['init']['init']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init','init')
G.edge['init']['init']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('init','immvibed')
G.edge['init']['immvibed']['write-read'] = '[open open][write read]'
G.edge['init']['immvibed']['fill'] = 'red'
G.add_edge('init','init')
G.edge['init']['init']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['init']['init']['fill'] = 'red'
G.add_edge('init','immvibed')
G.edge['init']['immvibed']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('init','immvibed')
G.edge['init']['immvibed']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('init','init')
G.edge['init']['init']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('init','init')
G.edge['init']['init']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init','init')
G.edge['init']['init']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom]'
G.add_edge('mediaserver','immvibed')
G.edge['mediaserver']['immvibed']['write-read'] = '[open open]'
G.add_edge('mediaserver','init')
G.edge['mediaserver']['init']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','init')
G.edge['mediaserver']['init']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('mediaserver','immvibed')
G.edge['mediaserver']['immvibed']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['immvibed']['fill'] = 'red'
G.add_edge('mediaserver','init')
G.edge['mediaserver']['init']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['mediaserver']['init']['fill'] = 'red'
G.add_edge('mediaserver','immvibed')
G.edge['mediaserver']['immvibed']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('mediaserver','immvibed')
G.edge['mediaserver']['immvibed']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('mediaserver','init')
G.edge['mediaserver']['init']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('mediaserver','init')
G.edge['mediaserver']['init']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','immvibed')
G.edge['system_server']['immvibed']['write-read'] = '[open open]'
G.add_edge('system_server','init')
G.edge['system_server']['init']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','init')
G.edge['system_server']['init']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','immvibed')
G.edge['system_server']['immvibed']['write-read'] = '[open open][write read]'
G.edge['system_server']['immvibed']['fill'] = 'red'
G.add_edge('system_server','init')
G.edge['system_server']['init']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['init']['fill'] = 'red'
G.add_edge('system_server','immvibed')
G.edge['system_server']['immvibed']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('system_server','immvibed')
G.edge['system_server']['immvibed']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('system_server','init')
G.edge['system_server']['init']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','init')
G.edge['system_server']['init']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()