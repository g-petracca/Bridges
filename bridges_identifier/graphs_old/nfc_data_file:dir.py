import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('commonplatformappdomain','installd')
G.edge['commonplatformappdomain']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][open open]'
G.add_edge('commonplatformappdomain','nfc')
G.edge['commonplatformappdomain']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('commonplatformappdomain','installd')
G.edge['commonplatformappdomain']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','nfc')
G.edge['commonplatformappdomain']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','installd')
G.edge['commonplatformappdomain']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['installd']['fill'] = 'red'
G.add_edge('commonplatformappdomain','nfc')
G.edge['commonplatformappdomain']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['nfc']['fill'] = 'red'
G.add_edge('commonplatformappdomain','installd')
G.edge['commonplatformappdomain']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search]'
G.add_edge('commonplatformappdomain','installd')
G.edge['commonplatformappdomain']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('commonplatformappdomain','nfc')
G.edge['commonplatformappdomain']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('commonplatformappdomain','nfc')
G.edge['commonplatformappdomain']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open]'
G.add_edge('installd','nfc')
G.edge['installd']['nfc']['write-read'] = '[setattr getattr][open open]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr]'
G.add_edge('installd','nfc')
G.edge['installd']['nfc']['write-read'] = '[setattr getattr][open open][setattr getattr]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read]'
G.edge['installd']['installd']['fill'] = 'red'
G.add_edge('installd','nfc')
G.edge['installd']['nfc']['write-read'] = '[setattr getattr][open open][setattr getattr][write read]'
G.edge['installd']['nfc']['fill'] = 'red'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','nfc')
G.edge['installd']['nfc']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','nfc')
G.edge['installd']['nfc']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom]'
G.add_edge('nfc','installd')
G.edge['nfc']['installd']['write-read'] = '[setattr getattr][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('nfc','nfc')
G.edge['nfc']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('nfc','installd')
G.edge['nfc']['installd']['write-read'] = '[setattr getattr][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('nfc','nfc')
G.edge['nfc']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('nfc','installd')
G.edge['nfc']['installd']['write-read'] = '[setattr getattr][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['nfc']['installd']['fill'] = 'red'
G.add_edge('nfc','nfc')
G.edge['nfc']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['nfc']['nfc']['fill'] = 'red'
G.add_edge('nfc','installd')
G.edge['nfc']['installd']['write-read'] = '[setattr getattr][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('nfc','installd')
G.edge['nfc']['installd']['write-read'] = '[setattr getattr][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('nfc','nfc')
G.edge['nfc']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('nfc','nfc')
G.edge['nfc']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][setattr getattr][open open][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][relabelto relabelfrom][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('system_server','nfc')
G.edge['system_server']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][setattr getattr][open open][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][relabelto relabelfrom][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read]'
G.edge['system_server']['installd']['fill'] = 'red'
G.add_edge('system_server','nfc')
G.edge['system_server']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read]'
G.edge['system_server']['nfc']['fill'] = 'red'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][setattr getattr][open open][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][relabelto relabelfrom][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read][add_name search]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][setattr getattr][open open][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][relabelto relabelfrom][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','nfc')
G.edge['system_server']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][add_name search]'
G.add_edge('system_server','nfc')
G.edge['system_server']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()