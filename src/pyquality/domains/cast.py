class CastDomain:
    def __init__(self, driver):
        self.driver = driver

    def enable(self, presentationUrl=None):
        """
        Starts observing for sinks that can be used for tab mirroring, and if set, sinks compatible with |presentationUrl| as well. When sinks are found, a |sinksUpdated| event is fired. Also starts observing for issue messages. When an issue is added or removed, an |issueUpdated| event is fired.
        - presentationUrl (string): 
        """
        params = {}
        if presentationUrl is not None:
            params["presentationUrl"] = presentationUrl
        return self.driver.execute_and_wait("Cast.enable", params)

    def disable(self):
        """
        Stops observing for sinks and issues.
        """
        params = {}
        return self.driver.execute_and_wait("Cast.disable", params)

    def setSinkToUse(self, sinkName):
        """
        Sets a sink to be used when the web page requests the browser to choose a sink via Presentation API, Remote Playback API, or Cast SDK.
        - sinkName (string): 
        """
        params = {}
        params["sinkName"] = sinkName
        return self.driver.execute_and_wait("Cast.setSinkToUse", params)

    def startDesktopMirroring(self, sinkName):
        """
        Starts mirroring the desktop to the sink.
        - sinkName (string): 
        """
        params = {}
        params["sinkName"] = sinkName
        return self.driver.execute_and_wait("Cast.startDesktopMirroring", params)

    def startTabMirroring(self, sinkName):
        """
        Starts mirroring the tab to the sink.
        - sinkName (string): 
        """
        params = {}
        params["sinkName"] = sinkName
        return self.driver.execute_and_wait("Cast.startTabMirroring", params)

    def stopCasting(self, sinkName):
        """
        Stops the active Cast session on the sink.
        - sinkName (string): 
        """
        params = {}
        params["sinkName"] = sinkName
        return self.driver.execute_and_wait("Cast.stopCasting", params)

