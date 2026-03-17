class SmartCardEmulationDomain:
    def __init__(self, driver):
        self.driver = driver

    def enable(self):
        """
        Enables the |SmartCardEmulation| domain.
        """
        params = {}
        return self.driver.execute_and_wait("SmartCardEmulation.enable", params)

    def disable(self):
        """
        Disables the |SmartCardEmulation| domain.
        """
        params = {}
        return self.driver.execute_and_wait("SmartCardEmulation.disable", params)

    def reportEstablishContextResult(self, requestId, contextId):
        """
        Reports the successful result of a |SCardEstablishContext| call.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaa1b8970169fd4883a6dc4a8f43f19b67 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardestablishcontext
        - requestId (string): 
        - contextId (integer): 
        """
        params = {}
        params["requestId"] = requestId
        params["contextId"] = contextId
        return self.driver.execute_and_wait("SmartCardEmulation.reportEstablishContextResult", params)

    def reportReleaseContextResult(self, requestId):
        """
        Reports the successful result of a |SCardReleaseContext| call.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga6aabcba7744c5c9419fdd6404f73a934 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardreleasecontext
        - requestId (string): 
        """
        params = {}
        params["requestId"] = requestId
        return self.driver.execute_and_wait("SmartCardEmulation.reportReleaseContextResult", params)

    def reportListReadersResult(self, requestId, readers):
        """
        Reports the successful result of a |SCardListReaders| call.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga93b07815789b3cf2629d439ecf20f0d9 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardlistreadersa
        - requestId (string): 
        - readers (array): 
        """
        params = {}
        params["requestId"] = requestId
        params["readers"] = readers
        return self.driver.execute_and_wait("SmartCardEmulation.reportListReadersResult", params)

    def reportGetStatusChangeResult(self, requestId, readerStates):
        """
        Reports the successful result of a |SCardGetStatusChange| call.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga33247d5d1257d59e55647c3bb717db24 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardgetstatuschangea
        - requestId (string): 
        - readerStates (array): 
        """
        params = {}
        params["requestId"] = requestId
        params["readerStates"] = readerStates
        return self.driver.execute_and_wait("SmartCardEmulation.reportGetStatusChangeResult", params)

    def reportBeginTransactionResult(self, requestId, handle):
        """
        Reports the result of a |SCardBeginTransaction| call. On success, this creates a new transaction object.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaddb835dce01a0da1d6ca02d33ee7d861 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardbegintransaction
        - requestId (string): 
        - handle (integer): 
        """
        params = {}
        params["requestId"] = requestId
        params["handle"] = handle
        return self.driver.execute_and_wait("SmartCardEmulation.reportBeginTransactionResult", params)

    def reportPlainResult(self, requestId):
        """
        Reports the successful result of a call that returns only a result code. Used for: |SCardCancel|, |SCardDisconnect|, |SCardSetAttrib|, |SCardEndTransaction|.  This maps to: 1. SCardCancel    PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaacbbc0c6d6c0cbbeb4f4debf6fbeeee6    Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardcancel  2. SCardDisconnect    PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga4be198045c73ec0deb79e66c0ca1738a    Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scarddisconnect  3. SCardSetAttrib    PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga060f0038a4ddfd5dd2b8fadf3c3a2e4f    Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardsetattrib  4. SCardEndTransaction    PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gae8742473b404363e5c587f570d7e2f3b    Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardendtransaction
        - requestId (string): 
        """
        params = {}
        params["requestId"] = requestId
        return self.driver.execute_and_wait("SmartCardEmulation.reportPlainResult", params)

    def reportConnectResult(self, requestId, handle, activeProtocol=None):
        """
        Reports the successful result of a |SCardConnect| call.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga4e515829752e0a8dbc4d630696a8d6a5 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardconnecta
        - requestId (string): 
        - handle (integer): 
        - activeProtocol (any): 
        """
        params = {}
        params["requestId"] = requestId
        params["handle"] = handle
        if activeProtocol is not None:
            params["activeProtocol"] = activeProtocol
        return self.driver.execute_and_wait("SmartCardEmulation.reportConnectResult", params)

    def reportDataResult(self, requestId, data):
        """
        Reports the successful result of a call that sends back data on success. Used for |SCardTransmit|, |SCardControl|, and |SCardGetAttrib|.  This maps to: 1. SCardTransmit    PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga9a2d77242a271310269065e64633ab99    Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardtransmit  2. SCardControl    PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gac3454d4657110fd7f753b2d3d8f4e32f    Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardcontrol  3. SCardGetAttrib    PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaacfec51917255b7a25b94c5104961602    Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardgetattrib
        - requestId (string): 
        - data (string): 
        """
        params = {}
        params["requestId"] = requestId
        params["data"] = data
        return self.driver.execute_and_wait("SmartCardEmulation.reportDataResult", params)

    def reportStatusResult(self, requestId, readerName, state, atr, protocol=None):
        """
        Reports the successful result of a |SCardStatus| call.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gae49c3c894ad7ac12a5b896bde70d0382 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardstatusa
        - requestId (string): 
        - readerName (string): 
        - state (any): 
        - atr (string): 
        - protocol (any): 
        """
        params = {}
        params["requestId"] = requestId
        params["readerName"] = readerName
        params["state"] = state
        params["atr"] = atr
        if protocol is not None:
            params["protocol"] = protocol
        return self.driver.execute_and_wait("SmartCardEmulation.reportStatusResult", params)

    def reportError(self, requestId, resultCode):
        """
        Reports an error result for the given request.
        - requestId (string): 
        - resultCode (any): 
        """
        params = {}
        params["requestId"] = requestId
        params["resultCode"] = resultCode
        return self.driver.execute_and_wait("SmartCardEmulation.reportError", params)

