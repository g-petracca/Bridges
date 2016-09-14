import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('adbd','itsonbs')
G.edge['adbd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('adbd','newAttr1')
G.edge['adbd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('adbd','shell')
G.edge['adbd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('adbd','installd')
G.edge['adbd']['installd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][setattr getattr]'
G.add_edge('adbd','itsonbs')
G.edge['adbd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('adbd','shell')
G.edge['adbd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('adbd','itsonbs')
G.edge['adbd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['adbd']['itsonbs']['fill'] = 'red'
G.add_edge('adbd','itsonbs')
G.edge['adbd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('adbd','newAttr1')
G.edge['adbd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['adbd']['newAttr1']['fill'] = 'red'
G.add_edge('adbd','shell')
G.edge['adbd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['adbd']['shell']['fill'] = 'red'
G.add_edge('adbd','shell')
G.edge['adbd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','itsonbs')
G.edge['commonplatformappdomain']['itsonbs']['write-read'] = '[write read]'
G.edge['commonplatformappdomain']['itsonbs']['fill'] = 'red'
G.add_edge('commonplatformappdomain','itsonbs')
G.edge['commonplatformappdomain']['itsonbs']['write-read'] = '[write read][append read]'
G.add_edge('commonplatformappdomain','newAttr1')
G.edge['commonplatformappdomain']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['commonplatformappdomain']['newAttr1']['fill'] = 'red'
G.add_edge('commonplatformappdomain','shell')
G.edge['commonplatformappdomain']['shell']['write-read'] = '[write read][setopt getopt][write read]'
G.edge['commonplatformappdomain']['shell']['fill'] = 'red'
G.add_edge('commonplatformappdomain','shell')
G.edge['commonplatformappdomain']['shell']['write-read'] = '[write read][setopt getopt][write read][append read]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][relabelto relabelfrom][setattr getattr]'
G.add_edge('installd','itsonbs')
G.edge['installd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('installd','shell')
G.edge['installd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][relabelto relabelfrom][setattr getattr][relabelto relabelfrom]'
G.add_edge('itsonbs','itsonbs')
G.edge['itsonbs']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('itsonbs','newAttr1')
G.edge['itsonbs']['newAttr1']['write-read'] = '[open open]'
G.add_edge('itsonbs','shell')
G.edge['itsonbs']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('itsonbs','installd')
G.edge['itsonbs']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('itsonbs','itsonbs')
G.edge['itsonbs']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('itsonbs','shell')
G.edge['itsonbs']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('itsonbs','itsonbs')
G.edge['itsonbs']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['itsonbs']['itsonbs']['fill'] = 'red'
G.add_edge('itsonbs','itsonbs')
G.edge['itsonbs']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('itsonbs','newAttr1')
G.edge['itsonbs']['newAttr1']['write-read'] = '[open open][write read]'
G.edge['itsonbs']['newAttr1']['fill'] = 'red'
G.add_edge('itsonbs','shell')
G.edge['itsonbs']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['itsonbs']['shell']['fill'] = 'red'
G.add_edge('itsonbs','shell')
G.edge['itsonbs']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','itsonbs')
G.edge['newAttr1']['itsonbs']['write-read'] = '[open open]'
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open execmod][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr1','shell')
G.edge['newAttr1']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr1','installd')
G.edge['newAttr1']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('newAttr1','itsonbs')
G.edge['newAttr1']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr1','shell')
G.edge['newAttr1']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('newAttr1','itsonbs')
G.edge['newAttr1']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr1']['itsonbs']['fill'] = 'red'
G.add_edge('newAttr1','itsonbs')
G.edge['newAttr1']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open execmod][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['newAttr1']['newAttr1']['fill'] = 'red'
G.add_edge('newAttr1','shell')
G.edge['newAttr1']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['newAttr1']['shell']['fill'] = 'red'
G.add_edge('newAttr1','shell')
G.edge['newAttr1']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('shell','itsonbs')
G.edge['shell']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('shell','newAttr1')
G.edge['shell']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('shell','shell')
G.edge['shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('shell','installd')
G.edge['shell']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr]'
G.add_edge('shell','itsonbs')
G.edge['shell']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('shell','shell')
G.edge['shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('shell','itsonbs')
G.edge['shell']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['shell']['itsonbs']['fill'] = 'red'
G.add_edge('shell','itsonbs')
G.edge['shell']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('shell','newAttr1')
G.edge['shell']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['shell']['newAttr1']['fill'] = 'red'
G.add_edge('shell','shell')
G.edge['shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['shell']['shell']['fill'] = 'red'
G.add_edge('shell','shell')
G.edge['shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('uncrypt','itsonbs')
G.edge['uncrypt']['itsonbs']['write-read'] = '[open open]'
G.add_edge('uncrypt','newAttr1')
G.edge['uncrypt']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('uncrypt','shell')
G.edge['uncrypt']['shell']['write-read'] = '[open open]'
G.add_edge('uncrypt','installd')
G.edge['uncrypt']['installd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('uncrypt','itsonbs')
G.edge['uncrypt']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('uncrypt','shell')
G.edge['uncrypt']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('uncrypt','itsonbs')
G.edge['uncrypt']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['uncrypt']['itsonbs']['fill'] = 'red'
G.add_edge('uncrypt','itsonbs')
G.edge['uncrypt']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('uncrypt','newAttr1')
G.edge['uncrypt']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['uncrypt']['newAttr1']['fill'] = 'red'
G.add_edge('uncrypt','shell')
G.edge['uncrypt']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['uncrypt']['shell']['fill'] = 'red'
G.add_edge('uncrypt','shell')
G.edge['uncrypt']['shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()