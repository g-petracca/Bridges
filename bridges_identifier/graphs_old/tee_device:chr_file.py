import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('drmserver','drmserver')
G.edge['drmserver']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('drmserver','fidodaemon')
G.edge['drmserver']['fidodaemon']['write-read'] = '[open open]'
G.add_edge('drmserver','keystore')
G.edge['drmserver']['keystore']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('drmserver','launcher')
G.edge['drmserver']['launcher']['write-read'] = '[open open]'
G.add_edge('drmserver','mcStarter')
G.edge['drmserver']['mcStarter']['write-read'] = '[open open]'
G.add_edge('drmserver','mediaserver')
G.edge['drmserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('drmserver','seempd')
G.edge['drmserver']['seempd']['write-read'] = '[open open]'
G.add_edge('drmserver','surfaceflinger')
G.edge['drmserver']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('drmserver','tbaseLoader')
G.edge['drmserver']['tbaseLoader']['write-read'] = '[open open]'
G.add_edge('drmserver','tee')
G.edge['drmserver']['tee']['write-read'] = '[open open]'
G.add_edge('drmserver','vold')
G.edge['drmserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('drmserver','wfdservice')
G.edge['drmserver']['wfdservice']['write-read'] = '[open open]'
G.add_edge('drmserver','drmserver')
G.edge['drmserver']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['drmserver']['drmserver']['fill'] = 'red'
G.add_edge('drmserver','drmserver')
G.edge['drmserver']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('drmserver','fidodaemon')
G.edge['drmserver']['fidodaemon']['write-read'] = '[open open][write read]'
G.edge['drmserver']['fidodaemon']['fill'] = 'red'
G.add_edge('drmserver','fidodaemon')
G.edge['drmserver']['fidodaemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('drmserver','keystore')
G.edge['drmserver']['keystore']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['drmserver']['keystore']['fill'] = 'red'
G.add_edge('drmserver','keystore')
G.edge['drmserver']['keystore']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('drmserver','launcher')
G.edge['drmserver']['launcher']['write-read'] = '[open open][write read]'
G.edge['drmserver']['launcher']['fill'] = 'red'
G.add_edge('drmserver','launcher')
G.edge['drmserver']['launcher']['write-read'] = '[open open][write read][append read]'
G.add_edge('drmserver','mcStarter')
G.edge['drmserver']['mcStarter']['write-read'] = '[open open][write read]'
G.edge['drmserver']['mcStarter']['fill'] = 'red'
G.add_edge('drmserver','mcStarter')
G.edge['drmserver']['mcStarter']['write-read'] = '[open open][write read][append read]'
G.add_edge('drmserver','mediaserver')
G.edge['drmserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['drmserver']['mediaserver']['fill'] = 'red'
G.add_edge('drmserver','mediaserver')
G.edge['drmserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('drmserver','seempd')
G.edge['drmserver']['seempd']['write-read'] = '[open open][write read]'
G.edge['drmserver']['seempd']['fill'] = 'red'
G.add_edge('drmserver','seempd')
G.edge['drmserver']['seempd']['write-read'] = '[open open][write read][append read]'
G.add_edge('drmserver','surfaceflinger')
G.edge['drmserver']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['drmserver']['surfaceflinger']['fill'] = 'red'
G.add_edge('drmserver','surfaceflinger')
G.edge['drmserver']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('drmserver','tbaseLoader')
G.edge['drmserver']['tbaseLoader']['write-read'] = '[open open][write read]'
G.edge['drmserver']['tbaseLoader']['fill'] = 'red'
G.add_edge('drmserver','tbaseLoader')
G.edge['drmserver']['tbaseLoader']['write-read'] = '[open open][write read][append read]'
G.add_edge('drmserver','tee')
G.edge['drmserver']['tee']['write-read'] = '[open open][write read]'
G.edge['drmserver']['tee']['fill'] = 'red'
G.add_edge('drmserver','tee')
G.edge['drmserver']['tee']['write-read'] = '[open open][write read][append read]'
G.add_edge('drmserver','vold')
G.edge['drmserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['drmserver']['vold']['fill'] = 'red'
G.add_edge('drmserver','vold')
G.edge['drmserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('drmserver','wfdservice')
G.edge['drmserver']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['drmserver']['wfdservice']['fill'] = 'red'
G.add_edge('drmserver','wfdservice')
G.edge['drmserver']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('fidodaemon','drmserver')
G.edge['fidodaemon']['drmserver']['write-read'] = '[open open]'
G.add_edge('fidodaemon','fidodaemon')
G.edge['fidodaemon']['fidodaemon']['write-read'] = '[write read][open open]'
G.add_edge('fidodaemon','keystore')
G.edge['fidodaemon']['keystore']['write-read'] = '[open open]'
G.add_edge('fidodaemon','launcher')
G.edge['fidodaemon']['launcher']['write-read'] = '[open open]'
G.add_edge('fidodaemon','mcStarter')
G.edge['fidodaemon']['mcStarter']['write-read'] = '[open open]'
G.add_edge('fidodaemon','mediaserver')
G.edge['fidodaemon']['mediaserver']['write-read'] = '[open open]'
G.add_edge('fidodaemon','seempd')
G.edge['fidodaemon']['seempd']['write-read'] = '[open open]'
G.add_edge('fidodaemon','surfaceflinger')
G.edge['fidodaemon']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('fidodaemon','tbaseLoader')
G.edge['fidodaemon']['tbaseLoader']['write-read'] = '[open open]'
G.add_edge('fidodaemon','tee')
G.edge['fidodaemon']['tee']['write-read'] = '[open open]'
G.add_edge('fidodaemon','vold')
G.edge['fidodaemon']['vold']['write-read'] = '[open open]'
G.add_edge('fidodaemon','wfdservice')
G.edge['fidodaemon']['wfdservice']['write-read'] = '[open open]'
G.add_edge('fidodaemon','drmserver')
G.edge['fidodaemon']['drmserver']['write-read'] = '[open open][write read]'
G.edge['fidodaemon']['drmserver']['fill'] = 'red'
G.add_edge('fidodaemon','drmserver')
G.edge['fidodaemon']['drmserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('fidodaemon','fidodaemon')
G.edge['fidodaemon']['fidodaemon']['write-read'] = '[write read][open open][write read]'
G.edge['fidodaemon']['fidodaemon']['fill'] = 'red'
G.add_edge('fidodaemon','fidodaemon')
G.edge['fidodaemon']['fidodaemon']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('fidodaemon','keystore')
G.edge['fidodaemon']['keystore']['write-read'] = '[open open][write read]'
G.edge['fidodaemon']['keystore']['fill'] = 'red'
G.add_edge('fidodaemon','keystore')
G.edge['fidodaemon']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('fidodaemon','launcher')
G.edge['fidodaemon']['launcher']['write-read'] = '[open open][write read]'
G.edge['fidodaemon']['launcher']['fill'] = 'red'
G.add_edge('fidodaemon','launcher')
G.edge['fidodaemon']['launcher']['write-read'] = '[open open][write read][append read]'
G.add_edge('fidodaemon','mcStarter')
G.edge['fidodaemon']['mcStarter']['write-read'] = '[open open][write read]'
G.edge['fidodaemon']['mcStarter']['fill'] = 'red'
G.add_edge('fidodaemon','mcStarter')
G.edge['fidodaemon']['mcStarter']['write-read'] = '[open open][write read][append read]'
G.add_edge('fidodaemon','mediaserver')
G.edge['fidodaemon']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['fidodaemon']['mediaserver']['fill'] = 'red'
G.add_edge('fidodaemon','mediaserver')
G.edge['fidodaemon']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('fidodaemon','seempd')
G.edge['fidodaemon']['seempd']['write-read'] = '[open open][write read]'
G.edge['fidodaemon']['seempd']['fill'] = 'red'
G.add_edge('fidodaemon','seempd')
G.edge['fidodaemon']['seempd']['write-read'] = '[open open][write read][append read]'
G.add_edge('fidodaemon','surfaceflinger')
G.edge['fidodaemon']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['fidodaemon']['surfaceflinger']['fill'] = 'red'
G.add_edge('fidodaemon','surfaceflinger')
G.edge['fidodaemon']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('fidodaemon','tbaseLoader')
G.edge['fidodaemon']['tbaseLoader']['write-read'] = '[open open][write read]'
G.edge['fidodaemon']['tbaseLoader']['fill'] = 'red'
G.add_edge('fidodaemon','tbaseLoader')
G.edge['fidodaemon']['tbaseLoader']['write-read'] = '[open open][write read][append read]'
G.add_edge('fidodaemon','tee')
G.edge['fidodaemon']['tee']['write-read'] = '[open open][write read]'
G.edge['fidodaemon']['tee']['fill'] = 'red'
G.add_edge('fidodaemon','tee')
G.edge['fidodaemon']['tee']['write-read'] = '[open open][write read][append read]'
G.add_edge('fidodaemon','vold')
G.edge['fidodaemon']['vold']['write-read'] = '[open open][write read]'
G.edge['fidodaemon']['vold']['fill'] = 'red'
G.add_edge('fidodaemon','vold')
G.edge['fidodaemon']['vold']['write-read'] = '[open open][write read][append read]'
G.add_edge('fidodaemon','wfdservice')
G.edge['fidodaemon']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['fidodaemon']['wfdservice']['fill'] = 'red'
G.add_edge('fidodaemon','wfdservice')
G.edge['fidodaemon']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('keystore','drmserver')
G.edge['keystore']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('keystore','fidodaemon')
G.edge['keystore']['fidodaemon']['write-read'] = '[open open]'
G.add_edge('keystore','keystore')
G.edge['keystore']['keystore']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('keystore','launcher')
G.edge['keystore']['launcher']['write-read'] = '[open open]'
G.add_edge('keystore','mcStarter')
G.edge['keystore']['mcStarter']['write-read'] = '[open open]'
G.add_edge('keystore','mediaserver')
G.edge['keystore']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('keystore','seempd')
G.edge['keystore']['seempd']['write-read'] = '[open open]'
G.add_edge('keystore','surfaceflinger')
G.edge['keystore']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('keystore','tbaseLoader')
G.edge['keystore']['tbaseLoader']['write-read'] = '[open open]'
G.add_edge('keystore','tee')
G.edge['keystore']['tee']['write-read'] = '[open open]'
G.add_edge('keystore','vold')
G.edge['keystore']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('keystore','wfdservice')
G.edge['keystore']['wfdservice']['write-read'] = '[open open]'
G.add_edge('keystore','drmserver')
G.edge['keystore']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['keystore']['drmserver']['fill'] = 'red'
G.add_edge('keystore','drmserver')
G.edge['keystore']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('keystore','fidodaemon')
G.edge['keystore']['fidodaemon']['write-read'] = '[open open][write read]'
G.edge['keystore']['fidodaemon']['fill'] = 'red'
G.add_edge('keystore','fidodaemon')
G.edge['keystore']['fidodaemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('keystore','keystore')
G.edge['keystore']['keystore']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['keystore']['keystore']['fill'] = 'red'
G.add_edge('keystore','keystore')
G.edge['keystore']['keystore']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('keystore','launcher')
G.edge['keystore']['launcher']['write-read'] = '[open open][write read]'
G.edge['keystore']['launcher']['fill'] = 'red'
G.add_edge('keystore','launcher')
G.edge['keystore']['launcher']['write-read'] = '[open open][write read][append read]'
G.add_edge('keystore','mcStarter')
G.edge['keystore']['mcStarter']['write-read'] = '[open open][write read]'
G.edge['keystore']['mcStarter']['fill'] = 'red'
G.add_edge('keystore','mcStarter')
G.edge['keystore']['mcStarter']['write-read'] = '[open open][write read][append read]'
G.add_edge('keystore','mediaserver')
G.edge['keystore']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['keystore']['mediaserver']['fill'] = 'red'
G.add_edge('keystore','mediaserver')
G.edge['keystore']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('keystore','seempd')
G.edge['keystore']['seempd']['write-read'] = '[open open][write read]'
G.edge['keystore']['seempd']['fill'] = 'red'
G.add_edge('keystore','seempd')
G.edge['keystore']['seempd']['write-read'] = '[open open][write read][append read]'
G.add_edge('keystore','surfaceflinger')
G.edge['keystore']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['keystore']['surfaceflinger']['fill'] = 'red'
G.add_edge('keystore','surfaceflinger')
G.edge['keystore']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('keystore','tbaseLoader')
G.edge['keystore']['tbaseLoader']['write-read'] = '[open open][write read]'
G.edge['keystore']['tbaseLoader']['fill'] = 'red'
G.add_edge('keystore','tbaseLoader')
G.edge['keystore']['tbaseLoader']['write-read'] = '[open open][write read][append read]'
G.add_edge('keystore','tee')
G.edge['keystore']['tee']['write-read'] = '[open open][write read]'
G.edge['keystore']['tee']['fill'] = 'red'
G.add_edge('keystore','tee')
G.edge['keystore']['tee']['write-read'] = '[open open][write read][append read]'
G.add_edge('keystore','vold')
G.edge['keystore']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['keystore']['vold']['fill'] = 'red'
G.add_edge('keystore','vold')
G.edge['keystore']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('keystore','wfdservice')
G.edge['keystore']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['keystore']['wfdservice']['fill'] = 'red'
G.add_edge('keystore','wfdservice')
G.edge['keystore']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('launcher','drmserver')
G.edge['launcher']['drmserver']['write-read'] = '[open open]'
G.add_edge('launcher','fidodaemon')
G.edge['launcher']['fidodaemon']['write-read'] = '[open open]'
G.add_edge('launcher','keystore')
G.edge['launcher']['keystore']['write-read'] = '[open open]'
G.add_edge('launcher','launcher')
G.edge['launcher']['launcher']['write-read'] = '[write read][open open]'
G.add_edge('launcher','mcStarter')
G.edge['launcher']['mcStarter']['write-read'] = '[open open]'
G.add_edge('launcher','mediaserver')
G.edge['launcher']['mediaserver']['write-read'] = '[open open]'
G.add_edge('launcher','seempd')
G.edge['launcher']['seempd']['write-read'] = '[open open]'
G.add_edge('launcher','surfaceflinger')
G.edge['launcher']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('launcher','tbaseLoader')
G.edge['launcher']['tbaseLoader']['write-read'] = '[open open]'
G.add_edge('launcher','tee')
G.edge['launcher']['tee']['write-read'] = '[open open]'
G.add_edge('launcher','vold')
G.edge['launcher']['vold']['write-read'] = '[open open]'
G.add_edge('launcher','wfdservice')
G.edge['launcher']['wfdservice']['write-read'] = '[open open]'
G.add_edge('launcher','drmserver')
G.edge['launcher']['drmserver']['write-read'] = '[open open][write read]'
G.edge['launcher']['drmserver']['fill'] = 'red'
G.add_edge('launcher','drmserver')
G.edge['launcher']['drmserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('launcher','fidodaemon')
G.edge['launcher']['fidodaemon']['write-read'] = '[open open][write read]'
G.edge['launcher']['fidodaemon']['fill'] = 'red'
G.add_edge('launcher','fidodaemon')
G.edge['launcher']['fidodaemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('launcher','keystore')
G.edge['launcher']['keystore']['write-read'] = '[open open][write read]'
G.edge['launcher']['keystore']['fill'] = 'red'
G.add_edge('launcher','keystore')
G.edge['launcher']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('launcher','launcher')
G.edge['launcher']['launcher']['write-read'] = '[write read][open open][write read]'
G.edge['launcher']['launcher']['fill'] = 'red'
G.add_edge('launcher','launcher')
G.edge['launcher']['launcher']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('launcher','mcStarter')
G.edge['launcher']['mcStarter']['write-read'] = '[open open][write read]'
G.edge['launcher']['mcStarter']['fill'] = 'red'
G.add_edge('launcher','mcStarter')
G.edge['launcher']['mcStarter']['write-read'] = '[open open][write read][append read]'
G.add_edge('launcher','mediaserver')
G.edge['launcher']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['launcher']['mediaserver']['fill'] = 'red'
G.add_edge('launcher','mediaserver')
G.edge['launcher']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('launcher','seempd')
G.edge['launcher']['seempd']['write-read'] = '[open open][write read]'
G.edge['launcher']['seempd']['fill'] = 'red'
G.add_edge('launcher','seempd')
G.edge['launcher']['seempd']['write-read'] = '[open open][write read][append read]'
G.add_edge('launcher','surfaceflinger')
G.edge['launcher']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['launcher']['surfaceflinger']['fill'] = 'red'
G.add_edge('launcher','surfaceflinger')
G.edge['launcher']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('launcher','tbaseLoader')
G.edge['launcher']['tbaseLoader']['write-read'] = '[open open][write read]'
G.edge['launcher']['tbaseLoader']['fill'] = 'red'
G.add_edge('launcher','tbaseLoader')
G.edge['launcher']['tbaseLoader']['write-read'] = '[open open][write read][append read]'
G.add_edge('launcher','tee')
G.edge['launcher']['tee']['write-read'] = '[open open][write read]'
G.edge['launcher']['tee']['fill'] = 'red'
G.add_edge('launcher','tee')
G.edge['launcher']['tee']['write-read'] = '[open open][write read][append read]'
G.add_edge('launcher','vold')
G.edge['launcher']['vold']['write-read'] = '[open open][write read]'
G.edge['launcher']['vold']['fill'] = 'red'
G.add_edge('launcher','vold')
G.edge['launcher']['vold']['write-read'] = '[open open][write read][append read]'
G.add_edge('launcher','wfdservice')
G.edge['launcher']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['launcher']['wfdservice']['fill'] = 'red'
G.add_edge('launcher','wfdservice')
G.edge['launcher']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('mcStarter','drmserver')
G.edge['mcStarter']['drmserver']['write-read'] = '[open open]'
G.add_edge('mcStarter','fidodaemon')
G.edge['mcStarter']['fidodaemon']['write-read'] = '[open open]'
G.add_edge('mcStarter','keystore')
G.edge['mcStarter']['keystore']['write-read'] = '[open open]'
G.add_edge('mcStarter','launcher')
G.edge['mcStarter']['launcher']['write-read'] = '[open open]'
G.add_edge('mcStarter','mcStarter')
G.edge['mcStarter']['mcStarter']['write-read'] = '[open open]'
G.add_edge('mcStarter','mediaserver')
G.edge['mcStarter']['mediaserver']['write-read'] = '[open open]'
G.add_edge('mcStarter','seempd')
G.edge['mcStarter']['seempd']['write-read'] = '[open open]'
G.add_edge('mcStarter','surfaceflinger')
G.edge['mcStarter']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('mcStarter','tbaseLoader')
G.edge['mcStarter']['tbaseLoader']['write-read'] = '[open open]'
G.add_edge('mcStarter','tee')
G.edge['mcStarter']['tee']['write-read'] = '[open open]'
G.add_edge('mcStarter','vold')
G.edge['mcStarter']['vold']['write-read'] = '[open open]'
G.add_edge('mcStarter','wfdservice')
G.edge['mcStarter']['wfdservice']['write-read'] = '[open open]'
G.add_edge('mcStarter','drmserver')
G.edge['mcStarter']['drmserver']['write-read'] = '[open open][write read]'
G.edge['mcStarter']['drmserver']['fill'] = 'red'
G.add_edge('mcStarter','drmserver')
G.edge['mcStarter']['drmserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('mcStarter','fidodaemon')
G.edge['mcStarter']['fidodaemon']['write-read'] = '[open open][write read]'
G.edge['mcStarter']['fidodaemon']['fill'] = 'red'
G.add_edge('mcStarter','fidodaemon')
G.edge['mcStarter']['fidodaemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('mcStarter','keystore')
G.edge['mcStarter']['keystore']['write-read'] = '[open open][write read]'
G.edge['mcStarter']['keystore']['fill'] = 'red'
G.add_edge('mcStarter','keystore')
G.edge['mcStarter']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('mcStarter','launcher')
G.edge['mcStarter']['launcher']['write-read'] = '[open open][write read]'
G.edge['mcStarter']['launcher']['fill'] = 'red'
G.add_edge('mcStarter','launcher')
G.edge['mcStarter']['launcher']['write-read'] = '[open open][write read][append read]'
G.add_edge('mcStarter','mcStarter')
G.edge['mcStarter']['mcStarter']['write-read'] = '[open open][write read]'
G.edge['mcStarter']['mcStarter']['fill'] = 'red'
G.add_edge('mcStarter','mcStarter')
G.edge['mcStarter']['mcStarter']['write-read'] = '[open open][write read][append read]'
G.add_edge('mcStarter','mediaserver')
G.edge['mcStarter']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['mcStarter']['mediaserver']['fill'] = 'red'
G.add_edge('mcStarter','mediaserver')
G.edge['mcStarter']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('mcStarter','seempd')
G.edge['mcStarter']['seempd']['write-read'] = '[open open][write read]'
G.edge['mcStarter']['seempd']['fill'] = 'red'
G.add_edge('mcStarter','seempd')
G.edge['mcStarter']['seempd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mcStarter','surfaceflinger')
G.edge['mcStarter']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['mcStarter']['surfaceflinger']['fill'] = 'red'
G.add_edge('mcStarter','surfaceflinger')
G.edge['mcStarter']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('mcStarter','tbaseLoader')
G.edge['mcStarter']['tbaseLoader']['write-read'] = '[open open][write read]'
G.edge['mcStarter']['tbaseLoader']['fill'] = 'red'
G.add_edge('mcStarter','tbaseLoader')
G.edge['mcStarter']['tbaseLoader']['write-read'] = '[open open][write read][append read]'
G.add_edge('mcStarter','tee')
G.edge['mcStarter']['tee']['write-read'] = '[open open][write read]'
G.edge['mcStarter']['tee']['fill'] = 'red'
G.add_edge('mcStarter','tee')
G.edge['mcStarter']['tee']['write-read'] = '[open open][write read][append read]'
G.add_edge('mcStarter','vold')
G.edge['mcStarter']['vold']['write-read'] = '[open open][write read]'
G.edge['mcStarter']['vold']['fill'] = 'red'
G.add_edge('mcStarter','vold')
G.edge['mcStarter']['vold']['write-read'] = '[open open][write read][append read]'
G.add_edge('mcStarter','wfdservice')
G.edge['mcStarter']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['mcStarter']['wfdservice']['fill'] = 'red'
G.add_edge('mcStarter','wfdservice')
G.edge['mcStarter']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','drmserver')
G.edge['mediaserver']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','fidodaemon')
G.edge['mediaserver']['fidodaemon']['write-read'] = '[open open]'
G.add_edge('mediaserver','keystore')
G.edge['mediaserver']['keystore']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','launcher')
G.edge['mediaserver']['launcher']['write-read'] = '[open open]'
G.add_edge('mediaserver','mcStarter')
G.edge['mediaserver']['mcStarter']['write-read'] = '[open open]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('mediaserver','seempd')
G.edge['mediaserver']['seempd']['write-read'] = '[open open]'
G.add_edge('mediaserver','surfaceflinger')
G.edge['mediaserver']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read][open open]'
G.add_edge('mediaserver','tbaseLoader')
G.edge['mediaserver']['tbaseLoader']['write-read'] = '[open open]'
G.add_edge('mediaserver','tee')
G.edge['mediaserver']['tee']['write-read'] = '[open open]'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('mediaserver','wfdservice')
G.edge['mediaserver']['wfdservice']['write-read'] = '[open open]'
G.add_edge('mediaserver','drmserver')
G.edge['mediaserver']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['drmserver']['fill'] = 'red'
G.add_edge('mediaserver','drmserver')
G.edge['mediaserver']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','fidodaemon')
G.edge['mediaserver']['fidodaemon']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['fidodaemon']['fill'] = 'red'
G.add_edge('mediaserver','fidodaemon')
G.edge['mediaserver']['fidodaemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','keystore')
G.edge['mediaserver']['keystore']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['keystore']['fill'] = 'red'
G.add_edge('mediaserver','keystore')
G.edge['mediaserver']['keystore']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','launcher')
G.edge['mediaserver']['launcher']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['launcher']['fill'] = 'red'
G.add_edge('mediaserver','launcher')
G.edge['mediaserver']['launcher']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','mcStarter')
G.edge['mediaserver']['mcStarter']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['mcStarter']['fill'] = 'red'
G.add_edge('mediaserver','mcStarter')
G.edge['mediaserver']['mcStarter']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['mediaserver']['mediaserver']['fill'] = 'red'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('mediaserver','seempd')
G.edge['mediaserver']['seempd']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['seempd']['fill'] = 'red'
G.add_edge('mediaserver','seempd')
G.edge['mediaserver']['seempd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','surfaceflinger')
G.edge['mediaserver']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read][open open][write read]'
G.edge['mediaserver']['surfaceflinger']['fill'] = 'red'
G.add_edge('mediaserver','surfaceflinger')
G.edge['mediaserver']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read]'
G.add_edge('mediaserver','tbaseLoader')
G.edge['mediaserver']['tbaseLoader']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['tbaseLoader']['fill'] = 'red'
G.add_edge('mediaserver','tbaseLoader')
G.edge['mediaserver']['tbaseLoader']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','tee')
G.edge['mediaserver']['tee']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['tee']['fill'] = 'red'
G.add_edge('mediaserver','tee')
G.edge['mediaserver']['tee']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['mediaserver']['vold']['fill'] = 'red'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('mediaserver','wfdservice')
G.edge['mediaserver']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['wfdservice']['fill'] = 'red'
G.add_edge('mediaserver','wfdservice')
G.edge['mediaserver']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('seempd','drmserver')
G.edge['seempd']['drmserver']['write-read'] = '[open open]'
G.add_edge('seempd','fidodaemon')
G.edge['seempd']['fidodaemon']['write-read'] = '[open open]'
G.add_edge('seempd','keystore')
G.edge['seempd']['keystore']['write-read'] = '[open open]'
G.add_edge('seempd','launcher')
G.edge['seempd']['launcher']['write-read'] = '[open open]'
G.add_edge('seempd','mcStarter')
G.edge['seempd']['mcStarter']['write-read'] = '[open open]'
G.add_edge('seempd','mediaserver')
G.edge['seempd']['mediaserver']['write-read'] = '[open open]'
G.add_edge('seempd','seempd')
G.edge['seempd']['seempd']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('seempd','surfaceflinger')
G.edge['seempd']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('seempd','tbaseLoader')
G.edge['seempd']['tbaseLoader']['write-read'] = '[open open]'
G.add_edge('seempd','tee')
G.edge['seempd']['tee']['write-read'] = '[open open]'
G.add_edge('seempd','vold')
G.edge['seempd']['vold']['write-read'] = '[open open]'
G.add_edge('seempd','wfdservice')
G.edge['seempd']['wfdservice']['write-read'] = '[open open]'
G.add_edge('seempd','drmserver')
G.edge['seempd']['drmserver']['write-read'] = '[open open][write read]'
G.edge['seempd']['drmserver']['fill'] = 'red'
G.add_edge('seempd','drmserver')
G.edge['seempd']['drmserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('seempd','fidodaemon')
G.edge['seempd']['fidodaemon']['write-read'] = '[open open][write read]'
G.edge['seempd']['fidodaemon']['fill'] = 'red'
G.add_edge('seempd','fidodaemon')
G.edge['seempd']['fidodaemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('seempd','keystore')
G.edge['seempd']['keystore']['write-read'] = '[open open][write read]'
G.edge['seempd']['keystore']['fill'] = 'red'
G.add_edge('seempd','keystore')
G.edge['seempd']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('seempd','launcher')
G.edge['seempd']['launcher']['write-read'] = '[open open][write read]'
G.edge['seempd']['launcher']['fill'] = 'red'
G.add_edge('seempd','launcher')
G.edge['seempd']['launcher']['write-read'] = '[open open][write read][append read]'
G.add_edge('seempd','mcStarter')
G.edge['seempd']['mcStarter']['write-read'] = '[open open][write read]'
G.edge['seempd']['mcStarter']['fill'] = 'red'
G.add_edge('seempd','mcStarter')
G.edge['seempd']['mcStarter']['write-read'] = '[open open][write read][append read]'
G.add_edge('seempd','mediaserver')
G.edge['seempd']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['seempd']['mediaserver']['fill'] = 'red'
G.add_edge('seempd','mediaserver')
G.edge['seempd']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('seempd','seempd')
G.edge['seempd']['seempd']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['seempd']['seempd']['fill'] = 'red'
G.add_edge('seempd','seempd')
G.edge['seempd']['seempd']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('seempd','surfaceflinger')
G.edge['seempd']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['seempd']['surfaceflinger']['fill'] = 'red'
G.add_edge('seempd','surfaceflinger')
G.edge['seempd']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('seempd','tbaseLoader')
G.edge['seempd']['tbaseLoader']['write-read'] = '[open open][write read]'
G.edge['seempd']['tbaseLoader']['fill'] = 'red'
G.add_edge('seempd','tbaseLoader')
G.edge['seempd']['tbaseLoader']['write-read'] = '[open open][write read][append read]'
G.add_edge('seempd','tee')
G.edge['seempd']['tee']['write-read'] = '[open open][write read]'
G.edge['seempd']['tee']['fill'] = 'red'
G.add_edge('seempd','tee')
G.edge['seempd']['tee']['write-read'] = '[open open][write read][append read]'
G.add_edge('seempd','vold')
G.edge['seempd']['vold']['write-read'] = '[open open][write read]'
G.edge['seempd']['vold']['fill'] = 'red'
G.add_edge('seempd','vold')
G.edge['seempd']['vold']['write-read'] = '[open open][write read][append read]'
G.add_edge('seempd','wfdservice')
G.edge['seempd']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['seempd']['wfdservice']['fill'] = 'red'
G.add_edge('seempd','wfdservice')
G.edge['seempd']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','drmserver')
G.edge['surfaceflinger']['drmserver']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','fidodaemon')
G.edge['surfaceflinger']['fidodaemon']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','keystore')
G.edge['surfaceflinger']['keystore']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','launcher')
G.edge['surfaceflinger']['launcher']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','mcStarter')
G.edge['surfaceflinger']['mcStarter']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','mediaserver')
G.edge['surfaceflinger']['mediaserver']['write-read'] = '[open open][write read][append read][write read][append read][open open]'
G.add_edge('surfaceflinger','seempd')
G.edge['surfaceflinger']['seempd']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open]'
G.add_edge('surfaceflinger','tbaseLoader')
G.edge['surfaceflinger']['tbaseLoader']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','tee')
G.edge['surfaceflinger']['tee']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','vold')
G.edge['surfaceflinger']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open]'
G.add_edge('surfaceflinger','wfdservice')
G.edge['surfaceflinger']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open]'
G.add_edge('surfaceflinger','drmserver')
G.edge['surfaceflinger']['drmserver']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['drmserver']['fill'] = 'red'
G.add_edge('surfaceflinger','drmserver')
G.edge['surfaceflinger']['drmserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','fidodaemon')
G.edge['surfaceflinger']['fidodaemon']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['fidodaemon']['fill'] = 'red'
G.add_edge('surfaceflinger','fidodaemon')
G.edge['surfaceflinger']['fidodaemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','keystore')
G.edge['surfaceflinger']['keystore']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['keystore']['fill'] = 'red'
G.add_edge('surfaceflinger','keystore')
G.edge['surfaceflinger']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','launcher')
G.edge['surfaceflinger']['launcher']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['launcher']['fill'] = 'red'
G.add_edge('surfaceflinger','launcher')
G.edge['surfaceflinger']['launcher']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','mcStarter')
G.edge['surfaceflinger']['mcStarter']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['mcStarter']['fill'] = 'red'
G.add_edge('surfaceflinger','mcStarter')
G.edge['surfaceflinger']['mcStarter']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','mediaserver')
G.edge['surfaceflinger']['mediaserver']['write-read'] = '[open open][write read][append read][write read][append read][open open][write read]'
G.edge['surfaceflinger']['mediaserver']['fill'] = 'red'
G.add_edge('surfaceflinger','mediaserver')
G.edge['surfaceflinger']['mediaserver']['write-read'] = '[open open][write read][append read][write read][append read][open open][write read][append read]'
G.add_edge('surfaceflinger','seempd')
G.edge['surfaceflinger']['seempd']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['seempd']['fill'] = 'red'
G.add_edge('surfaceflinger','seempd')
G.edge['surfaceflinger']['seempd']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read]'
G.edge['surfaceflinger']['surfaceflinger']['fill'] = 'red'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read]'
G.add_edge('surfaceflinger','tbaseLoader')
G.edge['surfaceflinger']['tbaseLoader']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['tbaseLoader']['fill'] = 'red'
G.add_edge('surfaceflinger','tbaseLoader')
G.edge['surfaceflinger']['tbaseLoader']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','tee')
G.edge['surfaceflinger']['tee']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['tee']['fill'] = 'red'
G.add_edge('surfaceflinger','tee')
G.edge['surfaceflinger']['tee']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','vold')
G.edge['surfaceflinger']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read]'
G.edge['surfaceflinger']['vold']['fill'] = 'red'
G.add_edge('surfaceflinger','vold')
G.edge['surfaceflinger']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read]'
G.add_edge('surfaceflinger','wfdservice')
G.edge['surfaceflinger']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read]'
G.edge['surfaceflinger']['wfdservice']['fill'] = 'red'
G.add_edge('surfaceflinger','wfdservice')
G.edge['surfaceflinger']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read]'
G.add_edge('tbaseLoader','drmserver')
G.edge['tbaseLoader']['drmserver']['write-read'] = '[open open]'
G.add_edge('tbaseLoader','fidodaemon')
G.edge['tbaseLoader']['fidodaemon']['write-read'] = '[open open]'
G.add_edge('tbaseLoader','keystore')
G.edge['tbaseLoader']['keystore']['write-read'] = '[open open]'
G.add_edge('tbaseLoader','launcher')
G.edge['tbaseLoader']['launcher']['write-read'] = '[open open]'
G.add_edge('tbaseLoader','mcStarter')
G.edge['tbaseLoader']['mcStarter']['write-read'] = '[open open]'
G.add_edge('tbaseLoader','mediaserver')
G.edge['tbaseLoader']['mediaserver']['write-read'] = '[open open]'
G.add_edge('tbaseLoader','seempd')
G.edge['tbaseLoader']['seempd']['write-read'] = '[open open]'
G.add_edge('tbaseLoader','surfaceflinger')
G.edge['tbaseLoader']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('tbaseLoader','tbaseLoader')
G.edge['tbaseLoader']['tbaseLoader']['write-read'] = '[open open]'
G.add_edge('tbaseLoader','tee')
G.edge['tbaseLoader']['tee']['write-read'] = '[open open]'
G.add_edge('tbaseLoader','vold')
G.edge['tbaseLoader']['vold']['write-read'] = '[open open]'
G.add_edge('tbaseLoader','wfdservice')
G.edge['tbaseLoader']['wfdservice']['write-read'] = '[open open]'
G.add_edge('tbaseLoader','drmserver')
G.edge['tbaseLoader']['drmserver']['write-read'] = '[open open][write read]'
G.edge['tbaseLoader']['drmserver']['fill'] = 'red'
G.add_edge('tbaseLoader','drmserver')
G.edge['tbaseLoader']['drmserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('tbaseLoader','fidodaemon')
G.edge['tbaseLoader']['fidodaemon']['write-read'] = '[open open][write read]'
G.edge['tbaseLoader']['fidodaemon']['fill'] = 'red'
G.add_edge('tbaseLoader','fidodaemon')
G.edge['tbaseLoader']['fidodaemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('tbaseLoader','keystore')
G.edge['tbaseLoader']['keystore']['write-read'] = '[open open][write read]'
G.edge['tbaseLoader']['keystore']['fill'] = 'red'
G.add_edge('tbaseLoader','keystore')
G.edge['tbaseLoader']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('tbaseLoader','launcher')
G.edge['tbaseLoader']['launcher']['write-read'] = '[open open][write read]'
G.edge['tbaseLoader']['launcher']['fill'] = 'red'
G.add_edge('tbaseLoader','launcher')
G.edge['tbaseLoader']['launcher']['write-read'] = '[open open][write read][append read]'
G.add_edge('tbaseLoader','mcStarter')
G.edge['tbaseLoader']['mcStarter']['write-read'] = '[open open][write read]'
G.edge['tbaseLoader']['mcStarter']['fill'] = 'red'
G.add_edge('tbaseLoader','mcStarter')
G.edge['tbaseLoader']['mcStarter']['write-read'] = '[open open][write read][append read]'
G.add_edge('tbaseLoader','mediaserver')
G.edge['tbaseLoader']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['tbaseLoader']['mediaserver']['fill'] = 'red'
G.add_edge('tbaseLoader','mediaserver')
G.edge['tbaseLoader']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('tbaseLoader','seempd')
G.edge['tbaseLoader']['seempd']['write-read'] = '[open open][write read]'
G.edge['tbaseLoader']['seempd']['fill'] = 'red'
G.add_edge('tbaseLoader','seempd')
G.edge['tbaseLoader']['seempd']['write-read'] = '[open open][write read][append read]'
G.add_edge('tbaseLoader','surfaceflinger')
G.edge['tbaseLoader']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['tbaseLoader']['surfaceflinger']['fill'] = 'red'
G.add_edge('tbaseLoader','surfaceflinger')
G.edge['tbaseLoader']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('tbaseLoader','tbaseLoader')
G.edge['tbaseLoader']['tbaseLoader']['write-read'] = '[open open][write read]'
G.edge['tbaseLoader']['tbaseLoader']['fill'] = 'red'
G.add_edge('tbaseLoader','tbaseLoader')
G.edge['tbaseLoader']['tbaseLoader']['write-read'] = '[open open][write read][append read]'
G.add_edge('tbaseLoader','tee')
G.edge['tbaseLoader']['tee']['write-read'] = '[open open][write read]'
G.edge['tbaseLoader']['tee']['fill'] = 'red'
G.add_edge('tbaseLoader','tee')
G.edge['tbaseLoader']['tee']['write-read'] = '[open open][write read][append read]'
G.add_edge('tbaseLoader','vold')
G.edge['tbaseLoader']['vold']['write-read'] = '[open open][write read]'
G.edge['tbaseLoader']['vold']['fill'] = 'red'
G.add_edge('tbaseLoader','vold')
G.edge['tbaseLoader']['vold']['write-read'] = '[open open][write read][append read]'
G.add_edge('tbaseLoader','wfdservice')
G.edge['tbaseLoader']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['tbaseLoader']['wfdservice']['fill'] = 'red'
G.add_edge('tbaseLoader','wfdservice')
G.edge['tbaseLoader']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('tee','drmserver')
G.edge['tee']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('tee','fidodaemon')
G.edge['tee']['fidodaemon']['write-read'] = '[open open]'
G.add_edge('tee','keystore')
G.edge['tee']['keystore']['write-read'] = '[open open]'
G.add_edge('tee','launcher')
G.edge['tee']['launcher']['write-read'] = '[open open]'
G.add_edge('tee','mcStarter')
G.edge['tee']['mcStarter']['write-read'] = '[open open]'
G.add_edge('tee','mediaserver')
G.edge['tee']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('tee','seempd')
G.edge['tee']['seempd']['write-read'] = '[open open]'
G.add_edge('tee','surfaceflinger')
G.edge['tee']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('tee','tbaseLoader')
G.edge['tee']['tbaseLoader']['write-read'] = '[open open]'
G.add_edge('tee','tee')
G.edge['tee']['tee']['write-read'] = '[write read][open open]'
G.add_edge('tee','vold')
G.edge['tee']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('tee','wfdservice')
G.edge['tee']['wfdservice']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('tee','drmserver')
G.edge['tee']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['tee']['drmserver']['fill'] = 'red'
G.add_edge('tee','drmserver')
G.edge['tee']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('tee','fidodaemon')
G.edge['tee']['fidodaemon']['write-read'] = '[open open][write read]'
G.edge['tee']['fidodaemon']['fill'] = 'red'
G.add_edge('tee','fidodaemon')
G.edge['tee']['fidodaemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('tee','keystore')
G.edge['tee']['keystore']['write-read'] = '[open open][write read]'
G.edge['tee']['keystore']['fill'] = 'red'
G.add_edge('tee','keystore')
G.edge['tee']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('tee','launcher')
G.edge['tee']['launcher']['write-read'] = '[open open][write read]'
G.edge['tee']['launcher']['fill'] = 'red'
G.add_edge('tee','launcher')
G.edge['tee']['launcher']['write-read'] = '[open open][write read][append read]'
G.add_edge('tee','mcStarter')
G.edge['tee']['mcStarter']['write-read'] = '[open open][write read]'
G.edge['tee']['mcStarter']['fill'] = 'red'
G.add_edge('tee','mcStarter')
G.edge['tee']['mcStarter']['write-read'] = '[open open][write read][append read]'
G.add_edge('tee','mediaserver')
G.edge['tee']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['tee']['mediaserver']['fill'] = 'red'
G.add_edge('tee','mediaserver')
G.edge['tee']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('tee','seempd')
G.edge['tee']['seempd']['write-read'] = '[open open][write read]'
G.edge['tee']['seempd']['fill'] = 'red'
G.add_edge('tee','seempd')
G.edge['tee']['seempd']['write-read'] = '[open open][write read][append read]'
G.add_edge('tee','surfaceflinger')
G.edge['tee']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['tee']['surfaceflinger']['fill'] = 'red'
G.add_edge('tee','surfaceflinger')
G.edge['tee']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('tee','tbaseLoader')
G.edge['tee']['tbaseLoader']['write-read'] = '[open open][write read]'
G.edge['tee']['tbaseLoader']['fill'] = 'red'
G.add_edge('tee','tbaseLoader')
G.edge['tee']['tbaseLoader']['write-read'] = '[open open][write read][append read]'
G.add_edge('tee','tee')
G.edge['tee']['tee']['write-read'] = '[write read][open open][write read]'
G.edge['tee']['tee']['fill'] = 'red'
G.add_edge('tee','tee')
G.edge['tee']['tee']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('tee','vold')
G.edge['tee']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['tee']['vold']['fill'] = 'red'
G.add_edge('tee','vold')
G.edge['tee']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('tee','wfdservice')
G.edge['tee']['wfdservice']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['tee']['wfdservice']['fill'] = 'red'
G.add_edge('tee','wfdservice')
G.edge['tee']['wfdservice']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('vold','drmserver')
G.edge['vold']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('vold','fidodaemon')
G.edge['vold']['fidodaemon']['write-read'] = '[open open]'
G.add_edge('vold','keystore')
G.edge['vold']['keystore']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','launcher')
G.edge['vold']['launcher']['write-read'] = '[open open]'
G.add_edge('vold','mcStarter')
G.edge['vold']['mcStarter']['write-read'] = '[open open]'
G.add_edge('vold','mediaserver')
G.edge['vold']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('vold','seempd')
G.edge['vold']['seempd']['write-read'] = '[open open]'
G.add_edge('vold','surfaceflinger')
G.edge['vold']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][open open]'
G.add_edge('vold','tbaseLoader')
G.edge['vold']['tbaseLoader']['write-read'] = '[open open]'
G.add_edge('vold','tee')
G.edge['vold']['tee']['write-read'] = '[open open]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('vold','wfdservice')
G.edge['vold']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('vold','drmserver')
G.edge['vold']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['vold']['drmserver']['fill'] = 'red'
G.add_edge('vold','drmserver')
G.edge['vold']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','fidodaemon')
G.edge['vold']['fidodaemon']['write-read'] = '[open open][write read]'
G.edge['vold']['fidodaemon']['fill'] = 'red'
G.add_edge('vold','fidodaemon')
G.edge['vold']['fidodaemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','keystore')
G.edge['vold']['keystore']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['keystore']['fill'] = 'red'
G.add_edge('vold','keystore')
G.edge['vold']['keystore']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','launcher')
G.edge['vold']['launcher']['write-read'] = '[open open][write read]'
G.edge['vold']['launcher']['fill'] = 'red'
G.add_edge('vold','launcher')
G.edge['vold']['launcher']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','mcStarter')
G.edge['vold']['mcStarter']['write-read'] = '[open open][write read]'
G.edge['vold']['mcStarter']['fill'] = 'red'
G.add_edge('vold','mcStarter')
G.edge['vold']['mcStarter']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','mediaserver')
G.edge['vold']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['vold']['mediaserver']['fill'] = 'red'
G.add_edge('vold','mediaserver')
G.edge['vold']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('vold','seempd')
G.edge['vold']['seempd']['write-read'] = '[open open][write read]'
G.edge['vold']['seempd']['fill'] = 'red'
G.add_edge('vold','seempd')
G.edge['vold']['seempd']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','surfaceflinger')
G.edge['vold']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][open open][write read]'
G.edge['vold']['surfaceflinger']['fill'] = 'red'
G.add_edge('vold','surfaceflinger')
G.edge['vold']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read]'
G.add_edge('vold','tbaseLoader')
G.edge['vold']['tbaseLoader']['write-read'] = '[open open][write read]'
G.edge['vold']['tbaseLoader']['fill'] = 'red'
G.add_edge('vold','tbaseLoader')
G.edge['vold']['tbaseLoader']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','tee')
G.edge['vold']['tee']['write-read'] = '[open open][write read]'
G.edge['vold']['tee']['fill'] = 'red'
G.add_edge('vold','tee')
G.edge['vold']['tee']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['vold']['vold']['fill'] = 'red'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('vold','wfdservice')
G.edge['vold']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['vold']['wfdservice']['fill'] = 'red'
G.add_edge('vold','wfdservice')
G.edge['vold']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('wfdservice','drmserver')
G.edge['wfdservice']['drmserver']['write-read'] = '[open open]'
G.add_edge('wfdservice','fidodaemon')
G.edge['wfdservice']['fidodaemon']['write-read'] = '[open open]'
G.add_edge('wfdservice','keystore')
G.edge['wfdservice']['keystore']['write-read'] = '[open open]'
G.add_edge('wfdservice','launcher')
G.edge['wfdservice']['launcher']['write-read'] = '[open open]'
G.add_edge('wfdservice','mcStarter')
G.edge['wfdservice']['mcStarter']['write-read'] = '[open open]'
G.add_edge('wfdservice','mediaserver')
G.edge['wfdservice']['mediaserver']['write-read'] = '[open open]'
G.add_edge('wfdservice','seempd')
G.edge['wfdservice']['seempd']['write-read'] = '[open open]'
G.add_edge('wfdservice','surfaceflinger')
G.edge['wfdservice']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open]'
G.add_edge('wfdservice','tbaseLoader')
G.edge['wfdservice']['tbaseLoader']['write-read'] = '[open open]'
G.add_edge('wfdservice','tee')
G.edge['wfdservice']['tee']['write-read'] = '[open open]'
G.add_edge('wfdservice','vold')
G.edge['wfdservice']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('wfdservice','wfdservice')
G.edge['wfdservice']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open]'
G.add_edge('wfdservice','drmserver')
G.edge['wfdservice']['drmserver']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['drmserver']['fill'] = 'red'
G.add_edge('wfdservice','drmserver')
G.edge['wfdservice']['drmserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','fidodaemon')
G.edge['wfdservice']['fidodaemon']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['fidodaemon']['fill'] = 'red'
G.add_edge('wfdservice','fidodaemon')
G.edge['wfdservice']['fidodaemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','keystore')
G.edge['wfdservice']['keystore']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['keystore']['fill'] = 'red'
G.add_edge('wfdservice','keystore')
G.edge['wfdservice']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','launcher')
G.edge['wfdservice']['launcher']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['launcher']['fill'] = 'red'
G.add_edge('wfdservice','launcher')
G.edge['wfdservice']['launcher']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','mcStarter')
G.edge['wfdservice']['mcStarter']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['mcStarter']['fill'] = 'red'
G.add_edge('wfdservice','mcStarter')
G.edge['wfdservice']['mcStarter']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','mediaserver')
G.edge['wfdservice']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['mediaserver']['fill'] = 'red'
G.add_edge('wfdservice','mediaserver')
G.edge['wfdservice']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','seempd')
G.edge['wfdservice']['seempd']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['seempd']['fill'] = 'red'
G.add_edge('wfdservice','seempd')
G.edge['wfdservice']['seempd']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','surfaceflinger')
G.edge['wfdservice']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read]'
G.edge['wfdservice']['surfaceflinger']['fill'] = 'red'
G.add_edge('wfdservice','surfaceflinger')
G.edge['wfdservice']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read]'
G.add_edge('wfdservice','tbaseLoader')
G.edge['wfdservice']['tbaseLoader']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['tbaseLoader']['fill'] = 'red'
G.add_edge('wfdservice','tbaseLoader')
G.edge['wfdservice']['tbaseLoader']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','tee')
G.edge['wfdservice']['tee']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['tee']['fill'] = 'red'
G.add_edge('wfdservice','tee')
G.edge['wfdservice']['tee']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','vold')
G.edge['wfdservice']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['wfdservice']['vold']['fill'] = 'red'
G.add_edge('wfdservice','vold')
G.edge['wfdservice']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('wfdservice','wfdservice')
G.edge['wfdservice']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read]'
G.edge['wfdservice']['wfdservice']['fill'] = 'red'
G.add_edge('wfdservice','wfdservice')
G.edge['wfdservice']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()