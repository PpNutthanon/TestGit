import graphviz

# Create a Graphviz graph object
graph = graphviz.Digraph(format='png')

# Add nodes to the graph
graph.node('Voice Control', shape='diamond', style='filled', color='yellow')
graph.node('Speech Recognition', shape='ellipse', style='filled', color='lightblue')
graph.node('Signal Processing', shape='ellipse', style='filled', color='lightblue')
graph.node('Microcontrollers', shape='ellipse', style='filled', color='lightblue')
graph.node('Communication Protocols', shape='ellipse', style='filled', color='lightblue')
graph.node('Electrical Engineering', shape='ellipse', style='filled', color='lightblue')
graph.node('Arduino', shape='box', style='filled', color='green')
graph.node('Raspberry Pi', shape='box', style='filled', color='green')
graph.node('Voice Assistants', shape='box', style='filled', color='green')
graph.node('Mobile Devices', shape='box', style='filled', color='green')

# Add edges to the graph
graph.edge('Voice Control', 'Speech Recognition')
graph.edge('Voice Control', 'Signal Processing')
graph.edge('Voice Control', 'Microcontrollers')
graph.edge('Voice Control', 'Communication Protocols')
graph.edge('Voice Control', 'Electrical Engineering')
graph.edge('Microcontrollers', 'Arduino')
graph.edge('Microcontrollers', 'Raspberry Pi')
graph.edge('Voice Assistants', 'Amazon Echo')
graph.edge('Voice Assistants', 'Google Home')
graph.edge('Mobile Devices', 'Android')
graph.edge('Mobile Devices', 'iOS')

# Render the graph to a file
graph.render('mindmap', view=True)