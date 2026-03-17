class FedCmDomain:
    def __init__(self, driver):
        self.driver = driver

    def enable(self, disableRejectionDelay=None):
        """
        Call FedCm.enable
        - disableRejectionDelay (boolean): Allows callers to disable the promise rejection delay that would
normally happen, if this is unimportant to what's being tested.
(step 4 of https://fedidcg.github.io/FedCM/#browser-api-rp-sign-in)
        """
        params = {}
        if disableRejectionDelay is not None:
            params["disableRejectionDelay"] = disableRejectionDelay
        return self.driver.execute_and_wait("FedCm.enable", params)

    def disable(self):
        """
        Call FedCm.disable
        """
        params = {}
        return self.driver.execute_and_wait("FedCm.disable", params)

    def selectAccount(self, dialogId, accountIndex):
        """
        Call FedCm.selectAccount
        - dialogId (string): 
        - accountIndex (integer): 
        """
        params = {}
        params["dialogId"] = dialogId
        params["accountIndex"] = accountIndex
        return self.driver.execute_and_wait("FedCm.selectAccount", params)

    def clickDialogButton(self, dialogId, dialogButton):
        """
        Call FedCm.clickDialogButton
        - dialogId (string): 
        - dialogButton (any): 
        """
        params = {}
        params["dialogId"] = dialogId
        params["dialogButton"] = dialogButton
        return self.driver.execute_and_wait("FedCm.clickDialogButton", params)

    def openUrl(self, dialogId, accountIndex, accountUrlType):
        """
        Call FedCm.openUrl
        - dialogId (string): 
        - accountIndex (integer): 
        - accountUrlType (any): 
        """
        params = {}
        params["dialogId"] = dialogId
        params["accountIndex"] = accountIndex
        params["accountUrlType"] = accountUrlType
        return self.driver.execute_and_wait("FedCm.openUrl", params)

    def dismissDialog(self, dialogId, triggerCooldown=None):
        """
        Call FedCm.dismissDialog
        - dialogId (string): 
        - triggerCooldown (boolean): 
        """
        params = {}
        params["dialogId"] = dialogId
        if triggerCooldown is not None:
            params["triggerCooldown"] = triggerCooldown
        return self.driver.execute_and_wait("FedCm.dismissDialog", params)

    def resetCooldown(self):
        """
        Resets the cooldown time, if any, to allow the next FedCM call to show a dialog even if one was recently dismissed by the user.
        """
        params = {}
        return self.driver.execute_and_wait("FedCm.resetCooldown", params)

