class DeviceOrientationDomain:
    def __init__(self, driver):
        self.driver = driver

    def clearDeviceOrientationOverride(self):
        """
        Clears the overridden Device Orientation.
        """
        params = {}
        return self.driver.execute_and_wait("DeviceOrientation.clearDeviceOrientationOverride", params)

    def setDeviceOrientationOverride(self, alpha, beta, gamma):
        """
        Overrides the Device Orientation.
        - alpha (number): Mock alpha
        - beta (number): Mock beta
        - gamma (number): Mock gamma
        """
        params = {}
        params["alpha"] = alpha
        params["beta"] = beta
        params["gamma"] = gamma
        return self.driver.execute_and_wait("DeviceOrientation.setDeviceOrientationOverride", params)

