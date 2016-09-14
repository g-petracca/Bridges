import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('atfwd','ssr_setup')
G.edge['atfwd']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('atfwd','ssr_setup')
G.edge['atfwd']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['atfwd']['ssr_setup']['fill'] = 'red'
G.add_edge('atfwd','ssr_setup')
G.edge['atfwd']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('domain','ssr_setup')
G.edge['domain']['ssr_setup']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('domain','ssr_setup')
G.edge['domain']['ssr_setup']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['domain']['ssr_setup']['fill'] = 'red'
G.add_edge('domain','ssr_setup')
G.edge['domain']['ssr_setup']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('mdm_helper','ssr_setup')
G.edge['mdm_helper']['ssr_setup']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mdm_helper','ssr_setup')
G.edge['mdm_helper']['ssr_setup']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['mdm_helper']['ssr_setup']['fill'] = 'red'
G.add_edge('mdm_helper','ssr_setup')
G.edge['mdm_helper']['ssr_setup']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('netmgrd','ssr_setup')
G.edge['netmgrd']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('netmgrd','ssr_setup')
G.edge['netmgrd']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['netmgrd']['ssr_setup']['fill'] = 'red'
G.add_edge('netmgrd','ssr_setup')
G.edge['netmgrd']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('per_mgr','ssr_setup')
G.edge['per_mgr']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('per_mgr','ssr_setup')
G.edge['per_mgr']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['per_mgr']['ssr_setup']['fill'] = 'red'
G.add_edge('per_mgr','ssr_setup')
G.edge['per_mgr']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('qmuxd','ssr_setup')
G.edge['qmuxd']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('qmuxd','ssr_setup')
G.edge['qmuxd']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['qmuxd']['ssr_setup']['fill'] = 'red'
G.add_edge('qmuxd','ssr_setup')
G.edge['qmuxd']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('rild','ssr_setup')
G.edge['rild']['ssr_setup']['write-read'] = '[open open][write read][append read][write read]'
G.edge['rild']['ssr_setup']['fill'] = 'red'
G.add_edge('rild','ssr_setup')
G.edge['rild']['ssr_setup']['write-read'] = '[open open][write read][append read][write read][append read]'
G.add_edge('rild','ssr_setup')
G.edge['rild']['ssr_setup']['write-read'] = '[open open][write read][append read][write read][append read][open open]'
G.add_edge('rild','ssr_setup')
G.edge['rild']['ssr_setup']['write-read'] = '[open open][write read][append read][write read][append read][open open][write read]'
G.edge['rild']['ssr_setup']['fill'] = 'red'
G.add_edge('rild','ssr_setup')
G.edge['rild']['ssr_setup']['write-read'] = '[open open][write read][append read][write read][append read][open open][write read][append read]'
G.add_edge('ssr_setup','ssr_setup')
G.edge['ssr_setup']['ssr_setup']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('ssr_setup','ssr_setup')
G.edge['ssr_setup']['ssr_setup']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['ssr_setup']['ssr_setup']['fill'] = 'red'
G.add_edge('ssr_setup','ssr_setup')
G.edge['ssr_setup']['ssr_setup']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('thermal-engine','ssr_setup')
G.edge['thermal-engine']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('thermal-engine','ssr_setup')
G.edge['thermal-engine']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['thermal-engine']['ssr_setup']['fill'] = 'red'
G.add_edge('thermal-engine','ssr_setup')
G.edge['thermal-engine']['ssr_setup']['write-read'] = '[open open][write read][append read]'
app = Viewer(G)
app.mainloop()