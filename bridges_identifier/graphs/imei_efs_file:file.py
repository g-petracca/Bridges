import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('at_distributor','at_distributor')
G.edge['at_distributor']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('at_distributor','init_shell')
G.edge['at_distributor']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('at_distributor','radio')
G.edge['at_distributor']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('at_distributor','rild')
G.edge['at_distributor']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','rild')
G.edge['at_distributor']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open]'
G.add_edge('at_distributor','rild')
G.edge['at_distributor']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open]'
G.add_edge('at_distributor','sec-ril')
G.edge['at_distributor']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','at_distributor')
G.edge['at_distributor']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('at_distributor','init_shell')
G.edge['at_distributor']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('at_distributor','radio')
G.edge['at_distributor']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('at_distributor','rild')
G.edge['at_distributor']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr]'
G.add_edge('at_distributor','sec-ril')
G.edge['at_distributor']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('at_distributor','at_distributor')
G.edge['at_distributor']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['at_distributor']['at_distributor']['fill'] = 'red'
G.add_edge('at_distributor','at_distributor')
G.edge['at_distributor']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('at_distributor','init_shell')
G.edge['at_distributor']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['at_distributor']['init_shell']['fill'] = 'red'
G.add_edge('at_distributor','init_shell')
G.edge['at_distributor']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('at_distributor','radio')
G.edge['at_distributor']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['at_distributor']['radio']['fill'] = 'red'
G.add_edge('at_distributor','radio')
G.edge['at_distributor']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('at_distributor','rild')
G.edge['at_distributor']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read]'
G.edge['at_distributor']['rild']['fill'] = 'red'
G.add_edge('at_distributor','rild')
G.edge['at_distributor']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read]'
G.add_edge('at_distributor','rild')
G.edge['at_distributor']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['at_distributor']['rild']['fill'] = 'red'
G.add_edge('at_distributor','rild')
G.edge['at_distributor']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('at_distributor','rild')
G.edge['at_distributor']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read]'
G.edge['at_distributor']['rild']['fill'] = 'red'
G.add_edge('at_distributor','rild')
G.edge['at_distributor']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read]'
G.add_edge('at_distributor','sec-ril')
G.edge['at_distributor']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['at_distributor']['sec-ril']['fill'] = 'red'
G.add_edge('at_distributor','sec-ril')
G.edge['at_distributor']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('bootanim','at_distributor')
G.edge['bootanim']['at_distributor']['write-read'] = '[open open]'
G.add_edge('bootanim','init_shell')
G.edge['bootanim']['init_shell']['write-read'] = '[open open]'
G.add_edge('bootanim','radio')
G.edge['bootanim']['radio']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bootanim','rild')
G.edge['bootanim']['rild']['write-read'] = '[open open]'
G.add_edge('bootanim','rild')
G.edge['bootanim']['rild']['write-read'] = '[open open][open open]'
G.add_edge('bootanim','rild')
G.edge['bootanim']['rild']['write-read'] = '[open open][open open][open open]'
G.add_edge('bootanim','sec-ril')
G.edge['bootanim']['sec-ril']['write-read'] = '[open open]'
G.add_edge('bootanim','at_distributor')
G.edge['bootanim']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bootanim','init_shell')
G.edge['bootanim']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bootanim','radio')
G.edge['bootanim']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('bootanim','rild')
G.edge['bootanim']['rild']['write-read'] = '[open open][open open][open open][setattr getattr]'
G.add_edge('bootanim','sec-ril')
G.edge['bootanim']['sec-ril']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bootanim','at_distributor')
G.edge['bootanim']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['bootanim']['at_distributor']['fill'] = 'red'
G.add_edge('bootanim','at_distributor')
G.edge['bootanim']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('bootanim','init_shell')
G.edge['bootanim']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['bootanim']['init_shell']['fill'] = 'red'
G.add_edge('bootanim','init_shell')
G.edge['bootanim']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('bootanim','radio')
G.edge['bootanim']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['bootanim']['radio']['fill'] = 'red'
G.add_edge('bootanim','radio')
G.edge['bootanim']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('bootanim','rild')
G.edge['bootanim']['rild']['write-read'] = '[open open][open open][open open][setattr getattr][write read]'
G.edge['bootanim']['rild']['fill'] = 'red'
G.add_edge('bootanim','rild')
G.edge['bootanim']['rild']['write-read'] = '[open open][open open][open open][setattr getattr][write read][append read]'
G.add_edge('bootanim','rild')
G.edge['bootanim']['rild']['write-read'] = '[open open][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['bootanim']['rild']['fill'] = 'red'
G.add_edge('bootanim','rild')
G.edge['bootanim']['rild']['write-read'] = '[open open][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('bootanim','rild')
G.edge['bootanim']['rild']['write-read'] = '[open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read]'
G.edge['bootanim']['rild']['fill'] = 'red'
G.add_edge('bootanim','rild')
G.edge['bootanim']['rild']['write-read'] = '[open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read]'
G.add_edge('bootanim','sec-ril')
G.edge['bootanim']['sec-ril']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['bootanim']['sec-ril']['fill'] = 'red'
G.add_edge('bootanim','sec-ril')
G.edge['bootanim']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','at_distributor')
G.edge['commonplatformappdomain']['at_distributor']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','init_shell')
G.edge['commonplatformappdomain']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('commonplatformappdomain','radio')
G.edge['commonplatformappdomain']['radio']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('commonplatformappdomain','rild')
G.edge['commonplatformappdomain']['rild']['write-read'] = '[write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('commonplatformappdomain','rild')
G.edge['commonplatformappdomain']['rild']['write-read'] = '[write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][open open]'
G.add_edge('commonplatformappdomain','rild')
G.edge['commonplatformappdomain']['rild']['write-read'] = '[write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][open open][open open]'
G.add_edge('commonplatformappdomain','sec-ril')
G.edge['commonplatformappdomain']['sec-ril']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','at_distributor')
G.edge['commonplatformappdomain']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','init_shell')
G.edge['commonplatformappdomain']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','radio')
G.edge['commonplatformappdomain']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','rild')
G.edge['commonplatformappdomain']['rild']['write-read'] = '[write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][open open][open open][setattr getattr]'
G.add_edge('commonplatformappdomain','sec-ril')
G.edge['commonplatformappdomain']['sec-ril']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','at_distributor')
G.edge['commonplatformappdomain']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['at_distributor']['fill'] = 'red'
G.add_edge('commonplatformappdomain','at_distributor')
G.edge['commonplatformappdomain']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','init_shell')
G.edge['commonplatformappdomain']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['init_shell']['fill'] = 'red'
G.add_edge('commonplatformappdomain','init_shell')
G.edge['commonplatformappdomain']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','radio')
G.edge['commonplatformappdomain']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['radio']['fill'] = 'red'
G.add_edge('commonplatformappdomain','radio')
G.edge['commonplatformappdomain']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','rild')
G.edge['commonplatformappdomain']['rild']['write-read'] = '[write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][open open][open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['rild']['fill'] = 'red'
G.add_edge('commonplatformappdomain','rild')
G.edge['commonplatformappdomain']['rild']['write-read'] = '[write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][open open][open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','rild')
G.edge['commonplatformappdomain']['rild']['write-read'] = '[write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['commonplatformappdomain']['rild']['fill'] = 'red'
G.add_edge('commonplatformappdomain','rild')
G.edge['commonplatformappdomain']['rild']['write-read'] = '[write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('commonplatformappdomain','rild')
G.edge['commonplatformappdomain']['rild']['write-read'] = '[write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read]'
G.edge['commonplatformappdomain']['rild']['fill'] = 'red'
G.add_edge('commonplatformappdomain','rild')
G.edge['commonplatformappdomain']['rild']['write-read'] = '[write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read]'
G.add_edge('commonplatformappdomain','sec-ril')
G.edge['commonplatformappdomain']['sec-ril']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['sec-ril']['fill'] = 'red'
G.add_edge('commonplatformappdomain','sec-ril')
G.edge['commonplatformappdomain']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','at_distributor')
G.edge['init_shell']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','radio')
G.edge['init_shell']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','rild')
G.edge['init_shell']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('init_shell','rild')
G.edge['init_shell']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open]'
G.add_edge('init_shell','rild')
G.edge['init_shell']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open]'
G.add_edge('init_shell','sec-ril')
G.edge['init_shell']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('init_shell','at_distributor')
G.edge['init_shell']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','radio')
G.edge['init_shell']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('init_shell','rild')
G.edge['init_shell']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr]'
G.add_edge('init_shell','sec-ril')
G.edge['init_shell']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('init_shell','at_distributor')
G.edge['init_shell']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['at_distributor']['fill'] = 'red'
G.add_edge('init_shell','at_distributor')
G.edge['init_shell']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['init_shell']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','radio')
G.edge['init_shell']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['init_shell']['radio']['fill'] = 'red'
G.add_edge('init_shell','radio')
G.edge['init_shell']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','rild')
G.edge['init_shell']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read]'
G.edge['init_shell']['rild']['fill'] = 'red'
G.add_edge('init_shell','rild')
G.edge['init_shell']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','rild')
G.edge['init_shell']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['init_shell']['rild']['fill'] = 'red'
G.add_edge('init_shell','rild')
G.edge['init_shell']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('init_shell','rild')
G.edge['init_shell']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read]'
G.edge['init_shell']['rild']['fill'] = 'red'
G.add_edge('init_shell','rild')
G.edge['init_shell']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read]'
G.add_edge('init_shell','sec-ril')
G.edge['init_shell']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['init_shell']['sec-ril']['fill'] = 'red'
G.add_edge('init_shell','sec-ril')
G.edge['init_shell']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','at_distributor')
G.edge['newAttr1']['at_distributor']['write-read'] = '[open open]'
G.add_edge('newAttr1','init_shell')
G.edge['newAttr1']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open]'
G.add_edge('newAttr1','radio')
G.edge['newAttr1']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr1','rild')
G.edge['newAttr1']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr1','rild')
G.edge['newAttr1']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('newAttr1','rild')
G.edge['newAttr1']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open]'
G.add_edge('newAttr1','sec-ril')
G.edge['newAttr1']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('newAttr1','at_distributor')
G.edge['newAttr1']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr1','init_shell')
G.edge['newAttr1']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr]'
G.add_edge('newAttr1','radio')
G.edge['newAttr1']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('newAttr1','rild')
G.edge['newAttr1']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr]'
G.add_edge('newAttr1','sec-ril')
G.edge['newAttr1']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('newAttr1','at_distributor')
G.edge['newAttr1']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr1']['at_distributor']['fill'] = 'red'
G.add_edge('newAttr1','at_distributor')
G.edge['newAttr1']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','init_shell')
G.edge['newAttr1']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read]'
G.edge['newAttr1']['init_shell']['fill'] = 'red'
G.add_edge('newAttr1','init_shell')
G.edge['newAttr1']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','radio')
G.edge['newAttr1']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['newAttr1']['radio']['fill'] = 'red'
G.add_edge('newAttr1','radio')
G.edge['newAttr1']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','rild')
G.edge['newAttr1']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read]'
G.edge['newAttr1']['rild']['fill'] = 'red'
G.add_edge('newAttr1','rild')
G.edge['newAttr1']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','rild')
G.edge['newAttr1']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['newAttr1']['rild']['fill'] = 'red'
G.add_edge('newAttr1','rild')
G.edge['newAttr1']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('newAttr1','rild')
G.edge['newAttr1']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read]'
G.edge['newAttr1']['rild']['fill'] = 'red'
G.add_edge('newAttr1','rild')
G.edge['newAttr1']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read]'
G.add_edge('newAttr1','sec-ril')
G.edge['newAttr1']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['newAttr1']['sec-ril']['fill'] = 'red'
G.add_edge('newAttr1','sec-ril')
G.edge['newAttr1']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('oneseg_mw','at_distributor')
G.edge['oneseg_mw']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('oneseg_mw','init_shell')
G.edge['oneseg_mw']['init_shell']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('oneseg_mw','radio')
G.edge['oneseg_mw']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('oneseg_mw','rild')
G.edge['oneseg_mw']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('oneseg_mw','rild')
G.edge['oneseg_mw']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open]'
G.add_edge('oneseg_mw','rild')
G.edge['oneseg_mw']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open]'
G.add_edge('oneseg_mw','sec-ril')
G.edge['oneseg_mw']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('oneseg_mw','at_distributor')
G.edge['oneseg_mw']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('oneseg_mw','init_shell')
G.edge['oneseg_mw']['init_shell']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('oneseg_mw','radio')
G.edge['oneseg_mw']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('oneseg_mw','rild')
G.edge['oneseg_mw']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr]'
G.add_edge('oneseg_mw','sec-ril')
G.edge['oneseg_mw']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('oneseg_mw','at_distributor')
G.edge['oneseg_mw']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['oneseg_mw']['at_distributor']['fill'] = 'red'
G.add_edge('oneseg_mw','at_distributor')
G.edge['oneseg_mw']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('oneseg_mw','init_shell')
G.edge['oneseg_mw']['init_shell']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['oneseg_mw']['init_shell']['fill'] = 'red'
G.add_edge('oneseg_mw','init_shell')
G.edge['oneseg_mw']['init_shell']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('oneseg_mw','radio')
G.edge['oneseg_mw']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['oneseg_mw']['radio']['fill'] = 'red'
G.add_edge('oneseg_mw','radio')
G.edge['oneseg_mw']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('oneseg_mw','rild')
G.edge['oneseg_mw']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read]'
G.edge['oneseg_mw']['rild']['fill'] = 'red'
G.add_edge('oneseg_mw','rild')
G.edge['oneseg_mw']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read]'
G.add_edge('oneseg_mw','rild')
G.edge['oneseg_mw']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['oneseg_mw']['rild']['fill'] = 'red'
G.add_edge('oneseg_mw','rild')
G.edge['oneseg_mw']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('oneseg_mw','rild')
G.edge['oneseg_mw']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read]'
G.edge['oneseg_mw']['rild']['fill'] = 'red'
G.add_edge('oneseg_mw','rild')
G.edge['oneseg_mw']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read]'
G.add_edge('oneseg_mw','sec-ril')
G.edge['oneseg_mw']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['oneseg_mw']['sec-ril']['fill'] = 'red'
G.add_edge('oneseg_mw','sec-ril')
G.edge['oneseg_mw']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('radio','at_distributor')
G.edge['radio']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('radio','init_shell')
G.edge['radio']['init_shell']['write-read'] = '[add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open]'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('radio','rild')
G.edge['radio']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('radio','rild')
G.edge['radio']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('radio','rild')
G.edge['radio']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open]'
G.add_edge('radio','sec-ril')
G.edge['radio']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('radio','at_distributor')
G.edge['radio']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('radio','init_shell')
G.edge['radio']['init_shell']['write-read'] = '[add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr]'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('radio','rild')
G.edge['radio']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr]'
G.add_edge('radio','sec-ril')
G.edge['radio']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('radio','at_distributor')
G.edge['radio']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['radio']['at_distributor']['fill'] = 'red'
G.add_edge('radio','at_distributor')
G.edge['radio']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('radio','init_shell')
G.edge['radio']['init_shell']['write-read'] = '[add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read]'
G.edge['radio']['init_shell']['fill'] = 'red'
G.add_edge('radio','init_shell')
G.edge['radio']['init_shell']['write-read'] = '[add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read]'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['radio']['radio']['fill'] = 'red'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('radio','rild')
G.edge['radio']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read]'
G.edge['radio']['rild']['fill'] = 'red'
G.add_edge('radio','rild')
G.edge['radio']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read]'
G.add_edge('radio','rild')
G.edge['radio']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['radio']['rild']['fill'] = 'red'
G.add_edge('radio','rild')
G.edge['radio']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('radio','rild')
G.edge['radio']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read]'
G.edge['radio']['rild']['fill'] = 'red'
G.add_edge('radio','rild')
G.edge['radio']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read]'
G.add_edge('radio','sec-ril')
G.edge['radio']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['radio']['sec-ril']['fill'] = 'red'
G.add_edge('radio','sec-ril')
G.edge['radio']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('rild','at_distributor')
G.edge['rild']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open]'
G.add_edge('rild','radio')
G.edge['rild']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open]'
G.add_edge('rild','sec-ril')
G.edge['rild']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','at_distributor')
G.edge['rild']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr]'
G.add_edge('rild','radio')
G.edge['rild']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr]'
G.add_edge('rild','sec-ril')
G.edge['rild']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('rild','at_distributor')
G.edge['rild']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['rild']['at_distributor']['fill'] = 'red'
G.add_edge('rild','at_distributor')
G.edge['rild']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read]'
G.edge['rild']['init_shell']['fill'] = 'red'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read]'
G.add_edge('rild','radio')
G.edge['rild']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['rild']['radio']['fill'] = 'red'
G.add_edge('rild','radio')
G.edge['rild']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read]'
G.edge['rild']['rild']['fill'] = 'red'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['rild']['rild']['fill'] = 'red'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read]'
G.edge['rild']['rild']['fill'] = 'red'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read]'
G.add_edge('rild','sec-ril')
G.edge['rild']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['rild']['sec-ril']['fill'] = 'red'
G.add_edge('rild','sec-ril')
G.edge['rild']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('rild','at_distributor')
G.edge['rild']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open]'
G.add_edge('rild','radio')
G.edge['rild']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open]'
G.add_edge('rild','sec-ril')
G.edge['rild']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('rild','at_distributor')
G.edge['rild']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('rild','radio')
G.edge['rild']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr]'
G.add_edge('rild','sec-ril')
G.edge['rild']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('rild','at_distributor')
G.edge['rild']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['at_distributor']['fill'] = 'red'
G.add_edge('rild','at_distributor')
G.edge['rild']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['init_shell']['fill'] = 'red'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('rild','radio')
G.edge['rild']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['radio']['fill'] = 'red'
G.add_edge('rild','radio')
G.edge['rild']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read]'
G.edge['rild']['rild']['fill'] = 'red'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['rild']['rild']['fill'] = 'red'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read]'
G.edge['rild']['rild']['fill'] = 'red'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read]'
G.add_edge('rild','sec-ril')
G.edge['rild']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['sec-ril']['fill'] = 'red'
G.add_edge('rild','sec-ril')
G.edge['rild']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('sec-ril','at_distributor')
G.edge['sec-ril']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sec-ril','init_shell')
G.edge['sec-ril']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open]'
G.add_edge('sec-ril','radio')
G.edge['sec-ril']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('sec-ril','rild')
G.edge['sec-ril']['rild']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sec-ril','rild')
G.edge['sec-ril']['rild']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('sec-ril','rild')
G.edge['sec-ril']['rild']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open]'
G.add_edge('sec-ril','sec-ril')
G.edge['sec-ril']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sec-ril','at_distributor')
G.edge['sec-ril']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('sec-ril','init_shell')
G.edge['sec-ril']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr]'
G.add_edge('sec-ril','radio')
G.edge['sec-ril']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('sec-ril','rild')
G.edge['sec-ril']['rild']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr]'
G.add_edge('sec-ril','sec-ril')
G.edge['sec-ril']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('sec-ril','at_distributor')
G.edge['sec-ril']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['sec-ril']['at_distributor']['fill'] = 'red'
G.add_edge('sec-ril','at_distributor')
G.edge['sec-ril']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('sec-ril','init_shell')
G.edge['sec-ril']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read]'
G.edge['sec-ril']['init_shell']['fill'] = 'red'
G.add_edge('sec-ril','init_shell')
G.edge['sec-ril']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read]'
G.add_edge('sec-ril','radio')
G.edge['sec-ril']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['sec-ril']['radio']['fill'] = 'red'
G.add_edge('sec-ril','radio')
G.edge['sec-ril']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('sec-ril','rild')
G.edge['sec-ril']['rild']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read]'
G.edge['sec-ril']['rild']['fill'] = 'red'
G.add_edge('sec-ril','rild')
G.edge['sec-ril']['rild']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read]'
G.add_edge('sec-ril','rild')
G.edge['sec-ril']['rild']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['sec-ril']['rild']['fill'] = 'red'
G.add_edge('sec-ril','rild')
G.edge['sec-ril']['rild']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('sec-ril','rild')
G.edge['sec-ril']['rild']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read]'
G.edge['sec-ril']['rild']['fill'] = 'red'
G.add_edge('sec-ril','rild')
G.edge['sec-ril']['rild']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read]'
G.add_edge('sec-ril','sec-ril')
G.edge['sec-ril']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['sec-ril']['sec-ril']['fill'] = 'red'
G.add_edge('sec-ril','sec-ril')
G.edge['sec-ril']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()