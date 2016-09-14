import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('auditd','auditd')
G.edge['auditd']['auditd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('auditd','drsd')
G.edge['auditd']['drsd']['write-read'] = '[open open]'
G.add_edge('auditd','system_server')
G.edge['auditd']['system_server']['write-read'] = '[open open]'
G.add_edge('auditd','auditd')
G.edge['auditd']['auditd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('auditd','auditd')
G.edge['auditd']['auditd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['auditd']['auditd']['fill'] = 'red'
G.add_edge('auditd','drsd')
G.edge['auditd']['drsd']['write-read'] = '[open open][write read]'
G.edge['auditd']['drsd']['fill'] = 'red'
G.add_edge('auditd','system_server')
G.edge['auditd']['system_server']['write-read'] = '[open open][write read]'
G.edge['auditd']['system_server']['fill'] = 'red'
G.add_edge('auditd','auditd')
G.edge['auditd']['auditd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('auditd','auditd')
G.edge['auditd']['auditd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('auditd','drsd')
G.edge['auditd']['drsd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('auditd','drsd')
G.edge['auditd']['drsd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('auditd','system_server')
G.edge['auditd']['system_server']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('auditd','system_server')
G.edge['auditd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('commonplatformappdomain','auditd')
G.edge['commonplatformappdomain']['auditd']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','drsd')
G.edge['commonplatformappdomain']['drsd']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','system_server')
G.edge['commonplatformappdomain']['system_server']['write-read'] = '[write read][append read][open open]'
G.add_edge('commonplatformappdomain','auditd')
G.edge['commonplatformappdomain']['auditd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','auditd')
G.edge['commonplatformappdomain']['auditd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['auditd']['fill'] = 'red'
G.add_edge('commonplatformappdomain','drsd')
G.edge['commonplatformappdomain']['drsd']['write-read'] = '[open open][write read]'
G.edge['commonplatformappdomain']['drsd']['fill'] = 'red'
G.add_edge('commonplatformappdomain','system_server')
G.edge['commonplatformappdomain']['system_server']['write-read'] = '[write read][append read][open open][write read]'
G.edge['commonplatformappdomain']['system_server']['fill'] = 'red'
G.add_edge('commonplatformappdomain','auditd')
G.edge['commonplatformappdomain']['auditd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('commonplatformappdomain','auditd')
G.edge['commonplatformappdomain']['auditd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('commonplatformappdomain','drsd')
G.edge['commonplatformappdomain']['drsd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('commonplatformappdomain','drsd')
G.edge['commonplatformappdomain']['drsd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('commonplatformappdomain','system_server')
G.edge['commonplatformappdomain']['system_server']['write-read'] = '[write read][append read][open open][write read][add_name search]'
G.add_edge('commonplatformappdomain','system_server')
G.edge['commonplatformappdomain']['system_server']['write-read'] = '[write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('drsd','auditd')
G.edge['drsd']['auditd']['write-read'] = '[open open]'
G.add_edge('drsd','drsd')
G.edge['drsd']['drsd']['write-read'] = '[open open]'
G.add_edge('drsd','system_server')
G.edge['drsd']['system_server']['write-read'] = '[open open]'
G.add_edge('drsd','auditd')
G.edge['drsd']['auditd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('drsd','auditd')
G.edge['drsd']['auditd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['drsd']['auditd']['fill'] = 'red'
G.add_edge('drsd','drsd')
G.edge['drsd']['drsd']['write-read'] = '[open open][write read]'
G.edge['drsd']['drsd']['fill'] = 'red'
G.add_edge('drsd','system_server')
G.edge['drsd']['system_server']['write-read'] = '[open open][write read]'
G.edge['drsd']['system_server']['fill'] = 'red'
G.add_edge('drsd','auditd')
G.edge['drsd']['auditd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('drsd','auditd')
G.edge['drsd']['auditd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('drsd','drsd')
G.edge['drsd']['drsd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('drsd','drsd')
G.edge['drsd']['drsd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('drsd','system_server')
G.edge['drsd']['system_server']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('drsd','system_server')
G.edge['drsd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('shell','auditd')
G.edge['shell']['auditd']['write-read'] = '[add_name search][write read]'
G.edge['shell']['auditd']['fill'] = 'red'
G.add_edge('shell','drsd')
G.edge['shell']['drsd']['write-read'] = '[write read]'
G.edge['shell']['drsd']['fill'] = 'red'
G.add_edge('shell','system_server')
G.edge['shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read]'
G.edge['shell']['system_server']['fill'] = 'red'
G.add_edge('system_server','auditd')
G.edge['system_server']['auditd']['write-read'] = '[add_name search][open open]'
G.add_edge('system_server','drsd')
G.edge['system_server']['drsd']['write-read'] = '[open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','auditd')
G.edge['system_server']['auditd']['write-read'] = '[add_name search][open open][add_name search]'
G.add_edge('system_server','auditd')
G.edge['system_server']['auditd']['write-read'] = '[add_name search][open open][add_name search][remove_name search]'
G.add_edge('system_server','drsd')
G.edge['system_server']['drsd']['write-read'] = '[open open][add_name search]'
G.add_edge('system_server','drsd')
G.edge['system_server']['drsd']['write-read'] = '[open open][add_name search][remove_name search]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()