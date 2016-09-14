import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('secstarter','secstarter')
G.edge['secstarter']['secstarter']['write-read'] = '[open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read]'
G.edge['secstarter']['secstarter']['fill'] = 'red'
app = Viewer(G)
app.mainloop()