class AutofillDomain:
    def __init__(self, driver):
        self.driver = driver

    def trigger(self, fieldId, frameId=None, card=None, address=None):
        """
        Trigger autofill on a form identified by the fieldId. If the field and related form cannot be autofilled, returns an error.
        - fieldId (any): Identifies a field that serves as an anchor for autofill.
        - frameId (any): Identifies the frame that field belongs to.
        - card (any): Credit card information to fill out the form. Credit card data is not saved.  Mutually exclusive with `address`.
        - address (any): Address to fill out the form. Address data is not saved. Mutually exclusive with `card`.
        """
        params = {}
        params["fieldId"] = fieldId
        if frameId is not None:
            params["frameId"] = frameId
        if card is not None:
            params["card"] = card
        if address is not None:
            params["address"] = address
        return self.driver.execute_and_wait("Autofill.trigger", params)

    def setAddresses(self, addresses):
        """
        Set addresses so that developers can verify their forms implementation.
        - addresses (array): 
        """
        params = {}
        params["addresses"] = addresses
        return self.driver.execute_and_wait("Autofill.setAddresses", params)

    def disable(self):
        """
        Disables autofill domain notifications.
        """
        params = {}
        return self.driver.execute_and_wait("Autofill.disable", params)

    def enable(self):
        """
        Enables autofill domain notifications.
        """
        params = {}
        return self.driver.execute_and_wait("Autofill.enable", params)

