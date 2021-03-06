# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:

"""This package has the visualization nodes that can be placed on the Node Editor.

It includes several visualization techniques to understand
"""

from dial_core.node_editor import NodeRegistrySingleton
from dial_core.notebook import NodeCellsRegistrySingleton

from .conv_visualization import(
    ConvVisualizationNode,
    ConvVisualizationNodeCells,
    ConvVisualizationNodeFactory
)

from .preprocessor_loader import(
    PreProcessorLoaderNode,
    PreProcessorLoaderNodeFactory
)


def load_plugin():
    node_registry = NodeRegistrySingleton()

    # Register Node
    node_registry.register_node(
        "Visualization/Convolutional Visualization", ConvVisualizationNodeFactory
     )

    node_registry.register_node(
        "Visualization/Image Preprocessor Loader", PreProcessorLoaderNodeFactory
     )

    # Register Notebook Transformers
    node_cells_registry = NodeCellsRegistrySingleton()
    node_cells_registry.register_transformer(
        ConvVisualizationNode, ConvVisualizationNodeCells
    )


def unload_plugin():
    node_registry = NodeRegistrySingleton()

    # Unregister Nodes
    node_registry.unregister_node("Visualization/Convolutional Visualization")
    node_registry.unregister_node("Visualization/Image Preprocessor Loader")

    # Unregister Notebook Transformers
    node_registry.unregister_node(ConvVisualizationNodeCells)


#load_plugin()

__all__ = [
    "load_plugin",
    "unload_plugin",
]
