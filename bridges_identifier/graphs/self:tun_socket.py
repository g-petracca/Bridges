import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][open open][write read][setattr getattr]'
G.add_edge('bluetooth','clatd')
G.edge['bluetooth']['clatd']['write-read'] = '[open open][write read][append read][open open][write read][append read][setattr getattr]'
G.add_edge('bluetooth','domain')
G.edge['bluetooth']['domain']['read-write'] = '* >getattr'
G.add_edge('bluetooth','racoon')
G.edge['bluetooth']['racoon']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('bluetooth','vpnclientd')
G.edge['bluetooth']['vpnclientd']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][setattr getattr]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][open open][write read][setattr getattr][write read]'
G.edge['bluetooth']['bluetooth']['fill'] = 'red'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][open open][write read][setattr getattr][write read][append read]'
G.add_edge('bluetooth','clatd')
G.edge['bluetooth']['clatd']['write-read'] = '[open open][write read][append read][open open][write read][append read][setattr getattr][write read]'
G.edge['bluetooth']['clatd']['fill'] = 'red'
G.add_edge('bluetooth','clatd')
G.edge['bluetooth']['clatd']['write-read'] = '[open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read]'
G.add_edge('bluetooth','domain')
G.edge['bluetooth']['domain']['read-write'] = '* >read'
G.add_edge('bluetooth','racoon')
G.edge['bluetooth']['racoon']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['bluetooth']['racoon']['fill'] = 'red'
G.add_edge('bluetooth','racoon')
G.edge['bluetooth']['racoon']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read]'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['bluetooth']['system_server']['fill'] = 'red'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read]'
G.add_edge('bluetooth','vpnclientd')
G.edge['bluetooth']['vpnclientd']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][setattr getattr][write read]'
G.edge['bluetooth']['vpnclientd']['fill'] = 'red'
G.add_edge('bluetooth','vpnclientd')
G.edge['bluetooth']['vpnclientd']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][open open][write read][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('bluetooth','clatd')
G.edge['bluetooth']['clatd']['write-read'] = '[open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('bluetooth','domain')
G.edge['bluetooth']['domain']['read-write'] = '* >getopt'
G.add_edge('bluetooth','racoon')
G.edge['bluetooth']['racoon']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('bluetooth','vpnclientd')
G.edge['bluetooth']['vpnclientd']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('clatd','bluetooth')
G.edge['clatd']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read][open open][append read][setattr getattr]'
G.add_edge('clatd','clatd')
G.edge['clatd']['clatd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][write read][write read][open open][write read][append read][write read][setattr getattr]'
G.add_edge('clatd','domain')
G.edge['clatd']['domain']['read-write'] = '* >getattr'
G.add_edge('clatd','racoon')
G.edge['clatd']['racoon']['write-read'] = '[setattr getattr]'
G.add_edge('clatd','system_server')
G.edge['clatd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][setopt getopt][open open][write read][append read][setattr getattr]'
G.add_edge('clatd','vpnclientd')
G.edge['clatd']['vpnclientd']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('clatd','bluetooth')
G.edge['clatd']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read][open open][append read][setattr getattr][write read]'
G.edge['clatd']['bluetooth']['fill'] = 'red'
G.add_edge('clatd','bluetooth')
G.edge['clatd']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read][open open][append read][setattr getattr][write read][append read]'
G.add_edge('clatd','clatd')
G.edge['clatd']['clatd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][write read][write read][open open][write read][append read][write read][setattr getattr][write read]'
G.edge['clatd']['clatd']['fill'] = 'red'
G.add_edge('clatd','clatd')
G.edge['clatd']['clatd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][write read][write read][open open][write read][append read][write read][setattr getattr][write read][append read]'
G.add_edge('clatd','domain')
G.edge['clatd']['domain']['read-write'] = '* >read'
G.add_edge('clatd','racoon')
G.edge['clatd']['racoon']['write-read'] = '[setattr getattr][write read]'
G.edge['clatd']['racoon']['fill'] = 'red'
G.add_edge('clatd','racoon')
G.edge['clatd']['racoon']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('clatd','system_server')
G.edge['clatd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][setopt getopt][open open][write read][append read][setattr getattr][write read]'
G.edge['clatd']['system_server']['fill'] = 'red'
G.add_edge('clatd','system_server')
G.edge['clatd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read]'
G.add_edge('clatd','vpnclientd')
G.edge['clatd']['vpnclientd']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['clatd']['vpnclientd']['fill'] = 'red'
G.add_edge('clatd','vpnclientd')
G.edge['clatd']['vpnclientd']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read]'
G.add_edge('clatd','bluetooth')
G.edge['clatd']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read][open open][append read][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('clatd','clatd')
G.edge['clatd']['clatd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][write read][write read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('clatd','domain')
G.edge['clatd']['domain']['read-write'] = '* >getopt'
G.add_edge('clatd','racoon')
G.edge['clatd']['racoon']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('clatd','system_server')
G.edge['clatd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('clatd','vpnclientd')
G.edge['clatd']['vpnclientd']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('domain','bluetooth')
G.add_edge('domain','clatd')
G.add_edge('domain','domain')
G.add_edge('domain','ime_app')
G.add_edge('domain','netd')
G.add_edge('domain','racoon')
G.add_edge('domain','s_system_app')
G.add_edge('domain','system_app')
G.add_edge('domain','system_server')
G.add_edge('domain','vpnclientd')
G.add_edge('racoon','bluetooth')
G.edge['racoon']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('racoon','clatd')
G.edge['racoon']['clatd']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('racoon','domain')
G.edge['racoon']['domain']['read-write'] = '* >getattr'
G.add_edge('racoon','racoon')
G.edge['racoon']['racoon']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('racoon','system_server')
G.edge['racoon']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('racoon','vpnclientd')
G.edge['racoon']['vpnclientd']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('racoon','bluetooth')
G.edge['racoon']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['racoon']['bluetooth']['fill'] = 'red'
G.add_edge('racoon','bluetooth')
G.edge['racoon']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read]'
G.add_edge('racoon','clatd')
G.edge['racoon']['clatd']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['racoon']['clatd']['fill'] = 'red'
G.add_edge('racoon','clatd')
G.edge['racoon']['clatd']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read]'
G.add_edge('racoon','domain')
G.edge['racoon']['domain']['read-write'] = '* >read'
G.add_edge('racoon','racoon')
G.edge['racoon']['racoon']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['racoon']['racoon']['fill'] = 'red'
G.add_edge('racoon','racoon')
G.edge['racoon']['racoon']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read]'
G.add_edge('racoon','system_server')
G.edge['racoon']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['racoon']['system_server']['fill'] = 'red'
G.add_edge('racoon','system_server')
G.edge['racoon']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read]'
G.add_edge('racoon','vpnclientd')
G.edge['racoon']['vpnclientd']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['racoon']['vpnclientd']['fill'] = 'red'
G.add_edge('racoon','vpnclientd')
G.edge['racoon']['vpnclientd']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read]'
G.add_edge('racoon','bluetooth')
G.edge['racoon']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('racoon','clatd')
G.edge['racoon']['clatd']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('racoon','domain')
G.edge['racoon']['domain']['read-write'] = '* >getopt'
G.add_edge('racoon','racoon')
G.edge['racoon']['racoon']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('racoon','system_server')
G.edge['racoon']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('racoon','vpnclientd')
G.edge['racoon']['vpnclientd']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][setattr getattr]'
G.add_edge('system_server','clatd')
G.edge['system_server']['clatd']['write-read'] = '[add_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setopt getopt][write read][append read][setattr getattr]'
G.add_edge('system_server','domain')
G.edge['system_server']['domain']['read-write'] = '* >getattr'
G.add_edge('system_server','racoon')
G.edge['system_server']['racoon']['write-read'] = '[add_name search][setattr getattr]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setopt getopt][write read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setsched getsched][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][write read][append read][write read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][setattr getattr]'
G.add_edge('system_server','vpnclientd')
G.edge['system_server']['vpnclientd']['write-read'] = '[write read][open open][write read][append read][setattr getattr]'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][setattr getattr][write read]'
G.edge['system_server']['bluetooth']['fill'] = 'red'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][setattr getattr][write read][append read]'
G.add_edge('system_server','clatd')
G.edge['system_server']['clatd']['write-read'] = '[add_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setopt getopt][write read][append read][setattr getattr][write read]'
G.edge['system_server']['clatd']['fill'] = 'red'
G.add_edge('system_server','clatd')
G.edge['system_server']['clatd']['write-read'] = '[add_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setopt getopt][write read][append read][setattr getattr][write read][append read]'
G.add_edge('system_server','domain')
G.edge['system_server']['domain']['read-write'] = '* >read'
G.add_edge('system_server','racoon')
G.edge['system_server']['racoon']['write-read'] = '[add_name search][setattr getattr][write read]'
G.edge['system_server']['racoon']['fill'] = 'red'
G.add_edge('system_server','racoon')
G.edge['system_server']['racoon']['write-read'] = '[add_name search][setattr getattr][write read][append read]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setopt getopt][write read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setsched getsched][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][write read][append read][write read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setopt getopt][write read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setsched getsched][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][write read][append read][write read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read]'
G.add_edge('system_server','vpnclientd')
G.edge['system_server']['vpnclientd']['write-read'] = '[write read][open open][write read][append read][setattr getattr][write read]'
G.edge['system_server']['vpnclientd']['fill'] = 'red'
G.add_edge('system_server','vpnclientd')
G.edge['system_server']['vpnclientd']['write-read'] = '[write read][open open][write read][append read][setattr getattr][write read][append read]'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_server','clatd')
G.edge['system_server']['clatd']['write-read'] = '[add_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setopt getopt][write read][append read][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_server','domain')
G.edge['system_server']['domain']['read-write'] = '* >getopt'
G.add_edge('system_server','racoon')
G.edge['system_server']['racoon']['write-read'] = '[add_name search][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setopt getopt][write read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setsched getsched][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][write read][append read][write read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_server','vpnclientd')
G.edge['system_server']['vpnclientd']['write-read'] = '[write read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('vpnclientd','bluetooth')
G.edge['vpnclientd']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read][setattr getattr]'
G.add_edge('vpnclientd','clatd')
G.edge['vpnclientd']['clatd']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('vpnclientd','domain')
G.edge['vpnclientd']['domain']['read-write'] = '* >getattr'
G.add_edge('vpnclientd','racoon')
G.edge['vpnclientd']['racoon']['write-read'] = '[setattr getattr]'
G.add_edge('vpnclientd','system_server')
G.edge['vpnclientd']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('vpnclientd','vpnclientd')
G.edge['vpnclientd']['vpnclientd']['write-read'] = '[add_name search][write read][open open][write read][append read][open open][write read][append read][setattr getattr]'
G.add_edge('vpnclientd','bluetooth')
G.edge['vpnclientd']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read][setattr getattr][write read]'
G.edge['vpnclientd']['bluetooth']['fill'] = 'red'
G.add_edge('vpnclientd','bluetooth')
G.edge['vpnclientd']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read][setattr getattr][write read][append read]'
G.add_edge('vpnclientd','clatd')
G.edge['vpnclientd']['clatd']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['vpnclientd']['clatd']['fill'] = 'red'
G.add_edge('vpnclientd','clatd')
G.edge['vpnclientd']['clatd']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read]'
G.add_edge('vpnclientd','domain')
G.edge['vpnclientd']['domain']['read-write'] = '* >read'
G.add_edge('vpnclientd','racoon')
G.edge['vpnclientd']['racoon']['write-read'] = '[setattr getattr][write read]'
G.edge['vpnclientd']['racoon']['fill'] = 'red'
G.add_edge('vpnclientd','racoon')
G.edge['vpnclientd']['racoon']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('vpnclientd','system_server')
G.edge['vpnclientd']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['vpnclientd']['system_server']['fill'] = 'red'
G.add_edge('vpnclientd','system_server')
G.edge['vpnclientd']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read]'
G.add_edge('vpnclientd','vpnclientd')
G.edge['vpnclientd']['vpnclientd']['write-read'] = '[add_name search][write read][open open][write read][append read][open open][write read][append read][setattr getattr][write read]'
G.edge['vpnclientd']['vpnclientd']['fill'] = 'red'
G.add_edge('vpnclientd','vpnclientd')
G.edge['vpnclientd']['vpnclientd']['write-read'] = '[add_name search][write read][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read]'
G.add_edge('vpnclientd','bluetooth')
G.edge['vpnclientd']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('vpnclientd','clatd')
G.edge['vpnclientd']['clatd']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('vpnclientd','domain')
G.edge['vpnclientd']['domain']['read-write'] = '* >getopt'
G.add_edge('vpnclientd','racoon')
G.edge['vpnclientd']['racoon']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('vpnclientd','system_server')
G.edge['vpnclientd']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('vpnclientd','vpnclientd')
G.edge['vpnclientd']['vpnclientd']['write-read'] = '[add_name search][write read][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt]'
app = Viewer(G)
app.mainloop()