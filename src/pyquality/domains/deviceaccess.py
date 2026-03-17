class DeviceAccessDomain:
    def __init__(self, driver):
        self.driver = driver

    def enable(self):
        """
        Enable events in this domain.
        """
        params = {}
        return self.driver.execute_and_wait("DeviceAccess.enable", params)

    def disable(self):
        """
        Disable events in this domain.
        """
        params = {}
        return self.driver.execute_and_wait("DeviceAccess.disable", params)

    def selectPrompt(self, id_, deviceId):
        """
        Select a device in response to a DeviceAccess.deviceRequestPrompted event.
        - id (any): 
        - deviceId (any): 
        """
        params = {}
        params["id"] = id_
        params["deviceId"] = deviceId
        return self.driver.execute_and_wait("DeviceAccess.selectPrompt", params)

    def cancelPrompt(self, id_):
        """
        Cancel a prompt in response to a DeviceAccess.deviceRequestPrompted event.
        - id (any): 
        """
        params = {}
        params["id"] = id_
        return self.driver.execute_and_wait("DeviceAccess.cancelPrompt", params)

