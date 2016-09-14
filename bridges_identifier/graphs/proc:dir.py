import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('charon','clatd')
G.edge['charon']['clatd']['write-read'] = '[add_name search][open open][write read][append read][open open]'
G.add_edge('charon','netmgrd')
G.edge['charon']['netmgrd']['write-read'] = '[open open][write read][append read][write read][open open]'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['charon']['charon']['fill'] = 'red'
G.add_edge('charon','clatd')
G.edge['charon']['clatd']['write-read'] = '[add_name search][open open][write read][append read][open open][write read]'
G.edge['charon']['clatd']['fill'] = 'red'
G.add_edge('charon','netmgrd')
G.edge['charon']['netmgrd']['write-read'] = '[open open][write read][append read][write read][open open][write read]'
G.edge['charon']['netmgrd']['fill'] = 'red'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('charon','clatd')
G.edge['charon']['clatd']['write-read'] = '[add_name search][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('charon','clatd')
G.edge['charon']['clatd']['write-read'] = '[add_name search][open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('charon','netmgrd')
G.edge['charon']['netmgrd']['write-read'] = '[open open][write read][append read][write read][open open][write read][add_name search]'
G.add_edge('charon','netmgrd')
G.edge['charon']['netmgrd']['write-read'] = '[open open][write read][append read][write read][open open][write read][add_name search][remove_name search]'
G.add_edge('clatd','charon')
G.edge['clatd']['charon']['write-read'] = '[open open]'
G.add_edge('clatd','clatd')
G.edge['clatd']['clatd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('clatd','netmgrd')
G.edge['clatd']['netmgrd']['write-read'] = '[open open]'
G.add_edge('clatd','charon')
G.edge['clatd']['charon']['write-read'] = '[open open][write read]'
G.edge['clatd']['charon']['fill'] = 'red'
G.add_edge('clatd','clatd')
G.edge['clatd']['clatd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['clatd']['clatd']['fill'] = 'red'
G.add_edge('clatd','netmgrd')
G.edge['clatd']['netmgrd']['write-read'] = '[open open][write read]'
G.edge['clatd']['netmgrd']['fill'] = 'red'
G.add_edge('clatd','charon')
G.edge['clatd']['charon']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('clatd','charon')
G.edge['clatd']['charon']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('clatd','clatd')
G.edge['clatd']['clatd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search]'
G.add_edge('clatd','clatd')
G.edge['clatd']['clatd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search]'
G.add_edge('clatd','netmgrd')
G.edge['clatd']['netmgrd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('clatd','netmgrd')
G.edge['clatd']['netmgrd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('domain','charon')
G.edge['domain']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('domain','clatd')
G.edge['domain']['clatd']['write-read'] = '[add_name search][add_name search][open open][write read][append read][open open]'
G.add_edge('domain','netmgrd')
G.edge['domain']['netmgrd']['write-read'] = '[add_name search][add_name search][remove_name search][open open][write read][append read][write read][open open]'
G.add_edge('domain','charon')
G.edge['domain']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['domain']['charon']['fill'] = 'red'
G.add_edge('domain','clatd')
G.edge['domain']['clatd']['write-read'] = '[add_name search][add_name search][open open][write read][append read][open open][write read]'
G.edge['domain']['clatd']['fill'] = 'red'
G.add_edge('domain','netmgrd')
G.edge['domain']['netmgrd']['write-read'] = '[add_name search][add_name search][remove_name search][open open][write read][append read][write read][open open][write read]'
G.edge['domain']['netmgrd']['fill'] = 'red'
G.add_edge('domain','charon')
G.edge['domain']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('domain','charon')
G.edge['domain']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('domain','clatd')
G.edge['domain']['clatd']['write-read'] = '[add_name search][add_name search][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('domain','clatd')
G.edge['domain']['clatd']['write-read'] = '[add_name search][add_name search][open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('domain','netmgrd')
G.edge['domain']['netmgrd']['write-read'] = '[add_name search][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][add_name search]'
G.add_edge('domain','netmgrd')
G.edge['domain']['netmgrd']['write-read'] = '[add_name search][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][add_name search][remove_name search]'
G.add_edge('netmgrd','charon')
G.edge['netmgrd']['charon']['write-read'] = '[open open]'
G.add_edge('netmgrd','clatd')
G.edge['netmgrd']['clatd']['write-read'] = '[open open]'
G.add_edge('netmgrd','netmgrd')
G.edge['netmgrd']['netmgrd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read][open open]'
G.add_edge('netmgrd','charon')
G.edge['netmgrd']['charon']['write-read'] = '[open open][add_name search]'
G.add_edge('netmgrd','charon')
G.edge['netmgrd']['charon']['write-read'] = '[open open][add_name search][remove_name search]'
G.add_edge('netmgrd','clatd')
G.edge['netmgrd']['clatd']['write-read'] = '[open open][add_name search]'
G.add_edge('netmgrd','clatd')
G.edge['netmgrd']['clatd']['write-read'] = '[open open][add_name search][remove_name search]'
G.add_edge('netmgrd','netmgrd')
G.edge['netmgrd']['netmgrd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read][open open][add_name search]'
G.add_edge('netmgrd','netmgrd')
G.edge['netmgrd']['netmgrd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read][open open][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()