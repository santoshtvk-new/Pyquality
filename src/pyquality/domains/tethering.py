class TetheringDomain:
    def __init__(self, driver):
        self.driver = driver

    def bind(self, port):
        """
        Request browser port binding.
        - port (integer): Port number to bind.
        """
        params = {}
        params["port"] = port
        return self.driver.execute_and_wait("Tethering.bind", params)

    def unbind(self, port):
        """
        Request browser port unbinding.
        - port (integer): Port number to unbind.
        """
        params = {}
        params["port"] = port
        return self.driver.execute_and_wait("Tethering.unbind", params)

