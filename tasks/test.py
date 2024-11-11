class SignalInformation:
    def __init__(self, signal_power: float, path: list):
        # Validate input types
        if not isinstance(signal_power, float):
            raise TypeError("Signal power must be a float.")
        if not isinstance(path, list) or not all(isinstance(node, str) for node in path):
            raise TypeError("Path must be a list of strings.")

        # Set attributes
        self.signal_power = signal_power
        self.noise_power = 0.0  # Initialized to zero
        self.latency = 0.0  # Initialized to zero
        self.path = path

    def update_signal_power(self, increment: float):
        """Update signal power by a given increment."""
        if not isinstance(increment, float):
            raise TypeError("Increment must be a float.")
        self.signal_power += increment

    def update_noise_power(self, increment: float):
        """Update noise power by a given increment."""
        if not isinstance(increment, float):
            raise TypeError("Increment must be a float.")
        self.noise_power += increment

    def update_latency(self, increment: float):
        """Update latency by a given increment."""
        if not isinstance(increment, float):
            raise TypeError("Increment must be a float.")
        self.latency += increment

    def update_path(self, node: str):
        """Update the path when crossing a node."""
        if not isinstance(node, str):
            raise TypeError("Node must be a string.")
        self.path.append(node)

    def __str__(self):
        return f"Signal Power: {self.signal_power}, Noise Power: {self.noise_power}, Latency: {self.latency}, Path: {self.path}"


class Node:
    def __init__(self, node_info: dict):
        # Validate input type
        if not isinstance(node_info, dict):
            raise TypeError("Node information must be a dictionary.")

        # Set attributes
        self.label = node_info.get('label', '')
        self.position = node_info.get('position', (0.0, 0.0))
        self.connected_nodes = node_info.get('connected_nodes', [])
        self.successive = {}

    def propagate(self, signal_info: SignalInformation):
        """Update a SignalInformation object's path attribute and call successive element's propagate method."""
        if not isinstance(signal_info, SignalInformation):
            raise TypeError("Signal information must be a SignalInformation object.")

        # Update SignalInformation's path attribute
        signal_info.update_path(self.label)

        # Propagate to connected nodes
        for connected_node_label in self.connected_nodes:
            connected_node = self.successive.get(connected_node_label)
            if connected_node:
                connected_node.propagate(signal_info)

    def __str__(self):
        return f"Node Label: {self.label}, Position: {self.position}, Connected Nodes: {self.connected_nodes}"


# Example Usage:
try:
    # Creating instances of SignalInformation and Node
    signal_info = SignalInformation(signal_power=10.5, path=['A', 'B', 'C'])
    node_info = {'label': 'A', 'position': (0.0, 0.0), 'connected_nodes': ['B']}
    node_A = Node(node_info)

    # Propagate signal through the network
    node_A.propagate(signal_info)

    # Display updated SignalInformation and Node information
    print(signal_info)
    print(node_A)
except TypeError as e:
    print(e)
