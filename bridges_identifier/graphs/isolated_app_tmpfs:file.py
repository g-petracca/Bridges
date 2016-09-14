import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('isolated_app','bauthserver')
G.edge['isolated_app']['bauthserver']['write-read'] = '[write read]'
G.edge['isolated_app']['bauthserver']['fill'] = 'red'
G.add_edge('isolated_app','dumpstate')
G.edge['isolated_app']['dumpstate']['write-read'] = '[write read]'
G.edge['isolated_app']['dumpstate']['fill'] = 'red'
G.add_edge('isolated_app','isolated_app')
G.edge['isolated_app']['isolated_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['isolated_app']['isolated_app']['fill'] = 'red'
G.add_edge('isolated_app','isolated_app')
G.edge['isolated_app']['isolated_app']['write-read'] = '[open open][setattr getattr][write read][write read]'
G.edge['isolated_app']['isolated_app']['fill'] = 'red'
G.add_edge('isolated_app','mediaserver')
G.edge['isolated_app']['mediaserver']['write-read'] = '[write read]'
G.edge['isolated_app']['mediaserver']['fill'] = 'red'
G.add_edge('isolated_app','mediaserver')
G.edge['isolated_app']['mediaserver']['write-read'] = '[write read][append read]'
G.add_edge('isolated_app','netd')
G.edge['isolated_app']['netd']['write-read'] = '[write read]'
G.edge['isolated_app']['netd']['fill'] = 'red'
G.add_edge('isolated_app','netd')
G.edge['isolated_app']['netd']['write-read'] = '[write read][append read]'
G.add_edge('isolated_app','rtc_log')
G.edge['isolated_app']['rtc_log']['write-read'] = '[write read]'
G.edge['isolated_app']['rtc_log']['fill'] = 'red'
G.add_edge('isolated_app','surfaceflinger')
G.edge['isolated_app']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['isolated_app']['surfaceflinger']['fill'] = 'red'
G.add_edge('isolated_app','ueventd')
G.edge['isolated_app']['ueventd']['write-read'] = '[write read]'
G.edge['isolated_app']['ueventd']['fill'] = 'red'
G.add_edge('isolated_app','ueventd')
G.edge['isolated_app']['ueventd']['write-read'] = '[write read][append read]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','netd')
G.edge['mediaserver']['netd']['write-read'] = '[open open][write read][append read][write read][open open]'
G.add_edge('mediaserver','ueventd')
G.edge['mediaserver']['ueventd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mediaserver','bauthserver')
G.edge['mediaserver']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['mediaserver']['bauthserver']['fill'] = 'red'
G.add_edge('mediaserver','dumpstate')
G.edge['mediaserver']['dumpstate']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['mediaserver']['dumpstate']['fill'] = 'red'
G.add_edge('mediaserver','isolated_app')
G.edge['mediaserver']['isolated_app']['write-read'] = '[write read]'
G.edge['mediaserver']['isolated_app']['fill'] = 'red'
G.add_edge('mediaserver','isolated_app')
G.edge['mediaserver']['isolated_app']['write-read'] = '[write read][write read]'
G.edge['mediaserver']['isolated_app']['fill'] = 'red'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['mediaserver']['fill'] = 'red'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','netd')
G.edge['mediaserver']['netd']['write-read'] = '[open open][write read][append read][write read][open open][write read]'
G.edge['mediaserver']['netd']['fill'] = 'red'
G.add_edge('mediaserver','netd')
G.edge['mediaserver']['netd']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read]'
G.add_edge('mediaserver','rtc_log')
G.edge['mediaserver']['rtc_log']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['mediaserver']['rtc_log']['fill'] = 'red'
G.add_edge('mediaserver','surfaceflinger')
G.edge['mediaserver']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][write read]'
G.edge['mediaserver']['surfaceflinger']['fill'] = 'red'
G.add_edge('mediaserver','ueventd')
G.edge['mediaserver']['ueventd']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['mediaserver']['ueventd']['fill'] = 'red'
G.add_edge('mediaserver','ueventd')
G.edge['mediaserver']['ueventd']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('ueventd','mediaserver')
G.edge['ueventd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read][open open]'
G.add_edge('ueventd','netd')
G.edge['ueventd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][add_name search][remove_name search][add_name search][remove_name search][write read][open open]'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][relabelto relabelfrom][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open]'
G.add_edge('ueventd','bauthserver')
G.edge['ueventd']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['ueventd']['bauthserver']['fill'] = 'red'
G.add_edge('ueventd','dumpstate')
G.edge['ueventd']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['ueventd']['dumpstate']['fill'] = 'red'
G.add_edge('ueventd','isolated_app')
G.edge['ueventd']['isolated_app']['write-read'] = '[write read]'
G.edge['ueventd']['isolated_app']['fill'] = 'red'
G.add_edge('ueventd','isolated_app')
G.edge['ueventd']['isolated_app']['write-read'] = '[write read][write read]'
G.edge['ueventd']['isolated_app']['fill'] = 'red'
G.add_edge('ueventd','mediaserver')
G.edge['ueventd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][write read]'
G.edge['ueventd']['mediaserver']['fill'] = 'red'
G.add_edge('ueventd','mediaserver')
G.edge['ueventd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][write read][append read]'
G.add_edge('ueventd','netd')
G.edge['ueventd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][add_name search][remove_name search][add_name search][remove_name search][write read][open open][write read]'
G.edge['ueventd']['netd']['fill'] = 'red'
G.add_edge('ueventd','netd')
G.edge['ueventd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][add_name search][remove_name search][add_name search][remove_name search][write read][open open][write read][append read]'
G.add_edge('ueventd','rtc_log')
G.edge['ueventd']['rtc_log']['write-read'] = '[write read]'
G.edge['ueventd']['rtc_log']['fill'] = 'red'
G.add_edge('ueventd','surfaceflinger')
G.edge['ueventd']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][write read]'
G.edge['ueventd']['surfaceflinger']['fill'] = 'red'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][relabelto relabelfrom][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][write read]'
G.edge['ueventd']['ueventd']['fill'] = 'red'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][relabelto relabelfrom][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][write read][append read]'
app = Viewer(G)
app.mainloop()