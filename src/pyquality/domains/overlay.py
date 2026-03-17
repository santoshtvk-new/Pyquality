class OverlayDomain:
    def __init__(self, driver):
        self.driver = driver

    def disable(self):
        """
        Disables domain notifications.
        """
        params = {}
        return self.driver.execute_and_wait("Overlay.disable", params)

    def enable(self):
        """
        Enables domain notifications.
        """
        params = {}
        return self.driver.execute_and_wait("Overlay.enable", params)

    def getHighlightObjectForTest(self, nodeId, includeDistance=None, includeStyle=None, colorFormat=None, showAccessibilityInfo=None):
        """
        For testing.
        - nodeId (any): Id of the node to get highlight object for.
        - includeDistance (boolean): Whether to include distance info.
        - includeStyle (boolean): Whether to include style info.
        - colorFormat (any): The color format to get config with (default: hex).
        - showAccessibilityInfo (boolean): Whether to show accessibility info (default: true).
        """
        params = {}
        params["nodeId"] = nodeId
        if includeDistance is not None:
            params["includeDistance"] = includeDistance
        if includeStyle is not None:
            params["includeStyle"] = includeStyle
        if colorFormat is not None:
            params["colorFormat"] = colorFormat
        if showAccessibilityInfo is not None:
            params["showAccessibilityInfo"] = showAccessibilityInfo
        return self.driver.execute_and_wait("Overlay.getHighlightObjectForTest", params)

    def getGridHighlightObjectsForTest(self, nodeIds):
        """
        For Persistent Grid testing.
        - nodeIds (array): Ids of the node to get highlight object for.
        """
        params = {}
        params["nodeIds"] = nodeIds
        return self.driver.execute_and_wait("Overlay.getGridHighlightObjectsForTest", params)

    def getSourceOrderHighlightObjectForTest(self, nodeId):
        """
        For Source Order Viewer testing.
        - nodeId (any): Id of the node to highlight.
        """
        params = {}
        params["nodeId"] = nodeId
        return self.driver.execute_and_wait("Overlay.getSourceOrderHighlightObjectForTest", params)

    def hideHighlight(self):
        """
        Hides any highlight.
        """
        params = {}
        return self.driver.execute_and_wait("Overlay.hideHighlight", params)

    def highlightFrame(self, frameId, contentColor=None, contentOutlineColor=None):
        """
        Highlights owner element of the frame with given id. Deprecated: Doesn't work reliably and cannot be fixed due to process separation (the owner node might be in a different process). Determine the owner node in the client and use highlightNode.
        - frameId (any): Identifier of the frame to highlight.
        - contentColor (any): The content box highlight fill color (default: transparent).
        - contentOutlineColor (any): The content box highlight outline color (default: transparent).
        """
        params = {}
        params["frameId"] = frameId
        if contentColor is not None:
            params["contentColor"] = contentColor
        if contentOutlineColor is not None:
            params["contentOutlineColor"] = contentOutlineColor
        return self.driver.execute_and_wait("Overlay.highlightFrame", params)

    def highlightNode(self, highlightConfig, nodeId=None, backendNodeId=None, objectId=None, selector=None):
        """
        Highlights DOM node with given id or with the given JavaScript object wrapper. Either nodeId or objectId must be specified.
        - highlightConfig (any): A descriptor for the highlight appearance.
        - nodeId (any): Identifier of the node to highlight.
        - backendNodeId (any): Identifier of the backend node to highlight.
        - objectId (any): JavaScript object id of the node to be highlighted.
        - selector (string): Selectors to highlight relevant nodes.
        """
        params = {}
        params["highlightConfig"] = highlightConfig
        if nodeId is not None:
            params["nodeId"] = nodeId
        if backendNodeId is not None:
            params["backendNodeId"] = backendNodeId
        if objectId is not None:
            params["objectId"] = objectId
        if selector is not None:
            params["selector"] = selector
        return self.driver.execute_and_wait("Overlay.highlightNode", params)

    def highlightQuad(self, quad, color=None, outlineColor=None):
        """
        Highlights given quad. Coordinates are absolute with respect to the main frame viewport.
        - quad (any): Quad to highlight
        - color (any): The highlight fill color (default: transparent).
        - outlineColor (any): The highlight outline color (default: transparent).
        """
        params = {}
        params["quad"] = quad
        if color is not None:
            params["color"] = color
        if outlineColor is not None:
            params["outlineColor"] = outlineColor
        return self.driver.execute_and_wait("Overlay.highlightQuad", params)

    def highlightRect(self, x, y, width, height, color=None, outlineColor=None):
        """
        Highlights given rectangle. Coordinates are absolute with respect to the main frame viewport. Issue: the method does not handle device pixel ratio (DPR) correctly. The coordinates currently have to be adjusted by the client if DPR is not 1 (see crbug.com/437807128).
        - x (integer): X coordinate
        - y (integer): Y coordinate
        - width (integer): Rectangle width
        - height (integer): Rectangle height
        - color (any): The highlight fill color (default: transparent).
        - outlineColor (any): The highlight outline color (default: transparent).
        """
        params = {}
        params["x"] = x
        params["y"] = y
        params["width"] = width
        params["height"] = height
        if color is not None:
            params["color"] = color
        if outlineColor is not None:
            params["outlineColor"] = outlineColor
        return self.driver.execute_and_wait("Overlay.highlightRect", params)

    def highlightSourceOrder(self, sourceOrderConfig, nodeId=None, backendNodeId=None, objectId=None):
        """
        Highlights the source order of the children of the DOM node with given id or with the given JavaScript object wrapper. Either nodeId or objectId must be specified.
        - sourceOrderConfig (any): A descriptor for the appearance of the overlay drawing.
        - nodeId (any): Identifier of the node to highlight.
        - backendNodeId (any): Identifier of the backend node to highlight.
        - objectId (any): JavaScript object id of the node to be highlighted.
        """
        params = {}
        params["sourceOrderConfig"] = sourceOrderConfig
        if nodeId is not None:
            params["nodeId"] = nodeId
        if backendNodeId is not None:
            params["backendNodeId"] = backendNodeId
        if objectId is not None:
            params["objectId"] = objectId
        return self.driver.execute_and_wait("Overlay.highlightSourceOrder", params)

    def setInspectMode(self, mode, highlightConfig=None):
        """
        Enters the 'inspect' mode. In this mode, elements that user is hovering over are highlighted. Backend then generates 'inspectNodeRequested' event upon element selection.
        - mode (any): Set an inspection mode.
        - highlightConfig (any): A descriptor for the highlight appearance of hovered-over nodes. May be omitted if `enabled
== false`.
        """
        params = {}
        params["mode"] = mode
        if highlightConfig is not None:
            params["highlightConfig"] = highlightConfig
        return self.driver.execute_and_wait("Overlay.setInspectMode", params)

    def setShowAdHighlights(self, show):
        """
        Highlights owner element of all frames detected to be ads.
        - show (boolean): True for showing ad highlights
        """
        params = {}
        params["show"] = show
        return self.driver.execute_and_wait("Overlay.setShowAdHighlights", params)

    def setPausedInDebuggerMessage(self, message=None):
        """
        Call Overlay.setPausedInDebuggerMessage
        - message (string): The message to display, also triggers resume and step over controls.
        """
        params = {}
        if message is not None:
            params["message"] = message
        return self.driver.execute_and_wait("Overlay.setPausedInDebuggerMessage", params)

    def setShowDebugBorders(self, show):
        """
        Requests that backend shows debug borders on layers
        - show (boolean): True for showing debug borders
        """
        params = {}
        params["show"] = show
        return self.driver.execute_and_wait("Overlay.setShowDebugBorders", params)

    def setShowFPSCounter(self, show):
        """
        Requests that backend shows the FPS counter
        - show (boolean): True for showing the FPS counter
        """
        params = {}
        params["show"] = show
        return self.driver.execute_and_wait("Overlay.setShowFPSCounter", params)

    def setShowGridOverlays(self, gridNodeHighlightConfigs):
        """
        Highlight multiple elements with the CSS Grid overlay.
        - gridNodeHighlightConfigs (array): An array of node identifiers and descriptors for the highlight appearance.
        """
        params = {}
        params["gridNodeHighlightConfigs"] = gridNodeHighlightConfigs
        return self.driver.execute_and_wait("Overlay.setShowGridOverlays", params)

    def setShowFlexOverlays(self, flexNodeHighlightConfigs):
        """
        Call Overlay.setShowFlexOverlays
        - flexNodeHighlightConfigs (array): An array of node identifiers and descriptors for the highlight appearance.
        """
        params = {}
        params["flexNodeHighlightConfigs"] = flexNodeHighlightConfigs
        return self.driver.execute_and_wait("Overlay.setShowFlexOverlays", params)

    def setShowScrollSnapOverlays(self, scrollSnapHighlightConfigs):
        """
        Call Overlay.setShowScrollSnapOverlays
        - scrollSnapHighlightConfigs (array): An array of node identifiers and descriptors for the highlight appearance.
        """
        params = {}
        params["scrollSnapHighlightConfigs"] = scrollSnapHighlightConfigs
        return self.driver.execute_and_wait("Overlay.setShowScrollSnapOverlays", params)

    def setShowContainerQueryOverlays(self, containerQueryHighlightConfigs):
        """
        Call Overlay.setShowContainerQueryOverlays
        - containerQueryHighlightConfigs (array): An array of node identifiers and descriptors for the highlight appearance.
        """
        params = {}
        params["containerQueryHighlightConfigs"] = containerQueryHighlightConfigs
        return self.driver.execute_and_wait("Overlay.setShowContainerQueryOverlays", params)

    def setShowInspectedElementAnchor(self, inspectedElementAnchorConfig):
        """
        Call Overlay.setShowInspectedElementAnchor
        - inspectedElementAnchorConfig (any): Node identifier for which to show an anchor for.
        """
        params = {}
        params["inspectedElementAnchorConfig"] = inspectedElementAnchorConfig
        return self.driver.execute_and_wait("Overlay.setShowInspectedElementAnchor", params)

    def setShowPaintRects(self, result):
        """
        Requests that backend shows paint rectangles
        - result (boolean): True for showing paint rectangles
        """
        params = {}
        params["result"] = result
        return self.driver.execute_and_wait("Overlay.setShowPaintRects", params)

    def setShowLayoutShiftRegions(self, result):
        """
        Requests that backend shows layout shift regions
        - result (boolean): True for showing layout shift regions
        """
        params = {}
        params["result"] = result
        return self.driver.execute_and_wait("Overlay.setShowLayoutShiftRegions", params)

    def setShowScrollBottleneckRects(self, show):
        """
        Requests that backend shows scroll bottleneck rects
        - show (boolean): True for showing scroll bottleneck rects
        """
        params = {}
        params["show"] = show
        return self.driver.execute_and_wait("Overlay.setShowScrollBottleneckRects", params)

    def setShowHitTestBorders(self, show):
        """
        Deprecated, no longer has any effect.
        - show (boolean): True for showing hit-test borders
        """
        params = {}
        params["show"] = show
        return self.driver.execute_and_wait("Overlay.setShowHitTestBorders", params)

    def setShowWebVitals(self, show):
        """
        Deprecated, no longer has any effect.
        - show (boolean): 
        """
        params = {}
        params["show"] = show
        return self.driver.execute_and_wait("Overlay.setShowWebVitals", params)

    def setShowViewportSizeOnResize(self, show):
        """
        Paints viewport size upon main frame resize.
        - show (boolean): Whether to paint size or not.
        """
        params = {}
        params["show"] = show
        return self.driver.execute_and_wait("Overlay.setShowViewportSizeOnResize", params)

    def setShowHinge(self, hingeConfig=None):
        """
        Add a dual screen device hinge
        - hingeConfig (any): hinge data, null means hideHinge
        """
        params = {}
        if hingeConfig is not None:
            params["hingeConfig"] = hingeConfig
        return self.driver.execute_and_wait("Overlay.setShowHinge", params)

    def setShowIsolatedElements(self, isolatedElementHighlightConfigs):
        """
        Show elements in isolation mode with overlays.
        - isolatedElementHighlightConfigs (array): An array of node identifiers and descriptors for the highlight appearance.
        """
        params = {}
        params["isolatedElementHighlightConfigs"] = isolatedElementHighlightConfigs
        return self.driver.execute_and_wait("Overlay.setShowIsolatedElements", params)

    def setShowWindowControlsOverlay(self, windowControlsOverlayConfig=None):
        """
        Show Window Controls Overlay for PWA
        - windowControlsOverlayConfig (any): Window Controls Overlay data, null means hide Window Controls Overlay
        """
        params = {}
        if windowControlsOverlayConfig is not None:
            params["windowControlsOverlayConfig"] = windowControlsOverlayConfig
        return self.driver.execute_and_wait("Overlay.setShowWindowControlsOverlay", params)

