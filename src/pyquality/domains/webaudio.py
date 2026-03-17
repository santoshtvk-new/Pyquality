class WebAudioDomain:
    def __init__(self, driver):
        self.driver = driver

    def enable(self):
        """
        Enables the WebAudio domain and starts sending context lifetime events.
        """
        params = {}
        return self.driver.execute_and_wait("WebAudio.enable", params)

    def disable(self):
        """
        Disables the WebAudio domain.
        """
        params = {}
        return self.driver.execute_and_wait("WebAudio.disable", params)

    def getRealtimeData(self, contextId):
        """
        Fetch the realtime data from the registered contexts.
        - contextId (any): 
        """
        params = {}
        params["contextId"] = contextId
        return self.driver.execute_and_wait("WebAudio.getRealtimeData", params)

