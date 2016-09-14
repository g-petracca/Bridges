import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('adbd','adbd')
G.edge['adbd']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('adbd','dumpstate')
G.edge['adbd']['dumpstate']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('adbd','ime_app')
G.edge['adbd']['ime_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('adbd','itsonbs')
G.edge['adbd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('adbd','knox_system_app')
G.edge['adbd']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('adbd','mediaserver')
G.edge['adbd']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('adbd','newAttr1')
G.edge['adbd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][open open]'
G.add_edge('adbd','qseecomd')
G.edge['adbd']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('adbd','shell')
G.edge['adbd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('adbd','s_system_app')
G.edge['adbd']['s_system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('adbd','s_system_app')
G.edge['adbd']['s_system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('adbd','sysprof')
G.edge['adbd']['sysprof']['write-read'] = '[open open]'
G.add_edge('adbd','system_app')
G.edge['adbd']['system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('adbd','adbd')
G.edge['adbd']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('adbd','dumpstate')
G.edge['adbd']['dumpstate']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('adbd','installd')
G.edge['adbd']['installd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('adbd','itsonbs')
G.edge['adbd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('adbd','mediaserver')
G.edge['adbd']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('adbd','qseecomd')
G.edge['adbd']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('adbd','shell')
G.edge['adbd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('adbd','sysprof')
G.edge['adbd']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('adbd','adbd')
G.edge['adbd']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['adbd']['adbd']['fill'] = 'red'
G.add_edge('adbd','adbd')
G.edge['adbd']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('adbd','binderservicedomain')
G.edge['adbd']['binderservicedomain']['write-read'] = '[open open][write read][append read][write read]'
G.edge['adbd']['binderservicedomain']['fill'] = 'red'
G.add_edge('adbd','dumpstate')
G.edge['adbd']['dumpstate']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['adbd']['dumpstate']['fill'] = 'red'
G.add_edge('adbd','dumpstate')
G.edge['adbd']['dumpstate']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('adbd','ime_app')
G.edge['adbd']['ime_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['adbd']['ime_app']['fill'] = 'red'
G.add_edge('adbd','itsonbs')
G.edge['adbd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['adbd']['itsonbs']['fill'] = 'red'
G.add_edge('adbd','itsonbs')
G.edge['adbd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('adbd','knox_system_app')
G.edge['adbd']['knox_system_app']['write-read'] = '[open open][write read]'
G.edge['adbd']['knox_system_app']['fill'] = 'red'
G.add_edge('adbd','mediaserver')
G.edge['adbd']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['adbd']['mediaserver']['fill'] = 'red'
G.add_edge('adbd','mediaserver')
G.edge['adbd']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('adbd','newAttr1')
G.edge['adbd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][open open][write read]'
G.edge['adbd']['newAttr1']['fill'] = 'red'
G.add_edge('adbd','newAttr1')
G.edge['adbd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][open open][write read][write read]'
G.edge['adbd']['newAttr1']['fill'] = 'red'
G.add_edge('adbd','newAttr40')
G.edge['adbd']['newAttr40']['write-read'] = '[write read]'
G.edge['adbd']['newAttr40']['fill'] = 'red'
G.add_edge('adbd','qseecomd')
G.edge['adbd']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['adbd']['qseecomd']['fill'] = 'red'
G.add_edge('adbd','qseecomd')
G.edge['adbd']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('adbd','runas')
G.edge['adbd']['runas']['write-read'] = '[write read][write read]'
G.edge['adbd']['runas']['fill'] = 'red'
G.add_edge('adbd','shell')
G.edge['adbd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['adbd']['shell']['fill'] = 'red'
G.add_edge('adbd','shell')
G.edge['adbd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('adbd','s_system_app')
G.edge['adbd']['s_system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read]'
G.edge['adbd']['s_system_app']['fill'] = 'red'
G.add_edge('adbd','s_system_app')
G.edge['adbd']['s_system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read]'
G.add_edge('adbd','s_system_app')
G.edge['adbd']['s_system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read][write read]'
G.edge['adbd']['s_system_app']['fill'] = 'red'
G.add_edge('adbd','sysprof')
G.edge['adbd']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['adbd']['sysprof']['fill'] = 'red'
G.add_edge('adbd','sysprof')
G.edge['adbd']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('adbd','system_app')
G.edge['adbd']['system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['adbd']['system_app']['fill'] = 'red'
G.add_edge('adbd','system_server')
G.edge['adbd']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['adbd']['system_server']['fill'] = 'red'
G.add_edge('adbd','vdc')
G.edge['adbd']['vdc']['write-read'] = '[write read]'
G.edge['adbd']['vdc']['fill'] = 'red'
G.add_edge('adbd','zygote')
G.edge['adbd']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][add_name search][remove_name search][write read]'
G.edge['adbd']['zygote']['fill'] = 'red'
G.add_edge('binderservicedomain','adbd')
G.edge['binderservicedomain']['adbd']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('binderservicedomain','dumpstate')
G.edge['binderservicedomain']['dumpstate']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('binderservicedomain','installd')
G.edge['binderservicedomain']['installd']['write-read'] = '[setattr getattr]'
G.add_edge('binderservicedomain','itsonbs')
G.edge['binderservicedomain']['itsonbs']['write-read'] = '[setattr getattr]'
G.add_edge('binderservicedomain','mediaserver')
G.edge['binderservicedomain']['mediaserver']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('binderservicedomain','qseecomd')
G.edge['binderservicedomain']['qseecomd']['write-read'] = '[setattr getattr]'
G.add_edge('binderservicedomain','shell')
G.edge['binderservicedomain']['shell']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('binderservicedomain','sysprof')
G.edge['binderservicedomain']['sysprof']['write-read'] = '[setattr getattr]'
G.add_edge('carrier_app','adbd')
G.edge['carrier_app']['adbd']['write-read'] = '[write read][open open]'
G.add_edge('carrier_app','dumpstate')
G.edge['carrier_app']['dumpstate']['write-read'] = '[open open]'
G.add_edge('carrier_app','ime_app')
G.edge['carrier_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('carrier_app','itsonbs')
G.edge['carrier_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('carrier_app','knox_system_app')
G.edge['carrier_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('carrier_app','mediaserver')
G.edge['carrier_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('carrier_app','newAttr1')
G.edge['carrier_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('carrier_app','qseecomd')
G.edge['carrier_app']['qseecomd']['write-read'] = '[open open]'
G.add_edge('carrier_app','shell')
G.edge['carrier_app']['shell']['write-read'] = '[open open]'
G.add_edge('carrier_app','s_system_app')
G.edge['carrier_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('carrier_app','s_system_app')
G.edge['carrier_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('carrier_app','sysprof')
G.edge['carrier_app']['sysprof']['write-read'] = '[open open]'
G.add_edge('carrier_app','system_app')
G.edge['carrier_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('carrier_app','adbd')
G.edge['carrier_app']['adbd']['write-read'] = '[write read][open open][setattr getattr]'
G.add_edge('carrier_app','dumpstate')
G.edge['carrier_app']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','installd')
G.edge['carrier_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('carrier_app','itsonbs')
G.edge['carrier_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('carrier_app','mediaserver')
G.edge['carrier_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('carrier_app','qseecomd')
G.edge['carrier_app']['qseecomd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','shell')
G.edge['carrier_app']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','sysprof')
G.edge['carrier_app']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','adbd')
G.edge['carrier_app']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read]'
G.edge['carrier_app']['adbd']['fill'] = 'red'
G.add_edge('carrier_app','adbd')
G.edge['carrier_app']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','binderservicedomain')
G.edge['carrier_app']['binderservicedomain']['write-read'] = '[write read]'
G.edge['carrier_app']['binderservicedomain']['fill'] = 'red'
G.add_edge('carrier_app','dumpstate')
G.edge['carrier_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['carrier_app']['dumpstate']['fill'] = 'red'
G.add_edge('carrier_app','dumpstate')
G.edge['carrier_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','ime_app')
G.edge['carrier_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['carrier_app']['ime_app']['fill'] = 'red'
G.add_edge('carrier_app','itsonbs')
G.edge['carrier_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['carrier_app']['itsonbs']['fill'] = 'red'
G.add_edge('carrier_app','itsonbs')
G.edge['carrier_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','knox_system_app')
G.edge['carrier_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['carrier_app']['knox_system_app']['fill'] = 'red'
G.add_edge('carrier_app','mediaserver')
G.edge['carrier_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['carrier_app']['mediaserver']['fill'] = 'red'
G.add_edge('carrier_app','mediaserver')
G.edge['carrier_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','newAttr1')
G.edge['carrier_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['carrier_app']['newAttr1']['fill'] = 'red'
G.add_edge('carrier_app','newAttr1')
G.edge['carrier_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read]'
G.edge['carrier_app']['newAttr1']['fill'] = 'red'
G.add_edge('carrier_app','newAttr40')
G.edge['carrier_app']['newAttr40']['write-read'] = '[write read]'
G.edge['carrier_app']['newAttr40']['fill'] = 'red'
G.add_edge('carrier_app','qseecomd')
G.edge['carrier_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['carrier_app']['qseecomd']['fill'] = 'red'
G.add_edge('carrier_app','qseecomd')
G.edge['carrier_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','runas')
G.edge['carrier_app']['runas']['write-read'] = '[write read]'
G.edge['carrier_app']['runas']['fill'] = 'red'
G.add_edge('carrier_app','shell')
G.edge['carrier_app']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['carrier_app']['shell']['fill'] = 'red'
G.add_edge('carrier_app','shell')
G.edge['carrier_app']['shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','s_system_app')
G.edge['carrier_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read]'
G.edge['carrier_app']['s_system_app']['fill'] = 'red'
G.add_edge('carrier_app','s_system_app')
G.edge['carrier_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read][append read]'
G.add_edge('carrier_app','s_system_app')
G.edge['carrier_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read]'
G.edge['carrier_app']['s_system_app']['fill'] = 'red'
G.add_edge('carrier_app','sysprof')
G.edge['carrier_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['carrier_app']['sysprof']['fill'] = 'red'
G.add_edge('carrier_app','sysprof')
G.edge['carrier_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','system_app')
G.edge['carrier_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['carrier_app']['system_app']['fill'] = 'red'
G.add_edge('carrier_app','system_server')
G.edge['carrier_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['carrier_app']['system_server']['fill'] = 'red'
G.add_edge('carrier_app','vdc')
G.edge['carrier_app']['vdc']['write-read'] = '[write read]'
G.edge['carrier_app']['vdc']['fill'] = 'red'
G.add_edge('carrier_app','zygote')
G.edge['carrier_app']['zygote']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['carrier_app']['zygote']['fill'] = 'red'
G.add_edge('commonplatformappdomain','adbd')
G.edge['commonplatformappdomain']['adbd']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','dumpstate')
G.edge['commonplatformappdomain']['dumpstate']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','ime_app')
G.edge['commonplatformappdomain']['ime_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('commonplatformappdomain','itsonbs')
G.edge['commonplatformappdomain']['itsonbs']['write-read'] = '[write read][append read][open open]'
G.add_edge('commonplatformappdomain','knox_system_app')
G.edge['commonplatformappdomain']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','mediaserver')
G.edge['commonplatformappdomain']['mediaserver']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','newAttr1')
G.edge['commonplatformappdomain']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open]'
G.add_edge('commonplatformappdomain','qseecomd')
G.edge['commonplatformappdomain']['qseecomd']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','shell')
G.edge['commonplatformappdomain']['shell']['write-read'] = '[write read][setopt getopt][write read][append read][open open]'
G.add_edge('commonplatformappdomain','s_system_app')
G.edge['commonplatformappdomain']['s_system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('commonplatformappdomain','s_system_app')
G.edge['commonplatformappdomain']['s_system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('commonplatformappdomain','sysprof')
G.edge['commonplatformappdomain']['sysprof']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','system_app')
G.edge['commonplatformappdomain']['system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('commonplatformappdomain','adbd')
G.edge['commonplatformappdomain']['adbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','dumpstate')
G.edge['commonplatformappdomain']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','installd')
G.edge['commonplatformappdomain']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr]'
G.add_edge('commonplatformappdomain','itsonbs')
G.edge['commonplatformappdomain']['itsonbs']['write-read'] = '[write read][append read][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','mediaserver')
G.edge['commonplatformappdomain']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','qseecomd')
G.edge['commonplatformappdomain']['qseecomd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','shell')
G.edge['commonplatformappdomain']['shell']['write-read'] = '[write read][setopt getopt][write read][append read][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','sysprof')
G.edge['commonplatformappdomain']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','adbd')
G.edge['commonplatformappdomain']['adbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['adbd']['fill'] = 'red'
G.add_edge('commonplatformappdomain','adbd')
G.edge['commonplatformappdomain']['adbd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','binderservicedomain')
G.edge['commonplatformappdomain']['binderservicedomain']['write-read'] = '[write read]'
G.edge['commonplatformappdomain']['binderservicedomain']['fill'] = 'red'
G.add_edge('commonplatformappdomain','dumpstate')
G.edge['commonplatformappdomain']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['dumpstate']['fill'] = 'red'
G.add_edge('commonplatformappdomain','dumpstate')
G.edge['commonplatformappdomain']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','ime_app')
G.edge['commonplatformappdomain']['ime_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['commonplatformappdomain']['ime_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','itsonbs')
G.edge['commonplatformappdomain']['itsonbs']['write-read'] = '[write read][append read][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['itsonbs']['fill'] = 'red'
G.add_edge('commonplatformappdomain','itsonbs')
G.edge['commonplatformappdomain']['itsonbs']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','knox_system_app')
G.edge['commonplatformappdomain']['knox_system_app']['write-read'] = '[open open][write read]'
G.edge['commonplatformappdomain']['knox_system_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','mediaserver')
G.edge['commonplatformappdomain']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['mediaserver']['fill'] = 'red'
G.add_edge('commonplatformappdomain','mediaserver')
G.edge['commonplatformappdomain']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','newAttr1')
G.edge['commonplatformappdomain']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][write read]'
G.edge['commonplatformappdomain']['newAttr1']['fill'] = 'red'
G.add_edge('commonplatformappdomain','newAttr1')
G.edge['commonplatformappdomain']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][write read][write read]'
G.edge['commonplatformappdomain']['newAttr1']['fill'] = 'red'
G.add_edge('commonplatformappdomain','newAttr40')
G.edge['commonplatformappdomain']['newAttr40']['write-read'] = '[write read]'
G.edge['commonplatformappdomain']['newAttr40']['fill'] = 'red'
G.add_edge('commonplatformappdomain','qseecomd')
G.edge['commonplatformappdomain']['qseecomd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['qseecomd']['fill'] = 'red'
G.add_edge('commonplatformappdomain','qseecomd')
G.edge['commonplatformappdomain']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','runas')
G.edge['commonplatformappdomain']['runas']['write-read'] = '[open open][write read][append read][write read]'
G.edge['commonplatformappdomain']['runas']['fill'] = 'red'
G.add_edge('commonplatformappdomain','shell')
G.edge['commonplatformappdomain']['shell']['write-read'] = '[write read][setopt getopt][write read][append read][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['shell']['fill'] = 'red'
G.add_edge('commonplatformappdomain','shell')
G.edge['commonplatformappdomain']['shell']['write-read'] = '[write read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','s_system_app')
G.edge['commonplatformappdomain']['s_system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][write read]'
G.edge['commonplatformappdomain']['s_system_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','s_system_app')
G.edge['commonplatformappdomain']['s_system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][write read][append read]'
G.add_edge('commonplatformappdomain','s_system_app')
G.edge['commonplatformappdomain']['s_system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read]'
G.edge['commonplatformappdomain']['s_system_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','sysprof')
G.edge['commonplatformappdomain']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['sysprof']['fill'] = 'red'
G.add_edge('commonplatformappdomain','sysprof')
G.edge['commonplatformappdomain']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','system_app')
G.edge['commonplatformappdomain']['system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['commonplatformappdomain']['system_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','system_server')
G.edge['commonplatformappdomain']['system_server']['write-read'] = '[write read][append read][open open][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['commonplatformappdomain']['system_server']['fill'] = 'red'
G.add_edge('commonplatformappdomain','vdc')
G.edge['commonplatformappdomain']['vdc']['write-read'] = '[write read]'
G.edge['commonplatformappdomain']['vdc']['fill'] = 'red'
G.add_edge('commonplatformappdomain','zygote')
G.edge['commonplatformappdomain']['zygote']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['commonplatformappdomain']['zygote']['fill'] = 'red'
G.add_edge('dumpstate','adbd')
G.edge['dumpstate']['adbd']['write-read'] = '[write read][add_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('dumpstate','ime_app')
G.edge['dumpstate']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','itsonbs')
G.edge['dumpstate']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','knox_system_app')
G.edge['dumpstate']['knox_system_app']['write-read'] = '[add_name search][remove_name search][open open]'
G.add_edge('dumpstate','mediaserver')
G.edge['dumpstate']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('dumpstate','newAttr1')
G.edge['dumpstate']['newAttr1']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','qseecomd')
G.edge['dumpstate']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','shell')
G.edge['dumpstate']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('dumpstate','s_system_app')
G.edge['dumpstate']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','s_system_app')
G.edge['dumpstate']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('dumpstate','sysprof')
G.edge['dumpstate']['sysprof']['write-read'] = '[open open]'
G.add_edge('dumpstate','system_app')
G.edge['dumpstate']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','adbd')
G.edge['dumpstate']['adbd']['write-read'] = '[write read][add_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('dumpstate','installd')
G.edge['dumpstate']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][add_name search][remove_name search][setattr getattr]'
G.add_edge('dumpstate','itsonbs')
G.edge['dumpstate']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('dumpstate','mediaserver')
G.edge['dumpstate']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('dumpstate','qseecomd')
G.edge['dumpstate']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('dumpstate','shell')
G.edge['dumpstate']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('dumpstate','sysprof')
G.edge['dumpstate']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','adbd')
G.edge['dumpstate']['adbd']['write-read'] = '[write read][add_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['dumpstate']['adbd']['fill'] = 'red'
G.add_edge('dumpstate','adbd')
G.edge['dumpstate']['adbd']['write-read'] = '[write read][add_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('dumpstate','binderservicedomain')
G.edge['dumpstate']['binderservicedomain']['write-read'] = '[open open][write read][append read][write read]'
G.edge['dumpstate']['binderservicedomain']['fill'] = 'red'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['dumpstate']['dumpstate']['fill'] = 'red'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('dumpstate','ime_app')
G.edge['dumpstate']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['dumpstate']['ime_app']['fill'] = 'red'
G.add_edge('dumpstate','itsonbs')
G.edge['dumpstate']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['dumpstate']['itsonbs']['fill'] = 'red'
G.add_edge('dumpstate','itsonbs')
G.edge['dumpstate']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('dumpstate','knox_system_app')
G.edge['dumpstate']['knox_system_app']['write-read'] = '[add_name search][remove_name search][open open][write read]'
G.edge['dumpstate']['knox_system_app']['fill'] = 'red'
G.add_edge('dumpstate','mediaserver')
G.edge['dumpstate']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['dumpstate']['mediaserver']['fill'] = 'red'
G.add_edge('dumpstate','mediaserver')
G.edge['dumpstate']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('dumpstate','newAttr1')
G.edge['dumpstate']['newAttr1']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['dumpstate']['newAttr1']['fill'] = 'red'
G.add_edge('dumpstate','newAttr1')
G.edge['dumpstate']['newAttr1']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read]'
G.edge['dumpstate']['newAttr1']['fill'] = 'red'
G.add_edge('dumpstate','newAttr40')
G.edge['dumpstate']['newAttr40']['write-read'] = '[write read]'
G.edge['dumpstate']['newAttr40']['fill'] = 'red'
G.add_edge('dumpstate','qseecomd')
G.edge['dumpstate']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['dumpstate']['qseecomd']['fill'] = 'red'
G.add_edge('dumpstate','qseecomd')
G.edge['dumpstate']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('dumpstate','runas')
G.edge['dumpstate']['runas']['write-read'] = '[write read][write read]'
G.edge['dumpstate']['runas']['fill'] = 'red'
G.add_edge('dumpstate','shell')
G.edge['dumpstate']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['dumpstate']['shell']['fill'] = 'red'
G.add_edge('dumpstate','shell')
G.edge['dumpstate']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('dumpstate','s_system_app')
G.edge['dumpstate']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][open open][write read]'
G.edge['dumpstate']['s_system_app']['fill'] = 'red'
G.add_edge('dumpstate','s_system_app')
G.edge['dumpstate']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][open open][write read][append read]'
G.add_edge('dumpstate','s_system_app')
G.edge['dumpstate']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][open open][write read][append read][write read]'
G.edge['dumpstate']['s_system_app']['fill'] = 'red'
G.add_edge('dumpstate','sysprof')
G.edge['dumpstate']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dumpstate']['sysprof']['fill'] = 'red'
G.add_edge('dumpstate','sysprof')
G.edge['dumpstate']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('dumpstate','system_app')
G.edge['dumpstate']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['dumpstate']['system_app']['fill'] = 'red'
G.add_edge('dumpstate','system_server')
G.edge['dumpstate']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['dumpstate']['system_server']['fill'] = 'red'
G.add_edge('dumpstate','vdc')
G.edge['dumpstate']['vdc']['write-read'] = '[write read][write read]'
G.edge['dumpstate']['vdc']['fill'] = 'red'
G.add_edge('dumpstate','zygote')
G.edge['dumpstate']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][write read]'
G.edge['dumpstate']['zygote']['fill'] = 'red'
G.add_edge('filtered_google_app','adbd')
G.edge['filtered_google_app']['adbd']['write-read'] = '[write read][open open]'
G.add_edge('filtered_google_app','dumpstate')
G.edge['filtered_google_app']['dumpstate']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','ime_app')
G.edge['filtered_google_app']['ime_app']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_google_app','itsonbs')
G.edge['filtered_google_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_google_app','knox_system_app')
G.edge['filtered_google_app']['knox_system_app']['write-read'] = '[setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_google_app','mediaserver')
G.edge['filtered_google_app']['mediaserver']['write-read'] = '[setattr getattr][setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_google_app','newAttr1')
G.edge['filtered_google_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_google_app','qseecomd')
G.edge['filtered_google_app']['qseecomd']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','shell')
G.edge['filtered_google_app']['shell']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','s_system_app')
G.edge['filtered_google_app']['s_system_app']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_google_app','s_system_app')
G.edge['filtered_google_app']['s_system_app']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][open open][open open]'
G.add_edge('filtered_google_app','sysprof')
G.edge['filtered_google_app']['sysprof']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','system_app')
G.edge['filtered_google_app']['system_app']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_google_app','adbd')
G.edge['filtered_google_app']['adbd']['write-read'] = '[write read][open open][setattr getattr]'
G.add_edge('filtered_google_app','dumpstate')
G.edge['filtered_google_app']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','installd')
G.edge['filtered_google_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('filtered_google_app','itsonbs')
G.edge['filtered_google_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('filtered_google_app','mediaserver')
G.edge['filtered_google_app']['mediaserver']['write-read'] = '[setattr getattr][setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('filtered_google_app','qseecomd')
G.edge['filtered_google_app']['qseecomd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','shell')
G.edge['filtered_google_app']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','sysprof')
G.edge['filtered_google_app']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','adbd')
G.edge['filtered_google_app']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read]'
G.edge['filtered_google_app']['adbd']['fill'] = 'red'
G.add_edge('filtered_google_app','adbd')
G.edge['filtered_google_app']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','binderservicedomain')
G.edge['filtered_google_app']['binderservicedomain']['write-read'] = '[write read]'
G.edge['filtered_google_app']['binderservicedomain']['fill'] = 'red'
G.add_edge('filtered_google_app','dumpstate')
G.edge['filtered_google_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_google_app']['dumpstate']['fill'] = 'red'
G.add_edge('filtered_google_app','dumpstate')
G.edge['filtered_google_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','ime_app')
G.edge['filtered_google_app']['ime_app']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_google_app']['ime_app']['fill'] = 'red'
G.add_edge('filtered_google_app','itsonbs')
G.edge['filtered_google_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['filtered_google_app']['itsonbs']['fill'] = 'red'
G.add_edge('filtered_google_app','itsonbs')
G.edge['filtered_google_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','knox_system_app')
G.edge['filtered_google_app']['knox_system_app']['write-read'] = '[setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_google_app']['knox_system_app']['fill'] = 'red'
G.add_edge('filtered_google_app','mediaserver')
G.edge['filtered_google_app']['mediaserver']['write-read'] = '[setattr getattr][setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['filtered_google_app']['mediaserver']['fill'] = 'red'
G.add_edge('filtered_google_app','mediaserver')
G.edge['filtered_google_app']['mediaserver']['write-read'] = '[setattr getattr][setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','newAttr1')
G.edge['filtered_google_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_google_app']['newAttr1']['fill'] = 'red'
G.add_edge('filtered_google_app','newAttr1')
G.edge['filtered_google_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read]'
G.edge['filtered_google_app']['newAttr1']['fill'] = 'red'
G.add_edge('filtered_google_app','newAttr40')
G.edge['filtered_google_app']['newAttr40']['write-read'] = '[write read]'
G.edge['filtered_google_app']['newAttr40']['fill'] = 'red'
G.add_edge('filtered_google_app','qseecomd')
G.edge['filtered_google_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_google_app']['qseecomd']['fill'] = 'red'
G.add_edge('filtered_google_app','qseecomd')
G.edge['filtered_google_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','runas')
G.edge['filtered_google_app']['runas']['write-read'] = '[write read]'
G.edge['filtered_google_app']['runas']['fill'] = 'red'
G.add_edge('filtered_google_app','shell')
G.edge['filtered_google_app']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_google_app']['shell']['fill'] = 'red'
G.add_edge('filtered_google_app','shell')
G.edge['filtered_google_app']['shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','s_system_app')
G.edge['filtered_google_app']['s_system_app']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][open open][open open][write read]'
G.edge['filtered_google_app']['s_system_app']['fill'] = 'red'
G.add_edge('filtered_google_app','s_system_app')
G.edge['filtered_google_app']['s_system_app']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][open open][open open][write read][append read]'
G.add_edge('filtered_google_app','s_system_app')
G.edge['filtered_google_app']['s_system_app']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][open open][open open][write read][append read][write read]'
G.edge['filtered_google_app']['s_system_app']['fill'] = 'red'
G.add_edge('filtered_google_app','sysprof')
G.edge['filtered_google_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_google_app']['sysprof']['fill'] = 'red'
G.add_edge('filtered_google_app','sysprof')
G.edge['filtered_google_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','system_app')
G.edge['filtered_google_app']['system_app']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_google_app']['system_app']['fill'] = 'red'
G.add_edge('filtered_google_app','system_server')
G.edge['filtered_google_app']['system_server']['write-read'] = '[setattr getattr][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['filtered_google_app']['system_server']['fill'] = 'red'
G.add_edge('filtered_google_app','vdc')
G.edge['filtered_google_app']['vdc']['write-read'] = '[write read]'
G.edge['filtered_google_app']['vdc']['fill'] = 'red'
G.add_edge('filtered_google_app','zygote')
G.edge['filtered_google_app']['zygote']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['filtered_google_app']['zygote']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','adbd')
G.edge['filtered_untrusted_app']['adbd']['write-read'] = '[write read][open open]'
G.add_edge('filtered_untrusted_app','dumpstate')
G.edge['filtered_untrusted_app']['dumpstate']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','ime_app')
G.edge['filtered_untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_untrusted_app','itsonbs')
G.edge['filtered_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_untrusted_app','knox_system_app')
G.edge['filtered_untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_untrusted_app','mediaserver')
G.edge['filtered_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_untrusted_app','newAttr1')
G.edge['filtered_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_untrusted_app','qseecomd')
G.edge['filtered_untrusted_app']['qseecomd']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','shell')
G.edge['filtered_untrusted_app']['shell']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','s_system_app')
G.edge['filtered_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_untrusted_app','s_system_app')
G.edge['filtered_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('filtered_untrusted_app','sysprof')
G.edge['filtered_untrusted_app']['sysprof']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','system_app')
G.edge['filtered_untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_untrusted_app','adbd')
G.edge['filtered_untrusted_app']['adbd']['write-read'] = '[write read][open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','dumpstate')
G.edge['filtered_untrusted_app']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','installd')
G.edge['filtered_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('filtered_untrusted_app','itsonbs')
G.edge['filtered_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','mediaserver')
G.edge['filtered_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','qseecomd')
G.edge['filtered_untrusted_app']['qseecomd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','shell')
G.edge['filtered_untrusted_app']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','sysprof')
G.edge['filtered_untrusted_app']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','adbd')
G.edge['filtered_untrusted_app']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['adbd']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','adbd')
G.edge['filtered_untrusted_app']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','binderservicedomain')
G.edge['filtered_untrusted_app']['binderservicedomain']['write-read'] = '[write read]'
G.edge['filtered_untrusted_app']['binderservicedomain']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','dumpstate')
G.edge['filtered_untrusted_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['dumpstate']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','dumpstate')
G.edge['filtered_untrusted_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','ime_app')
G.edge['filtered_untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_untrusted_app']['ime_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','itsonbs')
G.edge['filtered_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['itsonbs']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','itsonbs')
G.edge['filtered_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','knox_system_app')
G.edge['filtered_untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_untrusted_app']['knox_system_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','mediaserver')
G.edge['filtered_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['mediaserver']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','mediaserver')
G.edge['filtered_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','newAttr1')
G.edge['filtered_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_untrusted_app']['newAttr1']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','newAttr1')
G.edge['filtered_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read]'
G.edge['filtered_untrusted_app']['newAttr1']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','newAttr40')
G.edge['filtered_untrusted_app']['newAttr40']['write-read'] = '[write read]'
G.edge['filtered_untrusted_app']['newAttr40']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','qseecomd')
G.edge['filtered_untrusted_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['qseecomd']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','qseecomd')
G.edge['filtered_untrusted_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','runas')
G.edge['filtered_untrusted_app']['runas']['write-read'] = '[write read]'
G.edge['filtered_untrusted_app']['runas']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','shell')
G.edge['filtered_untrusted_app']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['shell']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','shell')
G.edge['filtered_untrusted_app']['shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','s_system_app')
G.edge['filtered_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read]'
G.edge['filtered_untrusted_app']['s_system_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','s_system_app')
G.edge['filtered_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read][append read]'
G.add_edge('filtered_untrusted_app','s_system_app')
G.edge['filtered_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read]'
G.edge['filtered_untrusted_app']['s_system_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','sysprof')
G.edge['filtered_untrusted_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['sysprof']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','sysprof')
G.edge['filtered_untrusted_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','system_app')
G.edge['filtered_untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['filtered_untrusted_app']['system_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','system_server')
G.edge['filtered_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['filtered_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','vdc')
G.edge['filtered_untrusted_app']['vdc']['write-read'] = '[write read]'
G.edge['filtered_untrusted_app']['vdc']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','zygote')
G.edge['filtered_untrusted_app']['zygote']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['filtered_untrusted_app']['zygote']['fill'] = 'red'
G.add_edge('fixmo_app','adbd')
G.edge['fixmo_app']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('fixmo_app','dumpstate')
G.edge['fixmo_app']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr]'
G.add_edge('fixmo_app','installd')
G.edge['fixmo_app']['installd']['write-read'] = '[setattr getattr][setattr getattr][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][setattr getattr]'
G.add_edge('fixmo_app','itsonbs')
G.edge['fixmo_app']['itsonbs']['write-read'] = '[setattr getattr]'
G.add_edge('fixmo_app','mediaserver')
G.edge['fixmo_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][add_name search][remove_name search][setattr getattr]'
G.add_edge('fixmo_app','qseecomd')
G.edge['fixmo_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][setattr getattr]'
G.add_edge('fixmo_app','shell')
G.edge['fixmo_app']['shell']['write-read'] = '[write read][setopt getopt][open open][write read][append read][setattr getattr]'
G.add_edge('fixmo_app','sysprof')
G.edge['fixmo_app']['sysprof']['write-read'] = '[setattr getattr]'
G.add_edge('gad_untrusted_app','adbd')
G.edge['gad_untrusted_app']['adbd']['write-read'] = '[write read][open open]'
G.add_edge('gad_untrusted_app','dumpstate')
G.edge['gad_untrusted_app']['dumpstate']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','ime_app')
G.edge['gad_untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('gad_untrusted_app','itsonbs')
G.edge['gad_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('gad_untrusted_app','knox_system_app')
G.edge['gad_untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gad_untrusted_app','mediaserver')
G.edge['gad_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('gad_untrusted_app','newAttr1')
G.edge['gad_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gad_untrusted_app','qseecomd')
G.edge['gad_untrusted_app']['qseecomd']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','shell')
G.edge['gad_untrusted_app']['shell']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','s_system_app')
G.edge['gad_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gad_untrusted_app','s_system_app')
G.edge['gad_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('gad_untrusted_app','sysprof')
G.edge['gad_untrusted_app']['sysprof']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','system_app')
G.edge['gad_untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gad_untrusted_app','adbd')
G.edge['gad_untrusted_app']['adbd']['write-read'] = '[write read][open open][setattr getattr]'
G.add_edge('gad_untrusted_app','dumpstate')
G.edge['gad_untrusted_app']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','installd')
G.edge['gad_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('gad_untrusted_app','itsonbs')
G.edge['gad_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('gad_untrusted_app','mediaserver')
G.edge['gad_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('gad_untrusted_app','qseecomd')
G.edge['gad_untrusted_app']['qseecomd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','shell')
G.edge['gad_untrusted_app']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','sysprof')
G.edge['gad_untrusted_app']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','adbd')
G.edge['gad_untrusted_app']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['adbd']['fill'] = 'red'
G.add_edge('gad_untrusted_app','adbd')
G.edge['gad_untrusted_app']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','binderservicedomain')
G.edge['gad_untrusted_app']['binderservicedomain']['write-read'] = '[write read]'
G.edge['gad_untrusted_app']['binderservicedomain']['fill'] = 'red'
G.add_edge('gad_untrusted_app','dumpstate')
G.edge['gad_untrusted_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['dumpstate']['fill'] = 'red'
G.add_edge('gad_untrusted_app','dumpstate')
G.edge['gad_untrusted_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','ime_app')
G.edge['gad_untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['gad_untrusted_app']['ime_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','itsonbs')
G.edge['gad_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['itsonbs']['fill'] = 'red'
G.add_edge('gad_untrusted_app','itsonbs')
G.edge['gad_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','knox_system_app')
G.edge['gad_untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['gad_untrusted_app']['knox_system_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','mediaserver')
G.edge['gad_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['mediaserver']['fill'] = 'red'
G.add_edge('gad_untrusted_app','mediaserver')
G.edge['gad_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','newAttr1')
G.edge['gad_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['gad_untrusted_app']['newAttr1']['fill'] = 'red'
G.add_edge('gad_untrusted_app','newAttr1')
G.edge['gad_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read]'
G.edge['gad_untrusted_app']['newAttr1']['fill'] = 'red'
G.add_edge('gad_untrusted_app','newAttr40')
G.edge['gad_untrusted_app']['newAttr40']['write-read'] = '[write read]'
G.edge['gad_untrusted_app']['newAttr40']['fill'] = 'red'
G.add_edge('gad_untrusted_app','qseecomd')
G.edge['gad_untrusted_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['qseecomd']['fill'] = 'red'
G.add_edge('gad_untrusted_app','qseecomd')
G.edge['gad_untrusted_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','runas')
G.edge['gad_untrusted_app']['runas']['write-read'] = '[write read]'
G.edge['gad_untrusted_app']['runas']['fill'] = 'red'
G.add_edge('gad_untrusted_app','shell')
G.edge['gad_untrusted_app']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['shell']['fill'] = 'red'
G.add_edge('gad_untrusted_app','shell')
G.edge['gad_untrusted_app']['shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','s_system_app')
G.edge['gad_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read]'
G.edge['gad_untrusted_app']['s_system_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','s_system_app')
G.edge['gad_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read]'
G.add_edge('gad_untrusted_app','s_system_app')
G.edge['gad_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read][write read]'
G.edge['gad_untrusted_app']['s_system_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','sysprof')
G.edge['gad_untrusted_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['sysprof']['fill'] = 'red'
G.add_edge('gad_untrusted_app','sysprof')
G.edge['gad_untrusted_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','system_app')
G.edge['gad_untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['gad_untrusted_app']['system_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','system_server')
G.edge['gad_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['gad_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('gad_untrusted_app','vdc')
G.edge['gad_untrusted_app']['vdc']['write-read'] = '[write read]'
G.edge['gad_untrusted_app']['vdc']['fill'] = 'red'
G.add_edge('gad_untrusted_app','zygote')
G.edge['gad_untrusted_app']['zygote']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['gad_untrusted_app']['zygote']['fill'] = 'red'
G.add_edge('good_app','adbd')
G.edge['good_app']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setattr getattr]'
G.add_edge('good_app','dumpstate')
G.edge['good_app']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr]'
G.add_edge('good_app','installd')
G.edge['good_app']['installd']['write-read'] = '[setattr getattr][setattr getattr][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('good_app','itsonbs')
G.edge['good_app']['itsonbs']['write-read'] = '[setattr getattr]'
G.add_edge('good_app','mediaserver')
G.edge['good_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('good_app','qseecomd')
G.edge['good_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][setattr getattr]'
G.add_edge('good_app','shell')
G.edge['good_app']['shell']['write-read'] = '[write read][setopt getopt][open open][write read][append read][setattr getattr]'
G.add_edge('good_app','sysprof')
G.edge['good_app']['sysprof']['write-read'] = '[setattr getattr]'
G.add_edge('init','adbd')
G.edge['init']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('init','dumpstate')
G.edge['init']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('init','installd')
G.edge['init']['installd']['write-read'] = '[setattr getattr]'
G.add_edge('init','itsonbs')
G.edge['init']['itsonbs']['write-read'] = '[setattr getattr]'
G.add_edge('init','mediaserver')
G.edge['init']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('init','qseecomd')
G.edge['init']['qseecomd']['write-read'] = '[setattr getattr]'
G.add_edge('init','shell')
G.edge['init']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('init','sysprof')
G.edge['init']['sysprof']['write-read'] = '[setattr getattr]'
G.add_edge('installd','adbd')
G.edge['installd']['adbd']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','dumpstate')
G.edge['installd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('installd','itsonbs')
G.edge['installd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr]'
G.add_edge('installd','mediaserver')
G.edge['installd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','qseecomd')
G.edge['installd']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('installd','shell')
G.edge['installd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('installd','sysprof')
G.edge['installd']['sysprof']['write-read'] = '[setattr getattr]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][setattr getattr][relabelto relabelfrom]'
G.add_edge('irm_app','adbd')
G.edge['irm_app']['adbd']['write-read'] = '[write read][open open]'
G.add_edge('irm_app','dumpstate')
G.edge['irm_app']['dumpstate']['write-read'] = '[open open]'
G.add_edge('irm_app','ime_app')
G.edge['irm_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('irm_app','itsonbs')
G.edge['irm_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('irm_app','knox_system_app')
G.edge['irm_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('irm_app','mediaserver')
G.edge['irm_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('irm_app','newAttr1')
G.edge['irm_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('irm_app','qseecomd')
G.edge['irm_app']['qseecomd']['write-read'] = '[open open]'
G.add_edge('irm_app','shell')
G.edge['irm_app']['shell']['write-read'] = '[write read][setopt getopt][open open]'
G.add_edge('irm_app','s_system_app')
G.edge['irm_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('irm_app','s_system_app')
G.edge['irm_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('irm_app','sysprof')
G.edge['irm_app']['sysprof']['write-read'] = '[open open]'
G.add_edge('irm_app','system_app')
G.edge['irm_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('irm_app','adbd')
G.edge['irm_app']['adbd']['write-read'] = '[write read][open open][setattr getattr]'
G.add_edge('irm_app','dumpstate')
G.edge['irm_app']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','installd')
G.edge['irm_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('irm_app','itsonbs')
G.edge['irm_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('irm_app','mediaserver')
G.edge['irm_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('irm_app','qseecomd')
G.edge['irm_app']['qseecomd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','shell')
G.edge['irm_app']['shell']['write-read'] = '[write read][setopt getopt][open open][setattr getattr]'
G.add_edge('irm_app','sysprof')
G.edge['irm_app']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','adbd')
G.edge['irm_app']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read]'
G.edge['irm_app']['adbd']['fill'] = 'red'
G.add_edge('irm_app','adbd')
G.edge['irm_app']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','binderservicedomain')
G.edge['irm_app']['binderservicedomain']['write-read'] = '[write read]'
G.edge['irm_app']['binderservicedomain']['fill'] = 'red'
G.add_edge('irm_app','dumpstate')
G.edge['irm_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_app']['dumpstate']['fill'] = 'red'
G.add_edge('irm_app','dumpstate')
G.edge['irm_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','ime_app')
G.edge['irm_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['irm_app']['ime_app']['fill'] = 'red'
G.add_edge('irm_app','itsonbs')
G.edge['irm_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['irm_app']['itsonbs']['fill'] = 'red'
G.add_edge('irm_app','itsonbs')
G.edge['irm_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','knox_system_app')
G.edge['irm_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['irm_app']['knox_system_app']['fill'] = 'red'
G.add_edge('irm_app','mediaserver')
G.edge['irm_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['irm_app']['mediaserver']['fill'] = 'red'
G.add_edge('irm_app','mediaserver')
G.edge['irm_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','newAttr1')
G.edge['irm_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['irm_app']['newAttr1']['fill'] = 'red'
G.add_edge('irm_app','newAttr1')
G.edge['irm_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read]'
G.edge['irm_app']['newAttr1']['fill'] = 'red'
G.add_edge('irm_app','newAttr40')
G.edge['irm_app']['newAttr40']['write-read'] = '[write read]'
G.edge['irm_app']['newAttr40']['fill'] = 'red'
G.add_edge('irm_app','qseecomd')
G.edge['irm_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_app']['qseecomd']['fill'] = 'red'
G.add_edge('irm_app','qseecomd')
G.edge['irm_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','runas')
G.edge['irm_app']['runas']['write-read'] = '[write read]'
G.edge['irm_app']['runas']['fill'] = 'red'
G.add_edge('irm_app','shell')
G.edge['irm_app']['shell']['write-read'] = '[write read][setopt getopt][open open][setattr getattr][write read]'
G.edge['irm_app']['shell']['fill'] = 'red'
G.add_edge('irm_app','shell')
G.edge['irm_app']['shell']['write-read'] = '[write read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','s_system_app')
G.edge['irm_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read]'
G.edge['irm_app']['s_system_app']['fill'] = 'red'
G.add_edge('irm_app','s_system_app')
G.edge['irm_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read][append read]'
G.add_edge('irm_app','s_system_app')
G.edge['irm_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read]'
G.edge['irm_app']['s_system_app']['fill'] = 'red'
G.add_edge('irm_app','sysprof')
G.edge['irm_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_app']['sysprof']['fill'] = 'red'
G.add_edge('irm_app','sysprof')
G.edge['irm_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','system_app')
G.edge['irm_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['irm_app']['system_app']['fill'] = 'red'
G.add_edge('irm_app','system_server')
G.edge['irm_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['irm_app']['system_server']['fill'] = 'red'
G.add_edge('irm_app','vdc')
G.edge['irm_app']['vdc']['write-read'] = '[write read]'
G.edge['irm_app']['vdc']['fill'] = 'red'
G.add_edge('irm_app','zygote')
G.edge['irm_app']['zygote']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['irm_app']['zygote']['fill'] = 'red'
G.add_edge('irm_platform_app','adbd')
G.edge['irm_platform_app']['adbd']['write-read'] = '[open open]'
G.add_edge('irm_platform_app','dumpstate')
G.edge['irm_platform_app']['dumpstate']['write-read'] = '[open open]'
G.add_edge('irm_platform_app','ime_app')
G.edge['irm_platform_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('irm_platform_app','itsonbs')
G.edge['irm_platform_app']['itsonbs']['write-read'] = '[open open]'
G.add_edge('irm_platform_app','knox_system_app')
G.edge['irm_platform_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('irm_platform_app','mediaserver')
G.edge['irm_platform_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('irm_platform_app','newAttr1')
G.edge['irm_platform_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('irm_platform_app','qseecomd')
G.edge['irm_platform_app']['qseecomd']['write-read'] = '[open open]'
G.add_edge('irm_platform_app','shell')
G.edge['irm_platform_app']['shell']['write-read'] = '[open open]'
G.add_edge('irm_platform_app','s_system_app')
G.edge['irm_platform_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('irm_platform_app','s_system_app')
G.edge['irm_platform_app']['s_system_app']['write-read'] = '[open open][open open]'
G.add_edge('irm_platform_app','sysprof')
G.edge['irm_platform_app']['sysprof']['write-read'] = '[open open]'
G.add_edge('irm_platform_app','system_app')
G.edge['irm_platform_app']['system_app']['write-read'] = '[open open]'
G.add_edge('irm_platform_app','adbd')
G.edge['irm_platform_app']['adbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_platform_app','dumpstate')
G.edge['irm_platform_app']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_platform_app','installd')
G.edge['irm_platform_app']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('irm_platform_app','itsonbs')
G.edge['irm_platform_app']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_platform_app','mediaserver')
G.edge['irm_platform_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('irm_platform_app','qseecomd')
G.edge['irm_platform_app']['qseecomd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_platform_app','shell')
G.edge['irm_platform_app']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_platform_app','sysprof')
G.edge['irm_platform_app']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_platform_app','adbd')
G.edge['irm_platform_app']['adbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_platform_app']['adbd']['fill'] = 'red'
G.add_edge('irm_platform_app','adbd')
G.edge['irm_platform_app']['adbd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('irm_platform_app','binderservicedomain')
G.edge['irm_platform_app']['binderservicedomain']['write-read'] = '[write read]'
G.edge['irm_platform_app']['binderservicedomain']['fill'] = 'red'
G.add_edge('irm_platform_app','dumpstate')
G.edge['irm_platform_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_platform_app']['dumpstate']['fill'] = 'red'
G.add_edge('irm_platform_app','dumpstate')
G.edge['irm_platform_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('irm_platform_app','ime_app')
G.edge['irm_platform_app']['ime_app']['write-read'] = '[open open][write read]'
G.edge['irm_platform_app']['ime_app']['fill'] = 'red'
G.add_edge('irm_platform_app','itsonbs')
G.edge['irm_platform_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_platform_app']['itsonbs']['fill'] = 'red'
G.add_edge('irm_platform_app','itsonbs')
G.edge['irm_platform_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('irm_platform_app','knox_system_app')
G.edge['irm_platform_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['irm_platform_app']['knox_system_app']['fill'] = 'red'
G.add_edge('irm_platform_app','mediaserver')
G.edge['irm_platform_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['irm_platform_app']['mediaserver']['fill'] = 'red'
G.add_edge('irm_platform_app','mediaserver')
G.edge['irm_platform_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('irm_platform_app','newAttr1')
G.edge['irm_platform_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['irm_platform_app']['newAttr1']['fill'] = 'red'
G.add_edge('irm_platform_app','newAttr1')
G.edge['irm_platform_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read]'
G.edge['irm_platform_app']['newAttr1']['fill'] = 'red'
G.add_edge('irm_platform_app','newAttr40')
G.edge['irm_platform_app']['newAttr40']['write-read'] = '[write read]'
G.edge['irm_platform_app']['newAttr40']['fill'] = 'red'
G.add_edge('irm_platform_app','qseecomd')
G.edge['irm_platform_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_platform_app']['qseecomd']['fill'] = 'red'
G.add_edge('irm_platform_app','qseecomd')
G.edge['irm_platform_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('irm_platform_app','runas')
G.edge['irm_platform_app']['runas']['write-read'] = '[write read]'
G.edge['irm_platform_app']['runas']['fill'] = 'red'
G.add_edge('irm_platform_app','shell')
G.edge['irm_platform_app']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_platform_app']['shell']['fill'] = 'red'
G.add_edge('irm_platform_app','shell')
G.edge['irm_platform_app']['shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('irm_platform_app','s_system_app')
G.edge['irm_platform_app']['s_system_app']['write-read'] = '[open open][open open][write read]'
G.edge['irm_platform_app']['s_system_app']['fill'] = 'red'
G.add_edge('irm_platform_app','s_system_app')
G.edge['irm_platform_app']['s_system_app']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('irm_platform_app','s_system_app')
G.edge['irm_platform_app']['s_system_app']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['irm_platform_app']['s_system_app']['fill'] = 'red'
G.add_edge('irm_platform_app','sysprof')
G.edge['irm_platform_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_platform_app']['sysprof']['fill'] = 'red'
G.add_edge('irm_platform_app','sysprof')
G.edge['irm_platform_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('irm_platform_app','system_app')
G.edge['irm_platform_app']['system_app']['write-read'] = '[open open][write read]'
G.edge['irm_platform_app']['system_app']['fill'] = 'red'
G.add_edge('irm_platform_app','system_server')
G.edge['irm_platform_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['irm_platform_app']['system_server']['fill'] = 'red'
G.add_edge('irm_platform_app','vdc')
G.edge['irm_platform_app']['vdc']['write-read'] = '[write read]'
G.edge['irm_platform_app']['vdc']['fill'] = 'red'
G.add_edge('irm_platform_app','zygote')
G.edge['irm_platform_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['irm_platform_app']['zygote']['fill'] = 'red'
G.add_edge('itsonbs','adbd')
G.edge['itsonbs']['adbd']['write-read'] = '[write read][add_name search][open open][write read][append read][open open]'
G.add_edge('itsonbs','dumpstate')
G.edge['itsonbs']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('itsonbs','ime_app')
G.edge['itsonbs']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('itsonbs','itsonbs')
G.edge['itsonbs']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('itsonbs','knox_system_app')
G.edge['itsonbs']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('itsonbs','mediaserver')
G.edge['itsonbs']['mediaserver']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('itsonbs','newAttr1')
G.edge['itsonbs']['newAttr1']['write-read'] = '[open open][write read][open open]'
G.add_edge('itsonbs','qseecomd')
G.edge['itsonbs']['qseecomd']['write-read'] = '[open open]'
G.add_edge('itsonbs','shell')
G.edge['itsonbs']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('itsonbs','s_system_app')
G.edge['itsonbs']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('itsonbs','s_system_app')
G.edge['itsonbs']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('itsonbs','sysprof')
G.edge['itsonbs']['sysprof']['write-read'] = '[open open]'
G.add_edge('itsonbs','system_app')
G.edge['itsonbs']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('itsonbs','adbd')
G.edge['itsonbs']['adbd']['write-read'] = '[write read][add_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('itsonbs','dumpstate')
G.edge['itsonbs']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('itsonbs','installd')
G.edge['itsonbs']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr]'
G.add_edge('itsonbs','itsonbs')
G.edge['itsonbs']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('itsonbs','mediaserver')
G.edge['itsonbs']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('itsonbs','qseecomd')
G.edge['itsonbs']['qseecomd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','shell')
G.edge['itsonbs']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('itsonbs','sysprof')
G.edge['itsonbs']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','adbd')
G.edge['itsonbs']['adbd']['write-read'] = '[write read][add_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['itsonbs']['adbd']['fill'] = 'red'
G.add_edge('itsonbs','adbd')
G.edge['itsonbs']['adbd']['write-read'] = '[write read][add_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('itsonbs','binderservicedomain')
G.edge['itsonbs']['binderservicedomain']['write-read'] = '[open open][write read][append read][write read]'
G.edge['itsonbs']['binderservicedomain']['fill'] = 'red'
G.add_edge('itsonbs','dumpstate')
G.edge['itsonbs']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['itsonbs']['dumpstate']['fill'] = 'red'
G.add_edge('itsonbs','dumpstate')
G.edge['itsonbs']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('itsonbs','ime_app')
G.edge['itsonbs']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['itsonbs']['ime_app']['fill'] = 'red'
G.add_edge('itsonbs','itsonbs')
G.edge['itsonbs']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['itsonbs']['itsonbs']['fill'] = 'red'
G.add_edge('itsonbs','itsonbs')
G.edge['itsonbs']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('itsonbs','knox_system_app')
G.edge['itsonbs']['knox_system_app']['write-read'] = '[open open][write read]'
G.edge['itsonbs']['knox_system_app']['fill'] = 'red'
G.add_edge('itsonbs','mediaserver')
G.edge['itsonbs']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['itsonbs']['mediaserver']['fill'] = 'red'
G.add_edge('itsonbs','mediaserver')
G.edge['itsonbs']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('itsonbs','newAttr1')
G.edge['itsonbs']['newAttr1']['write-read'] = '[open open][write read][open open][write read]'
G.edge['itsonbs']['newAttr1']['fill'] = 'red'
G.add_edge('itsonbs','newAttr1')
G.edge['itsonbs']['newAttr1']['write-read'] = '[open open][write read][open open][write read][write read]'
G.edge['itsonbs']['newAttr1']['fill'] = 'red'
G.add_edge('itsonbs','newAttr40')
G.edge['itsonbs']['newAttr40']['write-read'] = '[write read]'
G.edge['itsonbs']['newAttr40']['fill'] = 'red'
G.add_edge('itsonbs','qseecomd')
G.edge['itsonbs']['qseecomd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['qseecomd']['fill'] = 'red'
G.add_edge('itsonbs','qseecomd')
G.edge['itsonbs']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('itsonbs','runas')
G.edge['itsonbs']['runas']['write-read'] = '[write read][write read]'
G.edge['itsonbs']['runas']['fill'] = 'red'
G.add_edge('itsonbs','shell')
G.edge['itsonbs']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['itsonbs']['shell']['fill'] = 'red'
G.add_edge('itsonbs','shell')
G.edge['itsonbs']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('itsonbs','s_system_app')
G.edge['itsonbs']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read]'
G.edge['itsonbs']['s_system_app']['fill'] = 'red'
G.add_edge('itsonbs','s_system_app')
G.edge['itsonbs']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read]'
G.add_edge('itsonbs','s_system_app')
G.edge['itsonbs']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read][write read]'
G.edge['itsonbs']['s_system_app']['fill'] = 'red'
G.add_edge('itsonbs','sysprof')
G.edge['itsonbs']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['sysprof']['fill'] = 'red'
G.add_edge('itsonbs','sysprof')
G.edge['itsonbs']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('itsonbs','system_app')
G.edge['itsonbs']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['itsonbs']['system_app']['fill'] = 'red'
G.add_edge('itsonbs','system_server')
G.edge['itsonbs']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][write read]'
G.edge['itsonbs']['system_server']['fill'] = 'red'
G.add_edge('itsonbs','vdc')
G.edge['itsonbs']['vdc']['write-read'] = '[write read]'
G.edge['itsonbs']['vdc']['fill'] = 'red'
G.add_edge('itsonbs','zygote')
G.edge['itsonbs']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['itsonbs']['zygote']['fill'] = 'red'
G.add_edge('knox_system_app','adbd')
G.edge['knox_system_app']['adbd']['write-read'] = '[open open]'
G.add_edge('knox_system_app','dumpstate')
G.edge['knox_system_app']['dumpstate']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_system_app','ime_app')
G.edge['knox_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('knox_system_app','itsonbs')
G.edge['knox_system_app']['itsonbs']['write-read'] = '[open open]'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_system_app','mediaserver')
G.edge['knox_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_system_app','newAttr1')
G.edge['knox_system_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_system_app','qseecomd')
G.edge['knox_system_app']['qseecomd']['write-read'] = '[open open]'
G.add_edge('knox_system_app','shell')
G.edge['knox_system_app']['shell']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('knox_system_app','sysprof')
G.edge['knox_system_app']['sysprof']['write-read'] = '[open open]'
G.add_edge('knox_system_app','system_app')
G.edge['knox_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_system_app','adbd')
G.edge['knox_system_app']['adbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','dumpstate')
G.edge['knox_system_app']['dumpstate']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('knox_system_app','installd')
G.edge['knox_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('knox_system_app','itsonbs')
G.edge['knox_system_app']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','mediaserver')
G.edge['knox_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('knox_system_app','qseecomd')
G.edge['knox_system_app']['qseecomd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','shell')
G.edge['knox_system_app']['shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('knox_system_app','sysprof')
G.edge['knox_system_app']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','adbd')
G.edge['knox_system_app']['adbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['adbd']['fill'] = 'red'
G.add_edge('knox_system_app','adbd')
G.edge['knox_system_app']['adbd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','binderservicedomain')
G.edge['knox_system_app']['binderservicedomain']['write-read'] = '[write read]'
G.edge['knox_system_app']['binderservicedomain']['fill'] = 'red'
G.add_edge('knox_system_app','dumpstate')
G.edge['knox_system_app']['dumpstate']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['knox_system_app']['dumpstate']['fill'] = 'red'
G.add_edge('knox_system_app','dumpstate')
G.edge['knox_system_app']['dumpstate']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','ime_app')
G.edge['knox_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['knox_system_app']['ime_app']['fill'] = 'red'
G.add_edge('knox_system_app','itsonbs')
G.edge['knox_system_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['itsonbs']['fill'] = 'red'
G.add_edge('knox_system_app','itsonbs')
G.edge['knox_system_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['knox_system_app']['knox_system_app']['fill'] = 'red'
G.add_edge('knox_system_app','mediaserver')
G.edge['knox_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['knox_system_app']['mediaserver']['fill'] = 'red'
G.add_edge('knox_system_app','mediaserver')
G.edge['knox_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','newAttr1')
G.edge['knox_system_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['knox_system_app']['newAttr1']['fill'] = 'red'
G.add_edge('knox_system_app','newAttr1')
G.edge['knox_system_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read]'
G.edge['knox_system_app']['newAttr1']['fill'] = 'red'
G.add_edge('knox_system_app','newAttr40')
G.edge['knox_system_app']['newAttr40']['write-read'] = '[write read]'
G.edge['knox_system_app']['newAttr40']['fill'] = 'red'
G.add_edge('knox_system_app','qseecomd')
G.edge['knox_system_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['qseecomd']['fill'] = 'red'
G.add_edge('knox_system_app','qseecomd')
G.edge['knox_system_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','runas')
G.edge['knox_system_app']['runas']['write-read'] = '[write read]'
G.edge['knox_system_app']['runas']['fill'] = 'red'
G.add_edge('knox_system_app','shell')
G.edge['knox_system_app']['shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_system_app']['shell']['fill'] = 'red'
G.add_edge('knox_system_app','shell')
G.edge['knox_system_app']['shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read]'
G.edge['knox_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read]'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read][write read]'
G.edge['knox_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('knox_system_app','sysprof')
G.edge['knox_system_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['sysprof']['fill'] = 'red'
G.add_edge('knox_system_app','sysprof')
G.edge['knox_system_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','system_app')
G.edge['knox_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['knox_system_app']['system_app']['fill'] = 'red'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['knox_system_app']['system_server']['fill'] = 'red'
G.add_edge('knox_system_app','vdc')
G.edge['knox_system_app']['vdc']['write-read'] = '[write read]'
G.edge['knox_system_app']['vdc']['fill'] = 'red'
G.add_edge('knox_system_app','zygote')
G.edge['knox_system_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['knox_system_app']['zygote']['fill'] = 'red'
G.add_edge('knox_untrusted_app','adbd')
G.edge['knox_untrusted_app']['adbd']['write-read'] = '[write read][open open]'
G.add_edge('knox_untrusted_app','dumpstate')
G.edge['knox_untrusted_app']['dumpstate']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','ime_app')
G.edge['knox_untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_untrusted_app','itsonbs')
G.edge['knox_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_untrusted_app','knox_system_app')
G.edge['knox_untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_untrusted_app','mediaserver')
G.edge['knox_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_untrusted_app','newAttr1')
G.edge['knox_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_untrusted_app','qseecomd')
G.edge['knox_untrusted_app']['qseecomd']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','shell')
G.edge['knox_untrusted_app']['shell']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','s_system_app')
G.edge['knox_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_untrusted_app','s_system_app')
G.edge['knox_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('knox_untrusted_app','sysprof')
G.edge['knox_untrusted_app']['sysprof']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','system_app')
G.edge['knox_untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_untrusted_app','adbd')
G.edge['knox_untrusted_app']['adbd']['write-read'] = '[write read][open open][setattr getattr]'
G.add_edge('knox_untrusted_app','dumpstate')
G.edge['knox_untrusted_app']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','installd')
G.edge['knox_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('knox_untrusted_app','itsonbs')
G.edge['knox_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('knox_untrusted_app','mediaserver')
G.edge['knox_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('knox_untrusted_app','qseecomd')
G.edge['knox_untrusted_app']['qseecomd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','shell')
G.edge['knox_untrusted_app']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','sysprof')
G.edge['knox_untrusted_app']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','adbd')
G.edge['knox_untrusted_app']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['adbd']['fill'] = 'red'
G.add_edge('knox_untrusted_app','adbd')
G.edge['knox_untrusted_app']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','binderservicedomain')
G.edge['knox_untrusted_app']['binderservicedomain']['write-read'] = '[write read]'
G.edge['knox_untrusted_app']['binderservicedomain']['fill'] = 'red'
G.add_edge('knox_untrusted_app','dumpstate')
G.edge['knox_untrusted_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['dumpstate']['fill'] = 'red'
G.add_edge('knox_untrusted_app','dumpstate')
G.edge['knox_untrusted_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','ime_app')
G.edge['knox_untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['knox_untrusted_app']['ime_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','itsonbs')
G.edge['knox_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['itsonbs']['fill'] = 'red'
G.add_edge('knox_untrusted_app','itsonbs')
G.edge['knox_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','knox_system_app')
G.edge['knox_untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['knox_untrusted_app']['knox_system_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','mediaserver')
G.edge['knox_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['mediaserver']['fill'] = 'red'
G.add_edge('knox_untrusted_app','mediaserver')
G.edge['knox_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','newAttr1')
G.edge['knox_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['knox_untrusted_app']['newAttr1']['fill'] = 'red'
G.add_edge('knox_untrusted_app','newAttr1')
G.edge['knox_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read]'
G.edge['knox_untrusted_app']['newAttr1']['fill'] = 'red'
G.add_edge('knox_untrusted_app','newAttr40')
G.edge['knox_untrusted_app']['newAttr40']['write-read'] = '[write read]'
G.edge['knox_untrusted_app']['newAttr40']['fill'] = 'red'
G.add_edge('knox_untrusted_app','qseecomd')
G.edge['knox_untrusted_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['qseecomd']['fill'] = 'red'
G.add_edge('knox_untrusted_app','qseecomd')
G.edge['knox_untrusted_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','runas')
G.edge['knox_untrusted_app']['runas']['write-read'] = '[write read]'
G.edge['knox_untrusted_app']['runas']['fill'] = 'red'
G.add_edge('knox_untrusted_app','shell')
G.edge['knox_untrusted_app']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['shell']['fill'] = 'red'
G.add_edge('knox_untrusted_app','shell')
G.edge['knox_untrusted_app']['shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','s_system_app')
G.edge['knox_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read]'
G.edge['knox_untrusted_app']['s_system_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','s_system_app')
G.edge['knox_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read][append read]'
G.add_edge('knox_untrusted_app','s_system_app')
G.edge['knox_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read]'
G.edge['knox_untrusted_app']['s_system_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','sysprof')
G.edge['knox_untrusted_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['sysprof']['fill'] = 'red'
G.add_edge('knox_untrusted_app','sysprof')
G.edge['knox_untrusted_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','system_app')
G.edge['knox_untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['knox_untrusted_app']['system_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','system_server')
G.edge['knox_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['knox_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('knox_untrusted_app','vdc')
G.edge['knox_untrusted_app']['vdc']['write-read'] = '[write read]'
G.edge['knox_untrusted_app']['vdc']['fill'] = 'red'
G.add_edge('knox_untrusted_app','zygote')
G.edge['knox_untrusted_app']['zygote']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['knox_untrusted_app']['zygote']['fill'] = 'red'
G.add_edge('llk_untrusted_app','adbd')
G.edge['llk_untrusted_app']['adbd']['write-read'] = '[write read][open open]'
G.add_edge('llk_untrusted_app','dumpstate')
G.edge['llk_untrusted_app']['dumpstate']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','ime_app')
G.edge['llk_untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('llk_untrusted_app','itsonbs')
G.edge['llk_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('llk_untrusted_app','knox_system_app')
G.edge['llk_untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('llk_untrusted_app','mediaserver')
G.edge['llk_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('llk_untrusted_app','newAttr1')
G.edge['llk_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('llk_untrusted_app','qseecomd')
G.edge['llk_untrusted_app']['qseecomd']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','shell')
G.edge['llk_untrusted_app']['shell']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','s_system_app')
G.edge['llk_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('llk_untrusted_app','s_system_app')
G.edge['llk_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('llk_untrusted_app','sysprof')
G.edge['llk_untrusted_app']['sysprof']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','system_app')
G.edge['llk_untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('llk_untrusted_app','adbd')
G.edge['llk_untrusted_app']['adbd']['write-read'] = '[write read][open open][setattr getattr]'
G.add_edge('llk_untrusted_app','dumpstate')
G.edge['llk_untrusted_app']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','installd')
G.edge['llk_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('llk_untrusted_app','itsonbs')
G.edge['llk_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('llk_untrusted_app','mediaserver')
G.edge['llk_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('llk_untrusted_app','qseecomd')
G.edge['llk_untrusted_app']['qseecomd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','shell')
G.edge['llk_untrusted_app']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','sysprof')
G.edge['llk_untrusted_app']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','adbd')
G.edge['llk_untrusted_app']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['adbd']['fill'] = 'red'
G.add_edge('llk_untrusted_app','adbd')
G.edge['llk_untrusted_app']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','binderservicedomain')
G.edge['llk_untrusted_app']['binderservicedomain']['write-read'] = '[write read]'
G.edge['llk_untrusted_app']['binderservicedomain']['fill'] = 'red'
G.add_edge('llk_untrusted_app','dumpstate')
G.edge['llk_untrusted_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['dumpstate']['fill'] = 'red'
G.add_edge('llk_untrusted_app','dumpstate')
G.edge['llk_untrusted_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','ime_app')
G.edge['llk_untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['llk_untrusted_app']['ime_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','itsonbs')
G.edge['llk_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['itsonbs']['fill'] = 'red'
G.add_edge('llk_untrusted_app','itsonbs')
G.edge['llk_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','knox_system_app')
G.edge['llk_untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['llk_untrusted_app']['knox_system_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','mediaserver')
G.edge['llk_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['mediaserver']['fill'] = 'red'
G.add_edge('llk_untrusted_app','mediaserver')
G.edge['llk_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','newAttr1')
G.edge['llk_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['llk_untrusted_app']['newAttr1']['fill'] = 'red'
G.add_edge('llk_untrusted_app','newAttr1')
G.edge['llk_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read]'
G.edge['llk_untrusted_app']['newAttr1']['fill'] = 'red'
G.add_edge('llk_untrusted_app','newAttr40')
G.edge['llk_untrusted_app']['newAttr40']['write-read'] = '[write read]'
G.edge['llk_untrusted_app']['newAttr40']['fill'] = 'red'
G.add_edge('llk_untrusted_app','qseecomd')
G.edge['llk_untrusted_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['qseecomd']['fill'] = 'red'
G.add_edge('llk_untrusted_app','qseecomd')
G.edge['llk_untrusted_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','runas')
G.edge['llk_untrusted_app']['runas']['write-read'] = '[write read]'
G.edge['llk_untrusted_app']['runas']['fill'] = 'red'
G.add_edge('llk_untrusted_app','shell')
G.edge['llk_untrusted_app']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['shell']['fill'] = 'red'
G.add_edge('llk_untrusted_app','shell')
G.edge['llk_untrusted_app']['shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','s_system_app')
G.edge['llk_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read]'
G.edge['llk_untrusted_app']['s_system_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','s_system_app')
G.edge['llk_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read][append read]'
G.add_edge('llk_untrusted_app','s_system_app')
G.edge['llk_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read]'
G.edge['llk_untrusted_app']['s_system_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','sysprof')
G.edge['llk_untrusted_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['sysprof']['fill'] = 'red'
G.add_edge('llk_untrusted_app','sysprof')
G.edge['llk_untrusted_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','system_app')
G.edge['llk_untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['llk_untrusted_app']['system_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','system_server')
G.edge['llk_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['llk_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('llk_untrusted_app','vdc')
G.edge['llk_untrusted_app']['vdc']['write-read'] = '[write read]'
G.edge['llk_untrusted_app']['vdc']['fill'] = 'red'
G.add_edge('llk_untrusted_app','zygote')
G.edge['llk_untrusted_app']['zygote']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['llk_untrusted_app']['zygote']['fill'] = 'red'
G.add_edge('mediaserver','adbd')
G.edge['mediaserver']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('mediaserver','dumpstate')
G.edge['mediaserver']['dumpstate']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('mediaserver','ime_app')
G.edge['mediaserver']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','itsonbs')
G.edge['mediaserver']['itsonbs']['write-read'] = '[open open]'
G.add_edge('mediaserver','knox_system_app')
G.edge['mediaserver']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('mediaserver','newAttr1')
G.edge['mediaserver']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','qseecomd')
G.edge['mediaserver']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','shell')
G.edge['mediaserver']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('mediaserver','s_system_app')
G.edge['mediaserver']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','s_system_app')
G.edge['mediaserver']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open]'
G.add_edge('mediaserver','sysprof')
G.edge['mediaserver']['sysprof']['write-read'] = '[open open]'
G.add_edge('mediaserver','system_app')
G.edge['mediaserver']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','adbd')
G.edge['mediaserver']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','dumpstate')
G.edge['mediaserver']['dumpstate']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','installd')
G.edge['mediaserver']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr]'
G.add_edge('mediaserver','itsonbs')
G.edge['mediaserver']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','qseecomd')
G.edge['mediaserver']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','shell')
G.edge['mediaserver']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','sysprof')
G.edge['mediaserver']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','adbd')
G.edge['mediaserver']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['adbd']['fill'] = 'red'
G.add_edge('mediaserver','adbd')
G.edge['mediaserver']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','binderservicedomain')
G.edge['mediaserver']['binderservicedomain']['write-read'] = '[open open][write read][append read][write read]'
G.edge['mediaserver']['binderservicedomain']['fill'] = 'red'
G.add_edge('mediaserver','dumpstate')
G.edge['mediaserver']['dumpstate']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['dumpstate']['fill'] = 'red'
G.add_edge('mediaserver','dumpstate')
G.edge['mediaserver']['dumpstate']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','ime_app')
G.edge['mediaserver']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['ime_app']['fill'] = 'red'
G.add_edge('mediaserver','itsonbs')
G.edge['mediaserver']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['itsonbs']['fill'] = 'red'
G.add_edge('mediaserver','itsonbs')
G.edge['mediaserver']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','knox_system_app')
G.edge['mediaserver']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['knox_system_app']['fill'] = 'red'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['mediaserver']['fill'] = 'red'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','newAttr1')
G.edge['mediaserver']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['newAttr1']['fill'] = 'red'
G.add_edge('mediaserver','newAttr1')
G.edge['mediaserver']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][write read]'
G.edge['mediaserver']['newAttr1']['fill'] = 'red'
G.add_edge('mediaserver','newAttr40')
G.edge['mediaserver']['newAttr40']['write-read'] = '[write read]'
G.edge['mediaserver']['newAttr40']['fill'] = 'red'
G.add_edge('mediaserver','qseecomd')
G.edge['mediaserver']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['qseecomd']['fill'] = 'red'
G.add_edge('mediaserver','qseecomd')
G.edge['mediaserver']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','runas')
G.edge['mediaserver']['runas']['write-read'] = '[write read][write read]'
G.edge['mediaserver']['runas']['fill'] = 'red'
G.add_edge('mediaserver','shell')
G.edge['mediaserver']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['shell']['fill'] = 'red'
G.add_edge('mediaserver','shell')
G.edge['mediaserver']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','s_system_app')
G.edge['mediaserver']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read]'
G.edge['mediaserver']['s_system_app']['fill'] = 'red'
G.add_edge('mediaserver','s_system_app')
G.edge['mediaserver']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][append read]'
G.add_edge('mediaserver','s_system_app')
G.edge['mediaserver']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][append read][write read]'
G.edge['mediaserver']['s_system_app']['fill'] = 'red'
G.add_edge('mediaserver','sysprof')
G.edge['mediaserver']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['sysprof']['fill'] = 'red'
G.add_edge('mediaserver','sysprof')
G.edge['mediaserver']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','system_app')
G.edge['mediaserver']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['system_app']['fill'] = 'red'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['mediaserver']['system_server']['fill'] = 'red'
G.add_edge('mediaserver','vdc')
G.edge['mediaserver']['vdc']['write-read'] = '[write read][write read]'
G.edge['mediaserver']['vdc']['fill'] = 'red'
G.add_edge('mediaserver','zygote')
G.edge['mediaserver']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][write read]'
G.edge['mediaserver']['zygote']['fill'] = 'red'
G.add_edge('newAttr13','adbd')
G.edge['newAttr13']['adbd']['write-read'] = '[setattr getattr]'
G.add_edge('newAttr13','dumpstate')
G.edge['newAttr13']['dumpstate']['write-read'] = '[setattr getattr]'
G.add_edge('newAttr13','installd')
G.edge['newAttr13']['installd']['write-read'] = '[setattr getattr]'
G.add_edge('newAttr13','itsonbs')
G.edge['newAttr13']['itsonbs']['write-read'] = '[setattr getattr]'
G.add_edge('newAttr13','mediaserver')
G.edge['newAttr13']['mediaserver']['write-read'] = '[setattr getattr]'
G.add_edge('newAttr13','qseecomd')
G.edge['newAttr13']['qseecomd']['write-read'] = '[setattr getattr]'
G.add_edge('newAttr13','shell')
G.edge['newAttr13']['shell']['write-read'] = '[setattr getattr]'
G.add_edge('newAttr13','sysprof')
G.edge['newAttr13']['sysprof']['write-read'] = '[setattr getattr]'
G.add_edge('newAttr1','adbd')
G.edge['newAttr1']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr1','dumpstate')
G.edge['newAttr1']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr1','ime_app')
G.edge['newAttr1']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr1','itsonbs')
G.edge['newAttr1']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('newAttr1','knox_system_app')
G.edge['newAttr1']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr1','mediaserver')
G.edge['newAttr1']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open execmod][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('newAttr1','qseecomd')
G.edge['newAttr1']['qseecomd']['write-read'] = '[open open]'
G.add_edge('newAttr1','shell')
G.edge['newAttr1']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('newAttr1','s_system_app')
G.edge['newAttr1']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr1','s_system_app')
G.edge['newAttr1']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('newAttr1','sysprof')
G.edge['newAttr1']['sysprof']['write-read'] = '[open open]'
G.add_edge('newAttr1','system_app')
G.edge['newAttr1']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr1','adbd')
G.edge['newAttr1']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('newAttr1','dumpstate')
G.edge['newAttr1']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('newAttr1','installd')
G.edge['newAttr1']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('newAttr1','itsonbs')
G.edge['newAttr1']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('newAttr1','mediaserver')
G.edge['newAttr1']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('newAttr1','qseecomd')
G.edge['newAttr1']['qseecomd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr1','shell')
G.edge['newAttr1']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('newAttr1','sysprof')
G.edge['newAttr1']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr1','adbd')
G.edge['newAttr1']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['newAttr1']['adbd']['fill'] = 'red'
G.add_edge('newAttr1','adbd')
G.edge['newAttr1']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','binderservicedomain')
G.edge['newAttr1']['binderservicedomain']['write-read'] = '[write read]'
G.edge['newAttr1']['binderservicedomain']['fill'] = 'red'
G.add_edge('newAttr1','dumpstate')
G.edge['newAttr1']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['newAttr1']['dumpstate']['fill'] = 'red'
G.add_edge('newAttr1','dumpstate')
G.edge['newAttr1']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','ime_app')
G.edge['newAttr1']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['newAttr1']['ime_app']['fill'] = 'red'
G.add_edge('newAttr1','itsonbs')
G.edge['newAttr1']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['newAttr1']['itsonbs']['fill'] = 'red'
G.add_edge('newAttr1','itsonbs')
G.edge['newAttr1']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','knox_system_app')
G.edge['newAttr1']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['newAttr1']['knox_system_app']['fill'] = 'red'
G.add_edge('newAttr1','mediaserver')
G.edge['newAttr1']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['newAttr1']['mediaserver']['fill'] = 'red'
G.add_edge('newAttr1','mediaserver')
G.edge['newAttr1']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open execmod][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['newAttr1']['newAttr1']['fill'] = 'red'
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open execmod][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][write read][write read]'
G.edge['newAttr1']['newAttr1']['fill'] = 'red'
G.add_edge('newAttr1','newAttr40')
G.edge['newAttr1']['newAttr40']['write-read'] = '[write read]'
G.edge['newAttr1']['newAttr40']['fill'] = 'red'
G.add_edge('newAttr1','qseecomd')
G.edge['newAttr1']['qseecomd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr1']['qseecomd']['fill'] = 'red'
G.add_edge('newAttr1','qseecomd')
G.edge['newAttr1']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','runas')
G.edge['newAttr1']['runas']['write-read'] = '[write read]'
G.edge['newAttr1']['runas']['fill'] = 'red'
G.add_edge('newAttr1','shell')
G.edge['newAttr1']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['newAttr1']['shell']['fill'] = 'red'
G.add_edge('newAttr1','shell')
G.edge['newAttr1']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','s_system_app')
G.edge['newAttr1']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read]'
G.edge['newAttr1']['s_system_app']['fill'] = 'red'
G.add_edge('newAttr1','s_system_app')
G.edge['newAttr1']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read]'
G.add_edge('newAttr1','s_system_app')
G.edge['newAttr1']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read][write read]'
G.edge['newAttr1']['s_system_app']['fill'] = 'red'
G.add_edge('newAttr1','sysprof')
G.edge['newAttr1']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr1']['sysprof']['fill'] = 'red'
G.add_edge('newAttr1','sysprof')
G.edge['newAttr1']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','system_app')
G.edge['newAttr1']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['newAttr1']['system_app']['fill'] = 'red'
G.add_edge('newAttr1','system_server')
G.edge['newAttr1']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['newAttr1']['system_server']['fill'] = 'red'
G.add_edge('newAttr1','vdc')
G.edge['newAttr1']['vdc']['write-read'] = '[write read]'
G.edge['newAttr1']['vdc']['fill'] = 'red'
G.add_edge('newAttr1','zygote')
G.edge['newAttr1']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['newAttr1']['zygote']['fill'] = 'red'
G.add_edge('newAttr1','adbd')
G.edge['newAttr1']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('newAttr1','dumpstate')
G.edge['newAttr1']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('newAttr1','installd')
G.edge['newAttr1']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('newAttr1','itsonbs')
G.edge['newAttr1']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('newAttr1','mediaserver')
G.edge['newAttr1']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('newAttr1','qseecomd')
G.edge['newAttr1']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('newAttr1','shell')
G.edge['newAttr1']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('newAttr1','sysprof')
G.edge['newAttr1']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('platform_app','adbd')
G.edge['platform_app']['adbd']['write-read'] = '[open open]'
G.add_edge('platform_app','dumpstate')
G.edge['platform_app']['dumpstate']['write-read'] = '[open open]'
G.add_edge('platform_app','ime_app')
G.edge['platform_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('platform_app','itsonbs')
G.edge['platform_app']['itsonbs']['write-read'] = '[open open]'
G.add_edge('platform_app','knox_system_app')
G.edge['platform_app']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('platform_app','mediaserver')
G.edge['platform_app']['mediaserver']['write-read'] = '[open open]'
G.add_edge('platform_app','newAttr1')
G.edge['platform_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('platform_app','qseecomd')
G.edge['platform_app']['qseecomd']['write-read'] = '[open open]'
G.add_edge('platform_app','shell')
G.edge['platform_app']['shell']['write-read'] = '[open open]'
G.add_edge('platform_app','s_system_app')
G.edge['platform_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('platform_app','s_system_app')
G.edge['platform_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('platform_app','sysprof')
G.edge['platform_app']['sysprof']['write-read'] = '[open open]'
G.add_edge('platform_app','system_app')
G.edge['platform_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('platform_app','adbd')
G.edge['platform_app']['adbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platform_app','dumpstate')
G.edge['platform_app']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platform_app','installd')
G.edge['platform_app']['installd']['write-read'] = '[setattr getattr]'
G.add_edge('platform_app','itsonbs')
G.edge['platform_app']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platform_app','mediaserver')
G.edge['platform_app']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platform_app','qseecomd')
G.edge['platform_app']['qseecomd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platform_app','shell')
G.edge['platform_app']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platform_app','sysprof')
G.edge['platform_app']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platform_app','adbd')
G.edge['platform_app']['adbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platform_app']['adbd']['fill'] = 'red'
G.add_edge('platform_app','adbd')
G.edge['platform_app']['adbd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('platform_app','binderservicedomain')
G.edge['platform_app']['binderservicedomain']['write-read'] = '[write read]'
G.edge['platform_app']['binderservicedomain']['fill'] = 'red'
G.add_edge('platform_app','dumpstate')
G.edge['platform_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platform_app']['dumpstate']['fill'] = 'red'
G.add_edge('platform_app','dumpstate')
G.edge['platform_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('platform_app','ime_app')
G.edge['platform_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['platform_app']['ime_app']['fill'] = 'red'
G.add_edge('platform_app','itsonbs')
G.edge['platform_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platform_app']['itsonbs']['fill'] = 'red'
G.add_edge('platform_app','itsonbs')
G.edge['platform_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('platform_app','knox_system_app')
G.edge['platform_app']['knox_system_app']['write-read'] = '[open open][write read]'
G.edge['platform_app']['knox_system_app']['fill'] = 'red'
G.add_edge('platform_app','mediaserver')
G.edge['platform_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platform_app']['mediaserver']['fill'] = 'red'
G.add_edge('platform_app','mediaserver')
G.edge['platform_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('platform_app','newAttr1')
G.edge['platform_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['platform_app']['newAttr1']['fill'] = 'red'
G.add_edge('platform_app','newAttr1')
G.edge['platform_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][write read]'
G.edge['platform_app']['newAttr1']['fill'] = 'red'
G.add_edge('platform_app','newAttr40')
G.edge['platform_app']['newAttr40']['write-read'] = '[write read]'
G.edge['platform_app']['newAttr40']['fill'] = 'red'
G.add_edge('platform_app','qseecomd')
G.edge['platform_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platform_app']['qseecomd']['fill'] = 'red'
G.add_edge('platform_app','qseecomd')
G.edge['platform_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('platform_app','runas')
G.edge['platform_app']['runas']['write-read'] = '[write read]'
G.edge['platform_app']['runas']['fill'] = 'red'
G.add_edge('platform_app','shell')
G.edge['platform_app']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platform_app']['shell']['fill'] = 'red'
G.add_edge('platform_app','shell')
G.edge['platform_app']['shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('platform_app','s_system_app')
G.edge['platform_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read]'
G.edge['platform_app']['s_system_app']['fill'] = 'red'
G.add_edge('platform_app','s_system_app')
G.edge['platform_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read]'
G.add_edge('platform_app','s_system_app')
G.edge['platform_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read][write read]'
G.edge['platform_app']['s_system_app']['fill'] = 'red'
G.add_edge('platform_app','sysprof')
G.edge['platform_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platform_app']['sysprof']['fill'] = 'red'
G.add_edge('platform_app','sysprof')
G.edge['platform_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('platform_app','system_app')
G.edge['platform_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['platform_app']['system_app']['fill'] = 'red'
G.add_edge('platform_app','system_server')
G.edge['platform_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['platform_app']['system_server']['fill'] = 'red'
G.add_edge('platform_app','vdc')
G.edge['platform_app']['vdc']['write-read'] = '[write read]'
G.edge['platform_app']['vdc']['fill'] = 'red'
G.add_edge('platform_app','zygote')
G.edge['platform_app']['zygote']['write-read'] = '[write read]'
G.edge['platform_app']['zygote']['fill'] = 'red'
G.add_edge('policyloader_app','adbd')
G.edge['policyloader_app']['adbd']['write-read'] = '[open open]'
G.add_edge('policyloader_app','dumpstate')
G.edge['policyloader_app']['dumpstate']['write-read'] = '[open open]'
G.add_edge('policyloader_app','ime_app')
G.edge['policyloader_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('policyloader_app','itsonbs')
G.edge['policyloader_app']['itsonbs']['write-read'] = '[open open]'
G.add_edge('policyloader_app','knox_system_app')
G.edge['policyloader_app']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('policyloader_app','mediaserver')
G.edge['policyloader_app']['mediaserver']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('policyloader_app','newAttr1')
G.edge['policyloader_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('policyloader_app','qseecomd')
G.edge['policyloader_app']['qseecomd']['write-read'] = '[open open]'
G.add_edge('policyloader_app','shell')
G.edge['policyloader_app']['shell']['write-read'] = '[open open]'
G.add_edge('policyloader_app','s_system_app')
G.edge['policyloader_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('policyloader_app','s_system_app')
G.edge['policyloader_app']['s_system_app']['write-read'] = '[open open][open open]'
G.add_edge('policyloader_app','sysprof')
G.edge['policyloader_app']['sysprof']['write-read'] = '[open open]'
G.add_edge('policyloader_app','system_app')
G.edge['policyloader_app']['system_app']['write-read'] = '[open open]'
G.add_edge('policyloader_app','adbd')
G.edge['policyloader_app']['adbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('policyloader_app','dumpstate')
G.edge['policyloader_app']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('policyloader_app','installd')
G.edge['policyloader_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('policyloader_app','itsonbs')
G.edge['policyloader_app']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('policyloader_app','mediaserver')
G.edge['policyloader_app']['mediaserver']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('policyloader_app','qseecomd')
G.edge['policyloader_app']['qseecomd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('policyloader_app','shell')
G.edge['policyloader_app']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('policyloader_app','sysprof')
G.edge['policyloader_app']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('policyloader_app','adbd')
G.edge['policyloader_app']['adbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['policyloader_app']['adbd']['fill'] = 'red'
G.add_edge('policyloader_app','adbd')
G.edge['policyloader_app']['adbd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('policyloader_app','binderservicedomain')
G.edge['policyloader_app']['binderservicedomain']['write-read'] = '[write read]'
G.edge['policyloader_app']['binderservicedomain']['fill'] = 'red'
G.add_edge('policyloader_app','dumpstate')
G.edge['policyloader_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['policyloader_app']['dumpstate']['fill'] = 'red'
G.add_edge('policyloader_app','dumpstate')
G.edge['policyloader_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('policyloader_app','ime_app')
G.edge['policyloader_app']['ime_app']['write-read'] = '[open open][write read]'
G.edge['policyloader_app']['ime_app']['fill'] = 'red'
G.add_edge('policyloader_app','itsonbs')
G.edge['policyloader_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['policyloader_app']['itsonbs']['fill'] = 'red'
G.add_edge('policyloader_app','itsonbs')
G.edge['policyloader_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('policyloader_app','knox_system_app')
G.edge['policyloader_app']['knox_system_app']['write-read'] = '[open open][write read]'
G.edge['policyloader_app']['knox_system_app']['fill'] = 'red'
G.add_edge('policyloader_app','mediaserver')
G.edge['policyloader_app']['mediaserver']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['policyloader_app']['mediaserver']['fill'] = 'red'
G.add_edge('policyloader_app','mediaserver')
G.edge['policyloader_app']['mediaserver']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('policyloader_app','newAttr1')
G.edge['policyloader_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['policyloader_app']['newAttr1']['fill'] = 'red'
G.add_edge('policyloader_app','newAttr1')
G.edge['policyloader_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read]'
G.edge['policyloader_app']['newAttr1']['fill'] = 'red'
G.add_edge('policyloader_app','newAttr40')
G.edge['policyloader_app']['newAttr40']['write-read'] = '[write read]'
G.edge['policyloader_app']['newAttr40']['fill'] = 'red'
G.add_edge('policyloader_app','qseecomd')
G.edge['policyloader_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['policyloader_app']['qseecomd']['fill'] = 'red'
G.add_edge('policyloader_app','qseecomd')
G.edge['policyloader_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('policyloader_app','runas')
G.edge['policyloader_app']['runas']['write-read'] = '[write read]'
G.edge['policyloader_app']['runas']['fill'] = 'red'
G.add_edge('policyloader_app','shell')
G.edge['policyloader_app']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['policyloader_app']['shell']['fill'] = 'red'
G.add_edge('policyloader_app','shell')
G.edge['policyloader_app']['shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('policyloader_app','s_system_app')
G.edge['policyloader_app']['s_system_app']['write-read'] = '[open open][open open][write read]'
G.edge['policyloader_app']['s_system_app']['fill'] = 'red'
G.add_edge('policyloader_app','s_system_app')
G.edge['policyloader_app']['s_system_app']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('policyloader_app','s_system_app')
G.edge['policyloader_app']['s_system_app']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['policyloader_app']['s_system_app']['fill'] = 'red'
G.add_edge('policyloader_app','sysprof')
G.edge['policyloader_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['policyloader_app']['sysprof']['fill'] = 'red'
G.add_edge('policyloader_app','sysprof')
G.edge['policyloader_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('policyloader_app','system_app')
G.edge['policyloader_app']['system_app']['write-read'] = '[open open][write read]'
G.edge['policyloader_app']['system_app']['fill'] = 'red'
G.add_edge('policyloader_app','system_server')
G.edge['policyloader_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['policyloader_app']['system_server']['fill'] = 'red'
G.add_edge('policyloader_app','vdc')
G.edge['policyloader_app']['vdc']['write-read'] = '[write read]'
G.edge['policyloader_app']['vdc']['fill'] = 'red'
G.add_edge('policyloader_app','zygote')
G.edge['policyloader_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['policyloader_app']['zygote']['fill'] = 'red'
G.add_edge('qseecomd','adbd')
G.edge['qseecomd']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qseecomd','dumpstate')
G.edge['qseecomd']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('qseecomd','ime_app')
G.edge['qseecomd']['ime_app']['write-read'] = '[open open]'
G.add_edge('qseecomd','itsonbs')
G.edge['qseecomd']['itsonbs']['write-read'] = '[open open]'
G.add_edge('qseecomd','knox_system_app')
G.edge['qseecomd']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('qseecomd','mediaserver')
G.edge['qseecomd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qseecomd','newAttr1')
G.edge['qseecomd']['newAttr1']['write-read'] = '[open open]'
G.add_edge('qseecomd','qseecomd')
G.edge['qseecomd']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('qseecomd','shell')
G.edge['qseecomd']['shell']['write-read'] = '[open open]'
G.add_edge('qseecomd','s_system_app')
G.edge['qseecomd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qseecomd','s_system_app')
G.edge['qseecomd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('qseecomd','sysprof')
G.edge['qseecomd']['sysprof']['write-read'] = '[open open]'
G.add_edge('qseecomd','system_app')
G.edge['qseecomd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qseecomd','adbd')
G.edge['qseecomd']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('qseecomd','dumpstate')
G.edge['qseecomd']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('qseecomd','installd')
G.edge['qseecomd']['installd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr]'
G.add_edge('qseecomd','itsonbs')
G.edge['qseecomd']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qseecomd','mediaserver')
G.edge['qseecomd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('qseecomd','qseecomd')
G.edge['qseecomd']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('qseecomd','shell')
G.edge['qseecomd']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qseecomd','sysprof')
G.edge['qseecomd']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qseecomd','adbd')
G.edge['qseecomd']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['qseecomd']['adbd']['fill'] = 'red'
G.add_edge('qseecomd','adbd')
G.edge['qseecomd']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('qseecomd','binderservicedomain')
G.edge['qseecomd']['binderservicedomain']['write-read'] = '[write read]'
G.edge['qseecomd']['binderservicedomain']['fill'] = 'red'
G.add_edge('qseecomd','dumpstate')
G.edge['qseecomd']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['qseecomd']['dumpstate']['fill'] = 'red'
G.add_edge('qseecomd','dumpstate')
G.edge['qseecomd']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('qseecomd','ime_app')
G.edge['qseecomd']['ime_app']['write-read'] = '[open open][write read]'
G.edge['qseecomd']['ime_app']['fill'] = 'red'
G.add_edge('qseecomd','itsonbs')
G.edge['qseecomd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qseecomd']['itsonbs']['fill'] = 'red'
G.add_edge('qseecomd','itsonbs')
G.edge['qseecomd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('qseecomd','knox_system_app')
G.edge['qseecomd']['knox_system_app']['write-read'] = '[open open][write read]'
G.edge['qseecomd']['knox_system_app']['fill'] = 'red'
G.add_edge('qseecomd','mediaserver')
G.edge['qseecomd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['qseecomd']['mediaserver']['fill'] = 'red'
G.add_edge('qseecomd','mediaserver')
G.edge['qseecomd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('qseecomd','newAttr1')
G.edge['qseecomd']['newAttr1']['write-read'] = '[open open][write read]'
G.edge['qseecomd']['newAttr1']['fill'] = 'red'
G.add_edge('qseecomd','newAttr1')
G.edge['qseecomd']['newAttr1']['write-read'] = '[open open][write read][write read]'
G.edge['qseecomd']['newAttr1']['fill'] = 'red'
G.add_edge('qseecomd','newAttr40')
G.edge['qseecomd']['newAttr40']['write-read'] = '[write read]'
G.edge['qseecomd']['newAttr40']['fill'] = 'red'
G.add_edge('qseecomd','qseecomd')
G.edge['qseecomd']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['qseecomd']['qseecomd']['fill'] = 'red'
G.add_edge('qseecomd','qseecomd')
G.edge['qseecomd']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('qseecomd','runas')
G.edge['qseecomd']['runas']['write-read'] = '[write read]'
G.edge['qseecomd']['runas']['fill'] = 'red'
G.add_edge('qseecomd','shell')
G.edge['qseecomd']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qseecomd']['shell']['fill'] = 'red'
G.add_edge('qseecomd','shell')
G.edge['qseecomd']['shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('qseecomd','s_system_app')
G.edge['qseecomd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read]'
G.edge['qseecomd']['s_system_app']['fill'] = 'red'
G.add_edge('qseecomd','s_system_app')
G.edge['qseecomd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read]'
G.add_edge('qseecomd','s_system_app')
G.edge['qseecomd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read][write read]'
G.edge['qseecomd']['s_system_app']['fill'] = 'red'
G.add_edge('qseecomd','sysprof')
G.edge['qseecomd']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qseecomd']['sysprof']['fill'] = 'red'
G.add_edge('qseecomd','sysprof')
G.edge['qseecomd']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('qseecomd','system_app')
G.edge['qseecomd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['qseecomd']['system_app']['fill'] = 'red'
G.add_edge('qseecomd','system_server')
G.edge['qseecomd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['qseecomd']['system_server']['fill'] = 'red'
G.add_edge('qseecomd','vdc')
G.edge['qseecomd']['vdc']['write-read'] = '[write read]'
G.edge['qseecomd']['vdc']['fill'] = 'red'
G.add_edge('qseecomd','zygote')
G.edge['qseecomd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['qseecomd']['zygote']['fill'] = 'red'
G.add_edge('radio','adbd')
G.edge['radio']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open]'
G.add_edge('radio','dumpstate')
G.edge['radio']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open]'
G.add_edge('radio','ime_app')
G.edge['radio']['ime_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][open open]'
G.add_edge('radio','itsonbs')
G.edge['radio']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('radio','knox_system_app')
G.edge['radio']['knox_system_app']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open]'
G.add_edge('radio','mediaserver')
G.edge['radio']['mediaserver']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open]'
G.add_edge('radio','newAttr1')
G.edge['radio']['newAttr1']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('radio','qseecomd')
G.edge['radio']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('radio','shell')
G.edge['radio']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open]'
G.add_edge('radio','s_system_app')
G.edge['radio']['s_system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('radio','s_system_app')
G.edge['radio']['s_system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('radio','sysprof')
G.edge['radio']['sysprof']['write-read'] = '[open open]'
G.add_edge('radio','system_app')
G.edge['radio']['system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][open open]'
G.add_edge('radio','adbd')
G.edge['radio']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr]'
G.add_edge('radio','dumpstate')
G.edge['radio']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr]'
G.add_edge('radio','installd')
G.edge['radio']['installd']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('radio','itsonbs')
G.edge['radio']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('radio','mediaserver')
G.edge['radio']['mediaserver']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][setattr getattr]'
G.add_edge('radio','qseecomd')
G.edge['radio']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('radio','shell')
G.edge['radio']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr]'
G.add_edge('radio','sysprof')
G.edge['radio']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','adbd')
G.edge['radio']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read]'
G.edge['radio']['adbd']['fill'] = 'red'
G.add_edge('radio','adbd')
G.edge['radio']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('radio','binderservicedomain')
G.edge['radio']['binderservicedomain']['write-read'] = '[write read][append read][write read]'
G.edge['radio']['binderservicedomain']['fill'] = 'red'
G.add_edge('radio','dumpstate')
G.edge['radio']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read]'
G.edge['radio']['dumpstate']['fill'] = 'red'
G.add_edge('radio','dumpstate')
G.edge['radio']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('radio','ime_app')
G.edge['radio']['ime_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['radio']['ime_app']['fill'] = 'red'
G.add_edge('radio','itsonbs')
G.edge['radio']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['radio']['itsonbs']['fill'] = 'red'
G.add_edge('radio','itsonbs')
G.edge['radio']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('radio','knox_system_app')
G.edge['radio']['knox_system_app']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read]'
G.edge['radio']['knox_system_app']['fill'] = 'red'
G.add_edge('radio','mediaserver')
G.edge['radio']['mediaserver']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read]'
G.edge['radio']['mediaserver']['fill'] = 'red'
G.add_edge('radio','mediaserver')
G.edge['radio']['mediaserver']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('radio','newAttr1')
G.edge['radio']['newAttr1']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['radio']['newAttr1']['fill'] = 'red'
G.add_edge('radio','newAttr1')
G.edge['radio']['newAttr1']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read]'
G.edge['radio']['newAttr1']['fill'] = 'red'
G.add_edge('radio','newAttr40')
G.edge['radio']['newAttr40']['write-read'] = '[write read]'
G.edge['radio']['newAttr40']['fill'] = 'red'
G.add_edge('radio','qseecomd')
G.edge['radio']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['radio']['qseecomd']['fill'] = 'red'
G.add_edge('radio','qseecomd')
G.edge['radio']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('radio','runas')
G.edge['radio']['runas']['write-read'] = '[write read][write read]'
G.edge['radio']['runas']['fill'] = 'red'
G.add_edge('radio','shell')
G.edge['radio']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read]'
G.edge['radio']['shell']['fill'] = 'red'
G.add_edge('radio','shell')
G.edge['radio']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('radio','s_system_app')
G.edge['radio']['s_system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][open open][setattr getattr][write read][append read][open open][open open][write read]'
G.edge['radio']['s_system_app']['fill'] = 'red'
G.add_edge('radio','s_system_app')
G.edge['radio']['s_system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][open open][setattr getattr][write read][append read][open open][open open][write read][append read]'
G.add_edge('radio','s_system_app')
G.edge['radio']['s_system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read]'
G.edge['radio']['s_system_app']['fill'] = 'red'
G.add_edge('radio','sysprof')
G.edge['radio']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['radio']['sysprof']['fill'] = 'red'
G.add_edge('radio','sysprof')
G.edge['radio']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('radio','system_app')
G.edge['radio']['system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['radio']['system_app']['fill'] = 'red'
G.add_edge('radio','system_server')
G.edge['radio']['system_server']['write-read'] = '[add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][write read]'
G.edge['radio']['system_server']['fill'] = 'red'
G.add_edge('radio','vdc')
G.edge['radio']['vdc']['write-read'] = '[write read]'
G.edge['radio']['vdc']['fill'] = 'red'
G.add_edge('radio','zygote')
G.edge['radio']['zygote']['write-read'] = '[open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['radio']['zygote']['fill'] = 'red'
G.add_edge('runas','adbd')
G.edge['runas']['adbd']['write-read'] = '[write read][append read][write read]'
G.edge['runas']['adbd']['fill'] = 'red'
G.add_edge('runas','adbd')
G.edge['runas']['adbd']['write-read'] = '[write read][append read][write read][append read]'
G.add_edge('runas','binderservicedomain')
G.edge['runas']['binderservicedomain']['write-read'] = '[write read][append read][write read]'
G.edge['runas']['binderservicedomain']['fill'] = 'red'
G.add_edge('runas','dumpstate')
G.edge['runas']['dumpstate']['write-read'] = '[write read][append read][write read]'
G.edge['runas']['dumpstate']['fill'] = 'red'
G.add_edge('runas','dumpstate')
G.edge['runas']['dumpstate']['write-read'] = '[write read][append read][write read][append read]'
G.add_edge('runas','ime_app')
G.edge['runas']['ime_app']['write-read'] = '[write read]'
G.edge['runas']['ime_app']['fill'] = 'red'
G.add_edge('runas','itsonbs')
G.edge['runas']['itsonbs']['write-read'] = '[write read]'
G.edge['runas']['itsonbs']['fill'] = 'red'
G.add_edge('runas','itsonbs')
G.edge['runas']['itsonbs']['write-read'] = '[write read][append read]'
G.add_edge('runas','knox_system_app')
G.edge['runas']['knox_system_app']['write-read'] = '[write read]'
G.edge['runas']['knox_system_app']['fill'] = 'red'
G.add_edge('runas','mediaserver')
G.edge['runas']['mediaserver']['write-read'] = '[add_name search][remove_name search][write read][append read][write read]'
G.edge['runas']['mediaserver']['fill'] = 'red'
G.add_edge('runas','mediaserver')
G.edge['runas']['mediaserver']['write-read'] = '[add_name search][remove_name search][write read][append read][write read][append read]'
G.add_edge('runas','newAttr1')
G.edge['runas']['newAttr1']['write-read'] = '[setattr getattr][add_name search][remove_name search][write read]'
G.edge['runas']['newAttr1']['fill'] = 'red'
G.add_edge('runas','newAttr1')
G.edge['runas']['newAttr1']['write-read'] = '[setattr getattr][add_name search][remove_name search][write read][write read]'
G.edge['runas']['newAttr1']['fill'] = 'red'
G.add_edge('runas','newAttr40')
G.edge['runas']['newAttr40']['write-read'] = '[write read]'
G.edge['runas']['newAttr40']['fill'] = 'red'
G.add_edge('runas','qseecomd')
G.edge['runas']['qseecomd']['write-read'] = '[write read]'
G.edge['runas']['qseecomd']['fill'] = 'red'
G.add_edge('runas','qseecomd')
G.edge['runas']['qseecomd']['write-read'] = '[write read][append read]'
G.add_edge('runas','runas')
G.edge['runas']['runas']['write-read'] = '[write read][open open][write read][append read][write read][write read]'
G.edge['runas']['runas']['fill'] = 'red'
G.add_edge('runas','shell')
G.edge['runas']['shell']['write-read'] = '[write read][append read][write read]'
G.edge['runas']['shell']['fill'] = 'red'
G.add_edge('runas','shell')
G.edge['runas']['shell']['write-read'] = '[write read][append read][write read][append read]'
G.add_edge('runas','s_system_app')
G.edge['runas']['s_system_app']['write-read'] = '[write read]'
G.edge['runas']['s_system_app']['fill'] = 'red'
G.add_edge('runas','s_system_app')
G.edge['runas']['s_system_app']['write-read'] = '[write read][append read]'
G.add_edge('runas','s_system_app')
G.edge['runas']['s_system_app']['write-read'] = '[write read][append read][write read]'
G.edge['runas']['s_system_app']['fill'] = 'red'
G.add_edge('runas','sysprof')
G.edge['runas']['sysprof']['write-read'] = '[write read]'
G.edge['runas']['sysprof']['fill'] = 'red'
G.add_edge('runas','sysprof')
G.edge['runas']['sysprof']['write-read'] = '[write read][append read]'
G.add_edge('runas','system_app')
G.edge['runas']['system_app']['write-read'] = '[write read]'
G.edge['runas']['system_app']['fill'] = 'red'
G.add_edge('runas','system_server')
G.edge['runas']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][setattr getattr][add_name search][remove_name search][write read][append read][write read]'
G.edge['runas']['system_server']['fill'] = 'red'
G.add_edge('runas','vdc')
G.edge['runas']['vdc']['write-read'] = '[write read]'
G.edge['runas']['vdc']['fill'] = 'red'
G.add_edge('runas','zygote')
G.edge['runas']['zygote']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][write read]'
G.edge['runas']['zygote']['fill'] = 'red'
G.add_edge('shell','adbd')
G.edge['shell']['adbd']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('shell','dumpstate')
G.edge['shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('shell','ime_app')
G.edge['shell']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('shell','itsonbs')
G.edge['shell']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('shell','knox_system_app')
G.edge['shell']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('shell','mediaserver')
G.edge['shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('shell','newAttr1')
G.edge['shell']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][open open]'
G.add_edge('shell','qseecomd')
G.edge['shell']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('shell','shell')
G.edge['shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('shell','s_system_app')
G.edge['shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('shell','s_system_app')
G.edge['shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('shell','sysprof')
G.edge['shell']['sysprof']['write-read'] = '[open open]'
G.add_edge('shell','system_app')
G.edge['shell']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('shell','adbd')
G.edge['shell']['adbd']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('shell','dumpstate')
G.edge['shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('shell','installd')
G.edge['shell']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('shell','itsonbs')
G.edge['shell']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('shell','mediaserver')
G.edge['shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('shell','qseecomd')
G.edge['shell']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('shell','shell')
G.edge['shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('shell','sysprof')
G.edge['shell']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','adbd')
G.edge['shell']['adbd']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['shell']['adbd']['fill'] = 'red'
G.add_edge('shell','adbd')
G.edge['shell']['adbd']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('shell','binderservicedomain')
G.edge['shell']['binderservicedomain']['write-read'] = '[open open][write read][append read][write read]'
G.edge['shell']['binderservicedomain']['fill'] = 'red'
G.add_edge('shell','dumpstate')
G.edge['shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['shell']['dumpstate']['fill'] = 'red'
G.add_edge('shell','dumpstate')
G.edge['shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('shell','ime_app')
G.edge['shell']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['shell']['ime_app']['fill'] = 'red'
G.add_edge('shell','itsonbs')
G.edge['shell']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['shell']['itsonbs']['fill'] = 'red'
G.add_edge('shell','itsonbs')
G.edge['shell']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('shell','knox_system_app')
G.edge['shell']['knox_system_app']['write-read'] = '[open open][write read]'
G.edge['shell']['knox_system_app']['fill'] = 'red'
G.add_edge('shell','mediaserver')
G.edge['shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['shell']['mediaserver']['fill'] = 'red'
G.add_edge('shell','mediaserver')
G.edge['shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('shell','newAttr1')
G.edge['shell']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][open open][write read]'
G.edge['shell']['newAttr1']['fill'] = 'red'
G.add_edge('shell','newAttr1')
G.edge['shell']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][open open][write read][write read]'
G.edge['shell']['newAttr1']['fill'] = 'red'
G.add_edge('shell','newAttr40')
G.edge['shell']['newAttr40']['write-read'] = '[write read]'
G.edge['shell']['newAttr40']['fill'] = 'red'
G.add_edge('shell','qseecomd')
G.edge['shell']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['shell']['qseecomd']['fill'] = 'red'
G.add_edge('shell','qseecomd')
G.edge['shell']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('shell','runas')
G.edge['shell']['runas']['write-read'] = '[write read][write read]'
G.edge['shell']['runas']['fill'] = 'red'
G.add_edge('shell','shell')
G.edge['shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['shell']['shell']['fill'] = 'red'
G.add_edge('shell','shell')
G.edge['shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('shell','s_system_app')
G.edge['shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read]'
G.edge['shell']['s_system_app']['fill'] = 'red'
G.add_edge('shell','s_system_app')
G.edge['shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read]'
G.add_edge('shell','s_system_app')
G.edge['shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read][write read]'
G.edge['shell']['s_system_app']['fill'] = 'red'
G.add_edge('shell','sysprof')
G.edge['shell']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['sysprof']['fill'] = 'red'
G.add_edge('shell','sysprof')
G.edge['shell']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('shell','system_app')
G.edge['shell']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['shell']['system_app']['fill'] = 'red'
G.add_edge('shell','system_server')
G.edge['shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['shell']['system_server']['fill'] = 'red'
G.add_edge('shell','vdc')
G.edge['shell']['vdc']['write-read'] = '[write read]'
G.edge['shell']['vdc']['fill'] = 'red'
G.add_edge('shell','zygote')
G.edge['shell']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][add_name search][remove_name search][write read]'
G.edge['shell']['zygote']['fill'] = 'red'
G.add_edge('shell','adbd')
G.edge['shell']['adbd']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('shell','dumpstate')
G.edge['shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('shell','ime_app')
G.edge['shell']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open]'
G.add_edge('shell','itsonbs')
G.edge['shell']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('shell','knox_system_app')
G.edge['shell']['knox_system_app']['write-read'] = '[open open][write read][open open]'
G.add_edge('shell','mediaserver')
G.edge['shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('shell','newAttr1')
G.edge['shell']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][open open][write read][write read][open open]'
G.add_edge('shell','qseecomd')
G.edge['shell']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('shell','shell')
G.edge['shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('shell','s_system_app')
G.edge['shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read][write read][open open]'
G.add_edge('shell','s_system_app')
G.edge['shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read][write read][open open][open open]'
G.add_edge('shell','sysprof')
G.edge['shell']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('shell','system_app')
G.edge['shell']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open]'
G.add_edge('shell','adbd')
G.edge['shell']['adbd']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('shell','dumpstate')
G.edge['shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('shell','installd')
G.edge['shell']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr]'
G.add_edge('shell','itsonbs')
G.edge['shell']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('shell','mediaserver')
G.edge['shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('shell','qseecomd')
G.edge['shell']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('shell','shell')
G.edge['shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('shell','sysprof')
G.edge['shell']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('shell','adbd')
G.edge['shell']['adbd']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['shell']['adbd']['fill'] = 'red'
G.add_edge('shell','adbd')
G.edge['shell']['adbd']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('shell','binderservicedomain')
G.edge['shell']['binderservicedomain']['write-read'] = '[open open][write read][append read][write read][write read]'
G.edge['shell']['binderservicedomain']['fill'] = 'red'
G.add_edge('shell','dumpstate')
G.edge['shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['shell']['dumpstate']['fill'] = 'red'
G.add_edge('shell','dumpstate')
G.edge['shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('shell','ime_app')
G.edge['shell']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][write read]'
G.edge['shell']['ime_app']['fill'] = 'red'
G.add_edge('shell','itsonbs')
G.edge['shell']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['shell']['itsonbs']['fill'] = 'red'
G.add_edge('shell','itsonbs')
G.edge['shell']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('shell','knox_system_app')
G.edge['shell']['knox_system_app']['write-read'] = '[open open][write read][open open][write read]'
G.edge['shell']['knox_system_app']['fill'] = 'red'
G.add_edge('shell','mediaserver')
G.edge['shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['shell']['mediaserver']['fill'] = 'red'
G.add_edge('shell','mediaserver')
G.edge['shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('shell','newAttr1')
G.edge['shell']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][open open][write read][write read][open open][write read]'
G.edge['shell']['newAttr1']['fill'] = 'red'
G.add_edge('shell','newAttr1')
G.edge['shell']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][open open][write read][write read][open open][write read][write read]'
G.edge['shell']['newAttr1']['fill'] = 'red'
G.add_edge('shell','newAttr40')
G.edge['shell']['newAttr40']['write-read'] = '[write read][write read]'
G.edge['shell']['newAttr40']['fill'] = 'red'
G.add_edge('shell','qseecomd')
G.edge['shell']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['shell']['qseecomd']['fill'] = 'red'
G.add_edge('shell','qseecomd')
G.edge['shell']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('shell','runas')
G.edge['shell']['runas']['write-read'] = '[write read][write read][write read]'
G.edge['shell']['runas']['fill'] = 'red'
G.add_edge('shell','shell')
G.edge['shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['shell']['shell']['fill'] = 'red'
G.add_edge('shell','shell')
G.edge['shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('shell','s_system_app')
G.edge['shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read][write read][open open][open open][write read]'
G.edge['shell']['s_system_app']['fill'] = 'red'
G.add_edge('shell','s_system_app')
G.edge['shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read][write read][open open][open open][write read][append read]'
G.add_edge('shell','s_system_app')
G.edge['shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read][write read][open open][open open][write read][append read][write read]'
G.edge['shell']['s_system_app']['fill'] = 'red'
G.add_edge('shell','sysprof')
G.edge['shell']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['shell']['sysprof']['fill'] = 'red'
G.add_edge('shell','sysprof')
G.edge['shell']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('shell','system_app')
G.edge['shell']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][write read]'
G.edge['shell']['system_app']['fill'] = 'red'
G.add_edge('shell','system_server')
G.edge['shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][write read]'
G.edge['shell']['system_server']['fill'] = 'red'
G.add_edge('shell','vdc')
G.edge['shell']['vdc']['write-read'] = '[write read][write read]'
G.edge['shell']['vdc']['fill'] = 'red'
G.add_edge('shell','zygote')
G.edge['shell']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][add_name search][remove_name search][write read][write read]'
G.edge['shell']['zygote']['fill'] = 'red'
G.add_edge('s_platform_app','adbd')
G.edge['s_platform_app']['adbd']['write-read'] = '[open open]'
G.add_edge('s_platform_app','dumpstate')
G.edge['s_platform_app']['dumpstate']['write-read'] = '[open open]'
G.add_edge('s_platform_app','ime_app')
G.edge['s_platform_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_platform_app','itsonbs')
G.edge['s_platform_app']['itsonbs']['write-read'] = '[open open]'
G.add_edge('s_platform_app','knox_system_app')
G.edge['s_platform_app']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('s_platform_app','mediaserver')
G.edge['s_platform_app']['mediaserver']['write-read'] = '[open open]'
G.add_edge('s_platform_app','newAttr1')
G.edge['s_platform_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_platform_app','qseecomd')
G.edge['s_platform_app']['qseecomd']['write-read'] = '[open open]'
G.add_edge('s_platform_app','shell')
G.edge['s_platform_app']['shell']['write-read'] = '[open open]'
G.add_edge('s_platform_app','s_system_app')
G.edge['s_platform_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open]'
G.add_edge('s_platform_app','s_system_app')
G.edge['s_platform_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][open open]'
G.add_edge('s_platform_app','sysprof')
G.edge['s_platform_app']['sysprof']['write-read'] = '[open open]'
G.add_edge('s_platform_app','system_app')
G.edge['s_platform_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open]'
G.add_edge('s_platform_app','adbd')
G.edge['s_platform_app']['adbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_platform_app','dumpstate')
G.edge['s_platform_app']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_platform_app','installd')
G.edge['s_platform_app']['installd']['write-read'] = '[setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr]'
G.add_edge('s_platform_app','itsonbs')
G.edge['s_platform_app']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_platform_app','mediaserver')
G.edge['s_platform_app']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_platform_app','qseecomd')
G.edge['s_platform_app']['qseecomd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_platform_app','shell')
G.edge['s_platform_app']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_platform_app','sysprof')
G.edge['s_platform_app']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_platform_app','adbd')
G.edge['s_platform_app']['adbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_platform_app']['adbd']['fill'] = 'red'
G.add_edge('s_platform_app','adbd')
G.edge['s_platform_app']['adbd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_platform_app','binderservicedomain')
G.edge['s_platform_app']['binderservicedomain']['write-read'] = '[write read]'
G.edge['s_platform_app']['binderservicedomain']['fill'] = 'red'
G.add_edge('s_platform_app','dumpstate')
G.edge['s_platform_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_platform_app']['dumpstate']['fill'] = 'red'
G.add_edge('s_platform_app','dumpstate')
G.edge['s_platform_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_platform_app','ime_app')
G.edge['s_platform_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['s_platform_app']['ime_app']['fill'] = 'red'
G.add_edge('s_platform_app','itsonbs')
G.edge['s_platform_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_platform_app']['itsonbs']['fill'] = 'red'
G.add_edge('s_platform_app','itsonbs')
G.edge['s_platform_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_platform_app','knox_system_app')
G.edge['s_platform_app']['knox_system_app']['write-read'] = '[open open][write read]'
G.edge['s_platform_app']['knox_system_app']['fill'] = 'red'
G.add_edge('s_platform_app','mediaserver')
G.edge['s_platform_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_platform_app']['mediaserver']['fill'] = 'red'
G.add_edge('s_platform_app','mediaserver')
G.edge['s_platform_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_platform_app','newAttr1')
G.edge['s_platform_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['s_platform_app']['newAttr1']['fill'] = 'red'
G.add_edge('s_platform_app','newAttr1')
G.edge['s_platform_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][write read]'
G.edge['s_platform_app']['newAttr1']['fill'] = 'red'
G.add_edge('s_platform_app','newAttr40')
G.edge['s_platform_app']['newAttr40']['write-read'] = '[write read]'
G.edge['s_platform_app']['newAttr40']['fill'] = 'red'
G.add_edge('s_platform_app','qseecomd')
G.edge['s_platform_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_platform_app']['qseecomd']['fill'] = 'red'
G.add_edge('s_platform_app','qseecomd')
G.edge['s_platform_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_platform_app','runas')
G.edge['s_platform_app']['runas']['write-read'] = '[write read]'
G.edge['s_platform_app']['runas']['fill'] = 'red'
G.add_edge('s_platform_app','shell')
G.edge['s_platform_app']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_platform_app']['shell']['fill'] = 'red'
G.add_edge('s_platform_app','shell')
G.edge['s_platform_app']['shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_platform_app','s_system_app')
G.edge['s_platform_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][open open][write read]'
G.edge['s_platform_app']['s_system_app']['fill'] = 'red'
G.add_edge('s_platform_app','s_system_app')
G.edge['s_platform_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][open open][write read][append read]'
G.add_edge('s_platform_app','s_system_app')
G.edge['s_platform_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][open open][write read][append read][write read]'
G.edge['s_platform_app']['s_system_app']['fill'] = 'red'
G.add_edge('s_platform_app','sysprof')
G.edge['s_platform_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_platform_app']['sysprof']['fill'] = 'red'
G.add_edge('s_platform_app','sysprof')
G.edge['s_platform_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_platform_app','system_app')
G.edge['s_platform_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][write read]'
G.edge['s_platform_app']['system_app']['fill'] = 'red'
G.add_edge('s_platform_app','system_server')
G.edge['s_platform_app']['system_server']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['s_platform_app']['system_server']['fill'] = 'red'
G.add_edge('s_platform_app','vdc')
G.edge['s_platform_app']['vdc']['write-read'] = '[write read]'
G.edge['s_platform_app']['vdc']['fill'] = 'red'
G.add_edge('s_platform_app','zygote')
G.edge['s_platform_app']['zygote']['write-read'] = '[write read]'
G.edge['s_platform_app']['zygote']['fill'] = 'red'
G.add_edge('sysprof','adbd')
G.edge['sysprof']['adbd']['write-read'] = '[open open]'
G.add_edge('sysprof','dumpstate')
G.edge['sysprof']['dumpstate']['write-read'] = '[open open]'
G.add_edge('sysprof','ime_app')
G.edge['sysprof']['ime_app']['write-read'] = '[open open]'
G.add_edge('sysprof','itsonbs')
G.edge['sysprof']['itsonbs']['write-read'] = '[open open]'
G.add_edge('sysprof','knox_system_app')
G.edge['sysprof']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('sysprof','mediaserver')
G.edge['sysprof']['mediaserver']['write-read'] = '[open open]'
G.add_edge('sysprof','newAttr1')
G.edge['sysprof']['newAttr1']['write-read'] = '[open open]'
G.add_edge('sysprof','qseecomd')
G.edge['sysprof']['qseecomd']['write-read'] = '[open open]'
G.add_edge('sysprof','shell')
G.edge['sysprof']['shell']['write-read'] = '[open open]'
G.add_edge('sysprof','s_system_app')
G.edge['sysprof']['s_system_app']['write-read'] = '[open open]'
G.add_edge('sysprof','s_system_app')
G.edge['sysprof']['s_system_app']['write-read'] = '[open open][open open]'
G.add_edge('sysprof','sysprof')
G.edge['sysprof']['sysprof']['write-read'] = '[open open]'
G.add_edge('sysprof','system_app')
G.edge['sysprof']['system_app']['write-read'] = '[open open]'
G.add_edge('sysprof','adbd')
G.edge['sysprof']['adbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sysprof','dumpstate')
G.edge['sysprof']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sysprof','installd')
G.edge['sysprof']['installd']['write-read'] = '[setattr getattr]'
G.add_edge('sysprof','itsonbs')
G.edge['sysprof']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sysprof','mediaserver')
G.edge['sysprof']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sysprof','qseecomd')
G.edge['sysprof']['qseecomd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sysprof','shell')
G.edge['sysprof']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sysprof','sysprof')
G.edge['sysprof']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sysprof','adbd')
G.edge['sysprof']['adbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sysprof']['adbd']['fill'] = 'red'
G.add_edge('sysprof','adbd')
G.edge['sysprof']['adbd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sysprof','binderservicedomain')
G.edge['sysprof']['binderservicedomain']['write-read'] = '[write read]'
G.edge['sysprof']['binderservicedomain']['fill'] = 'red'
G.add_edge('sysprof','dumpstate')
G.edge['sysprof']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sysprof']['dumpstate']['fill'] = 'red'
G.add_edge('sysprof','dumpstate')
G.edge['sysprof']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sysprof','ime_app')
G.edge['sysprof']['ime_app']['write-read'] = '[open open][write read]'
G.edge['sysprof']['ime_app']['fill'] = 'red'
G.add_edge('sysprof','itsonbs')
G.edge['sysprof']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sysprof']['itsonbs']['fill'] = 'red'
G.add_edge('sysprof','itsonbs')
G.edge['sysprof']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sysprof','knox_system_app')
G.edge['sysprof']['knox_system_app']['write-read'] = '[open open][write read]'
G.edge['sysprof']['knox_system_app']['fill'] = 'red'
G.add_edge('sysprof','mediaserver')
G.edge['sysprof']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sysprof']['mediaserver']['fill'] = 'red'
G.add_edge('sysprof','mediaserver')
G.edge['sysprof']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sysprof','newAttr1')
G.edge['sysprof']['newAttr1']['write-read'] = '[open open][write read]'
G.edge['sysprof']['newAttr1']['fill'] = 'red'
G.add_edge('sysprof','newAttr1')
G.edge['sysprof']['newAttr1']['write-read'] = '[open open][write read][write read]'
G.edge['sysprof']['newAttr1']['fill'] = 'red'
G.add_edge('sysprof','newAttr40')
G.edge['sysprof']['newAttr40']['write-read'] = '[write read]'
G.edge['sysprof']['newAttr40']['fill'] = 'red'
G.add_edge('sysprof','qseecomd')
G.edge['sysprof']['qseecomd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sysprof']['qseecomd']['fill'] = 'red'
G.add_edge('sysprof','qseecomd')
G.edge['sysprof']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sysprof','runas')
G.edge['sysprof']['runas']['write-read'] = '[write read]'
G.edge['sysprof']['runas']['fill'] = 'red'
G.add_edge('sysprof','shell')
G.edge['sysprof']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sysprof']['shell']['fill'] = 'red'
G.add_edge('sysprof','shell')
G.edge['sysprof']['shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sysprof','s_system_app')
G.edge['sysprof']['s_system_app']['write-read'] = '[open open][open open][write read]'
G.edge['sysprof']['s_system_app']['fill'] = 'red'
G.add_edge('sysprof','s_system_app')
G.edge['sysprof']['s_system_app']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('sysprof','s_system_app')
G.edge['sysprof']['s_system_app']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['sysprof']['s_system_app']['fill'] = 'red'
G.add_edge('sysprof','sysprof')
G.edge['sysprof']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sysprof']['sysprof']['fill'] = 'red'
G.add_edge('sysprof','sysprof')
G.edge['sysprof']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sysprof','system_app')
G.edge['sysprof']['system_app']['write-read'] = '[open open][write read]'
G.edge['sysprof']['system_app']['fill'] = 'red'
G.add_edge('sysprof','system_server')
G.edge['sysprof']['system_server']['write-read'] = '[write read]'
G.edge['sysprof']['system_server']['fill'] = 'red'
G.add_edge('sysprof','vdc')
G.edge['sysprof']['vdc']['write-read'] = '[write read]'
G.edge['sysprof']['vdc']['fill'] = 'red'
G.add_edge('sysprof','zygote')
G.edge['sysprof']['zygote']['write-read'] = '[write read]'
G.edge['sysprof']['zygote']['fill'] = 'red'
G.add_edge('system_server','adbd')
G.edge['system_server']['adbd']['write-read'] = '[write read][add_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr]'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][setattr getattr][open open][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][relabelto relabelfrom][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][relabelto relabelfrom][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('system_server','itsonbs')
G.edge['system_server']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setattr getattr]'
G.add_edge('system_server','qseecomd')
G.edge['system_server']['qseecomd']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('system_server','shell')
G.edge['system_server']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr]'
G.add_edge('system_server','sysprof')
G.edge['system_server']['sysprof']['write-read'] = '[setattr getattr]'
G.add_edge('system_server','adbd')
G.edge['system_server']['adbd']['write-read'] = '[write read][add_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read]'
G.edge['system_server']['adbd']['fill'] = 'red'
G.add_edge('system_server','adbd')
G.edge['system_server']['adbd']['write-read'] = '[write read][add_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read]'
G.add_edge('system_server','binderservicedomain')
G.edge['system_server']['binderservicedomain']['write-read'] = '[open open][write read][append read][write read]'
G.edge['system_server']['binderservicedomain']['fill'] = 'red'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read]'
G.edge['system_server']['dumpstate']['fill'] = 'red'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read]'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][add_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['system_server']['ime_app']['fill'] = 'red'
G.add_edge('system_server','itsonbs')
G.edge['system_server']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['system_server']['itsonbs']['fill'] = 'red'
G.add_edge('system_server','itsonbs')
G.edge['system_server']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read]'
G.add_edge('system_server','knox_system_app')
G.edge['system_server']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['system_server']['knox_system_app']['fill'] = 'red'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setattr getattr][write read]'
G.edge['system_server']['mediaserver']['fill'] = 'red'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read]'
G.add_edge('system_server','newAttr1')
G.edge['system_server']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['system_server']['newAttr1']['fill'] = 'red'
G.add_edge('system_server','newAttr1')
G.edge['system_server']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['system_server']['newAttr1']['fill'] = 'red'
G.add_edge('system_server','newAttr40')
G.edge['system_server']['newAttr40']['write-read'] = '[write read]'
G.edge['system_server']['newAttr40']['fill'] = 'red'
G.add_edge('system_server','qseecomd')
G.edge['system_server']['qseecomd']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['system_server']['qseecomd']['fill'] = 'red'
G.add_edge('system_server','qseecomd')
G.edge['system_server']['qseecomd']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read]'
G.add_edge('system_server','runas')
G.edge['system_server']['runas']['write-read'] = '[open open][write read][append read][write read][write read]'
G.edge['system_server']['runas']['fill'] = 'red'
G.add_edge('system_server','shell')
G.edge['system_server']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read]'
G.edge['system_server']['shell']['fill'] = 'red'
G.add_edge('system_server','shell')
G.edge['system_server']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['system_server']['s_system_app']['fill'] = 'red'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][append read][write read]'
G.edge['system_server']['s_system_app']['fill'] = 'red'
G.add_edge('system_server','sysprof')
G.edge['system_server']['sysprof']['write-read'] = '[setattr getattr][write read]'
G.edge['system_server']['sysprof']['fill'] = 'red'
G.add_edge('system_server','sysprof')
G.edge['system_server']['sysprof']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['system_server']['system_app']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','vdc')
G.edge['system_server']['vdc']['write-read'] = '[write read][write read]'
G.edge['system_server']['vdc']['fill'] = 'red'
G.add_edge('system_server','zygote')
G.edge['system_server']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['system_server']['zygote']['fill'] = 'red'
G.add_edge('trustonicpartner_app','adbd')
G.edge['trustonicpartner_app']['adbd']['write-read'] = '[write read][open open]'
G.add_edge('trustonicpartner_app','dumpstate')
G.edge['trustonicpartner_app']['dumpstate']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','ime_app')
G.edge['trustonicpartner_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('trustonicpartner_app','itsonbs')
G.edge['trustonicpartner_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('trustonicpartner_app','knox_system_app')
G.edge['trustonicpartner_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('trustonicpartner_app','mediaserver')
G.edge['trustonicpartner_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('trustonicpartner_app','newAttr1')
G.edge['trustonicpartner_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('trustonicpartner_app','qseecomd')
G.edge['trustonicpartner_app']['qseecomd']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','shell')
G.edge['trustonicpartner_app']['shell']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','s_system_app')
G.edge['trustonicpartner_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('trustonicpartner_app','s_system_app')
G.edge['trustonicpartner_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('trustonicpartner_app','sysprof')
G.edge['trustonicpartner_app']['sysprof']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','system_app')
G.edge['trustonicpartner_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('trustonicpartner_app','adbd')
G.edge['trustonicpartner_app']['adbd']['write-read'] = '[write read][open open][setattr getattr]'
G.add_edge('trustonicpartner_app','dumpstate')
G.edge['trustonicpartner_app']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','installd')
G.edge['trustonicpartner_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('trustonicpartner_app','itsonbs')
G.edge['trustonicpartner_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('trustonicpartner_app','mediaserver')
G.edge['trustonicpartner_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('trustonicpartner_app','qseecomd')
G.edge['trustonicpartner_app']['qseecomd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','shell')
G.edge['trustonicpartner_app']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','sysprof')
G.edge['trustonicpartner_app']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','adbd')
G.edge['trustonicpartner_app']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['adbd']['fill'] = 'red'
G.add_edge('trustonicpartner_app','adbd')
G.edge['trustonicpartner_app']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','binderservicedomain')
G.edge['trustonicpartner_app']['binderservicedomain']['write-read'] = '[write read]'
G.edge['trustonicpartner_app']['binderservicedomain']['fill'] = 'red'
G.add_edge('trustonicpartner_app','dumpstate')
G.edge['trustonicpartner_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['dumpstate']['fill'] = 'red'
G.add_edge('trustonicpartner_app','dumpstate')
G.edge['trustonicpartner_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','ime_app')
G.edge['trustonicpartner_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['trustonicpartner_app']['ime_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','itsonbs')
G.edge['trustonicpartner_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['itsonbs']['fill'] = 'red'
G.add_edge('trustonicpartner_app','itsonbs')
G.edge['trustonicpartner_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','knox_system_app')
G.edge['trustonicpartner_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['trustonicpartner_app']['knox_system_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','mediaserver')
G.edge['trustonicpartner_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['mediaserver']['fill'] = 'red'
G.add_edge('trustonicpartner_app','mediaserver')
G.edge['trustonicpartner_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','newAttr1')
G.edge['trustonicpartner_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['trustonicpartner_app']['newAttr1']['fill'] = 'red'
G.add_edge('trustonicpartner_app','newAttr1')
G.edge['trustonicpartner_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read]'
G.edge['trustonicpartner_app']['newAttr1']['fill'] = 'red'
G.add_edge('trustonicpartner_app','newAttr40')
G.edge['trustonicpartner_app']['newAttr40']['write-read'] = '[write read]'
G.edge['trustonicpartner_app']['newAttr40']['fill'] = 'red'
G.add_edge('trustonicpartner_app','qseecomd')
G.edge['trustonicpartner_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['qseecomd']['fill'] = 'red'
G.add_edge('trustonicpartner_app','qseecomd')
G.edge['trustonicpartner_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','runas')
G.edge['trustonicpartner_app']['runas']['write-read'] = '[write read]'
G.edge['trustonicpartner_app']['runas']['fill'] = 'red'
G.add_edge('trustonicpartner_app','shell')
G.edge['trustonicpartner_app']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['shell']['fill'] = 'red'
G.add_edge('trustonicpartner_app','shell')
G.edge['trustonicpartner_app']['shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','s_system_app')
G.edge['trustonicpartner_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read]'
G.edge['trustonicpartner_app']['s_system_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','s_system_app')
G.edge['trustonicpartner_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read][append read]'
G.add_edge('trustonicpartner_app','s_system_app')
G.edge['trustonicpartner_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read]'
G.edge['trustonicpartner_app']['s_system_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','sysprof')
G.edge['trustonicpartner_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['sysprof']['fill'] = 'red'
G.add_edge('trustonicpartner_app','sysprof')
G.edge['trustonicpartner_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','system_app')
G.edge['trustonicpartner_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['trustonicpartner_app']['system_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','system_server')
G.edge['trustonicpartner_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['trustonicpartner_app']['system_server']['fill'] = 'red'
G.add_edge('trustonicpartner_app','vdc')
G.edge['trustonicpartner_app']['vdc']['write-read'] = '[write read]'
G.edge['trustonicpartner_app']['vdc']['fill'] = 'red'
G.add_edge('trustonicpartner_app','zygote')
G.edge['trustonicpartner_app']['zygote']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['trustonicpartner_app']['zygote']['fill'] = 'red'
G.add_edge('umcagent_app','adbd')
G.edge['umcagent_app']['adbd']['write-read'] = '[write read][open open]'
G.add_edge('umcagent_app','dumpstate')
G.edge['umcagent_app']['dumpstate']['write-read'] = '[open open]'
G.add_edge('umcagent_app','ime_app')
G.edge['umcagent_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('umcagent_app','itsonbs')
G.edge['umcagent_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('umcagent_app','knox_system_app')
G.edge['umcagent_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('umcagent_app','mediaserver')
G.edge['umcagent_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('umcagent_app','newAttr1')
G.edge['umcagent_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('umcagent_app','qseecomd')
G.edge['umcagent_app']['qseecomd']['write-read'] = '[open open]'
G.add_edge('umcagent_app','shell')
G.edge['umcagent_app']['shell']['write-read'] = '[open open]'
G.add_edge('umcagent_app','s_system_app')
G.edge['umcagent_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('umcagent_app','s_system_app')
G.edge['umcagent_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('umcagent_app','sysprof')
G.edge['umcagent_app']['sysprof']['write-read'] = '[open open]'
G.add_edge('umcagent_app','system_app')
G.edge['umcagent_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('umcagent_app','adbd')
G.edge['umcagent_app']['adbd']['write-read'] = '[write read][open open][setattr getattr]'
G.add_edge('umcagent_app','dumpstate')
G.edge['umcagent_app']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','installd')
G.edge['umcagent_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('umcagent_app','itsonbs')
G.edge['umcagent_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('umcagent_app','mediaserver')
G.edge['umcagent_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('umcagent_app','qseecomd')
G.edge['umcagent_app']['qseecomd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','shell')
G.edge['umcagent_app']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','sysprof')
G.edge['umcagent_app']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','adbd')
G.edge['umcagent_app']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read]'
G.edge['umcagent_app']['adbd']['fill'] = 'red'
G.add_edge('umcagent_app','adbd')
G.edge['umcagent_app']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','binderservicedomain')
G.edge['umcagent_app']['binderservicedomain']['write-read'] = '[write read]'
G.edge['umcagent_app']['binderservicedomain']['fill'] = 'red'
G.add_edge('umcagent_app','dumpstate')
G.edge['umcagent_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['umcagent_app']['dumpstate']['fill'] = 'red'
G.add_edge('umcagent_app','dumpstate')
G.edge['umcagent_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','ime_app')
G.edge['umcagent_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['umcagent_app']['ime_app']['fill'] = 'red'
G.add_edge('umcagent_app','itsonbs')
G.edge['umcagent_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['umcagent_app']['itsonbs']['fill'] = 'red'
G.add_edge('umcagent_app','itsonbs')
G.edge['umcagent_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','knox_system_app')
G.edge['umcagent_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['umcagent_app']['knox_system_app']['fill'] = 'red'
G.add_edge('umcagent_app','mediaserver')
G.edge['umcagent_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['umcagent_app']['mediaserver']['fill'] = 'red'
G.add_edge('umcagent_app','mediaserver')
G.edge['umcagent_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','newAttr1')
G.edge['umcagent_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['umcagent_app']['newAttr1']['fill'] = 'red'
G.add_edge('umcagent_app','newAttr1')
G.edge['umcagent_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read]'
G.edge['umcagent_app']['newAttr1']['fill'] = 'red'
G.add_edge('umcagent_app','newAttr40')
G.edge['umcagent_app']['newAttr40']['write-read'] = '[write read]'
G.edge['umcagent_app']['newAttr40']['fill'] = 'red'
G.add_edge('umcagent_app','qseecomd')
G.edge['umcagent_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['umcagent_app']['qseecomd']['fill'] = 'red'
G.add_edge('umcagent_app','qseecomd')
G.edge['umcagent_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','runas')
G.edge['umcagent_app']['runas']['write-read'] = '[write read]'
G.edge['umcagent_app']['runas']['fill'] = 'red'
G.add_edge('umcagent_app','shell')
G.edge['umcagent_app']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['umcagent_app']['shell']['fill'] = 'red'
G.add_edge('umcagent_app','shell')
G.edge['umcagent_app']['shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','s_system_app')
G.edge['umcagent_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read]'
G.edge['umcagent_app']['s_system_app']['fill'] = 'red'
G.add_edge('umcagent_app','s_system_app')
G.edge['umcagent_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read][append read]'
G.add_edge('umcagent_app','s_system_app')
G.edge['umcagent_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read]'
G.edge['umcagent_app']['s_system_app']['fill'] = 'red'
G.add_edge('umcagent_app','sysprof')
G.edge['umcagent_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['umcagent_app']['sysprof']['fill'] = 'red'
G.add_edge('umcagent_app','sysprof')
G.edge['umcagent_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','system_app')
G.edge['umcagent_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['umcagent_app']['system_app']['fill'] = 'red'
G.add_edge('umcagent_app','system_server')
G.edge['umcagent_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['umcagent_app']['system_server']['fill'] = 'red'
G.add_edge('umcagent_app','vdc')
G.edge['umcagent_app']['vdc']['write-read'] = '[write read]'
G.edge['umcagent_app']['vdc']['fill'] = 'red'
G.add_edge('umcagent_app','zygote')
G.edge['umcagent_app']['zygote']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['umcagent_app']['zygote']['fill'] = 'red'
G.add_edge('uncrypt','adbd')
G.edge['uncrypt']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('uncrypt','dumpstate')
G.edge['uncrypt']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('uncrypt','ime_app')
G.edge['uncrypt']['ime_app']['write-read'] = '[open open]'
G.add_edge('uncrypt','itsonbs')
G.edge['uncrypt']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('uncrypt','knox_system_app')
G.edge['uncrypt']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('uncrypt','mediaserver')
G.edge['uncrypt']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('uncrypt','newAttr1')
G.edge['uncrypt']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open]'
G.add_edge('uncrypt','qseecomd')
G.edge['uncrypt']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('uncrypt','shell')
G.edge['uncrypt']['shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('uncrypt','s_system_app')
G.edge['uncrypt']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('uncrypt','s_system_app')
G.edge['uncrypt']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('uncrypt','sysprof')
G.edge['uncrypt']['sysprof']['write-read'] = '[open open]'
G.add_edge('uncrypt','system_app')
G.edge['uncrypt']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('uncrypt','adbd')
G.edge['uncrypt']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('uncrypt','dumpstate')
G.edge['uncrypt']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('uncrypt','installd')
G.edge['uncrypt']['installd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('uncrypt','itsonbs')
G.edge['uncrypt']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('uncrypt','mediaserver')
G.edge['uncrypt']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('uncrypt','qseecomd')
G.edge['uncrypt']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('uncrypt','shell')
G.edge['uncrypt']['shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('uncrypt','sysprof')
G.edge['uncrypt']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('uncrypt','adbd')
G.edge['uncrypt']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['uncrypt']['adbd']['fill'] = 'red'
G.add_edge('uncrypt','adbd')
G.edge['uncrypt']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('uncrypt','binderservicedomain')
G.edge['uncrypt']['binderservicedomain']['write-read'] = '[write read]'
G.edge['uncrypt']['binderservicedomain']['fill'] = 'red'
G.add_edge('uncrypt','dumpstate')
G.edge['uncrypt']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['uncrypt']['dumpstate']['fill'] = 'red'
G.add_edge('uncrypt','dumpstate')
G.edge['uncrypt']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('uncrypt','ime_app')
G.edge['uncrypt']['ime_app']['write-read'] = '[open open][write read]'
G.edge['uncrypt']['ime_app']['fill'] = 'red'
G.add_edge('uncrypt','itsonbs')
G.edge['uncrypt']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['uncrypt']['itsonbs']['fill'] = 'red'
G.add_edge('uncrypt','itsonbs')
G.edge['uncrypt']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('uncrypt','knox_system_app')
G.edge['uncrypt']['knox_system_app']['write-read'] = '[open open][write read]'
G.edge['uncrypt']['knox_system_app']['fill'] = 'red'
G.add_edge('uncrypt','mediaserver')
G.edge['uncrypt']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['uncrypt']['mediaserver']['fill'] = 'red'
G.add_edge('uncrypt','mediaserver')
G.edge['uncrypt']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('uncrypt','newAttr1')
G.edge['uncrypt']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][write read]'
G.edge['uncrypt']['newAttr1']['fill'] = 'red'
G.add_edge('uncrypt','newAttr1')
G.edge['uncrypt']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][write read][write read]'
G.edge['uncrypt']['newAttr1']['fill'] = 'red'
G.add_edge('uncrypt','newAttr40')
G.edge['uncrypt']['newAttr40']['write-read'] = '[write read]'
G.edge['uncrypt']['newAttr40']['fill'] = 'red'
G.add_edge('uncrypt','qseecomd')
G.edge['uncrypt']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['uncrypt']['qseecomd']['fill'] = 'red'
G.add_edge('uncrypt','qseecomd')
G.edge['uncrypt']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('uncrypt','runas')
G.edge['uncrypt']['runas']['write-read'] = '[write read]'
G.edge['uncrypt']['runas']['fill'] = 'red'
G.add_edge('uncrypt','shell')
G.edge['uncrypt']['shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['uncrypt']['shell']['fill'] = 'red'
G.add_edge('uncrypt','shell')
G.edge['uncrypt']['shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('uncrypt','s_system_app')
G.edge['uncrypt']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read]'
G.edge['uncrypt']['s_system_app']['fill'] = 'red'
G.add_edge('uncrypt','s_system_app')
G.edge['uncrypt']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read]'
G.add_edge('uncrypt','s_system_app')
G.edge['uncrypt']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read][write read]'
G.edge['uncrypt']['s_system_app']['fill'] = 'red'
G.add_edge('uncrypt','sysprof')
G.edge['uncrypt']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['uncrypt']['sysprof']['fill'] = 'red'
G.add_edge('uncrypt','sysprof')
G.edge['uncrypt']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('uncrypt','system_app')
G.edge['uncrypt']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['uncrypt']['system_app']['fill'] = 'red'
G.add_edge('uncrypt','system_server')
G.edge['uncrypt']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['uncrypt']['system_server']['fill'] = 'red'
G.add_edge('uncrypt','vdc')
G.edge['uncrypt']['vdc']['write-read'] = '[write read]'
G.edge['uncrypt']['vdc']['fill'] = 'red'
G.add_edge('uncrypt','zygote')
G.edge['uncrypt']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['uncrypt']['zygote']['fill'] = 'red'
G.add_edge('untrusted_app','adbd')
G.edge['untrusted_app']['adbd']['write-read'] = '[write read][open open]'
G.add_edge('untrusted_app','dumpstate')
G.edge['untrusted_app']['dumpstate']['write-read'] = '[open open]'
G.add_edge('untrusted_app','ime_app')
G.edge['untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusted_app','itsonbs')
G.edge['untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusted_app','knox_system_app')
G.edge['untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusted_app','mediaserver')
G.edge['untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusted_app','newAttr1')
G.edge['untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusted_app','qseecomd')
G.edge['untrusted_app']['qseecomd']['write-read'] = '[open open]'
G.add_edge('untrusted_app','shell')
G.edge['untrusted_app']['shell']['write-read'] = '[open open]'
G.add_edge('untrusted_app','s_system_app')
G.edge['untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusted_app','s_system_app')
G.edge['untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('untrusted_app','sysprof')
G.edge['untrusted_app']['sysprof']['write-read'] = '[open open]'
G.add_edge('untrusted_app','system_app')
G.edge['untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusted_app','adbd')
G.edge['untrusted_app']['adbd']['write-read'] = '[write read][open open][setattr getattr]'
G.add_edge('untrusted_app','dumpstate')
G.edge['untrusted_app']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','installd')
G.edge['untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('untrusted_app','itsonbs')
G.edge['untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('untrusted_app','mediaserver')
G.edge['untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('untrusted_app','qseecomd')
G.edge['untrusted_app']['qseecomd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','shell')
G.edge['untrusted_app']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','sysprof')
G.edge['untrusted_app']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','adbd')
G.edge['untrusted_app']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read]'
G.edge['untrusted_app']['adbd']['fill'] = 'red'
G.add_edge('untrusted_app','adbd')
G.edge['untrusted_app']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','binderservicedomain')
G.edge['untrusted_app']['binderservicedomain']['write-read'] = '[write read]'
G.edge['untrusted_app']['binderservicedomain']['fill'] = 'red'
G.add_edge('untrusted_app','dumpstate')
G.edge['untrusted_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusted_app']['dumpstate']['fill'] = 'red'
G.add_edge('untrusted_app','dumpstate')
G.edge['untrusted_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','ime_app')
G.edge['untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['untrusted_app']['ime_app']['fill'] = 'red'
G.add_edge('untrusted_app','itsonbs')
G.edge['untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['untrusted_app']['itsonbs']['fill'] = 'red'
G.add_edge('untrusted_app','itsonbs')
G.edge['untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','knox_system_app')
G.edge['untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['untrusted_app']['knox_system_app']['fill'] = 'red'
G.add_edge('untrusted_app','mediaserver')
G.edge['untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['untrusted_app']['mediaserver']['fill'] = 'red'
G.add_edge('untrusted_app','mediaserver')
G.edge['untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','newAttr1')
G.edge['untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['untrusted_app']['newAttr1']['fill'] = 'red'
G.add_edge('untrusted_app','newAttr1')
G.edge['untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read]'
G.edge['untrusted_app']['newAttr1']['fill'] = 'red'
G.add_edge('untrusted_app','newAttr40')
G.edge['untrusted_app']['newAttr40']['write-read'] = '[write read]'
G.edge['untrusted_app']['newAttr40']['fill'] = 'red'
G.add_edge('untrusted_app','qseecomd')
G.edge['untrusted_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusted_app']['qseecomd']['fill'] = 'red'
G.add_edge('untrusted_app','qseecomd')
G.edge['untrusted_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','runas')
G.edge['untrusted_app']['runas']['write-read'] = '[write read]'
G.edge['untrusted_app']['runas']['fill'] = 'red'
G.add_edge('untrusted_app','shell')
G.edge['untrusted_app']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusted_app']['shell']['fill'] = 'red'
G.add_edge('untrusted_app','shell')
G.edge['untrusted_app']['shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','s_system_app')
G.edge['untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read]'
G.edge['untrusted_app']['s_system_app']['fill'] = 'red'
G.add_edge('untrusted_app','s_system_app')
G.edge['untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read][append read]'
G.add_edge('untrusted_app','s_system_app')
G.edge['untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read]'
G.edge['untrusted_app']['s_system_app']['fill'] = 'red'
G.add_edge('untrusted_app','sysprof')
G.edge['untrusted_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusted_app']['sysprof']['fill'] = 'red'
G.add_edge('untrusted_app','sysprof')
G.edge['untrusted_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','system_app')
G.edge['untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['untrusted_app']['system_app']['fill'] = 'red'
G.add_edge('untrusted_app','system_server')
G.edge['untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('untrusted_app','vdc')
G.edge['untrusted_app']['vdc']['write-read'] = '[write read]'
G.edge['untrusted_app']['vdc']['fill'] = 'red'
G.add_edge('untrusted_app','zygote')
G.edge['untrusted_app']['zygote']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['untrusted_app']['zygote']['fill'] = 'red'
G.add_edge('vdc','adbd')
G.edge['vdc']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('vdc','dumpstate')
G.edge['vdc']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr]'
G.add_edge('vdc','installd')
G.edge['vdc']['installd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr]'
G.add_edge('vdc','itsonbs')
G.edge['vdc']['itsonbs']['write-read'] = '[setattr getattr]'
G.add_edge('vdc','mediaserver')
G.edge['vdc']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('vdc','qseecomd')
G.edge['vdc']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('vdc','shell')
G.edge['vdc']['shell']['write-read'] = '[setattr getattr]'
G.add_edge('vdc','sysprof')
G.edge['vdc']['sysprof']['write-read'] = '[setattr getattr]'
G.add_edge('vpn_untrusted_app','adbd')
G.edge['vpn_untrusted_app']['adbd']['write-read'] = '[write read][open open]'
G.add_edge('vpn_untrusted_app','dumpstate')
G.edge['vpn_untrusted_app']['dumpstate']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','ime_app')
G.edge['vpn_untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('vpn_untrusted_app','itsonbs')
G.edge['vpn_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vpn_untrusted_app','knox_system_app')
G.edge['vpn_untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vpn_untrusted_app','mediaserver')
G.edge['vpn_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('vpn_untrusted_app','newAttr1')
G.edge['vpn_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vpn_untrusted_app','qseecomd')
G.edge['vpn_untrusted_app']['qseecomd']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','shell')
G.edge['vpn_untrusted_app']['shell']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','s_system_app')
G.edge['vpn_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('vpn_untrusted_app','s_system_app')
G.edge['vpn_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('vpn_untrusted_app','sysprof')
G.edge['vpn_untrusted_app']['sysprof']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','system_app')
G.edge['vpn_untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('vpn_untrusted_app','adbd')
G.edge['vpn_untrusted_app']['adbd']['write-read'] = '[write read][open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','dumpstate')
G.edge['vpn_untrusted_app']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','installd')
G.edge['vpn_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('vpn_untrusted_app','itsonbs')
G.edge['vpn_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','mediaserver')
G.edge['vpn_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','qseecomd')
G.edge['vpn_untrusted_app']['qseecomd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','shell')
G.edge['vpn_untrusted_app']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','sysprof')
G.edge['vpn_untrusted_app']['sysprof']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','adbd')
G.edge['vpn_untrusted_app']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['adbd']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','adbd')
G.edge['vpn_untrusted_app']['adbd']['write-read'] = '[write read][open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','binderservicedomain')
G.edge['vpn_untrusted_app']['binderservicedomain']['write-read'] = '[write read]'
G.edge['vpn_untrusted_app']['binderservicedomain']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','dumpstate')
G.edge['vpn_untrusted_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['dumpstate']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','dumpstate')
G.edge['vpn_untrusted_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','ime_app')
G.edge['vpn_untrusted_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['vpn_untrusted_app']['ime_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','itsonbs')
G.edge['vpn_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['itsonbs']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','itsonbs')
G.edge['vpn_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','knox_system_app')
G.edge['vpn_untrusted_app']['knox_system_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vpn_untrusted_app']['knox_system_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','mediaserver')
G.edge['vpn_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['mediaserver']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','mediaserver')
G.edge['vpn_untrusted_app']['mediaserver']['write-read'] = '[setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','newAttr1')
G.edge['vpn_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vpn_untrusted_app']['newAttr1']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','newAttr1')
G.edge['vpn_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read]'
G.edge['vpn_untrusted_app']['newAttr1']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','newAttr40')
G.edge['vpn_untrusted_app']['newAttr40']['write-read'] = '[write read]'
G.edge['vpn_untrusted_app']['newAttr40']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','qseecomd')
G.edge['vpn_untrusted_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['qseecomd']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','qseecomd')
G.edge['vpn_untrusted_app']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','runas')
G.edge['vpn_untrusted_app']['runas']['write-read'] = '[write read]'
G.edge['vpn_untrusted_app']['runas']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','shell')
G.edge['vpn_untrusted_app']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['shell']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','shell')
G.edge['vpn_untrusted_app']['shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','s_system_app')
G.edge['vpn_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read]'
G.edge['vpn_untrusted_app']['s_system_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','s_system_app')
G.edge['vpn_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read][append read]'
G.add_edge('vpn_untrusted_app','s_system_app')
G.edge['vpn_untrusted_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read]'
G.edge['vpn_untrusted_app']['s_system_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','sysprof')
G.edge['vpn_untrusted_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['sysprof']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','sysprof')
G.edge['vpn_untrusted_app']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','system_app')
G.edge['vpn_untrusted_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['vpn_untrusted_app']['system_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','system_server')
G.edge['vpn_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['vpn_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','vdc')
G.edge['vpn_untrusted_app']['vdc']['write-read'] = '[write read]'
G.edge['vpn_untrusted_app']['vdc']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','zygote')
G.edge['vpn_untrusted_app']['zygote']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['vpn_untrusted_app']['zygote']['fill'] = 'red'
G.add_edge('zygote','adbd')
G.edge['zygote']['adbd']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr]'
G.add_edge('zygote','dumpstate')
G.edge['zygote']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr]'
G.add_edge('zygote','installd')
G.edge['zygote']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('zygote','itsonbs')
G.edge['zygote']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('zygote','mediaserver')
G.edge['zygote']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('zygote','qseecomd')
G.edge['zygote']['qseecomd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('zygote','shell')
G.edge['zygote']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr]'
G.add_edge('zygote','sysprof')
G.edge['zygote']['sysprof']['write-read'] = '[setattr getattr]'
app = Viewer(G)
app.mainloop()