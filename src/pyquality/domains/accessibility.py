class AccessibilityDomain:
    def __init__(self, driver):
        self.driver = driver

    def disable(self):
        """
        Disables the accessibility domain.
        """
        params = {}
        return self.driver.execute_and_wait("Accessibility.disable", params)

    def enable(self):
        """
        Enables the accessibility domain which causes `AXNodeId`s to remain consistent between method calls. This turns on accessibility for the page, which can impact performance until accessibility is disabled.
        """
        params = {}
        return self.driver.execute_and_wait("Accessibility.enable", params)

    def getPartialAXTree(self, nodeId=None, backendNodeId=None, objectId=None, fetchRelatives=None):
        """
        Fetches the accessibility node and partial accessibility tree for this DOM node, if it exists.
        - nodeId (any): Identifier of the node to get the partial accessibility tree for.
        - backendNodeId (any): Identifier of the backend node to get the partial accessibility tree for.
        - objectId (any): JavaScript object id of the node wrapper to get the partial accessibility tree for.
        - fetchRelatives (boolean): Whether to fetch this node's ancestors, siblings and children. Defaults to true.
        """
        params = {}
        if nodeId is not None:
            params["nodeId"] = nodeId
        if backendNodeId is not None:
            params["backendNodeId"] = backendNodeId
        if objectId is not None:
            params["objectId"] = objectId
        if fetchRelatives is not None:
            params["fetchRelatives"] = fetchRelatives
        return self.driver.execute_and_wait("Accessibility.getPartialAXTree", params)

    def getFullAXTree(self, depth=None, frameId=None):
        """
        Fetches the entire accessibility tree for the root Document
        - depth (integer): The maximum depth at which descendants of the root node should be retrieved.
If omitted, the full tree is returned.
        - frameId (any): The frame for whose document the AX tree should be retrieved.
If omitted, the root frame is used.
        """
        params = {}
        if depth is not None:
            params["depth"] = depth
        if frameId is not None:
            params["frameId"] = frameId
        return self.driver.execute_and_wait("Accessibility.getFullAXTree", params)

    def getRootAXNode(self, frameId=None):
        """
        Fetches the root node. Requires `enable()` to have been called previously.
        - frameId (any): The frame in whose document the node resides.
If omitted, the root frame is used.
        """
        params = {}
        if frameId is not None:
            params["frameId"] = frameId
        return self.driver.execute_and_wait("Accessibility.getRootAXNode", params)

    def getAXNodeAndAncestors(self, nodeId=None, backendNodeId=None, objectId=None):
        """
        Fetches a node and all ancestors up to and including the root. Requires `enable()` to have been called previously.
        - nodeId (any): Identifier of the node to get.
        - backendNodeId (any): Identifier of the backend node to get.
        - objectId (any): JavaScript object id of the node wrapper to get.
        """
        params = {}
        if nodeId is not None:
            params["nodeId"] = nodeId
        if backendNodeId is not None:
            params["backendNodeId"] = backendNodeId
        if objectId is not None:
            params["objectId"] = objectId
        return self.driver.execute_and_wait("Accessibility.getAXNodeAndAncestors", params)

    def getChildAXNodes(self, id_, frameId=None):
        """
        Fetches a particular accessibility node by AXNodeId. Requires `enable()` to have been called previously.
        - id (any): 
        - frameId (any): The frame in whose document the node resides.
If omitted, the root frame is used.
        """
        params = {}
        params["id"] = id_
        if frameId is not None:
            params["frameId"] = frameId
        return self.driver.execute_and_wait("Accessibility.getChildAXNodes", params)

    def queryAXTree(self, nodeId=None, backendNodeId=None, objectId=None, accessibleName=None, role=None):
        """
        Query a DOM node's accessibility subtree for accessible name and role. This command computes the name and role for all nodes in the subtree, including those that are ignored for accessibility, and returns those that match the specified name and role. If no DOM node is specified, or the DOM node does not exist, the command returns an error. If neither `accessibleName` or `role` is specified, it returns all the accessibility nodes in the subtree.
        - nodeId (any): Identifier of the node for the root to query.
        - backendNodeId (any): Identifier of the backend node for the root to query.
        - objectId (any): JavaScript object id of the node wrapper for the root to query.
        - accessibleName (string): Find nodes with this computed name.
        - role (string): Find nodes with this computed role.
        """
        params = {}
        if nodeId is not None:
            params["nodeId"] = nodeId
        if backendNodeId is not None:
            params["backendNodeId"] = backendNodeId
        if objectId is not None:
            params["objectId"] = objectId
        if accessibleName is not None:
            params["accessibleName"] = accessibleName
        if role is not None:
            params["role"] = role
        return self.driver.execute_and_wait("Accessibility.queryAXTree", params)

