class LogDomain:
    def __init__(self, driver):
        self.driver = driver

    def clear(self):
        """
        Clears the log.
        """
        params = {}
        return self.driver.execute_and_wait("Log.clear", params)

    def disable(self):
        """
        Disables log domain, prevents further log entries from being reported to the client.
        """
        params = {}
        return self.driver.execute_and_wait("Log.disable", params)

    def enable(self):
        """
        Enables log domain, sends the entries collected so far to the client by means of the `entryAdded` notification.
        """
        params = {}
        return self.driver.execute_and_wait("Log.enable", params)

    def startViolationsReport(self, config):
        """
        start violation reporting.
        - config (array): Configuration for violations.
        """
        params = {}
        params["config"] = config
        return self.driver.execute_and_wait("Log.startViolationsReport", params)

    def stopViolationsReport(self):
        """
        Stop violation reporting.
        """
        params = {}
        return self.driver.execute_and_wait("Log.stopViolationsReport", params)

