import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('ftm_ptt','ftm_ptt')
G.edge['ftm_ptt']['ftm_ptt']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['ftm_ptt']['ftm_ptt']['fill'] = 'red'
app = Viewer(G)
app.mainloop()