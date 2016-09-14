import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('carrier_app','installd')
G.edge['carrier_app']['installd']['write-read'] = '[open open]'
G.add_edge('carrier_app','itsonbs')
G.edge['carrier_app']['itsonbs']['write-read'] = '[open open]'
G.add_edge('carrier_app','itsonclient_app')
G.edge['carrier_app']['itsonclient_app']['write-read'] = '[open open]'
G.add_edge('carrier_app','installd')
G.edge['carrier_app']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','itsonbs')
G.edge['carrier_app']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','itsonclient_app')
G.edge['carrier_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','installd')
G.edge['carrier_app']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['carrier_app']['installd']['fill'] = 'red'
G.add_edge('carrier_app','itsonbs')
G.edge['carrier_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['carrier_app']['itsonbs']['fill'] = 'red'
G.add_edge('carrier_app','itsonclient_app')
G.edge['carrier_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['carrier_app']['itsonclient_app']['fill'] = 'red'
G.add_edge('carrier_app','installd')
G.edge['carrier_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('carrier_app','installd')
G.edge['carrier_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('carrier_app','itsonbs')
G.edge['carrier_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('carrier_app','itsonbs')
G.edge['carrier_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('carrier_app','itsonclient_app')
G.edge['carrier_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('carrier_app','itsonclient_app')
G.edge['carrier_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dex2oat','installd')
G.edge['dex2oat']['installd']['write-read'] = '[open open]'
G.add_edge('dex2oat','itsonbs')
G.edge['dex2oat']['itsonbs']['write-read'] = '[open open]'
G.add_edge('dex2oat','itsonclient_app')
G.edge['dex2oat']['itsonclient_app']['write-read'] = '[open open]'
G.add_edge('dex2oat','installd')
G.edge['dex2oat']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dex2oat','itsonbs')
G.edge['dex2oat']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dex2oat','itsonclient_app')
G.edge['dex2oat']['itsonclient_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dex2oat','installd')
G.edge['dex2oat']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dex2oat']['installd']['fill'] = 'red'
G.add_edge('dex2oat','itsonbs')
G.edge['dex2oat']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dex2oat']['itsonbs']['fill'] = 'red'
G.add_edge('dex2oat','itsonclient_app')
G.edge['dex2oat']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dex2oat']['itsonclient_app']['fill'] = 'red'
G.add_edge('dex2oat','installd')
G.edge['dex2oat']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dex2oat','installd')
G.edge['dex2oat']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dex2oat','itsonbs')
G.edge['dex2oat']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dex2oat','itsonbs')
G.edge['dex2oat']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dex2oat','itsonclient_app')
G.edge['dex2oat']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dex2oat','itsonclient_app')
G.edge['dex2oat']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('filtered_google_app','installd')
G.edge['filtered_google_app']['installd']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','itsonbs')
G.edge['filtered_google_app']['itsonbs']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','itsonclient_app')
G.edge['filtered_google_app']['itsonclient_app']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','installd')
G.edge['filtered_google_app']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','itsonbs')
G.edge['filtered_google_app']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','itsonclient_app')
G.edge['filtered_google_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','installd')
G.edge['filtered_google_app']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_google_app']['installd']['fill'] = 'red'
G.add_edge('filtered_google_app','itsonbs')
G.edge['filtered_google_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_google_app']['itsonbs']['fill'] = 'red'
G.add_edge('filtered_google_app','itsonclient_app')
G.edge['filtered_google_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_google_app']['itsonclient_app']['fill'] = 'red'
G.add_edge('filtered_google_app','installd')
G.edge['filtered_google_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('filtered_google_app','installd')
G.edge['filtered_google_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('filtered_google_app','itsonbs')
G.edge['filtered_google_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('filtered_google_app','itsonbs')
G.edge['filtered_google_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('filtered_google_app','itsonclient_app')
G.edge['filtered_google_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('filtered_google_app','itsonclient_app')
G.edge['filtered_google_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('filtered_untrusted_app','installd')
G.edge['filtered_untrusted_app']['installd']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','itsonbs')
G.edge['filtered_untrusted_app']['itsonbs']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','itsonclient_app')
G.edge['filtered_untrusted_app']['itsonclient_app']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','installd')
G.edge['filtered_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','itsonbs')
G.edge['filtered_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','itsonclient_app')
G.edge['filtered_untrusted_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','installd')
G.edge['filtered_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['installd']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','itsonbs')
G.edge['filtered_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['itsonbs']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','itsonclient_app')
G.edge['filtered_untrusted_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['filtered_untrusted_app']['itsonclient_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','installd')
G.edge['filtered_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('filtered_untrusted_app','installd')
G.edge['filtered_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('filtered_untrusted_app','itsonbs')
G.edge['filtered_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('filtered_untrusted_app','itsonbs')
G.edge['filtered_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('filtered_untrusted_app','itsonclient_app')
G.edge['filtered_untrusted_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('filtered_untrusted_app','itsonclient_app')
G.edge['filtered_untrusted_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('gad_untrusted_app','installd')
G.edge['gad_untrusted_app']['installd']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','itsonbs')
G.edge['gad_untrusted_app']['itsonbs']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','itsonclient_app')
G.edge['gad_untrusted_app']['itsonclient_app']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','installd')
G.edge['gad_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','itsonbs')
G.edge['gad_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','itsonclient_app')
G.edge['gad_untrusted_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','installd')
G.edge['gad_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['installd']['fill'] = 'red'
G.add_edge('gad_untrusted_app','itsonbs')
G.edge['gad_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['itsonbs']['fill'] = 'red'
G.add_edge('gad_untrusted_app','itsonclient_app')
G.edge['gad_untrusted_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['gad_untrusted_app']['itsonclient_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','installd')
G.edge['gad_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('gad_untrusted_app','installd')
G.edge['gad_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('gad_untrusted_app','itsonbs')
G.edge['gad_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('gad_untrusted_app','itsonbs')
G.edge['gad_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('gad_untrusted_app','itsonclient_app')
G.edge['gad_untrusted_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('gad_untrusted_app','itsonclient_app')
G.edge['gad_untrusted_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('installd','itsonbs')
G.edge['installd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('installd','itsonclient_app')
G.edge['installd']['itsonclient_app']['write-read'] = '[open open]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('installd','itsonbs')
G.edge['installd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('installd','itsonclient_app')
G.edge['installd']['itsonclient_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['installd']['installd']['fill'] = 'red'
G.add_edge('installd','itsonbs')
G.edge['installd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['installd']['itsonbs']['fill'] = 'red'
G.add_edge('installd','itsonclient_app')
G.edge['installd']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['itsonclient_app']['fill'] = 'red'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','itsonbs')
G.edge['installd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','itsonbs')
G.edge['installd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','itsonclient_app')
G.edge['installd']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','itsonclient_app')
G.edge['installd']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('irm_app','installd')
G.edge['irm_app']['installd']['write-read'] = '[open open]'
G.add_edge('irm_app','itsonbs')
G.edge['irm_app']['itsonbs']['write-read'] = '[open open]'
G.add_edge('irm_app','itsonclient_app')
G.edge['irm_app']['itsonclient_app']['write-read'] = '[open open]'
G.add_edge('irm_app','installd')
G.edge['irm_app']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','itsonbs')
G.edge['irm_app']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','itsonclient_app')
G.edge['irm_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','installd')
G.edge['irm_app']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_app']['installd']['fill'] = 'red'
G.add_edge('irm_app','itsonbs')
G.edge['irm_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_app']['itsonbs']['fill'] = 'red'
G.add_edge('irm_app','itsonclient_app')
G.edge['irm_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_app']['itsonclient_app']['fill'] = 'red'
G.add_edge('irm_app','installd')
G.edge['irm_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('irm_app','installd')
G.edge['irm_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('irm_app','itsonbs')
G.edge['irm_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('irm_app','itsonbs')
G.edge['irm_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('irm_app','itsonclient_app')
G.edge['irm_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('irm_app','itsonclient_app')
G.edge['irm_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','installd')
G.edge['itsonbs']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('itsonbs','itsonbs')
G.edge['itsonbs']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('itsonbs','itsonclient_app')
G.edge['itsonbs']['itsonclient_app']['write-read'] = '[open open]'
G.add_edge('itsonbs','installd')
G.edge['itsonbs']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('itsonbs','itsonbs')
G.edge['itsonbs']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('itsonbs','itsonclient_app')
G.edge['itsonbs']['itsonclient_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','installd')
G.edge['itsonbs']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['itsonbs']['installd']['fill'] = 'red'
G.add_edge('itsonbs','itsonbs')
G.edge['itsonbs']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['itsonbs']['itsonbs']['fill'] = 'red'
G.add_edge('itsonbs','itsonclient_app')
G.edge['itsonbs']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['itsonclient_app']['fill'] = 'red'
G.add_edge('itsonbs','installd')
G.edge['itsonbs']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','installd')
G.edge['itsonbs']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','itsonbs')
G.edge['itsonbs']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','itsonbs')
G.edge['itsonbs']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','itsonclient_app')
G.edge['itsonbs']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','itsonclient_app')
G.edge['itsonbs']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonclient_app','installd')
G.edge['itsonclient_app']['installd']['write-read'] = '[open open]'
G.add_edge('itsonclient_app','itsonbs')
G.edge['itsonclient_app']['itsonbs']['write-read'] = '[open open]'
G.add_edge('itsonclient_app','itsonclient_app')
G.edge['itsonclient_app']['itsonclient_app']['write-read'] = '[open open]'
G.add_edge('itsonclient_app','installd')
G.edge['itsonclient_app']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonclient_app','itsonbs')
G.edge['itsonclient_app']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonclient_app','itsonclient_app')
G.edge['itsonclient_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonclient_app','installd')
G.edge['itsonclient_app']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonclient_app']['installd']['fill'] = 'red'
G.add_edge('itsonclient_app','itsonbs')
G.edge['itsonclient_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonclient_app']['itsonbs']['fill'] = 'red'
G.add_edge('itsonclient_app','itsonclient_app')
G.edge['itsonclient_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonclient_app']['itsonclient_app']['fill'] = 'red'
G.add_edge('itsonclient_app','installd')
G.edge['itsonclient_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonclient_app','installd')
G.edge['itsonclient_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonclient_app','itsonbs')
G.edge['itsonclient_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonclient_app','itsonbs')
G.edge['itsonclient_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonclient_app','itsonclient_app')
G.edge['itsonclient_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonclient_app','itsonclient_app')
G.edge['itsonclient_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('knox_untrusted_app','installd')
G.edge['knox_untrusted_app']['installd']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','itsonbs')
G.edge['knox_untrusted_app']['itsonbs']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','itsonclient_app')
G.edge['knox_untrusted_app']['itsonclient_app']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','installd')
G.edge['knox_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','itsonbs')
G.edge['knox_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','itsonclient_app')
G.edge['knox_untrusted_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','installd')
G.edge['knox_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['installd']['fill'] = 'red'
G.add_edge('knox_untrusted_app','itsonbs')
G.edge['knox_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['itsonbs']['fill'] = 'red'
G.add_edge('knox_untrusted_app','itsonclient_app')
G.edge['knox_untrusted_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['itsonclient_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','installd')
G.edge['knox_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('knox_untrusted_app','installd')
G.edge['knox_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('knox_untrusted_app','itsonbs')
G.edge['knox_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('knox_untrusted_app','itsonbs')
G.edge['knox_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('knox_untrusted_app','itsonclient_app')
G.edge['knox_untrusted_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('knox_untrusted_app','itsonclient_app')
G.edge['knox_untrusted_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('llk_untrusted_app','installd')
G.edge['llk_untrusted_app']['installd']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','itsonbs')
G.edge['llk_untrusted_app']['itsonbs']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','itsonclient_app')
G.edge['llk_untrusted_app']['itsonclient_app']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','installd')
G.edge['llk_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','itsonbs')
G.edge['llk_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','itsonclient_app')
G.edge['llk_untrusted_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','installd')
G.edge['llk_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['installd']['fill'] = 'red'
G.add_edge('llk_untrusted_app','itsonbs')
G.edge['llk_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['itsonbs']['fill'] = 'red'
G.add_edge('llk_untrusted_app','itsonclient_app')
G.edge['llk_untrusted_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['llk_untrusted_app']['itsonclient_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','installd')
G.edge['llk_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('llk_untrusted_app','installd')
G.edge['llk_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('llk_untrusted_app','itsonbs')
G.edge['llk_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('llk_untrusted_app','itsonbs')
G.edge['llk_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('llk_untrusted_app','itsonclient_app')
G.edge['llk_untrusted_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('llk_untrusted_app','itsonclient_app')
G.edge['llk_untrusted_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('radio','installd')
G.edge['radio']['installd']['write-read'] = '[setattr getattr][open open]'
G.add_edge('radio','itsonbs')
G.edge['radio']['itsonbs']['write-read'] = '[open open]'
G.add_edge('radio','itsonclient_app')
G.edge['radio']['itsonclient_app']['write-read'] = '[open open]'
G.add_edge('radio','installd')
G.edge['radio']['installd']['write-read'] = '[setattr getattr][open open][setattr getattr]'
G.add_edge('radio','itsonbs')
G.edge['radio']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','itsonclient_app')
G.edge['radio']['itsonclient_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','installd')
G.edge['radio']['installd']['write-read'] = '[setattr getattr][open open][setattr getattr][write read]'
G.edge['radio']['installd']['fill'] = 'red'
G.add_edge('radio','itsonbs')
G.edge['radio']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['radio']['itsonbs']['fill'] = 'red'
G.add_edge('radio','itsonclient_app')
G.edge['radio']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['radio']['itsonclient_app']['fill'] = 'red'
G.add_edge('radio','installd')
G.edge['radio']['installd']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][add_name search]'
G.add_edge('radio','installd')
G.edge['radio']['installd']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('radio','itsonbs')
G.edge['radio']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('radio','itsonbs')
G.edge['radio']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('radio','itsonclient_app')
G.edge['radio']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('radio','itsonclient_app')
G.edge['radio']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','installd')
G.edge['s_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','itsonbs')
G.edge['s_system_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','itsonclient_app')
G.edge['s_system_app']['itsonclient_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','installd')
G.edge['s_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','itsonbs')
G.edge['s_system_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('s_system_app','itsonclient_app')
G.edge['s_system_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','installd')
G.edge['s_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['installd']['fill'] = 'red'
G.add_edge('s_system_app','itsonbs')
G.edge['s_system_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['s_system_app']['itsonbs']['fill'] = 'red'
G.add_edge('s_system_app','itsonclient_app')
G.edge['s_system_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['itsonclient_app']['fill'] = 'red'
G.add_edge('s_system_app','installd')
G.edge['s_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','installd')
G.edge['s_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','itsonbs')
G.edge['s_system_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','itsonbs')
G.edge['s_system_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','itsonclient_app')
G.edge['s_system_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','itsonclient_app')
G.edge['s_system_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','installd')
G.edge['system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','itsonbs')
G.edge['system_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','itsonclient_app')
G.edge['system_app']['itsonclient_app']['write-read'] = '[open open]'
G.add_edge('system_app','installd')
G.edge['system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_app','itsonbs')
G.edge['system_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_app','itsonclient_app')
G.edge['system_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','installd')
G.edge['system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_app']['installd']['fill'] = 'red'
G.add_edge('system_app','itsonbs')
G.edge['system_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_app']['itsonbs']['fill'] = 'red'
G.add_edge('system_app','itsonclient_app')
G.edge['system_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['itsonclient_app']['fill'] = 'red'
G.add_edge('system_app','installd')
G.edge['system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','installd')
G.edge['system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','itsonbs')
G.edge['system_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','itsonbs')
G.edge['system_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','itsonclient_app')
G.edge['system_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','itsonclient_app')
G.edge['system_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','itsonbs')
G.edge['system_server']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','itsonclient_app')
G.edge['system_server']['itsonclient_app']['write-read'] = '[open open]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','itsonbs')
G.edge['system_server']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','itsonclient_app')
G.edge['system_server']['itsonclient_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['installd']['fill'] = 'red'
G.add_edge('system_server','itsonbs')
G.edge['system_server']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['itsonbs']['fill'] = 'red'
G.add_edge('system_server','itsonclient_app')
G.edge['system_server']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['itsonclient_app']['fill'] = 'red'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','itsonbs')
G.edge['system_server']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','itsonbs')
G.edge['system_server']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','itsonclient_app')
G.edge['system_server']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','itsonclient_app')
G.edge['system_server']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('trustonicpartner_app','installd')
G.edge['trustonicpartner_app']['installd']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','itsonbs')
G.edge['trustonicpartner_app']['itsonbs']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','itsonclient_app')
G.edge['trustonicpartner_app']['itsonclient_app']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','installd')
G.edge['trustonicpartner_app']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','itsonbs')
G.edge['trustonicpartner_app']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','itsonclient_app')
G.edge['trustonicpartner_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','installd')
G.edge['trustonicpartner_app']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['installd']['fill'] = 'red'
G.add_edge('trustonicpartner_app','itsonbs')
G.edge['trustonicpartner_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['itsonbs']['fill'] = 'red'
G.add_edge('trustonicpartner_app','itsonclient_app')
G.edge['trustonicpartner_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['trustonicpartner_app']['itsonclient_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','installd')
G.edge['trustonicpartner_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('trustonicpartner_app','installd')
G.edge['trustonicpartner_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('trustonicpartner_app','itsonbs')
G.edge['trustonicpartner_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('trustonicpartner_app','itsonbs')
G.edge['trustonicpartner_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('trustonicpartner_app','itsonclient_app')
G.edge['trustonicpartner_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('trustonicpartner_app','itsonclient_app')
G.edge['trustonicpartner_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('umcagent_app','installd')
G.edge['umcagent_app']['installd']['write-read'] = '[open open]'
G.add_edge('umcagent_app','itsonbs')
G.edge['umcagent_app']['itsonbs']['write-read'] = '[open open]'
G.add_edge('umcagent_app','itsonclient_app')
G.edge['umcagent_app']['itsonclient_app']['write-read'] = '[open open]'
G.add_edge('umcagent_app','installd')
G.edge['umcagent_app']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','itsonbs')
G.edge['umcagent_app']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','itsonclient_app')
G.edge['umcagent_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','installd')
G.edge['umcagent_app']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['umcagent_app']['installd']['fill'] = 'red'
G.add_edge('umcagent_app','itsonbs')
G.edge['umcagent_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['umcagent_app']['itsonbs']['fill'] = 'red'
G.add_edge('umcagent_app','itsonclient_app')
G.edge['umcagent_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['umcagent_app']['itsonclient_app']['fill'] = 'red'
G.add_edge('umcagent_app','installd')
G.edge['umcagent_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('umcagent_app','installd')
G.edge['umcagent_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('umcagent_app','itsonbs')
G.edge['umcagent_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('umcagent_app','itsonbs')
G.edge['umcagent_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('umcagent_app','itsonclient_app')
G.edge['umcagent_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('umcagent_app','itsonclient_app')
G.edge['umcagent_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('untrusted_app','installd')
G.edge['untrusted_app']['installd']['write-read'] = '[open open]'
G.add_edge('untrusted_app','itsonbs')
G.edge['untrusted_app']['itsonbs']['write-read'] = '[open open]'
G.add_edge('untrusted_app','itsonclient_app')
G.edge['untrusted_app']['itsonclient_app']['write-read'] = '[open open]'
G.add_edge('untrusted_app','installd')
G.edge['untrusted_app']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','itsonbs')
G.edge['untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','itsonclient_app')
G.edge['untrusted_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','installd')
G.edge['untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusted_app']['installd']['fill'] = 'red'
G.add_edge('untrusted_app','itsonbs')
G.edge['untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusted_app']['itsonbs']['fill'] = 'red'
G.add_edge('untrusted_app','itsonclient_app')
G.edge['untrusted_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusted_app']['itsonclient_app']['fill'] = 'red'
G.add_edge('untrusted_app','installd')
G.edge['untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('untrusted_app','installd')
G.edge['untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('untrusted_app','itsonbs')
G.edge['untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('untrusted_app','itsonbs')
G.edge['untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('untrusted_app','itsonclient_app')
G.edge['untrusted_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('untrusted_app','itsonclient_app')
G.edge['untrusted_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vpn_untrusted_app','installd')
G.edge['vpn_untrusted_app']['installd']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','itsonbs')
G.edge['vpn_untrusted_app']['itsonbs']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','itsonclient_app')
G.edge['vpn_untrusted_app']['itsonclient_app']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','installd')
G.edge['vpn_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','itsonbs')
G.edge['vpn_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','itsonclient_app')
G.edge['vpn_untrusted_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','installd')
G.edge['vpn_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['installd']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','itsonbs')
G.edge['vpn_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['itsonbs']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','itsonclient_app')
G.edge['vpn_untrusted_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vpn_untrusted_app']['itsonclient_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','installd')
G.edge['vpn_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vpn_untrusted_app','installd')
G.edge['vpn_untrusted_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vpn_untrusted_app','itsonbs')
G.edge['vpn_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vpn_untrusted_app','itsonbs')
G.edge['vpn_untrusted_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vpn_untrusted_app','itsonclient_app')
G.edge['vpn_untrusted_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vpn_untrusted_app','itsonclient_app')
G.edge['vpn_untrusted_app']['itsonclient_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()