class SecurityDomain:
    def __init__(self, driver):
        self.driver = driver

    def disable(self):
        """
        Disables tracking security state changes.
        """
        params = {}
        return self.driver.execute_and_wait("Security.disable", params)

    def enable(self):
        """
        Enables tracking security state changes.
        """
        params = {}
        return self.driver.execute_and_wait("Security.enable", params)

    def setIgnoreCertificateErrors(self, ignore):
        """
        Enable/disable whether all certificate errors should be ignored.
        - ignore (boolean): If true, all certificate errors will be ignored.
        """
        params = {}
        params["ignore"] = ignore
        return self.driver.execute_and_wait("Security.setIgnoreCertificateErrors", params)

    def handleCertificateError(self, eventId, action):
        """
        Handles a certificate error that fired a certificateError event.
        - eventId (integer): The ID of the event.
        - action (any): The action to take on the certificate error.
        """
        params = {}
        params["eventId"] = eventId
        params["action"] = action
        return self.driver.execute_and_wait("Security.handleCertificateError", params)

    def setOverrideCertificateErrors(self, override):
        """
        Enable/disable overriding certificate errors. If enabled, all certificate error events need to be handled by the DevTools client and should be answered with `handleCertificateError` commands.
        - override (boolean): If true, certificate errors will be overridden.
        """
        params = {}
        params["override"] = override
        return self.driver.execute_and_wait("Security.setOverrideCertificateErrors", params)

