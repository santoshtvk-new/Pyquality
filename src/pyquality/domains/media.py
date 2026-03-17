class MediaDomain:
    def __init__(self, driver):
        self.driver = driver

    def enable(self):
        """
        Enables the Media domain
        """
        params = {}
        return self.driver.execute_and_wait("Media.enable", params)

    def disable(self):
        """
        Disables the Media domain.
        """
        params = {}
        return self.driver.execute_and_wait("Media.disable", params)

