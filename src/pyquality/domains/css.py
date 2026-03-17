class CSSDomain:
    def __init__(self, driver):
        self.driver = driver

    def addRule(self, styleSheetId, ruleText, location, nodeForPropertySyntaxValidation=None):
        """
        Inserts a new rule with the given `ruleText` in a stylesheet with given `styleSheetId`, at the position specified by `location`.
        - styleSheetId (any): The css style sheet identifier where a new rule should be inserted.
        - ruleText (string): The text of a new rule.
        - location (any): Text position of a new rule in the target style sheet.
        - nodeForPropertySyntaxValidation (any): NodeId for the DOM node in whose context custom property declarations for registered properties should be
validated. If omitted, declarations in the new rule text can only be validated statically, which may produce
incorrect results if the declaration contains a var() for example.
        """
        params = {}
        params["styleSheetId"] = styleSheetId
        params["ruleText"] = ruleText
        params["location"] = location
        if nodeForPropertySyntaxValidation is not None:
            params["nodeForPropertySyntaxValidation"] = nodeForPropertySyntaxValidation
        return self.driver.execute_and_wait("CSS.addRule", params)

    def collectClassNames(self, styleSheetId):
        """
        Returns all class names from specified stylesheet.
        - styleSheetId (any): 
        """
        params = {}
        params["styleSheetId"] = styleSheetId
        return self.driver.execute_and_wait("CSS.collectClassNames", params)

    def createStyleSheet(self, frameId, force=None):
        """
        Creates a new special "via-inspector" stylesheet in the frame with given `frameId`.
        - frameId (any): Identifier of the frame where "via-inspector" stylesheet should be created.
        - force (boolean): If true, creates a new stylesheet for every call. If false,
returns a stylesheet previously created by a call with force=false
for the frame's document if it exists or creates a new stylesheet
(default: false).
        """
        params = {}
        params["frameId"] = frameId
        if force is not None:
            params["force"] = force
        return self.driver.execute_and_wait("CSS.createStyleSheet", params)

    def disable(self):
        """
        Disables the CSS agent for the given page.
        """
        params = {}
        return self.driver.execute_and_wait("CSS.disable", params)

    def enable(self):
        """
        Enables the CSS agent for the given page. Clients should not assume that the CSS agent has been enabled until the result of this command is received.
        """
        params = {}
        return self.driver.execute_and_wait("CSS.enable", params)

    def forcePseudoState(self, nodeId, forcedPseudoClasses):
        """
        Ensures that the given node will have specified pseudo-classes whenever its style is computed by the browser.
        - nodeId (any): The element id for which to force the pseudo state.
        - forcedPseudoClasses (array): Element pseudo classes to force when computing the element's style.
        """
        params = {}
        params["nodeId"] = nodeId
        params["forcedPseudoClasses"] = forcedPseudoClasses
        return self.driver.execute_and_wait("CSS.forcePseudoState", params)

    def forceStartingStyle(self, nodeId, forced):
        """
        Ensures that the given node is in its starting-style state.
        - nodeId (any): The element id for which to force the starting-style state.
        - forced (boolean): Boolean indicating if this is on or off.
        """
        params = {}
        params["nodeId"] = nodeId
        params["forced"] = forced
        return self.driver.execute_and_wait("CSS.forceStartingStyle", params)

    def getBackgroundColors(self, nodeId):
        """
        Call CSS.getBackgroundColors
        - nodeId (any): Id of the node to get background colors for.
        """
        params = {}
        params["nodeId"] = nodeId
        return self.driver.execute_and_wait("CSS.getBackgroundColors", params)

    def getComputedStyleForNode(self, nodeId):
        """
        Returns the computed style for a DOM node identified by `nodeId`.
        - nodeId (any): 
        """
        params = {}
        params["nodeId"] = nodeId
        return self.driver.execute_and_wait("CSS.getComputedStyleForNode", params)

    def resolveValues(self, values, nodeId, propertyName=None, pseudoType=None, pseudoIdentifier=None):
        """
        Resolve the specified values in the context of the provided element. For example, a value of '1em' is evaluated according to the computed 'font-size' of the element and a value 'calc(1px + 2px)' will be resolved to '3px'. If the `propertyName` was specified the `values` are resolved as if they were property's declaration. If a value cannot be parsed according to the provided property syntax, the value is parsed using combined syntax as if null `propertyName` was provided. If the value cannot be resolved even then, return the provided value without any changes. Note: this function currently does not resolve CSS random() function, it returns unmodified random() function parts.`
        - values (array): Cascade-dependent keywords (revert/revert-layer) do not work.
        - nodeId (any): Id of the node in whose context the expression is evaluated
        - propertyName (string): Only longhands and custom property names are accepted.
        - pseudoType (any): Pseudo element type, only works for pseudo elements that generate
elements in the tree, such as ::before and ::after.
        - pseudoIdentifier (string): Pseudo element custom ident.
        """
        params = {}
        params["values"] = values
        params["nodeId"] = nodeId
        if propertyName is not None:
            params["propertyName"] = propertyName
        if pseudoType is not None:
            params["pseudoType"] = pseudoType
        if pseudoIdentifier is not None:
            params["pseudoIdentifier"] = pseudoIdentifier
        return self.driver.execute_and_wait("CSS.resolveValues", params)

    def getLonghandProperties(self, shorthandName, value):
        """
        Call CSS.getLonghandProperties
        - shorthandName (string): 
        - value (string): 
        """
        params = {}
        params["shorthandName"] = shorthandName
        params["value"] = value
        return self.driver.execute_and_wait("CSS.getLonghandProperties", params)

    def getInlineStylesForNode(self, nodeId):
        """
        Returns the styles defined inline (explicitly in the "style" attribute and implicitly, using DOM attributes) for a DOM node identified by `nodeId`.
        - nodeId (any): 
        """
        params = {}
        params["nodeId"] = nodeId
        return self.driver.execute_and_wait("CSS.getInlineStylesForNode", params)

    def getAnimatedStylesForNode(self, nodeId):
        """
        Returns the styles coming from animations & transitions including the animation & transition styles coming from inheritance chain.
        - nodeId (any): 
        """
        params = {}
        params["nodeId"] = nodeId
        return self.driver.execute_and_wait("CSS.getAnimatedStylesForNode", params)

    def getMatchedStylesForNode(self, nodeId):
        """
        Returns requested styles for a DOM node identified by `nodeId`.
        - nodeId (any): 
        """
        params = {}
        params["nodeId"] = nodeId
        return self.driver.execute_and_wait("CSS.getMatchedStylesForNode", params)

    def getEnvironmentVariables(self):
        """
        Returns the values of the default UA-defined environment variables used in env()
        """
        params = {}
        return self.driver.execute_and_wait("CSS.getEnvironmentVariables", params)

    def getMediaQueries(self):
        """
        Returns all media queries parsed by the rendering engine.
        """
        params = {}
        return self.driver.execute_and_wait("CSS.getMediaQueries", params)

    def getPlatformFontsForNode(self, nodeId):
        """
        Requests information about platform fonts which we used to render child TextNodes in the given node.
        - nodeId (any): 
        """
        params = {}
        params["nodeId"] = nodeId
        return self.driver.execute_and_wait("CSS.getPlatformFontsForNode", params)

    def getStyleSheetText(self, styleSheetId):
        """
        Returns the current textual content for a stylesheet.
        - styleSheetId (any): 
        """
        params = {}
        params["styleSheetId"] = styleSheetId
        return self.driver.execute_and_wait("CSS.getStyleSheetText", params)

    def getLayersForNode(self, nodeId):
        """
        Returns all layers parsed by the rendering engine for the tree scope of a node. Given a DOM element identified by nodeId, getLayersForNode returns the root layer for the nearest ancestor document or shadow root. The layer root contains the full layer tree for the tree scope and their ordering.
        - nodeId (any): 
        """
        params = {}
        params["nodeId"] = nodeId
        return self.driver.execute_and_wait("CSS.getLayersForNode", params)

    def getLocationForSelector(self, styleSheetId, selectorText):
        """
        Given a CSS selector text and a style sheet ID, getLocationForSelector returns an array of locations of the CSS selector in the style sheet.
        - styleSheetId (any): 
        - selectorText (string): 
        """
        params = {}
        params["styleSheetId"] = styleSheetId
        params["selectorText"] = selectorText
        return self.driver.execute_and_wait("CSS.getLocationForSelector", params)

    def trackComputedStyleUpdatesForNode(self, nodeId=None):
        """
        Starts tracking the given node for the computed style updates and whenever the computed style is updated for node, it queues a `computedStyleUpdated` event with throttling. There can only be 1 node tracked for computed style updates so passing a new node id removes tracking from the previous node. Pass `undefined` to disable tracking.
        - nodeId (any): 
        """
        params = {}
        if nodeId is not None:
            params["nodeId"] = nodeId
        return self.driver.execute_and_wait("CSS.trackComputedStyleUpdatesForNode", params)

    def trackComputedStyleUpdates(self, propertiesToTrack):
        """
        Starts tracking the given computed styles for updates. The specified array of properties replaces the one previously specified. Pass empty array to disable tracking. Use takeComputedStyleUpdates to retrieve the list of nodes that had properties modified. The changes to computed style properties are only tracked for nodes pushed to the front-end by the DOM agent. If no changes to the tracked properties occur after the node has been pushed to the front-end, no updates will be issued for the node.
        - propertiesToTrack (array): 
        """
        params = {}
        params["propertiesToTrack"] = propertiesToTrack
        return self.driver.execute_and_wait("CSS.trackComputedStyleUpdates", params)

    def takeComputedStyleUpdates(self):
        """
        Polls the next batch of computed style updates.
        """
        params = {}
        return self.driver.execute_and_wait("CSS.takeComputedStyleUpdates", params)

    def setEffectivePropertyValueForNode(self, nodeId, propertyName, value):
        """
        Find a rule with the given active property for the given node and set the new value for this property
        - nodeId (any): The element id for which to set property.
        - propertyName (string): 
        - value (string): 
        """
        params = {}
        params["nodeId"] = nodeId
        params["propertyName"] = propertyName
        params["value"] = value
        return self.driver.execute_and_wait("CSS.setEffectivePropertyValueForNode", params)

    def setPropertyRulePropertyName(self, styleSheetId, range, propertyName):
        """
        Modifies the property rule property name.
        - styleSheetId (any): 
        - range (any): 
        - propertyName (string): 
        """
        params = {}
        params["styleSheetId"] = styleSheetId
        params["range"] = range
        params["propertyName"] = propertyName
        return self.driver.execute_and_wait("CSS.setPropertyRulePropertyName", params)

    def setKeyframeKey(self, styleSheetId, range, keyText):
        """
        Modifies the keyframe rule key text.
        - styleSheetId (any): 
        - range (any): 
        - keyText (string): 
        """
        params = {}
        params["styleSheetId"] = styleSheetId
        params["range"] = range
        params["keyText"] = keyText
        return self.driver.execute_and_wait("CSS.setKeyframeKey", params)

    def setMediaText(self, styleSheetId, range, text):
        """
        Modifies the rule selector.
        - styleSheetId (any): 
        - range (any): 
        - text (string): 
        """
        params = {}
        params["styleSheetId"] = styleSheetId
        params["range"] = range
        params["text"] = text
        return self.driver.execute_and_wait("CSS.setMediaText", params)

    def setContainerQueryText(self, styleSheetId, range, text):
        """
        Modifies the expression of a container query.
        - styleSheetId (any): 
        - range (any): 
        - text (string): 
        """
        params = {}
        params["styleSheetId"] = styleSheetId
        params["range"] = range
        params["text"] = text
        return self.driver.execute_and_wait("CSS.setContainerQueryText", params)

    def setSupportsText(self, styleSheetId, range, text):
        """
        Modifies the expression of a supports at-rule.
        - styleSheetId (any): 
        - range (any): 
        - text (string): 
        """
        params = {}
        params["styleSheetId"] = styleSheetId
        params["range"] = range
        params["text"] = text
        return self.driver.execute_and_wait("CSS.setSupportsText", params)

    def setNavigationText(self, styleSheetId, range, text):
        """
        Modifies the expression of a navigation at-rule.
        - styleSheetId (any): 
        - range (any): 
        - text (string): 
        """
        params = {}
        params["styleSheetId"] = styleSheetId
        params["range"] = range
        params["text"] = text
        return self.driver.execute_and_wait("CSS.setNavigationText", params)

    def setScopeText(self, styleSheetId, range, text):
        """
        Modifies the expression of a scope at-rule.
        - styleSheetId (any): 
        - range (any): 
        - text (string): 
        """
        params = {}
        params["styleSheetId"] = styleSheetId
        params["range"] = range
        params["text"] = text
        return self.driver.execute_and_wait("CSS.setScopeText", params)

    def setRuleSelector(self, styleSheetId, range, selector):
        """
        Modifies the rule selector.
        - styleSheetId (any): 
        - range (any): 
        - selector (string): 
        """
        params = {}
        params["styleSheetId"] = styleSheetId
        params["range"] = range
        params["selector"] = selector
        return self.driver.execute_and_wait("CSS.setRuleSelector", params)

    def setStyleSheetText(self, styleSheetId, text):
        """
        Sets the new stylesheet text.
        - styleSheetId (any): 
        - text (string): 
        """
        params = {}
        params["styleSheetId"] = styleSheetId
        params["text"] = text
        return self.driver.execute_and_wait("CSS.setStyleSheetText", params)

    def setStyleTexts(self, edits, nodeForPropertySyntaxValidation=None):
        """
        Applies specified style edits one after another in the given order.
        - edits (array): 
        - nodeForPropertySyntaxValidation (any): NodeId for the DOM node in whose context custom property declarations for registered properties should be
validated. If omitted, declarations in the new rule text can only be validated statically, which may produce
incorrect results if the declaration contains a var() for example.
        """
        params = {}
        params["edits"] = edits
        if nodeForPropertySyntaxValidation is not None:
            params["nodeForPropertySyntaxValidation"] = nodeForPropertySyntaxValidation
        return self.driver.execute_and_wait("CSS.setStyleTexts", params)

    def startRuleUsageTracking(self):
        """
        Enables the selector recording.
        """
        params = {}
        return self.driver.execute_and_wait("CSS.startRuleUsageTracking", params)

    def stopRuleUsageTracking(self):
        """
        Stop tracking rule usage and return the list of rules that were used since last call to `takeCoverageDelta` (or since start of coverage instrumentation).
        """
        params = {}
        return self.driver.execute_and_wait("CSS.stopRuleUsageTracking", params)

    def takeCoverageDelta(self):
        """
        Obtain list of rules that became used since last call to this method (or since start of coverage instrumentation).
        """
        params = {}
        return self.driver.execute_and_wait("CSS.takeCoverageDelta", params)

    def setLocalFontsEnabled(self, enabled):
        """
        Enables/disables rendering of local CSS fonts (enabled by default).
        - enabled (boolean): Whether rendering of local fonts is enabled.
        """
        params = {}
        params["enabled"] = enabled
        return self.driver.execute_and_wait("CSS.setLocalFontsEnabled", params)

