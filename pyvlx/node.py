"""
Module for basic object for nodes.

Node object is an interface class and should
be derived by other objects like window openers
and roller shutters.
"""
from .set_node_name import SetNodeName
from .exception import PyVLXException


class Node:
    """Class for node abstraction."""

    def __init__(self, pyvlx, node_id, name):
        """Initialize Node object."""
        self.pyvlx = pyvlx
        self.node_id = node_id
        self.name = name

    async def rename(self, name):
        """Change name of node."""
        set_node_name = SetNodeName(pyvlx=self.pyvlx, node_id=self.node_id, name=name)
        await set_node_name.do_api_call()
        if not set_node_name.success:
            raise PyVLXException("Unable to rename node")
        self.name = name

    def __str__(self):
        """Return object as readable string."""
        return '<{} name="{}" ' \
            'node_id="{}"/>' \
            .format(
                type(self).__name__,
                self.name,
                self.node_id)

    def __eq__(self, other):
        """Equal operator."""
        return type(self).__name__ == type(other).__name__ and \
            self.__dict__ == other.__dict__
