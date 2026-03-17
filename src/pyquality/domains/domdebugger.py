class DOMDebuggerDomain:
    def __init__(self, driver):
        self.driver = driver

    def getEventListeners(self, objectId, depth=None, pierce=None):
        """
        Returns event listeners of the given object.
        - objectId (any): Identifier of the object to return listeners for.
        - depth (integer): The maximum depth at which Node children should be retrieved, defaults to 1. Use -1 for the
entire subtree or provide an integer larger than 0.
        - pierce (boolean): Whether or not iframes and shadow roots should be traversed when returning the subtree
(default is false). Reports listeners for all contexts if pierce is enabled.
        """
        params = {}
        params["objectId"] = objectId
        if depth is not None:
            params["depth"] = depth
        if pierce is not None:
            params["pierce"] = pierce
        return self.driver.execute_and_wait("DOMDebugger.getEventListeners", params)

    def removeDOMBreakpoint(self, nodeId, type_):
        """
        Removes DOM breakpoint that was set using `setDOMBreakpoint`.
        - nodeId (any): Identifier of the node to remove breakpoint from.
        - type (any): Type of the breakpoint to remove.
        """
        params = {}
        params["nodeId"] = nodeId
        params["type"] = type_
        return self.driver.execute_and_wait("DOMDebugger.removeDOMBreakpoint", params)

    def removeEventListenerBreakpoint(self, eventName, targetName=None):
        """
        Removes breakpoint on particular DOM event.
        - eventName (string): Event name.
        - targetName (string): EventTarget interface name.
        """
        params = {}
        params["eventName"] = eventName
        if targetName is not None:
            params["targetName"] = targetName
        return self.driver.execute_and_wait("DOMDebugger.removeEventListenerBreakpoint", params)

    def removeInstrumentationBreakpoint(self, eventName):
        """
        Removes breakpoint on particular native event.
        - eventName (string): Instrumentation name to stop on.
        """
        params = {}
        params["eventName"] = eventName
        return self.driver.execute_and_wait("DOMDebugger.removeInstrumentationBreakpoint", params)

    def removeXHRBreakpoint(self, url):
        """
        Removes breakpoint from XMLHttpRequest.
        - url (string): Resource URL substring.
        """
        params = {}
        params["url"] = url
        return self.driver.execute_and_wait("DOMDebugger.removeXHRBreakpoint", params)

    def setBreakOnCSPViolation(self, violationTypes):
        """
        Sets breakpoint on particular CSP violations.
        - violationTypes (array): CSP Violations to stop upon.
        """
        params = {}
        params["violationTypes"] = violationTypes
        return self.driver.execute_and_wait("DOMDebugger.setBreakOnCSPViolation", params)

    def setDOMBreakpoint(self, nodeId, type_):
        """
        Sets breakpoint on particular operation with DOM.
        - nodeId (any): Identifier of the node to set breakpoint on.
        - type (any): Type of the operation to stop upon.
        """
        params = {}
        params["nodeId"] = nodeId
        params["type"] = type_
        return self.driver.execute_and_wait("DOMDebugger.setDOMBreakpoint", params)

    def setEventListenerBreakpoint(self, eventName, targetName=None):
        """
        Sets breakpoint on particular DOM event.
        - eventName (string): DOM Event name to stop on (any DOM event will do).
        - targetName (string): EventTarget interface name to stop on. If equal to `"*"` or not provided, will stop on any
EventTarget.
        """
        params = {}
        params["eventName"] = eventName
        if targetName is not None:
            params["targetName"] = targetName
        return self.driver.execute_and_wait("DOMDebugger.setEventListenerBreakpoint", params)

    def setInstrumentationBreakpoint(self, eventName):
        """
        Sets breakpoint on particular native event.
        - eventName (string): Instrumentation name to stop on.
        """
        params = {}
        params["eventName"] = eventName
        return self.driver.execute_and_wait("DOMDebugger.setInstrumentationBreakpoint", params)

    def setXHRBreakpoint(self, url):
        """
        Sets breakpoint on XMLHttpRequest.
        - url (string): Resource URL substring. All XHRs having this substring in the URL will get stopped upon.
        """
        params = {}
        params["url"] = url
        return self.driver.execute_and_wait("DOMDebugger.setXHRBreakpoint", params)

