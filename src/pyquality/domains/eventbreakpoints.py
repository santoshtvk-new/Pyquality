class EventBreakpointsDomain:
    def __init__(self, driver):
        self.driver = driver

    def setInstrumentationBreakpoint(self, eventName):
        """
        Sets breakpoint on particular native event.
        - eventName (string): Instrumentation name to stop on.
        """
        params = {}
        params["eventName"] = eventName
        return self.driver.execute_and_wait("EventBreakpoints.setInstrumentationBreakpoint", params)

    def removeInstrumentationBreakpoint(self, eventName):
        """
        Removes breakpoint on particular native event.
        - eventName (string): Instrumentation name to stop on.
        """
        params = {}
        params["eventName"] = eventName
        return self.driver.execute_and_wait("EventBreakpoints.removeInstrumentationBreakpoint", params)

    def disable(self):
        """
        Removes all breakpoints
        """
        params = {}
        return self.driver.execute_and_wait("EventBreakpoints.disable", params)

