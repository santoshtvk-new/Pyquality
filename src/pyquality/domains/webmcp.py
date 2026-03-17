class WebMCPDomain:
    def __init__(self, driver):
        self.driver = driver

    def enable(self):
        """
        Enables the WebMCP domain, allowing events to be sent. Enabling the domain will trigger a toolsAdded event for all currently registered tools.
        """
        params = {}
        return self.driver.execute_and_wait("WebMCP.enable", params)

