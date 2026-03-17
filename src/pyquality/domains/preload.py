class PreloadDomain:
    def __init__(self, driver):
        self.driver = driver

    def enable(self):
        """
        Call Preload.enable
        """
        params = {}
        return self.driver.execute_and_wait("Preload.enable", params)

    def disable(self):
        """
        Call Preload.disable
        """
        params = {}
        return self.driver.execute_and_wait("Preload.disable", params)

