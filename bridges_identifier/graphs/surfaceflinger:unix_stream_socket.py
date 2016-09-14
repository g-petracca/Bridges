import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][open execmod][write read][open open][open open][write read][append read][append read][open open][open open][write read][append read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['appdomain']['appdomain']['fill'] = 'red'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][open execmod][write read][open open][open open][write read][append read][append read][open open][open open][write read][append read][append read][open open][write read][append read][open open][write read][append read][write read][write read]'
G.edge['appdomain']['appdomain']['fill'] = 'red'
G.add_edge('appdomain','fixmo_app')
G.edge['appdomain']['fixmo_app']['write-read'] = '[open open][append read][open open][setattr getattr][open execmod][open open][append read][open open][append read][write read]'
G.edge['appdomain']['fixmo_app']['fill'] = 'red'
G.add_edge('appdomain','good_app')
G.edge['appdomain']['good_app']['write-read'] = '[open open][append read][open open][setattr getattr][open execmod][open open][append read][open open][append read][write read]'
G.edge['appdomain']['good_app']['fill'] = 'red'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open execmod][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][setattr getattr][write read][append read][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['appdomain']['system_server']['fill'] = 'red'
G.add_edge('appdomain','vmware_app')
G.edge['appdomain']['vmware_app']['read-write'] = '* >read'
G.add_edge('appdomain','vmware_app')
G.edge['appdomain']['vmware_app']['read-write'] = '* >getattr'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][open execmod][write read][open open][open open][write read][append read][append read][open open][open open][write read][append read][append read][open open][write read][append read][open open][write read][append read][write read][write read][write read]'
G.edge['appdomain']['appdomain']['fill'] = 'red'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][open execmod][write read][open open][open open][write read][append read][append read][open open][open open][write read][append read][append read][open open][write read][append read][open open][write read][append read][write read][write read][write read][write read]'
G.edge['appdomain']['appdomain']['fill'] = 'red'
G.add_edge('appdomain','fixmo_app')
G.edge['appdomain']['fixmo_app']['write-read'] = '[open open][append read][open open][setattr getattr][open execmod][open open][append read][open open][append read][write read][write read]'
G.edge['appdomain']['fixmo_app']['fill'] = 'red'
G.add_edge('appdomain','good_app')
G.edge['appdomain']['good_app']['write-read'] = '[open open][append read][open open][setattr getattr][open execmod][open open][append read][open open][append read][write read][write read]'
G.edge['appdomain']['good_app']['fill'] = 'red'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open execmod][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][setattr getattr][write read][append read][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][write read]'
G.edge['appdomain']['system_server']['fill'] = 'red'
G.add_edge('appdomain','vmware_app')
G.edge['appdomain']['vmware_app']['read-write'] = '* >read'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][open execmod][write read][open open][open open][write read][append read][append read][open open][open open][write read][append read][append read][open open][write read][append read][open open][write read][append read][write read][write read][write read][write read][setopt getopt]'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][open execmod][write read][open open][open open][write read][append read][append read][open open][open open][write read][append read][append read][open open][write read][append read][open open][write read][append read][write read][write read][write read][write read][setopt getopt][setopt getopt]'
G.add_edge('appdomain','fixmo_app')
G.edge['appdomain']['fixmo_app']['write-read'] = '[open open][append read][open open][setattr getattr][open execmod][open open][append read][open open][append read][write read][write read][setopt getopt]'
G.add_edge('appdomain','good_app')
G.edge['appdomain']['good_app']['write-read'] = '[open open][append read][open open][setattr getattr][open execmod][open open][append read][open open][append read][write read][write read][setopt getopt]'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open execmod][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][setattr getattr][write read][append read][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][write read][setopt getopt]'
G.add_edge('appdomain','vmware_app')
G.edge['appdomain']['vmware_app']['read-write'] = '* >getopt'
G.add_edge('fixmo_app','vmware_app')
G.edge['fixmo_app']['vmware_app']['read-write'] = '* >getattr'
G.add_edge('fixmo_app','appdomain')
G.edge['fixmo_app']['appdomain']['write-read'] = '[write read][open open][setattr getattr][open execmod][open open][open open][write read]'
G.edge['fixmo_app']['appdomain']['fill'] = 'red'
G.add_edge('fixmo_app','appdomain')
G.edge['fixmo_app']['appdomain']['write-read'] = '[write read][open open][setattr getattr][open execmod][open open][open open][write read][write read]'
G.edge['fixmo_app']['appdomain']['fill'] = 'red'
G.add_edge('fixmo_app','fixmo_app')
G.edge['fixmo_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read]'
G.edge['fixmo_app']['fixmo_app']['fill'] = 'red'
G.add_edge('fixmo_app','good_app')
G.edge['fixmo_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read]'
G.edge['fixmo_app']['good_app']['fill'] = 'red'
G.add_edge('fixmo_app','system_server')
G.edge['fixmo_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read]'
G.edge['fixmo_app']['system_server']['fill'] = 'red'
G.add_edge('fixmo_app','vmware_app')
G.edge['fixmo_app']['vmware_app']['read-write'] = '* >read'
G.add_edge('fixmo_app','appdomain')
G.edge['fixmo_app']['appdomain']['write-read'] = '[write read][open open][setattr getattr][open execmod][open open][open open][write read][write read][setopt getopt]'
G.add_edge('fixmo_app','appdomain')
G.edge['fixmo_app']['appdomain']['write-read'] = '[write read][open open][setattr getattr][open execmod][open open][open open][write read][write read][setopt getopt][setopt getopt]'
G.add_edge('fixmo_app','fixmo_app')
G.edge['fixmo_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read][setopt getopt]'
G.add_edge('fixmo_app','good_app')
G.edge['fixmo_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read][setopt getopt]'
G.add_edge('fixmo_app','system_server')
G.edge['fixmo_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][setopt getopt]'
G.add_edge('fixmo_app','vmware_app')
G.edge['fixmo_app']['vmware_app']['read-write'] = '* >getopt'
G.add_edge('good_app','vmware_app')
G.edge['good_app']['vmware_app']['read-write'] = '* >getattr'
G.add_edge('good_app','appdomain')
G.edge['good_app']['appdomain']['write-read'] = '[write read][open open][setattr getattr][open execmod][open open][open open][write read]'
G.edge['good_app']['appdomain']['fill'] = 'red'
G.add_edge('good_app','appdomain')
G.edge['good_app']['appdomain']['write-read'] = '[write read][open open][setattr getattr][open execmod][open open][open open][write read][write read]'
G.edge['good_app']['appdomain']['fill'] = 'red'
G.add_edge('good_app','fixmo_app')
G.edge['good_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read]'
G.edge['good_app']['fixmo_app']['fill'] = 'red'
G.add_edge('good_app','good_app')
G.edge['good_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read]'
G.edge['good_app']['good_app']['fill'] = 'red'
G.add_edge('good_app','system_server')
G.edge['good_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read]'
G.edge['good_app']['system_server']['fill'] = 'red'
G.add_edge('good_app','vmware_app')
G.edge['good_app']['vmware_app']['read-write'] = '* >read'
G.add_edge('good_app','appdomain')
G.edge['good_app']['appdomain']['write-read'] = '[write read][open open][setattr getattr][open execmod][open open][open open][write read][write read][setopt getopt]'
G.add_edge('good_app','appdomain')
G.edge['good_app']['appdomain']['write-read'] = '[write read][open open][setattr getattr][open execmod][open open][open open][write read][write read][setopt getopt][setopt getopt]'
G.add_edge('good_app','fixmo_app')
G.edge['good_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read][setopt getopt]'
G.add_edge('good_app','good_app')
G.edge['good_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read][setopt getopt]'
G.add_edge('good_app','system_server')
G.edge['good_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][setopt getopt]'
G.add_edge('good_app','vmware_app')
G.edge['good_app']['vmware_app']['read-write'] = '* >getopt'
G.add_edge('system_server','appdomain')
G.edge['system_server']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][setopt getopt][write read][append read][write read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open open][open open][write read][append read][append read][open open][write read][append read][write read]'
G.edge['system_server']['appdomain']['fill'] = 'red'
G.add_edge('system_server','appdomain')
G.edge['system_server']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][setopt getopt][write read][append read][write read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open open][open open][write read][append read][append read][open open][write read][append read][write read][write read]'
G.edge['system_server']['appdomain']['fill'] = 'red'
G.add_edge('system_server','fixmo_app')
G.edge['system_server']['fixmo_app']['write-read'] = '[open open][append read][open open][setattr getattr][open open][append read][write read]'
G.edge['system_server']['fixmo_app']['fill'] = 'red'
G.add_edge('system_server','good_app')
G.edge['system_server']['good_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][append read][open open][setattr getattr][open open][append read][write read]'
G.edge['system_server']['good_app']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setopt getopt][write read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setsched getsched][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][write read][append read][write read][open open][write read][append read][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','vmware_app')
G.edge['system_server']['vmware_app']['read-write'] = '* >read'
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','appdomain')
G.add_edge('vmware_app','fixmo_app')
G.add_edge('vmware_app','good_app')
G.add_edge('vmware_app','system_server')
G.add_edge('vmware_app','vmware_app')
app = Viewer(G)
app.mainloop()