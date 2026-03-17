class WebAuthnDomain:
    def __init__(self, driver):
        self.driver = driver

    def enable(self, enableUI=None):
        """
        Enable the WebAuthn domain and start intercepting credential storage and retrieval with a virtual authenticator.
        - enableUI (boolean): Whether to enable the WebAuthn user interface. Enabling the UI is
recommended for debugging and demo purposes, as it is closer to the real
experience. Disabling the UI is recommended for automated testing.
Supported at the embedder's discretion if UI is available.
Defaults to false.
        """
        params = {}
        if enableUI is not None:
            params["enableUI"] = enableUI
        return self.driver.execute_and_wait("WebAuthn.enable", params)

    def disable(self):
        """
        Disable the WebAuthn domain.
        """
        params = {}
        return self.driver.execute_and_wait("WebAuthn.disable", params)

    def addVirtualAuthenticator(self, options):
        """
        Creates and adds a virtual authenticator.
        - options (any): 
        """
        params = {}
        params["options"] = options
        return self.driver.execute_and_wait("WebAuthn.addVirtualAuthenticator", params)

    def setResponseOverrideBits(self, authenticatorId, isBogusSignature=None, isBadUV=None, isBadUP=None):
        """
        Resets parameters isBogusSignature, isBadUV, isBadUP to false if they are not present.
        - authenticatorId (any): 
        - isBogusSignature (boolean): If isBogusSignature is set, overrides the signature in the authenticator response to be zero.
Defaults to false.
        - isBadUV (boolean): If isBadUV is set, overrides the UV bit in the flags in the authenticator response to
be zero. Defaults to false.
        - isBadUP (boolean): If isBadUP is set, overrides the UP bit in the flags in the authenticator response to
be zero. Defaults to false.
        """
        params = {}
        params["authenticatorId"] = authenticatorId
        if isBogusSignature is not None:
            params["isBogusSignature"] = isBogusSignature
        if isBadUV is not None:
            params["isBadUV"] = isBadUV
        if isBadUP is not None:
            params["isBadUP"] = isBadUP
        return self.driver.execute_and_wait("WebAuthn.setResponseOverrideBits", params)

    def removeVirtualAuthenticator(self, authenticatorId):
        """
        Removes the given authenticator.
        - authenticatorId (any): 
        """
        params = {}
        params["authenticatorId"] = authenticatorId
        return self.driver.execute_and_wait("WebAuthn.removeVirtualAuthenticator", params)

    def addCredential(self, authenticatorId, credential):
        """
        Adds the credential to the specified authenticator.
        - authenticatorId (any): 
        - credential (any): 
        """
        params = {}
        params["authenticatorId"] = authenticatorId
        params["credential"] = credential
        return self.driver.execute_and_wait("WebAuthn.addCredential", params)

    def getCredential(self, authenticatorId, credentialId):
        """
        Returns a single credential stored in the given virtual authenticator that matches the credential ID.
        - authenticatorId (any): 
        - credentialId (string): 
        """
        params = {}
        params["authenticatorId"] = authenticatorId
        params["credentialId"] = credentialId
        return self.driver.execute_and_wait("WebAuthn.getCredential", params)

    def getCredentials(self, authenticatorId):
        """
        Returns all the credentials stored in the given virtual authenticator.
        - authenticatorId (any): 
        """
        params = {}
        params["authenticatorId"] = authenticatorId
        return self.driver.execute_and_wait("WebAuthn.getCredentials", params)

    def removeCredential(self, authenticatorId, credentialId):
        """
        Removes a credential from the authenticator.
        - authenticatorId (any): 
        - credentialId (string): 
        """
        params = {}
        params["authenticatorId"] = authenticatorId
        params["credentialId"] = credentialId
        return self.driver.execute_and_wait("WebAuthn.removeCredential", params)

    def clearCredentials(self, authenticatorId):
        """
        Clears all the credentials from the specified device.
        - authenticatorId (any): 
        """
        params = {}
        params["authenticatorId"] = authenticatorId
        return self.driver.execute_and_wait("WebAuthn.clearCredentials", params)

    def setUserVerified(self, authenticatorId, isUserVerified):
        """
        Sets whether User Verification succeeds or fails for an authenticator. The default is true.
        - authenticatorId (any): 
        - isUserVerified (boolean): 
        """
        params = {}
        params["authenticatorId"] = authenticatorId
        params["isUserVerified"] = isUserVerified
        return self.driver.execute_and_wait("WebAuthn.setUserVerified", params)

    def setAutomaticPresenceSimulation(self, authenticatorId, enabled):
        """
        Sets whether tests of user presence will succeed immediately (if true) or fail to resolve (if false) for an authenticator. The default is true.
        - authenticatorId (any): 
        - enabled (boolean): 
        """
        params = {}
        params["authenticatorId"] = authenticatorId
        params["enabled"] = enabled
        return self.driver.execute_and_wait("WebAuthn.setAutomaticPresenceSimulation", params)

    def setCredentialProperties(self, authenticatorId, credentialId, backupEligibility=None, backupState=None):
        """
        Allows setting credential properties. https://w3c.github.io/webauthn/#sctn-automation-set-credential-properties
        - authenticatorId (any): 
        - credentialId (string): 
        - backupEligibility (boolean): 
        - backupState (boolean): 
        """
        params = {}
        params["authenticatorId"] = authenticatorId
        params["credentialId"] = credentialId
        if backupEligibility is not None:
            params["backupEligibility"] = backupEligibility
        if backupState is not None:
            params["backupState"] = backupState
        return self.driver.execute_and_wait("WebAuthn.setCredentialProperties", params)

