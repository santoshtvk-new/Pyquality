class DOMDomain:
    def __init__(self, driver):
        self.driver = driver

    def collectClassNamesFromSubtree(self, nodeId):
        """
        Collects class names for the node with given id and all of it's child nodes.
        - nodeId (any): Id of the node to collect class names.
        """
        params = {}
        params["nodeId"] = nodeId
        return self.driver.execute_and_wait("DOM.collectClassNamesFromSubtree", params)

    def copyTo(self, nodeId, targetNodeId, insertBeforeNodeId=None):
        """
        Creates a deep copy of the specified node and places it into the target container before the given anchor.
        - nodeId (any): Id of the node to copy.
        - targetNodeId (any): Id of the element to drop the copy into.
        - insertBeforeNodeId (any): Drop the copy before this node (if absent, the copy becomes the last child of
`targetNodeId`).
        """
        params = {}
        params["nodeId"] = nodeId
        params["targetNodeId"] = targetNodeId
        if insertBeforeNodeId is not None:
            params["insertBeforeNodeId"] = insertBeforeNodeId
        return self.driver.execute_and_wait("DOM.copyTo", params)

    def describeNode(self, nodeId=None, backendNodeId=None, objectId=None, depth=None, pierce=None):
        """
        Describes node given its id, does not require domain to be enabled. Does not start tracking any objects, can be used for automation.
        - nodeId (any): Identifier of the node.
        - backendNodeId (any): Identifier of the backend node.
        - objectId (any): JavaScript object id of the node wrapper.
        - depth (integer): The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the
entire subtree or provide an integer larger than 0.
        - pierce (boolean): Whether or not iframes and shadow roots should be traversed when returning the subtree
(default is false).
        """
        params = {}
        if nodeId is not None:
            params["nodeId"] = nodeId
        if backendNodeId is not None:
            params["backendNodeId"] = backendNodeId
        if objectId is not None:
            params["objectId"] = objectId
        if depth is not None:
            params["depth"] = depth
        if pierce is not None:
            params["pierce"] = pierce
        return self.driver.execute_and_wait("DOM.describeNode", params)

    def scrollIntoViewIfNeeded(self, nodeId=None, backendNodeId=None, objectId=None, rect=None):
        """
        Scrolls the specified rect of the given node into view if not already visible. Note: exactly one between nodeId, backendNodeId and objectId should be passed to identify the node.
        - nodeId (any): Identifier of the node.
        - backendNodeId (any): Identifier of the backend node.
        - objectId (any): JavaScript object id of the node wrapper.
        - rect (any): The rect to be scrolled into view, relative to the node's border box, in CSS pixels.
When omitted, center of the node will be used, similar to Element.scrollIntoView.
        """
        params = {}
        if nodeId is not None:
            params["nodeId"] = nodeId
        if backendNodeId is not None:
            params["backendNodeId"] = backendNodeId
        if objectId is not None:
            params["objectId"] = objectId
        if rect is not None:
            params["rect"] = rect
        return self.driver.execute_and_wait("DOM.scrollIntoViewIfNeeded", params)

    def disable(self):
        """
        Disables DOM agent for the given page.
        """
        params = {}
        return self.driver.execute_and_wait("DOM.disable", params)

    def discardSearchResults(self, searchId):
        """
        Discards search results from the session with the given id. `getSearchResults` should no longer be called for that search.
        - searchId (string): Unique search session identifier.
        """
        params = {}
        params["searchId"] = searchId
        return self.driver.execute_and_wait("DOM.discardSearchResults", params)

    def enable(self, includeWhitespace=None):
        """
        Enables DOM agent for the given page.
        - includeWhitespace (string): Whether to include whitespaces in the children array of returned Nodes.
        """
        params = {}
        if includeWhitespace is not None:
            params["includeWhitespace"] = includeWhitespace
        return self.driver.execute_and_wait("DOM.enable", params)

    def focus(self, nodeId=None, backendNodeId=None, objectId=None):
        """
        Focuses the given element.
        - nodeId (any): Identifier of the node.
        - backendNodeId (any): Identifier of the backend node.
        - objectId (any): JavaScript object id of the node wrapper.
        """
        params = {}
        if nodeId is not None:
            params["nodeId"] = nodeId
        if backendNodeId is not None:
            params["backendNodeId"] = backendNodeId
        if objectId is not None:
            params["objectId"] = objectId
        return self.driver.execute_and_wait("DOM.focus", params)

    def getAttributes(self, nodeId):
        """
        Returns attributes for the specified node.
        - nodeId (any): Id of the node to retrieve attributes for.
        """
        params = {}
        params["nodeId"] = nodeId
        return self.driver.execute_and_wait("DOM.getAttributes", params)

    def getBoxModel(self, nodeId=None, backendNodeId=None, objectId=None):
        """
        Returns boxes for the given node.
        - nodeId (any): Identifier of the node.
        - backendNodeId (any): Identifier of the backend node.
        - objectId (any): JavaScript object id of the node wrapper.
        """
        params = {}
        if nodeId is not None:
            params["nodeId"] = nodeId
        if backendNodeId is not None:
            params["backendNodeId"] = backendNodeId
        if objectId is not None:
            params["objectId"] = objectId
        return self.driver.execute_and_wait("DOM.getBoxModel", params)

    def getContentQuads(self, nodeId=None, backendNodeId=None, objectId=None):
        """
        Returns quads that describe node position on the page. This method might return multiple quads for inline nodes.
        - nodeId (any): Identifier of the node.
        - backendNodeId (any): Identifier of the backend node.
        - objectId (any): JavaScript object id of the node wrapper.
        """
        params = {}
        if nodeId is not None:
            params["nodeId"] = nodeId
        if backendNodeId is not None:
            params["backendNodeId"] = backendNodeId
        if objectId is not None:
            params["objectId"] = objectId
        return self.driver.execute_and_wait("DOM.getContentQuads", params)

    def getDocument(self, depth=None, pierce=None):
        """
        Returns the root DOM node (and optionally the subtree) to the caller. Implicitly enables the DOM domain events for the current target.
        - depth (integer): The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the
entire subtree or provide an integer larger than 0.
        - pierce (boolean): Whether or not iframes and shadow roots should be traversed when returning the subtree
(default is false).
        """
        params = {}
        if depth is not None:
            params["depth"] = depth
        if pierce is not None:
            params["pierce"] = pierce
        return self.driver.execute_and_wait("DOM.getDocument", params)

    def getFlattenedDocument(self, depth=None, pierce=None):
        """
        Returns the root DOM node (and optionally the subtree) to the caller. Deprecated, as it is not designed to work well with the rest of the DOM agent. Use DOMSnapshot.captureSnapshot instead.
        - depth (integer): The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the
entire subtree or provide an integer larger than 0.
        - pierce (boolean): Whether or not iframes and shadow roots should be traversed when returning the subtree
(default is false).
        """
        params = {}
        if depth is not None:
            params["depth"] = depth
        if pierce is not None:
            params["pierce"] = pierce
        return self.driver.execute_and_wait("DOM.getFlattenedDocument", params)

    def getNodesForSubtreeByStyle(self, nodeId, computedStyles, pierce=None):
        """
        Finds nodes with a given computed style in a subtree.
        - nodeId (any): Node ID pointing to the root of a subtree.
        - computedStyles (array): The style to filter nodes by (includes nodes if any of properties matches).
        - pierce (boolean): Whether or not iframes and shadow roots in the same target should be traversed when returning the
results (default is false).
        """
        params = {}
        params["nodeId"] = nodeId
        params["computedStyles"] = computedStyles
        if pierce is not None:
            params["pierce"] = pierce
        return self.driver.execute_and_wait("DOM.getNodesForSubtreeByStyle", params)

    def getNodeForLocation(self, x, y, includeUserAgentShadowDOM=None, ignorePointerEventsNone=None):
        """
        Returns node id at given location. Depending on whether DOM domain is enabled, nodeId is either returned or not.
        - x (integer): X coordinate.
        - y (integer): Y coordinate.
        - includeUserAgentShadowDOM (boolean): False to skip to the nearest non-UA shadow root ancestor (default: false).
        - ignorePointerEventsNone (boolean): Whether to ignore pointer-events: none on elements and hit test them.
        """
        params = {}
        params["x"] = x
        params["y"] = y
        if includeUserAgentShadowDOM is not None:
            params["includeUserAgentShadowDOM"] = includeUserAgentShadowDOM
        if ignorePointerEventsNone is not None:
            params["ignorePointerEventsNone"] = ignorePointerEventsNone
        return self.driver.execute_and_wait("DOM.getNodeForLocation", params)

    def getOuterHTML(self, nodeId=None, backendNodeId=None, objectId=None, includeShadowDOM=None):
        """
        Returns node's HTML markup.
        - nodeId (any): Identifier of the node.
        - backendNodeId (any): Identifier of the backend node.
        - objectId (any): JavaScript object id of the node wrapper.
        - includeShadowDOM (boolean): Include all shadow roots. Equals to false if not specified.
        """
        params = {}
        if nodeId is not None:
            params["nodeId"] = nodeId
        if backendNodeId is not None:
            params["backendNodeId"] = backendNodeId
        if objectId is not None:
            params["objectId"] = objectId
        if includeShadowDOM is not None:
            params["includeShadowDOM"] = includeShadowDOM
        return self.driver.execute_and_wait("DOM.getOuterHTML", params)

    def getRelayoutBoundary(self, nodeId):
        """
        Returns the id of the nearest ancestor that is a relayout boundary.
        - nodeId (any): Id of the node.
        """
        params = {}
        params["nodeId"] = nodeId
        return self.driver.execute_and_wait("DOM.getRelayoutBoundary", params)

    def getSearchResults(self, searchId, fromIndex, toIndex):
        """
        Returns search results from given `fromIndex` to given `toIndex` from the search with the given identifier.
        - searchId (string): Unique search session identifier.
        - fromIndex (integer): Start index of the search result to be returned.
        - toIndex (integer): End index of the search result to be returned.
        """
        params = {}
        params["searchId"] = searchId
        params["fromIndex"] = fromIndex
        params["toIndex"] = toIndex
        return self.driver.execute_and_wait("DOM.getSearchResults", params)

    def hideHighlight(self):
        """
        Hides any highlight.
        """
        params = {}
        return self.driver.execute_and_wait("DOM.hideHighlight", params)

    def highlightNode(self):
        """
        Highlights DOM node.
        """
        params = {}
        return self.driver.execute_and_wait("DOM.highlightNode", params)

    def highlightRect(self):
        """
        Highlights given rectangle.
        """
        params = {}
        return self.driver.execute_and_wait("DOM.highlightRect", params)

    def markUndoableState(self):
        """
        Marks last undoable state.
        """
        params = {}
        return self.driver.execute_and_wait("DOM.markUndoableState", params)

    def moveTo(self, nodeId, targetNodeId, insertBeforeNodeId=None):
        """
        Moves node into the new container, places it before the given anchor.
        - nodeId (any): Id of the node to move.
        - targetNodeId (any): Id of the element to drop the moved node into.
        - insertBeforeNodeId (any): Drop node before this one (if absent, the moved node becomes the last child of
`targetNodeId`).
        """
        params = {}
        params["nodeId"] = nodeId
        params["targetNodeId"] = targetNodeId
        if insertBeforeNodeId is not None:
            params["insertBeforeNodeId"] = insertBeforeNodeId
        return self.driver.execute_and_wait("DOM.moveTo", params)

    def performSearch(self, query, includeUserAgentShadowDOM=None):
        """
        Searches for a given string in the DOM tree. Use `getSearchResults` to access search results or `cancelSearch` to end this search session.
        - query (string): Plain text or query selector or XPath search query.
        - includeUserAgentShadowDOM (boolean): True to search in user agent shadow DOM.
        """
        params = {}
        params["query"] = query
        if includeUserAgentShadowDOM is not None:
            params["includeUserAgentShadowDOM"] = includeUserAgentShadowDOM
        return self.driver.execute_and_wait("DOM.performSearch", params)

    def pushNodeByPathToFrontend(self, path):
        """
        Requests that the node is sent to the caller given its path. // FIXME, use XPath
        - path (string): Path to node in the proprietary format.
        """
        params = {}
        params["path"] = path
        return self.driver.execute_and_wait("DOM.pushNodeByPathToFrontend", params)

    def pushNodesByBackendIdsToFrontend(self, backendNodeIds):
        """
        Requests that a batch of nodes is sent to the caller given their backend node ids.
        - backendNodeIds (array): The array of backend node ids.
        """
        params = {}
        params["backendNodeIds"] = backendNodeIds
        return self.driver.execute_and_wait("DOM.pushNodesByBackendIdsToFrontend", params)

    def querySelector(self, nodeId, selector):
        """
        Executes `querySelector` on a given node.
        - nodeId (any): Id of the node to query upon.
        - selector (string): Selector string.
        """
        params = {}
        params["nodeId"] = nodeId
        params["selector"] = selector
        return self.driver.execute_and_wait("DOM.querySelector", params)

    def querySelectorAll(self, nodeId, selector):
        """
        Executes `querySelectorAll` on a given node.
        - nodeId (any): Id of the node to query upon.
        - selector (string): Selector string.
        """
        params = {}
        params["nodeId"] = nodeId
        params["selector"] = selector
        return self.driver.execute_and_wait("DOM.querySelectorAll", params)

    def getTopLayerElements(self):
        """
        Returns NodeIds of current top layer elements. Top layer is rendered closest to the user within a viewport, therefore its elements always appear on top of all other content.
        """
        params = {}
        return self.driver.execute_and_wait("DOM.getTopLayerElements", params)

    def getElementByRelation(self, nodeId, relation):
        """
        Returns the NodeId of the matched element according to certain relations.
        - nodeId (any): Id of the node from which to query the relation.
        - relation (string): Type of relation to get.
        """
        params = {}
        params["nodeId"] = nodeId
        params["relation"] = relation
        return self.driver.execute_and_wait("DOM.getElementByRelation", params)

    def redo(self):
        """
        Re-does the last undone action.
        """
        params = {}
        return self.driver.execute_and_wait("DOM.redo", params)

    def removeAttribute(self, nodeId, name):
        """
        Removes attribute with given name from an element with given id.
        - nodeId (any): Id of the element to remove attribute from.
        - name (string): Name of the attribute to remove.
        """
        params = {}
        params["nodeId"] = nodeId
        params["name"] = name
        return self.driver.execute_and_wait("DOM.removeAttribute", params)

    def removeNode(self, nodeId):
        """
        Removes node with given id.
        - nodeId (any): Id of the node to remove.
        """
        params = {}
        params["nodeId"] = nodeId
        return self.driver.execute_and_wait("DOM.removeNode", params)

    def requestChildNodes(self, nodeId, depth=None, pierce=None):
        """
        Requests that children of the node with given id are returned to the caller in form of `setChildNodes` events where not only immediate children are retrieved, but all children down to the specified depth.
        - nodeId (any): Id of the node to get children for.
        - depth (integer): The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the
entire subtree or provide an integer larger than 0.
        - pierce (boolean): Whether or not iframes and shadow roots should be traversed when returning the sub-tree
(default is false).
        """
        params = {}
        params["nodeId"] = nodeId
        if depth is not None:
            params["depth"] = depth
        if pierce is not None:
            params["pierce"] = pierce
        return self.driver.execute_and_wait("DOM.requestChildNodes", params)

    def requestNode(self, objectId):
        """
        Requests that the node is sent to the caller given the JavaScript node object reference. All nodes that form the path from the node to the root are also sent to the client as a series of `setChildNodes` notifications.
        - objectId (any): JavaScript object id to convert into node.
        """
        params = {}
        params["objectId"] = objectId
        return self.driver.execute_and_wait("DOM.requestNode", params)

    def resolveNode(self, nodeId=None, backendNodeId=None, objectGroup=None, executionContextId=None):
        """
        Resolves the JavaScript node object for a given NodeId or BackendNodeId.
        - nodeId (any): Id of the node to resolve.
        - backendNodeId (any): Backend identifier of the node to resolve.
        - objectGroup (string): Symbolic group name that can be used to release multiple objects.
        - executionContextId (any): Execution context in which to resolve the node.
        """
        params = {}
        if nodeId is not None:
            params["nodeId"] = nodeId
        if backendNodeId is not None:
            params["backendNodeId"] = backendNodeId
        if objectGroup is not None:
            params["objectGroup"] = objectGroup
        if executionContextId is not None:
            params["executionContextId"] = executionContextId
        return self.driver.execute_and_wait("DOM.resolveNode", params)

    def setAttributeValue(self, nodeId, name, value):
        """
        Sets attribute for an element with given id.
        - nodeId (any): Id of the element to set attribute for.
        - name (string): Attribute name.
        - value (string): Attribute value.
        """
        params = {}
        params["nodeId"] = nodeId
        params["name"] = name
        params["value"] = value
        return self.driver.execute_and_wait("DOM.setAttributeValue", params)

    def setAttributesAsText(self, nodeId, text, name=None):
        """
        Sets attributes on element with given id. This method is useful when user edits some existing attribute value and types in several attribute name/value pairs.
        - nodeId (any): Id of the element to set attributes for.
        - text (string): Text with a number of attributes. Will parse this text using HTML parser.
        - name (string): Attribute name to replace with new attributes derived from text in case text parsed
successfully.
        """
        params = {}
        params["nodeId"] = nodeId
        params["text"] = text
        if name is not None:
            params["name"] = name
        return self.driver.execute_and_wait("DOM.setAttributesAsText", params)

    def setFileInputFiles(self, files, nodeId=None, backendNodeId=None, objectId=None):
        """
        Sets files for the given file input element.
        - files (array): Array of file paths to set.
        - nodeId (any): Identifier of the node.
        - backendNodeId (any): Identifier of the backend node.
        - objectId (any): JavaScript object id of the node wrapper.
        """
        params = {}
        params["files"] = files
        if nodeId is not None:
            params["nodeId"] = nodeId
        if backendNodeId is not None:
            params["backendNodeId"] = backendNodeId
        if objectId is not None:
            params["objectId"] = objectId
        return self.driver.execute_and_wait("DOM.setFileInputFiles", params)

    def setNodeStackTracesEnabled(self, enable):
        """
        Sets if stack traces should be captured for Nodes. See `Node.getNodeStackTraces`. Default is disabled.
        - enable (boolean): Enable or disable.
        """
        params = {}
        params["enable"] = enable
        return self.driver.execute_and_wait("DOM.setNodeStackTracesEnabled", params)

    def getNodeStackTraces(self, nodeId):
        """
        Gets stack traces associated with a Node. As of now, only provides stack trace for Node creation.
        - nodeId (any): Id of the node to get stack traces for.
        """
        params = {}
        params["nodeId"] = nodeId
        return self.driver.execute_and_wait("DOM.getNodeStackTraces", params)

    def getFileInfo(self, objectId):
        """
        Returns file information for the given File wrapper.
        - objectId (any): JavaScript object id of the node wrapper.
        """
        params = {}
        params["objectId"] = objectId
        return self.driver.execute_and_wait("DOM.getFileInfo", params)

    def getDetachedDomNodes(self):
        """
        Returns list of detached nodes
        """
        params = {}
        return self.driver.execute_and_wait("DOM.getDetachedDomNodes", params)

    def setInspectedNode(self, nodeId):
        """
        Enables console to refer to the node with given id via $x (see Command Line API for more details $x functions).
        - nodeId (any): DOM node id to be accessible by means of $x command line API.
        """
        params = {}
        params["nodeId"] = nodeId
        return self.driver.execute_and_wait("DOM.setInspectedNode", params)

    def setNodeName(self, nodeId, name):
        """
        Sets node name for a node with given id.
        - nodeId (any): Id of the node to set name for.
        - name (string): New node's name.
        """
        params = {}
        params["nodeId"] = nodeId
        params["name"] = name
        return self.driver.execute_and_wait("DOM.setNodeName", params)

    def setNodeValue(self, nodeId, value):
        """
        Sets node value for a node with given id.
        - nodeId (any): Id of the node to set value for.
        - value (string): New node's value.
        """
        params = {}
        params["nodeId"] = nodeId
        params["value"] = value
        return self.driver.execute_and_wait("DOM.setNodeValue", params)

    def setOuterHTML(self, nodeId, outerHTML):
        """
        Sets node HTML markup, returns new node id.
        - nodeId (any): Id of the node to set markup for.
        - outerHTML (string): Outer HTML markup to set.
        """
        params = {}
        params["nodeId"] = nodeId
        params["outerHTML"] = outerHTML
        return self.driver.execute_and_wait("DOM.setOuterHTML", params)

    def undo(self):
        """
        Undoes the last performed action.
        """
        params = {}
        return self.driver.execute_and_wait("DOM.undo", params)

    def getFrameOwner(self, frameId):
        """
        Returns iframe node that owns iframe with the given domain.
        - frameId (any): 
        """
        params = {}
        params["frameId"] = frameId
        return self.driver.execute_and_wait("DOM.getFrameOwner", params)

    def getContainerForNode(self, nodeId, containerName=None, physicalAxes=None, logicalAxes=None, queriesScrollState=None, queriesAnchored=None):
        """
        Returns the query container of the given node based on container query conditions: containerName, physical and logical axes, and whether it queries scroll-state or anchored elements. If no axes are provided and queriesScrollState is false, the style container is returned, which is the direct parent or the closest element with a matching container-name.
        - nodeId (any): 
        - containerName (string): 
        - physicalAxes (any): 
        - logicalAxes (any): 
        - queriesScrollState (boolean): 
        - queriesAnchored (boolean): 
        """
        params = {}
        params["nodeId"] = nodeId
        if containerName is not None:
            params["containerName"] = containerName
        if physicalAxes is not None:
            params["physicalAxes"] = physicalAxes
        if logicalAxes is not None:
            params["logicalAxes"] = logicalAxes
        if queriesScrollState is not None:
            params["queriesScrollState"] = queriesScrollState
        if queriesAnchored is not None:
            params["queriesAnchored"] = queriesAnchored
        return self.driver.execute_and_wait("DOM.getContainerForNode", params)

    def getQueryingDescendantsForContainer(self, nodeId):
        """
        Returns the descendants of a container query container that have container queries against this container.
        - nodeId (any): Id of the container node to find querying descendants from.
        """
        params = {}
        params["nodeId"] = nodeId
        return self.driver.execute_and_wait("DOM.getQueryingDescendantsForContainer", params)

    def getAnchorElement(self, nodeId, anchorSpecifier=None):
        """
        Returns the target anchor element of the given anchor query according to https://www.w3.org/TR/css-anchor-position-1/#target.
        - nodeId (any): Id of the positioned element from which to find the anchor.
        - anchorSpecifier (string): An optional anchor specifier, as defined in
https://www.w3.org/TR/css-anchor-position-1/#anchor-specifier.
If not provided, it will return the implicit anchor element for
the given positioned element.
        """
        params = {}
        params["nodeId"] = nodeId
        if anchorSpecifier is not None:
            params["anchorSpecifier"] = anchorSpecifier
        return self.driver.execute_and_wait("DOM.getAnchorElement", params)

    def forceShowPopover(self, nodeId, enable):
        """
        When enabling, this API force-opens the popover identified by nodeId and keeps it open until disabled.
        - nodeId (any): Id of the popover HTMLElement
        - enable (boolean): If true, opens the popover and keeps it open. If false, closes the
popover if it was previously force-opened.
        """
        params = {}
        params["nodeId"] = nodeId
        params["enable"] = enable
        return self.driver.execute_and_wait("DOM.forceShowPopover", params)

