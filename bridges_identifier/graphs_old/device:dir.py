import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('cbd','cbd')
G.edge['cbd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('cbd','init_shell')
G.edge['cbd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('cbd','mpdecision')
G.edge['cbd']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('cbd','rild')
G.edge['cbd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('cbd','rtcc')
G.edge['cbd']['rtcc']['write-read'] = '[open open]'
G.add_edge('cbd','sdcardd')
G.edge['cbd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('cbd','vold')
G.edge['cbd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('cbd','init_shell')
G.edge['cbd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('cbd','vold')
G.edge['cbd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('cbd','cbd')
G.edge['cbd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['cbd']['cbd']['fill'] = 'red'
G.add_edge('cbd','healthd')
G.edge['cbd']['healthd']['write-read'] = '[write read]'
G.edge['cbd']['healthd']['fill'] = 'red'
G.add_edge('cbd','init_shell')
G.edge['cbd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['cbd']['init_shell']['fill'] = 'red'
G.add_edge('cbd','mpdecision')
G.edge['cbd']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['cbd']['mpdecision']['fill'] = 'red'
G.add_edge('cbd','rild')
G.edge['cbd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['cbd']['rild']['fill'] = 'red'
G.add_edge('cbd','rtcc')
G.edge['cbd']['rtcc']['write-read'] = '[open open][write read]'
G.edge['cbd']['rtcc']['fill'] = 'red'
G.add_edge('cbd','sdcardd')
G.edge['cbd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['cbd']['sdcardd']['fill'] = 'red'
G.add_edge('cbd','ueventd')
G.edge['cbd']['ueventd']['write-read'] = '[write read]'
G.edge['cbd']['ueventd']['fill'] = 'red'
G.add_edge('cbd','vold')
G.edge['cbd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['cbd']['vold']['fill'] = 'red'
G.add_edge('cbd','vold')
G.edge['cbd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read]'
G.edge['cbd']['vold']['fill'] = 'red'
G.add_edge('cbd','vold')
G.edge['cbd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read]'
G.edge['cbd']['vold']['fill'] = 'red'
G.add_edge('cbd','watchdogd')
G.edge['cbd']['watchdogd']['write-read'] = '[write read]'
G.edge['cbd']['watchdogd']['fill'] = 'red'
G.add_edge('cbd','watchdogd')
G.edge['cbd']['watchdogd']['write-read'] = '[write read][write read]'
G.edge['cbd']['watchdogd']['fill'] = 'red'
G.add_edge('cbd','cbd')
G.edge['cbd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('cbd','cbd')
G.edge['cbd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('cbd','healthd')
G.edge['cbd']['healthd']['write-read'] = '[write read][add_name search]'
G.add_edge('cbd','healthd')
G.edge['cbd']['healthd']['write-read'] = '[write read][add_name search][remove_name search]'
G.add_edge('cbd','init_shell')
G.edge['cbd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','init_shell')
G.edge['cbd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','mpdecision')
G.edge['cbd']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('cbd','mpdecision')
G.edge['cbd']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('cbd','rild')
G.edge['cbd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('cbd','rild')
G.edge['cbd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('cbd','rtcc')
G.edge['cbd']['rtcc']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('cbd','rtcc')
G.edge['cbd']['rtcc']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('cbd','sdcardd')
G.edge['cbd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('cbd','sdcardd')
G.edge['cbd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('cbd','ueventd')
G.edge['cbd']['ueventd']['write-read'] = '[write read][add_name search]'
G.add_edge('cbd','ueventd')
G.edge['cbd']['ueventd']['write-read'] = '[write read][add_name search][remove_name search]'
G.add_edge('cbd','vold')
G.edge['cbd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('cbd','vold')
G.edge['cbd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('cbd','vold')
G.edge['cbd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('cbd','vold')
G.edge['cbd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('cbd','watchdogd')
G.edge['cbd']['watchdogd']['write-read'] = '[write read][write read][add_name search]'
G.add_edge('cbd','watchdogd')
G.edge['cbd']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search]'
G.add_edge('cbd','watchdogd')
G.edge['cbd']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('cbd','watchdogd')
G.edge['cbd']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','cbd')
G.edge['domain']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][add_name search]'
G.add_edge('domain','cbd')
G.edge['domain']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','healthd')
G.edge['domain']['healthd']['write-read'] = '[add_name search]'
G.add_edge('domain','healthd')
G.edge['domain']['healthd']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][add_name search][remove_name search][add_name search]'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','mpdecision')
G.edge['domain']['mpdecision']['write-read'] = '[add_name search][remove_name search][add_name search]'
G.add_edge('domain','mpdecision')
G.edge['domain']['mpdecision']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','rild')
G.edge['domain']['rild']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('domain','rild')
G.edge['domain']['rild']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','rtcc')
G.edge['domain']['rtcc']['write-read'] = '[setattr getattr][add_name search]'
G.add_edge('domain','rtcc')
G.edge['domain']['rtcc']['write-read'] = '[setattr getattr][add_name search][remove_name search]'
G.add_edge('domain','sdcardd')
G.edge['domain']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][add_name search]'
G.add_edge('domain','sdcardd')
G.edge['domain']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','ueventd')
G.edge['domain']['ueventd']['write-read'] = '[setattr getattr][add_name search]'
G.add_edge('domain','ueventd')
G.edge['domain']['ueventd']['write-read'] = '[setattr getattr][add_name search][remove_name search]'
G.add_edge('domain','vold')
G.edge['domain']['vold']['write-read'] = '[setattr getattr][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('domain','vold')
G.edge['domain']['vold']['write-read'] = '[setattr getattr][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','vold')
G.edge['domain']['vold']['write-read'] = '[setattr getattr][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][add_name search]'
G.add_edge('domain','vold')
G.edge['domain']['vold']['write-read'] = '[setattr getattr][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','watchdogd')
G.edge['domain']['watchdogd']['write-read'] = '[add_name search]'
G.add_edge('domain','watchdogd')
G.edge['domain']['watchdogd']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('domain','watchdogd')
G.edge['domain']['watchdogd']['write-read'] = '[add_name search][remove_name search][add_name search]'
G.add_edge('domain','watchdogd')
G.edge['domain']['watchdogd']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('init_shell','cbd')
G.edge['init_shell']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','mpdecision')
G.edge['init_shell']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','rild')
G.edge['init_shell']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('init_shell','rtcc')
G.edge['init_shell']['rtcc']['write-read'] = '[setattr getattr][open open]'
G.add_edge('init_shell','sdcardd')
G.edge['init_shell']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('init_shell','cbd')
G.edge['init_shell']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['cbd']['fill'] = 'red'
G.add_edge('init_shell','healthd')
G.edge['init_shell']['healthd']['write-read'] = '[write read]'
G.edge['init_shell']['healthd']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['init_shell']['fill'] = 'red'
G.add_edge('init_shell','mpdecision')
G.edge['init_shell']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['mpdecision']['fill'] = 'red'
G.add_edge('init_shell','rild')
G.edge['init_shell']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['rild']['fill'] = 'red'
G.add_edge('init_shell','rtcc')
G.edge['init_shell']['rtcc']['write-read'] = '[setattr getattr][open open][write read]'
G.edge['init_shell']['rtcc']['fill'] = 'red'
G.add_edge('init_shell','sdcardd')
G.edge['init_shell']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['sdcardd']['fill'] = 'red'
G.add_edge('init_shell','ueventd')
G.edge['init_shell']['ueventd']['write-read'] = '[setattr getattr][open open][write read][append read][write read]'
G.edge['init_shell']['ueventd']['fill'] = 'red'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['init_shell']['vold']['fill'] = 'red'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read]'
G.edge['init_shell']['vold']['fill'] = 'red'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read]'
G.edge['init_shell']['vold']['fill'] = 'red'
G.add_edge('init_shell','watchdogd')
G.edge['init_shell']['watchdogd']['write-read'] = '[write read]'
G.edge['init_shell']['watchdogd']['fill'] = 'red'
G.add_edge('init_shell','watchdogd')
G.edge['init_shell']['watchdogd']['write-read'] = '[write read][write read]'
G.edge['init_shell']['watchdogd']['fill'] = 'red'
G.add_edge('init_shell','cbd')
G.edge['init_shell']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('init_shell','cbd')
G.edge['init_shell']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('init_shell','healthd')
G.edge['init_shell']['healthd']['write-read'] = '[write read][add_name search]'
G.add_edge('init_shell','healthd')
G.edge['init_shell']['healthd']['write-read'] = '[write read][add_name search][remove_name search]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','mpdecision')
G.edge['init_shell']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('init_shell','mpdecision')
G.edge['init_shell']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('init_shell','rild')
G.edge['init_shell']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('init_shell','rild')
G.edge['init_shell']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('init_shell','rtcc')
G.edge['init_shell']['rtcc']['write-read'] = '[setattr getattr][open open][write read][add_name search]'
G.add_edge('init_shell','rtcc')
G.edge['init_shell']['rtcc']['write-read'] = '[setattr getattr][open open][write read][add_name search][remove_name search]'
G.add_edge('init_shell','sdcardd')
G.edge['init_shell']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('init_shell','sdcardd')
G.edge['init_shell']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('init_shell','ueventd')
G.edge['init_shell']['ueventd']['write-read'] = '[setattr getattr][open open][write read][append read][write read][add_name search]'
G.add_edge('init_shell','ueventd')
G.edge['init_shell']['ueventd']['write-read'] = '[setattr getattr][open open][write read][append read][write read][add_name search][remove_name search]'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('init_shell','watchdogd')
G.edge['init_shell']['watchdogd']['write-read'] = '[write read][write read][add_name search]'
G.add_edge('init_shell','watchdogd')
G.edge['init_shell']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search]'
G.add_edge('init_shell','watchdogd')
G.edge['init_shell']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('init_shell','watchdogd')
G.edge['init_shell']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('init_shell','kernel')
G.edge['init_shell']['kernel']['write-read'] = '[relabelto relabelfrom]'
G.add_edge('init_shell','kernel')
G.edge['init_shell']['kernel']['write-read'] = '[relabelto relabelfrom][relabelto relabelfrom]'
G.add_edge('mpdecision','cbd')
G.edge['mpdecision']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','init_shell')
G.edge['mpdecision']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','rild')
G.edge['mpdecision']['rild']['write-read'] = '[write read][append read][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','rtcc')
G.edge['mpdecision']['rtcc']['write-read'] = '[open open]'
G.add_edge('mpdecision','sdcardd')
G.edge['mpdecision']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','vold')
G.edge['mpdecision']['vold']['write-read'] = '[write read][append read][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','init_shell')
G.edge['mpdecision']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('mpdecision','vold')
G.edge['mpdecision']['vold']['write-read'] = '[write read][append read][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('mpdecision','cbd')
G.edge['mpdecision']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mpdecision']['cbd']['fill'] = 'red'
G.add_edge('mpdecision','healthd')
G.edge['mpdecision']['healthd']['write-read'] = '[write read][append read][write read][append read][write read]'
G.edge['mpdecision']['healthd']['fill'] = 'red'
G.add_edge('mpdecision','init_shell')
G.edge['mpdecision']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['mpdecision']['init_shell']['fill'] = 'red'
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['mpdecision']['mpdecision']['fill'] = 'red'
G.add_edge('mpdecision','rild')
G.edge['mpdecision']['rild']['write-read'] = '[write read][append read][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['mpdecision']['rild']['fill'] = 'red'
G.add_edge('mpdecision','rtcc')
G.edge['mpdecision']['rtcc']['write-read'] = '[open open][write read]'
G.edge['mpdecision']['rtcc']['fill'] = 'red'
G.add_edge('mpdecision','sdcardd')
G.edge['mpdecision']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mpdecision']['sdcardd']['fill'] = 'red'
G.add_edge('mpdecision','ueventd')
G.edge['mpdecision']['ueventd']['write-read'] = '[write read][append read][write read][append read][write read]'
G.edge['mpdecision']['ueventd']['fill'] = 'red'
G.add_edge('mpdecision','vold')
G.edge['mpdecision']['vold']['write-read'] = '[write read][append read][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['mpdecision']['vold']['fill'] = 'red'
G.add_edge('mpdecision','vold')
G.edge['mpdecision']['vold']['write-read'] = '[write read][append read][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read]'
G.edge['mpdecision']['vold']['fill'] = 'red'
G.add_edge('mpdecision','vold')
G.edge['mpdecision']['vold']['write-read'] = '[write read][append read][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read]'
G.edge['mpdecision']['vold']['fill'] = 'red'
G.add_edge('mpdecision','watchdogd')
G.edge['mpdecision']['watchdogd']['write-read'] = '[write read]'
G.edge['mpdecision']['watchdogd']['fill'] = 'red'
G.add_edge('mpdecision','watchdogd')
G.edge['mpdecision']['watchdogd']['write-read'] = '[write read][write read]'
G.edge['mpdecision']['watchdogd']['fill'] = 'red'
G.add_edge('mpdecision','cbd')
G.edge['mpdecision']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('mpdecision','cbd')
G.edge['mpdecision']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('mpdecision','healthd')
G.edge['mpdecision']['healthd']['write-read'] = '[write read][append read][write read][append read][write read][add_name search]'
G.add_edge('mpdecision','healthd')
G.edge['mpdecision']['healthd']['write-read'] = '[write read][append read][write read][append read][write read][add_name search][remove_name search]'
G.add_edge('mpdecision','init_shell')
G.edge['mpdecision']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('mpdecision','init_shell')
G.edge['mpdecision']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('mpdecision','rild')
G.edge['mpdecision']['rild']['write-read'] = '[write read][append read][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('mpdecision','rild')
G.edge['mpdecision']['rild']['write-read'] = '[write read][append read][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('mpdecision','rtcc')
G.edge['mpdecision']['rtcc']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('mpdecision','rtcc')
G.edge['mpdecision']['rtcc']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('mpdecision','sdcardd')
G.edge['mpdecision']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('mpdecision','sdcardd')
G.edge['mpdecision']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('mpdecision','ueventd')
G.edge['mpdecision']['ueventd']['write-read'] = '[write read][append read][write read][append read][write read][add_name search]'
G.add_edge('mpdecision','ueventd')
G.edge['mpdecision']['ueventd']['write-read'] = '[write read][append read][write read][append read][write read][add_name search][remove_name search]'
G.add_edge('mpdecision','vold')
G.edge['mpdecision']['vold']['write-read'] = '[write read][append read][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('mpdecision','vold')
G.edge['mpdecision']['vold']['write-read'] = '[write read][append read][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('mpdecision','vold')
G.edge['mpdecision']['vold']['write-read'] = '[write read][append read][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('mpdecision','vold')
G.edge['mpdecision']['vold']['write-read'] = '[write read][append read][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('mpdecision','watchdogd')
G.edge['mpdecision']['watchdogd']['write-read'] = '[write read][write read][add_name search]'
G.add_edge('mpdecision','watchdogd')
G.edge['mpdecision']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search]'
G.add_edge('mpdecision','watchdogd')
G.edge['mpdecision']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('mpdecision','watchdogd')
G.edge['mpdecision']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('qlogd','cbd')
G.edge['qlogd']['cbd']['write-read'] = '[open open]'
G.add_edge('qlogd','init_shell')
G.edge['qlogd']['init_shell']['write-read'] = '[open open]'
G.add_edge('qlogd','mpdecision')
G.edge['qlogd']['mpdecision']['write-read'] = '[open open]'
G.add_edge('qlogd','rild')
G.edge['qlogd']['rild']['write-read'] = '[setopt getopt][open open]'
G.add_edge('qlogd','rtcc')
G.edge['qlogd']['rtcc']['write-read'] = '[open open]'
G.add_edge('qlogd','sdcardd')
G.edge['qlogd']['sdcardd']['write-read'] = '[open open]'
G.add_edge('qlogd','vold')
G.edge['qlogd']['vold']['write-read'] = '[open open]'
G.add_edge('qlogd','init_shell')
G.edge['qlogd']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qlogd','vold')
G.edge['qlogd']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qlogd','cbd')
G.edge['qlogd']['cbd']['write-read'] = '[open open][write read]'
G.edge['qlogd']['cbd']['fill'] = 'red'
G.add_edge('qlogd','healthd')
G.edge['qlogd']['healthd']['write-read'] = '[write read]'
G.edge['qlogd']['healthd']['fill'] = 'red'
G.add_edge('qlogd','init_shell')
G.edge['qlogd']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qlogd']['init_shell']['fill'] = 'red'
G.add_edge('qlogd','mpdecision')
G.edge['qlogd']['mpdecision']['write-read'] = '[open open][write read]'
G.edge['qlogd']['mpdecision']['fill'] = 'red'
G.add_edge('qlogd','rild')
G.edge['qlogd']['rild']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['qlogd']['rild']['fill'] = 'red'
G.add_edge('qlogd','rtcc')
G.edge['qlogd']['rtcc']['write-read'] = '[open open][write read]'
G.edge['qlogd']['rtcc']['fill'] = 'red'
G.add_edge('qlogd','sdcardd')
G.edge['qlogd']['sdcardd']['write-read'] = '[open open][write read]'
G.edge['qlogd']['sdcardd']['fill'] = 'red'
G.add_edge('qlogd','ueventd')
G.edge['qlogd']['ueventd']['write-read'] = '[write read]'
G.edge['qlogd']['ueventd']['fill'] = 'red'
G.add_edge('qlogd','vold')
G.edge['qlogd']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qlogd']['vold']['fill'] = 'red'
G.add_edge('qlogd','vold')
G.edge['qlogd']['vold']['write-read'] = '[open open][setattr getattr][write read][write read]'
G.edge['qlogd']['vold']['fill'] = 'red'
G.add_edge('qlogd','vold')
G.edge['qlogd']['vold']['write-read'] = '[open open][setattr getattr][write read][write read][write read]'
G.edge['qlogd']['vold']['fill'] = 'red'
G.add_edge('qlogd','watchdogd')
G.edge['qlogd']['watchdogd']['write-read'] = '[write read]'
G.edge['qlogd']['watchdogd']['fill'] = 'red'
G.add_edge('qlogd','watchdogd')
G.edge['qlogd']['watchdogd']['write-read'] = '[write read][write read]'
G.edge['qlogd']['watchdogd']['fill'] = 'red'
G.add_edge('qlogd','cbd')
G.edge['qlogd']['cbd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('qlogd','cbd')
G.edge['qlogd']['cbd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('qlogd','healthd')
G.edge['qlogd']['healthd']['write-read'] = '[write read][add_name search]'
G.add_edge('qlogd','healthd')
G.edge['qlogd']['healthd']['write-read'] = '[write read][add_name search][remove_name search]'
G.add_edge('qlogd','init_shell')
G.edge['qlogd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qlogd','init_shell')
G.edge['qlogd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qlogd','mpdecision')
G.edge['qlogd']['mpdecision']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('qlogd','mpdecision')
G.edge['qlogd']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('qlogd','rild')
G.edge['qlogd']['rild']['write-read'] = '[setopt getopt][open open][write read][add_name search]'
G.add_edge('qlogd','rild')
G.edge['qlogd']['rild']['write-read'] = '[setopt getopt][open open][write read][add_name search][remove_name search]'
G.add_edge('qlogd','rtcc')
G.edge['qlogd']['rtcc']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('qlogd','rtcc')
G.edge['qlogd']['rtcc']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('qlogd','sdcardd')
G.edge['qlogd']['sdcardd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('qlogd','sdcardd')
G.edge['qlogd']['sdcardd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('qlogd','ueventd')
G.edge['qlogd']['ueventd']['write-read'] = '[write read][add_name search]'
G.add_edge('qlogd','ueventd')
G.edge['qlogd']['ueventd']['write-read'] = '[write read][add_name search][remove_name search]'
G.add_edge('qlogd','vold')
G.edge['qlogd']['vold']['write-read'] = '[open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('qlogd','vold')
G.edge['qlogd']['vold']['write-read'] = '[open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('qlogd','vold')
G.edge['qlogd']['vold']['write-read'] = '[open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('qlogd','vold')
G.edge['qlogd']['vold']['write-read'] = '[open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('qlogd','watchdogd')
G.edge['qlogd']['watchdogd']['write-read'] = '[write read][write read][add_name search]'
G.add_edge('qlogd','watchdogd')
G.edge['qlogd']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search]'
G.add_edge('qlogd','watchdogd')
G.edge['qlogd']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('qlogd','watchdogd')
G.edge['qlogd']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('qseecomd','cbd')
G.edge['qseecomd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qseecomd','init_shell')
G.edge['qseecomd']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qseecomd','mpdecision')
G.edge['qseecomd']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('qseecomd','rild')
G.edge['qseecomd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('qseecomd','rtcc')
G.edge['qseecomd']['rtcc']['write-read'] = '[open open]'
G.add_edge('qseecomd','sdcardd')
G.edge['qseecomd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qseecomd','vold')
G.edge['qseecomd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('qseecomd','init_shell')
G.edge['qseecomd']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('qseecomd','vold')
G.edge['qseecomd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('qseecomd','cbd')
G.edge['qseecomd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['qseecomd']['cbd']['fill'] = 'red'
G.add_edge('qseecomd','healthd')
G.edge['qseecomd']['healthd']['write-read'] = '[write read]'
G.edge['qseecomd']['healthd']['fill'] = 'red'
G.add_edge('qseecomd','init_shell')
G.edge['qseecomd']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['qseecomd']['init_shell']['fill'] = 'red'
G.add_edge('qseecomd','mpdecision')
G.edge['qseecomd']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['qseecomd']['mpdecision']['fill'] = 'red'
G.add_edge('qseecomd','rild')
G.edge['qseecomd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['qseecomd']['rild']['fill'] = 'red'
G.add_edge('qseecomd','rtcc')
G.edge['qseecomd']['rtcc']['write-read'] = '[open open][write read]'
G.edge['qseecomd']['rtcc']['fill'] = 'red'
G.add_edge('qseecomd','sdcardd')
G.edge['qseecomd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['qseecomd']['sdcardd']['fill'] = 'red'
G.add_edge('qseecomd','ueventd')
G.edge['qseecomd']['ueventd']['write-read'] = '[write read]'
G.edge['qseecomd']['ueventd']['fill'] = 'red'
G.add_edge('qseecomd','vold')
G.edge['qseecomd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['qseecomd']['vold']['fill'] = 'red'
G.add_edge('qseecomd','vold')
G.edge['qseecomd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read]'
G.edge['qseecomd']['vold']['fill'] = 'red'
G.add_edge('qseecomd','vold')
G.edge['qseecomd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read]'
G.edge['qseecomd']['vold']['fill'] = 'red'
G.add_edge('qseecomd','watchdogd')
G.edge['qseecomd']['watchdogd']['write-read'] = '[write read]'
G.edge['qseecomd']['watchdogd']['fill'] = 'red'
G.add_edge('qseecomd','watchdogd')
G.edge['qseecomd']['watchdogd']['write-read'] = '[write read][write read]'
G.edge['qseecomd']['watchdogd']['fill'] = 'red'
G.add_edge('qseecomd','cbd')
G.edge['qseecomd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('qseecomd','cbd')
G.edge['qseecomd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('qseecomd','healthd')
G.edge['qseecomd']['healthd']['write-read'] = '[write read][add_name search]'
G.add_edge('qseecomd','healthd')
G.edge['qseecomd']['healthd']['write-read'] = '[write read][add_name search][remove_name search]'
G.add_edge('qseecomd','init_shell')
G.edge['qseecomd']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('qseecomd','init_shell')
G.edge['qseecomd']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qseecomd','mpdecision')
G.edge['qseecomd']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('qseecomd','mpdecision')
G.edge['qseecomd']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('qseecomd','rild')
G.edge['qseecomd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('qseecomd','rild')
G.edge['qseecomd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('qseecomd','rtcc')
G.edge['qseecomd']['rtcc']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('qseecomd','rtcc')
G.edge['qseecomd']['rtcc']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('qseecomd','sdcardd')
G.edge['qseecomd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('qseecomd','sdcardd')
G.edge['qseecomd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('qseecomd','ueventd')
G.edge['qseecomd']['ueventd']['write-read'] = '[write read][add_name search]'
G.add_edge('qseecomd','ueventd')
G.edge['qseecomd']['ueventd']['write-read'] = '[write read][add_name search][remove_name search]'
G.add_edge('qseecomd','vold')
G.edge['qseecomd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('qseecomd','vold')
G.edge['qseecomd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('qseecomd','vold')
G.edge['qseecomd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('qseecomd','vold')
G.edge['qseecomd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('qseecomd','watchdogd')
G.edge['qseecomd']['watchdogd']['write-read'] = '[write read][write read][add_name search]'
G.add_edge('qseecomd','watchdogd')
G.edge['qseecomd']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search]'
G.add_edge('qseecomd','watchdogd')
G.edge['qseecomd']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('qseecomd','watchdogd')
G.edge['qseecomd']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('rild','cbd')
G.edge['rild']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('rild','mpdecision')
G.edge['rild']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('rild','rtcc')
G.edge['rild']['rtcc']['write-read'] = '[open open]'
G.add_edge('rild','sdcardd')
G.edge['rild']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('rild','cbd')
G.edge['rild']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read]'
G.edge['rild']['cbd']['fill'] = 'red'
G.add_edge('rild','healthd')
G.edge['rild']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][write read]'
G.edge['rild']['healthd']['fill'] = 'red'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['rild']['init_shell']['fill'] = 'red'
G.add_edge('rild','mpdecision')
G.edge['rild']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read]'
G.edge['rild']['mpdecision']['fill'] = 'red'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['rild']['rild']['fill'] = 'red'
G.add_edge('rild','rtcc')
G.edge['rild']['rtcc']['write-read'] = '[open open][write read]'
G.edge['rild']['rtcc']['fill'] = 'red'
G.add_edge('rild','sdcardd')
G.edge['rild']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read]'
G.edge['rild']['sdcardd']['fill'] = 'red'
G.add_edge('rild','ueventd')
G.edge['rild']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][write read]'
G.edge['rild']['ueventd']['fill'] = 'red'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['rild']['vold']['fill'] = 'red'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read]'
G.edge['rild']['vold']['fill'] = 'red'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read]'
G.edge['rild']['vold']['fill'] = 'red'
G.add_edge('rild','watchdogd')
G.edge['rild']['watchdogd']['write-read'] = '[write read]'
G.edge['rild']['watchdogd']['fill'] = 'red'
G.add_edge('rild','watchdogd')
G.edge['rild']['watchdogd']['write-read'] = '[write read][write read]'
G.edge['rild']['watchdogd']['fill'] = 'red'
G.add_edge('rild','cbd')
G.edge['rild']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('rild','cbd')
G.edge['rild']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('rild','healthd')
G.edge['rild']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][write read][add_name search]'
G.add_edge('rild','healthd')
G.edge['rild']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][write read][add_name search][remove_name search]'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','mpdecision')
G.edge['rild']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('rild','mpdecision')
G.edge['rild']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('rild','rtcc')
G.edge['rild']['rtcc']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('rild','rtcc')
G.edge['rild']['rtcc']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('rild','sdcardd')
G.edge['rild']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('rild','sdcardd')
G.edge['rild']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('rild','ueventd')
G.edge['rild']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][write read][add_name search]'
G.add_edge('rild','ueventd')
G.edge['rild']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][write read][add_name search][remove_name search]'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('rild','watchdogd')
G.edge['rild']['watchdogd']['write-read'] = '[write read][write read][add_name search]'
G.add_edge('rild','watchdogd')
G.edge['rild']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search]'
G.add_edge('rild','watchdogd')
G.edge['rild']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('rild','watchdogd')
G.edge['rild']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('rtcc','cbd')
G.edge['rtcc']['cbd']['write-read'] = '[open open]'
G.add_edge('rtcc','init_shell')
G.edge['rtcc']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('rtcc','mpdecision')
G.edge['rtcc']['mpdecision']['write-read'] = '[open open]'
G.add_edge('rtcc','rild')
G.edge['rtcc']['rild']['write-read'] = '[open open]'
G.add_edge('rtcc','rtcc')
G.edge['rtcc']['rtcc']['write-read'] = '[open open]'
G.add_edge('rtcc','sdcardd')
G.edge['rtcc']['sdcardd']['write-read'] = '[open open]'
G.add_edge('rtcc','vold')
G.edge['rtcc']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rtcc','init_shell')
G.edge['rtcc']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('rtcc','vold')
G.edge['rtcc']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('rtcc','cbd')
G.edge['rtcc']['cbd']['write-read'] = '[open open][write read]'
G.edge['rtcc']['cbd']['fill'] = 'red'
G.add_edge('rtcc','healthd')
G.edge['rtcc']['healthd']['write-read'] = '[write read]'
G.edge['rtcc']['healthd']['fill'] = 'red'
G.add_edge('rtcc','init_shell')
G.edge['rtcc']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['rtcc']['init_shell']['fill'] = 'red'
G.add_edge('rtcc','mpdecision')
G.edge['rtcc']['mpdecision']['write-read'] = '[open open][write read]'
G.edge['rtcc']['mpdecision']['fill'] = 'red'
G.add_edge('rtcc','rild')
G.edge['rtcc']['rild']['write-read'] = '[open open][write read]'
G.edge['rtcc']['rild']['fill'] = 'red'
G.add_edge('rtcc','rtcc')
G.edge['rtcc']['rtcc']['write-read'] = '[open open][write read]'
G.edge['rtcc']['rtcc']['fill'] = 'red'
G.add_edge('rtcc','sdcardd')
G.edge['rtcc']['sdcardd']['write-read'] = '[open open][write read]'
G.edge['rtcc']['sdcardd']['fill'] = 'red'
G.add_edge('rtcc','ueventd')
G.edge['rtcc']['ueventd']['write-read'] = '[write read]'
G.edge['rtcc']['ueventd']['fill'] = 'red'
G.add_edge('rtcc','vold')
G.edge['rtcc']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['rtcc']['vold']['fill'] = 'red'
G.add_edge('rtcc','vold')
G.edge['rtcc']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read]'
G.edge['rtcc']['vold']['fill'] = 'red'
G.add_edge('rtcc','vold')
G.edge['rtcc']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read]'
G.edge['rtcc']['vold']['fill'] = 'red'
G.add_edge('rtcc','watchdogd')
G.edge['rtcc']['watchdogd']['write-read'] = '[write read]'
G.edge['rtcc']['watchdogd']['fill'] = 'red'
G.add_edge('rtcc','watchdogd')
G.edge['rtcc']['watchdogd']['write-read'] = '[write read][write read]'
G.edge['rtcc']['watchdogd']['fill'] = 'red'
G.add_edge('rtcc','cbd')
G.edge['rtcc']['cbd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('rtcc','cbd')
G.edge['rtcc']['cbd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('rtcc','healthd')
G.edge['rtcc']['healthd']['write-read'] = '[write read][add_name search]'
G.add_edge('rtcc','healthd')
G.edge['rtcc']['healthd']['write-read'] = '[write read][add_name search][remove_name search]'
G.add_edge('rtcc','init_shell')
G.edge['rtcc']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('rtcc','init_shell')
G.edge['rtcc']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rtcc','mpdecision')
G.edge['rtcc']['mpdecision']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('rtcc','mpdecision')
G.edge['rtcc']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('rtcc','rild')
G.edge['rtcc']['rild']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('rtcc','rild')
G.edge['rtcc']['rild']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('rtcc','rtcc')
G.edge['rtcc']['rtcc']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('rtcc','rtcc')
G.edge['rtcc']['rtcc']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('rtcc','sdcardd')
G.edge['rtcc']['sdcardd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('rtcc','sdcardd')
G.edge['rtcc']['sdcardd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('rtcc','ueventd')
G.edge['rtcc']['ueventd']['write-read'] = '[write read][add_name search]'
G.add_edge('rtcc','ueventd')
G.edge['rtcc']['ueventd']['write-read'] = '[write read][add_name search][remove_name search]'
G.add_edge('rtcc','vold')
G.edge['rtcc']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('rtcc','vold')
G.edge['rtcc']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('rtcc','vold')
G.edge['rtcc']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('rtcc','vold')
G.edge['rtcc']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('rtcc','watchdogd')
G.edge['rtcc']['watchdogd']['write-read'] = '[write read][write read][add_name search]'
G.add_edge('rtcc','watchdogd')
G.edge['rtcc']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search]'
G.add_edge('rtcc','watchdogd')
G.edge['rtcc']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('rtcc','watchdogd')
G.edge['rtcc']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('sdcardd','cbd')
G.edge['sdcardd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sdcardd','init_shell')
G.edge['sdcardd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sdcardd','mpdecision')
G.edge['sdcardd']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('sdcardd','rild')
G.edge['sdcardd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('sdcardd','rtcc')
G.edge['sdcardd']['rtcc']['write-read'] = '[open open]'
G.add_edge('sdcardd','sdcardd')
G.edge['sdcardd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sdcardd','vold')
G.edge['sdcardd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('sdcardd','init_shell')
G.edge['sdcardd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('sdcardd','vold')
G.edge['sdcardd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('sdcardd','cbd')
G.edge['sdcardd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['sdcardd']['cbd']['fill'] = 'red'
G.add_edge('sdcardd','healthd')
G.edge['sdcardd']['healthd']['write-read'] = '[write read]'
G.edge['sdcardd']['healthd']['fill'] = 'red'
G.add_edge('sdcardd','init_shell')
G.edge['sdcardd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['sdcardd']['init_shell']['fill'] = 'red'
G.add_edge('sdcardd','mpdecision')
G.edge['sdcardd']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['sdcardd']['mpdecision']['fill'] = 'red'
G.add_edge('sdcardd','rild')
G.edge['sdcardd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['sdcardd']['rild']['fill'] = 'red'
G.add_edge('sdcardd','rtcc')
G.edge['sdcardd']['rtcc']['write-read'] = '[open open][write read]'
G.edge['sdcardd']['rtcc']['fill'] = 'red'
G.add_edge('sdcardd','sdcardd')
G.edge['sdcardd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['sdcardd']['sdcardd']['fill'] = 'red'
G.add_edge('sdcardd','ueventd')
G.edge['sdcardd']['ueventd']['write-read'] = '[write read]'
G.edge['sdcardd']['ueventd']['fill'] = 'red'
G.add_edge('sdcardd','vold')
G.edge['sdcardd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['sdcardd']['vold']['fill'] = 'red'
G.add_edge('sdcardd','vold')
G.edge['sdcardd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read]'
G.edge['sdcardd']['vold']['fill'] = 'red'
G.add_edge('sdcardd','vold')
G.edge['sdcardd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read]'
G.edge['sdcardd']['vold']['fill'] = 'red'
G.add_edge('sdcardd','watchdogd')
G.edge['sdcardd']['watchdogd']['write-read'] = '[write read]'
G.edge['sdcardd']['watchdogd']['fill'] = 'red'
G.add_edge('sdcardd','watchdogd')
G.edge['sdcardd']['watchdogd']['write-read'] = '[write read][write read]'
G.edge['sdcardd']['watchdogd']['fill'] = 'red'
G.add_edge('sdcardd','cbd')
G.edge['sdcardd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('sdcardd','cbd')
G.edge['sdcardd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','healthd')
G.edge['sdcardd']['healthd']['write-read'] = '[write read][add_name search]'
G.add_edge('sdcardd','healthd')
G.edge['sdcardd']['healthd']['write-read'] = '[write read][add_name search][remove_name search]'
G.add_edge('sdcardd','init_shell')
G.edge['sdcardd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','init_shell')
G.edge['sdcardd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','mpdecision')
G.edge['sdcardd']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('sdcardd','mpdecision')
G.edge['sdcardd']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','rild')
G.edge['sdcardd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('sdcardd','rild')
G.edge['sdcardd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','rtcc')
G.edge['sdcardd']['rtcc']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('sdcardd','rtcc')
G.edge['sdcardd']['rtcc']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','sdcardd')
G.edge['sdcardd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('sdcardd','sdcardd')
G.edge['sdcardd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','ueventd')
G.edge['sdcardd']['ueventd']['write-read'] = '[write read][add_name search]'
G.add_edge('sdcardd','ueventd')
G.edge['sdcardd']['ueventd']['write-read'] = '[write read][add_name search][remove_name search]'
G.add_edge('sdcardd','vold')
G.edge['sdcardd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('sdcardd','vold')
G.edge['sdcardd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','vold')
G.edge['sdcardd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('sdcardd','vold')
G.edge['sdcardd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('sdcardd','watchdogd')
G.edge['sdcardd']['watchdogd']['write-read'] = '[write read][write read][add_name search]'
G.add_edge('sdcardd','watchdogd')
G.edge['sdcardd']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','watchdogd')
G.edge['sdcardd']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('sdcardd','watchdogd')
G.edge['sdcardd']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('system_server','cbd')
G.edge['system_server']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','mpdecision')
G.edge['system_server']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('system_server','rtcc')
G.edge['system_server']['rtcc']['write-read'] = '[setattr getattr][open open]'
G.add_edge('system_server','sdcardd')
G.edge['system_server']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','cbd')
G.edge['system_server']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['cbd']['fill'] = 'red'
G.add_edge('system_server','healthd')
G.edge['system_server']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read]'
G.edge['system_server']['healthd']['fill'] = 'red'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['init_shell']['fill'] = 'red'
G.add_edge('system_server','mpdecision')
G.edge['system_server']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['mpdecision']['fill'] = 'red'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['rild']['fill'] = 'red'
G.add_edge('system_server','rtcc')
G.edge['system_server']['rtcc']['write-read'] = '[setattr getattr][open open][write read]'
G.edge['system_server']['rtcc']['fill'] = 'red'
G.add_edge('system_server','sdcardd')
G.edge['system_server']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['sdcardd']['fill'] = 'red'
G.add_edge('system_server','ueventd')
G.edge['system_server']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['system_server']['ueventd']['fill'] = 'red'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['vold']['fill'] = 'red'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][write read]'
G.edge['system_server']['vold']['fill'] = 'red'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][write read][write read]'
G.edge['system_server']['vold']['fill'] = 'red'
G.add_edge('system_server','watchdogd')
G.edge['system_server']['watchdogd']['write-read'] = '[write read]'
G.edge['system_server']['watchdogd']['fill'] = 'red'
G.add_edge('system_server','watchdogd')
G.edge['system_server']['watchdogd']['write-read'] = '[write read][write read]'
G.edge['system_server']['watchdogd']['fill'] = 'red'
G.add_edge('system_server','cbd')
G.edge['system_server']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('system_server','cbd')
G.edge['system_server']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('system_server','healthd')
G.edge['system_server']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][add_name search]'
G.add_edge('system_server','healthd')
G.edge['system_server']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][add_name search][remove_name search]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','mpdecision')
G.edge['system_server']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('system_server','mpdecision')
G.edge['system_server']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('system_server','rtcc')
G.edge['system_server']['rtcc']['write-read'] = '[setattr getattr][open open][write read][add_name search]'
G.add_edge('system_server','rtcc')
G.edge['system_server']['rtcc']['write-read'] = '[setattr getattr][open open][write read][add_name search][remove_name search]'
G.add_edge('system_server','sdcardd')
G.edge['system_server']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('system_server','sdcardd')
G.edge['system_server']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('system_server','ueventd')
G.edge['system_server']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search]'
G.add_edge('system_server','ueventd')
G.edge['system_server']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('system_server','watchdogd')
G.edge['system_server']['watchdogd']['write-read'] = '[write read][write read][add_name search]'
G.add_edge('system_server','watchdogd')
G.edge['system_server']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search]'
G.add_edge('system_server','watchdogd')
G.edge['system_server']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('system_server','watchdogd')
G.edge['system_server']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('tee','cbd')
G.edge['tee']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('tee','init_shell')
G.edge['tee']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('tee','mpdecision')
G.edge['tee']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('tee','rild')
G.edge['tee']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('tee','rtcc')
G.edge['tee']['rtcc']['write-read'] = '[open open]'
G.add_edge('tee','sdcardd')
G.edge['tee']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('tee','vold')
G.edge['tee']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('tee','init_shell')
G.edge['tee']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('tee','vold')
G.edge['tee']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('tee','cbd')
G.edge['tee']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['tee']['cbd']['fill'] = 'red'
G.add_edge('tee','healthd')
G.edge['tee']['healthd']['write-read'] = '[open open][write read][append read][write read]'
G.edge['tee']['healthd']['fill'] = 'red'
G.add_edge('tee','init_shell')
G.edge['tee']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['tee']['init_shell']['fill'] = 'red'
G.add_edge('tee','mpdecision')
G.edge['tee']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['tee']['mpdecision']['fill'] = 'red'
G.add_edge('tee','rild')
G.edge['tee']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['tee']['rild']['fill'] = 'red'
G.add_edge('tee','rtcc')
G.edge['tee']['rtcc']['write-read'] = '[open open][write read]'
G.edge['tee']['rtcc']['fill'] = 'red'
G.add_edge('tee','sdcardd')
G.edge['tee']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['tee']['sdcardd']['fill'] = 'red'
G.add_edge('tee','ueventd')
G.edge['tee']['ueventd']['write-read'] = '[write read]'
G.edge['tee']['ueventd']['fill'] = 'red'
G.add_edge('tee','vold')
G.edge['tee']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['tee']['vold']['fill'] = 'red'
G.add_edge('tee','vold')
G.edge['tee']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read]'
G.edge['tee']['vold']['fill'] = 'red'
G.add_edge('tee','vold')
G.edge['tee']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read]'
G.edge['tee']['vold']['fill'] = 'red'
G.add_edge('tee','watchdogd')
G.edge['tee']['watchdogd']['write-read'] = '[write read]'
G.edge['tee']['watchdogd']['fill'] = 'red'
G.add_edge('tee','watchdogd')
G.edge['tee']['watchdogd']['write-read'] = '[write read][write read]'
G.edge['tee']['watchdogd']['fill'] = 'red'
G.add_edge('tee','cbd')
G.edge['tee']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('tee','cbd')
G.edge['tee']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('tee','healthd')
G.edge['tee']['healthd']['write-read'] = '[open open][write read][append read][write read][add_name search]'
G.add_edge('tee','healthd')
G.edge['tee']['healthd']['write-read'] = '[open open][write read][append read][write read][add_name search][remove_name search]'
G.add_edge('tee','init_shell')
G.edge['tee']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('tee','init_shell')
G.edge['tee']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('tee','mpdecision')
G.edge['tee']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('tee','mpdecision')
G.edge['tee']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('tee','rild')
G.edge['tee']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('tee','rild')
G.edge['tee']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('tee','rtcc')
G.edge['tee']['rtcc']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('tee','rtcc')
G.edge['tee']['rtcc']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('tee','sdcardd')
G.edge['tee']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('tee','sdcardd')
G.edge['tee']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('tee','ueventd')
G.edge['tee']['ueventd']['write-read'] = '[write read][add_name search]'
G.add_edge('tee','ueventd')
G.edge['tee']['ueventd']['write-read'] = '[write read][add_name search][remove_name search]'
G.add_edge('tee','vold')
G.edge['tee']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('tee','vold')
G.edge['tee']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('tee','vold')
G.edge['tee']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('tee','vold')
G.edge['tee']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('tee','watchdogd')
G.edge['tee']['watchdogd']['write-read'] = '[write read][write read][add_name search]'
G.add_edge('tee','watchdogd')
G.edge['tee']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search]'
G.add_edge('tee','watchdogd')
G.edge['tee']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('tee','watchdogd')
G.edge['tee']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('vold','cbd')
G.edge['vold']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','mpdecision')
G.edge['vold']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','rild')
G.edge['vold']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('vold','rtcc')
G.edge['vold']['rtcc']['write-read'] = '[open open]'
G.add_edge('vold','sdcardd')
G.edge['vold']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('vold','cbd')
G.edge['vold']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['cbd']['fill'] = 'red'
G.add_edge('vold','healthd')
G.edge['vold']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read]'
G.edge['vold']['healthd']['fill'] = 'red'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['vold']['init_shell']['fill'] = 'red'
G.add_edge('vold','mpdecision')
G.edge['vold']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['mpdecision']['fill'] = 'red'
G.add_edge('vold','rild')
G.edge['vold']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['vold']['rild']['fill'] = 'red'
G.add_edge('vold','rtcc')
G.edge['vold']['rtcc']['write-read'] = '[open open][write read]'
G.edge['vold']['rtcc']['fill'] = 'red'
G.add_edge('vold','sdcardd')
G.edge['vold']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['sdcardd']['fill'] = 'red'
G.add_edge('vold','ueventd')
G.edge['vold']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['vold']['ueventd']['fill'] = 'red'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['vold']['vold']['fill'] = 'red'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read]'
G.edge['vold']['vold']['fill'] = 'red'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read]'
G.edge['vold']['vold']['fill'] = 'red'
G.add_edge('vold','watchdogd')
G.edge['vold']['watchdogd']['write-read'] = '[write read]'
G.edge['vold']['watchdogd']['fill'] = 'red'
G.add_edge('vold','watchdogd')
G.edge['vold']['watchdogd']['write-read'] = '[write read][write read]'
G.edge['vold']['watchdogd']['fill'] = 'red'
G.add_edge('vold','cbd')
G.edge['vold']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('vold','cbd')
G.edge['vold']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('vold','healthd')
G.edge['vold']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][add_name search]'
G.add_edge('vold','healthd')
G.edge['vold']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][add_name search][remove_name search]'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vold','mpdecision')
G.edge['vold']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('vold','mpdecision')
G.edge['vold']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('vold','rild')
G.edge['vold']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('vold','rild')
G.edge['vold']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('vold','rtcc')
G.edge['vold']['rtcc']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('vold','rtcc')
G.edge['vold']['rtcc']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('vold','sdcardd')
G.edge['vold']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('vold','sdcardd')
G.edge['vold']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('vold','ueventd')
G.edge['vold']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][add_name search]'
G.add_edge('vold','ueventd')
G.edge['vold']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][add_name search][remove_name search]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('vold','watchdogd')
G.edge['vold']['watchdogd']['write-read'] = '[write read][write read][add_name search]'
G.add_edge('vold','watchdogd')
G.edge['vold']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search]'
G.add_edge('vold','watchdogd')
G.edge['vold']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('vold','watchdogd')
G.edge['vold']['watchdogd']['write-read'] = '[write read][write read][add_name search][remove_name search][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()