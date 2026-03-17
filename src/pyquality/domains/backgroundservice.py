class BackgroundServiceDomain:
    def __init__(self, driver):
        self.driver = driver

    def startObserving(self, service):
        """
        Enables event updates for the service.
        - service (any): 
        """
        params = {}
        params["service"] = service
        return self.driver.execute_and_wait("BackgroundService.startObserving", params)

    def stopObserving(self, service):
        """
        Disables event updates for the service.
        - service (any): 
        """
        params = {}
        params["service"] = service
        return self.driver.execute_and_wait("BackgroundService.stopObserving", params)

    def setRecording(self, shouldRecord, service):
        """
        Set the recording state for the service.
        - shouldRecord (boolean): 
        - service (any): 
        """
        params = {}
        params["shouldRecord"] = shouldRecord
        params["service"] = service
        return self.driver.execute_and_wait("BackgroundService.setRecording", params)

    def clearEvents(self, service):
        """
        Clears all stored data for the service.
        - service (any): 
        """
        params = {}
        params["service"] = service
        return self.driver.execute_and_wait("BackgroundService.clearEvents", params)

