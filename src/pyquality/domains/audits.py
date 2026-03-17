class AuditsDomain:
    def __init__(self, driver):
        self.driver = driver

    def getEncodedResponse(self, requestId, encoding, quality=None, sizeOnly=None):
        """
        Returns the response body and size if it were re-encoded with the specified settings. Only applies to images.
        - requestId (any): Identifier of the network request to get content for.
        - encoding (string): The encoding to use.
        - quality (number): The quality of the encoding (0-1). (defaults to 1)
        - sizeOnly (boolean): Whether to only return the size information (defaults to false).
        """
        params = {}
        params["requestId"] = requestId
        params["encoding"] = encoding
        if quality is not None:
            params["quality"] = quality
        if sizeOnly is not None:
            params["sizeOnly"] = sizeOnly
        return self.driver.execute_and_wait("Audits.getEncodedResponse", params)

    def disable(self):
        """
        Disables issues domain, prevents further issues from being reported to the client.
        """
        params = {}
        return self.driver.execute_and_wait("Audits.disable", params)

    def enable(self):
        """
        Enables issues domain, sends the issues collected so far to the client by means of the `issueAdded` event.
        """
        params = {}
        return self.driver.execute_and_wait("Audits.enable", params)

    def checkFormsIssues(self):
        """
        Runs the form issues check for the target page. Found issues are reported using Audits.issueAdded event.
        """
        params = {}
        return self.driver.execute_and_wait("Audits.checkFormsIssues", params)

