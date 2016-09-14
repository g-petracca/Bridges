import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('bluetooth','installd')
G.edge['bluetooth']['installd']['write-read'] = '[setattr getattr][open open]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('bluetooth','installd')
G.edge['bluetooth']['installd']['write-read'] = '[setattr getattr][open open][setattr getattr]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['bluetooth']['bluetooth']['fill'] = 'red'
G.add_edge('bluetooth','installd')
G.edge['bluetooth']['installd']['write-read'] = '[setattr getattr][open open][setattr getattr][write read]'
G.edge['bluetooth']['installd']['fill'] = 'red'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('bluetooth','installd')
G.edge['bluetooth']['installd']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][add_name search]'
G.add_edge('bluetooth','installd')
G.edge['bluetooth']['installd']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('commonplatformappdomain','bluetooth')
G.edge['commonplatformappdomain']['bluetooth']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','installd')
G.edge['commonplatformappdomain']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('commonplatformappdomain','bluetooth')
G.edge['commonplatformappdomain']['bluetooth']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','installd')
G.edge['commonplatformappdomain']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','bluetooth')
G.edge['commonplatformappdomain']['bluetooth']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['bluetooth']['fill'] = 'red'
G.add_edge('commonplatformappdomain','installd')
G.edge['commonplatformappdomain']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['installd']['fill'] = 'red'
G.add_edge('commonplatformappdomain','bluetooth')
G.edge['commonplatformappdomain']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('commonplatformappdomain','bluetooth')
G.edge['commonplatformappdomain']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('commonplatformappdomain','installd')
G.edge['commonplatformappdomain']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('commonplatformappdomain','installd')
G.edge['commonplatformappdomain']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','bluetooth')
G.edge['installd']['bluetooth']['write-read'] = '[setattr getattr][open open]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('installd','bluetooth')
G.edge['installd']['bluetooth']['write-read'] = '[setattr getattr][open open][setattr getattr]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('installd','bluetooth')
G.edge['installd']['bluetooth']['write-read'] = '[setattr getattr][open open][setattr getattr][write read]'
G.edge['installd']['bluetooth']['fill'] = 'red'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['installd']['installd']['fill'] = 'red'
G.add_edge('installd','bluetooth')
G.edge['installd']['bluetooth']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','bluetooth')
G.edge['installd']['bluetooth']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom]'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read]'
G.edge['system_server']['bluetooth']['fill'] = 'red'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['system_server']['installd']['fill'] = 'red'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search]'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()