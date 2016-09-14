import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('appdomain','newAttr98')
G.edge['appdomain']['newAttr98']['write-read'] = '[write read]'
G.edge['appdomain']['newAttr98']['fill'] = 'red'
G.add_edge('appdomain','newAttr98')
G.edge['appdomain']['newAttr98']['write-read'] = '[write read][append read]'
G.add_edge('appdomain','zygote')
G.edge['appdomain']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][append read]'
G.add_edge('appdomain','zygote')
G.edge['appdomain']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][append read][write read]'
G.edge['appdomain']['zygote']['fill'] = 'red'
G.add_edge('fixmo_app','newAttr98')
G.edge['fixmo_app']['newAttr98']['write-read'] = '[open open]'
G.add_edge('fixmo_app','newAttr98')
G.edge['fixmo_app']['newAttr98']['write-read'] = '[open open][write read]'
G.edge['fixmo_app']['newAttr98']['fill'] = 'red'
G.add_edge('fixmo_app','newAttr98')
G.edge['fixmo_app']['newAttr98']['write-read'] = '[open open][write read][append read]'
G.add_edge('fixmo_app','zygote')
G.edge['fixmo_app']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][add_name search][remove_name search][append read]'
G.add_edge('fixmo_app','zygote')
G.edge['fixmo_app']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][add_name search][remove_name search][append read][write read]'
G.edge['fixmo_app']['zygote']['fill'] = 'red'
G.add_edge('good_app','newAttr98')
G.edge['good_app']['newAttr98']['write-read'] = '[open open]'
G.add_edge('good_app','newAttr98')
G.edge['good_app']['newAttr98']['write-read'] = '[open open][write read]'
G.edge['good_app']['newAttr98']['fill'] = 'red'
G.add_edge('good_app','newAttr98')
G.edge['good_app']['newAttr98']['write-read'] = '[open open][write read][append read]'
G.add_edge('good_app','zygote')
G.edge['good_app']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][append read]'
G.add_edge('good_app','zygote')
G.edge['good_app']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][append read][write read]'
G.edge['good_app']['zygote']['fill'] = 'red'
G.add_edge('newAttr98','newAttr98')
G.edge['newAttr98']['newAttr98']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr98','newAttr98')
G.edge['newAttr98']['newAttr98']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['newAttr98']['newAttr98']['fill'] = 'red'
G.add_edge('newAttr98','newAttr98')
G.edge['newAttr98']['newAttr98']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('newAttr98','zygote')
G.edge['newAttr98']['zygote']['write-read'] = '[append read]'
G.add_edge('newAttr98','zygote')
G.edge['newAttr98']['zygote']['write-read'] = '[append read][write read]'
G.edge['newAttr98']['zygote']['fill'] = 'red'
G.add_edge('system_server','newAttr98')
G.edge['system_server']['newAttr98']['write-read'] = '[write read]'
G.edge['system_server']['newAttr98']['fill'] = 'red'
G.add_edge('system_server','newAttr98')
G.edge['system_server']['newAttr98']['write-read'] = '[write read][append read]'
G.add_edge('system_server','zygote')
G.edge['system_server']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][write read][write read][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][append read]'
G.add_edge('system_server','zygote')
G.edge['system_server']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][write read][write read][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][append read][write read]'
G.edge['system_server']['zygote']['fill'] = 'red'
G.add_edge('vmware_app','newAttr98')
G.edge['vmware_app']['newAttr98']['write-read'] = '[write read]'
G.edge['vmware_app']['newAttr98']['fill'] = 'red'
G.add_edge('vmware_app','newAttr98')
G.edge['vmware_app']['newAttr98']['write-read'] = '[write read][append read]'
G.add_edge('vmware_app','zygote')
G.edge['vmware_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][append read]'
G.add_edge('vmware_app','zygote')
G.edge['vmware_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][append read][write read]'
G.edge['vmware_app']['zygote']['fill'] = 'red'
G.add_edge('zygote','newAttr98')
G.edge['zygote']['newAttr98']['write-read'] = '[write read]'
G.edge['zygote']['newAttr98']['fill'] = 'red'
G.add_edge('zygote','newAttr98')
G.edge['zygote']['newAttr98']['write-read'] = '[write read][append read]'
G.add_edge('zygote','zygote')
G.edge['zygote']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setpgid getpgid][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][append read]'
G.add_edge('zygote','zygote')
G.edge['zygote']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setpgid getpgid][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][append read][write read]'
G.edge['zygote']['zygote']['fill'] = 'red'
app = Viewer(G)
app.mainloop()