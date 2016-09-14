import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('charger_monitor','energy-awareness')
G.edge['charger_monitor']['energy-awareness']['write-read'] = '[write read]'
G.edge['charger_monitor']['energy-awareness']['fill'] = 'red'
G.add_edge('charger_monitor','energy-awareness')
G.edge['charger_monitor']['energy-awareness']['write-read'] = '[write read][append read]'
G.add_edge('charger_monitor','energyawareness')
G.edge['charger_monitor']['energyawareness']['write-read'] = '[write read]'
G.edge['charger_monitor']['energyawareness']['fill'] = 'red'
G.add_edge('charger_monitor','energyawareness')
G.edge['charger_monitor']['energyawareness']['write-read'] = '[write read][append read]'
G.add_edge('charger_monitor','healthd')
G.edge['charger_monitor']['healthd']['write-read'] = '[write read]'
G.edge['charger_monitor']['healthd']['fill'] = 'red'
G.add_edge('charger_monitor','healthd')
G.edge['charger_monitor']['healthd']['write-read'] = '[write read][append read]'
G.add_edge('charger_monitor','hvdcp')
G.edge['charger_monitor']['hvdcp']['write-read'] = '[write read]'
G.edge['charger_monitor']['hvdcp']['fill'] = 'red'
G.add_edge('charger_monitor','hvdcp')
G.edge['charger_monitor']['hvdcp']['write-read'] = '[write read][append read]'
G.add_edge('charger_monitor','netd')
G.edge['charger_monitor']['netd']['write-read'] = '[write read]'
G.edge['charger_monitor']['netd']['fill'] = 'red'
G.add_edge('charger_monitor','netd')
G.edge['charger_monitor']['netd']['write-read'] = '[write read][append read]'
G.add_edge('charger_monitor','rild')
G.edge['charger_monitor']['rild']['write-read'] = '[write read]'
G.edge['charger_monitor']['rild']['fill'] = 'red'
G.add_edge('charger_monitor','rild')
G.edge['charger_monitor']['rild']['write-read'] = '[write read][append read]'
G.add_edge('charger_monitor','s_system_app')
G.edge['charger_monitor']['s_system_app']['read-write'] = '* >read'
G.add_edge('charger_monitor','surfaceflinger')
G.edge['charger_monitor']['surfaceflinger']['write-read'] = '[write read]'
G.edge['charger_monitor']['surfaceflinger']['fill'] = 'red'
G.add_edge('charger_monitor','surfaceflinger')
G.edge['charger_monitor']['surfaceflinger']['write-read'] = '[write read][append read]'
G.add_edge('charger_monitor','system_server')
G.edge['charger_monitor']['system_server']['write-read'] = '[write read]'
G.edge['charger_monitor']['system_server']['fill'] = 'red'
G.add_edge('charger_monitor','system_server')
G.edge['charger_monitor']['system_server']['write-read'] = '[write read][append read]'
G.add_edge('charger_monitor','thermald')
G.edge['charger_monitor']['thermald']['read-write'] = '* >read'
G.add_edge('charger_monitor','ueventd')
G.edge['charger_monitor']['ueventd']['write-read'] = '[write read]'
G.edge['charger_monitor']['ueventd']['fill'] = 'red'
G.add_edge('charger_monitor','ueventd')
G.edge['charger_monitor']['ueventd']['write-read'] = '[write read][append read]'
G.add_edge('charger_monitor','vold')
G.edge['charger_monitor']['vold']['write-read'] = '[write read]'
G.edge['charger_monitor']['vold']['fill'] = 'red'
G.add_edge('charger_monitor','vold')
G.edge['charger_monitor']['vold']['write-read'] = '[write read][append read]'
G.add_edge('charger_monitor','wfdservice')
G.edge['charger_monitor']['wfdservice']['write-read'] = '[write read]'
G.edge['charger_monitor']['wfdservice']['fill'] = 'red'
G.add_edge('charger_monitor','wfdservice')
G.edge['charger_monitor']['wfdservice']['write-read'] = '[write read][append read]'
G.add_edge('commonplatformappdomain','energy-awareness')
G.edge['commonplatformappdomain']['energy-awareness']['write-read'] = '[write read]'
G.edge['commonplatformappdomain']['energy-awareness']['fill'] = 'red'
G.add_edge('commonplatformappdomain','energy-awareness')
G.edge['commonplatformappdomain']['energy-awareness']['write-read'] = '[write read][append read]'
G.add_edge('commonplatformappdomain','energyawareness')
G.edge['commonplatformappdomain']['energyawareness']['write-read'] = '[write read]'
G.edge['commonplatformappdomain']['energyawareness']['fill'] = 'red'
G.add_edge('commonplatformappdomain','energyawareness')
G.edge['commonplatformappdomain']['energyawareness']['write-read'] = '[write read][append read]'
G.add_edge('commonplatformappdomain','healthd')
G.edge['commonplatformappdomain']['healthd']['write-read'] = '[write read]'
G.edge['commonplatformappdomain']['healthd']['fill'] = 'red'
G.add_edge('commonplatformappdomain','healthd')
G.edge['commonplatformappdomain']['healthd']['write-read'] = '[write read][append read]'
G.add_edge('commonplatformappdomain','hvdcp')
G.edge['commonplatformappdomain']['hvdcp']['write-read'] = '[write read]'
G.edge['commonplatformappdomain']['hvdcp']['fill'] = 'red'
G.add_edge('commonplatformappdomain','hvdcp')
G.edge['commonplatformappdomain']['hvdcp']['write-read'] = '[write read][append read]'
G.add_edge('commonplatformappdomain','netd')
G.edge['commonplatformappdomain']['netd']['write-read'] = '[write read]'
G.edge['commonplatformappdomain']['netd']['fill'] = 'red'
G.add_edge('commonplatformappdomain','netd')
G.edge['commonplatformappdomain']['netd']['write-read'] = '[write read][append read]'
G.add_edge('commonplatformappdomain','rild')
G.edge['commonplatformappdomain']['rild']['write-read'] = '[write read]'
G.edge['commonplatformappdomain']['rild']['fill'] = 'red'
G.add_edge('commonplatformappdomain','rild')
G.edge['commonplatformappdomain']['rild']['write-read'] = '[write read][append read]'
G.add_edge('commonplatformappdomain','s_system_app')
G.edge['commonplatformappdomain']['s_system_app']['read-write'] = '* >read'
G.add_edge('commonplatformappdomain','surfaceflinger')
G.edge['commonplatformappdomain']['surfaceflinger']['write-read'] = '[write read]'
G.edge['commonplatformappdomain']['surfaceflinger']['fill'] = 'red'
G.add_edge('commonplatformappdomain','surfaceflinger')
G.edge['commonplatformappdomain']['surfaceflinger']['write-read'] = '[write read][append read]'
G.add_edge('commonplatformappdomain','system_server')
G.edge['commonplatformappdomain']['system_server']['write-read'] = '[write read]'
G.edge['commonplatformappdomain']['system_server']['fill'] = 'red'
G.add_edge('commonplatformappdomain','system_server')
G.edge['commonplatformappdomain']['system_server']['write-read'] = '[write read][append read]'
G.add_edge('commonplatformappdomain','thermald')
G.edge['commonplatformappdomain']['thermald']['read-write'] = '* >read'
G.add_edge('commonplatformappdomain','ueventd')
G.edge['commonplatformappdomain']['ueventd']['write-read'] = '[write read]'
G.edge['commonplatformappdomain']['ueventd']['fill'] = 'red'
G.add_edge('commonplatformappdomain','ueventd')
G.edge['commonplatformappdomain']['ueventd']['write-read'] = '[write read][append read]'
G.add_edge('commonplatformappdomain','vold')
G.edge['commonplatformappdomain']['vold']['write-read'] = '[write read]'
G.edge['commonplatformappdomain']['vold']['fill'] = 'red'
G.add_edge('commonplatformappdomain','vold')
G.edge['commonplatformappdomain']['vold']['write-read'] = '[write read][append read]'
G.add_edge('commonplatformappdomain','wfdservice')
G.edge['commonplatformappdomain']['wfdservice']['write-read'] = '[write read]'
G.edge['commonplatformappdomain']['wfdservice']['fill'] = 'red'
G.add_edge('commonplatformappdomain','wfdservice')
G.edge['commonplatformappdomain']['wfdservice']['write-read'] = '[write read][append read]'
G.add_edge('energy-awareness','energy-awareness')
G.edge['energy-awareness']['energy-awareness']['write-read'] = '[setattr getattr]'
G.add_edge('energy-awareness','energyawareness')
G.edge['energy-awareness']['energyawareness']['write-read'] = '[setattr getattr]'
G.add_edge('energy-awareness','healthd')
G.edge['energy-awareness']['healthd']['write-read'] = '[setattr getattr]'
G.add_edge('energy-awareness','hvdcp')
G.edge['energy-awareness']['hvdcp']['write-read'] = '[setattr getattr]'
G.add_edge('energy-awareness','ime_app')
G.edge['energy-awareness']['ime_app']['write-read'] = '[setattr getattr]'
G.add_edge('energy-awareness','netd')
G.edge['energy-awareness']['netd']['write-read'] = '[setattr getattr]'
G.add_edge('energy-awareness','rild')
G.edge['energy-awareness']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('energy-awareness','s_system_app')
G.edge['energy-awareness']['s_system_app']['read-write'] = '* >getattr'
G.add_edge('energy-awareness','s_system_app')
G.edge['energy-awareness']['s_system_app']['write-read'] = '[setattr getattr]'
G.add_edge('energy-awareness','surfaceflinger')
G.edge['energy-awareness']['surfaceflinger']['write-read'] = '[setattr getattr]'
G.add_edge('energy-awareness','system_app')
G.edge['energy-awareness']['system_app']['write-read'] = '[setattr getattr]'
G.add_edge('energy-awareness','system_server')
G.edge['energy-awareness']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('energy-awareness','thermald')
G.edge['energy-awareness']['thermald']['read-write'] = '* >getattr'
G.add_edge('energy-awareness','ueventd')
G.edge['energy-awareness']['ueventd']['write-read'] = '[setattr getattr]'
G.add_edge('energy-awareness','vold')
G.edge['energy-awareness']['vold']['write-read'] = '[setattr getattr]'
G.add_edge('energy-awareness','wfdservice')
G.edge['energy-awareness']['wfdservice']['write-read'] = '[setattr getattr]'
G.add_edge('energy-awareness','energy-awareness')
G.edge['energy-awareness']['energy-awareness']['write-read'] = '[setattr getattr][write read]'
G.edge['energy-awareness']['energy-awareness']['fill'] = 'red'
G.add_edge('energy-awareness','energy-awareness')
G.edge['energy-awareness']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('energy-awareness','energyawareness')
G.edge['energy-awareness']['energyawareness']['write-read'] = '[setattr getattr][write read]'
G.edge['energy-awareness']['energyawareness']['fill'] = 'red'
G.add_edge('energy-awareness','energyawareness')
G.edge['energy-awareness']['energyawareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('energy-awareness','healthd')
G.edge['energy-awareness']['healthd']['write-read'] = '[setattr getattr][write read]'
G.edge['energy-awareness']['healthd']['fill'] = 'red'
G.add_edge('energy-awareness','healthd')
G.edge['energy-awareness']['healthd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('energy-awareness','hvdcp')
G.edge['energy-awareness']['hvdcp']['write-read'] = '[setattr getattr][write read]'
G.edge['energy-awareness']['hvdcp']['fill'] = 'red'
G.add_edge('energy-awareness','hvdcp')
G.edge['energy-awareness']['hvdcp']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('energy-awareness','netd')
G.edge['energy-awareness']['netd']['write-read'] = '[setattr getattr][write read]'
G.edge['energy-awareness']['netd']['fill'] = 'red'
G.add_edge('energy-awareness','netd')
G.edge['energy-awareness']['netd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('energy-awareness','rild')
G.edge['energy-awareness']['rild']['write-read'] = '[setattr getattr][write read]'
G.edge['energy-awareness']['rild']['fill'] = 'red'
G.add_edge('energy-awareness','rild')
G.edge['energy-awareness']['rild']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('energy-awareness','s_system_app')
G.edge['energy-awareness']['s_system_app']['read-write'] = '* >read'
G.add_edge('energy-awareness','surfaceflinger')
G.edge['energy-awareness']['surfaceflinger']['write-read'] = '[setattr getattr][write read]'
G.edge['energy-awareness']['surfaceflinger']['fill'] = 'red'
G.add_edge('energy-awareness','surfaceflinger')
G.edge['energy-awareness']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('energy-awareness','system_server')
G.edge['energy-awareness']['system_server']['write-read'] = '[setattr getattr][write read]'
G.edge['energy-awareness']['system_server']['fill'] = 'red'
G.add_edge('energy-awareness','system_server')
G.edge['energy-awareness']['system_server']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('energy-awareness','thermald')
G.edge['energy-awareness']['thermald']['read-write'] = '* >read'
G.add_edge('energy-awareness','ueventd')
G.edge['energy-awareness']['ueventd']['write-read'] = '[setattr getattr][write read]'
G.edge['energy-awareness']['ueventd']['fill'] = 'red'
G.add_edge('energy-awareness','ueventd')
G.edge['energy-awareness']['ueventd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('energy-awareness','vold')
G.edge['energy-awareness']['vold']['write-read'] = '[setattr getattr][write read]'
G.edge['energy-awareness']['vold']['fill'] = 'red'
G.add_edge('energy-awareness','vold')
G.edge['energy-awareness']['vold']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('energy-awareness','wfdservice')
G.edge['energy-awareness']['wfdservice']['write-read'] = '[setattr getattr][write read]'
G.edge['energy-awareness']['wfdservice']['fill'] = 'red'
G.add_edge('energy-awareness','wfdservice')
G.edge['energy-awareness']['wfdservice']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('energy-awareness','charger_monitor')
G.edge['energy-awareness']['charger_monitor']['write-read'] = '[setopt getopt]'
G.add_edge('energy-awareness','commonplatformappdomain')
G.edge['energy-awareness']['commonplatformappdomain']['write-read'] = '[setopt getopt]'
G.add_edge('energy-awareness','energy-awareness')
G.edge['energy-awareness']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('energy-awareness','energyawareness')
G.edge['energy-awareness']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('energy-awareness','hbtp')
G.edge['energy-awareness']['hbtp']['write-read'] = '[setopt getopt]'
G.add_edge('energy-awareness','healthd')
G.edge['energy-awareness']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('energy-awareness','hvdcp')
G.edge['energy-awareness']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('energy-awareness','ime_app')
G.edge['energy-awareness']['ime_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('energy-awareness','lpm')
G.edge['energy-awareness']['lpm']['write-read'] = '[setopt getopt]'
G.add_edge('energy-awareness','mpdecision')
G.edge['energy-awareness']['mpdecision']['write-read'] = '[setopt getopt]'
G.add_edge('energy-awareness','mpdecision')
G.edge['energy-awareness']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt]'
G.add_edge('energy-awareness','netd')
G.edge['energy-awareness']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('energy-awareness','perfd')
G.edge['energy-awareness']['perfd']['write-read'] = '[setopt getopt]'
G.add_edge('energy-awareness','rild')
G.edge['energy-awareness']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('energy-awareness','samsung_app')
G.edge['energy-awareness']['samsung_app']['write-read'] = '[setopt getopt]'
G.add_edge('energy-awareness','ssr_diag')
G.edge['energy-awareness']['ssr_diag']['write-read'] = '[setopt getopt]'
G.add_edge('energy-awareness','s_system_app')
G.edge['energy-awareness']['s_system_app']['read-write'] = '* >getopt'
G.add_edge('energy-awareness','s_system_app')
G.edge['energy-awareness']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('energy-awareness','surfaceflinger')
G.edge['energy-awareness']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('energy-awareness','system_app')
G.edge['energy-awareness']['system_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('energy-awareness','system_server')
G.edge['energy-awareness']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('energy-awareness','thermald')
G.edge['energy-awareness']['thermald']['read-write'] = '* >getopt'
G.add_edge('energy-awareness','thermal-engine')
G.edge['energy-awareness']['thermal-engine']['write-read'] = '[setopt getopt]'
G.add_edge('energy-awareness','ueventd')
G.edge['energy-awareness']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('energy-awareness','vold')
G.edge['energy-awareness']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('energy-awareness','wfdservice')
G.edge['energy-awareness']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('energyawareness','energy-awareness')
G.edge['energyawareness']['energy-awareness']['write-read'] = '[setattr getattr]'
G.add_edge('energyawareness','energyawareness')
G.edge['energyawareness']['energyawareness']['write-read'] = '[setattr getattr]'
G.add_edge('energyawareness','healthd')
G.edge['energyawareness']['healthd']['write-read'] = '[setattr getattr]'
G.add_edge('energyawareness','hvdcp')
G.edge['energyawareness']['hvdcp']['write-read'] = '[setattr getattr]'
G.add_edge('energyawareness','ime_app')
G.edge['energyawareness']['ime_app']['write-read'] = '[setattr getattr]'
G.add_edge('energyawareness','netd')
G.edge['energyawareness']['netd']['write-read'] = '[setattr getattr]'
G.add_edge('energyawareness','rild')
G.edge['energyawareness']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('energyawareness','s_system_app')
G.edge['energyawareness']['s_system_app']['read-write'] = '* >getattr'
G.add_edge('energyawareness','s_system_app')
G.edge['energyawareness']['s_system_app']['write-read'] = '[setattr getattr]'
G.add_edge('energyawareness','surfaceflinger')
G.edge['energyawareness']['surfaceflinger']['write-read'] = '[setattr getattr]'
G.add_edge('energyawareness','system_app')
G.edge['energyawareness']['system_app']['write-read'] = '[setattr getattr]'
G.add_edge('energyawareness','system_server')
G.edge['energyawareness']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('energyawareness','thermald')
G.edge['energyawareness']['thermald']['read-write'] = '* >getattr'
G.add_edge('energyawareness','ueventd')
G.edge['energyawareness']['ueventd']['write-read'] = '[setattr getattr]'
G.add_edge('energyawareness','vold')
G.edge['energyawareness']['vold']['write-read'] = '[setattr getattr]'
G.add_edge('energyawareness','wfdservice')
G.edge['energyawareness']['wfdservice']['write-read'] = '[setattr getattr]'
G.add_edge('energyawareness','energy-awareness')
G.edge['energyawareness']['energy-awareness']['write-read'] = '[setattr getattr][write read]'
G.edge['energyawareness']['energy-awareness']['fill'] = 'red'
G.add_edge('energyawareness','energy-awareness')
G.edge['energyawareness']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('energyawareness','energyawareness')
G.edge['energyawareness']['energyawareness']['write-read'] = '[setattr getattr][write read]'
G.edge['energyawareness']['energyawareness']['fill'] = 'red'
G.add_edge('energyawareness','energyawareness')
G.edge['energyawareness']['energyawareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('energyawareness','healthd')
G.edge['energyawareness']['healthd']['write-read'] = '[setattr getattr][write read]'
G.edge['energyawareness']['healthd']['fill'] = 'red'
G.add_edge('energyawareness','healthd')
G.edge['energyawareness']['healthd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('energyawareness','hvdcp')
G.edge['energyawareness']['hvdcp']['write-read'] = '[setattr getattr][write read]'
G.edge['energyawareness']['hvdcp']['fill'] = 'red'
G.add_edge('energyawareness','hvdcp')
G.edge['energyawareness']['hvdcp']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('energyawareness','netd')
G.edge['energyawareness']['netd']['write-read'] = '[setattr getattr][write read]'
G.edge['energyawareness']['netd']['fill'] = 'red'
G.add_edge('energyawareness','netd')
G.edge['energyawareness']['netd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('energyawareness','rild')
G.edge['energyawareness']['rild']['write-read'] = '[setattr getattr][write read]'
G.edge['energyawareness']['rild']['fill'] = 'red'
G.add_edge('energyawareness','rild')
G.edge['energyawareness']['rild']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('energyawareness','s_system_app')
G.edge['energyawareness']['s_system_app']['read-write'] = '* >read'
G.add_edge('energyawareness','surfaceflinger')
G.edge['energyawareness']['surfaceflinger']['write-read'] = '[setattr getattr][write read]'
G.edge['energyawareness']['surfaceflinger']['fill'] = 'red'
G.add_edge('energyawareness','surfaceflinger')
G.edge['energyawareness']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('energyawareness','system_server')
G.edge['energyawareness']['system_server']['write-read'] = '[setattr getattr][write read]'
G.edge['energyawareness']['system_server']['fill'] = 'red'
G.add_edge('energyawareness','system_server')
G.edge['energyawareness']['system_server']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('energyawareness','thermald')
G.edge['energyawareness']['thermald']['read-write'] = '* >read'
G.add_edge('energyawareness','ueventd')
G.edge['energyawareness']['ueventd']['write-read'] = '[setattr getattr][write read]'
G.edge['energyawareness']['ueventd']['fill'] = 'red'
G.add_edge('energyawareness','ueventd')
G.edge['energyawareness']['ueventd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('energyawareness','vold')
G.edge['energyawareness']['vold']['write-read'] = '[setattr getattr][write read]'
G.edge['energyawareness']['vold']['fill'] = 'red'
G.add_edge('energyawareness','vold')
G.edge['energyawareness']['vold']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('energyawareness','wfdservice')
G.edge['energyawareness']['wfdservice']['write-read'] = '[setattr getattr][write read]'
G.edge['energyawareness']['wfdservice']['fill'] = 'red'
G.add_edge('energyawareness','wfdservice')
G.edge['energyawareness']['wfdservice']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('energyawareness','charger_monitor')
G.edge['energyawareness']['charger_monitor']['write-read'] = '[setopt getopt]'
G.add_edge('energyawareness','commonplatformappdomain')
G.edge['energyawareness']['commonplatformappdomain']['write-read'] = '[setopt getopt]'
G.add_edge('energyawareness','energy-awareness')
G.edge['energyawareness']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('energyawareness','energyawareness')
G.edge['energyawareness']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('energyawareness','hbtp')
G.edge['energyawareness']['hbtp']['write-read'] = '[setopt getopt]'
G.add_edge('energyawareness','healthd')
G.edge['energyawareness']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('energyawareness','hvdcp')
G.edge['energyawareness']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('energyawareness','ime_app')
G.edge['energyawareness']['ime_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('energyawareness','lpm')
G.edge['energyawareness']['lpm']['write-read'] = '[setopt getopt]'
G.add_edge('energyawareness','mpdecision')
G.edge['energyawareness']['mpdecision']['write-read'] = '[setopt getopt]'
G.add_edge('energyawareness','mpdecision')
G.edge['energyawareness']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt]'
G.add_edge('energyawareness','netd')
G.edge['energyawareness']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('energyawareness','perfd')
G.edge['energyawareness']['perfd']['write-read'] = '[setopt getopt]'
G.add_edge('energyawareness','rild')
G.edge['energyawareness']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('energyawareness','samsung_app')
G.edge['energyawareness']['samsung_app']['write-read'] = '[setopt getopt]'
G.add_edge('energyawareness','ssr_diag')
G.edge['energyawareness']['ssr_diag']['write-read'] = '[setopt getopt]'
G.add_edge('energyawareness','s_system_app')
G.edge['energyawareness']['s_system_app']['read-write'] = '* >getopt'
G.add_edge('energyawareness','s_system_app')
G.edge['energyawareness']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('energyawareness','surfaceflinger')
G.edge['energyawareness']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('energyawareness','system_app')
G.edge['energyawareness']['system_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('energyawareness','system_server')
G.edge['energyawareness']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('energyawareness','thermald')
G.edge['energyawareness']['thermald']['read-write'] = '* >getopt'
G.add_edge('energyawareness','thermal-engine')
G.edge['energyawareness']['thermal-engine']['write-read'] = '[setopt getopt]'
G.add_edge('energyawareness','ueventd')
G.edge['energyawareness']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('energyawareness','vold')
G.edge['energyawareness']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('energyawareness','wfdservice')
G.edge['energyawareness']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('hbtp','energy-awareness')
G.edge['hbtp']['energy-awareness']['write-read'] = '[write read]'
G.edge['hbtp']['energy-awareness']['fill'] = 'red'
G.add_edge('hbtp','energy-awareness')
G.edge['hbtp']['energy-awareness']['write-read'] = '[write read][append read]'
G.add_edge('hbtp','energyawareness')
G.edge['hbtp']['energyawareness']['write-read'] = '[write read]'
G.edge['hbtp']['energyawareness']['fill'] = 'red'
G.add_edge('hbtp','energyawareness')
G.edge['hbtp']['energyawareness']['write-read'] = '[write read][append read]'
G.add_edge('hbtp','healthd')
G.edge['hbtp']['healthd']['write-read'] = '[write read]'
G.edge['hbtp']['healthd']['fill'] = 'red'
G.add_edge('hbtp','healthd')
G.edge['hbtp']['healthd']['write-read'] = '[write read][append read]'
G.add_edge('hbtp','hvdcp')
G.edge['hbtp']['hvdcp']['write-read'] = '[write read]'
G.edge['hbtp']['hvdcp']['fill'] = 'red'
G.add_edge('hbtp','hvdcp')
G.edge['hbtp']['hvdcp']['write-read'] = '[write read][append read]'
G.add_edge('hbtp','netd')
G.edge['hbtp']['netd']['write-read'] = '[write read]'
G.edge['hbtp']['netd']['fill'] = 'red'
G.add_edge('hbtp','netd')
G.edge['hbtp']['netd']['write-read'] = '[write read][append read]'
G.add_edge('hbtp','rild')
G.edge['hbtp']['rild']['write-read'] = '[write read]'
G.edge['hbtp']['rild']['fill'] = 'red'
G.add_edge('hbtp','rild')
G.edge['hbtp']['rild']['write-read'] = '[write read][append read]'
G.add_edge('hbtp','s_system_app')
G.edge['hbtp']['s_system_app']['read-write'] = '* >read'
G.add_edge('hbtp','surfaceflinger')
G.edge['hbtp']['surfaceflinger']['write-read'] = '[write read]'
G.edge['hbtp']['surfaceflinger']['fill'] = 'red'
G.add_edge('hbtp','surfaceflinger')
G.edge['hbtp']['surfaceflinger']['write-read'] = '[write read][append read]'
G.add_edge('hbtp','system_server')
G.edge['hbtp']['system_server']['write-read'] = '[write read]'
G.edge['hbtp']['system_server']['fill'] = 'red'
G.add_edge('hbtp','system_server')
G.edge['hbtp']['system_server']['write-read'] = '[write read][append read]'
G.add_edge('hbtp','thermald')
G.edge['hbtp']['thermald']['read-write'] = '* >read'
G.add_edge('hbtp','ueventd')
G.edge['hbtp']['ueventd']['write-read'] = '[write read]'
G.edge['hbtp']['ueventd']['fill'] = 'red'
G.add_edge('hbtp','ueventd')
G.edge['hbtp']['ueventd']['write-read'] = '[write read][append read]'
G.add_edge('hbtp','vold')
G.edge['hbtp']['vold']['write-read'] = '[write read]'
G.edge['hbtp']['vold']['fill'] = 'red'
G.add_edge('hbtp','vold')
G.edge['hbtp']['vold']['write-read'] = '[write read][append read]'
G.add_edge('hbtp','wfdservice')
G.edge['hbtp']['wfdservice']['write-read'] = '[write read]'
G.edge['hbtp']['wfdservice']['fill'] = 'red'
G.add_edge('hbtp','wfdservice')
G.edge['hbtp']['wfdservice']['write-read'] = '[write read][append read]'
G.add_edge('healthd','energy-awareness')
G.edge['healthd']['energy-awareness']['write-read'] = '[setattr getattr]'
G.add_edge('healthd','energyawareness')
G.edge['healthd']['energyawareness']['write-read'] = '[setattr getattr]'
G.add_edge('healthd','healthd')
G.edge['healthd']['healthd']['write-read'] = '[setattr getattr]'
G.add_edge('healthd','hvdcp')
G.edge['healthd']['hvdcp']['write-read'] = '[setattr getattr]'
G.add_edge('healthd','ime_app')
G.edge['healthd']['ime_app']['write-read'] = '[setattr getattr]'
G.add_edge('healthd','netd')
G.edge['healthd']['netd']['write-read'] = '[setattr getattr]'
G.add_edge('healthd','rild')
G.edge['healthd']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('healthd','s_system_app')
G.edge['healthd']['s_system_app']['read-write'] = '* >getattr'
G.add_edge('healthd','s_system_app')
G.edge['healthd']['s_system_app']['write-read'] = '[setattr getattr]'
G.add_edge('healthd','surfaceflinger')
G.edge['healthd']['surfaceflinger']['write-read'] = '[setattr getattr]'
G.add_edge('healthd','system_app')
G.edge['healthd']['system_app']['write-read'] = '[setattr getattr]'
G.add_edge('healthd','system_server')
G.edge['healthd']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('healthd','thermald')
G.edge['healthd']['thermald']['read-write'] = '* >getattr'
G.add_edge('healthd','ueventd')
G.edge['healthd']['ueventd']['write-read'] = '[setattr getattr]'
G.add_edge('healthd','vold')
G.edge['healthd']['vold']['write-read'] = '[setattr getattr]'
G.add_edge('healthd','wfdservice')
G.edge['healthd']['wfdservice']['write-read'] = '[setattr getattr]'
G.add_edge('healthd','energy-awareness')
G.edge['healthd']['energy-awareness']['write-read'] = '[setattr getattr][write read]'
G.edge['healthd']['energy-awareness']['fill'] = 'red'
G.add_edge('healthd','energy-awareness')
G.edge['healthd']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('healthd','energyawareness')
G.edge['healthd']['energyawareness']['write-read'] = '[setattr getattr][write read]'
G.edge['healthd']['energyawareness']['fill'] = 'red'
G.add_edge('healthd','energyawareness')
G.edge['healthd']['energyawareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('healthd','healthd')
G.edge['healthd']['healthd']['write-read'] = '[setattr getattr][write read]'
G.edge['healthd']['healthd']['fill'] = 'red'
G.add_edge('healthd','healthd')
G.edge['healthd']['healthd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('healthd','hvdcp')
G.edge['healthd']['hvdcp']['write-read'] = '[setattr getattr][write read]'
G.edge['healthd']['hvdcp']['fill'] = 'red'
G.add_edge('healthd','hvdcp')
G.edge['healthd']['hvdcp']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('healthd','netd')
G.edge['healthd']['netd']['write-read'] = '[setattr getattr][write read]'
G.edge['healthd']['netd']['fill'] = 'red'
G.add_edge('healthd','netd')
G.edge['healthd']['netd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('healthd','rild')
G.edge['healthd']['rild']['write-read'] = '[setattr getattr][write read]'
G.edge['healthd']['rild']['fill'] = 'red'
G.add_edge('healthd','rild')
G.edge['healthd']['rild']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('healthd','s_system_app')
G.edge['healthd']['s_system_app']['read-write'] = '* >read'
G.add_edge('healthd','surfaceflinger')
G.edge['healthd']['surfaceflinger']['write-read'] = '[setattr getattr][write read]'
G.edge['healthd']['surfaceflinger']['fill'] = 'red'
G.add_edge('healthd','surfaceflinger')
G.edge['healthd']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('healthd','system_server')
G.edge['healthd']['system_server']['write-read'] = '[setattr getattr][write read]'
G.edge['healthd']['system_server']['fill'] = 'red'
G.add_edge('healthd','system_server')
G.edge['healthd']['system_server']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('healthd','thermald')
G.edge['healthd']['thermald']['read-write'] = '* >read'
G.add_edge('healthd','ueventd')
G.edge['healthd']['ueventd']['write-read'] = '[setattr getattr][write read]'
G.edge['healthd']['ueventd']['fill'] = 'red'
G.add_edge('healthd','ueventd')
G.edge['healthd']['ueventd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('healthd','vold')
G.edge['healthd']['vold']['write-read'] = '[setattr getattr][write read]'
G.edge['healthd']['vold']['fill'] = 'red'
G.add_edge('healthd','vold')
G.edge['healthd']['vold']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('healthd','wfdservice')
G.edge['healthd']['wfdservice']['write-read'] = '[setattr getattr][write read]'
G.edge['healthd']['wfdservice']['fill'] = 'red'
G.add_edge('healthd','wfdservice')
G.edge['healthd']['wfdservice']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('healthd','charger_monitor')
G.edge['healthd']['charger_monitor']['write-read'] = '[setopt getopt]'
G.add_edge('healthd','commonplatformappdomain')
G.edge['healthd']['commonplatformappdomain']['write-read'] = '[setopt getopt]'
G.add_edge('healthd','energy-awareness')
G.edge['healthd']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('healthd','energyawareness')
G.edge['healthd']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('healthd','hbtp')
G.edge['healthd']['hbtp']['write-read'] = '[setopt getopt]'
G.add_edge('healthd','healthd')
G.edge['healthd']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('healthd','hvdcp')
G.edge['healthd']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('healthd','ime_app')
G.edge['healthd']['ime_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('healthd','lpm')
G.edge['healthd']['lpm']['write-read'] = '[setopt getopt]'
G.add_edge('healthd','mpdecision')
G.edge['healthd']['mpdecision']['write-read'] = '[setopt getopt]'
G.add_edge('healthd','mpdecision')
G.edge['healthd']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt]'
G.add_edge('healthd','netd')
G.edge['healthd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('healthd','perfd')
G.edge['healthd']['perfd']['write-read'] = '[setopt getopt]'
G.add_edge('healthd','rild')
G.edge['healthd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('healthd','samsung_app')
G.edge['healthd']['samsung_app']['write-read'] = '[setopt getopt]'
G.add_edge('healthd','ssr_diag')
G.edge['healthd']['ssr_diag']['write-read'] = '[setopt getopt]'
G.add_edge('healthd','s_system_app')
G.edge['healthd']['s_system_app']['read-write'] = '* >getopt'
G.add_edge('healthd','s_system_app')
G.edge['healthd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('healthd','surfaceflinger')
G.edge['healthd']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('healthd','system_app')
G.edge['healthd']['system_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('healthd','system_server')
G.edge['healthd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('healthd','thermald')
G.edge['healthd']['thermald']['read-write'] = '* >getopt'
G.add_edge('healthd','thermal-engine')
G.edge['healthd']['thermal-engine']['write-read'] = '[setopt getopt]'
G.add_edge('healthd','ueventd')
G.edge['healthd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('healthd','vold')
G.edge['healthd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('healthd','wfdservice')
G.edge['healthd']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('hvdcp','energy-awareness')
G.edge['hvdcp']['energy-awareness']['write-read'] = '[setattr getattr]'
G.add_edge('hvdcp','energyawareness')
G.edge['hvdcp']['energyawareness']['write-read'] = '[setattr getattr]'
G.add_edge('hvdcp','healthd')
G.edge['hvdcp']['healthd']['write-read'] = '[setattr getattr]'
G.add_edge('hvdcp','hvdcp')
G.edge['hvdcp']['hvdcp']['write-read'] = '[setattr getattr]'
G.add_edge('hvdcp','ime_app')
G.edge['hvdcp']['ime_app']['write-read'] = '[setattr getattr]'
G.add_edge('hvdcp','netd')
G.edge['hvdcp']['netd']['write-read'] = '[setattr getattr]'
G.add_edge('hvdcp','rild')
G.edge['hvdcp']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('hvdcp','s_system_app')
G.edge['hvdcp']['s_system_app']['read-write'] = '* >getattr'
G.add_edge('hvdcp','s_system_app')
G.edge['hvdcp']['s_system_app']['write-read'] = '[setattr getattr]'
G.add_edge('hvdcp','surfaceflinger')
G.edge['hvdcp']['surfaceflinger']['write-read'] = '[setattr getattr]'
G.add_edge('hvdcp','system_app')
G.edge['hvdcp']['system_app']['write-read'] = '[setattr getattr]'
G.add_edge('hvdcp','system_server')
G.edge['hvdcp']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('hvdcp','thermald')
G.edge['hvdcp']['thermald']['read-write'] = '* >getattr'
G.add_edge('hvdcp','ueventd')
G.edge['hvdcp']['ueventd']['write-read'] = '[setattr getattr]'
G.add_edge('hvdcp','vold')
G.edge['hvdcp']['vold']['write-read'] = '[setattr getattr]'
G.add_edge('hvdcp','wfdservice')
G.edge['hvdcp']['wfdservice']['write-read'] = '[setattr getattr]'
G.add_edge('hvdcp','energy-awareness')
G.edge['hvdcp']['energy-awareness']['write-read'] = '[setattr getattr][write read]'
G.edge['hvdcp']['energy-awareness']['fill'] = 'red'
G.add_edge('hvdcp','energy-awareness')
G.edge['hvdcp']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('hvdcp','energyawareness')
G.edge['hvdcp']['energyawareness']['write-read'] = '[setattr getattr][write read]'
G.edge['hvdcp']['energyawareness']['fill'] = 'red'
G.add_edge('hvdcp','energyawareness')
G.edge['hvdcp']['energyawareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('hvdcp','healthd')
G.edge['hvdcp']['healthd']['write-read'] = '[setattr getattr][write read]'
G.edge['hvdcp']['healthd']['fill'] = 'red'
G.add_edge('hvdcp','healthd')
G.edge['hvdcp']['healthd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('hvdcp','hvdcp')
G.edge['hvdcp']['hvdcp']['write-read'] = '[setattr getattr][write read]'
G.edge['hvdcp']['hvdcp']['fill'] = 'red'
G.add_edge('hvdcp','hvdcp')
G.edge['hvdcp']['hvdcp']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('hvdcp','netd')
G.edge['hvdcp']['netd']['write-read'] = '[setattr getattr][write read]'
G.edge['hvdcp']['netd']['fill'] = 'red'
G.add_edge('hvdcp','netd')
G.edge['hvdcp']['netd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('hvdcp','rild')
G.edge['hvdcp']['rild']['write-read'] = '[setattr getattr][write read]'
G.edge['hvdcp']['rild']['fill'] = 'red'
G.add_edge('hvdcp','rild')
G.edge['hvdcp']['rild']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('hvdcp','s_system_app')
G.edge['hvdcp']['s_system_app']['read-write'] = '* >read'
G.add_edge('hvdcp','surfaceflinger')
G.edge['hvdcp']['surfaceflinger']['write-read'] = '[setattr getattr][write read]'
G.edge['hvdcp']['surfaceflinger']['fill'] = 'red'
G.add_edge('hvdcp','surfaceflinger')
G.edge['hvdcp']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('hvdcp','system_server')
G.edge['hvdcp']['system_server']['write-read'] = '[setattr getattr][write read]'
G.edge['hvdcp']['system_server']['fill'] = 'red'
G.add_edge('hvdcp','system_server')
G.edge['hvdcp']['system_server']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('hvdcp','thermald')
G.edge['hvdcp']['thermald']['read-write'] = '* >read'
G.add_edge('hvdcp','ueventd')
G.edge['hvdcp']['ueventd']['write-read'] = '[setattr getattr][write read]'
G.edge['hvdcp']['ueventd']['fill'] = 'red'
G.add_edge('hvdcp','ueventd')
G.edge['hvdcp']['ueventd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('hvdcp','vold')
G.edge['hvdcp']['vold']['write-read'] = '[setattr getattr][write read]'
G.edge['hvdcp']['vold']['fill'] = 'red'
G.add_edge('hvdcp','vold')
G.edge['hvdcp']['vold']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('hvdcp','wfdservice')
G.edge['hvdcp']['wfdservice']['write-read'] = '[setattr getattr][write read]'
G.edge['hvdcp']['wfdservice']['fill'] = 'red'
G.add_edge('hvdcp','wfdservice')
G.edge['hvdcp']['wfdservice']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('hvdcp','charger_monitor')
G.edge['hvdcp']['charger_monitor']['write-read'] = '[setopt getopt]'
G.add_edge('hvdcp','commonplatformappdomain')
G.edge['hvdcp']['commonplatformappdomain']['write-read'] = '[setopt getopt]'
G.add_edge('hvdcp','energy-awareness')
G.edge['hvdcp']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('hvdcp','energyawareness')
G.edge['hvdcp']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('hvdcp','hbtp')
G.edge['hvdcp']['hbtp']['write-read'] = '[setopt getopt]'
G.add_edge('hvdcp','healthd')
G.edge['hvdcp']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('hvdcp','hvdcp')
G.edge['hvdcp']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('hvdcp','ime_app')
G.edge['hvdcp']['ime_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('hvdcp','lpm')
G.edge['hvdcp']['lpm']['write-read'] = '[setopt getopt]'
G.add_edge('hvdcp','mpdecision')
G.edge['hvdcp']['mpdecision']['write-read'] = '[setopt getopt]'
G.add_edge('hvdcp','mpdecision')
G.edge['hvdcp']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt]'
G.add_edge('hvdcp','netd')
G.edge['hvdcp']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('hvdcp','perfd')
G.edge['hvdcp']['perfd']['write-read'] = '[setopt getopt]'
G.add_edge('hvdcp','rild')
G.edge['hvdcp']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('hvdcp','samsung_app')
G.edge['hvdcp']['samsung_app']['write-read'] = '[setopt getopt]'
G.add_edge('hvdcp','ssr_diag')
G.edge['hvdcp']['ssr_diag']['write-read'] = '[setopt getopt]'
G.add_edge('hvdcp','s_system_app')
G.edge['hvdcp']['s_system_app']['read-write'] = '* >getopt'
G.add_edge('hvdcp','s_system_app')
G.edge['hvdcp']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('hvdcp','surfaceflinger')
G.edge['hvdcp']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('hvdcp','system_app')
G.edge['hvdcp']['system_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('hvdcp','system_server')
G.edge['hvdcp']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('hvdcp','thermald')
G.edge['hvdcp']['thermald']['read-write'] = '* >getopt'
G.add_edge('hvdcp','thermal-engine')
G.edge['hvdcp']['thermal-engine']['write-read'] = '[setopt getopt]'
G.add_edge('hvdcp','ueventd')
G.edge['hvdcp']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('hvdcp','vold')
G.edge['hvdcp']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('hvdcp','wfdservice')
G.edge['hvdcp']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['read-write'] = '* >recv_msg'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg]'
G.add_edge('ime_app','thermald')
G.edge['ime_app']['thermald']['read-write'] = '* >recv_msg'
G.add_edge('ime_app','energy-awareness')
G.edge['ime_app']['energy-awareness']['write-read'] = '[setattr getattr]'
G.add_edge('ime_app','energyawareness')
G.edge['ime_app']['energyawareness']['write-read'] = '[setattr getattr]'
G.add_edge('ime_app','healthd')
G.edge['ime_app']['healthd']['write-read'] = '[setattr getattr]'
G.add_edge('ime_app','hvdcp')
G.edge['ime_app']['hvdcp']['write-read'] = '[setattr getattr]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr]'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr]'
G.add_edge('ime_app','rild')
G.edge['ime_app']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['read-write'] = '* >getattr'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr]'
G.add_edge('ime_app','surfaceflinger')
G.edge['ime_app']['surfaceflinger']['write-read'] = '[setattr getattr]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('ime_app','thermald')
G.edge['ime_app']['thermald']['read-write'] = '* >getattr'
G.add_edge('ime_app','ueventd')
G.edge['ime_app']['ueventd']['write-read'] = '[setattr getattr]'
G.add_edge('ime_app','vold')
G.edge['ime_app']['vold']['write-read'] = '[setattr getattr]'
G.add_edge('ime_app','wfdservice')
G.edge['ime_app']['wfdservice']['write-read'] = '[setattr getattr]'
G.add_edge('ime_app','energy-awareness')
G.edge['ime_app']['energy-awareness']['write-read'] = '[setattr getattr][write read]'
G.edge['ime_app']['energy-awareness']['fill'] = 'red'
G.add_edge('ime_app','energy-awareness')
G.edge['ime_app']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('ime_app','energyawareness')
G.edge['ime_app']['energyawareness']['write-read'] = '[setattr getattr][write read]'
G.edge['ime_app']['energyawareness']['fill'] = 'red'
G.add_edge('ime_app','energyawareness')
G.edge['ime_app']['energyawareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('ime_app','healthd')
G.edge['ime_app']['healthd']['write-read'] = '[setattr getattr][write read]'
G.edge['ime_app']['healthd']['fill'] = 'red'
G.add_edge('ime_app','healthd')
G.edge['ime_app']['healthd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('ime_app','hvdcp')
G.edge['ime_app']['hvdcp']['write-read'] = '[setattr getattr][write read]'
G.edge['ime_app']['hvdcp']['fill'] = 'red'
G.add_edge('ime_app','hvdcp')
G.edge['ime_app']['hvdcp']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr][write read]'
G.edge['ime_app']['netd']['fill'] = 'red'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('ime_app','rild')
G.edge['ime_app']['rild']['write-read'] = '[setattr getattr][write read]'
G.edge['ime_app']['rild']['fill'] = 'red'
G.add_edge('ime_app','rild')
G.edge['ime_app']['rild']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['read-write'] = '* >read'
G.add_edge('ime_app','surfaceflinger')
G.edge['ime_app']['surfaceflinger']['write-read'] = '[setattr getattr][write read]'
G.edge['ime_app']['surfaceflinger']['fill'] = 'red'
G.add_edge('ime_app','surfaceflinger')
G.edge['ime_app']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read]'
G.edge['ime_app']['system_server']['fill'] = 'red'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('ime_app','thermald')
G.edge['ime_app']['thermald']['read-write'] = '* >read'
G.add_edge('ime_app','ueventd')
G.edge['ime_app']['ueventd']['write-read'] = '[setattr getattr][write read]'
G.edge['ime_app']['ueventd']['fill'] = 'red'
G.add_edge('ime_app','ueventd')
G.edge['ime_app']['ueventd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('ime_app','vold')
G.edge['ime_app']['vold']['write-read'] = '[setattr getattr][write read]'
G.edge['ime_app']['vold']['fill'] = 'red'
G.add_edge('ime_app','vold')
G.edge['ime_app']['vold']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('ime_app','wfdservice')
G.edge['ime_app']['wfdservice']['write-read'] = '[setattr getattr][write read]'
G.edge['ime_app']['wfdservice']['fill'] = 'red'
G.add_edge('ime_app','wfdservice')
G.edge['ime_app']['wfdservice']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('ime_app','charger_monitor')
G.edge['ime_app']['charger_monitor']['write-read'] = '[setopt getopt]'
G.add_edge('ime_app','commonplatformappdomain')
G.edge['ime_app']['commonplatformappdomain']['write-read'] = '[setopt getopt]'
G.add_edge('ime_app','energy-awareness')
G.edge['ime_app']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('ime_app','energyawareness')
G.edge['ime_app']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('ime_app','hbtp')
G.edge['ime_app']['hbtp']['write-read'] = '[setopt getopt]'
G.add_edge('ime_app','healthd')
G.edge['ime_app']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('ime_app','hvdcp')
G.edge['ime_app']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt]'
G.add_edge('ime_app','lpm')
G.edge['ime_app']['lpm']['write-read'] = '[setopt getopt]'
G.add_edge('ime_app','mpdecision')
G.edge['ime_app']['mpdecision']['write-read'] = '[setopt getopt]'
G.add_edge('ime_app','mpdecision')
G.edge['ime_app']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt]'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('ime_app','perfd')
G.edge['ime_app']['perfd']['write-read'] = '[setopt getopt]'
G.add_edge('ime_app','rild')
G.edge['ime_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('ime_app','samsung_app')
G.edge['ime_app']['samsung_app']['write-read'] = '[setopt getopt]'
G.add_edge('ime_app','ssr_diag')
G.edge['ime_app']['ssr_diag']['write-read'] = '[setopt getopt]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['read-write'] = '* >getopt'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt]'
G.add_edge('ime_app','surfaceflinger')
G.edge['ime_app']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('ime_app','thermald')
G.edge['ime_app']['thermald']['read-write'] = '* >getopt'
G.add_edge('ime_app','thermal-engine')
G.edge['ime_app']['thermal-engine']['write-read'] = '[setopt getopt]'
G.add_edge('ime_app','ueventd')
G.edge['ime_app']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('ime_app','vold')
G.edge['ime_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('ime_app','wfdservice')
G.edge['ime_app']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['read-write'] = '* >recvfrom'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom]'
G.add_edge('ime_app','thermald')
G.edge['ime_app']['thermald']['read-write'] = '* >recvfrom'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['read-write'] = '* >relabelfrom'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom]'
G.add_edge('ime_app','thermald')
G.edge['ime_app']['thermald']['read-write'] = '* >relabelfrom'
G.add_edge('lpm','energy-awareness')
G.edge['lpm']['energy-awareness']['write-read'] = '[write read]'
G.edge['lpm']['energy-awareness']['fill'] = 'red'
G.add_edge('lpm','energy-awareness')
G.edge['lpm']['energy-awareness']['write-read'] = '[write read][append read]'
G.add_edge('lpm','energyawareness')
G.edge['lpm']['energyawareness']['write-read'] = '[write read]'
G.edge['lpm']['energyawareness']['fill'] = 'red'
G.add_edge('lpm','energyawareness')
G.edge['lpm']['energyawareness']['write-read'] = '[write read][append read]'
G.add_edge('lpm','healthd')
G.edge['lpm']['healthd']['write-read'] = '[write read]'
G.edge['lpm']['healthd']['fill'] = 'red'
G.add_edge('lpm','healthd')
G.edge['lpm']['healthd']['write-read'] = '[write read][append read]'
G.add_edge('lpm','hvdcp')
G.edge['lpm']['hvdcp']['write-read'] = '[write read]'
G.edge['lpm']['hvdcp']['fill'] = 'red'
G.add_edge('lpm','hvdcp')
G.edge['lpm']['hvdcp']['write-read'] = '[write read][append read]'
G.add_edge('lpm','netd')
G.edge['lpm']['netd']['write-read'] = '[write read]'
G.edge['lpm']['netd']['fill'] = 'red'
G.add_edge('lpm','netd')
G.edge['lpm']['netd']['write-read'] = '[write read][append read]'
G.add_edge('lpm','rild')
G.edge['lpm']['rild']['write-read'] = '[write read]'
G.edge['lpm']['rild']['fill'] = 'red'
G.add_edge('lpm','rild')
G.edge['lpm']['rild']['write-read'] = '[write read][append read]'
G.add_edge('lpm','s_system_app')
G.edge['lpm']['s_system_app']['read-write'] = '* >read'
G.add_edge('lpm','surfaceflinger')
G.edge['lpm']['surfaceflinger']['write-read'] = '[write read]'
G.edge['lpm']['surfaceflinger']['fill'] = 'red'
G.add_edge('lpm','surfaceflinger')
G.edge['lpm']['surfaceflinger']['write-read'] = '[write read][append read]'
G.add_edge('lpm','system_server')
G.edge['lpm']['system_server']['write-read'] = '[write read]'
G.edge['lpm']['system_server']['fill'] = 'red'
G.add_edge('lpm','system_server')
G.edge['lpm']['system_server']['write-read'] = '[write read][append read]'
G.add_edge('lpm','thermald')
G.edge['lpm']['thermald']['read-write'] = '* >read'
G.add_edge('lpm','ueventd')
G.edge['lpm']['ueventd']['write-read'] = '[write read]'
G.edge['lpm']['ueventd']['fill'] = 'red'
G.add_edge('lpm','ueventd')
G.edge['lpm']['ueventd']['write-read'] = '[write read][append read]'
G.add_edge('lpm','vold')
G.edge['lpm']['vold']['write-read'] = '[write read]'
G.edge['lpm']['vold']['fill'] = 'red'
G.add_edge('lpm','vold')
G.edge['lpm']['vold']['write-read'] = '[write read][append read]'
G.add_edge('lpm','wfdservice')
G.edge['lpm']['wfdservice']['write-read'] = '[write read]'
G.edge['lpm']['wfdservice']['fill'] = 'red'
G.add_edge('lpm','wfdservice')
G.edge['lpm']['wfdservice']['write-read'] = '[write read][append read]'
G.add_edge('mpdecision','energy-awareness')
G.edge['mpdecision']['energy-awareness']['write-read'] = '[write read]'
G.edge['mpdecision']['energy-awareness']['fill'] = 'red'
G.add_edge('mpdecision','energy-awareness')
G.edge['mpdecision']['energy-awareness']['write-read'] = '[write read][append read]'
G.add_edge('mpdecision','energyawareness')
G.edge['mpdecision']['energyawareness']['write-read'] = '[write read]'
G.edge['mpdecision']['energyawareness']['fill'] = 'red'
G.add_edge('mpdecision','energyawareness')
G.edge['mpdecision']['energyawareness']['write-read'] = '[write read][append read]'
G.add_edge('mpdecision','healthd')
G.edge['mpdecision']['healthd']['write-read'] = '[write read]'
G.edge['mpdecision']['healthd']['fill'] = 'red'
G.add_edge('mpdecision','healthd')
G.edge['mpdecision']['healthd']['write-read'] = '[write read][append read]'
G.add_edge('mpdecision','hvdcp')
G.edge['mpdecision']['hvdcp']['write-read'] = '[write read]'
G.edge['mpdecision']['hvdcp']['fill'] = 'red'
G.add_edge('mpdecision','hvdcp')
G.edge['mpdecision']['hvdcp']['write-read'] = '[write read][append read]'
G.add_edge('mpdecision','netd')
G.edge['mpdecision']['netd']['write-read'] = '[write read]'
G.edge['mpdecision']['netd']['fill'] = 'red'
G.add_edge('mpdecision','netd')
G.edge['mpdecision']['netd']['write-read'] = '[write read][append read]'
G.add_edge('mpdecision','rild')
G.edge['mpdecision']['rild']['write-read'] = '[write read]'
G.edge['mpdecision']['rild']['fill'] = 'red'
G.add_edge('mpdecision','rild')
G.edge['mpdecision']['rild']['write-read'] = '[write read][append read]'
G.add_edge('mpdecision','s_system_app')
G.edge['mpdecision']['s_system_app']['read-write'] = '* >read'
G.add_edge('mpdecision','surfaceflinger')
G.edge['mpdecision']['surfaceflinger']['write-read'] = '[write read]'
G.edge['mpdecision']['surfaceflinger']['fill'] = 'red'
G.add_edge('mpdecision','surfaceflinger')
G.edge['mpdecision']['surfaceflinger']['write-read'] = '[write read][append read]'
G.add_edge('mpdecision','system_server')
G.edge['mpdecision']['system_server']['write-read'] = '[write read]'
G.edge['mpdecision']['system_server']['fill'] = 'red'
G.add_edge('mpdecision','system_server')
G.edge['mpdecision']['system_server']['write-read'] = '[write read][append read]'
G.add_edge('mpdecision','thermald')
G.edge['mpdecision']['thermald']['read-write'] = '* >read'
G.add_edge('mpdecision','ueventd')
G.edge['mpdecision']['ueventd']['write-read'] = '[write read]'
G.edge['mpdecision']['ueventd']['fill'] = 'red'
G.add_edge('mpdecision','ueventd')
G.edge['mpdecision']['ueventd']['write-read'] = '[write read][append read]'
G.add_edge('mpdecision','vold')
G.edge['mpdecision']['vold']['write-read'] = '[write read]'
G.edge['mpdecision']['vold']['fill'] = 'red'
G.add_edge('mpdecision','vold')
G.edge['mpdecision']['vold']['write-read'] = '[write read][append read]'
G.add_edge('mpdecision','wfdservice')
G.edge['mpdecision']['wfdservice']['write-read'] = '[write read]'
G.edge['mpdecision']['wfdservice']['fill'] = 'red'
G.add_edge('mpdecision','wfdservice')
G.edge['mpdecision']['wfdservice']['write-read'] = '[write read][append read]'
G.add_edge('mpdecision','energy-awareness')
G.edge['mpdecision']['energy-awareness']['write-read'] = '[write read][append read][write read]'
G.edge['mpdecision']['energy-awareness']['fill'] = 'red'
G.add_edge('mpdecision','energy-awareness')
G.edge['mpdecision']['energy-awareness']['write-read'] = '[write read][append read][write read][append read]'
G.add_edge('mpdecision','energyawareness')
G.edge['mpdecision']['energyawareness']['write-read'] = '[write read][append read][write read]'
G.edge['mpdecision']['energyawareness']['fill'] = 'red'
G.add_edge('mpdecision','energyawareness')
G.edge['mpdecision']['energyawareness']['write-read'] = '[write read][append read][write read][append read]'
G.add_edge('mpdecision','healthd')
G.edge['mpdecision']['healthd']['write-read'] = '[write read][append read][write read]'
G.edge['mpdecision']['healthd']['fill'] = 'red'
G.add_edge('mpdecision','healthd')
G.edge['mpdecision']['healthd']['write-read'] = '[write read][append read][write read][append read]'
G.add_edge('mpdecision','hvdcp')
G.edge['mpdecision']['hvdcp']['write-read'] = '[write read][append read][write read]'
G.edge['mpdecision']['hvdcp']['fill'] = 'red'
G.add_edge('mpdecision','hvdcp')
G.edge['mpdecision']['hvdcp']['write-read'] = '[write read][append read][write read][append read]'
G.add_edge('mpdecision','netd')
G.edge['mpdecision']['netd']['write-read'] = '[write read][append read][write read]'
G.edge['mpdecision']['netd']['fill'] = 'red'
G.add_edge('mpdecision','netd')
G.edge['mpdecision']['netd']['write-read'] = '[write read][append read][write read][append read]'
G.add_edge('mpdecision','rild')
G.edge['mpdecision']['rild']['write-read'] = '[write read][append read][write read]'
G.edge['mpdecision']['rild']['fill'] = 'red'
G.add_edge('mpdecision','rild')
G.edge['mpdecision']['rild']['write-read'] = '[write read][append read][write read][append read]'
G.add_edge('mpdecision','s_system_app')
G.edge['mpdecision']['s_system_app']['read-write'] = '* >read'
G.add_edge('mpdecision','surfaceflinger')
G.edge['mpdecision']['surfaceflinger']['write-read'] = '[write read][append read][write read]'
G.edge['mpdecision']['surfaceflinger']['fill'] = 'red'
G.add_edge('mpdecision','surfaceflinger')
G.edge['mpdecision']['surfaceflinger']['write-read'] = '[write read][append read][write read][append read]'
G.add_edge('mpdecision','system_server')
G.edge['mpdecision']['system_server']['write-read'] = '[write read][append read][write read]'
G.edge['mpdecision']['system_server']['fill'] = 'red'
G.add_edge('mpdecision','system_server')
G.edge['mpdecision']['system_server']['write-read'] = '[write read][append read][write read][append read]'
G.add_edge('mpdecision','thermald')
G.edge['mpdecision']['thermald']['read-write'] = '* >read'
G.add_edge('mpdecision','ueventd')
G.edge['mpdecision']['ueventd']['write-read'] = '[write read][append read][write read]'
G.edge['mpdecision']['ueventd']['fill'] = 'red'
G.add_edge('mpdecision','ueventd')
G.edge['mpdecision']['ueventd']['write-read'] = '[write read][append read][write read][append read]'
G.add_edge('mpdecision','vold')
G.edge['mpdecision']['vold']['write-read'] = '[write read][append read][write read]'
G.edge['mpdecision']['vold']['fill'] = 'red'
G.add_edge('mpdecision','vold')
G.edge['mpdecision']['vold']['write-read'] = '[write read][append read][write read][append read]'
G.add_edge('mpdecision','wfdservice')
G.edge['mpdecision']['wfdservice']['write-read'] = '[write read][append read][write read]'
G.edge['mpdecision']['wfdservice']['fill'] = 'red'
G.add_edge('mpdecision','wfdservice')
G.edge['mpdecision']['wfdservice']['write-read'] = '[write read][append read][write read][append read]'
G.add_edge('netd','energy-awareness')
G.edge['netd']['energy-awareness']['write-read'] = '[setattr getattr]'
G.add_edge('netd','energyawareness')
G.edge['netd']['energyawareness']['write-read'] = '[setattr getattr]'
G.add_edge('netd','healthd')
G.edge['netd']['healthd']['write-read'] = '[setattr getattr]'
G.add_edge('netd','hvdcp')
G.edge['netd']['hvdcp']['write-read'] = '[setattr getattr]'
G.add_edge('netd','ime_app')
G.edge['netd']['ime_app']['write-read'] = '[setattr getattr]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr]'
G.add_edge('netd','rild')
G.edge['netd']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['read-write'] = '* >getattr'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['write-read'] = '[setattr getattr]'
G.add_edge('netd','surfaceflinger')
G.edge['netd']['surfaceflinger']['write-read'] = '[setattr getattr]'
G.add_edge('netd','system_app')
G.edge['netd']['system_app']['write-read'] = '[setattr getattr]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('netd','thermald')
G.edge['netd']['thermald']['read-write'] = '* >getattr'
G.add_edge('netd','ueventd')
G.edge['netd']['ueventd']['write-read'] = '[setattr getattr]'
G.add_edge('netd','vold')
G.edge['netd']['vold']['write-read'] = '[setattr getattr]'
G.add_edge('netd','wfdservice')
G.edge['netd']['wfdservice']['write-read'] = '[setattr getattr]'
G.add_edge('netd','energy-awareness')
G.edge['netd']['energy-awareness']['write-read'] = '[setattr getattr][write read]'
G.edge['netd']['energy-awareness']['fill'] = 'red'
G.add_edge('netd','energy-awareness')
G.edge['netd']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('netd','energyawareness')
G.edge['netd']['energyawareness']['write-read'] = '[setattr getattr][write read]'
G.edge['netd']['energyawareness']['fill'] = 'red'
G.add_edge('netd','energyawareness')
G.edge['netd']['energyawareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('netd','healthd')
G.edge['netd']['healthd']['write-read'] = '[setattr getattr][write read]'
G.edge['netd']['healthd']['fill'] = 'red'
G.add_edge('netd','healthd')
G.edge['netd']['healthd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('netd','hvdcp')
G.edge['netd']['hvdcp']['write-read'] = '[setattr getattr][write read]'
G.edge['netd']['hvdcp']['fill'] = 'red'
G.add_edge('netd','hvdcp')
G.edge['netd']['hvdcp']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read]'
G.edge['netd']['netd']['fill'] = 'red'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('netd','rild')
G.edge['netd']['rild']['write-read'] = '[setattr getattr][write read]'
G.edge['netd']['rild']['fill'] = 'red'
G.add_edge('netd','rild')
G.edge['netd']['rild']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['read-write'] = '* >read'
G.add_edge('netd','surfaceflinger')
G.edge['netd']['surfaceflinger']['write-read'] = '[setattr getattr][write read]'
G.edge['netd']['surfaceflinger']['fill'] = 'red'
G.add_edge('netd','surfaceflinger')
G.edge['netd']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read]'
G.edge['netd']['system_server']['fill'] = 'red'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('netd','thermald')
G.edge['netd']['thermald']['read-write'] = '* >read'
G.add_edge('netd','ueventd')
G.edge['netd']['ueventd']['write-read'] = '[setattr getattr][write read]'
G.edge['netd']['ueventd']['fill'] = 'red'
G.add_edge('netd','ueventd')
G.edge['netd']['ueventd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('netd','vold')
G.edge['netd']['vold']['write-read'] = '[setattr getattr][write read]'
G.edge['netd']['vold']['fill'] = 'red'
G.add_edge('netd','vold')
G.edge['netd']['vold']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('netd','wfdservice')
G.edge['netd']['wfdservice']['write-read'] = '[setattr getattr][write read]'
G.edge['netd']['wfdservice']['fill'] = 'red'
G.add_edge('netd','wfdservice')
G.edge['netd']['wfdservice']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('netd','charger_monitor')
G.edge['netd']['charger_monitor']['write-read'] = '[setopt getopt]'
G.add_edge('netd','commonplatformappdomain')
G.edge['netd']['commonplatformappdomain']['write-read'] = '[setopt getopt]'
G.add_edge('netd','energy-awareness')
G.edge['netd']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('netd','energyawareness')
G.edge['netd']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('netd','hbtp')
G.edge['netd']['hbtp']['write-read'] = '[setopt getopt]'
G.add_edge('netd','healthd')
G.edge['netd']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('netd','hvdcp')
G.edge['netd']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('netd','ime_app')
G.edge['netd']['ime_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('netd','lpm')
G.edge['netd']['lpm']['write-read'] = '[setopt getopt]'
G.add_edge('netd','mpdecision')
G.edge['netd']['mpdecision']['write-read'] = '[setopt getopt]'
G.add_edge('netd','mpdecision')
G.edge['netd']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('netd','perfd')
G.edge['netd']['perfd']['write-read'] = '[setopt getopt]'
G.add_edge('netd','rild')
G.edge['netd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('netd','samsung_app')
G.edge['netd']['samsung_app']['write-read'] = '[setopt getopt]'
G.add_edge('netd','ssr_diag')
G.edge['netd']['ssr_diag']['write-read'] = '[setopt getopt]'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['read-write'] = '* >getopt'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('netd','surfaceflinger')
G.edge['netd']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('netd','system_app')
G.edge['netd']['system_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('netd','thermald')
G.edge['netd']['thermald']['read-write'] = '* >getopt'
G.add_edge('netd','thermal-engine')
G.edge['netd']['thermal-engine']['write-read'] = '[setopt getopt]'
G.add_edge('netd','ueventd')
G.edge['netd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('netd','vold')
G.edge['netd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('netd','wfdservice')
G.edge['netd']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('perfd','energy-awareness')
G.edge['perfd']['energy-awareness']['write-read'] = '[write read]'
G.edge['perfd']['energy-awareness']['fill'] = 'red'
G.add_edge('perfd','energy-awareness')
G.edge['perfd']['energy-awareness']['write-read'] = '[write read][append read]'
G.add_edge('perfd','energyawareness')
G.edge['perfd']['energyawareness']['write-read'] = '[write read]'
G.edge['perfd']['energyawareness']['fill'] = 'red'
G.add_edge('perfd','energyawareness')
G.edge['perfd']['energyawareness']['write-read'] = '[write read][append read]'
G.add_edge('perfd','healthd')
G.edge['perfd']['healthd']['write-read'] = '[write read]'
G.edge['perfd']['healthd']['fill'] = 'red'
G.add_edge('perfd','healthd')
G.edge['perfd']['healthd']['write-read'] = '[write read][append read]'
G.add_edge('perfd','hvdcp')
G.edge['perfd']['hvdcp']['write-read'] = '[write read]'
G.edge['perfd']['hvdcp']['fill'] = 'red'
G.add_edge('perfd','hvdcp')
G.edge['perfd']['hvdcp']['write-read'] = '[write read][append read]'
G.add_edge('perfd','netd')
G.edge['perfd']['netd']['write-read'] = '[write read]'
G.edge['perfd']['netd']['fill'] = 'red'
G.add_edge('perfd','netd')
G.edge['perfd']['netd']['write-read'] = '[write read][append read]'
G.add_edge('perfd','rild')
G.edge['perfd']['rild']['write-read'] = '[write read]'
G.edge['perfd']['rild']['fill'] = 'red'
G.add_edge('perfd','rild')
G.edge['perfd']['rild']['write-read'] = '[write read][append read]'
G.add_edge('perfd','s_system_app')
G.edge['perfd']['s_system_app']['read-write'] = '* >read'
G.add_edge('perfd','surfaceflinger')
G.edge['perfd']['surfaceflinger']['write-read'] = '[write read]'
G.edge['perfd']['surfaceflinger']['fill'] = 'red'
G.add_edge('perfd','surfaceflinger')
G.edge['perfd']['surfaceflinger']['write-read'] = '[write read][append read]'
G.add_edge('perfd','system_server')
G.edge['perfd']['system_server']['write-read'] = '[write read]'
G.edge['perfd']['system_server']['fill'] = 'red'
G.add_edge('perfd','system_server')
G.edge['perfd']['system_server']['write-read'] = '[write read][append read]'
G.add_edge('perfd','thermald')
G.edge['perfd']['thermald']['read-write'] = '* >read'
G.add_edge('perfd','ueventd')
G.edge['perfd']['ueventd']['write-read'] = '[write read]'
G.edge['perfd']['ueventd']['fill'] = 'red'
G.add_edge('perfd','ueventd')
G.edge['perfd']['ueventd']['write-read'] = '[write read][append read]'
G.add_edge('perfd','vold')
G.edge['perfd']['vold']['write-read'] = '[write read]'
G.edge['perfd']['vold']['fill'] = 'red'
G.add_edge('perfd','vold')
G.edge['perfd']['vold']['write-read'] = '[write read][append read]'
G.add_edge('perfd','wfdservice')
G.edge['perfd']['wfdservice']['write-read'] = '[write read]'
G.edge['perfd']['wfdservice']['fill'] = 'red'
G.add_edge('perfd','wfdservice')
G.edge['perfd']['wfdservice']['write-read'] = '[write read][append read]'
G.add_edge('rild','energy-awareness')
G.edge['rild']['energy-awareness']['write-read'] = '[setattr getattr]'
G.add_edge('rild','energyawareness')
G.edge['rild']['energyawareness']['write-read'] = '[setattr getattr]'
G.add_edge('rild','healthd')
G.edge['rild']['healthd']['write-read'] = '[setattr getattr]'
G.add_edge('rild','hvdcp')
G.edge['rild']['hvdcp']['write-read'] = '[setattr getattr]'
G.add_edge('rild','ime_app')
G.edge['rild']['ime_app']['write-read'] = '[setattr getattr]'
G.add_edge('rild','netd')
G.edge['rild']['netd']['write-read'] = '[setattr getattr]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('rild','s_system_app')
G.edge['rild']['s_system_app']['read-write'] = '* >getattr'
G.add_edge('rild','s_system_app')
G.edge['rild']['s_system_app']['write-read'] = '[setattr getattr]'
G.add_edge('rild','surfaceflinger')
G.edge['rild']['surfaceflinger']['write-read'] = '[setattr getattr]'
G.add_edge('rild','system_app')
G.edge['rild']['system_app']['write-read'] = '[setattr getattr]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('rild','thermald')
G.edge['rild']['thermald']['read-write'] = '* >getattr'
G.add_edge('rild','ueventd')
G.edge['rild']['ueventd']['write-read'] = '[setattr getattr]'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr]'
G.add_edge('rild','wfdservice')
G.edge['rild']['wfdservice']['write-read'] = '[setattr getattr]'
G.add_edge('rild','energy-awareness')
G.edge['rild']['energy-awareness']['write-read'] = '[setattr getattr][write read]'
G.edge['rild']['energy-awareness']['fill'] = 'red'
G.add_edge('rild','energy-awareness')
G.edge['rild']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('rild','energyawareness')
G.edge['rild']['energyawareness']['write-read'] = '[setattr getattr][write read]'
G.edge['rild']['energyawareness']['fill'] = 'red'
G.add_edge('rild','energyawareness')
G.edge['rild']['energyawareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('rild','healthd')
G.edge['rild']['healthd']['write-read'] = '[setattr getattr][write read]'
G.edge['rild']['healthd']['fill'] = 'red'
G.add_edge('rild','healthd')
G.edge['rild']['healthd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('rild','hvdcp')
G.edge['rild']['hvdcp']['write-read'] = '[setattr getattr][write read]'
G.edge['rild']['hvdcp']['fill'] = 'red'
G.add_edge('rild','hvdcp')
G.edge['rild']['hvdcp']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('rild','netd')
G.edge['rild']['netd']['write-read'] = '[setattr getattr][write read]'
G.edge['rild']['netd']['fill'] = 'red'
G.add_edge('rild','netd')
G.edge['rild']['netd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read]'
G.edge['rild']['rild']['fill'] = 'red'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('rild','s_system_app')
G.edge['rild']['s_system_app']['read-write'] = '* >read'
G.add_edge('rild','surfaceflinger')
G.edge['rild']['surfaceflinger']['write-read'] = '[setattr getattr][write read]'
G.edge['rild']['surfaceflinger']['fill'] = 'red'
G.add_edge('rild','surfaceflinger')
G.edge['rild']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read]'
G.edge['rild']['system_server']['fill'] = 'red'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('rild','thermald')
G.edge['rild']['thermald']['read-write'] = '* >read'
G.add_edge('rild','ueventd')
G.edge['rild']['ueventd']['write-read'] = '[setattr getattr][write read]'
G.edge['rild']['ueventd']['fill'] = 'red'
G.add_edge('rild','ueventd')
G.edge['rild']['ueventd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr][write read]'
G.edge['rild']['vold']['fill'] = 'red'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('rild','wfdservice')
G.edge['rild']['wfdservice']['write-read'] = '[setattr getattr][write read]'
G.edge['rild']['wfdservice']['fill'] = 'red'
G.add_edge('rild','wfdservice')
G.edge['rild']['wfdservice']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('rild','charger_monitor')
G.edge['rild']['charger_monitor']['write-read'] = '[setopt getopt]'
G.add_edge('rild','commonplatformappdomain')
G.edge['rild']['commonplatformappdomain']['write-read'] = '[setopt getopt]'
G.add_edge('rild','energy-awareness')
G.edge['rild']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('rild','energyawareness')
G.edge['rild']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('rild','hbtp')
G.edge['rild']['hbtp']['write-read'] = '[setopt getopt]'
G.add_edge('rild','healthd')
G.edge['rild']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('rild','hvdcp')
G.edge['rild']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('rild','ime_app')
G.edge['rild']['ime_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('rild','lpm')
G.edge['rild']['lpm']['write-read'] = '[setopt getopt]'
G.add_edge('rild','mpdecision')
G.edge['rild']['mpdecision']['write-read'] = '[setopt getopt]'
G.add_edge('rild','mpdecision')
G.edge['rild']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt]'
G.add_edge('rild','netd')
G.edge['rild']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('rild','perfd')
G.edge['rild']['perfd']['write-read'] = '[setopt getopt]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('rild','samsung_app')
G.edge['rild']['samsung_app']['write-read'] = '[setopt getopt]'
G.add_edge('rild','ssr_diag')
G.edge['rild']['ssr_diag']['write-read'] = '[setopt getopt]'
G.add_edge('rild','s_system_app')
G.edge['rild']['s_system_app']['read-write'] = '* >getopt'
G.add_edge('rild','s_system_app')
G.edge['rild']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('rild','surfaceflinger')
G.edge['rild']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('rild','system_app')
G.edge['rild']['system_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('rild','thermald')
G.edge['rild']['thermald']['read-write'] = '* >getopt'
G.add_edge('rild','thermal-engine')
G.edge['rild']['thermal-engine']['write-read'] = '[setopt getopt]'
G.add_edge('rild','ueventd')
G.edge['rild']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('rild','wfdservice')
G.edge['rild']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('rild','energy-awareness')
G.edge['rild']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['rild']['energy-awareness']['fill'] = 'red'
G.add_edge('rild','energy-awareness')
G.edge['rild']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read]'
G.add_edge('rild','energyawareness')
G.edge['rild']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['rild']['energyawareness']['fill'] = 'red'
G.add_edge('rild','energyawareness')
G.edge['rild']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read]'
G.add_edge('rild','healthd')
G.edge['rild']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['rild']['healthd']['fill'] = 'red'
G.add_edge('rild','healthd')
G.edge['rild']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read]'
G.add_edge('rild','hvdcp')
G.edge['rild']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['rild']['hvdcp']['fill'] = 'red'
G.add_edge('rild','hvdcp')
G.edge['rild']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read]'
G.add_edge('rild','netd')
G.edge['rild']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['rild']['netd']['fill'] = 'red'
G.add_edge('rild','netd')
G.edge['rild']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['rild']['rild']['fill'] = 'red'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read]'
G.add_edge('rild','s_system_app')
G.edge['rild']['s_system_app']['read-write'] = '* >read'
G.add_edge('rild','surfaceflinger')
G.edge['rild']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['rild']['surfaceflinger']['fill'] = 'red'
G.add_edge('rild','surfaceflinger')
G.edge['rild']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['rild']['system_server']['fill'] = 'red'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read]'
G.add_edge('rild','thermald')
G.edge['rild']['thermald']['read-write'] = '* >read'
G.add_edge('rild','ueventd')
G.edge['rild']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['rild']['ueventd']['fill'] = 'red'
G.add_edge('rild','ueventd')
G.edge['rild']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read]'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['rild']['vold']['fill'] = 'red'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read]'
G.add_edge('rild','wfdservice')
G.edge['rild']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['rild']['wfdservice']['fill'] = 'red'
G.add_edge('rild','wfdservice')
G.edge['rild']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read]'
G.add_edge('samsung_app','energy-awareness')
G.edge['samsung_app']['energy-awareness']['write-read'] = '[write read]'
G.edge['samsung_app']['energy-awareness']['fill'] = 'red'
G.add_edge('samsung_app','energy-awareness')
G.edge['samsung_app']['energy-awareness']['write-read'] = '[write read][append read]'
G.add_edge('samsung_app','energyawareness')
G.edge['samsung_app']['energyawareness']['write-read'] = '[write read]'
G.edge['samsung_app']['energyawareness']['fill'] = 'red'
G.add_edge('samsung_app','energyawareness')
G.edge['samsung_app']['energyawareness']['write-read'] = '[write read][append read]'
G.add_edge('samsung_app','healthd')
G.edge['samsung_app']['healthd']['write-read'] = '[write read]'
G.edge['samsung_app']['healthd']['fill'] = 'red'
G.add_edge('samsung_app','healthd')
G.edge['samsung_app']['healthd']['write-read'] = '[write read][append read]'
G.add_edge('samsung_app','hvdcp')
G.edge['samsung_app']['hvdcp']['write-read'] = '[write read]'
G.edge['samsung_app']['hvdcp']['fill'] = 'red'
G.add_edge('samsung_app','hvdcp')
G.edge['samsung_app']['hvdcp']['write-read'] = '[write read][append read]'
G.add_edge('samsung_app','netd')
G.edge['samsung_app']['netd']['write-read'] = '[write read]'
G.edge['samsung_app']['netd']['fill'] = 'red'
G.add_edge('samsung_app','netd')
G.edge['samsung_app']['netd']['write-read'] = '[write read][append read]'
G.add_edge('samsung_app','rild')
G.edge['samsung_app']['rild']['write-read'] = '[write read]'
G.edge['samsung_app']['rild']['fill'] = 'red'
G.add_edge('samsung_app','rild')
G.edge['samsung_app']['rild']['write-read'] = '[write read][append read]'
G.add_edge('samsung_app','s_system_app')
G.edge['samsung_app']['s_system_app']['read-write'] = '* >read'
G.add_edge('samsung_app','surfaceflinger')
G.edge['samsung_app']['surfaceflinger']['write-read'] = '[write read]'
G.edge['samsung_app']['surfaceflinger']['fill'] = 'red'
G.add_edge('samsung_app','surfaceflinger')
G.edge['samsung_app']['surfaceflinger']['write-read'] = '[write read][append read]'
G.add_edge('samsung_app','system_server')
G.edge['samsung_app']['system_server']['write-read'] = '[write read]'
G.edge['samsung_app']['system_server']['fill'] = 'red'
G.add_edge('samsung_app','system_server')
G.edge['samsung_app']['system_server']['write-read'] = '[write read][append read]'
G.add_edge('samsung_app','thermald')
G.edge['samsung_app']['thermald']['read-write'] = '* >read'
G.add_edge('samsung_app','ueventd')
G.edge['samsung_app']['ueventd']['write-read'] = '[write read]'
G.edge['samsung_app']['ueventd']['fill'] = 'red'
G.add_edge('samsung_app','ueventd')
G.edge['samsung_app']['ueventd']['write-read'] = '[write read][append read]'
G.add_edge('samsung_app','vold')
G.edge['samsung_app']['vold']['write-read'] = '[write read]'
G.edge['samsung_app']['vold']['fill'] = 'red'
G.add_edge('samsung_app','vold')
G.edge['samsung_app']['vold']['write-read'] = '[write read][append read]'
G.add_edge('samsung_app','wfdservice')
G.edge['samsung_app']['wfdservice']['write-read'] = '[write read]'
G.edge['samsung_app']['wfdservice']['fill'] = 'red'
G.add_edge('samsung_app','wfdservice')
G.edge['samsung_app']['wfdservice']['write-read'] = '[write read][append read]'
G.add_edge('ssr_diag','energy-awareness')
G.edge['ssr_diag']['energy-awareness']['write-read'] = '[write read]'
G.edge['ssr_diag']['energy-awareness']['fill'] = 'red'
G.add_edge('ssr_diag','energy-awareness')
G.edge['ssr_diag']['energy-awareness']['write-read'] = '[write read][append read]'
G.add_edge('ssr_diag','energyawareness')
G.edge['ssr_diag']['energyawareness']['write-read'] = '[write read]'
G.edge['ssr_diag']['energyawareness']['fill'] = 'red'
G.add_edge('ssr_diag','energyawareness')
G.edge['ssr_diag']['energyawareness']['write-read'] = '[write read][append read]'
G.add_edge('ssr_diag','healthd')
G.edge['ssr_diag']['healthd']['write-read'] = '[write read]'
G.edge['ssr_diag']['healthd']['fill'] = 'red'
G.add_edge('ssr_diag','healthd')
G.edge['ssr_diag']['healthd']['write-read'] = '[write read][append read]'
G.add_edge('ssr_diag','hvdcp')
G.edge['ssr_diag']['hvdcp']['write-read'] = '[write read]'
G.edge['ssr_diag']['hvdcp']['fill'] = 'red'
G.add_edge('ssr_diag','hvdcp')
G.edge['ssr_diag']['hvdcp']['write-read'] = '[write read][append read]'
G.add_edge('ssr_diag','netd')
G.edge['ssr_diag']['netd']['write-read'] = '[write read]'
G.edge['ssr_diag']['netd']['fill'] = 'red'
G.add_edge('ssr_diag','netd')
G.edge['ssr_diag']['netd']['write-read'] = '[write read][append read]'
G.add_edge('ssr_diag','rild')
G.edge['ssr_diag']['rild']['write-read'] = '[write read]'
G.edge['ssr_diag']['rild']['fill'] = 'red'
G.add_edge('ssr_diag','rild')
G.edge['ssr_diag']['rild']['write-read'] = '[write read][append read]'
G.add_edge('ssr_diag','s_system_app')
G.edge['ssr_diag']['s_system_app']['read-write'] = '* >read'
G.add_edge('ssr_diag','surfaceflinger')
G.edge['ssr_diag']['surfaceflinger']['write-read'] = '[write read]'
G.edge['ssr_diag']['surfaceflinger']['fill'] = 'red'
G.add_edge('ssr_diag','surfaceflinger')
G.edge['ssr_diag']['surfaceflinger']['write-read'] = '[write read][append read]'
G.add_edge('ssr_diag','system_server')
G.edge['ssr_diag']['system_server']['write-read'] = '[write read]'
G.edge['ssr_diag']['system_server']['fill'] = 'red'
G.add_edge('ssr_diag','system_server')
G.edge['ssr_diag']['system_server']['write-read'] = '[write read][append read]'
G.add_edge('ssr_diag','thermald')
G.edge['ssr_diag']['thermald']['read-write'] = '* >read'
G.add_edge('ssr_diag','ueventd')
G.edge['ssr_diag']['ueventd']['write-read'] = '[write read]'
G.edge['ssr_diag']['ueventd']['fill'] = 'red'
G.add_edge('ssr_diag','ueventd')
G.edge['ssr_diag']['ueventd']['write-read'] = '[write read][append read]'
G.add_edge('ssr_diag','vold')
G.edge['ssr_diag']['vold']['write-read'] = '[write read]'
G.edge['ssr_diag']['vold']['fill'] = 'red'
G.add_edge('ssr_diag','vold')
G.edge['ssr_diag']['vold']['write-read'] = '[write read][append read]'
G.add_edge('ssr_diag','wfdservice')
G.edge['ssr_diag']['wfdservice']['write-read'] = '[write read]'
G.edge['ssr_diag']['wfdservice']['fill'] = 'red'
G.add_edge('ssr_diag','wfdservice')
G.edge['ssr_diag']['wfdservice']['write-read'] = '[write read][append read]'
G.add_edge('ssr_diag','energy-awareness')
G.edge['ssr_diag']['energy-awareness']['write-read'] = '[write read][append read][write read]'
G.edge['ssr_diag']['energy-awareness']['fill'] = 'red'
G.add_edge('ssr_diag','energy-awareness')
G.edge['ssr_diag']['energy-awareness']['write-read'] = '[write read][append read][write read][append read]'
G.add_edge('ssr_diag','energyawareness')
G.edge['ssr_diag']['energyawareness']['write-read'] = '[write read][append read][write read]'
G.edge['ssr_diag']['energyawareness']['fill'] = 'red'
G.add_edge('ssr_diag','energyawareness')
G.edge['ssr_diag']['energyawareness']['write-read'] = '[write read][append read][write read][append read]'
G.add_edge('ssr_diag','healthd')
G.edge['ssr_diag']['healthd']['write-read'] = '[write read][append read][write read]'
G.edge['ssr_diag']['healthd']['fill'] = 'red'
G.add_edge('ssr_diag','healthd')
G.edge['ssr_diag']['healthd']['write-read'] = '[write read][append read][write read][append read]'
G.add_edge('ssr_diag','hvdcp')
G.edge['ssr_diag']['hvdcp']['write-read'] = '[write read][append read][write read]'
G.edge['ssr_diag']['hvdcp']['fill'] = 'red'
G.add_edge('ssr_diag','hvdcp')
G.edge['ssr_diag']['hvdcp']['write-read'] = '[write read][append read][write read][append read]'
G.add_edge('ssr_diag','netd')
G.edge['ssr_diag']['netd']['write-read'] = '[write read][append read][write read]'
G.edge['ssr_diag']['netd']['fill'] = 'red'
G.add_edge('ssr_diag','netd')
G.edge['ssr_diag']['netd']['write-read'] = '[write read][append read][write read][append read]'
G.add_edge('ssr_diag','rild')
G.edge['ssr_diag']['rild']['write-read'] = '[write read][append read][write read]'
G.edge['ssr_diag']['rild']['fill'] = 'red'
G.add_edge('ssr_diag','rild')
G.edge['ssr_diag']['rild']['write-read'] = '[write read][append read][write read][append read]'
G.add_edge('ssr_diag','s_system_app')
G.edge['ssr_diag']['s_system_app']['read-write'] = '* >read'
G.add_edge('ssr_diag','surfaceflinger')
G.edge['ssr_diag']['surfaceflinger']['write-read'] = '[write read][append read][write read]'
G.edge['ssr_diag']['surfaceflinger']['fill'] = 'red'
G.add_edge('ssr_diag','surfaceflinger')
G.edge['ssr_diag']['surfaceflinger']['write-read'] = '[write read][append read][write read][append read]'
G.add_edge('ssr_diag','system_server')
G.edge['ssr_diag']['system_server']['write-read'] = '[write read][append read][write read]'
G.edge['ssr_diag']['system_server']['fill'] = 'red'
G.add_edge('ssr_diag','system_server')
G.edge['ssr_diag']['system_server']['write-read'] = '[write read][append read][write read][append read]'
G.add_edge('ssr_diag','thermald')
G.edge['ssr_diag']['thermald']['read-write'] = '* >read'
G.add_edge('ssr_diag','ueventd')
G.edge['ssr_diag']['ueventd']['write-read'] = '[write read][append read][write read]'
G.edge['ssr_diag']['ueventd']['fill'] = 'red'
G.add_edge('ssr_diag','ueventd')
G.edge['ssr_diag']['ueventd']['write-read'] = '[write read][append read][write read][append read]'
G.add_edge('ssr_diag','vold')
G.edge['ssr_diag']['vold']['write-read'] = '[write read][append read][write read]'
G.edge['ssr_diag']['vold']['fill'] = 'red'
G.add_edge('ssr_diag','vold')
G.edge['ssr_diag']['vold']['write-read'] = '[write read][append read][write read][append read]'
G.add_edge('ssr_diag','wfdservice')
G.edge['ssr_diag']['wfdservice']['write-read'] = '[write read][append read][write read]'
G.edge['ssr_diag']['wfdservice']['fill'] = 'red'
G.add_edge('ssr_diag','wfdservice')
G.edge['ssr_diag']['wfdservice']['write-read'] = '[write read][append read][write read][append read]'
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','charger_monitor')
G.add_edge('s_system_app','commonplatformappdomain')
G.add_edge('s_system_app','energy-awareness')
G.add_edge('s_system_app','energyawareness')
G.add_edge('s_system_app','hbtp')
G.add_edge('s_system_app','healthd')
G.add_edge('s_system_app','hvdcp')
G.add_edge('s_system_app','ime_app')
G.add_edge('s_system_app','lpm')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','mpdecision')
G.add_edge('s_system_app','netd')
G.add_edge('s_system_app','perfd')
G.add_edge('s_system_app','rild')
G.add_edge('s_system_app','samsung_app')
G.add_edge('s_system_app','ssr_diag')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','s_system_app')
G.add_edge('s_system_app','surfaceflinger')
G.add_edge('s_system_app','system_app')
G.add_edge('s_system_app','system_server')
G.add_edge('s_system_app','thermald')
G.add_edge('s_system_app','thermal-engine')
G.add_edge('s_system_app','ueventd')
G.add_edge('s_system_app','vold')
G.add_edge('s_system_app','wfdservice')
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['read-write'] = '* >recv_msg'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg]'
G.add_edge('s_system_app','thermald')
G.edge['s_system_app']['thermald']['read-write'] = '* >recv_msg'
G.add_edge('s_system_app','energy-awareness')
G.edge['s_system_app']['energy-awareness']['write-read'] = '[setattr getattr]'
G.add_edge('s_system_app','energyawareness')
G.edge['s_system_app']['energyawareness']['write-read'] = '[setattr getattr]'
G.add_edge('s_system_app','healthd')
G.edge['s_system_app']['healthd']['write-read'] = '[setattr getattr]'
G.add_edge('s_system_app','hvdcp')
G.edge['s_system_app']['hvdcp']['write-read'] = '[setattr getattr]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr]'
G.add_edge('s_system_app','rild')
G.edge['s_system_app']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['read-write'] = '* >getattr'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr]'
G.add_edge('s_system_app','surfaceflinger')
G.edge['s_system_app']['surfaceflinger']['write-read'] = '[setattr getattr]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('s_system_app','thermald')
G.edge['s_system_app']['thermald']['read-write'] = '* >getattr'
G.add_edge('s_system_app','ueventd')
G.edge['s_system_app']['ueventd']['write-read'] = '[setattr getattr]'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr]'
G.add_edge('s_system_app','wfdservice')
G.edge['s_system_app']['wfdservice']['write-read'] = '[setattr getattr]'
G.add_edge('s_system_app','energy-awareness')
G.edge['s_system_app']['energy-awareness']['write-read'] = '[setattr getattr][write read]'
G.edge['s_system_app']['energy-awareness']['fill'] = 'red'
G.add_edge('s_system_app','energy-awareness')
G.edge['s_system_app']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('s_system_app','energyawareness')
G.edge['s_system_app']['energyawareness']['write-read'] = '[setattr getattr][write read]'
G.edge['s_system_app']['energyawareness']['fill'] = 'red'
G.add_edge('s_system_app','energyawareness')
G.edge['s_system_app']['energyawareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('s_system_app','healthd')
G.edge['s_system_app']['healthd']['write-read'] = '[setattr getattr][write read]'
G.edge['s_system_app']['healthd']['fill'] = 'red'
G.add_edge('s_system_app','healthd')
G.edge['s_system_app']['healthd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('s_system_app','hvdcp')
G.edge['s_system_app']['hvdcp']['write-read'] = '[setattr getattr][write read]'
G.edge['s_system_app']['hvdcp']['fill'] = 'red'
G.add_edge('s_system_app','hvdcp')
G.edge['s_system_app']['hvdcp']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read]'
G.edge['s_system_app']['netd']['fill'] = 'red'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('s_system_app','rild')
G.edge['s_system_app']['rild']['write-read'] = '[setattr getattr][write read]'
G.edge['s_system_app']['rild']['fill'] = 'red'
G.add_edge('s_system_app','rild')
G.edge['s_system_app']['rild']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['read-write'] = '* >read'
G.add_edge('s_system_app','surfaceflinger')
G.edge['s_system_app']['surfaceflinger']['write-read'] = '[setattr getattr][write read]'
G.edge['s_system_app']['surfaceflinger']['fill'] = 'red'
G.add_edge('s_system_app','surfaceflinger')
G.edge['s_system_app']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read]'
G.edge['s_system_app']['system_server']['fill'] = 'red'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('s_system_app','thermald')
G.edge['s_system_app']['thermald']['read-write'] = '* >read'
G.add_edge('s_system_app','ueventd')
G.edge['s_system_app']['ueventd']['write-read'] = '[setattr getattr][write read]'
G.edge['s_system_app']['ueventd']['fill'] = 'red'
G.add_edge('s_system_app','ueventd')
G.edge['s_system_app']['ueventd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read]'
G.edge['s_system_app']['vold']['fill'] = 'red'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('s_system_app','wfdservice')
G.edge['s_system_app']['wfdservice']['write-read'] = '[setattr getattr][write read]'
G.edge['s_system_app']['wfdservice']['fill'] = 'red'
G.add_edge('s_system_app','wfdservice')
G.edge['s_system_app']['wfdservice']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('s_system_app','charger_monitor')
G.edge['s_system_app']['charger_monitor']['write-read'] = '[setopt getopt]'
G.add_edge('s_system_app','commonplatformappdomain')
G.edge['s_system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt]'
G.add_edge('s_system_app','energy-awareness')
G.edge['s_system_app']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('s_system_app','energyawareness')
G.edge['s_system_app']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('s_system_app','hbtp')
G.edge['s_system_app']['hbtp']['write-read'] = '[setopt getopt]'
G.add_edge('s_system_app','healthd')
G.edge['s_system_app']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('s_system_app','hvdcp')
G.edge['s_system_app']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt]'
G.add_edge('s_system_app','lpm')
G.edge['s_system_app']['lpm']['write-read'] = '[setopt getopt]'
G.add_edge('s_system_app','mpdecision')
G.edge['s_system_app']['mpdecision']['write-read'] = '[setopt getopt]'
G.add_edge('s_system_app','mpdecision')
G.edge['s_system_app']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('s_system_app','perfd')
G.edge['s_system_app']['perfd']['write-read'] = '[setopt getopt]'
G.add_edge('s_system_app','rild')
G.edge['s_system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('s_system_app','samsung_app')
G.edge['s_system_app']['samsung_app']['write-read'] = '[setopt getopt]'
G.add_edge('s_system_app','ssr_diag')
G.edge['s_system_app']['ssr_diag']['write-read'] = '[setopt getopt]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['read-write'] = '* >getopt'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt]'
G.add_edge('s_system_app','surfaceflinger')
G.edge['s_system_app']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('s_system_app','thermald')
G.edge['s_system_app']['thermald']['read-write'] = '* >getopt'
G.add_edge('s_system_app','thermal-engine')
G.edge['s_system_app']['thermal-engine']['write-read'] = '[setopt getopt]'
G.add_edge('s_system_app','ueventd')
G.edge['s_system_app']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('s_system_app','wfdservice')
G.edge['s_system_app']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['read-write'] = '* >recvfrom'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom]'
G.add_edge('s_system_app','thermald')
G.edge['s_system_app']['thermald']['read-write'] = '* >recvfrom'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['read-write'] = '* >relabelfrom'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom]'
G.add_edge('s_system_app','thermald')
G.edge['s_system_app']['thermald']['read-write'] = '* >relabelfrom'
G.add_edge('surfaceflinger','energy-awareness')
G.edge['surfaceflinger']['energy-awareness']['write-read'] = '[setattr getattr]'
G.add_edge('surfaceflinger','energyawareness')
G.edge['surfaceflinger']['energyawareness']['write-read'] = '[setattr getattr]'
G.add_edge('surfaceflinger','healthd')
G.edge['surfaceflinger']['healthd']['write-read'] = '[setattr getattr]'
G.add_edge('surfaceflinger','hvdcp')
G.edge['surfaceflinger']['hvdcp']['write-read'] = '[setattr getattr]'
G.add_edge('surfaceflinger','ime_app')
G.edge['surfaceflinger']['ime_app']['write-read'] = '[setattr getattr]'
G.add_edge('surfaceflinger','netd')
G.edge['surfaceflinger']['netd']['write-read'] = '[setattr getattr]'
G.add_edge('surfaceflinger','rild')
G.edge['surfaceflinger']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('surfaceflinger','s_system_app')
G.edge['surfaceflinger']['s_system_app']['read-write'] = '* >getattr'
G.add_edge('surfaceflinger','s_system_app')
G.edge['surfaceflinger']['s_system_app']['write-read'] = '[setattr getattr]'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr]'
G.add_edge('surfaceflinger','system_app')
G.edge['surfaceflinger']['system_app']['write-read'] = '[setattr getattr]'
G.add_edge('surfaceflinger','system_server')
G.edge['surfaceflinger']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('surfaceflinger','thermald')
G.edge['surfaceflinger']['thermald']['read-write'] = '* >getattr'
G.add_edge('surfaceflinger','ueventd')
G.edge['surfaceflinger']['ueventd']['write-read'] = '[setattr getattr]'
G.add_edge('surfaceflinger','vold')
G.edge['surfaceflinger']['vold']['write-read'] = '[setattr getattr]'
G.add_edge('surfaceflinger','wfdservice')
G.edge['surfaceflinger']['wfdservice']['write-read'] = '[setattr getattr]'
G.add_edge('surfaceflinger','energy-awareness')
G.edge['surfaceflinger']['energy-awareness']['write-read'] = '[setattr getattr][write read]'
G.edge['surfaceflinger']['energy-awareness']['fill'] = 'red'
G.add_edge('surfaceflinger','energy-awareness')
G.edge['surfaceflinger']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('surfaceflinger','energyawareness')
G.edge['surfaceflinger']['energyawareness']['write-read'] = '[setattr getattr][write read]'
G.edge['surfaceflinger']['energyawareness']['fill'] = 'red'
G.add_edge('surfaceflinger','energyawareness')
G.edge['surfaceflinger']['energyawareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('surfaceflinger','healthd')
G.edge['surfaceflinger']['healthd']['write-read'] = '[setattr getattr][write read]'
G.edge['surfaceflinger']['healthd']['fill'] = 'red'
G.add_edge('surfaceflinger','healthd')
G.edge['surfaceflinger']['healthd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('surfaceflinger','hvdcp')
G.edge['surfaceflinger']['hvdcp']['write-read'] = '[setattr getattr][write read]'
G.edge['surfaceflinger']['hvdcp']['fill'] = 'red'
G.add_edge('surfaceflinger','hvdcp')
G.edge['surfaceflinger']['hvdcp']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('surfaceflinger','netd')
G.edge['surfaceflinger']['netd']['write-read'] = '[setattr getattr][write read]'
G.edge['surfaceflinger']['netd']['fill'] = 'red'
G.add_edge('surfaceflinger','netd')
G.edge['surfaceflinger']['netd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('surfaceflinger','rild')
G.edge['surfaceflinger']['rild']['write-read'] = '[setattr getattr][write read]'
G.edge['surfaceflinger']['rild']['fill'] = 'red'
G.add_edge('surfaceflinger','rild')
G.edge['surfaceflinger']['rild']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('surfaceflinger','s_system_app')
G.edge['surfaceflinger']['s_system_app']['read-write'] = '* >read'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read]'
G.edge['surfaceflinger']['surfaceflinger']['fill'] = 'red'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('surfaceflinger','system_server')
G.edge['surfaceflinger']['system_server']['write-read'] = '[setattr getattr][write read]'
G.edge['surfaceflinger']['system_server']['fill'] = 'red'
G.add_edge('surfaceflinger','system_server')
G.edge['surfaceflinger']['system_server']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('surfaceflinger','thermald')
G.edge['surfaceflinger']['thermald']['read-write'] = '* >read'
G.add_edge('surfaceflinger','ueventd')
G.edge['surfaceflinger']['ueventd']['write-read'] = '[setattr getattr][write read]'
G.edge['surfaceflinger']['ueventd']['fill'] = 'red'
G.add_edge('surfaceflinger','ueventd')
G.edge['surfaceflinger']['ueventd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('surfaceflinger','vold')
G.edge['surfaceflinger']['vold']['write-read'] = '[setattr getattr][write read]'
G.edge['surfaceflinger']['vold']['fill'] = 'red'
G.add_edge('surfaceflinger','vold')
G.edge['surfaceflinger']['vold']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('surfaceflinger','wfdservice')
G.edge['surfaceflinger']['wfdservice']['write-read'] = '[setattr getattr][write read]'
G.edge['surfaceflinger']['wfdservice']['fill'] = 'red'
G.add_edge('surfaceflinger','wfdservice')
G.edge['surfaceflinger']['wfdservice']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('surfaceflinger','charger_monitor')
G.edge['surfaceflinger']['charger_monitor']['write-read'] = '[setopt getopt]'
G.add_edge('surfaceflinger','commonplatformappdomain')
G.edge['surfaceflinger']['commonplatformappdomain']['write-read'] = '[setopt getopt]'
G.add_edge('surfaceflinger','energy-awareness')
G.edge['surfaceflinger']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('surfaceflinger','energyawareness')
G.edge['surfaceflinger']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('surfaceflinger','hbtp')
G.edge['surfaceflinger']['hbtp']['write-read'] = '[setopt getopt]'
G.add_edge('surfaceflinger','healthd')
G.edge['surfaceflinger']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('surfaceflinger','hvdcp')
G.edge['surfaceflinger']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('surfaceflinger','ime_app')
G.edge['surfaceflinger']['ime_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('surfaceflinger','lpm')
G.edge['surfaceflinger']['lpm']['write-read'] = '[setopt getopt]'
G.add_edge('surfaceflinger','mpdecision')
G.edge['surfaceflinger']['mpdecision']['write-read'] = '[setopt getopt]'
G.add_edge('surfaceflinger','mpdecision')
G.edge['surfaceflinger']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt]'
G.add_edge('surfaceflinger','netd')
G.edge['surfaceflinger']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('surfaceflinger','perfd')
G.edge['surfaceflinger']['perfd']['write-read'] = '[setopt getopt]'
G.add_edge('surfaceflinger','rild')
G.edge['surfaceflinger']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('surfaceflinger','samsung_app')
G.edge['surfaceflinger']['samsung_app']['write-read'] = '[setopt getopt]'
G.add_edge('surfaceflinger','ssr_diag')
G.edge['surfaceflinger']['ssr_diag']['write-read'] = '[setopt getopt]'
G.add_edge('surfaceflinger','s_system_app')
G.edge['surfaceflinger']['s_system_app']['read-write'] = '* >getopt'
G.add_edge('surfaceflinger','s_system_app')
G.edge['surfaceflinger']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('surfaceflinger','system_app')
G.edge['surfaceflinger']['system_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('surfaceflinger','system_server')
G.edge['surfaceflinger']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('surfaceflinger','thermald')
G.edge['surfaceflinger']['thermald']['read-write'] = '* >getopt'
G.add_edge('surfaceflinger','thermal-engine')
G.edge['surfaceflinger']['thermal-engine']['write-read'] = '[setopt getopt]'
G.add_edge('surfaceflinger','ueventd')
G.edge['surfaceflinger']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('surfaceflinger','vold')
G.edge['surfaceflinger']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('surfaceflinger','wfdservice')
G.edge['surfaceflinger']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['read-write'] = '* >recv_msg'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg]'
G.add_edge('system_app','thermald')
G.edge['system_app']['thermald']['read-write'] = '* >recv_msg'
G.add_edge('system_app','energy-awareness')
G.edge['system_app']['energy-awareness']['write-read'] = '[setattr getattr]'
G.add_edge('system_app','energyawareness')
G.edge['system_app']['energyawareness']['write-read'] = '[setattr getattr]'
G.add_edge('system_app','healthd')
G.edge['system_app']['healthd']['write-read'] = '[setattr getattr]'
G.add_edge('system_app','hvdcp')
G.edge['system_app']['hvdcp']['write-read'] = '[setattr getattr]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr]'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr]'
G.add_edge('system_app','rild')
G.edge['system_app']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['read-write'] = '* >getattr'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr]'
G.add_edge('system_app','surfaceflinger')
G.edge['system_app']['surfaceflinger']['write-read'] = '[setattr getattr]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('system_app','thermald')
G.edge['system_app']['thermald']['read-write'] = '* >getattr'
G.add_edge('system_app','ueventd')
G.edge['system_app']['ueventd']['write-read'] = '[setattr getattr]'
G.add_edge('system_app','vold')
G.edge['system_app']['vold']['write-read'] = '[setattr getattr]'
G.add_edge('system_app','wfdservice')
G.edge['system_app']['wfdservice']['write-read'] = '[setattr getattr]'
G.add_edge('system_app','energy-awareness')
G.edge['system_app']['energy-awareness']['write-read'] = '[setattr getattr][write read]'
G.edge['system_app']['energy-awareness']['fill'] = 'red'
G.add_edge('system_app','energy-awareness')
G.edge['system_app']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('system_app','energyawareness')
G.edge['system_app']['energyawareness']['write-read'] = '[setattr getattr][write read]'
G.edge['system_app']['energyawareness']['fill'] = 'red'
G.add_edge('system_app','energyawareness')
G.edge['system_app']['energyawareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('system_app','healthd')
G.edge['system_app']['healthd']['write-read'] = '[setattr getattr][write read]'
G.edge['system_app']['healthd']['fill'] = 'red'
G.add_edge('system_app','healthd')
G.edge['system_app']['healthd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('system_app','hvdcp')
G.edge['system_app']['hvdcp']['write-read'] = '[setattr getattr][write read]'
G.edge['system_app']['hvdcp']['fill'] = 'red'
G.add_edge('system_app','hvdcp')
G.edge['system_app']['hvdcp']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr][write read]'
G.edge['system_app']['netd']['fill'] = 'red'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('system_app','rild')
G.edge['system_app']['rild']['write-read'] = '[setattr getattr][write read]'
G.edge['system_app']['rild']['fill'] = 'red'
G.add_edge('system_app','rild')
G.edge['system_app']['rild']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['read-write'] = '* >read'
G.add_edge('system_app','surfaceflinger')
G.edge['system_app']['surfaceflinger']['write-read'] = '[setattr getattr][write read]'
G.edge['system_app']['surfaceflinger']['fill'] = 'red'
G.add_edge('system_app','surfaceflinger')
G.edge['system_app']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read]'
G.edge['system_app']['system_server']['fill'] = 'red'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('system_app','thermald')
G.edge['system_app']['thermald']['read-write'] = '* >read'
G.add_edge('system_app','ueventd')
G.edge['system_app']['ueventd']['write-read'] = '[setattr getattr][write read]'
G.edge['system_app']['ueventd']['fill'] = 'red'
G.add_edge('system_app','ueventd')
G.edge['system_app']['ueventd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('system_app','vold')
G.edge['system_app']['vold']['write-read'] = '[setattr getattr][write read]'
G.edge['system_app']['vold']['fill'] = 'red'
G.add_edge('system_app','vold')
G.edge['system_app']['vold']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('system_app','wfdservice')
G.edge['system_app']['wfdservice']['write-read'] = '[setattr getattr][write read]'
G.edge['system_app']['wfdservice']['fill'] = 'red'
G.add_edge('system_app','wfdservice')
G.edge['system_app']['wfdservice']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('system_app','charger_monitor')
G.edge['system_app']['charger_monitor']['write-read'] = '[setopt getopt]'
G.add_edge('system_app','commonplatformappdomain')
G.edge['system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt]'
G.add_edge('system_app','energy-awareness')
G.edge['system_app']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_app','energyawareness')
G.edge['system_app']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_app','hbtp')
G.edge['system_app']['hbtp']['write-read'] = '[setopt getopt]'
G.add_edge('system_app','healthd')
G.edge['system_app']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_app','hvdcp')
G.edge['system_app']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt]'
G.add_edge('system_app','lpm')
G.edge['system_app']['lpm']['write-read'] = '[setopt getopt]'
G.add_edge('system_app','mpdecision')
G.edge['system_app']['mpdecision']['write-read'] = '[setopt getopt]'
G.add_edge('system_app','mpdecision')
G.edge['system_app']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt]'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_app','perfd')
G.edge['system_app']['perfd']['write-read'] = '[setopt getopt]'
G.add_edge('system_app','rild')
G.edge['system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_app','samsung_app')
G.edge['system_app']['samsung_app']['write-read'] = '[setopt getopt]'
G.add_edge('system_app','ssr_diag')
G.edge['system_app']['ssr_diag']['write-read'] = '[setopt getopt]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['read-write'] = '* >getopt'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt]'
G.add_edge('system_app','surfaceflinger')
G.edge['system_app']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_app','thermald')
G.edge['system_app']['thermald']['read-write'] = '* >getopt'
G.add_edge('system_app','thermal-engine')
G.edge['system_app']['thermal-engine']['write-read'] = '[setopt getopt]'
G.add_edge('system_app','ueventd')
G.edge['system_app']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_app','vold')
G.edge['system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_app','wfdservice')
G.edge['system_app']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['read-write'] = '* >recvfrom'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom]'
G.add_edge('system_app','thermald')
G.edge['system_app']['thermald']['read-write'] = '* >recvfrom'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['read-write'] = '* >relabelfrom'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom]'
G.add_edge('system_app','thermald')
G.edge['system_app']['thermald']['read-write'] = '* >relabelfrom'
G.add_edge('system_server','energy-awareness')
G.edge['system_server']['energy-awareness']['write-read'] = '[setattr getattr]'
G.add_edge('system_server','energyawareness')
G.edge['system_server']['energyawareness']['write-read'] = '[setattr getattr]'
G.add_edge('system_server','healthd')
G.edge['system_server']['healthd']['write-read'] = '[setattr getattr]'
G.add_edge('system_server','hvdcp')
G.edge['system_server']['hvdcp']['write-read'] = '[setattr getattr]'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['read-write'] = '* >getattr'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('system_server','surfaceflinger')
G.edge['system_server']['surfaceflinger']['write-read'] = '[setattr getattr]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('system_server','thermald')
G.edge['system_server']['thermald']['read-write'] = '* >getattr'
G.add_edge('system_server','ueventd')
G.edge['system_server']['ueventd']['write-read'] = '[setattr getattr]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr]'
G.add_edge('system_server','wfdservice')
G.edge['system_server']['wfdservice']['write-read'] = '[setattr getattr]'
G.add_edge('system_server','energy-awareness')
G.edge['system_server']['energy-awareness']['write-read'] = '[setattr getattr][write read]'
G.edge['system_server']['energy-awareness']['fill'] = 'red'
G.add_edge('system_server','energy-awareness')
G.edge['system_server']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('system_server','energyawareness')
G.edge['system_server']['energyawareness']['write-read'] = '[setattr getattr][write read]'
G.edge['system_server']['energyawareness']['fill'] = 'red'
G.add_edge('system_server','energyawareness')
G.edge['system_server']['energyawareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('system_server','healthd')
G.edge['system_server']['healthd']['write-read'] = '[setattr getattr][write read]'
G.edge['system_server']['healthd']['fill'] = 'red'
G.add_edge('system_server','healthd')
G.edge['system_server']['healthd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('system_server','hvdcp')
G.edge['system_server']['hvdcp']['write-read'] = '[setattr getattr][write read]'
G.edge['system_server']['hvdcp']['fill'] = 'red'
G.add_edge('system_server','hvdcp')
G.edge['system_server']['hvdcp']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read]'
G.edge['system_server']['netd']['fill'] = 'red'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read]'
G.edge['system_server']['rild']['fill'] = 'red'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['read-write'] = '* >read'
G.add_edge('system_server','surfaceflinger')
G.edge['system_server']['surfaceflinger']['write-read'] = '[setattr getattr][write read]'
G.edge['system_server']['surfaceflinger']['fill'] = 'red'
G.add_edge('system_server','surfaceflinger')
G.edge['system_server']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('system_server','thermald')
G.edge['system_server']['thermald']['read-write'] = '* >read'
G.add_edge('system_server','ueventd')
G.edge['system_server']['ueventd']['write-read'] = '[setattr getattr][write read]'
G.edge['system_server']['ueventd']['fill'] = 'red'
G.add_edge('system_server','ueventd')
G.edge['system_server']['ueventd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read]'
G.edge['system_server']['vold']['fill'] = 'red'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('system_server','wfdservice')
G.edge['system_server']['wfdservice']['write-read'] = '[setattr getattr][write read]'
G.edge['system_server']['wfdservice']['fill'] = 'red'
G.add_edge('system_server','wfdservice')
G.edge['system_server']['wfdservice']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('system_server','charger_monitor')
G.edge['system_server']['charger_monitor']['write-read'] = '[setopt getopt]'
G.add_edge('system_server','commonplatformappdomain')
G.edge['system_server']['commonplatformappdomain']['write-read'] = '[setopt getopt]'
G.add_edge('system_server','energy-awareness')
G.edge['system_server']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_server','energyawareness')
G.edge['system_server']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_server','hbtp')
G.edge['system_server']['hbtp']['write-read'] = '[setopt getopt]'
G.add_edge('system_server','healthd')
G.edge['system_server']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_server','hvdcp')
G.edge['system_server']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt]'
G.add_edge('system_server','lpm')
G.edge['system_server']['lpm']['write-read'] = '[setopt getopt]'
G.add_edge('system_server','mpdecision')
G.edge['system_server']['mpdecision']['write-read'] = '[setopt getopt]'
G.add_edge('system_server','mpdecision')
G.edge['system_server']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt]'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_server','perfd')
G.edge['system_server']['perfd']['write-read'] = '[setopt getopt]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_server','samsung_app')
G.edge['system_server']['samsung_app']['write-read'] = '[setopt getopt]'
G.add_edge('system_server','ssr_diag')
G.edge['system_server']['ssr_diag']['write-read'] = '[setopt getopt]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['read-write'] = '* >getopt'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt]'
G.add_edge('system_server','surfaceflinger')
G.edge['system_server']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_server','thermald')
G.edge['system_server']['thermald']['read-write'] = '* >getopt'
G.add_edge('system_server','thermal-engine')
G.edge['system_server']['thermal-engine']['write-read'] = '[setopt getopt]'
G.add_edge('system_server','ueventd')
G.edge['system_server']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_server','wfdservice')
G.edge['system_server']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermald','charger_monitor')
G.add_edge('thermald','commonplatformappdomain')
G.add_edge('thermald','energy-awareness')
G.add_edge('thermald','energyawareness')
G.add_edge('thermald','hbtp')
G.add_edge('thermald','healthd')
G.add_edge('thermald','hvdcp')
G.add_edge('thermald','ime_app')
G.add_edge('thermald','lpm')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','mpdecision')
G.add_edge('thermald','netd')
G.add_edge('thermald','perfd')
G.add_edge('thermald','rild')
G.add_edge('thermald','samsung_app')
G.add_edge('thermald','ssr_diag')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','s_system_app')
G.add_edge('thermald','surfaceflinger')
G.add_edge('thermald','system_app')
G.add_edge('thermald','system_server')
G.add_edge('thermald','thermald')
G.add_edge('thermald','thermal-engine')
G.add_edge('thermald','ueventd')
G.add_edge('thermald','vold')
G.add_edge('thermald','wfdservice')
G.add_edge('thermal-engine','energy-awareness')
G.edge['thermal-engine']['energy-awareness']['write-read'] = '[write read]'
G.edge['thermal-engine']['energy-awareness']['fill'] = 'red'
G.add_edge('thermal-engine','energy-awareness')
G.edge['thermal-engine']['energy-awareness']['write-read'] = '[write read][append read]'
G.add_edge('thermal-engine','energyawareness')
G.edge['thermal-engine']['energyawareness']['write-read'] = '[write read]'
G.edge['thermal-engine']['energyawareness']['fill'] = 'red'
G.add_edge('thermal-engine','energyawareness')
G.edge['thermal-engine']['energyawareness']['write-read'] = '[write read][append read]'
G.add_edge('thermal-engine','healthd')
G.edge['thermal-engine']['healthd']['write-read'] = '[write read]'
G.edge['thermal-engine']['healthd']['fill'] = 'red'
G.add_edge('thermal-engine','healthd')
G.edge['thermal-engine']['healthd']['write-read'] = '[write read][append read]'
G.add_edge('thermal-engine','hvdcp')
G.edge['thermal-engine']['hvdcp']['write-read'] = '[write read]'
G.edge['thermal-engine']['hvdcp']['fill'] = 'red'
G.add_edge('thermal-engine','hvdcp')
G.edge['thermal-engine']['hvdcp']['write-read'] = '[write read][append read]'
G.add_edge('thermal-engine','netd')
G.edge['thermal-engine']['netd']['write-read'] = '[write read]'
G.edge['thermal-engine']['netd']['fill'] = 'red'
G.add_edge('thermal-engine','netd')
G.edge['thermal-engine']['netd']['write-read'] = '[write read][append read]'
G.add_edge('thermal-engine','rild')
G.edge['thermal-engine']['rild']['write-read'] = '[write read]'
G.edge['thermal-engine']['rild']['fill'] = 'red'
G.add_edge('thermal-engine','rild')
G.edge['thermal-engine']['rild']['write-read'] = '[write read][append read]'
G.add_edge('thermal-engine','s_system_app')
G.edge['thermal-engine']['s_system_app']['read-write'] = '* >read'
G.add_edge('thermal-engine','surfaceflinger')
G.edge['thermal-engine']['surfaceflinger']['write-read'] = '[write read]'
G.edge['thermal-engine']['surfaceflinger']['fill'] = 'red'
G.add_edge('thermal-engine','surfaceflinger')
G.edge['thermal-engine']['surfaceflinger']['write-read'] = '[write read][append read]'
G.add_edge('thermal-engine','system_server')
G.edge['thermal-engine']['system_server']['write-read'] = '[write read]'
G.edge['thermal-engine']['system_server']['fill'] = 'red'
G.add_edge('thermal-engine','system_server')
G.edge['thermal-engine']['system_server']['write-read'] = '[write read][append read]'
G.add_edge('thermal-engine','thermald')
G.edge['thermal-engine']['thermald']['read-write'] = '* >read'
G.add_edge('thermal-engine','ueventd')
G.edge['thermal-engine']['ueventd']['write-read'] = '[write read]'
G.edge['thermal-engine']['ueventd']['fill'] = 'red'
G.add_edge('thermal-engine','ueventd')
G.edge['thermal-engine']['ueventd']['write-read'] = '[write read][append read]'
G.add_edge('thermal-engine','vold')
G.edge['thermal-engine']['vold']['write-read'] = '[write read]'
G.edge['thermal-engine']['vold']['fill'] = 'red'
G.add_edge('thermal-engine','vold')
G.edge['thermal-engine']['vold']['write-read'] = '[write read][append read]'
G.add_edge('thermal-engine','wfdservice')
G.edge['thermal-engine']['wfdservice']['write-read'] = '[write read]'
G.edge['thermal-engine']['wfdservice']['fill'] = 'red'
G.add_edge('thermal-engine','wfdservice')
G.edge['thermal-engine']['wfdservice']['write-read'] = '[write read][append read]'
G.add_edge('ueventd','energy-awareness')
G.edge['ueventd']['energy-awareness']['write-read'] = '[setattr getattr]'
G.add_edge('ueventd','energyawareness')
G.edge['ueventd']['energyawareness']['write-read'] = '[setattr getattr]'
G.add_edge('ueventd','healthd')
G.edge['ueventd']['healthd']['write-read'] = '[setattr getattr]'
G.add_edge('ueventd','hvdcp')
G.edge['ueventd']['hvdcp']['write-read'] = '[setattr getattr]'
G.add_edge('ueventd','ime_app')
G.edge['ueventd']['ime_app']['write-read'] = '[setattr getattr]'
G.add_edge('ueventd','netd')
G.edge['ueventd']['netd']['write-read'] = '[setattr getattr]'
G.add_edge('ueventd','rild')
G.edge['ueventd']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('ueventd','s_system_app')
G.edge['ueventd']['s_system_app']['read-write'] = '* >getattr'
G.add_edge('ueventd','s_system_app')
G.edge['ueventd']['s_system_app']['write-read'] = '[setattr getattr]'
G.add_edge('ueventd','surfaceflinger')
G.edge['ueventd']['surfaceflinger']['write-read'] = '[setattr getattr]'
G.add_edge('ueventd','system_app')
G.edge['ueventd']['system_app']['write-read'] = '[setattr getattr]'
G.add_edge('ueventd','system_server')
G.edge['ueventd']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('ueventd','thermald')
G.edge['ueventd']['thermald']['read-write'] = '* >getattr'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr]'
G.add_edge('ueventd','vold')
G.edge['ueventd']['vold']['write-read'] = '[setattr getattr]'
G.add_edge('ueventd','wfdservice')
G.edge['ueventd']['wfdservice']['write-read'] = '[setattr getattr]'
G.add_edge('ueventd','energy-awareness')
G.edge['ueventd']['energy-awareness']['write-read'] = '[setattr getattr][write read]'
G.edge['ueventd']['energy-awareness']['fill'] = 'red'
G.add_edge('ueventd','energy-awareness')
G.edge['ueventd']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('ueventd','energyawareness')
G.edge['ueventd']['energyawareness']['write-read'] = '[setattr getattr][write read]'
G.edge['ueventd']['energyawareness']['fill'] = 'red'
G.add_edge('ueventd','energyawareness')
G.edge['ueventd']['energyawareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('ueventd','healthd')
G.edge['ueventd']['healthd']['write-read'] = '[setattr getattr][write read]'
G.edge['ueventd']['healthd']['fill'] = 'red'
G.add_edge('ueventd','healthd')
G.edge['ueventd']['healthd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('ueventd','hvdcp')
G.edge['ueventd']['hvdcp']['write-read'] = '[setattr getattr][write read]'
G.edge['ueventd']['hvdcp']['fill'] = 'red'
G.add_edge('ueventd','hvdcp')
G.edge['ueventd']['hvdcp']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('ueventd','netd')
G.edge['ueventd']['netd']['write-read'] = '[setattr getattr][write read]'
G.edge['ueventd']['netd']['fill'] = 'red'
G.add_edge('ueventd','netd')
G.edge['ueventd']['netd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('ueventd','rild')
G.edge['ueventd']['rild']['write-read'] = '[setattr getattr][write read]'
G.edge['ueventd']['rild']['fill'] = 'red'
G.add_edge('ueventd','rild')
G.edge['ueventd']['rild']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('ueventd','s_system_app')
G.edge['ueventd']['s_system_app']['read-write'] = '* >read'
G.add_edge('ueventd','surfaceflinger')
G.edge['ueventd']['surfaceflinger']['write-read'] = '[setattr getattr][write read]'
G.edge['ueventd']['surfaceflinger']['fill'] = 'red'
G.add_edge('ueventd','surfaceflinger')
G.edge['ueventd']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('ueventd','system_server')
G.edge['ueventd']['system_server']['write-read'] = '[setattr getattr][write read]'
G.edge['ueventd']['system_server']['fill'] = 'red'
G.add_edge('ueventd','system_server')
G.edge['ueventd']['system_server']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('ueventd','thermald')
G.edge['ueventd']['thermald']['read-write'] = '* >read'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read]'
G.edge['ueventd']['ueventd']['fill'] = 'red'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('ueventd','vold')
G.edge['ueventd']['vold']['write-read'] = '[setattr getattr][write read]'
G.edge['ueventd']['vold']['fill'] = 'red'
G.add_edge('ueventd','vold')
G.edge['ueventd']['vold']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('ueventd','wfdservice')
G.edge['ueventd']['wfdservice']['write-read'] = '[setattr getattr][write read]'
G.edge['ueventd']['wfdservice']['fill'] = 'red'
G.add_edge('ueventd','wfdservice')
G.edge['ueventd']['wfdservice']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('ueventd','charger_monitor')
G.edge['ueventd']['charger_monitor']['write-read'] = '[setopt getopt]'
G.add_edge('ueventd','commonplatformappdomain')
G.edge['ueventd']['commonplatformappdomain']['write-read'] = '[setopt getopt]'
G.add_edge('ueventd','energy-awareness')
G.edge['ueventd']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('ueventd','energyawareness')
G.edge['ueventd']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('ueventd','hbtp')
G.edge['ueventd']['hbtp']['write-read'] = '[setopt getopt]'
G.add_edge('ueventd','healthd')
G.edge['ueventd']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('ueventd','hvdcp')
G.edge['ueventd']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('ueventd','ime_app')
G.edge['ueventd']['ime_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('ueventd','lpm')
G.edge['ueventd']['lpm']['write-read'] = '[setopt getopt]'
G.add_edge('ueventd','mpdecision')
G.edge['ueventd']['mpdecision']['write-read'] = '[setopt getopt]'
G.add_edge('ueventd','mpdecision')
G.edge['ueventd']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt]'
G.add_edge('ueventd','netd')
G.edge['ueventd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('ueventd','perfd')
G.edge['ueventd']['perfd']['write-read'] = '[setopt getopt]'
G.add_edge('ueventd','rild')
G.edge['ueventd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('ueventd','samsung_app')
G.edge['ueventd']['samsung_app']['write-read'] = '[setopt getopt]'
G.add_edge('ueventd','ssr_diag')
G.edge['ueventd']['ssr_diag']['write-read'] = '[setopt getopt]'
G.add_edge('ueventd','s_system_app')
G.edge['ueventd']['s_system_app']['read-write'] = '* >getopt'
G.add_edge('ueventd','s_system_app')
G.edge['ueventd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('ueventd','surfaceflinger')
G.edge['ueventd']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('ueventd','system_app')
G.edge['ueventd']['system_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('ueventd','system_server')
G.edge['ueventd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('ueventd','thermald')
G.edge['ueventd']['thermald']['read-write'] = '* >getopt'
G.add_edge('ueventd','thermal-engine')
G.edge['ueventd']['thermal-engine']['write-read'] = '[setopt getopt]'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('ueventd','vold')
G.edge['ueventd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('ueventd','wfdservice')
G.edge['ueventd']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('vold','energy-awareness')
G.edge['vold']['energy-awareness']['write-read'] = '[setattr getattr]'
G.add_edge('vold','energyawareness')
G.edge['vold']['energyawareness']['write-read'] = '[setattr getattr]'
G.add_edge('vold','healthd')
G.edge['vold']['healthd']['write-read'] = '[setattr getattr]'
G.add_edge('vold','hvdcp')
G.edge['vold']['hvdcp']['write-read'] = '[setattr getattr]'
G.add_edge('vold','ime_app')
G.edge['vold']['ime_app']['write-read'] = '[setattr getattr]'
G.add_edge('vold','netd')
G.edge['vold']['netd']['write-read'] = '[setattr getattr]'
G.add_edge('vold','rild')
G.edge['vold']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['read-write'] = '* >getattr'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['write-read'] = '[setattr getattr]'
G.add_edge('vold','surfaceflinger')
G.edge['vold']['surfaceflinger']['write-read'] = '[setattr getattr]'
G.add_edge('vold','system_app')
G.edge['vold']['system_app']['write-read'] = '[setattr getattr]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('vold','thermald')
G.edge['vold']['thermald']['read-write'] = '* >getattr'
G.add_edge('vold','ueventd')
G.edge['vold']['ueventd']['write-read'] = '[setattr getattr]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr]'
G.add_edge('vold','wfdservice')
G.edge['vold']['wfdservice']['write-read'] = '[setattr getattr]'
G.add_edge('vold','energy-awareness')
G.edge['vold']['energy-awareness']['write-read'] = '[setattr getattr][write read]'
G.edge['vold']['energy-awareness']['fill'] = 'red'
G.add_edge('vold','energy-awareness')
G.edge['vold']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('vold','energyawareness')
G.edge['vold']['energyawareness']['write-read'] = '[setattr getattr][write read]'
G.edge['vold']['energyawareness']['fill'] = 'red'
G.add_edge('vold','energyawareness')
G.edge['vold']['energyawareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('vold','healthd')
G.edge['vold']['healthd']['write-read'] = '[setattr getattr][write read]'
G.edge['vold']['healthd']['fill'] = 'red'
G.add_edge('vold','healthd')
G.edge['vold']['healthd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('vold','hvdcp')
G.edge['vold']['hvdcp']['write-read'] = '[setattr getattr][write read]'
G.edge['vold']['hvdcp']['fill'] = 'red'
G.add_edge('vold','hvdcp')
G.edge['vold']['hvdcp']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('vold','netd')
G.edge['vold']['netd']['write-read'] = '[setattr getattr][write read]'
G.edge['vold']['netd']['fill'] = 'red'
G.add_edge('vold','netd')
G.edge['vold']['netd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('vold','rild')
G.edge['vold']['rild']['write-read'] = '[setattr getattr][write read]'
G.edge['vold']['rild']['fill'] = 'red'
G.add_edge('vold','rild')
G.edge['vold']['rild']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['read-write'] = '* >read'
G.add_edge('vold','surfaceflinger')
G.edge['vold']['surfaceflinger']['write-read'] = '[setattr getattr][write read]'
G.edge['vold']['surfaceflinger']['fill'] = 'red'
G.add_edge('vold','surfaceflinger')
G.edge['vold']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read]'
G.edge['vold']['system_server']['fill'] = 'red'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('vold','thermald')
G.edge['vold']['thermald']['read-write'] = '* >read'
G.add_edge('vold','ueventd')
G.edge['vold']['ueventd']['write-read'] = '[setattr getattr][write read]'
G.edge['vold']['ueventd']['fill'] = 'red'
G.add_edge('vold','ueventd')
G.edge['vold']['ueventd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read]'
G.edge['vold']['vold']['fill'] = 'red'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('vold','wfdservice')
G.edge['vold']['wfdservice']['write-read'] = '[setattr getattr][write read]'
G.edge['vold']['wfdservice']['fill'] = 'red'
G.add_edge('vold','wfdservice')
G.edge['vold']['wfdservice']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('vold','charger_monitor')
G.edge['vold']['charger_monitor']['write-read'] = '[setopt getopt]'
G.add_edge('vold','commonplatformappdomain')
G.edge['vold']['commonplatformappdomain']['write-read'] = '[setopt getopt]'
G.add_edge('vold','energy-awareness')
G.edge['vold']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('vold','energyawareness')
G.edge['vold']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('vold','hbtp')
G.edge['vold']['hbtp']['write-read'] = '[setopt getopt]'
G.add_edge('vold','healthd')
G.edge['vold']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('vold','hvdcp')
G.edge['vold']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('vold','ime_app')
G.edge['vold']['ime_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('vold','lpm')
G.edge['vold']['lpm']['write-read'] = '[setopt getopt]'
G.add_edge('vold','mpdecision')
G.edge['vold']['mpdecision']['write-read'] = '[setopt getopt]'
G.add_edge('vold','mpdecision')
G.edge['vold']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt]'
G.add_edge('vold','netd')
G.edge['vold']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('vold','perfd')
G.edge['vold']['perfd']['write-read'] = '[setopt getopt]'
G.add_edge('vold','rild')
G.edge['vold']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('vold','samsung_app')
G.edge['vold']['samsung_app']['write-read'] = '[setopt getopt]'
G.add_edge('vold','ssr_diag')
G.edge['vold']['ssr_diag']['write-read'] = '[setopt getopt]'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['read-write'] = '* >getopt'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('vold','surfaceflinger')
G.edge['vold']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('vold','system_app')
G.edge['vold']['system_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('vold','thermald')
G.edge['vold']['thermald']['read-write'] = '* >getopt'
G.add_edge('vold','thermal-engine')
G.edge['vold']['thermal-engine']['write-read'] = '[setopt getopt]'
G.add_edge('vold','ueventd')
G.edge['vold']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('vold','wfdservice')
G.edge['vold']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('wfdservice','energy-awareness')
G.edge['wfdservice']['energy-awareness']['write-read'] = '[setattr getattr]'
G.add_edge('wfdservice','energyawareness')
G.edge['wfdservice']['energyawareness']['write-read'] = '[setattr getattr]'
G.add_edge('wfdservice','healthd')
G.edge['wfdservice']['healthd']['write-read'] = '[setattr getattr]'
G.add_edge('wfdservice','hvdcp')
G.edge['wfdservice']['hvdcp']['write-read'] = '[setattr getattr]'
G.add_edge('wfdservice','ime_app')
G.edge['wfdservice']['ime_app']['write-read'] = '[setattr getattr]'
G.add_edge('wfdservice','netd')
G.edge['wfdservice']['netd']['write-read'] = '[setattr getattr]'
G.add_edge('wfdservice','rild')
G.edge['wfdservice']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('wfdservice','s_system_app')
G.edge['wfdservice']['s_system_app']['read-write'] = '* >getattr'
G.add_edge('wfdservice','s_system_app')
G.edge['wfdservice']['s_system_app']['write-read'] = '[setattr getattr]'
G.add_edge('wfdservice','surfaceflinger')
G.edge['wfdservice']['surfaceflinger']['write-read'] = '[setattr getattr]'
G.add_edge('wfdservice','system_app')
G.edge['wfdservice']['system_app']['write-read'] = '[setattr getattr]'
G.add_edge('wfdservice','system_server')
G.edge['wfdservice']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('wfdservice','thermald')
G.edge['wfdservice']['thermald']['read-write'] = '* >getattr'
G.add_edge('wfdservice','ueventd')
G.edge['wfdservice']['ueventd']['write-read'] = '[setattr getattr]'
G.add_edge('wfdservice','vold')
G.edge['wfdservice']['vold']['write-read'] = '[setattr getattr]'
G.add_edge('wfdservice','wfdservice')
G.edge['wfdservice']['wfdservice']['write-read'] = '[setattr getattr]'
G.add_edge('wfdservice','energy-awareness')
G.edge['wfdservice']['energy-awareness']['write-read'] = '[setattr getattr][write read]'
G.edge['wfdservice']['energy-awareness']['fill'] = 'red'
G.add_edge('wfdservice','energy-awareness')
G.edge['wfdservice']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('wfdservice','energyawareness')
G.edge['wfdservice']['energyawareness']['write-read'] = '[setattr getattr][write read]'
G.edge['wfdservice']['energyawareness']['fill'] = 'red'
G.add_edge('wfdservice','energyawareness')
G.edge['wfdservice']['energyawareness']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('wfdservice','healthd')
G.edge['wfdservice']['healthd']['write-read'] = '[setattr getattr][write read]'
G.edge['wfdservice']['healthd']['fill'] = 'red'
G.add_edge('wfdservice','healthd')
G.edge['wfdservice']['healthd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('wfdservice','hvdcp')
G.edge['wfdservice']['hvdcp']['write-read'] = '[setattr getattr][write read]'
G.edge['wfdservice']['hvdcp']['fill'] = 'red'
G.add_edge('wfdservice','hvdcp')
G.edge['wfdservice']['hvdcp']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('wfdservice','netd')
G.edge['wfdservice']['netd']['write-read'] = '[setattr getattr][write read]'
G.edge['wfdservice']['netd']['fill'] = 'red'
G.add_edge('wfdservice','netd')
G.edge['wfdservice']['netd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('wfdservice','rild')
G.edge['wfdservice']['rild']['write-read'] = '[setattr getattr][write read]'
G.edge['wfdservice']['rild']['fill'] = 'red'
G.add_edge('wfdservice','rild')
G.edge['wfdservice']['rild']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('wfdservice','s_system_app')
G.edge['wfdservice']['s_system_app']['read-write'] = '* >read'
G.add_edge('wfdservice','surfaceflinger')
G.edge['wfdservice']['surfaceflinger']['write-read'] = '[setattr getattr][write read]'
G.edge['wfdservice']['surfaceflinger']['fill'] = 'red'
G.add_edge('wfdservice','surfaceflinger')
G.edge['wfdservice']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('wfdservice','system_server')
G.edge['wfdservice']['system_server']['write-read'] = '[setattr getattr][write read]'
G.edge['wfdservice']['system_server']['fill'] = 'red'
G.add_edge('wfdservice','system_server')
G.edge['wfdservice']['system_server']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('wfdservice','thermald')
G.edge['wfdservice']['thermald']['read-write'] = '* >read'
G.add_edge('wfdservice','ueventd')
G.edge['wfdservice']['ueventd']['write-read'] = '[setattr getattr][write read]'
G.edge['wfdservice']['ueventd']['fill'] = 'red'
G.add_edge('wfdservice','ueventd')
G.edge['wfdservice']['ueventd']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('wfdservice','vold')
G.edge['wfdservice']['vold']['write-read'] = '[setattr getattr][write read]'
G.edge['wfdservice']['vold']['fill'] = 'red'
G.add_edge('wfdservice','vold')
G.edge['wfdservice']['vold']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('wfdservice','wfdservice')
G.edge['wfdservice']['wfdservice']['write-read'] = '[setattr getattr][write read]'
G.edge['wfdservice']['wfdservice']['fill'] = 'red'
G.add_edge('wfdservice','wfdservice')
G.edge['wfdservice']['wfdservice']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('wfdservice','charger_monitor')
G.edge['wfdservice']['charger_monitor']['write-read'] = '[setopt getopt]'
G.add_edge('wfdservice','commonplatformappdomain')
G.edge['wfdservice']['commonplatformappdomain']['write-read'] = '[setopt getopt]'
G.add_edge('wfdservice','energy-awareness')
G.edge['wfdservice']['energy-awareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('wfdservice','energyawareness')
G.edge['wfdservice']['energyawareness']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('wfdservice','hbtp')
G.edge['wfdservice']['hbtp']['write-read'] = '[setopt getopt]'
G.add_edge('wfdservice','healthd')
G.edge['wfdservice']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('wfdservice','hvdcp')
G.edge['wfdservice']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('wfdservice','ime_app')
G.edge['wfdservice']['ime_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('wfdservice','lpm')
G.edge['wfdservice']['lpm']['write-read'] = '[setopt getopt]'
G.add_edge('wfdservice','mpdecision')
G.edge['wfdservice']['mpdecision']['write-read'] = '[setopt getopt]'
G.add_edge('wfdservice','mpdecision')
G.edge['wfdservice']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt]'
G.add_edge('wfdservice','netd')
G.edge['wfdservice']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('wfdservice','perfd')
G.edge['wfdservice']['perfd']['write-read'] = '[setopt getopt]'
G.add_edge('wfdservice','rild')
G.edge['wfdservice']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('wfdservice','samsung_app')
G.edge['wfdservice']['samsung_app']['write-read'] = '[setopt getopt]'
G.add_edge('wfdservice','ssr_diag')
G.edge['wfdservice']['ssr_diag']['write-read'] = '[setopt getopt]'
G.add_edge('wfdservice','s_system_app')
G.edge['wfdservice']['s_system_app']['read-write'] = '* >getopt'
G.add_edge('wfdservice','s_system_app')
G.edge['wfdservice']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('wfdservice','surfaceflinger')
G.edge['wfdservice']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('wfdservice','system_app')
G.edge['wfdservice']['system_app']['write-read'] = '[setattr getattr][setopt getopt]'
G.add_edge('wfdservice','system_server')
G.edge['wfdservice']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('wfdservice','thermald')
G.edge['wfdservice']['thermald']['read-write'] = '* >getopt'
G.add_edge('wfdservice','thermal-engine')
G.edge['wfdservice']['thermal-engine']['write-read'] = '[setopt getopt]'
G.add_edge('wfdservice','ueventd')
G.edge['wfdservice']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('wfdservice','vold')
G.edge['wfdservice']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('wfdservice','wfdservice')
G.edge['wfdservice']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
app = Viewer(G)
app.mainloop()