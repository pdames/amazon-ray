import ray


def set_resource(resource_name, capacity, node_id=None):
    """ Set a resource to a specified capacity.

    This creates, updates or deletes a custom resource for a target NodeID.
    If the resource already exists, it's capacity is updated to the new value.
    If the capacity is set to 0, the resource is deleted.
    If NodeID is not specified or set to None,
    the resource is created on the local node where the actor is running.

    Args:
        resource_name (str): Name of the resource to be created
        capacity (int): Capacity of the new resource. Resource is deleted if
            capacity is 0.
        node_id (str): The NodeID of the node where the resource is to be
            set.

    Returns:
        None

    Raises:
          ValueError: This exception is raised when a negative or non-integer
          capacity is specified.
    """
    if node_id is not None:
        node_id_obj = ray.NodeID(ray.utils.hex_to_binary(node_id))
    else:
        node_id_obj = ray.NodeID.nil()
    if (capacity < 0) or (capacity != int(capacity)):
        raise ValueError(
            "Capacity {} must be a non-negative integer.".format(capacity))
    return ray.worker.global_worker.core_worker.set_resource(
        resource_name, capacity, node_id_obj)
