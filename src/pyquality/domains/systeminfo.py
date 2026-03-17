class SystemInfoDomain:
    def __init__(self, driver):
        self.driver = driver

    def getInfo(self):
        """
        Returns information about the system.
        """
        params = {}
        return self.driver.execute_and_wait("SystemInfo.getInfo", params)

    def getFeatureState(self, featureState):
        """
        Returns information about the feature state.
        - featureState (string): 
        """
        params = {}
        params["featureState"] = featureState
        return self.driver.execute_and_wait("SystemInfo.getFeatureState", params)

    def getProcessInfo(self):
        """
        Returns information about all running processes.
        """
        params = {}
        return self.driver.execute_and_wait("SystemInfo.getProcessInfo", params)

