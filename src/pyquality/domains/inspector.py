class InspectorDomain:
    def __init__(self, driver):
        self.driver = driver

    def disable(self):
        """
        Disables inspector domain notifications.
        """
        params = {}
        return self.driver.execute_and_wait("Inspector.disable", params)

    def enable(self):
        """
        Enables inspector domain notifications.
        """
        params = {}
        return self.driver.execute_and_wait("Inspector.enable", params)

