import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('auditd','auditd')
G.edge['auditd']['auditd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][open open][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('auditd','commonplatformappdomain')
G.edge['auditd']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('auditd','drsd')
G.edge['auditd']['drsd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][open open][open open][write read][open open][write read][open open]'
G.add_edge('auditd','ime_app')
G.edge['auditd']['ime_app']['write-read'] = '[open open]'
G.add_edge('auditd','keystore')
G.edge['auditd']['keystore']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('auditd','samsung_app')
G.edge['auditd']['samsung_app']['write-read'] = '[open open]'
G.add_edge('auditd','servicemanager')
G.edge['auditd']['servicemanager']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('auditd','s_system_app')
G.edge['auditd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('auditd','system_app')
G.edge['auditd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('auditd','system_server')
G.edge['auditd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('auditd','vdc')
G.edge['auditd']['vdc']['write-read'] = '[open open]'
G.add_edge('auditd','zygote')
G.edge['auditd']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('auditd','auditd')
G.edge['auditd']['auditd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][open open][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('auditd','commonplatformappdomain')
G.edge['auditd']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('auditd','drsd')
G.edge['auditd']['drsd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][open open][open open][write read][open open][write read][open open][setattr getattr]'
G.add_edge('auditd','samsung_app')
G.edge['auditd']['samsung_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('auditd','system_server')
G.edge['auditd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('auditd','auditd')
G.edge['auditd']['auditd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][open open][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['auditd']['auditd']['fill'] = 'red'
G.add_edge('auditd','auditd')
G.edge['auditd']['auditd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][open open][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('auditd','commonplatformappdomain')
G.edge['auditd']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['auditd']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('auditd','commonplatformappdomain')
G.edge['auditd']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('auditd','drsd')
G.edge['auditd']['drsd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][open open][open open][write read][open open][write read][open open][setattr getattr][write read]'
G.edge['auditd']['drsd']['fill'] = 'red'
G.add_edge('auditd','drsd')
G.edge['auditd']['drsd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][open open][open open][write read][open open][write read][open open][setattr getattr][write read][append read]'
G.add_edge('auditd','ime_app')
G.edge['auditd']['ime_app']['write-read'] = '[open open][write read]'
G.edge['auditd']['ime_app']['fill'] = 'red'
G.add_edge('auditd','ime_app')
G.edge['auditd']['ime_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('auditd','keystore')
G.edge['auditd']['keystore']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['auditd']['keystore']['fill'] = 'red'
G.add_edge('auditd','keystore')
G.edge['auditd']['keystore']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('auditd','samsung_app')
G.edge['auditd']['samsung_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['auditd']['samsung_app']['fill'] = 'red'
G.add_edge('auditd','samsung_app')
G.edge['auditd']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('auditd','servicemanager')
G.edge['auditd']['servicemanager']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['auditd']['servicemanager']['fill'] = 'red'
G.add_edge('auditd','servicemanager')
G.edge['auditd']['servicemanager']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('auditd','s_system_app')
G.edge['auditd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['auditd']['s_system_app']['fill'] = 'red'
G.add_edge('auditd','s_system_app')
G.edge['auditd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('auditd','system_app')
G.edge['auditd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['auditd']['system_app']['fill'] = 'red'
G.add_edge('auditd','system_app')
G.edge['auditd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('auditd','system_server')
G.edge['auditd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['auditd']['system_server']['fill'] = 'red'
G.add_edge('auditd','system_server')
G.edge['auditd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('auditd','vdc')
G.edge['auditd']['vdc']['write-read'] = '[open open][write read]'
G.edge['auditd']['vdc']['fill'] = 'red'
G.add_edge('auditd','vdc')
G.edge['auditd']['vdc']['write-read'] = '[open open][write read][append read]'
G.add_edge('auditd','zygote')
G.edge['auditd']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['auditd']['zygote']['fill'] = 'red'
G.add_edge('auditd','zygote')
G.edge['auditd']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('commonplatformappdomain','auditd')
G.edge['commonplatformappdomain']['auditd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('commonplatformappdomain','drsd')
G.edge['commonplatformappdomain']['drsd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][open open]'
G.add_edge('commonplatformappdomain','ime_app')
G.edge['commonplatformappdomain']['ime_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('commonplatformappdomain','keystore')
G.edge['commonplatformappdomain']['keystore']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('commonplatformappdomain','samsung_app')
G.edge['commonplatformappdomain']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('commonplatformappdomain','servicemanager')
G.edge['commonplatformappdomain']['servicemanager']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('commonplatformappdomain','s_system_app')
G.edge['commonplatformappdomain']['s_system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('commonplatformappdomain','system_app')
G.edge['commonplatformappdomain']['system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('commonplatformappdomain','system_server')
G.edge['commonplatformappdomain']['system_server']['write-read'] = '[write read][append read][open open][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('commonplatformappdomain','vdc')
G.edge['commonplatformappdomain']['vdc']['write-read'] = '[write read][open open]'
G.add_edge('commonplatformappdomain','zygote')
G.edge['commonplatformappdomain']['zygote']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('commonplatformappdomain','auditd')
G.edge['commonplatformappdomain']['auditd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','drsd')
G.edge['commonplatformappdomain']['drsd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','samsung_app')
G.edge['commonplatformappdomain']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','system_server')
G.edge['commonplatformappdomain']['system_server']['write-read'] = '[write read][append read][open open][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','auditd')
G.edge['commonplatformappdomain']['auditd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['auditd']['fill'] = 'red'
G.add_edge('commonplatformappdomain','auditd')
G.edge['commonplatformappdomain']['auditd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','drsd')
G.edge['commonplatformappdomain']['drsd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['drsd']['fill'] = 'red'
G.add_edge('commonplatformappdomain','drsd')
G.edge['commonplatformappdomain']['drsd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','ime_app')
G.edge['commonplatformappdomain']['ime_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['commonplatformappdomain']['ime_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','ime_app')
G.edge['commonplatformappdomain']['ime_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('commonplatformappdomain','keystore')
G.edge['commonplatformappdomain']['keystore']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['commonplatformappdomain']['keystore']['fill'] = 'red'
G.add_edge('commonplatformappdomain','keystore')
G.edge['commonplatformappdomain']['keystore']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('commonplatformappdomain','samsung_app')
G.edge['commonplatformappdomain']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['samsung_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','samsung_app')
G.edge['commonplatformappdomain']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','servicemanager')
G.edge['commonplatformappdomain']['servicemanager']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['commonplatformappdomain']['servicemanager']['fill'] = 'red'
G.add_edge('commonplatformappdomain','servicemanager')
G.edge['commonplatformappdomain']['servicemanager']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('commonplatformappdomain','s_system_app')
G.edge['commonplatformappdomain']['s_system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['commonplatformappdomain']['s_system_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','s_system_app')
G.edge['commonplatformappdomain']['s_system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('commonplatformappdomain','system_app')
G.edge['commonplatformappdomain']['system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['commonplatformappdomain']['system_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','system_app')
G.edge['commonplatformappdomain']['system_app']['write-read'] = '[open open][write read][append read][write read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('commonplatformappdomain','system_server')
G.edge['commonplatformappdomain']['system_server']['write-read'] = '[write read][append read][open open][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['system_server']['fill'] = 'red'
G.add_edge('commonplatformappdomain','system_server')
G.edge['commonplatformappdomain']['system_server']['write-read'] = '[write read][append read][open open][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','vdc')
G.edge['commonplatformappdomain']['vdc']['write-read'] = '[write read][open open][write read]'
G.edge['commonplatformappdomain']['vdc']['fill'] = 'red'
G.add_edge('commonplatformappdomain','vdc')
G.edge['commonplatformappdomain']['vdc']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('commonplatformappdomain','zygote')
G.edge['commonplatformappdomain']['zygote']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['commonplatformappdomain']['zygote']['fill'] = 'red'
G.add_edge('commonplatformappdomain','zygote')
G.edge['commonplatformappdomain']['zygote']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('drsd','auditd')
G.edge['drsd']['auditd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('drsd','commonplatformappdomain')
G.edge['drsd']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('drsd','drsd')
G.edge['drsd']['drsd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][relabelto relabelfrom][open open][write read][relabelto relabelfrom][open open][write read][open open][write read][relabelto relabelfrom][open open][write read][relabelto relabelfrom][open open][write read][open open][write read][relabelto relabelfrom][open open]'
G.add_edge('drsd','ime_app')
G.edge['drsd']['ime_app']['write-read'] = '[open open]'
G.add_edge('drsd','keystore')
G.edge['drsd']['keystore']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('drsd','samsung_app')
G.edge['drsd']['samsung_app']['write-read'] = '[open open]'
G.add_edge('drsd','servicemanager')
G.edge['drsd']['servicemanager']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('drsd','s_system_app')
G.edge['drsd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('drsd','system_app')
G.edge['drsd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('drsd','system_server')
G.edge['drsd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('drsd','vdc')
G.edge['drsd']['vdc']['write-read'] = '[open open]'
G.add_edge('drsd','zygote')
G.edge['drsd']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('drsd','auditd')
G.edge['drsd']['auditd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('drsd','commonplatformappdomain')
G.edge['drsd']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('drsd','drsd')
G.edge['drsd']['drsd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][relabelto relabelfrom][open open][write read][relabelto relabelfrom][open open][write read][open open][write read][relabelto relabelfrom][open open][write read][relabelto relabelfrom][open open][write read][open open][write read][relabelto relabelfrom][open open][setattr getattr]'
G.add_edge('drsd','samsung_app')
G.edge['drsd']['samsung_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('drsd','system_server')
G.edge['drsd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('drsd','auditd')
G.edge['drsd']['auditd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['drsd']['auditd']['fill'] = 'red'
G.add_edge('drsd','auditd')
G.edge['drsd']['auditd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('drsd','commonplatformappdomain')
G.edge['drsd']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['drsd']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('drsd','commonplatformappdomain')
G.edge['drsd']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('drsd','drsd')
G.edge['drsd']['drsd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][relabelto relabelfrom][open open][write read][relabelto relabelfrom][open open][write read][open open][write read][relabelto relabelfrom][open open][write read][relabelto relabelfrom][open open][write read][open open][write read][relabelto relabelfrom][open open][setattr getattr][write read]'
G.edge['drsd']['drsd']['fill'] = 'red'
G.add_edge('drsd','drsd')
G.edge['drsd']['drsd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][relabelto relabelfrom][open open][write read][relabelto relabelfrom][open open][write read][open open][write read][relabelto relabelfrom][open open][write read][relabelto relabelfrom][open open][write read][open open][write read][relabelto relabelfrom][open open][setattr getattr][write read][append read]'
G.add_edge('drsd','ime_app')
G.edge['drsd']['ime_app']['write-read'] = '[open open][write read]'
G.edge['drsd']['ime_app']['fill'] = 'red'
G.add_edge('drsd','ime_app')
G.edge['drsd']['ime_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('drsd','keystore')
G.edge['drsd']['keystore']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['drsd']['keystore']['fill'] = 'red'
G.add_edge('drsd','keystore')
G.edge['drsd']['keystore']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('drsd','samsung_app')
G.edge['drsd']['samsung_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['drsd']['samsung_app']['fill'] = 'red'
G.add_edge('drsd','samsung_app')
G.edge['drsd']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('drsd','servicemanager')
G.edge['drsd']['servicemanager']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['drsd']['servicemanager']['fill'] = 'red'
G.add_edge('drsd','servicemanager')
G.edge['drsd']['servicemanager']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('drsd','s_system_app')
G.edge['drsd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['drsd']['s_system_app']['fill'] = 'red'
G.add_edge('drsd','s_system_app')
G.edge['drsd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('drsd','system_app')
G.edge['drsd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['drsd']['system_app']['fill'] = 'red'
G.add_edge('drsd','system_app')
G.edge['drsd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('drsd','system_server')
G.edge['drsd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['drsd']['system_server']['fill'] = 'red'
G.add_edge('drsd','system_server')
G.edge['drsd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('drsd','vdc')
G.edge['drsd']['vdc']['write-read'] = '[open open][write read]'
G.edge['drsd']['vdc']['fill'] = 'red'
G.add_edge('drsd','vdc')
G.edge['drsd']['vdc']['write-read'] = '[open open][write read][append read]'
G.add_edge('drsd','zygote')
G.edge['drsd']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['drsd']['zygote']['fill'] = 'red'
G.add_edge('drsd','zygote')
G.edge['drsd']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('keystore','auditd')
G.edge['keystore']['auditd']['write-read'] = '[open open]'
G.add_edge('keystore','commonplatformappdomain')
G.edge['keystore']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('keystore','drsd')
G.edge['keystore']['drsd']['write-read'] = '[open open]'
G.add_edge('keystore','ime_app')
G.edge['keystore']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('keystore','keystore')
G.edge['keystore']['keystore']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open]'
G.add_edge('keystore','samsung_app')
G.edge['keystore']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('keystore','servicemanager')
G.edge['keystore']['servicemanager']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('keystore','s_system_app')
G.edge['keystore']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('keystore','system_app')
G.edge['keystore']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('keystore','system_server')
G.edge['keystore']['system_server']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('keystore','vdc')
G.edge['keystore']['vdc']['write-read'] = '[open open]'
G.add_edge('keystore','zygote')
G.edge['keystore']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open]'
G.add_edge('keystore','auditd')
G.edge['keystore']['auditd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('keystore','commonplatformappdomain')
G.edge['keystore']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('keystore','drsd')
G.edge['keystore']['drsd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('keystore','samsung_app')
G.edge['keystore']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('keystore','system_server')
G.edge['keystore']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('keystore','auditd')
G.edge['keystore']['auditd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['keystore']['auditd']['fill'] = 'red'
G.add_edge('keystore','auditd')
G.edge['keystore']['auditd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('keystore','commonplatformappdomain')
G.edge['keystore']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['keystore']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('keystore','commonplatformappdomain')
G.edge['keystore']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('keystore','drsd')
G.edge['keystore']['drsd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['keystore']['drsd']['fill'] = 'red'
G.add_edge('keystore','drsd')
G.edge['keystore']['drsd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('keystore','ime_app')
G.edge['keystore']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['keystore']['ime_app']['fill'] = 'red'
G.add_edge('keystore','ime_app')
G.edge['keystore']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('keystore','keystore')
G.edge['keystore']['keystore']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read]'
G.edge['keystore']['keystore']['fill'] = 'red'
G.add_edge('keystore','keystore')
G.edge['keystore']['keystore']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read]'
G.add_edge('keystore','samsung_app')
G.edge['keystore']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['keystore']['samsung_app']['fill'] = 'red'
G.add_edge('keystore','samsung_app')
G.edge['keystore']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('keystore','servicemanager')
G.edge['keystore']['servicemanager']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['keystore']['servicemanager']['fill'] = 'red'
G.add_edge('keystore','servicemanager')
G.edge['keystore']['servicemanager']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('keystore','s_system_app')
G.edge['keystore']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['keystore']['s_system_app']['fill'] = 'red'
G.add_edge('keystore','s_system_app')
G.edge['keystore']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('keystore','system_app')
G.edge['keystore']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['keystore']['system_app']['fill'] = 'red'
G.add_edge('keystore','system_app')
G.edge['keystore']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('keystore','system_server')
G.edge['keystore']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['keystore']['system_server']['fill'] = 'red'
G.add_edge('keystore','system_server')
G.edge['keystore']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('keystore','vdc')
G.edge['keystore']['vdc']['write-read'] = '[open open][write read]'
G.edge['keystore']['vdc']['fill'] = 'red'
G.add_edge('keystore','vdc')
G.edge['keystore']['vdc']['write-read'] = '[open open][write read][append read]'
G.add_edge('keystore','zygote')
G.edge['keystore']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][write read]'
G.edge['keystore']['zygote']['fill'] = 'red'
G.add_edge('keystore','zygote')
G.edge['keystore']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][write read][append read]'
G.add_edge('samsung_app','auditd')
G.edge['samsung_app']['auditd']['write-read'] = '[open open]'
G.add_edge('samsung_app','commonplatformappdomain')
G.edge['samsung_app']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('samsung_app','drsd')
G.edge['samsung_app']['drsd']['write-read'] = '[open open]'
G.add_edge('samsung_app','ime_app')
G.edge['samsung_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('samsung_app','keystore')
G.edge['samsung_app']['keystore']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('samsung_app','samsung_app')
G.edge['samsung_app']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('samsung_app','servicemanager')
G.edge['samsung_app']['servicemanager']['write-read'] = '[open open]'
G.add_edge('samsung_app','s_system_app')
G.edge['samsung_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('samsung_app','system_app')
G.edge['samsung_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('samsung_app','system_server')
G.edge['samsung_app']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('samsung_app','vdc')
G.edge['samsung_app']['vdc']['write-read'] = '[open open]'
G.add_edge('samsung_app','zygote')
G.edge['samsung_app']['zygote']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('samsung_app','auditd')
G.edge['samsung_app']['auditd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('samsung_app','commonplatformappdomain')
G.edge['samsung_app']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('samsung_app','drsd')
G.edge['samsung_app']['drsd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('samsung_app','samsung_app')
G.edge['samsung_app']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('samsung_app','system_server')
G.edge['samsung_app']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('samsung_app','auditd')
G.edge['samsung_app']['auditd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['samsung_app']['auditd']['fill'] = 'red'
G.add_edge('samsung_app','auditd')
G.edge['samsung_app']['auditd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('samsung_app','commonplatformappdomain')
G.edge['samsung_app']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['samsung_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('samsung_app','commonplatformappdomain')
G.edge['samsung_app']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('samsung_app','drsd')
G.edge['samsung_app']['drsd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['samsung_app']['drsd']['fill'] = 'red'
G.add_edge('samsung_app','drsd')
G.edge['samsung_app']['drsd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('samsung_app','ime_app')
G.edge['samsung_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['samsung_app']['ime_app']['fill'] = 'red'
G.add_edge('samsung_app','ime_app')
G.edge['samsung_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('samsung_app','keystore')
G.edge['samsung_app']['keystore']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['samsung_app']['keystore']['fill'] = 'red'
G.add_edge('samsung_app','keystore')
G.edge['samsung_app']['keystore']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('samsung_app','samsung_app')
G.edge['samsung_app']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['samsung_app']['samsung_app']['fill'] = 'red'
G.add_edge('samsung_app','samsung_app')
G.edge['samsung_app']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('samsung_app','servicemanager')
G.edge['samsung_app']['servicemanager']['write-read'] = '[open open][write read]'
G.edge['samsung_app']['servicemanager']['fill'] = 'red'
G.add_edge('samsung_app','servicemanager')
G.edge['samsung_app']['servicemanager']['write-read'] = '[open open][write read][append read]'
G.add_edge('samsung_app','s_system_app')
G.edge['samsung_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['samsung_app']['s_system_app']['fill'] = 'red'
G.add_edge('samsung_app','s_system_app')
G.edge['samsung_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('samsung_app','system_app')
G.edge['samsung_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['samsung_app']['system_app']['fill'] = 'red'
G.add_edge('samsung_app','system_app')
G.edge['samsung_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('samsung_app','system_server')
G.edge['samsung_app']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['samsung_app']['system_server']['fill'] = 'red'
G.add_edge('samsung_app','system_server')
G.edge['samsung_app']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('samsung_app','vdc')
G.edge['samsung_app']['vdc']['write-read'] = '[open open][write read]'
G.edge['samsung_app']['vdc']['fill'] = 'red'
G.add_edge('samsung_app','vdc')
G.edge['samsung_app']['vdc']['write-read'] = '[open open][write read][append read]'
G.add_edge('samsung_app','zygote')
G.edge['samsung_app']['zygote']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['samsung_app']['zygote']['fill'] = 'red'
G.add_edge('samsung_app','zygote')
G.edge['samsung_app']['zygote']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('servicemanager','auditd')
G.edge['servicemanager']['auditd']['write-read'] = '[open open]'
G.add_edge('servicemanager','commonplatformappdomain')
G.edge['servicemanager']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('servicemanager','drsd')
G.edge['servicemanager']['drsd']['write-read'] = '[open open][write read][open open]'
G.add_edge('servicemanager','ime_app')
G.edge['servicemanager']['ime_app']['write-read'] = '[open open]'
G.add_edge('servicemanager','keystore')
G.edge['servicemanager']['keystore']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('servicemanager','samsung_app')
G.edge['servicemanager']['samsung_app']['write-read'] = '[open open]'
G.add_edge('servicemanager','servicemanager')
G.edge['servicemanager']['servicemanager']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('servicemanager','s_system_app')
G.edge['servicemanager']['s_system_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('servicemanager','system_app')
G.edge['servicemanager']['system_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('servicemanager','system_server')
G.edge['servicemanager']['system_server']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('servicemanager','vdc')
G.edge['servicemanager']['vdc']['write-read'] = '[open open]'
G.add_edge('servicemanager','zygote')
G.edge['servicemanager']['zygote']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('servicemanager','auditd')
G.edge['servicemanager']['auditd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('servicemanager','commonplatformappdomain')
G.edge['servicemanager']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('servicemanager','drsd')
G.edge['servicemanager']['drsd']['write-read'] = '[open open][write read][open open][setattr getattr]'
G.add_edge('servicemanager','samsung_app')
G.edge['servicemanager']['samsung_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('servicemanager','system_server')
G.edge['servicemanager']['system_server']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('servicemanager','auditd')
G.edge['servicemanager']['auditd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['servicemanager']['auditd']['fill'] = 'red'
G.add_edge('servicemanager','auditd')
G.edge['servicemanager']['auditd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('servicemanager','commonplatformappdomain')
G.edge['servicemanager']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['servicemanager']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('servicemanager','commonplatformappdomain')
G.edge['servicemanager']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('servicemanager','drsd')
G.edge['servicemanager']['drsd']['write-read'] = '[open open][write read][open open][setattr getattr][write read]'
G.edge['servicemanager']['drsd']['fill'] = 'red'
G.add_edge('servicemanager','drsd')
G.edge['servicemanager']['drsd']['write-read'] = '[open open][write read][open open][setattr getattr][write read][append read]'
G.add_edge('servicemanager','ime_app')
G.edge['servicemanager']['ime_app']['write-read'] = '[open open][write read]'
G.edge['servicemanager']['ime_app']['fill'] = 'red'
G.add_edge('servicemanager','ime_app')
G.edge['servicemanager']['ime_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('servicemanager','keystore')
G.edge['servicemanager']['keystore']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['servicemanager']['keystore']['fill'] = 'red'
G.add_edge('servicemanager','keystore')
G.edge['servicemanager']['keystore']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('servicemanager','samsung_app')
G.edge['servicemanager']['samsung_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['servicemanager']['samsung_app']['fill'] = 'red'
G.add_edge('servicemanager','samsung_app')
G.edge['servicemanager']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('servicemanager','servicemanager')
G.edge['servicemanager']['servicemanager']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['servicemanager']['servicemanager']['fill'] = 'red'
G.add_edge('servicemanager','servicemanager')
G.edge['servicemanager']['servicemanager']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('servicemanager','s_system_app')
G.edge['servicemanager']['s_system_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['servicemanager']['s_system_app']['fill'] = 'red'
G.add_edge('servicemanager','s_system_app')
G.edge['servicemanager']['s_system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('servicemanager','system_app')
G.edge['servicemanager']['system_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['servicemanager']['system_app']['fill'] = 'red'
G.add_edge('servicemanager','system_app')
G.edge['servicemanager']['system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('servicemanager','system_server')
G.edge['servicemanager']['system_server']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['servicemanager']['system_server']['fill'] = 'red'
G.add_edge('servicemanager','system_server')
G.edge['servicemanager']['system_server']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('servicemanager','vdc')
G.edge['servicemanager']['vdc']['write-read'] = '[open open][write read]'
G.edge['servicemanager']['vdc']['fill'] = 'red'
G.add_edge('servicemanager','vdc')
G.edge['servicemanager']['vdc']['write-read'] = '[open open][write read][append read]'
G.add_edge('servicemanager','zygote')
G.edge['servicemanager']['zygote']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['servicemanager']['zygote']['fill'] = 'red'
G.add_edge('servicemanager','zygote')
G.edge['servicemanager']['zygote']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('shell','auditd')
G.edge['shell']['auditd']['write-read'] = '[add_name search][write read][write read]'
G.edge['shell']['auditd']['fill'] = 'red'
G.add_edge('shell','auditd')
G.edge['shell']['auditd']['write-read'] = '[add_name search][write read][write read][append read]'
G.add_edge('shell','commonplatformappdomain')
G.edge['shell']['commonplatformappdomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['shell']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('shell','commonplatformappdomain')
G.edge['shell']['commonplatformappdomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('shell','drsd')
G.edge['shell']['drsd']['write-read'] = '[write read][write read]'
G.edge['shell']['drsd']['fill'] = 'red'
G.add_edge('shell','drsd')
G.edge['shell']['drsd']['write-read'] = '[write read][write read][append read]'
G.add_edge('shell','ime_app')
G.edge['shell']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][write read][open open][setattr getattr][write read][append read][write read]'
G.edge['shell']['ime_app']['fill'] = 'red'
G.add_edge('shell','ime_app')
G.edge['shell']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][write read][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('shell','keystore')
G.edge['shell']['keystore']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['shell']['keystore']['fill'] = 'red'
G.add_edge('shell','keystore')
G.edge['shell']['keystore']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][append read]'
G.add_edge('shell','samsung_app')
G.edge['shell']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['shell']['samsung_app']['fill'] = 'red'
G.add_edge('shell','samsung_app')
G.edge['shell']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('shell','servicemanager')
G.edge['shell']['servicemanager']['write-read'] = '[write read]'
G.edge['shell']['servicemanager']['fill'] = 'red'
G.add_edge('shell','servicemanager')
G.edge['shell']['servicemanager']['write-read'] = '[write read][append read]'
G.add_edge('shell','s_system_app')
G.edge['shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['shell']['s_system_app']['fill'] = 'red'
G.add_edge('shell','s_system_app')
G.edge['shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('shell','system_app')
G.edge['shell']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][write read][open open][setattr getattr][write read][append read][write read]'
G.edge['shell']['system_app']['fill'] = 'red'
G.add_edge('shell','system_app')
G.edge['shell']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][write read][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('shell','system_server')
G.edge['shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][write read][open open][setattr getattr][write read][append read][write read]'
G.edge['shell']['system_server']['fill'] = 'red'
G.add_edge('shell','system_server')
G.edge['shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][write read][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('shell','vdc')
G.edge['shell']['vdc']['write-read'] = '[write read][write read][write read]'
G.edge['shell']['vdc']['fill'] = 'red'
G.add_edge('shell','vdc')
G.edge['shell']['vdc']['write-read'] = '[write read][write read][write read][append read]'
G.add_edge('shell','zygote')
G.edge['shell']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][append read][write read]'
G.edge['shell']['zygote']['fill'] = 'red'
G.add_edge('shell','zygote')
G.edge['shell']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('system_server','auditd')
G.edge['system_server']['auditd']['write-read'] = '[add_name search][open open][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','commonplatformappdomain')
G.edge['system_server']['commonplatformappdomain']['write-read'] = '[setopt getopt][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','drsd')
G.edge['system_server']['drsd']['write-read'] = '[open open][add_name search][remove_name search][open open][relabelto relabelfrom][open open][write read][open open][write read][open open][write read][open open][write read][open open]'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][add_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','keystore')
G.edge['system_server']['keystore']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('system_server','samsung_app')
G.edge['system_server']['samsung_app']['write-read'] = '[setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','servicemanager')
G.edge['system_server']['servicemanager']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','vdc')
G.edge['system_server']['vdc']['write-read'] = '[write read][write read][open open]'
G.add_edge('system_server','zygote')
G.edge['system_server']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][write read][write read][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','auditd')
G.edge['system_server']['auditd']['write-read'] = '[add_name search][open open][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','commonplatformappdomain')
G.edge['system_server']['commonplatformappdomain']['write-read'] = '[setopt getopt][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','drsd')
G.edge['system_server']['drsd']['write-read'] = '[open open][add_name search][remove_name search][open open][relabelto relabelfrom][open open][write read][open open][write read][open open][write read][open open][write read][open open][setattr getattr]'
G.add_edge('system_server','samsung_app')
G.edge['system_server']['samsung_app']['write-read'] = '[setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','auditd')
G.edge['system_server']['auditd']['write-read'] = '[add_name search][open open][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['auditd']['fill'] = 'red'
G.add_edge('system_server','auditd')
G.edge['system_server']['auditd']['write-read'] = '[add_name search][open open][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','commonplatformappdomain')
G.edge['system_server']['commonplatformappdomain']['write-read'] = '[setopt getopt][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('system_server','commonplatformappdomain')
G.edge['system_server']['commonplatformappdomain']['write-read'] = '[setopt getopt][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','drsd')
G.edge['system_server']['drsd']['write-read'] = '[open open][add_name search][remove_name search][open open][relabelto relabelfrom][open open][write read][open open][write read][open open][write read][open open][write read][open open][setattr getattr][write read]'
G.edge['system_server']['drsd']['fill'] = 'red'
G.add_edge('system_server','drsd')
G.edge['system_server']['drsd']['write-read'] = '[open open][add_name search][remove_name search][open open][relabelto relabelfrom][open open][write read][open open][write read][open open][write read][open open][write read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][add_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['ime_app']['fill'] = 'red'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][add_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','keystore')
G.edge['system_server']['keystore']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['system_server']['keystore']['fill'] = 'red'
G.add_edge('system_server','keystore')
G.edge['system_server']['keystore']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','samsung_app')
G.edge['system_server']['samsung_app']['write-read'] = '[setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['samsung_app']['fill'] = 'red'
G.add_edge('system_server','samsung_app')
G.edge['system_server']['samsung_app']['write-read'] = '[setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','servicemanager')
G.edge['system_server']['servicemanager']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['system_server']['servicemanager']['fill'] = 'red'
G.add_edge('system_server','servicemanager')
G.edge['system_server']['servicemanager']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['s_system_app']['fill'] = 'red'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['system_app']['fill'] = 'red'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','vdc')
G.edge['system_server']['vdc']['write-read'] = '[write read][write read][open open][write read]'
G.edge['system_server']['vdc']['fill'] = 'red'
G.add_edge('system_server','vdc')
G.edge['system_server']['vdc']['write-read'] = '[write read][write read][open open][write read][append read]'
G.add_edge('system_server','zygote')
G.edge['system_server']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][write read][write read][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['zygote']['fill'] = 'red'
G.add_edge('system_server','zygote')
G.edge['system_server']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][write read][write read][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('zygote','auditd')
G.edge['zygote']['auditd']['write-read'] = '[add_name search][open open][open open][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('zygote','commonplatformappdomain')
G.edge['zygote']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('zygote','drsd')
G.edge['zygote']['drsd']['write-read'] = '[open open][open open][open open][write read][open open][write read][open open]'
G.add_edge('zygote','ime_app')
G.edge['zygote']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('zygote','keystore')
G.edge['zygote']['keystore']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('zygote','samsung_app')
G.edge['zygote']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('zygote','servicemanager')
G.edge['zygote']['servicemanager']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('zygote','s_system_app')
G.edge['zygote']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('zygote','system_app')
G.edge['zygote']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('zygote','system_server')
G.edge['zygote']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('zygote','vdc')
G.edge['zygote']['vdc']['write-read'] = '[open open]'
G.add_edge('zygote','zygote')
G.edge['zygote']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setpgid getpgid][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('zygote','auditd')
G.edge['zygote']['auditd']['write-read'] = '[add_name search][open open][open open][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('zygote','commonplatformappdomain')
G.edge['zygote']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('zygote','drsd')
G.edge['zygote']['drsd']['write-read'] = '[open open][open open][open open][write read][open open][write read][open open][setattr getattr]'
G.add_edge('zygote','samsung_app')
G.edge['zygote']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('zygote','system_server')
G.edge['zygote']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('zygote','auditd')
G.edge['zygote']['auditd']['write-read'] = '[add_name search][open open][open open][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['zygote']['auditd']['fill'] = 'red'
G.add_edge('zygote','auditd')
G.edge['zygote']['auditd']['write-read'] = '[add_name search][open open][open open][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('zygote','commonplatformappdomain')
G.edge['zygote']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['zygote']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('zygote','commonplatformappdomain')
G.edge['zygote']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('zygote','drsd')
G.edge['zygote']['drsd']['write-read'] = '[open open][open open][open open][write read][open open][write read][open open][setattr getattr][write read]'
G.edge['zygote']['drsd']['fill'] = 'red'
G.add_edge('zygote','drsd')
G.edge['zygote']['drsd']['write-read'] = '[open open][open open][open open][write read][open open][write read][open open][setattr getattr][write read][append read]'
G.add_edge('zygote','ime_app')
G.edge['zygote']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['zygote']['ime_app']['fill'] = 'red'
G.add_edge('zygote','ime_app')
G.edge['zygote']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('zygote','keystore')
G.edge['zygote']['keystore']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['zygote']['keystore']['fill'] = 'red'
G.add_edge('zygote','keystore')
G.edge['zygote']['keystore']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('zygote','samsung_app')
G.edge['zygote']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['zygote']['samsung_app']['fill'] = 'red'
G.add_edge('zygote','samsung_app')
G.edge['zygote']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('zygote','servicemanager')
G.edge['zygote']['servicemanager']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['zygote']['servicemanager']['fill'] = 'red'
G.add_edge('zygote','servicemanager')
G.edge['zygote']['servicemanager']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('zygote','s_system_app')
G.edge['zygote']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['zygote']['s_system_app']['fill'] = 'red'
G.add_edge('zygote','s_system_app')
G.edge['zygote']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('zygote','system_app')
G.edge['zygote']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['zygote']['system_app']['fill'] = 'red'
G.add_edge('zygote','system_app')
G.edge['zygote']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('zygote','system_server')
G.edge['zygote']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['zygote']['system_server']['fill'] = 'red'
G.add_edge('zygote','system_server')
G.edge['zygote']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('zygote','vdc')
G.edge['zygote']['vdc']['write-read'] = '[open open][write read]'
G.edge['zygote']['vdc']['fill'] = 'red'
G.add_edge('zygote','vdc')
G.edge['zygote']['vdc']['write-read'] = '[open open][write read][append read]'
G.add_edge('zygote','zygote')
G.edge['zygote']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setpgid getpgid][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['zygote']['zygote']['fill'] = 'red'
G.add_edge('zygote','zygote')
G.edge['zygote']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setpgid getpgid][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
app = Viewer(G)
app.mainloop()