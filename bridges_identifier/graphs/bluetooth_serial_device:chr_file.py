import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('bluetooth','init_shell')
G.edge['bluetooth']['init_shell']['write-read'] = '[open open]'
G.add_edge('bluetooth','mediaserver')
G.edge['bluetooth']['mediaserver']['write-read'] = '[open open]'
G.add_edge('bluetooth','zygote')
G.edge['bluetooth']['zygote']['write-read'] = '[open open]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['bluetooth']['bluetooth']['fill'] = 'red'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','init_shell')
G.edge['bluetooth']['init_shell']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['init_shell']['fill'] = 'red'
G.add_edge('bluetooth','init_shell')
G.edge['bluetooth']['init_shell']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','mediaserver')
G.edge['bluetooth']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['mediaserver']['fill'] = 'red'
G.add_edge('bluetooth','mediaserver')
G.edge['bluetooth']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','zygote')
G.edge['bluetooth']['zygote']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['zygote']['fill'] = 'red'
G.add_edge('bluetooth','zygote')
G.edge['bluetooth']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('init_shell','bluetooth')
G.edge['init_shell']['bluetooth']['write-read'] = '[open open]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','mediaserver')
G.edge['init_shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','zygote')
G.edge['init_shell']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','bluetooth')
G.edge['init_shell']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['init_shell']['bluetooth']['fill'] = 'red'
G.add_edge('init_shell','bluetooth')
G.edge['init_shell']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['init_shell']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('init_shell','mediaserver')
G.edge['init_shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['init_shell']['mediaserver']['fill'] = 'red'
G.add_edge('init_shell','mediaserver')
G.edge['init_shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('init_shell','zygote')
G.edge['init_shell']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['zygote']['fill'] = 'red'
G.add_edge('init_shell','zygote')
G.edge['init_shell']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','bluetooth')
G.edge['mediaserver']['bluetooth']['write-read'] = '[open open]'
G.add_edge('mediaserver','init_shell')
G.edge['mediaserver']['init_shell']['write-read'] = '[open open][open open]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','zygote')
G.edge['mediaserver']['zygote']['write-read'] = '[open open]'
G.add_edge('mediaserver','bluetooth')
G.edge['mediaserver']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['bluetooth']['fill'] = 'red'
G.add_edge('mediaserver','bluetooth')
G.edge['mediaserver']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','init_shell')
G.edge['mediaserver']['init_shell']['write-read'] = '[open open][open open][write read]'
G.edge['mediaserver']['init_shell']['fill'] = 'red'
G.add_edge('mediaserver','init_shell')
G.edge['mediaserver']['init_shell']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['mediaserver']['mediaserver']['fill'] = 'red'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('mediaserver','zygote')
G.edge['mediaserver']['zygote']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['zygote']['fill'] = 'red'
G.add_edge('mediaserver','zygote')
G.edge['mediaserver']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('zygote','bluetooth')
G.edge['zygote']['bluetooth']['write-read'] = '[open open]'
G.add_edge('zygote','init_shell')
G.edge['zygote']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('zygote','mediaserver')
G.edge['zygote']['mediaserver']['write-read'] = '[open open]'
G.add_edge('zygote','zygote')
G.edge['zygote']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('zygote','bluetooth')
G.edge['zygote']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['zygote']['bluetooth']['fill'] = 'red'
G.add_edge('zygote','bluetooth')
G.edge['zygote']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('zygote','init_shell')
G.edge['zygote']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['zygote']['init_shell']['fill'] = 'red'
G.add_edge('zygote','init_shell')
G.edge['zygote']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('zygote','mediaserver')
G.edge['zygote']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['zygote']['mediaserver']['fill'] = 'red'
G.add_edge('zygote','mediaserver')
G.edge['zygote']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('zygote','zygote')
G.edge['zygote']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['zygote']['zygote']['fill'] = 'red'
G.add_edge('zygote','zygote')
G.edge['zygote']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()