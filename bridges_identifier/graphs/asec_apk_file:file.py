import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('carrier_app','commonplatformappdomain')
G.edge['carrier_app']['commonplatformappdomain']['write-read'] = '[open open][open open]'
G.add_edge('carrier_app','epmd')
G.edge['carrier_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open]'
G.add_edge('carrier_app','newAttr1')
G.edge['carrier_app']['newAttr1']['write-read'] = '[open open]'
G.add_edge('carrier_app','platform_app')
G.edge['carrier_app']['platform_app']['write-read'] = '[open open]'
G.add_edge('carrier_app','s_platform_app')
G.edge['carrier_app']['s_platform_app']['write-read'] = '[open open]'
G.add_edge('carrier_app','system_server')
G.edge['carrier_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open]'
G.add_edge('carrier_app','vold')
G.edge['carrier_app']['vold']['write-read'] = '[open open]'
G.add_edge('carrier_app','vold')
G.edge['carrier_app']['vold']['write-read'] = '[open open][open open]'
G.add_edge('carrier_app','commonplatformappdomain')
G.edge['carrier_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('carrier_app','epmd')
G.edge['carrier_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('carrier_app','newAttr1')
G.edge['carrier_app']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','platform_app')
G.edge['carrier_app']['platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','s_platform_app')
G.edge['carrier_app']['s_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','system_server')
G.edge['carrier_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr]'
G.add_edge('carrier_app','vold')
G.edge['carrier_app']['vold']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('carrier_app','vold')
G.edge['carrier_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('carrier_app','commonplatformappdomain')
G.edge['carrier_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['carrier_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('carrier_app','commonplatformappdomain')
G.edge['carrier_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','drmserver')
G.edge['carrier_app']['drmserver']['write-read'] = '[write read]'
G.edge['carrier_app']['drmserver']['fill'] = 'red'
G.add_edge('carrier_app','epmd')
G.edge['carrier_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['carrier_app']['epmd']['fill'] = 'red'
G.add_edge('carrier_app','epmd')
G.edge['carrier_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','newAttr1')
G.edge['carrier_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['carrier_app']['newAttr1']['fill'] = 'red'
G.add_edge('carrier_app','newAttr1')
G.edge['carrier_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','platform_app')
G.edge['carrier_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['carrier_app']['platform_app']['fill'] = 'red'
G.add_edge('carrier_app','platform_app')
G.edge['carrier_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','s_platform_app')
G.edge['carrier_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['carrier_app']['s_platform_app']['fill'] = 'red'
G.add_edge('carrier_app','s_platform_app')
G.edge['carrier_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','system_server')
G.edge['carrier_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read]'
G.edge['carrier_app']['system_server']['fill'] = 'red'
G.add_edge('carrier_app','system_server')
G.edge['carrier_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','vold')
G.edge['carrier_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['carrier_app']['vold']['fill'] = 'red'
G.add_edge('carrier_app','vold')
G.edge['carrier_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('commonplatformappdomain','epmd')
G.edge['commonplatformappdomain']['epmd']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','newAttr1')
G.edge['commonplatformappdomain']['newAttr1']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','platform_app')
G.edge['commonplatformappdomain']['platform_app']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','s_platform_app')
G.edge['commonplatformappdomain']['s_platform_app']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','system_server')
G.edge['commonplatformappdomain']['system_server']['write-read'] = '[write read][append read][open open][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('commonplatformappdomain','vold')
G.edge['commonplatformappdomain']['vold']['write-read'] = '[write read][append read][open open]'
G.add_edge('commonplatformappdomain','vold')
G.edge['commonplatformappdomain']['vold']['write-read'] = '[write read][append read][open open][open open]'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','epmd')
G.edge['commonplatformappdomain']['epmd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','newAttr1')
G.edge['commonplatformappdomain']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','platform_app')
G.edge['commonplatformappdomain']['platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','s_platform_app')
G.edge['commonplatformappdomain']['s_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','system_server')
G.edge['commonplatformappdomain']['system_server']['write-read'] = '[write read][append read][open open][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','vold')
G.edge['commonplatformappdomain']['vold']['write-read'] = '[write read][append read][open open][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','vold')
G.edge['commonplatformappdomain']['vold']['write-read'] = '[write read][append read][open open][open open][setattr getattr][setattr getattr]'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','drmserver')
G.edge['commonplatformappdomain']['drmserver']['write-read'] = '[write read]'
G.edge['commonplatformappdomain']['drmserver']['fill'] = 'red'
G.add_edge('commonplatformappdomain','epmd')
G.edge['commonplatformappdomain']['epmd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['epmd']['fill'] = 'red'
G.add_edge('commonplatformappdomain','epmd')
G.edge['commonplatformappdomain']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','newAttr1')
G.edge['commonplatformappdomain']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['newAttr1']['fill'] = 'red'
G.add_edge('commonplatformappdomain','newAttr1')
G.edge['commonplatformappdomain']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','platform_app')
G.edge['commonplatformappdomain']['platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['platform_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','platform_app')
G.edge['commonplatformappdomain']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','s_platform_app')
G.edge['commonplatformappdomain']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['s_platform_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','s_platform_app')
G.edge['commonplatformappdomain']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','system_server')
G.edge['commonplatformappdomain']['system_server']['write-read'] = '[write read][append read][open open][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['system_server']['fill'] = 'red'
G.add_edge('commonplatformappdomain','system_server')
G.edge['commonplatformappdomain']['system_server']['write-read'] = '[write read][append read][open open][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','vold')
G.edge['commonplatformappdomain']['vold']['write-read'] = '[write read][append read][open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['commonplatformappdomain']['vold']['fill'] = 'red'
G.add_edge('commonplatformappdomain','vold')
G.edge['commonplatformappdomain']['vold']['write-read'] = '[write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('dex2oat','commonplatformappdomain')
G.edge['dex2oat']['commonplatformappdomain']['write-read'] = '[write read]'
G.edge['dex2oat']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('dex2oat','commonplatformappdomain')
G.edge['dex2oat']['commonplatformappdomain']['write-read'] = '[write read][append read]'
G.add_edge('dex2oat','drmserver')
G.edge['dex2oat']['drmserver']['write-read'] = '[write read]'
G.edge['dex2oat']['drmserver']['fill'] = 'red'
G.add_edge('dex2oat','epmd')
G.edge['dex2oat']['epmd']['write-read'] = '[write read]'
G.edge['dex2oat']['epmd']['fill'] = 'red'
G.add_edge('dex2oat','epmd')
G.edge['dex2oat']['epmd']['write-read'] = '[write read][append read]'
G.add_edge('dex2oat','newAttr1')
G.edge['dex2oat']['newAttr1']['write-read'] = '[write read]'
G.edge['dex2oat']['newAttr1']['fill'] = 'red'
G.add_edge('dex2oat','newAttr1')
G.edge['dex2oat']['newAttr1']['write-read'] = '[write read][append read]'
G.add_edge('dex2oat','platform_app')
G.edge['dex2oat']['platform_app']['write-read'] = '[write read]'
G.edge['dex2oat']['platform_app']['fill'] = 'red'
G.add_edge('dex2oat','platform_app')
G.edge['dex2oat']['platform_app']['write-read'] = '[write read][append read]'
G.add_edge('dex2oat','s_platform_app')
G.edge['dex2oat']['s_platform_app']['write-read'] = '[write read]'
G.edge['dex2oat']['s_platform_app']['fill'] = 'red'
G.add_edge('dex2oat','s_platform_app')
G.edge['dex2oat']['s_platform_app']['write-read'] = '[write read][append read]'
G.add_edge('dex2oat','system_server')
G.edge['dex2oat']['system_server']['write-read'] = '[write read]'
G.edge['dex2oat']['system_server']['fill'] = 'red'
G.add_edge('dex2oat','system_server')
G.edge['dex2oat']['system_server']['write-read'] = '[write read][append read]'
G.add_edge('dex2oat','vold')
G.edge['dex2oat']['vold']['write-read'] = '[write read]'
G.edge['dex2oat']['vold']['fill'] = 'red'
G.add_edge('dex2oat','vold')
G.edge['dex2oat']['vold']['write-read'] = '[write read][append read]'
G.add_edge('drmserver','commonplatformappdomain')
G.edge['drmserver']['commonplatformappdomain']['write-read'] = '[setattr getattr]'
G.add_edge('drmserver','epmd')
G.edge['drmserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('drmserver','newAttr1')
G.edge['drmserver']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('drmserver','platform_app')
G.edge['drmserver']['platform_app']['write-read'] = '[setattr getattr]'
G.add_edge('drmserver','s_platform_app')
G.edge['drmserver']['s_platform_app']['write-read'] = '[setattr getattr]'
G.add_edge('drmserver','system_server')
G.edge['drmserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('drmserver','vold')
G.edge['drmserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('drmserver','vold')
G.edge['drmserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('drmserver','commonplatformappdomain')
G.edge['drmserver']['commonplatformappdomain']['write-read'] = '[setattr getattr][write read]'
G.edge['drmserver']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('drmserver','commonplatformappdomain')
G.edge['drmserver']['commonplatformappdomain']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('drmserver','drmserver')
G.edge['drmserver']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['drmserver']['drmserver']['fill'] = 'red'
G.add_edge('drmserver','epmd')
G.edge['drmserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['drmserver']['epmd']['fill'] = 'red'
G.add_edge('drmserver','epmd')
G.edge['drmserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read]'
G.add_edge('drmserver','newAttr1')
G.edge['drmserver']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['drmserver']['newAttr1']['fill'] = 'red'
G.add_edge('drmserver','newAttr1')
G.edge['drmserver']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][append read]'
G.add_edge('drmserver','platform_app')
G.edge['drmserver']['platform_app']['write-read'] = '[setattr getattr][write read]'
G.edge['drmserver']['platform_app']['fill'] = 'red'
G.add_edge('drmserver','platform_app')
G.edge['drmserver']['platform_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('drmserver','s_platform_app')
G.edge['drmserver']['s_platform_app']['write-read'] = '[setattr getattr][write read]'
G.edge['drmserver']['s_platform_app']['fill'] = 'red'
G.add_edge('drmserver','s_platform_app')
G.edge['drmserver']['s_platform_app']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('drmserver','system_server')
G.edge['drmserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['drmserver']['system_server']['fill'] = 'red'
G.add_edge('drmserver','system_server')
G.edge['drmserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][append read]'
G.add_edge('drmserver','vold')
G.edge['drmserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read]'
G.edge['drmserver']['vold']['fill'] = 'red'
G.add_edge('drmserver','vold')
G.edge['drmserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('drmserver','commonplatformappdomain')
G.edge['drmserver']['commonplatformappdomain']['write-read'] = '[setattr getattr][write read][append read][setattr getattr]'
G.add_edge('drmserver','epmd')
G.edge['drmserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('drmserver','newAttr1')
G.edge['drmserver']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('drmserver','platform_app')
G.edge['drmserver']['platform_app']['write-read'] = '[setattr getattr][write read][append read][setattr getattr]'
G.add_edge('drmserver','s_platform_app')
G.edge['drmserver']['s_platform_app']['write-read'] = '[setattr getattr][write read][append read][setattr getattr]'
G.add_edge('drmserver','system_server')
G.edge['drmserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('drmserver','vold')
G.edge['drmserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('drmserver','vold')
G.edge['drmserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr]'
G.add_edge('drmserver','commonplatformappdomain')
G.edge['drmserver']['commonplatformappdomain']['write-read'] = '[setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['drmserver']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('drmserver','commonplatformappdomain')
G.edge['drmserver']['commonplatformappdomain']['write-read'] = '[setattr getattr][write read][append read][setattr getattr][write read][append read]'
G.add_edge('drmserver','drmserver')
G.edge['drmserver']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['drmserver']['drmserver']['fill'] = 'red'
G.add_edge('drmserver','epmd')
G.edge['drmserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['drmserver']['epmd']['fill'] = 'red'
G.add_edge('drmserver','epmd')
G.edge['drmserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setattr getattr][write read][append read]'
G.add_edge('drmserver','newAttr1')
G.edge['drmserver']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['drmserver']['newAttr1']['fill'] = 'red'
G.add_edge('drmserver','newAttr1')
G.edge['drmserver']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setattr getattr][write read][append read]'
G.add_edge('drmserver','platform_app')
G.edge['drmserver']['platform_app']['write-read'] = '[setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['drmserver']['platform_app']['fill'] = 'red'
G.add_edge('drmserver','platform_app')
G.edge['drmserver']['platform_app']['write-read'] = '[setattr getattr][write read][append read][setattr getattr][write read][append read]'
G.add_edge('drmserver','s_platform_app')
G.edge['drmserver']['s_platform_app']['write-read'] = '[setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['drmserver']['s_platform_app']['fill'] = 'red'
G.add_edge('drmserver','s_platform_app')
G.edge['drmserver']['s_platform_app']['write-read'] = '[setattr getattr][write read][append read][setattr getattr][write read][append read]'
G.add_edge('drmserver','system_server')
G.edge['drmserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['drmserver']['system_server']['fill'] = 'red'
G.add_edge('drmserver','system_server')
G.edge['drmserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setattr getattr][write read][append read]'
G.add_edge('drmserver','vold')
G.edge['drmserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read]'
G.edge['drmserver']['vold']['fill'] = 'red'
G.add_edge('drmserver','vold')
G.edge['drmserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('epmd','commonplatformappdomain')
G.edge['epmd']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('epmd','newAttr1')
G.edge['epmd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('epmd','platform_app')
G.edge['epmd']['platform_app']['write-read'] = '[open open]'
G.add_edge('epmd','s_platform_app')
G.edge['epmd']['s_platform_app']['write-read'] = '[open open]'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open]'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('epmd','commonplatformappdomain')
G.edge['epmd']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('epmd','newAttr1')
G.edge['epmd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('epmd','platform_app')
G.edge['epmd']['platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('epmd','s_platform_app')
G.edge['epmd']['s_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr]'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr]'
G.add_edge('epmd','commonplatformappdomain')
G.edge['epmd']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['epmd']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('epmd','commonplatformappdomain')
G.edge['epmd']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('epmd','drmserver')
G.edge['epmd']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read]'
G.edge['epmd']['drmserver']['fill'] = 'red'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['epmd']['epmd']['fill'] = 'red'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('epmd','newAttr1')
G.edge['epmd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['epmd']['newAttr1']['fill'] = 'red'
G.add_edge('epmd','newAttr1')
G.edge['epmd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('epmd','platform_app')
G.edge['epmd']['platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['epmd']['platform_app']['fill'] = 'red'
G.add_edge('epmd','platform_app')
G.edge['epmd']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('epmd','s_platform_app')
G.edge['epmd']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['epmd']['s_platform_app']['fill'] = 'red'
G.add_edge('epmd','s_platform_app')
G.edge['epmd']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read]'
G.edge['epmd']['system_server']['fill'] = 'red'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['epmd']['vold']['fill'] = 'red'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','commonplatformappdomain')
G.edge['filtered_google_app']['commonplatformappdomain']['write-read'] = '[open open][open open]'
G.add_edge('filtered_google_app','epmd')
G.edge['filtered_google_app']['epmd']['write-read'] = '[setattr getattr][setattr getattr][write read][append read][open open]'
G.add_edge('filtered_google_app','newAttr1')
G.edge['filtered_google_app']['newAttr1']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','platform_app')
G.edge['filtered_google_app']['platform_app']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','s_platform_app')
G.edge['filtered_google_app']['s_platform_app']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','system_server')
G.edge['filtered_google_app']['system_server']['write-read'] = '[setattr getattr][setattr getattr][write read][write read][append read][open open]'
G.add_edge('filtered_google_app','vold')
G.edge['filtered_google_app']['vold']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','vold')
G.edge['filtered_google_app']['vold']['write-read'] = '[open open][open open]'
G.add_edge('filtered_google_app','commonplatformappdomain')
G.edge['filtered_google_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('filtered_google_app','epmd')
G.edge['filtered_google_app']['epmd']['write-read'] = '[setattr getattr][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('filtered_google_app','newAttr1')
G.edge['filtered_google_app']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','platform_app')
G.edge['filtered_google_app']['platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','s_platform_app')
G.edge['filtered_google_app']['s_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','system_server')
G.edge['filtered_google_app']['system_server']['write-read'] = '[setattr getattr][setattr getattr][write read][write read][append read][open open][setattr getattr]'
G.add_edge('filtered_google_app','vold')
G.edge['filtered_google_app']['vold']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('filtered_google_app','vold')
G.edge['filtered_google_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('filtered_google_app','commonplatformappdomain')
G.edge['filtered_google_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['filtered_google_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('filtered_google_app','commonplatformappdomain')
G.edge['filtered_google_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','drmserver')
G.edge['filtered_google_app']['drmserver']['write-read'] = '[write read]'
G.edge['filtered_google_app']['drmserver']['fill'] = 'red'
G.add_edge('filtered_google_app','epmd')
G.edge['filtered_google_app']['epmd']['write-read'] = '[setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['filtered_google_app']['epmd']['fill'] = 'red'
G.add_edge('filtered_google_app','epmd')
G.edge['filtered_google_app']['epmd']['write-read'] = '[setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','newAttr1')
G.edge['filtered_google_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_google_app']['newAttr1']['fill'] = 'red'
G.add_edge('filtered_google_app','newAttr1')
G.edge['filtered_google_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','platform_app')
G.edge['filtered_google_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_google_app']['platform_app']['fill'] = 'red'
G.add_edge('filtered_google_app','platform_app')
G.edge['filtered_google_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','s_platform_app')
G.edge['filtered_google_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_google_app']['s_platform_app']['fill'] = 'red'
G.add_edge('filtered_google_app','s_platform_app')
G.edge['filtered_google_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','system_server')
G.edge['filtered_google_app']['system_server']['write-read'] = '[setattr getattr][setattr getattr][write read][write read][append read][open open][setattr getattr][write read]'
G.edge['filtered_google_app']['system_server']['fill'] = 'red'
G.add_edge('filtered_google_app','system_server')
G.edge['filtered_google_app']['system_server']['write-read'] = '[setattr getattr][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_google_app','vold')
G.edge['filtered_google_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['filtered_google_app']['vold']['fill'] = 'red'
G.add_edge('filtered_google_app','vold')
G.edge['filtered_google_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','commonplatformappdomain')
G.edge['filtered_untrusted_app']['commonplatformappdomain']['write-read'] = '[open open][open open]'
G.add_edge('filtered_untrusted_app','epmd')
G.edge['filtered_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open]'
G.add_edge('filtered_untrusted_app','newAttr1')
G.edge['filtered_untrusted_app']['newAttr1']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','platform_app')
G.edge['filtered_untrusted_app']['platform_app']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','s_platform_app')
G.edge['filtered_untrusted_app']['s_platform_app']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','system_server')
G.edge['filtered_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open]'
G.add_edge('filtered_untrusted_app','vold')
G.edge['filtered_untrusted_app']['vold']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','vold')
G.edge['filtered_untrusted_app']['vold']['write-read'] = '[open open][open open]'
G.add_edge('filtered_untrusted_app','commonplatformappdomain')
G.edge['filtered_untrusted_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','epmd')
G.edge['filtered_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','newAttr1')
G.edge['filtered_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','platform_app')
G.edge['filtered_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','s_platform_app')
G.edge['filtered_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','system_server')
G.edge['filtered_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','vold')
G.edge['filtered_untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','vold')
G.edge['filtered_untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('filtered_untrusted_app','commonplatformappdomain')
G.edge['filtered_untrusted_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','commonplatformappdomain')
G.edge['filtered_untrusted_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','drmserver')
G.edge['filtered_untrusted_app']['drmserver']['write-read'] = '[write read]'
G.edge['filtered_untrusted_app']['drmserver']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','epmd')
G.edge['filtered_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['epmd']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','epmd')
G.edge['filtered_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','newAttr1')
G.edge['filtered_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['newAttr1']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','newAttr1')
G.edge['filtered_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','platform_app')
G.edge['filtered_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['platform_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','platform_app')
G.edge['filtered_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','s_platform_app')
G.edge['filtered_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['s_platform_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','s_platform_app')
G.edge['filtered_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','system_server')
G.edge['filtered_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','system_server')
G.edge['filtered_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('filtered_untrusted_app','vold')
G.edge['filtered_untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['vold']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','vold')
G.edge['filtered_untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','commonplatformappdomain')
G.edge['gad_untrusted_app']['commonplatformappdomain']['write-read'] = '[open open][open open]'
G.add_edge('gad_untrusted_app','epmd')
G.edge['gad_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open]'
G.add_edge('gad_untrusted_app','newAttr1')
G.edge['gad_untrusted_app']['newAttr1']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','platform_app')
G.edge['gad_untrusted_app']['platform_app']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','s_platform_app')
G.edge['gad_untrusted_app']['s_platform_app']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','system_server')
G.edge['gad_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open]'
G.add_edge('gad_untrusted_app','vold')
G.edge['gad_untrusted_app']['vold']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','vold')
G.edge['gad_untrusted_app']['vold']['write-read'] = '[open open][open open]'
G.add_edge('gad_untrusted_app','commonplatformappdomain')
G.edge['gad_untrusted_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('gad_untrusted_app','epmd')
G.edge['gad_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('gad_untrusted_app','newAttr1')
G.edge['gad_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','platform_app')
G.edge['gad_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','s_platform_app')
G.edge['gad_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','system_server')
G.edge['gad_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr]'
G.add_edge('gad_untrusted_app','vold')
G.edge['gad_untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('gad_untrusted_app','vold')
G.edge['gad_untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('gad_untrusted_app','commonplatformappdomain')
G.edge['gad_untrusted_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('gad_untrusted_app','commonplatformappdomain')
G.edge['gad_untrusted_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','drmserver')
G.edge['gad_untrusted_app']['drmserver']['write-read'] = '[write read]'
G.edge['gad_untrusted_app']['drmserver']['fill'] = 'red'
G.add_edge('gad_untrusted_app','epmd')
G.edge['gad_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['epmd']['fill'] = 'red'
G.add_edge('gad_untrusted_app','epmd')
G.edge['gad_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','newAttr1')
G.edge['gad_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['newAttr1']['fill'] = 'red'
G.add_edge('gad_untrusted_app','newAttr1')
G.edge['gad_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','platform_app')
G.edge['gad_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['platform_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','platform_app')
G.edge['gad_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','s_platform_app')
G.edge['gad_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['s_platform_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','s_platform_app')
G.edge['gad_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','system_server')
G.edge['gad_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('gad_untrusted_app','system_server')
G.edge['gad_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','vold')
G.edge['gad_untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['gad_untrusted_app']['vold']['fill'] = 'red'
G.add_edge('gad_untrusted_app','vold')
G.edge['gad_untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('ime_app','commonplatformappdomain')
G.edge['ime_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','epmd')
G.edge['ime_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open]'
G.add_edge('ime_app','newAttr1')
G.edge['ime_app']['newAttr1']['write-read'] = '[open open]'
G.add_edge('ime_app','platform_app')
G.edge['ime_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','s_platform_app')
G.edge['ime_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open]'
G.add_edge('ime_app','vold')
G.edge['ime_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','vold')
G.edge['ime_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('ime_app','commonplatformappdomain')
G.edge['ime_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ime_app','epmd')
G.edge['ime_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr]'
G.add_edge('ime_app','newAttr1')
G.edge['ime_app']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','platform_app')
G.edge['ime_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ime_app','s_platform_app')
G.edge['ime_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','vold')
G.edge['ime_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('ime_app','vold')
G.edge['ime_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr]'
G.add_edge('ime_app','commonplatformappdomain')
G.edge['ime_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ime_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('ime_app','commonplatformappdomain')
G.edge['ime_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','drmserver')
G.edge['ime_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['ime_app']['drmserver']['fill'] = 'red'
G.add_edge('ime_app','epmd')
G.edge['ime_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read]'
G.edge['ime_app']['epmd']['fill'] = 'red'
G.add_edge('ime_app','epmd')
G.edge['ime_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','newAttr1')
G.edge['ime_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['newAttr1']['fill'] = 'red'
G.add_edge('ime_app','newAttr1')
G.edge['ime_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','platform_app')
G.edge['ime_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ime_app']['platform_app']['fill'] = 'red'
G.add_edge('ime_app','platform_app')
G.edge['ime_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','s_platform_app')
G.edge['ime_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ime_app']['s_platform_app']['fill'] = 'red'
G.add_edge('ime_app','s_platform_app')
G.edge['ime_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['system_server']['fill'] = 'red'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','vold')
G.edge['ime_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['ime_app']['vold']['fill'] = 'red'
G.add_edge('ime_app','vold')
G.edge['ime_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('installd','commonplatformappdomain')
G.edge['installd']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('installd','epmd')
G.edge['installd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open]'
G.add_edge('installd','newAttr1')
G.edge['installd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('installd','platform_app')
G.edge['installd']['platform_app']['write-read'] = '[open open]'
G.add_edge('installd','s_platform_app')
G.edge['installd']['s_platform_app']['write-read'] = '[open open]'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][add_name search][remove_name search][setattr getattr][open open][write read][append read][open open]'
G.add_edge('installd','vold')
G.edge['installd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('installd','vold')
G.edge['installd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('installd','commonplatformappdomain')
G.edge['installd']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('installd','epmd')
G.edge['installd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr]'
G.add_edge('installd','newAttr1')
G.edge['installd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('installd','platform_app')
G.edge['installd']['platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','s_platform_app')
G.edge['installd']['s_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][add_name search][remove_name search][setattr getattr][open open][write read][append read][open open][setattr getattr]'
G.add_edge('installd','vold')
G.edge['installd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('installd','vold')
G.edge['installd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr]'
G.add_edge('installd','commonplatformappdomain')
G.edge['installd']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['installd']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('installd','commonplatformappdomain')
G.edge['installd']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('installd','drmserver')
G.edge['installd']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['installd']['drmserver']['fill'] = 'red'
G.add_edge('installd','epmd')
G.edge['installd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read]'
G.edge['installd']['epmd']['fill'] = 'red'
G.add_edge('installd','epmd')
G.edge['installd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read]'
G.add_edge('installd','newAttr1')
G.edge['installd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['installd']['newAttr1']['fill'] = 'red'
G.add_edge('installd','newAttr1')
G.edge['installd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('installd','platform_app')
G.edge['installd']['platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['platform_app']['fill'] = 'red'
G.add_edge('installd','platform_app')
G.edge['installd']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('installd','s_platform_app')
G.edge['installd']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['s_platform_app']['fill'] = 'red'
G.add_edge('installd','s_platform_app')
G.edge['installd']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][add_name search][remove_name search][setattr getattr][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['installd']['system_server']['fill'] = 'red'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][write read][add_name search][remove_name search][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('installd','vold')
G.edge['installd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['installd']['vold']['fill'] = 'red'
G.add_edge('installd','vold')
G.edge['installd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('irm_app','commonplatformappdomain')
G.edge['irm_app']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('irm_app','epmd')
G.edge['irm_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open]'
G.add_edge('irm_app','newAttr1')
G.edge['irm_app']['newAttr1']['write-read'] = '[open open]'
G.add_edge('irm_app','platform_app')
G.edge['irm_app']['platform_app']['write-read'] = '[open open]'
G.add_edge('irm_app','s_platform_app')
G.edge['irm_app']['s_platform_app']['write-read'] = '[open open]'
G.add_edge('irm_app','system_server')
G.edge['irm_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open]'
G.add_edge('irm_app','vold')
G.edge['irm_app']['vold']['write-read'] = '[open open]'
G.add_edge('irm_app','vold')
G.edge['irm_app']['vold']['write-read'] = '[open open][open open]'
G.add_edge('irm_app','commonplatformappdomain')
G.edge['irm_app']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('irm_app','epmd')
G.edge['irm_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('irm_app','newAttr1')
G.edge['irm_app']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','platform_app')
G.edge['irm_app']['platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','s_platform_app')
G.edge['irm_app']['s_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','system_server')
G.edge['irm_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr]'
G.add_edge('irm_app','vold')
G.edge['irm_app']['vold']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('irm_app','vold')
G.edge['irm_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('irm_app','commonplatformappdomain')
G.edge['irm_app']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['irm_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('irm_app','commonplatformappdomain')
G.edge['irm_app']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','drmserver')
G.edge['irm_app']['drmserver']['write-read'] = '[write read]'
G.edge['irm_app']['drmserver']['fill'] = 'red'
G.add_edge('irm_app','epmd')
G.edge['irm_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['irm_app']['epmd']['fill'] = 'red'
G.add_edge('irm_app','epmd')
G.edge['irm_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','newAttr1')
G.edge['irm_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_app']['newAttr1']['fill'] = 'red'
G.add_edge('irm_app','newAttr1')
G.edge['irm_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','platform_app')
G.edge['irm_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_app']['platform_app']['fill'] = 'red'
G.add_edge('irm_app','platform_app')
G.edge['irm_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','s_platform_app')
G.edge['irm_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_app']['s_platform_app']['fill'] = 'red'
G.add_edge('irm_app','s_platform_app')
G.edge['irm_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','system_server')
G.edge['irm_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read]'
G.edge['irm_app']['system_server']['fill'] = 'red'
G.add_edge('irm_app','system_server')
G.edge['irm_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','vold')
G.edge['irm_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['irm_app']['vold']['fill'] = 'red'
G.add_edge('irm_app','vold')
G.edge['irm_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','commonplatformappdomain')
G.edge['knox_untrusted_app']['commonplatformappdomain']['write-read'] = '[open open][open open]'
G.add_edge('knox_untrusted_app','epmd')
G.edge['knox_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open]'
G.add_edge('knox_untrusted_app','newAttr1')
G.edge['knox_untrusted_app']['newAttr1']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','platform_app')
G.edge['knox_untrusted_app']['platform_app']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','s_platform_app')
G.edge['knox_untrusted_app']['s_platform_app']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','system_server')
G.edge['knox_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open]'
G.add_edge('knox_untrusted_app','vold')
G.edge['knox_untrusted_app']['vold']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','vold')
G.edge['knox_untrusted_app']['vold']['write-read'] = '[open open][open open]'
G.add_edge('knox_untrusted_app','commonplatformappdomain')
G.edge['knox_untrusted_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('knox_untrusted_app','epmd')
G.edge['knox_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('knox_untrusted_app','newAttr1')
G.edge['knox_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','platform_app')
G.edge['knox_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','s_platform_app')
G.edge['knox_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','system_server')
G.edge['knox_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr]'
G.add_edge('knox_untrusted_app','vold')
G.edge['knox_untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('knox_untrusted_app','vold')
G.edge['knox_untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('knox_untrusted_app','commonplatformappdomain')
G.edge['knox_untrusted_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('knox_untrusted_app','commonplatformappdomain')
G.edge['knox_untrusted_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','drmserver')
G.edge['knox_untrusted_app']['drmserver']['write-read'] = '[write read]'
G.edge['knox_untrusted_app']['drmserver']['fill'] = 'red'
G.add_edge('knox_untrusted_app','epmd')
G.edge['knox_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['epmd']['fill'] = 'red'
G.add_edge('knox_untrusted_app','epmd')
G.edge['knox_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','newAttr1')
G.edge['knox_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['newAttr1']['fill'] = 'red'
G.add_edge('knox_untrusted_app','newAttr1')
G.edge['knox_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','platform_app')
G.edge['knox_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['platform_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','platform_app')
G.edge['knox_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','s_platform_app')
G.edge['knox_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['s_platform_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','s_platform_app')
G.edge['knox_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','system_server')
G.edge['knox_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('knox_untrusted_app','system_server')
G.edge['knox_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','vold')
G.edge['knox_untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['knox_untrusted_app']['vold']['fill'] = 'red'
G.add_edge('knox_untrusted_app','vold')
G.edge['knox_untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','commonplatformappdomain')
G.edge['llk_untrusted_app']['commonplatformappdomain']['write-read'] = '[open open][open open]'
G.add_edge('llk_untrusted_app','epmd')
G.edge['llk_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open]'
G.add_edge('llk_untrusted_app','newAttr1')
G.edge['llk_untrusted_app']['newAttr1']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','platform_app')
G.edge['llk_untrusted_app']['platform_app']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','s_platform_app')
G.edge['llk_untrusted_app']['s_platform_app']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','system_server')
G.edge['llk_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open]'
G.add_edge('llk_untrusted_app','vold')
G.edge['llk_untrusted_app']['vold']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','vold')
G.edge['llk_untrusted_app']['vold']['write-read'] = '[open open][open open]'
G.add_edge('llk_untrusted_app','commonplatformappdomain')
G.edge['llk_untrusted_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('llk_untrusted_app','epmd')
G.edge['llk_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('llk_untrusted_app','newAttr1')
G.edge['llk_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','platform_app')
G.edge['llk_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','s_platform_app')
G.edge['llk_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','system_server')
G.edge['llk_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr]'
G.add_edge('llk_untrusted_app','vold')
G.edge['llk_untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('llk_untrusted_app','vold')
G.edge['llk_untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('llk_untrusted_app','commonplatformappdomain')
G.edge['llk_untrusted_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('llk_untrusted_app','commonplatformappdomain')
G.edge['llk_untrusted_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','drmserver')
G.edge['llk_untrusted_app']['drmserver']['write-read'] = '[write read]'
G.edge['llk_untrusted_app']['drmserver']['fill'] = 'red'
G.add_edge('llk_untrusted_app','epmd')
G.edge['llk_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['epmd']['fill'] = 'red'
G.add_edge('llk_untrusted_app','epmd')
G.edge['llk_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','newAttr1')
G.edge['llk_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['newAttr1']['fill'] = 'red'
G.add_edge('llk_untrusted_app','newAttr1')
G.edge['llk_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','platform_app')
G.edge['llk_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['platform_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','platform_app')
G.edge['llk_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','s_platform_app')
G.edge['llk_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['s_platform_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','s_platform_app')
G.edge['llk_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','system_server')
G.edge['llk_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('llk_untrusted_app','system_server')
G.edge['llk_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('llk_untrusted_app','vold')
G.edge['llk_untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['llk_untrusted_app']['vold']['fill'] = 'red'
G.add_edge('llk_untrusted_app','vold')
G.edge['llk_untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('mediaserver','commonplatformappdomain')
G.edge['mediaserver']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','newAttr1')
G.edge['mediaserver']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','platform_app')
G.edge['mediaserver']['platform_app']['write-read'] = '[open open]'
G.add_edge('mediaserver','s_platform_app')
G.edge['mediaserver']['s_platform_app']['write-read'] = '[open open]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open]'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('mediaserver','commonplatformappdomain')
G.edge['mediaserver']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('mediaserver','newAttr1')
G.edge['mediaserver']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','platform_app')
G.edge['mediaserver']['platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','s_platform_app')
G.edge['mediaserver']['s_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr]'
G.add_edge('mediaserver','commonplatformappdomain')
G.edge['mediaserver']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('mediaserver','commonplatformappdomain')
G.edge['mediaserver']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','drmserver')
G.edge['mediaserver']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read]'
G.edge['mediaserver']['drmserver']['fill'] = 'red'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['mediaserver']['epmd']['fill'] = 'red'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','newAttr1')
G.edge['mediaserver']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['newAttr1']['fill'] = 'red'
G.add_edge('mediaserver','newAttr1')
G.edge['mediaserver']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','platform_app')
G.edge['mediaserver']['platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['platform_app']['fill'] = 'red'
G.add_edge('mediaserver','platform_app')
G.edge['mediaserver']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','s_platform_app')
G.edge['mediaserver']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['s_platform_app']['fill'] = 'red'
G.add_edge('mediaserver','s_platform_app')
G.edge['mediaserver']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['system_server']['fill'] = 'red'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['mediaserver']['vold']['fill'] = 'red'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('mediaserver','commonplatformappdomain')
G.edge['mediaserver']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('mediaserver','newAttr1')
G.edge['mediaserver']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('mediaserver','platform_app')
G.edge['mediaserver']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('mediaserver','s_platform_app')
G.edge['mediaserver']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr]'
G.add_edge('mediaserver','commonplatformappdomain')
G.edge['mediaserver']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['mediaserver']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('mediaserver','commonplatformappdomain')
G.edge['mediaserver']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][append read]'
G.add_edge('mediaserver','drmserver')
G.edge['mediaserver']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][write read]'
G.edge['mediaserver']['drmserver']['fill'] = 'red'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['mediaserver']['epmd']['fill'] = 'red'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read]'
G.add_edge('mediaserver','newAttr1')
G.edge['mediaserver']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['mediaserver']['newAttr1']['fill'] = 'red'
G.add_edge('mediaserver','newAttr1')
G.edge['mediaserver']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read]'
G.add_edge('mediaserver','platform_app')
G.edge['mediaserver']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['mediaserver']['platform_app']['fill'] = 'red'
G.add_edge('mediaserver','platform_app')
G.edge['mediaserver']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][append read]'
G.add_edge('mediaserver','s_platform_app')
G.edge['mediaserver']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['mediaserver']['s_platform_app']['fill'] = 'red'
G.add_edge('mediaserver','s_platform_app')
G.edge['mediaserver']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][append read]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['mediaserver']['system_server']['fill'] = 'red'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read]'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read]'
G.edge['mediaserver']['vold']['fill'] = 'red'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('newAttr1','commonplatformappdomain')
G.edge['newAttr1']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('newAttr1','epmd')
G.edge['newAttr1']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open]'
G.add_edge('newAttr1','platform_app')
G.edge['newAttr1']['platform_app']['write-read'] = '[open open]'
G.add_edge('newAttr1','s_platform_app')
G.edge['newAttr1']['s_platform_app']['write-read'] = '[open open]'
G.add_edge('newAttr1','system_server')
G.edge['newAttr1']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('newAttr1','vold')
G.edge['newAttr1']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('newAttr1','vold')
G.edge['newAttr1']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('newAttr1','commonplatformappdomain')
G.edge['newAttr1']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr1','epmd')
G.edge['newAttr1']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr]'
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr]'
G.add_edge('newAttr1','platform_app')
G.edge['newAttr1']['platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr1','s_platform_app')
G.edge['newAttr1']['s_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr1','system_server')
G.edge['newAttr1']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('newAttr1','vold')
G.edge['newAttr1']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('newAttr1','vold')
G.edge['newAttr1']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr]'
G.add_edge('newAttr1','commonplatformappdomain')
G.edge['newAttr1']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr1']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('newAttr1','commonplatformappdomain')
G.edge['newAttr1']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','drmserver')
G.edge['newAttr1']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['newAttr1']['drmserver']['fill'] = 'red'
G.add_edge('newAttr1','epmd')
G.edge['newAttr1']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read]'
G.edge['newAttr1']['epmd']['fill'] = 'red'
G.add_edge('newAttr1','epmd')
G.edge['newAttr1']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read]'
G.edge['newAttr1']['newAttr1']['fill'] = 'red'
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','platform_app')
G.edge['newAttr1']['platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr1']['platform_app']['fill'] = 'red'
G.add_edge('newAttr1','platform_app')
G.edge['newAttr1']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','s_platform_app')
G.edge['newAttr1']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr1']['s_platform_app']['fill'] = 'red'
G.add_edge('newAttr1','s_platform_app')
G.edge['newAttr1']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','system_server')
G.edge['newAttr1']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['newAttr1']['system_server']['fill'] = 'red'
G.add_edge('newAttr1','system_server')
G.edge['newAttr1']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','vold')
G.edge['newAttr1']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['newAttr1']['vold']['fill'] = 'red'
G.add_edge('newAttr1','vold')
G.edge['newAttr1']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('newAttr1','commonplatformappdomain')
G.edge['newAttr1']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][open execmod]'
G.add_edge('newAttr1','epmd')
G.edge['newAttr1']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open execmod]'
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open execmod]'
G.add_edge('newAttr1','platform_app')
G.edge['newAttr1']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open execmod]'
G.add_edge('newAttr1','s_platform_app')
G.edge['newAttr1']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open execmod]'
G.add_edge('newAttr1','system_server')
G.edge['newAttr1']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open execmod]'
G.add_edge('newAttr1','vold')
G.edge['newAttr1']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open execmod]'
G.add_edge('newAttr1','vold')
G.edge['newAttr1']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open execmod][open execmod]'
G.add_edge('platform_app','commonplatformappdomain')
G.edge['platform_app']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('platform_app','epmd')
G.edge['platform_app']['epmd']['write-read'] = '[open open]'
G.add_edge('platform_app','newAttr1')
G.edge['platform_app']['newAttr1']['write-read'] = '[open open]'
G.add_edge('platform_app','platform_app')
G.edge['platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('platform_app','s_platform_app')
G.edge['platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('platform_app','system_server')
G.edge['platform_app']['system_server']['write-read'] = '[open open]'
G.add_edge('platform_app','vold')
G.edge['platform_app']['vold']['write-read'] = '[open open]'
G.add_edge('platform_app','vold')
G.edge['platform_app']['vold']['write-read'] = '[open open][open open]'
G.add_edge('platform_app','commonplatformappdomain')
G.edge['platform_app']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platform_app','epmd')
G.edge['platform_app']['epmd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platform_app','newAttr1')
G.edge['platform_app']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platform_app','platform_app')
G.edge['platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('platform_app','s_platform_app')
G.edge['platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('platform_app','system_server')
G.edge['platform_app']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('platform_app','vold')
G.edge['platform_app']['vold']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('platform_app','vold')
G.edge['platform_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('platform_app','commonplatformappdomain')
G.edge['platform_app']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platform_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('platform_app','commonplatformappdomain')
G.edge['platform_app']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('platform_app','drmserver')
G.edge['platform_app']['drmserver']['write-read'] = '[write read]'
G.edge['platform_app']['drmserver']['fill'] = 'red'
G.add_edge('platform_app','epmd')
G.edge['platform_app']['epmd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platform_app']['epmd']['fill'] = 'red'
G.add_edge('platform_app','epmd')
G.edge['platform_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('platform_app','newAttr1')
G.edge['platform_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platform_app']['newAttr1']['fill'] = 'red'
G.add_edge('platform_app','newAttr1')
G.edge['platform_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('platform_app','platform_app')
G.edge['platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['platform_app']['platform_app']['fill'] = 'red'
G.add_edge('platform_app','platform_app')
G.edge['platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('platform_app','s_platform_app')
G.edge['platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['platform_app']['s_platform_app']['fill'] = 'red'
G.add_edge('platform_app','s_platform_app')
G.edge['platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('platform_app','system_server')
G.edge['platform_app']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['platform_app']['system_server']['fill'] = 'red'
G.add_edge('platform_app','system_server')
G.edge['platform_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('platform_app','vold')
G.edge['platform_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['platform_app']['vold']['fill'] = 'red'
G.add_edge('platform_app','vold')
G.edge['platform_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('s_platform_app','commonplatformappdomain')
G.edge['s_platform_app']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('s_platform_app','epmd')
G.edge['s_platform_app']['epmd']['write-read'] = '[open open]'
G.add_edge('s_platform_app','newAttr1')
G.edge['s_platform_app']['newAttr1']['write-read'] = '[open open]'
G.add_edge('s_platform_app','platform_app')
G.edge['s_platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_platform_app','s_platform_app')
G.edge['s_platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_platform_app','system_server')
G.edge['s_platform_app']['system_server']['write-read'] = '[setattr getattr][open open]'
G.add_edge('s_platform_app','vold')
G.edge['s_platform_app']['vold']['write-read'] = '[open open]'
G.add_edge('s_platform_app','vold')
G.edge['s_platform_app']['vold']['write-read'] = '[open open][open open]'
G.add_edge('s_platform_app','commonplatformappdomain')
G.edge['s_platform_app']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_platform_app','epmd')
G.edge['s_platform_app']['epmd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_platform_app','newAttr1')
G.edge['s_platform_app']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_platform_app','platform_app')
G.edge['s_platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_platform_app','s_platform_app')
G.edge['s_platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_platform_app','system_server')
G.edge['s_platform_app']['system_server']['write-read'] = '[setattr getattr][open open][setattr getattr]'
G.add_edge('s_platform_app','vold')
G.edge['s_platform_app']['vold']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('s_platform_app','vold')
G.edge['s_platform_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('s_platform_app','commonplatformappdomain')
G.edge['s_platform_app']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_platform_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('s_platform_app','commonplatformappdomain')
G.edge['s_platform_app']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_platform_app','drmserver')
G.edge['s_platform_app']['drmserver']['write-read'] = '[write read]'
G.edge['s_platform_app']['drmserver']['fill'] = 'red'
G.add_edge('s_platform_app','epmd')
G.edge['s_platform_app']['epmd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_platform_app']['epmd']['fill'] = 'red'
G.add_edge('s_platform_app','epmd')
G.edge['s_platform_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_platform_app','newAttr1')
G.edge['s_platform_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_platform_app']['newAttr1']['fill'] = 'red'
G.add_edge('s_platform_app','newAttr1')
G.edge['s_platform_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_platform_app','platform_app')
G.edge['s_platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_platform_app']['platform_app']['fill'] = 'red'
G.add_edge('s_platform_app','platform_app')
G.edge['s_platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('s_platform_app','s_platform_app')
G.edge['s_platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_platform_app']['s_platform_app']['fill'] = 'red'
G.add_edge('s_platform_app','s_platform_app')
G.edge['s_platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('s_platform_app','system_server')
G.edge['s_platform_app']['system_server']['write-read'] = '[setattr getattr][open open][setattr getattr][write read]'
G.edge['s_platform_app']['system_server']['fill'] = 'red'
G.add_edge('s_platform_app','system_server')
G.edge['s_platform_app']['system_server']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][append read]'
G.add_edge('s_platform_app','vold')
G.edge['s_platform_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['s_platform_app']['vold']['fill'] = 'red'
G.add_edge('s_platform_app','vold')
G.edge['s_platform_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('s_system_app','commonplatformappdomain')
G.edge['s_system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','epmd')
G.edge['s_system_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open]'
G.add_edge('s_system_app','newAttr1')
G.edge['s_system_app']['newAttr1']['write-read'] = '[open open]'
G.add_edge('s_system_app','platform_app')
G.edge['s_system_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','s_platform_app')
G.edge['s_system_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open]'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('s_system_app','commonplatformappdomain')
G.edge['s_system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','epmd')
G.edge['s_system_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr]'
G.add_edge('s_system_app','newAttr1')
G.edge['s_system_app']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','platform_app')
G.edge['s_system_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','s_platform_app')
G.edge['s_system_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr]'
G.add_edge('s_system_app','commonplatformappdomain')
G.edge['s_system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('s_system_app','commonplatformappdomain')
G.edge['s_system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','drmserver')
G.edge['s_system_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['s_system_app']['drmserver']['fill'] = 'red'
G.add_edge('s_system_app','epmd')
G.edge['s_system_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read]'
G.edge['s_system_app']['epmd']['fill'] = 'red'
G.add_edge('s_system_app','epmd')
G.edge['s_system_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','newAttr1')
G.edge['s_system_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['newAttr1']['fill'] = 'red'
G.add_edge('s_system_app','newAttr1')
G.edge['s_system_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','platform_app')
G.edge['s_system_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['platform_app']['fill'] = 'red'
G.add_edge('s_system_app','platform_app')
G.edge['s_system_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','s_platform_app')
G.edge['s_system_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['s_platform_app']['fill'] = 'red'
G.add_edge('s_system_app','s_platform_app')
G.edge['s_system_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['system_server']['fill'] = 'red'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['s_system_app']['vold']['fill'] = 'red'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('system_app','commonplatformappdomain')
G.edge['system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','epmd')
G.edge['system_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open]'
G.add_edge('system_app','newAttr1')
G.edge['system_app']['newAttr1']['write-read'] = '[open open]'
G.add_edge('system_app','platform_app')
G.edge['system_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','s_platform_app')
G.edge['system_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open]'
G.add_edge('system_app','vold')
G.edge['system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','vold')
G.edge['system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('system_app','commonplatformappdomain')
G.edge['system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_app','epmd')
G.edge['system_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr]'
G.add_edge('system_app','newAttr1')
G.edge['system_app']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','platform_app')
G.edge['system_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_app','s_platform_app')
G.edge['system_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','vold')
G.edge['system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('system_app','vold')
G.edge['system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr]'
G.add_edge('system_app','commonplatformappdomain')
G.edge['system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('system_app','commonplatformappdomain')
G.edge['system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','drmserver')
G.edge['system_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['system_app']['drmserver']['fill'] = 'red'
G.add_edge('system_app','epmd')
G.edge['system_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read]'
G.edge['system_app']['epmd']['fill'] = 'red'
G.add_edge('system_app','epmd')
G.edge['system_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','newAttr1')
G.edge['system_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['newAttr1']['fill'] = 'red'
G.add_edge('system_app','newAttr1')
G.edge['system_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_app','platform_app')
G.edge['system_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_app']['platform_app']['fill'] = 'red'
G.add_edge('system_app','platform_app')
G.edge['system_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','s_platform_app')
G.edge['system_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_app']['s_platform_app']['fill'] = 'red'
G.add_edge('system_app','s_platform_app')
G.edge['system_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['system_server']['fill'] = 'red'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','vold')
G.edge['system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['system_app']['vold']['fill'] = 'red'
G.add_edge('system_app','vold')
G.edge['system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('system_server','commonplatformappdomain')
G.edge['system_server']['commonplatformappdomain']['write-read'] = '[setopt getopt][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','newAttr1')
G.edge['system_server']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','platform_app')
G.edge['system_server']['platform_app']['write-read'] = '[open open]'
G.add_edge('system_server','s_platform_app')
G.edge['system_server']['s_platform_app']['write-read'] = '[open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('system_server','commonplatformappdomain')
G.edge['system_server']['commonplatformappdomain']['write-read'] = '[setopt getopt][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','newAttr1')
G.edge['system_server']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','platform_app')
G.edge['system_server']['platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','s_platform_app')
G.edge['system_server']['s_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr]'
G.add_edge('system_server','commonplatformappdomain')
G.edge['system_server']['commonplatformappdomain']['write-read'] = '[setopt getopt][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('system_server','commonplatformappdomain')
G.edge['system_server']['commonplatformappdomain']['write-read'] = '[setopt getopt][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','drmserver')
G.edge['system_server']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['system_server']['drmserver']['fill'] = 'red'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['epmd']['fill'] = 'red'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','newAttr1')
G.edge['system_server']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['newAttr1']['fill'] = 'red'
G.add_edge('system_server','newAttr1')
G.edge['system_server']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','platform_app')
G.edge['system_server']['platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['platform_app']['fill'] = 'red'
G.add_edge('system_server','platform_app')
G.edge['system_server']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_server','s_platform_app')
G.edge['system_server']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['s_platform_app']['fill'] = 'red'
G.add_edge('system_server','s_platform_app')
G.edge['system_server']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['system_server']['vold']['fill'] = 'red'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','commonplatformappdomain')
G.edge['trustonicpartner_app']['commonplatformappdomain']['write-read'] = '[open open][open open]'
G.add_edge('trustonicpartner_app','epmd')
G.edge['trustonicpartner_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open]'
G.add_edge('trustonicpartner_app','newAttr1')
G.edge['trustonicpartner_app']['newAttr1']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','platform_app')
G.edge['trustonicpartner_app']['platform_app']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','s_platform_app')
G.edge['trustonicpartner_app']['s_platform_app']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','system_server')
G.edge['trustonicpartner_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open]'
G.add_edge('trustonicpartner_app','vold')
G.edge['trustonicpartner_app']['vold']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','vold')
G.edge['trustonicpartner_app']['vold']['write-read'] = '[open open][open open]'
G.add_edge('trustonicpartner_app','commonplatformappdomain')
G.edge['trustonicpartner_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('trustonicpartner_app','epmd')
G.edge['trustonicpartner_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('trustonicpartner_app','newAttr1')
G.edge['trustonicpartner_app']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','platform_app')
G.edge['trustonicpartner_app']['platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','s_platform_app')
G.edge['trustonicpartner_app']['s_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','system_server')
G.edge['trustonicpartner_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr]'
G.add_edge('trustonicpartner_app','vold')
G.edge['trustonicpartner_app']['vold']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('trustonicpartner_app','vold')
G.edge['trustonicpartner_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('trustonicpartner_app','commonplatformappdomain')
G.edge['trustonicpartner_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('trustonicpartner_app','commonplatformappdomain')
G.edge['trustonicpartner_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','drmserver')
G.edge['trustonicpartner_app']['drmserver']['write-read'] = '[write read]'
G.edge['trustonicpartner_app']['drmserver']['fill'] = 'red'
G.add_edge('trustonicpartner_app','epmd')
G.edge['trustonicpartner_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['epmd']['fill'] = 'red'
G.add_edge('trustonicpartner_app','epmd')
G.edge['trustonicpartner_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','newAttr1')
G.edge['trustonicpartner_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['newAttr1']['fill'] = 'red'
G.add_edge('trustonicpartner_app','newAttr1')
G.edge['trustonicpartner_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','platform_app')
G.edge['trustonicpartner_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['platform_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','platform_app')
G.edge['trustonicpartner_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','s_platform_app')
G.edge['trustonicpartner_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['s_platform_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','s_platform_app')
G.edge['trustonicpartner_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','system_server')
G.edge['trustonicpartner_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['system_server']['fill'] = 'red'
G.add_edge('trustonicpartner_app','system_server')
G.edge['trustonicpartner_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('trustonicpartner_app','vold')
G.edge['trustonicpartner_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['trustonicpartner_app']['vold']['fill'] = 'red'
G.add_edge('trustonicpartner_app','vold')
G.edge['trustonicpartner_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','commonplatformappdomain')
G.edge['umcagent_app']['commonplatformappdomain']['write-read'] = '[open open][open open]'
G.add_edge('umcagent_app','epmd')
G.edge['umcagent_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open]'
G.add_edge('umcagent_app','newAttr1')
G.edge['umcagent_app']['newAttr1']['write-read'] = '[open open]'
G.add_edge('umcagent_app','platform_app')
G.edge['umcagent_app']['platform_app']['write-read'] = '[open open]'
G.add_edge('umcagent_app','s_platform_app')
G.edge['umcagent_app']['s_platform_app']['write-read'] = '[open open]'
G.add_edge('umcagent_app','system_server')
G.edge['umcagent_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open]'
G.add_edge('umcagent_app','vold')
G.edge['umcagent_app']['vold']['write-read'] = '[open open]'
G.add_edge('umcagent_app','vold')
G.edge['umcagent_app']['vold']['write-read'] = '[open open][open open]'
G.add_edge('umcagent_app','commonplatformappdomain')
G.edge['umcagent_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('umcagent_app','epmd')
G.edge['umcagent_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('umcagent_app','newAttr1')
G.edge['umcagent_app']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','platform_app')
G.edge['umcagent_app']['platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','s_platform_app')
G.edge['umcagent_app']['s_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','system_server')
G.edge['umcagent_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr]'
G.add_edge('umcagent_app','vold')
G.edge['umcagent_app']['vold']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('umcagent_app','vold')
G.edge['umcagent_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('umcagent_app','commonplatformappdomain')
G.edge['umcagent_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['umcagent_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('umcagent_app','commonplatformappdomain')
G.edge['umcagent_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','drmserver')
G.edge['umcagent_app']['drmserver']['write-read'] = '[write read]'
G.edge['umcagent_app']['drmserver']['fill'] = 'red'
G.add_edge('umcagent_app','epmd')
G.edge['umcagent_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['umcagent_app']['epmd']['fill'] = 'red'
G.add_edge('umcagent_app','epmd')
G.edge['umcagent_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','newAttr1')
G.edge['umcagent_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['umcagent_app']['newAttr1']['fill'] = 'red'
G.add_edge('umcagent_app','newAttr1')
G.edge['umcagent_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','platform_app')
G.edge['umcagent_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['umcagent_app']['platform_app']['fill'] = 'red'
G.add_edge('umcagent_app','platform_app')
G.edge['umcagent_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','s_platform_app')
G.edge['umcagent_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['umcagent_app']['s_platform_app']['fill'] = 'red'
G.add_edge('umcagent_app','s_platform_app')
G.edge['umcagent_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','system_server')
G.edge['umcagent_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read]'
G.edge['umcagent_app']['system_server']['fill'] = 'red'
G.add_edge('umcagent_app','system_server')
G.edge['umcagent_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('umcagent_app','vold')
G.edge['umcagent_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['umcagent_app']['vold']['fill'] = 'red'
G.add_edge('umcagent_app','vold')
G.edge['umcagent_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','commonplatformappdomain')
G.edge['untrusted_app']['commonplatformappdomain']['write-read'] = '[open open][open open]'
G.add_edge('untrusted_app','epmd')
G.edge['untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open]'
G.add_edge('untrusted_app','newAttr1')
G.edge['untrusted_app']['newAttr1']['write-read'] = '[open open]'
G.add_edge('untrusted_app','platform_app')
G.edge['untrusted_app']['platform_app']['write-read'] = '[open open]'
G.add_edge('untrusted_app','s_platform_app')
G.edge['untrusted_app']['s_platform_app']['write-read'] = '[open open]'
G.add_edge('untrusted_app','system_server')
G.edge['untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open]'
G.add_edge('untrusted_app','vold')
G.edge['untrusted_app']['vold']['write-read'] = '[open open]'
G.add_edge('untrusted_app','vold')
G.edge['untrusted_app']['vold']['write-read'] = '[open open][open open]'
G.add_edge('untrusted_app','commonplatformappdomain')
G.edge['untrusted_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('untrusted_app','epmd')
G.edge['untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('untrusted_app','newAttr1')
G.edge['untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','platform_app')
G.edge['untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','s_platform_app')
G.edge['untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','system_server')
G.edge['untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr]'
G.add_edge('untrusted_app','vold')
G.edge['untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('untrusted_app','vold')
G.edge['untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('untrusted_app','commonplatformappdomain')
G.edge['untrusted_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['untrusted_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('untrusted_app','commonplatformappdomain')
G.edge['untrusted_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','drmserver')
G.edge['untrusted_app']['drmserver']['write-read'] = '[write read]'
G.edge['untrusted_app']['drmserver']['fill'] = 'red'
G.add_edge('untrusted_app','epmd')
G.edge['untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['untrusted_app']['epmd']['fill'] = 'red'
G.add_edge('untrusted_app','epmd')
G.edge['untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','newAttr1')
G.edge['untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusted_app']['newAttr1']['fill'] = 'red'
G.add_edge('untrusted_app','newAttr1')
G.edge['untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','platform_app')
G.edge['untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusted_app']['platform_app']['fill'] = 'red'
G.add_edge('untrusted_app','platform_app')
G.edge['untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','s_platform_app')
G.edge['untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusted_app']['s_platform_app']['fill'] = 'red'
G.add_edge('untrusted_app','s_platform_app')
G.edge['untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','system_server')
G.edge['untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read]'
G.edge['untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('untrusted_app','system_server')
G.edge['untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusted_app','vold')
G.edge['untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['untrusted_app']['vold']['fill'] = 'red'
G.add_edge('untrusted_app','vold')
G.edge['untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','commonplatformappdomain')
G.edge['untrusteddomain']['commonplatformappdomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('untrusteddomain','epmd')
G.edge['untrusteddomain']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusteddomain','newAttr1')
G.edge['untrusteddomain']['newAttr1']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','platform_app')
G.edge['untrusteddomain']['platform_app']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','s_platform_app')
G.edge['untrusteddomain']['s_platform_app']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open]'
G.add_edge('untrusteddomain','vold')
G.edge['untrusteddomain']['vold']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','vold')
G.edge['untrusteddomain']['vold']['write-read'] = '[open open][open open]'
G.add_edge('untrusteddomain','commonplatformappdomain')
G.edge['untrusteddomain']['commonplatformappdomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('untrusteddomain','epmd')
G.edge['untrusteddomain']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('untrusteddomain','newAttr1')
G.edge['untrusteddomain']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusteddomain','platform_app')
G.edge['untrusteddomain']['platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusteddomain','s_platform_app')
G.edge['untrusteddomain']['s_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('untrusteddomain','vold')
G.edge['untrusteddomain']['vold']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('untrusteddomain','vold')
G.edge['untrusteddomain']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('untrusteddomain','commonplatformappdomain')
G.edge['untrusteddomain']['commonplatformappdomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('untrusteddomain','commonplatformappdomain')
G.edge['untrusteddomain']['commonplatformappdomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','drmserver')
G.edge['untrusteddomain']['drmserver']['write-read'] = '[write read]'
G.edge['untrusteddomain']['drmserver']['fill'] = 'red'
G.add_edge('untrusteddomain','epmd')
G.edge['untrusteddomain']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['epmd']['fill'] = 'red'
G.add_edge('untrusteddomain','epmd')
G.edge['untrusteddomain']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','newAttr1')
G.edge['untrusteddomain']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusteddomain']['newAttr1']['fill'] = 'red'
G.add_edge('untrusteddomain','newAttr1')
G.edge['untrusteddomain']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','platform_app')
G.edge['untrusteddomain']['platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusteddomain']['platform_app']['fill'] = 'red'
G.add_edge('untrusteddomain','platform_app')
G.edge['untrusteddomain']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','s_platform_app')
G.edge['untrusteddomain']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusteddomain']['s_platform_app']['fill'] = 'red'
G.add_edge('untrusteddomain','s_platform_app')
G.edge['untrusteddomain']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['system_server']['fill'] = 'red'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','vold')
G.edge['untrusteddomain']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['untrusteddomain']['vold']['fill'] = 'red'
G.add_edge('untrusteddomain','vold')
G.edge['untrusteddomain']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('vold','commonplatformappdomain')
G.edge['vold']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open]'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','newAttr1')
G.edge['vold']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('vold','platform_app')
G.edge['vold']['platform_app']['write-read'] = '[open open]'
G.add_edge('vold','s_platform_app')
G.edge['vold']['s_platform_app']['write-read'] = '[open open]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('vold','commonplatformappdomain')
G.edge['vold']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][setattr getattr]'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('vold','newAttr1')
G.edge['vold']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('vold','platform_app')
G.edge['vold']['platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vold','s_platform_app')
G.edge['vold']['s_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr]'
G.add_edge('vold','commonplatformappdomain')
G.edge['vold']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][setattr getattr][write read]'
G.edge['vold']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('vold','commonplatformappdomain')
G.edge['vold']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('vold','drmserver')
G.edge['vold']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read]'
G.edge['vold']['drmserver']['fill'] = 'red'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['vold']['epmd']['fill'] = 'red'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('vold','newAttr1')
G.edge['vold']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['vold']['newAttr1']['fill'] = 'red'
G.add_edge('vold','newAttr1')
G.edge['vold']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('vold','platform_app')
G.edge['vold']['platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vold']['platform_app']['fill'] = 'red'
G.add_edge('vold','platform_app')
G.edge['vold']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('vold','s_platform_app')
G.edge['vold']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vold']['s_platform_app']['fill'] = 'red'
G.add_edge('vold','s_platform_app')
G.edge['vold']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['vold']['system_server']['fill'] = 'red'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['vold']['vold']['fill'] = 'red'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('vold','commonplatformappdomain')
G.edge['vold']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vold','newAttr1')
G.edge['vold']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vold','platform_app')
G.edge['vold']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('vold','s_platform_app')
G.edge['vold']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open]'
G.add_edge('vold','commonplatformappdomain')
G.edge['vold']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('vold','newAttr1')
G.edge['vold']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('vold','platform_app')
G.edge['vold']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('vold','s_platform_app')
G.edge['vold']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr]'
G.add_edge('vold','commonplatformappdomain')
G.edge['vold']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['vold']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('vold','commonplatformappdomain')
G.edge['vold']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('vold','drmserver')
G.edge['vold']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][write read]'
G.edge['vold']['drmserver']['fill'] = 'red'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['vold']['epmd']['fill'] = 'red'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('vold','newAttr1')
G.edge['vold']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['vold']['newAttr1']['fill'] = 'red'
G.add_edge('vold','newAttr1')
G.edge['vold']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('vold','platform_app')
G.edge['vold']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['vold']['platform_app']['fill'] = 'red'
G.add_edge('vold','platform_app')
G.edge['vold']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('vold','s_platform_app')
G.edge['vold']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['vold']['s_platform_app']['fill'] = 'red'
G.add_edge('vold','s_platform_app')
G.edge['vold']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['vold']['system_server']['fill'] = 'red'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['vold']['vold']['fill'] = 'red'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom]'
G.add_edge('vpn_untrusted_app','commonplatformappdomain')
G.edge['vpn_untrusted_app']['commonplatformappdomain']['write-read'] = '[open open][open open]'
G.add_edge('vpn_untrusted_app','epmd')
G.edge['vpn_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open]'
G.add_edge('vpn_untrusted_app','newAttr1')
G.edge['vpn_untrusted_app']['newAttr1']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','platform_app')
G.edge['vpn_untrusted_app']['platform_app']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','s_platform_app')
G.edge['vpn_untrusted_app']['s_platform_app']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','system_server')
G.edge['vpn_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open]'
G.add_edge('vpn_untrusted_app','vold')
G.edge['vpn_untrusted_app']['vold']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','vold')
G.edge['vpn_untrusted_app']['vold']['write-read'] = '[open open][open open]'
G.add_edge('vpn_untrusted_app','commonplatformappdomain')
G.edge['vpn_untrusted_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','epmd')
G.edge['vpn_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','newAttr1')
G.edge['vpn_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','platform_app')
G.edge['vpn_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','s_platform_app')
G.edge['vpn_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','system_server')
G.edge['vpn_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','vold')
G.edge['vpn_untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','vold')
G.edge['vpn_untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('vpn_untrusted_app','commonplatformappdomain')
G.edge['vpn_untrusted_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','commonplatformappdomain')
G.edge['vpn_untrusted_app']['commonplatformappdomain']['write-read'] = '[open open][open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','drmserver')
G.edge['vpn_untrusted_app']['drmserver']['write-read'] = '[write read]'
G.edge['vpn_untrusted_app']['drmserver']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','epmd')
G.edge['vpn_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['epmd']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','epmd')
G.edge['vpn_untrusted_app']['epmd']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','newAttr1')
G.edge['vpn_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['newAttr1']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','newAttr1')
G.edge['vpn_untrusted_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','platform_app')
G.edge['vpn_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['platform_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','platform_app')
G.edge['vpn_untrusted_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','s_platform_app')
G.edge['vpn_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['s_platform_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','s_platform_app')
G.edge['vpn_untrusted_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','system_server')
G.edge['vpn_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['system_server']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','system_server')
G.edge['vpn_untrusted_app']['system_server']['write-read'] = '[setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','vold')
G.edge['vpn_untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['vold']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','vold')
G.edge['vpn_untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()