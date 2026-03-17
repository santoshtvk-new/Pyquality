class PerformanceDomain:
    def __init__(self, driver):
        self.driver = driver

    def disable(self):
        """
        Disable collecting and reporting metrics.
        """
        params = {}
        return self.driver.execute_and_wait("Performance.disable", params)

    def enable(self, timeDomain=None):
        """
        Enable collecting and reporting metrics.
        - timeDomain (string): Time domain to use for collecting and reporting duration metrics.
        """
        params = {}
        if timeDomain is not None:
            params["timeDomain"] = timeDomain
        return self.driver.execute_and_wait("Performance.enable", params)

    def setTimeDomain(self, timeDomain):
        """
        Sets time domain to use for collecting and reporting duration metrics. Note that this must be called before enabling metrics collection. Calling this method while metrics collection is enabled returns an error.
        - timeDomain (string): Time domain
        """
        params = {}
        params["timeDomain"] = timeDomain
        return self.driver.execute_and_wait("Performance.setTimeDomain", params)

    def getMetrics(self):
        """
        Retrieve current values of run-time metrics.
        """
        params = {}
        return self.driver.execute_and_wait("Performance.getMetrics", params)

