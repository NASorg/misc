# Instagram the Intifada - Mapping the Social Network of Students for Justice in Palestine
# By Mason Goad, Research Fellow
# The National Association of Scholars

# Import Required Libraries
import pandas as pd
import networkx
import matplotlib.pyplot as plt
import numpy as np

from bokeh.io import output_notebook, show, save

# Upload Data as Pandas Data Frame
iti_df = pd.read_csv("/home/masong/Desktop/all_targets.csv")

# Create Edge List:
G = networkx.from_pandas_edgelist(iti_df, 'followed_by', 'user_name')

# Create Bokeh Visual:
from bokeh.io import output_notebook, show, save
from bokeh.models import Range1d, Circle, ColumnDataSource, MultiLine, EdgesAndLinkedNodes, NodesAndLinkedEdges, LabelSet
from bokeh.plotting import figure
from bokeh.plotting import from_networkx
from bokeh.palettes import Blues8, Reds8, Purples8, Oranges8, Viridis8, Spectral8
from bokeh.transform import linear_cmap
from networkx.algorithms import community

# Set Title:
title = 'Instagram the Intifada: Mapping the Social Network of Students for Justice in Palestine'


# Establish Hover Categories
#HOVER_TOOLTIPS = [("User Name", "@user_name"), ("Given Name", "@given_name")]

# Create Plot:
plot = figure(#tooltips=HOVER_TOOLTIPS,                                         # Uncomment Hovertools if desired.
              #tools="pan,wheel_zoom,save,reset", active_scroll='wheel_zoom',
              x_range=Range1d(-5.1, 5.1), y_range=Range1d(-5.1, 5.1), title=title)


#Create Network Graph Object - Spring_Layout
# https://networkx.github.io/documentation/networkx-1.9/reference/generated/networkx.drawing.layout.spring_layout.html
network_graph = from_networkx(G, networkx.spring_layout, scale=10, center=(0, 0))

#Set Node Size:
network_graph.node_renderer.glyph = Circle(radius=0.001, fill_color='black')

#Set Edge Width, Opacity, Etc.:
network_graph.edge_renderer.glyph = MultiLine(line_alpha=0.5, line_width=0.07)

#Add Network Graph to Plot:
plot.renderers.append(network_graph)

#Add Labels:
x, y = zip(*network_graph.layout_provider.graph_layout.values())
node_labels = list(G.nodes())
source = ColumnDataSource({'x': x, 'y': y, 'user_name': [node_labels[i] for i in range(len(x))]})
labels = LabelSet(x='x', y='y', text='user_name', source=source, background_fill_color='white', text_font_size='8px', background_fill_alpha=.7)
plot.renderers.append(labels)


#print(iti_df.columns)
#show(plot)             # Uncomment this line if desired.
save(plot, filename=f"Instagram_the_Intifada.html")





