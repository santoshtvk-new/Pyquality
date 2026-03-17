class FetchDomain:
    def __init__(self, driver):
        self.driver = driver

    def disable(self):
        """
        Disables the fetch domain.
        """
        params = {}
        return self.driver.execute_and_wait("Fetch.disable", params)

    def enable(self, patterns=None, handleAuthRequests=None):
        """
        Enables issuing of requestPaused events. A request will be paused until client calls one of failRequest, fulfillRequest or continueRequest/continueWithAuth.
        - patterns (array): If specified, only requests matching any of these patterns will produce
fetchRequested event and will be paused until clients response. If not set,
all requests will be affected.
        - handleAuthRequests (boolean): If true, authRequired events will be issued and requests will be paused
expecting a call to continueWithAuth.
        """
        params = {}
        if patterns is not None:
            params["patterns"] = patterns
        if handleAuthRequests is not None:
            params["handleAuthRequests"] = handleAuthRequests
        return self.driver.execute_and_wait("Fetch.enable", params)

    def failRequest(self, requestId, errorReason):
        """
        Causes the request to fail with specified reason.
        - requestId (any): An id the client received in requestPaused event.
        - errorReason (any): Causes the request to fail with the given reason.
        """
        params = {}
        params["requestId"] = requestId
        params["errorReason"] = errorReason
        return self.driver.execute_and_wait("Fetch.failRequest", params)

    def fulfillRequest(self, requestId, responseCode, responseHeaders=None, binaryResponseHeaders=None, body=None, responsePhrase=None):
        """
        Provides response to the request.
        - requestId (any): An id the client received in requestPaused event.
        - responseCode (integer): An HTTP response code.
        - responseHeaders (array): Response headers.
        - binaryResponseHeaders (string): Alternative way of specifying response headers as a \0-separated
series of name: value pairs. Prefer the above method unless you
need to represent some non-UTF8 values that can't be transmitted
over the protocol as text. (Encoded as a base64 string when passed over JSON)
        - body (string): A response body. If absent, original response body will be used if
the request is intercepted at the response stage and empty body
will be used if the request is intercepted at the request stage. (Encoded as a base64 string when passed over JSON)
        - responsePhrase (string): A textual representation of responseCode.
If absent, a standard phrase matching responseCode is used.
        """
        params = {}
        params["requestId"] = requestId
        params["responseCode"] = responseCode
        if responseHeaders is not None:
            params["responseHeaders"] = responseHeaders
        if binaryResponseHeaders is not None:
            params["binaryResponseHeaders"] = binaryResponseHeaders
        if body is not None:
            params["body"] = body
        if responsePhrase is not None:
            params["responsePhrase"] = responsePhrase
        return self.driver.execute_and_wait("Fetch.fulfillRequest", params)

    def continueRequest(self, requestId, url=None, method=None, postData=None, headers=None, interceptResponse=None):
        """
        Continues the request, optionally modifying some of its parameters.
        - requestId (any): An id the client received in requestPaused event.
        - url (string): If set, the request url will be modified in a way that's not observable by page.
        - method (string): If set, the request method is overridden.
        - postData (string): If set, overrides the post data in the request. (Encoded as a base64 string when passed over JSON)
        - headers (array): If set, overrides the request headers. Note that the overrides do not
extend to subsequent redirect hops, if a redirect happens. Another override
may be applied to a different request produced by a redirect.
        - interceptResponse (boolean): If set, overrides response interception behavior for this request.
        """
        params = {}
        params["requestId"] = requestId
        if url is not None:
            params["url"] = url
        if method is not None:
            params["method"] = method
        if postData is not None:
            params["postData"] = postData
        if headers is not None:
            params["headers"] = headers
        if interceptResponse is not None:
            params["interceptResponse"] = interceptResponse
        return self.driver.execute_and_wait("Fetch.continueRequest", params)

    def continueWithAuth(self, requestId, authChallengeResponse):
        """
        Continues a request supplying authChallengeResponse following authRequired event.
        - requestId (any): An id the client received in authRequired event.
        - authChallengeResponse (any): Response to  with an authChallenge.
        """
        params = {}
        params["requestId"] = requestId
        params["authChallengeResponse"] = authChallengeResponse
        return self.driver.execute_and_wait("Fetch.continueWithAuth", params)

    def continueResponse(self, requestId, responseCode=None, responsePhrase=None, responseHeaders=None, binaryResponseHeaders=None):
        """
        Continues loading of the paused response, optionally modifying the response headers. If either responseCode or headers are modified, all of them must be present.
        - requestId (any): An id the client received in requestPaused event.
        - responseCode (integer): An HTTP response code. If absent, original response code will be used.
        - responsePhrase (string): A textual representation of responseCode.
If absent, a standard phrase matching responseCode is used.
        - responseHeaders (array): Response headers. If absent, original response headers will be used.
        - binaryResponseHeaders (string): Alternative way of specifying response headers as a \0-separated
series of name: value pairs. Prefer the above method unless you
need to represent some non-UTF8 values that can't be transmitted
over the protocol as text. (Encoded as a base64 string when passed over JSON)
        """
        params = {}
        params["requestId"] = requestId
        if responseCode is not None:
            params["responseCode"] = responseCode
        if responsePhrase is not None:
            params["responsePhrase"] = responsePhrase
        if responseHeaders is not None:
            params["responseHeaders"] = responseHeaders
        if binaryResponseHeaders is not None:
            params["binaryResponseHeaders"] = binaryResponseHeaders
        return self.driver.execute_and_wait("Fetch.continueResponse", params)

    def getResponseBody(self, requestId):
        """
        Causes the body of the response to be received from the server and returned as a single string. May only be issued for a request that is paused in the Response stage and is mutually exclusive with takeResponseBodyForInterceptionAsStream. Calling other methods that affect the request or disabling fetch domain before body is received results in an undefined behavior. Note that the response body is not available for redirects. Requests paused in the _redirect received_ state may be differentiated by `responseCode` and presence of `location` response header, see comments to `requestPaused` for details.
        - requestId (any): Identifier for the intercepted request to get body for.
        """
        params = {}
        params["requestId"] = requestId
        return self.driver.execute_and_wait("Fetch.getResponseBody", params)

    def takeResponseBodyAsStream(self, requestId):
        """
        Returns a handle to the stream representing the response body. The request must be paused in the HeadersReceived stage. Note that after this command the request can't be continued as is -- client either needs to cancel it or to provide the response body. The stream only supports sequential read, IO.read will fail if the position is specified. This method is mutually exclusive with getResponseBody. Calling other methods that affect the request or disabling fetch domain before body is received results in an undefined behavior.
        - requestId (any): 
        """
        params = {}
        params["requestId"] = requestId
        return self.driver.execute_and_wait("Fetch.takeResponseBodyAsStream", params)

