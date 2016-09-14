import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('appdomain','init_shell')
G.edge['appdomain']['init_shell']['write-read'] = '[setattr getattr][open open]'
G.add_edge('appdomain','installd')
G.edge['appdomain']['installd']['write-read'] = '[setattr getattr][setattr getattr][add_name search][remove_name search][setattr getattr][open open]'
G.add_edge('appdomain','keystore')
G.edge['appdomain']['keystore']['write-read'] = '[open open]'
G.add_edge('appdomain','runas')
G.edge['appdomain']['runas']['write-read'] = '[open open]'
G.add_edge('appdomain','servicemanager')
G.edge['appdomain']['servicemanager']['write-read'] = '[open open]'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open]'
G.add_edge('appdomain','zygote')
G.edge['appdomain']['zygote']['write-read'] = '[open open]'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['appdomain']['appdomain']['fill'] = 'red'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('appdomain','init_shell')
G.edge['appdomain']['init_shell']['write-read'] = '[setattr getattr][open open][write read]'
G.edge['appdomain']['init_shell']['fill'] = 'red'
G.add_edge('appdomain','init_shell')
G.edge['appdomain']['init_shell']['write-read'] = '[setattr getattr][open open][write read][append read]'
G.add_edge('appdomain','installd')
G.edge['appdomain']['installd']['write-read'] = '[setattr getattr][setattr getattr][add_name search][remove_name search][setattr getattr][open open][write read]'
G.edge['appdomain']['installd']['fill'] = 'red'
G.add_edge('appdomain','installd')
G.edge['appdomain']['installd']['write-read'] = '[setattr getattr][setattr getattr][add_name search][remove_name search][setattr getattr][open open][write read][append read]'
G.add_edge('appdomain','keystore')
G.edge['appdomain']['keystore']['write-read'] = '[open open][write read]'
G.edge['appdomain']['keystore']['fill'] = 'red'
G.add_edge('appdomain','keystore')
G.edge['appdomain']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('appdomain','runas')
G.edge['appdomain']['runas']['write-read'] = '[open open][write read]'
G.edge['appdomain']['runas']['fill'] = 'red'
G.add_edge('appdomain','runas')
G.edge['appdomain']['runas']['write-read'] = '[open open][write read][append read]'
G.add_edge('appdomain','servicemanager')
G.edge['appdomain']['servicemanager']['write-read'] = '[open open][write read]'
G.edge['appdomain']['servicemanager']['fill'] = 'red'
G.add_edge('appdomain','servicemanager')
G.edge['appdomain']['servicemanager']['write-read'] = '[open open][write read][append read]'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read]'
G.edge['appdomain']['system_server']['fill'] = 'red'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read]'
G.add_edge('appdomain','zygote')
G.edge['appdomain']['zygote']['write-read'] = '[open open][write read]'
G.edge['appdomain']['zygote']['fill'] = 'red'
G.add_edge('appdomain','zygote')
G.edge['appdomain']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('auditd','appdomain')
G.edge['auditd']['appdomain']['write-read'] = '[open open]'
G.add_edge('auditd','init_shell')
G.edge['auditd']['init_shell']['write-read'] = '[open open]'
G.add_edge('auditd','installd')
G.edge['auditd']['installd']['write-read'] = '[open open]'
G.add_edge('auditd','keystore')
G.edge['auditd']['keystore']['write-read'] = '[open open]'
G.add_edge('auditd','runas')
G.edge['auditd']['runas']['write-read'] = '[open open]'
G.add_edge('auditd','servicemanager')
G.edge['auditd']['servicemanager']['write-read'] = '[open open]'
G.add_edge('auditd','system_server')
G.edge['auditd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('auditd','zygote')
G.edge['auditd']['zygote']['write-read'] = '[open open]'
G.add_edge('auditd','appdomain')
G.edge['auditd']['appdomain']['write-read'] = '[open open][write read]'
G.edge['auditd']['appdomain']['fill'] = 'red'
G.add_edge('auditd','appdomain')
G.edge['auditd']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('auditd','init_shell')
G.edge['auditd']['init_shell']['write-read'] = '[open open][write read]'
G.edge['auditd']['init_shell']['fill'] = 'red'
G.add_edge('auditd','init_shell')
G.edge['auditd']['init_shell']['write-read'] = '[open open][write read][append read]'
G.add_edge('auditd','installd')
G.edge['auditd']['installd']['write-read'] = '[open open][write read]'
G.edge['auditd']['installd']['fill'] = 'red'
G.add_edge('auditd','installd')
G.edge['auditd']['installd']['write-read'] = '[open open][write read][append read]'
G.add_edge('auditd','keystore')
G.edge['auditd']['keystore']['write-read'] = '[open open][write read]'
G.edge['auditd']['keystore']['fill'] = 'red'
G.add_edge('auditd','keystore')
G.edge['auditd']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('auditd','runas')
G.edge['auditd']['runas']['write-read'] = '[open open][write read]'
G.edge['auditd']['runas']['fill'] = 'red'
G.add_edge('auditd','runas')
G.edge['auditd']['runas']['write-read'] = '[open open][write read][append read]'
G.add_edge('auditd','servicemanager')
G.edge['auditd']['servicemanager']['write-read'] = '[open open][write read]'
G.edge['auditd']['servicemanager']['fill'] = 'red'
G.add_edge('auditd','servicemanager')
G.edge['auditd']['servicemanager']['write-read'] = '[open open][write read][append read]'
G.add_edge('auditd','system_server')
G.edge['auditd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['auditd']['system_server']['fill'] = 'red'
G.add_edge('auditd','system_server')
G.edge['auditd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('auditd','zygote')
G.edge['auditd']['zygote']['write-read'] = '[open open][write read]'
G.edge['auditd']['zygote']['fill'] = 'red'
G.add_edge('auditd','zygote')
G.edge['auditd']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('commonplatformappdomain','appdomain')
G.edge['commonplatformappdomain']['appdomain']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','init_shell')
G.edge['commonplatformappdomain']['init_shell']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','installd')
G.edge['commonplatformappdomain']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('commonplatformappdomain','keystore')
G.edge['commonplatformappdomain']['keystore']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','runas')
G.edge['commonplatformappdomain']['runas']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','servicemanager')
G.edge['commonplatformappdomain']['servicemanager']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','system_server')
G.edge['commonplatformappdomain']['system_server']['write-read'] = '[write read][append read][open open][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('commonplatformappdomain','zygote')
G.edge['commonplatformappdomain']['zygote']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('commonplatformappdomain','appdomain')
G.edge['commonplatformappdomain']['appdomain']['write-read'] = '[open open][write read]'
G.edge['commonplatformappdomain']['appdomain']['fill'] = 'red'
G.add_edge('commonplatformappdomain','appdomain')
G.edge['commonplatformappdomain']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('commonplatformappdomain','init_shell')
G.edge['commonplatformappdomain']['init_shell']['write-read'] = '[open open][write read]'
G.edge['commonplatformappdomain']['init_shell']['fill'] = 'red'
G.add_edge('commonplatformappdomain','init_shell')
G.edge['commonplatformappdomain']['init_shell']['write-read'] = '[open open][write read][append read]'
G.add_edge('commonplatformappdomain','installd')
G.edge['commonplatformappdomain']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['commonplatformappdomain']['installd']['fill'] = 'red'
G.add_edge('commonplatformappdomain','installd')
G.edge['commonplatformappdomain']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('commonplatformappdomain','keystore')
G.edge['commonplatformappdomain']['keystore']['write-read'] = '[open open][write read]'
G.edge['commonplatformappdomain']['keystore']['fill'] = 'red'
G.add_edge('commonplatformappdomain','keystore')
G.edge['commonplatformappdomain']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('commonplatformappdomain','runas')
G.edge['commonplatformappdomain']['runas']['write-read'] = '[open open][write read]'
G.edge['commonplatformappdomain']['runas']['fill'] = 'red'
G.add_edge('commonplatformappdomain','runas')
G.edge['commonplatformappdomain']['runas']['write-read'] = '[open open][write read][append read]'
G.add_edge('commonplatformappdomain','servicemanager')
G.edge['commonplatformappdomain']['servicemanager']['write-read'] = '[open open][write read]'
G.edge['commonplatformappdomain']['servicemanager']['fill'] = 'red'
G.add_edge('commonplatformappdomain','servicemanager')
G.edge['commonplatformappdomain']['servicemanager']['write-read'] = '[open open][write read][append read]'
G.add_edge('commonplatformappdomain','system_server')
G.edge['commonplatformappdomain']['system_server']['write-read'] = '[write read][append read][open open][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['commonplatformappdomain']['system_server']['fill'] = 'red'
G.add_edge('commonplatformappdomain','system_server')
G.edge['commonplatformappdomain']['system_server']['write-read'] = '[write read][append read][open open][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('commonplatformappdomain','zygote')
G.edge['commonplatformappdomain']['zygote']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['commonplatformappdomain']['zygote']['fill'] = 'red'
G.add_edge('commonplatformappdomain','zygote')
G.edge['commonplatformappdomain']['zygote']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('debuggerd','appdomain')
G.edge['debuggerd']['appdomain']['write-read'] = '[open open]'
G.add_edge('debuggerd','init_shell')
G.edge['debuggerd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('debuggerd','installd')
G.edge['debuggerd']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('debuggerd','keystore')
G.edge['debuggerd']['keystore']['write-read'] = '[open open]'
G.add_edge('debuggerd','runas')
G.edge['debuggerd']['runas']['write-read'] = '[open open]'
G.add_edge('debuggerd','servicemanager')
G.edge['debuggerd']['servicemanager']['write-read'] = '[open open]'
G.add_edge('debuggerd','system_server')
G.edge['debuggerd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open]'
G.add_edge('debuggerd','zygote')
G.edge['debuggerd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('debuggerd','appdomain')
G.edge['debuggerd']['appdomain']['write-read'] = '[open open][write read]'
G.edge['debuggerd']['appdomain']['fill'] = 'red'
G.add_edge('debuggerd','appdomain')
G.edge['debuggerd']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('debuggerd','init_shell')
G.edge['debuggerd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['debuggerd']['init_shell']['fill'] = 'red'
G.add_edge('debuggerd','init_shell')
G.edge['debuggerd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('debuggerd','installd')
G.edge['debuggerd']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['debuggerd']['installd']['fill'] = 'red'
G.add_edge('debuggerd','installd')
G.edge['debuggerd']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('debuggerd','keystore')
G.edge['debuggerd']['keystore']['write-read'] = '[open open][write read]'
G.edge['debuggerd']['keystore']['fill'] = 'red'
G.add_edge('debuggerd','keystore')
G.edge['debuggerd']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('debuggerd','runas')
G.edge['debuggerd']['runas']['write-read'] = '[open open][write read]'
G.edge['debuggerd']['runas']['fill'] = 'red'
G.add_edge('debuggerd','runas')
G.edge['debuggerd']['runas']['write-read'] = '[open open][write read][append read]'
G.add_edge('debuggerd','servicemanager')
G.edge['debuggerd']['servicemanager']['write-read'] = '[open open][write read]'
G.edge['debuggerd']['servicemanager']['fill'] = 'red'
G.add_edge('debuggerd','servicemanager')
G.edge['debuggerd']['servicemanager']['write-read'] = '[open open][write read][append read]'
G.add_edge('debuggerd','system_server')
G.edge['debuggerd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read]'
G.edge['debuggerd']['system_server']['fill'] = 'red'
G.add_edge('debuggerd','system_server')
G.edge['debuggerd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read]'
G.add_edge('debuggerd','zygote')
G.edge['debuggerd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['debuggerd']['zygote']['fill'] = 'red'
G.add_edge('debuggerd','zygote')
G.edge['debuggerd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','appdomain')
G.edge['domain']['appdomain']['write-read'] = '[open open]'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('domain','installd')
G.edge['domain']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][setattr getattr][open open]'
G.add_edge('domain','keystore')
G.edge['domain']['keystore']['write-read'] = '[open open]'
G.add_edge('domain','runas')
G.edge['domain']['runas']['write-read'] = '[open open]'
G.add_edge('domain','servicemanager')
G.edge['domain']['servicemanager']['write-read'] = '[open open]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open]'
G.add_edge('domain','zygote')
G.edge['domain']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('domain','appdomain')
G.edge['domain']['appdomain']['write-read'] = '[open open][write read]'
G.edge['domain']['appdomain']['fill'] = 'red'
G.add_edge('domain','appdomain')
G.edge['domain']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['domain']['init_shell']['fill'] = 'red'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('domain','installd')
G.edge['domain']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read]'
G.edge['domain']['installd']['fill'] = 'red'
G.add_edge('domain','installd')
G.edge['domain']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][append read]'
G.add_edge('domain','keystore')
G.edge['domain']['keystore']['write-read'] = '[open open][write read]'
G.edge['domain']['keystore']['fill'] = 'red'
G.add_edge('domain','keystore')
G.edge['domain']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('domain','runas')
G.edge['domain']['runas']['write-read'] = '[open open][write read]'
G.edge['domain']['runas']['fill'] = 'red'
G.add_edge('domain','runas')
G.edge['domain']['runas']['write-read'] = '[open open][write read][append read]'
G.add_edge('domain','servicemanager')
G.edge['domain']['servicemanager']['write-read'] = '[open open][write read]'
G.edge['domain']['servicemanager']['fill'] = 'red'
G.add_edge('domain','servicemanager')
G.edge['domain']['servicemanager']['write-read'] = '[open open][write read][append read]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read]'
G.edge['domain']['system_server']['fill'] = 'red'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','zygote')
G.edge['domain']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['domain']['zygote']['fill'] = 'red'
G.add_edge('domain','zygote')
G.edge['domain']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('drsd','appdomain')
G.edge['drsd']['appdomain']['write-read'] = '[open open]'
G.add_edge('drsd','init_shell')
G.edge['drsd']['init_shell']['write-read'] = '[open open]'
G.add_edge('drsd','installd')
G.edge['drsd']['installd']['write-read'] = '[open open]'
G.add_edge('drsd','keystore')
G.edge['drsd']['keystore']['write-read'] = '[open open]'
G.add_edge('drsd','runas')
G.edge['drsd']['runas']['write-read'] = '[open open]'
G.add_edge('drsd','servicemanager')
G.edge['drsd']['servicemanager']['write-read'] = '[open open]'
G.add_edge('drsd','system_server')
G.edge['drsd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('drsd','zygote')
G.edge['drsd']['zygote']['write-read'] = '[open open]'
G.add_edge('drsd','appdomain')
G.edge['drsd']['appdomain']['write-read'] = '[open open][write read]'
G.edge['drsd']['appdomain']['fill'] = 'red'
G.add_edge('drsd','appdomain')
G.edge['drsd']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('drsd','init_shell')
G.edge['drsd']['init_shell']['write-read'] = '[open open][write read]'
G.edge['drsd']['init_shell']['fill'] = 'red'
G.add_edge('drsd','init_shell')
G.edge['drsd']['init_shell']['write-read'] = '[open open][write read][append read]'
G.add_edge('drsd','installd')
G.edge['drsd']['installd']['write-read'] = '[open open][write read]'
G.edge['drsd']['installd']['fill'] = 'red'
G.add_edge('drsd','installd')
G.edge['drsd']['installd']['write-read'] = '[open open][write read][append read]'
G.add_edge('drsd','keystore')
G.edge['drsd']['keystore']['write-read'] = '[open open][write read]'
G.edge['drsd']['keystore']['fill'] = 'red'
G.add_edge('drsd','keystore')
G.edge['drsd']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('drsd','runas')
G.edge['drsd']['runas']['write-read'] = '[open open][write read]'
G.edge['drsd']['runas']['fill'] = 'red'
G.add_edge('drsd','runas')
G.edge['drsd']['runas']['write-read'] = '[open open][write read][append read]'
G.add_edge('drsd','servicemanager')
G.edge['drsd']['servicemanager']['write-read'] = '[open open][write read]'
G.edge['drsd']['servicemanager']['fill'] = 'red'
G.add_edge('drsd','servicemanager')
G.edge['drsd']['servicemanager']['write-read'] = '[open open][write read][append read]'
G.add_edge('drsd','system_server')
G.edge['drsd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['drsd']['system_server']['fill'] = 'red'
G.add_edge('drsd','system_server')
G.edge['drsd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('drsd','zygote')
G.edge['drsd']['zygote']['write-read'] = '[open open][write read]'
G.edge['drsd']['zygote']['fill'] = 'red'
G.add_edge('drsd','zygote')
G.edge['drsd']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('ime_app','appdomain')
G.edge['ime_app']['appdomain']['write-read'] = '[open open]'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','installd')
G.edge['ime_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr][setattr getattr][open open]'
G.add_edge('ime_app','keystore')
G.edge['ime_app']['keystore']['write-read'] = '[open open]'
G.add_edge('ime_app','runas')
G.edge['ime_app']['runas']['write-read'] = '[open open]'
G.add_edge('ime_app','servicemanager')
G.edge['ime_app']['servicemanager']['write-read'] = '[open open]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open]'
G.add_edge('ime_app','zygote')
G.edge['ime_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('ime_app','appdomain')
G.edge['ime_app']['appdomain']['write-read'] = '[open open][write read]'
G.edge['ime_app']['appdomain']['fill'] = 'red'
G.add_edge('ime_app','appdomain')
G.edge['ime_app']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['ime_app']['init_shell']['fill'] = 'red'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('ime_app','installd')
G.edge['ime_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr][setattr getattr][open open][write read]'
G.edge['ime_app']['installd']['fill'] = 'red'
G.add_edge('ime_app','installd')
G.edge['ime_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr][setattr getattr][open open][write read][append read]'
G.add_edge('ime_app','keystore')
G.edge['ime_app']['keystore']['write-read'] = '[open open][write read]'
G.edge['ime_app']['keystore']['fill'] = 'red'
G.add_edge('ime_app','keystore')
G.edge['ime_app']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('ime_app','runas')
G.edge['ime_app']['runas']['write-read'] = '[open open][write read]'
G.edge['ime_app']['runas']['fill'] = 'red'
G.add_edge('ime_app','runas')
G.edge['ime_app']['runas']['write-read'] = '[open open][write read][append read]'
G.add_edge('ime_app','servicemanager')
G.edge['ime_app']['servicemanager']['write-read'] = '[open open][write read]'
G.edge['ime_app']['servicemanager']['fill'] = 'red'
G.add_edge('ime_app','servicemanager')
G.edge['ime_app']['servicemanager']['write-read'] = '[open open][write read][append read]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read]'
G.edge['ime_app']['system_server']['fill'] = 'red'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read]'
G.add_edge('ime_app','zygote')
G.edge['ime_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['ime_app']['zygote']['fill'] = 'red'
G.add_edge('ime_app','zygote')
G.edge['ime_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('init_shell','appdomain')
G.edge['init_shell']['appdomain']['write-read'] = '[open open]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('init_shell','installd')
G.edge['init_shell']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open]'
G.add_edge('init_shell','keystore')
G.edge['init_shell']['keystore']['write-read'] = '[open open]'
G.add_edge('init_shell','runas')
G.edge['init_shell']['runas']['write-read'] = '[open open]'
G.add_edge('init_shell','servicemanager')
G.edge['init_shell']['servicemanager']['write-read'] = '[open open]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('init_shell','zygote')
G.edge['init_shell']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','appdomain')
G.edge['init_shell']['appdomain']['write-read'] = '[open open][write read]'
G.edge['init_shell']['appdomain']['fill'] = 'red'
G.add_edge('init_shell','appdomain')
G.edge['init_shell']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['init_shell']['init_shell']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('init_shell','installd')
G.edge['init_shell']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read]'
G.edge['init_shell']['installd']['fill'] = 'red'
G.add_edge('init_shell','installd')
G.edge['init_shell']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][append read]'
G.add_edge('init_shell','keystore')
G.edge['init_shell']['keystore']['write-read'] = '[open open][write read]'
G.edge['init_shell']['keystore']['fill'] = 'red'
G.add_edge('init_shell','keystore')
G.edge['init_shell']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('init_shell','runas')
G.edge['init_shell']['runas']['write-read'] = '[open open][write read]'
G.edge['init_shell']['runas']['fill'] = 'red'
G.add_edge('init_shell','runas')
G.edge['init_shell']['runas']['write-read'] = '[open open][write read][append read]'
G.add_edge('init_shell','servicemanager')
G.edge['init_shell']['servicemanager']['write-read'] = '[open open][write read]'
G.edge['init_shell']['servicemanager']['fill'] = 'red'
G.add_edge('init_shell','servicemanager')
G.edge['init_shell']['servicemanager']['write-read'] = '[open open][write read][append read]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['init_shell']['system_server']['fill'] = 'red'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('init_shell','zygote')
G.edge['init_shell']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['zygote']['fill'] = 'red'
G.add_edge('init_shell','zygote')
G.edge['init_shell']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('installd','appdomain')
G.edge['installd']['appdomain']['write-read'] = '[open open]'
G.add_edge('installd','init_shell')
G.edge['installd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open]'
G.add_edge('installd','keystore')
G.edge['installd']['keystore']['write-read'] = '[open open]'
G.add_edge('installd','runas')
G.edge['installd']['runas']['write-read'] = '[open open]'
G.add_edge('installd','servicemanager')
G.edge['installd']['servicemanager']['write-read'] = '[open open]'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][add_name search][remove_name search][setattr getattr][open open]'
G.add_edge('installd','zygote')
G.edge['installd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('installd','appdomain')
G.edge['installd']['appdomain']['write-read'] = '[open open][write read]'
G.edge['installd']['appdomain']['fill'] = 'red'
G.add_edge('installd','appdomain')
G.edge['installd']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('installd','init_shell')
G.edge['installd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read]'
G.edge['installd']['init_shell']['fill'] = 'red'
G.add_edge('installd','init_shell')
G.edge['installd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][append read]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][write read]'
G.edge['installd']['installd']['fill'] = 'red'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][relabelto relabelfrom][setattr getattr][setattr getattr][relabelto relabelfrom][open open][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][write read][append read]'
G.add_edge('installd','keystore')
G.edge['installd']['keystore']['write-read'] = '[open open][write read]'
G.edge['installd']['keystore']['fill'] = 'red'
G.add_edge('installd','keystore')
G.edge['installd']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('installd','runas')
G.edge['installd']['runas']['write-read'] = '[open open][write read]'
G.edge['installd']['runas']['fill'] = 'red'
G.add_edge('installd','runas')
G.edge['installd']['runas']['write-read'] = '[open open][write read][append read]'
G.add_edge('installd','servicemanager')
G.edge['installd']['servicemanager']['write-read'] = '[open open][write read]'
G.edge['installd']['servicemanager']['fill'] = 'red'
G.add_edge('installd','servicemanager')
G.edge['installd']['servicemanager']['write-read'] = '[open open][write read][append read]'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][add_name search][remove_name search][setattr getattr][open open][write read]'
G.edge['installd']['system_server']['fill'] = 'red'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][add_name search][remove_name search][setattr getattr][open open][write read][append read]'
G.add_edge('installd','zygote')
G.edge['installd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['installd']['zygote']['fill'] = 'red'
G.add_edge('installd','zygote')
G.edge['installd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('keystore','appdomain')
G.edge['keystore']['appdomain']['write-read'] = '[open open]'
G.add_edge('keystore','init_shell')
G.edge['keystore']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('keystore','installd')
G.edge['keystore']['installd']['write-read'] = '[open open]'
G.add_edge('keystore','keystore')
G.edge['keystore']['keystore']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('keystore','runas')
G.edge['keystore']['runas']['write-read'] = '[open open]'
G.add_edge('keystore','servicemanager')
G.edge['keystore']['servicemanager']['write-read'] = '[open open]'
G.add_edge('keystore','system_server')
G.edge['keystore']['system_server']['write-read'] = '[open open]'
G.add_edge('keystore','zygote')
G.edge['keystore']['zygote']['write-read'] = '[open open]'
G.add_edge('keystore','appdomain')
G.edge['keystore']['appdomain']['write-read'] = '[open open][write read]'
G.edge['keystore']['appdomain']['fill'] = 'red'
G.add_edge('keystore','appdomain')
G.edge['keystore']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('keystore','init_shell')
G.edge['keystore']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['keystore']['init_shell']['fill'] = 'red'
G.add_edge('keystore','init_shell')
G.edge['keystore']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('keystore','installd')
G.edge['keystore']['installd']['write-read'] = '[open open][write read]'
G.edge['keystore']['installd']['fill'] = 'red'
G.add_edge('keystore','installd')
G.edge['keystore']['installd']['write-read'] = '[open open][write read][append read]'
G.add_edge('keystore','keystore')
G.edge['keystore']['keystore']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['keystore']['keystore']['fill'] = 'red'
G.add_edge('keystore','keystore')
G.edge['keystore']['keystore']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('keystore','runas')
G.edge['keystore']['runas']['write-read'] = '[open open][write read]'
G.edge['keystore']['runas']['fill'] = 'red'
G.add_edge('keystore','runas')
G.edge['keystore']['runas']['write-read'] = '[open open][write read][append read]'
G.add_edge('keystore','servicemanager')
G.edge['keystore']['servicemanager']['write-read'] = '[open open][write read]'
G.edge['keystore']['servicemanager']['fill'] = 'red'
G.add_edge('keystore','servicemanager')
G.edge['keystore']['servicemanager']['write-read'] = '[open open][write read][append read]'
G.add_edge('keystore','system_server')
G.edge['keystore']['system_server']['write-read'] = '[open open][write read]'
G.edge['keystore']['system_server']['fill'] = 'red'
G.add_edge('keystore','system_server')
G.edge['keystore']['system_server']['write-read'] = '[open open][write read][append read]'
G.add_edge('keystore','zygote')
G.edge['keystore']['zygote']['write-read'] = '[open open][write read]'
G.edge['keystore']['zygote']['fill'] = 'red'
G.add_edge('keystore','zygote')
G.edge['keystore']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('runas','appdomain')
G.edge['runas']['appdomain']['write-read'] = '[open open]'
G.add_edge('runas','init_shell')
G.edge['runas']['init_shell']['write-read'] = '[open open]'
G.add_edge('runas','installd')
G.edge['runas']['installd']['write-read'] = '[open open]'
G.add_edge('runas','keystore')
G.edge['runas']['keystore']['write-read'] = '[open open]'
G.add_edge('runas','runas')
G.edge['runas']['runas']['write-read'] = '[write read][open open]'
G.add_edge('runas','servicemanager')
G.edge['runas']['servicemanager']['write-read'] = '[open open]'
G.add_edge('runas','system_server')
G.edge['runas']['system_server']['write-read'] = '[write read][append read][open open]'
G.add_edge('runas','zygote')
G.edge['runas']['zygote']['write-read'] = '[open open]'
G.add_edge('runas','appdomain')
G.edge['runas']['appdomain']['write-read'] = '[open open][write read]'
G.edge['runas']['appdomain']['fill'] = 'red'
G.add_edge('runas','appdomain')
G.edge['runas']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('runas','init_shell')
G.edge['runas']['init_shell']['write-read'] = '[open open][write read]'
G.edge['runas']['init_shell']['fill'] = 'red'
G.add_edge('runas','init_shell')
G.edge['runas']['init_shell']['write-read'] = '[open open][write read][append read]'
G.add_edge('runas','installd')
G.edge['runas']['installd']['write-read'] = '[open open][write read]'
G.edge['runas']['installd']['fill'] = 'red'
G.add_edge('runas','installd')
G.edge['runas']['installd']['write-read'] = '[open open][write read][append read]'
G.add_edge('runas','keystore')
G.edge['runas']['keystore']['write-read'] = '[open open][write read]'
G.edge['runas']['keystore']['fill'] = 'red'
G.add_edge('runas','keystore')
G.edge['runas']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('runas','runas')
G.edge['runas']['runas']['write-read'] = '[write read][open open][write read]'
G.edge['runas']['runas']['fill'] = 'red'
G.add_edge('runas','runas')
G.edge['runas']['runas']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('runas','servicemanager')
G.edge['runas']['servicemanager']['write-read'] = '[open open][write read]'
G.edge['runas']['servicemanager']['fill'] = 'red'
G.add_edge('runas','servicemanager')
G.edge['runas']['servicemanager']['write-read'] = '[open open][write read][append read]'
G.add_edge('runas','system_server')
G.edge['runas']['system_server']['write-read'] = '[write read][append read][open open][write read]'
G.edge['runas']['system_server']['fill'] = 'red'
G.add_edge('runas','system_server')
G.edge['runas']['system_server']['write-read'] = '[write read][append read][open open][write read][append read]'
G.add_edge('runas','zygote')
G.edge['runas']['zygote']['write-read'] = '[open open][write read]'
G.edge['runas']['zygote']['fill'] = 'red'
G.add_edge('runas','zygote')
G.edge['runas']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('servicemanager','appdomain')
G.edge['servicemanager']['appdomain']['write-read'] = '[open open]'
G.add_edge('servicemanager','init_shell')
G.edge['servicemanager']['init_shell']['write-read'] = '[open open]'
G.add_edge('servicemanager','installd')
G.edge['servicemanager']['installd']['write-read'] = '[open open]'
G.add_edge('servicemanager','keystore')
G.edge['servicemanager']['keystore']['write-read'] = '[open open]'
G.add_edge('servicemanager','runas')
G.edge['servicemanager']['runas']['write-read'] = '[open open]'
G.add_edge('servicemanager','servicemanager')
G.edge['servicemanager']['servicemanager']['write-read'] = '[open open]'
G.add_edge('servicemanager','system_server')
G.edge['servicemanager']['system_server']['write-read'] = '[open open]'
G.add_edge('servicemanager','zygote')
G.edge['servicemanager']['zygote']['write-read'] = '[open open]'
G.add_edge('servicemanager','appdomain')
G.edge['servicemanager']['appdomain']['write-read'] = '[open open][write read]'
G.edge['servicemanager']['appdomain']['fill'] = 'red'
G.add_edge('servicemanager','appdomain')
G.edge['servicemanager']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('servicemanager','init_shell')
G.edge['servicemanager']['init_shell']['write-read'] = '[open open][write read]'
G.edge['servicemanager']['init_shell']['fill'] = 'red'
G.add_edge('servicemanager','init_shell')
G.edge['servicemanager']['init_shell']['write-read'] = '[open open][write read][append read]'
G.add_edge('servicemanager','installd')
G.edge['servicemanager']['installd']['write-read'] = '[open open][write read]'
G.edge['servicemanager']['installd']['fill'] = 'red'
G.add_edge('servicemanager','installd')
G.edge['servicemanager']['installd']['write-read'] = '[open open][write read][append read]'
G.add_edge('servicemanager','keystore')
G.edge['servicemanager']['keystore']['write-read'] = '[open open][write read]'
G.edge['servicemanager']['keystore']['fill'] = 'red'
G.add_edge('servicemanager','keystore')
G.edge['servicemanager']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('servicemanager','runas')
G.edge['servicemanager']['runas']['write-read'] = '[open open][write read]'
G.edge['servicemanager']['runas']['fill'] = 'red'
G.add_edge('servicemanager','runas')
G.edge['servicemanager']['runas']['write-read'] = '[open open][write read][append read]'
G.add_edge('servicemanager','servicemanager')
G.edge['servicemanager']['servicemanager']['write-read'] = '[open open][write read]'
G.edge['servicemanager']['servicemanager']['fill'] = 'red'
G.add_edge('servicemanager','servicemanager')
G.edge['servicemanager']['servicemanager']['write-read'] = '[open open][write read][append read]'
G.add_edge('servicemanager','system_server')
G.edge['servicemanager']['system_server']['write-read'] = '[open open][write read]'
G.edge['servicemanager']['system_server']['fill'] = 'red'
G.add_edge('servicemanager','system_server')
G.edge['servicemanager']['system_server']['write-read'] = '[open open][write read][append read]'
G.add_edge('servicemanager','zygote')
G.edge['servicemanager']['zygote']['write-read'] = '[open open][write read]'
G.edge['servicemanager']['zygote']['fill'] = 'red'
G.add_edge('servicemanager','zygote')
G.edge['servicemanager']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','appdomain')
G.edge['s_system_app']['appdomain']['write-read'] = '[open open]'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','installd')
G.edge['s_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr][setattr getattr][open open]'
G.add_edge('s_system_app','keystore')
G.edge['s_system_app']['keystore']['write-read'] = '[open open]'
G.add_edge('s_system_app','runas')
G.edge['s_system_app']['runas']['write-read'] = '[open open]'
G.add_edge('s_system_app','servicemanager')
G.edge['s_system_app']['servicemanager']['write-read'] = '[open open]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open]'
G.add_edge('s_system_app','zygote')
G.edge['s_system_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('s_system_app','appdomain')
G.edge['s_system_app']['appdomain']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['appdomain']['fill'] = 'red'
G.add_edge('s_system_app','appdomain')
G.edge['s_system_app']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['s_system_app']['init_shell']['fill'] = 'red'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('s_system_app','installd')
G.edge['s_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr][setattr getattr][open open][write read]'
G.edge['s_system_app']['installd']['fill'] = 'red'
G.add_edge('s_system_app','installd')
G.edge['s_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr][setattr getattr][open open][write read][append read]'
G.add_edge('s_system_app','keystore')
G.edge['s_system_app']['keystore']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['keystore']['fill'] = 'red'
G.add_edge('s_system_app','keystore')
G.edge['s_system_app']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','runas')
G.edge['s_system_app']['runas']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['runas']['fill'] = 'red'
G.add_edge('s_system_app','runas')
G.edge['s_system_app']['runas']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','servicemanager')
G.edge['s_system_app']['servicemanager']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['servicemanager']['fill'] = 'red'
G.add_edge('s_system_app','servicemanager')
G.edge['s_system_app']['servicemanager']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read]'
G.edge['s_system_app']['system_server']['fill'] = 'red'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read]'
G.add_edge('s_system_app','zygote')
G.edge['s_system_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['s_system_app']['zygote']['fill'] = 'red'
G.add_edge('s_system_app','zygote')
G.edge['s_system_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_app','appdomain')
G.edge['system_app']['appdomain']['write-read'] = '[open open]'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','installd')
G.edge['system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr][setattr getattr][open open]'
G.add_edge('system_app','keystore')
G.edge['system_app']['keystore']['write-read'] = '[open open]'
G.add_edge('system_app','runas')
G.edge['system_app']['runas']['write-read'] = '[open open]'
G.add_edge('system_app','servicemanager')
G.edge['system_app']['servicemanager']['write-read'] = '[open open]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open]'
G.add_edge('system_app','zygote')
G.edge['system_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_app','appdomain')
G.edge['system_app']['appdomain']['write-read'] = '[open open][write read]'
G.edge['system_app']['appdomain']['fill'] = 'red'
G.add_edge('system_app','appdomain')
G.edge['system_app']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['system_app']['init_shell']['fill'] = 'red'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('system_app','installd')
G.edge['system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr][setattr getattr][open open][write read]'
G.edge['system_app']['installd']['fill'] = 'red'
G.add_edge('system_app','installd')
G.edge['system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][setattr getattr][setattr getattr][open open][write read][append read]'
G.add_edge('system_app','keystore')
G.edge['system_app']['keystore']['write-read'] = '[open open][write read]'
G.edge['system_app']['keystore']['fill'] = 'red'
G.add_edge('system_app','keystore')
G.edge['system_app']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_app','runas')
G.edge['system_app']['runas']['write-read'] = '[open open][write read]'
G.edge['system_app']['runas']['fill'] = 'red'
G.add_edge('system_app','runas')
G.edge['system_app']['runas']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_app','servicemanager')
G.edge['system_app']['servicemanager']['write-read'] = '[open open][write read]'
G.edge['system_app']['servicemanager']['fill'] = 'red'
G.add_edge('system_app','servicemanager')
G.edge['system_app']['servicemanager']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read]'
G.edge['system_app']['system_server']['fill'] = 'red'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read]'
G.add_edge('system_app','zygote')
G.edge['system_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['system_app']['zygote']['fill'] = 'red'
G.add_edge('system_app','zygote')
G.edge['system_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','appdomain')
G.edge['system_server']['appdomain']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][setattr getattr][open open][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open]'
G.add_edge('system_server','keystore')
G.edge['system_server']['keystore']['write-read'] = '[open open]'
G.add_edge('system_server','runas')
G.edge['system_server']['runas']['write-read'] = '[open open]'
G.add_edge('system_server','servicemanager')
G.edge['system_server']['servicemanager']['write-read'] = '[open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open]'
G.add_edge('system_server','zygote')
G.edge['system_server']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','appdomain')
G.edge['system_server']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['system_server']['appdomain']['fill'] = 'red'
G.add_edge('system_server','appdomain')
G.edge['system_server']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['init_shell']['fill'] = 'red'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][setattr getattr][open open][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read]'
G.edge['system_server']['installd']['fill'] = 'red'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][setattr getattr][open open][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][append read]'
G.add_edge('system_server','keystore')
G.edge['system_server']['keystore']['write-read'] = '[open open][write read]'
G.edge['system_server']['keystore']['fill'] = 'red'
G.add_edge('system_server','keystore')
G.edge['system_server']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','runas')
G.edge['system_server']['runas']['write-read'] = '[open open][write read]'
G.edge['system_server']['runas']['fill'] = 'red'
G.add_edge('system_server','runas')
G.edge['system_server']['runas']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','servicemanager')
G.edge['system_server']['servicemanager']['write-read'] = '[open open][write read]'
G.edge['system_server']['servicemanager']['fill'] = 'red'
G.add_edge('system_server','servicemanager')
G.edge['system_server']['servicemanager']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read]'
G.add_edge('system_server','zygote')
G.edge['system_server']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['zygote']['fill'] = 'red'
G.add_edge('system_server','zygote')
G.edge['system_server']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('ueventd','appdomain')
G.edge['ueventd']['appdomain']['write-read'] = '[open open]'
G.add_edge('ueventd','init_shell')
G.edge['ueventd']['init_shell']['write-read'] = '[open open]'
G.add_edge('ueventd','installd')
G.edge['ueventd']['installd']['write-read'] = '[open open]'
G.add_edge('ueventd','keystore')
G.edge['ueventd']['keystore']['write-read'] = '[open open]'
G.add_edge('ueventd','runas')
G.edge['ueventd']['runas']['write-read'] = '[open open]'
G.add_edge('ueventd','servicemanager')
G.edge['ueventd']['servicemanager']['write-read'] = '[open open]'
G.add_edge('ueventd','system_server')
G.edge['ueventd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ueventd','zygote')
G.edge['ueventd']['zygote']['write-read'] = '[open open]'
G.add_edge('ueventd','appdomain')
G.edge['ueventd']['appdomain']['write-read'] = '[open open][write read]'
G.edge['ueventd']['appdomain']['fill'] = 'red'
G.add_edge('ueventd','appdomain')
G.edge['ueventd']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('ueventd','init_shell')
G.edge['ueventd']['init_shell']['write-read'] = '[open open][write read]'
G.edge['ueventd']['init_shell']['fill'] = 'red'
G.add_edge('ueventd','init_shell')
G.edge['ueventd']['init_shell']['write-read'] = '[open open][write read][append read]'
G.add_edge('ueventd','installd')
G.edge['ueventd']['installd']['write-read'] = '[open open][write read]'
G.edge['ueventd']['installd']['fill'] = 'red'
G.add_edge('ueventd','installd')
G.edge['ueventd']['installd']['write-read'] = '[open open][write read][append read]'
G.add_edge('ueventd','keystore')
G.edge['ueventd']['keystore']['write-read'] = '[open open][write read]'
G.edge['ueventd']['keystore']['fill'] = 'red'
G.add_edge('ueventd','keystore')
G.edge['ueventd']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('ueventd','runas')
G.edge['ueventd']['runas']['write-read'] = '[open open][write read]'
G.edge['ueventd']['runas']['fill'] = 'red'
G.add_edge('ueventd','runas')
G.edge['ueventd']['runas']['write-read'] = '[open open][write read][append read]'
G.add_edge('ueventd','servicemanager')
G.edge['ueventd']['servicemanager']['write-read'] = '[open open][write read]'
G.edge['ueventd']['servicemanager']['fill'] = 'red'
G.add_edge('ueventd','servicemanager')
G.edge['ueventd']['servicemanager']['write-read'] = '[open open][write read][append read]'
G.add_edge('ueventd','system_server')
G.edge['ueventd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['ueventd']['system_server']['fill'] = 'red'
G.add_edge('ueventd','system_server')
G.edge['ueventd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('ueventd','zygote')
G.edge['ueventd']['zygote']['write-read'] = '[open open][write read]'
G.edge['ueventd']['zygote']['fill'] = 'red'
G.add_edge('ueventd','zygote')
G.edge['ueventd']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrusteddomain','appdomain')
G.edge['untrusteddomain']['appdomain']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','init_shell')
G.edge['untrusteddomain']['init_shell']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','installd')
G.edge['untrusteddomain']['installd']['write-read'] = '[setattr getattr][open open]'
G.add_edge('untrusteddomain','keystore')
G.edge['untrusteddomain']['keystore']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','runas')
G.edge['untrusteddomain']['runas']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','servicemanager')
G.edge['untrusteddomain']['servicemanager']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open]'
G.add_edge('untrusteddomain','zygote')
G.edge['untrusteddomain']['zygote']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','appdomain')
G.edge['untrusteddomain']['appdomain']['write-read'] = '[open open][write read]'
G.edge['untrusteddomain']['appdomain']['fill'] = 'red'
G.add_edge('untrusteddomain','appdomain')
G.edge['untrusteddomain']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrusteddomain','init_shell')
G.edge['untrusteddomain']['init_shell']['write-read'] = '[open open][write read]'
G.edge['untrusteddomain']['init_shell']['fill'] = 'red'
G.add_edge('untrusteddomain','init_shell')
G.edge['untrusteddomain']['init_shell']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrusteddomain','installd')
G.edge['untrusteddomain']['installd']['write-read'] = '[setattr getattr][open open][write read]'
G.edge['untrusteddomain']['installd']['fill'] = 'red'
G.add_edge('untrusteddomain','installd')
G.edge['untrusteddomain']['installd']['write-read'] = '[setattr getattr][open open][write read][append read]'
G.add_edge('untrusteddomain','keystore')
G.edge['untrusteddomain']['keystore']['write-read'] = '[open open][write read]'
G.edge['untrusteddomain']['keystore']['fill'] = 'red'
G.add_edge('untrusteddomain','keystore')
G.edge['untrusteddomain']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrusteddomain','runas')
G.edge['untrusteddomain']['runas']['write-read'] = '[open open][write read]'
G.edge['untrusteddomain']['runas']['fill'] = 'red'
G.add_edge('untrusteddomain','runas')
G.edge['untrusteddomain']['runas']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrusteddomain','servicemanager')
G.edge['untrusteddomain']['servicemanager']['write-read'] = '[open open][write read]'
G.edge['untrusteddomain']['servicemanager']['fill'] = 'red'
G.add_edge('untrusteddomain','servicemanager')
G.edge['untrusteddomain']['servicemanager']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read]'
G.edge['untrusteddomain']['system_server']['fill'] = 'red'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read]'
G.add_edge('untrusteddomain','zygote')
G.edge['untrusteddomain']['zygote']['write-read'] = '[open open][write read]'
G.edge['untrusteddomain']['zygote']['fill'] = 'red'
G.add_edge('untrusteddomain','zygote')
G.edge['untrusteddomain']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('zygote','appdomain')
G.edge['zygote']['appdomain']['write-read'] = '[open open]'
G.add_edge('zygote','init_shell')
G.edge['zygote']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('zygote','installd')
G.edge['zygote']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('zygote','keystore')
G.edge['zygote']['keystore']['write-read'] = '[open open]'
G.add_edge('zygote','runas')
G.edge['zygote']['runas']['write-read'] = '[open open]'
G.add_edge('zygote','servicemanager')
G.edge['zygote']['servicemanager']['write-read'] = '[open open]'
G.add_edge('zygote','system_server')
G.edge['zygote']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('zygote','zygote')
G.edge['zygote']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('zygote','appdomain')
G.edge['zygote']['appdomain']['write-read'] = '[open open][write read]'
G.edge['zygote']['appdomain']['fill'] = 'red'
G.add_edge('zygote','appdomain')
G.edge['zygote']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('zygote','init_shell')
G.edge['zygote']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['zygote']['init_shell']['fill'] = 'red'
G.add_edge('zygote','init_shell')
G.edge['zygote']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('zygote','installd')
G.edge['zygote']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['zygote']['installd']['fill'] = 'red'
G.add_edge('zygote','installd')
G.edge['zygote']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('zygote','keystore')
G.edge['zygote']['keystore']['write-read'] = '[open open][write read]'
G.edge['zygote']['keystore']['fill'] = 'red'
G.add_edge('zygote','keystore')
G.edge['zygote']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('zygote','runas')
G.edge['zygote']['runas']['write-read'] = '[open open][write read]'
G.edge['zygote']['runas']['fill'] = 'red'
G.add_edge('zygote','runas')
G.edge['zygote']['runas']['write-read'] = '[open open][write read][append read]'
G.add_edge('zygote','servicemanager')
G.edge['zygote']['servicemanager']['write-read'] = '[open open][write read]'
G.edge['zygote']['servicemanager']['fill'] = 'red'
G.add_edge('zygote','servicemanager')
G.edge['zygote']['servicemanager']['write-read'] = '[open open][write read][append read]'
G.add_edge('zygote','system_server')
G.edge['zygote']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['zygote']['system_server']['fill'] = 'red'
G.add_edge('zygote','system_server')
G.edge['zygote']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('zygote','zygote')
G.edge['zygote']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['zygote']['zygote']['fill'] = 'red'
G.add_edge('zygote','zygote')
G.edge['zygote']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
app = Viewer(G)
app.mainloop()