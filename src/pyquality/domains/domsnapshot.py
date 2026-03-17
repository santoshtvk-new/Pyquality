class DOMSnapshotDomain:
    def __init__(self, driver):
        self.driver = driver

    def disable(self):
        """
        Disables DOM snapshot agent for the given page.
        """
        params = {}
        return self.driver.execute_and_wait("DOMSnapshot.disable", params)

    def enable(self):
        """
        Enables DOM snapshot agent for the given page.
        """
        params = {}
        return self.driver.execute_and_wait("DOMSnapshot.enable", params)

    def getSnapshot(self, computedStyleWhitelist, includeEventListeners=None, includePaintOrder=None, includeUserAgentShadowTree=None):
        """
        Returns a document snapshot, including the full DOM tree of the root node (including iframes, template contents, and imported documents) in a flattened array, as well as layout and white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is flattened.
        - computedStyleWhitelist (array): Whitelist of computed styles to return.
        - includeEventListeners (boolean): Whether or not to retrieve details of DOM listeners (default false).
        - includePaintOrder (boolean): Whether to determine and include the paint order index of LayoutTreeNodes (default false).
        - includeUserAgentShadowTree (boolean): Whether to include UA shadow tree in the snapshot (default false).
        """
        params = {}
        params["computedStyleWhitelist"] = computedStyleWhitelist
        if includeEventListeners is not None:
            params["includeEventListeners"] = includeEventListeners
        if includePaintOrder is not None:
            params["includePaintOrder"] = includePaintOrder
        if includeUserAgentShadowTree is not None:
            params["includeUserAgentShadowTree"] = includeUserAgentShadowTree
        return self.driver.execute_and_wait("DOMSnapshot.getSnapshot", params)

    def captureSnapshot(self, computedStyles, includePaintOrder=None, includeDOMRects=None, includeBlendedBackgroundColors=None, includeTextColorOpacities=None):
        """
        Returns a document snapshot, including the full DOM tree of the root node (including iframes, template contents, and imported documents) in a flattened array, as well as layout and white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is flattened.
        - computedStyles (array): Whitelist of computed styles to return.
        - includePaintOrder (boolean): Whether to include layout object paint orders into the snapshot.
        - includeDOMRects (boolean): Whether to include DOM rectangles (offsetRects, clientRects, scrollRects) into the snapshot
        - includeBlendedBackgroundColors (boolean): Whether to include blended background colors in the snapshot (default: false).
Blended background color is achieved by blending background colors of all elements
that overlap with the current element.
        - includeTextColorOpacities (boolean): Whether to include text color opacity in the snapshot (default: false).
An element might have the opacity property set that affects the text color of the element.
The final text color opacity is computed based on the opacity of all overlapping elements.
        """
        params = {}
        params["computedStyles"] = computedStyles
        if includePaintOrder is not None:
            params["includePaintOrder"] = includePaintOrder
        if includeDOMRects is not None:
            params["includeDOMRects"] = includeDOMRects
        if includeBlendedBackgroundColors is not None:
            params["includeBlendedBackgroundColors"] = includeBlendedBackgroundColors
        if includeTextColorOpacities is not None:
            params["includeTextColorOpacities"] = includeTextColorOpacities
        return self.driver.execute_and_wait("DOMSnapshot.captureSnapshot", params)

