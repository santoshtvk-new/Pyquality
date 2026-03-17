class NetworkDomain:
    def __init__(self, driver):
        self.driver = driver

    def setAcceptedEncodings(self, encodings):
        """
        Sets a list of content encodings that will be accepted. Empty list means no encoding is accepted.
        - encodings (array): List of accepted content encodings.
        """
        params = {}
        params["encodings"] = encodings
        return self.driver.execute_and_wait("Network.setAcceptedEncodings", params)

    def clearAcceptedEncodingsOverride(self):
        """
        Clears accepted encodings set by setAcceptedEncodings
        """
        params = {}
        return self.driver.execute_and_wait("Network.clearAcceptedEncodingsOverride", params)

    def canClearBrowserCache(self):
        """
        Tells whether clearing browser cache is supported.
        """
        params = {}
        return self.driver.execute_and_wait("Network.canClearBrowserCache", params)

    def canClearBrowserCookies(self):
        """
        Tells whether clearing browser cookies is supported.
        """
        params = {}
        return self.driver.execute_and_wait("Network.canClearBrowserCookies", params)

    def canEmulateNetworkConditions(self):
        """
        Tells whether emulation of network conditions is supported.
        """
        params = {}
        return self.driver.execute_and_wait("Network.canEmulateNetworkConditions", params)

    def clearBrowserCache(self):
        """
        Clears browser cache.
        """
        params = {}
        return self.driver.execute_and_wait("Network.clearBrowserCache", params)

    def clearBrowserCookies(self):
        """
        Clears browser cookies.
        """
        params = {}
        return self.driver.execute_and_wait("Network.clearBrowserCookies", params)

    def continueInterceptedRequest(self, interceptionId, errorReason=None, rawResponse=None, url=None, method=None, postData=None, headers=None, authChallengeResponse=None):
        """
        Response to Network.requestIntercepted which either modifies the request to continue with any modifications, or blocks it, or completes it with the provided response bytes. If a network fetch occurs as a result which encounters a redirect an additional Network.requestIntercepted event will be sent with the same InterceptionId. Deprecated, use Fetch.continueRequest, Fetch.fulfillRequest and Fetch.failRequest instead.
        - interceptionId (any): 
        - errorReason (any): If set this causes the request to fail with the given reason. Passing `Aborted` for requests
marked with `isNavigationRequest` also cancels the navigation. Must not be set in response
to an authChallenge.
        - rawResponse (string): If set the requests completes using with the provided base64 encoded raw response, including
HTTP status line and headers etc... Must not be set in response to an authChallenge. (Encoded as a base64 string when passed over JSON)
        - url (string): If set the request url will be modified in a way that's not observable by page. Must not be
set in response to an authChallenge.
        - method (string): If set this allows the request method to be overridden. Must not be set in response to an
authChallenge.
        - postData (string): If set this allows postData to be set. Must not be set in response to an authChallenge.
        - headers (any): If set this allows the request headers to be changed. Must not be set in response to an
authChallenge.
        - authChallengeResponse (any): Response to a requestIntercepted with an authChallenge. Must not be set otherwise.
        """
        params = {}
        params["interceptionId"] = interceptionId
        if errorReason is not None:
            params["errorReason"] = errorReason
        if rawResponse is not None:
            params["rawResponse"] = rawResponse
        if url is not None:
            params["url"] = url
        if method is not None:
            params["method"] = method
        if postData is not None:
            params["postData"] = postData
        if headers is not None:
            params["headers"] = headers
        if authChallengeResponse is not None:
            params["authChallengeResponse"] = authChallengeResponse
        return self.driver.execute_and_wait("Network.continueInterceptedRequest", params)

    def deleteCookies(self, name, url=None, domain=None, path=None, partitionKey=None):
        """
        Deletes browser cookies with matching name and url or domain/path/partitionKey pair.
        - name (string): Name of the cookies to remove.
        - url (string): If specified, deletes all the cookies with the given name where domain and path match
provided URL.
        - domain (string): If specified, deletes only cookies with the exact domain.
        - path (string): If specified, deletes only cookies with the exact path.
        - partitionKey (any): If specified, deletes only cookies with the the given name and partitionKey where
all partition key attributes match the cookie partition key attribute.
        """
        params = {}
        params["name"] = name
        if url is not None:
            params["url"] = url
        if domain is not None:
            params["domain"] = domain
        if path is not None:
            params["path"] = path
        if partitionKey is not None:
            params["partitionKey"] = partitionKey
        return self.driver.execute_and_wait("Network.deleteCookies", params)

    def disable(self):
        """
        Disables network tracking, prevents network events from being sent to the client.
        """
        params = {}
        return self.driver.execute_and_wait("Network.disable", params)

    def emulateNetworkConditions(self, offline, latency, downloadThroughput, uploadThroughput, connectionType=None, packetLoss=None, packetQueueLength=None, packetReordering=None):
        """
        Activates emulation of network conditions. This command is deprecated in favor of the emulateNetworkConditionsByRule and overrideNetworkState commands, which can be used together to the same effect.
        - offline (boolean): True to emulate internet disconnection.
        - latency (number): Minimum latency from request sent to response headers received (ms).
        - downloadThroughput (number): Maximal aggregated download throughput (bytes/sec). -1 disables download throttling.
        - uploadThroughput (number): Maximal aggregated upload throughput (bytes/sec).  -1 disables upload throttling.
        - connectionType (any): Connection type if known.
        - packetLoss (number): WebRTC packet loss (percent, 0-100). 0 disables packet loss emulation, 100 drops all the packets.
        - packetQueueLength (integer): WebRTC packet queue length (packet). 0 removes any queue length limitations.
        - packetReordering (boolean): WebRTC packetReordering feature.
        """
        params = {}
        params["offline"] = offline
        params["latency"] = latency
        params["downloadThroughput"] = downloadThroughput
        params["uploadThroughput"] = uploadThroughput
        if connectionType is not None:
            params["connectionType"] = connectionType
        if packetLoss is not None:
            params["packetLoss"] = packetLoss
        if packetQueueLength is not None:
            params["packetQueueLength"] = packetQueueLength
        if packetReordering is not None:
            params["packetReordering"] = packetReordering
        return self.driver.execute_and_wait("Network.emulateNetworkConditions", params)

    def emulateNetworkConditionsByRule(self, offline, matchedNetworkConditions):
        """
        Activates emulation of network conditions for individual requests using URL match patterns. Unlike the deprecated Network.emulateNetworkConditions this method does not affect `navigator` state. Use Network.overrideNetworkState to explicitly modify `navigator` behavior.
        - offline (boolean): True to emulate internet disconnection.
        - matchedNetworkConditions (array): Configure conditions for matching requests. If multiple entries match a request, the first entry wins.  Global
conditions can be configured by leaving the urlPattern for the conditions empty. These global conditions are
also applied for throttling of p2p connections.
        """
        params = {}
        params["offline"] = offline
        params["matchedNetworkConditions"] = matchedNetworkConditions
        return self.driver.execute_and_wait("Network.emulateNetworkConditionsByRule", params)

    def overrideNetworkState(self, offline, latency, downloadThroughput, uploadThroughput, connectionType=None):
        """
        Override the state of navigator.onLine and navigator.connection.
        - offline (boolean): True to emulate internet disconnection.
        - latency (number): Minimum latency from request sent to response headers received (ms).
        - downloadThroughput (number): Maximal aggregated download throughput (bytes/sec). -1 disables download throttling.
        - uploadThroughput (number): Maximal aggregated upload throughput (bytes/sec).  -1 disables upload throttling.
        - connectionType (any): Connection type if known.
        """
        params = {}
        params["offline"] = offline
        params["latency"] = latency
        params["downloadThroughput"] = downloadThroughput
        params["uploadThroughput"] = uploadThroughput
        if connectionType is not None:
            params["connectionType"] = connectionType
        return self.driver.execute_and_wait("Network.overrideNetworkState", params)

    def enable(self, maxTotalBufferSize=None, maxResourceBufferSize=None, maxPostDataSize=None, reportDirectSocketTraffic=None, enableDurableMessages=None):
        """
        Enables network tracking, network events will now be delivered to the client.
        - maxTotalBufferSize (integer): Buffer size in bytes to use when preserving network payloads (XHRs, etc).
This is the maximum number of bytes that will be collected by this
DevTools session.
        - maxResourceBufferSize (integer): Per-resource buffer size in bytes to use when preserving network payloads (XHRs, etc).
        - maxPostDataSize (integer): Longest post body size (in bytes) that would be included in requestWillBeSent notification
        - reportDirectSocketTraffic (boolean): Whether DirectSocket chunk send/receive events should be reported.
        - enableDurableMessages (boolean): Enable storing response bodies outside of renderer, so that these survive
a cross-process navigation. Requires maxTotalBufferSize to be set.
Currently defaults to false. This field is being deprecated in favor of the dedicated
configureDurableMessages command, due to the possibility of deadlocks when awaiting
Network.enable before issuing Runtime.runIfWaitingForDebugger.
        """
        params = {}
        if maxTotalBufferSize is not None:
            params["maxTotalBufferSize"] = maxTotalBufferSize
        if maxResourceBufferSize is not None:
            params["maxResourceBufferSize"] = maxResourceBufferSize
        if maxPostDataSize is not None:
            params["maxPostDataSize"] = maxPostDataSize
        if reportDirectSocketTraffic is not None:
            params["reportDirectSocketTraffic"] = reportDirectSocketTraffic
        if enableDurableMessages is not None:
            params["enableDurableMessages"] = enableDurableMessages
        return self.driver.execute_and_wait("Network.enable", params)

    def configureDurableMessages(self, maxTotalBufferSize=None, maxResourceBufferSize=None):
        """
        Configures storing response bodies outside of renderer, so that these survive a cross-process navigation. If maxTotalBufferSize is not set, durable messages are disabled.
        - maxTotalBufferSize (integer): Buffer size in bytes to use when preserving network payloads (XHRs, etc).
        - maxResourceBufferSize (integer): Per-resource buffer size in bytes to use when preserving network payloads (XHRs, etc).
        """
        params = {}
        if maxTotalBufferSize is not None:
            params["maxTotalBufferSize"] = maxTotalBufferSize
        if maxResourceBufferSize is not None:
            params["maxResourceBufferSize"] = maxResourceBufferSize
        return self.driver.execute_and_wait("Network.configureDurableMessages", params)

    def getAllCookies(self):
        """
        Returns all browser cookies. Depending on the backend support, will return detailed cookie information in the `cookies` field. Deprecated. Use Storage.getCookies instead.
        """
        params = {}
        return self.driver.execute_and_wait("Network.getAllCookies", params)

    def getCertificate(self, origin):
        """
        Returns the DER-encoded certificate.
        - origin (string): Origin to get certificate for.
        """
        params = {}
        params["origin"] = origin
        return self.driver.execute_and_wait("Network.getCertificate", params)

    def getCookies(self, urls=None):
        """
        Returns all browser cookies for the current URL. Depending on the backend support, will return detailed cookie information in the `cookies` field.
        - urls (array): The list of URLs for which applicable cookies will be fetched.
If not specified, it's assumed to be set to the list containing
the URLs of the page and all of its subframes.
        """
        params = {}
        if urls is not None:
            params["urls"] = urls
        return self.driver.execute_and_wait("Network.getCookies", params)

    def getResponseBody(self, requestId):
        """
        Returns content served for the given request.
        - requestId (any): Identifier of the network request to get content for.
        """
        params = {}
        params["requestId"] = requestId
        return self.driver.execute_and_wait("Network.getResponseBody", params)

    def getRequestPostData(self, requestId):
        """
        Returns post data sent with the request. Returns an error when no data was sent with the request.
        - requestId (any): Identifier of the network request to get content for.
        """
        params = {}
        params["requestId"] = requestId
        return self.driver.execute_and_wait("Network.getRequestPostData", params)

    def getResponseBodyForInterception(self, interceptionId):
        """
        Returns content served for the given currently intercepted request.
        - interceptionId (any): Identifier for the intercepted request to get body for.
        """
        params = {}
        params["interceptionId"] = interceptionId
        return self.driver.execute_and_wait("Network.getResponseBodyForInterception", params)

    def takeResponseBodyForInterceptionAsStream(self, interceptionId):
        """
        Returns a handle to the stream representing the response body. Note that after this command, the intercepted request can't be continued as is -- you either need to cancel it or to provide the response body. The stream only supports sequential read, IO.read will fail if the position is specified.
        - interceptionId (any): 
        """
        params = {}
        params["interceptionId"] = interceptionId
        return self.driver.execute_and_wait("Network.takeResponseBodyForInterceptionAsStream", params)

    def replayXHR(self, requestId):
        """
        This method sends a new XMLHttpRequest which is identical to the original one. The following parameters should be identical: method, url, async, request body, extra headers, withCredentials attribute, user, password.
        - requestId (any): Identifier of XHR to replay.
        """
        params = {}
        params["requestId"] = requestId
        return self.driver.execute_and_wait("Network.replayXHR", params)

    def searchInResponseBody(self, requestId, query, caseSensitive=None, isRegex=None):
        """
        Searches for given string in response content.
        - requestId (any): Identifier of the network response to search.
        - query (string): String to search for.
        - caseSensitive (boolean): If true, search is case sensitive.
        - isRegex (boolean): If true, treats string parameter as regex.
        """
        params = {}
        params["requestId"] = requestId
        params["query"] = query
        if caseSensitive is not None:
            params["caseSensitive"] = caseSensitive
        if isRegex is not None:
            params["isRegex"] = isRegex
        return self.driver.execute_and_wait("Network.searchInResponseBody", params)

    def setBlockedURLs(self, urlPatterns=None, urls=None):
        """
        Blocks URLs from loading.
        - urlPatterns (array): Patterns to match in the order in which they are given. These patterns
also take precedence over any wildcard patterns defined in `urls`.
        - urls (array): URL patterns to block. Wildcards ('*') are allowed.
        """
        params = {}
        if urlPatterns is not None:
            params["urlPatterns"] = urlPatterns
        if urls is not None:
            params["urls"] = urls
        return self.driver.execute_and_wait("Network.setBlockedURLs", params)

    def setBypassServiceWorker(self, bypass):
        """
        Toggles ignoring of service worker for each request.
        - bypass (boolean): Bypass service worker and load from network.
        """
        params = {}
        params["bypass"] = bypass
        return self.driver.execute_and_wait("Network.setBypassServiceWorker", params)

    def setCacheDisabled(self, cacheDisabled):
        """
        Toggles ignoring cache for each request. If `true`, cache will not be used.
        - cacheDisabled (boolean): Cache disabled state.
        """
        params = {}
        params["cacheDisabled"] = cacheDisabled
        return self.driver.execute_and_wait("Network.setCacheDisabled", params)

    def setCookie(self, name, value, url=None, domain=None, path=None, secure=None, httpOnly=None, sameSite=None, expires=None, priority=None, sourceScheme=None, sourcePort=None, partitionKey=None):
        """
        Sets a cookie with the given cookie data; may overwrite equivalent cookies if they exist.
        - name (string): Cookie name.
        - value (string): Cookie value.
        - url (string): The request-URI to associate with the setting of the cookie. This value can affect the
default domain, path, source port, and source scheme values of the created cookie.
        - domain (string): Cookie domain.
        - path (string): Cookie path.
        - secure (boolean): True if cookie is secure.
        - httpOnly (boolean): True if cookie is http-only.
        - sameSite (any): Cookie SameSite type.
        - expires (any): Cookie expiration date, session cookie if not set
        - priority (any): Cookie Priority type.
        - sourceScheme (any): Cookie source scheme type.
        - sourcePort (integer): Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates an unspecified port.
An unspecified port value allows protocol clients to emulate legacy cookie scope for the port.
This is a temporary ability and it will be removed in the future.
        - partitionKey (any): Cookie partition key. If not set, the cookie will be set as not partitioned.
        """
        params = {}
        params["name"] = name
        params["value"] = value
        if url is not None:
            params["url"] = url
        if domain is not None:
            params["domain"] = domain
        if path is not None:
            params["path"] = path
        if secure is not None:
            params["secure"] = secure
        if httpOnly is not None:
            params["httpOnly"] = httpOnly
        if sameSite is not None:
            params["sameSite"] = sameSite
        if expires is not None:
            params["expires"] = expires
        if priority is not None:
            params["priority"] = priority
        if sourceScheme is not None:
            params["sourceScheme"] = sourceScheme
        if sourcePort is not None:
            params["sourcePort"] = sourcePort
        if partitionKey is not None:
            params["partitionKey"] = partitionKey
        return self.driver.execute_and_wait("Network.setCookie", params)

    def setCookies(self, cookies):
        """
        Sets given cookies.
        - cookies (array): Cookies to be set.
        """
        params = {}
        params["cookies"] = cookies
        return self.driver.execute_and_wait("Network.setCookies", params)

    def setExtraHTTPHeaders(self, headers):
        """
        Specifies whether to always send extra HTTP headers with the requests from this page.
        - headers (any): Map with extra HTTP headers.
        """
        params = {}
        params["headers"] = headers
        return self.driver.execute_and_wait("Network.setExtraHTTPHeaders", params)

    def setAttachDebugStack(self, enabled):
        """
        Specifies whether to attach a page script stack id in requests
        - enabled (boolean): Whether to attach a page script stack for debugging purpose.
        """
        params = {}
        params["enabled"] = enabled
        return self.driver.execute_and_wait("Network.setAttachDebugStack", params)

    def setRequestInterception(self, patterns):
        """
        Sets the requests to intercept that match the provided patterns and optionally resource types. Deprecated, please use Fetch.enable instead.
        - patterns (array): Requests matching any of these patterns will be forwarded and wait for the corresponding
continueInterceptedRequest call.
        """
        params = {}
        params["patterns"] = patterns
        return self.driver.execute_and_wait("Network.setRequestInterception", params)

    def setUserAgentOverride(self, userAgent, acceptLanguage=None, platform=None, userAgentMetadata=None):
        """
        Allows overriding user agent with the given string.
        - userAgent (string): User agent to use.
        - acceptLanguage (string): Browser language to emulate.
        - platform (string): The platform navigator.platform should return.
        - userAgentMetadata (any): To be sent in Sec-CH-UA-* headers and returned in navigator.userAgentData
        """
        params = {}
        params["userAgent"] = userAgent
        if acceptLanguage is not None:
            params["acceptLanguage"] = acceptLanguage
        if platform is not None:
            params["platform"] = platform
        if userAgentMetadata is not None:
            params["userAgentMetadata"] = userAgentMetadata
        return self.driver.execute_and_wait("Network.setUserAgentOverride", params)

    def streamResourceContent(self, requestId):
        """
        Enables streaming of the response for the given requestId. If enabled, the dataReceived event contains the data that was received during streaming.
        - requestId (any): Identifier of the request to stream.
        """
        params = {}
        params["requestId"] = requestId
        return self.driver.execute_and_wait("Network.streamResourceContent", params)

    def getSecurityIsolationStatus(self, frameId=None):
        """
        Returns information about the COEP/COOP isolation status.
        - frameId (any): If no frameId is provided, the status of the target is provided.
        """
        params = {}
        if frameId is not None:
            params["frameId"] = frameId
        return self.driver.execute_and_wait("Network.getSecurityIsolationStatus", params)

    def enableReportingApi(self, enable):
        """
        Enables tracking for the Reporting API, events generated by the Reporting API will now be delivered to the client. Enabling triggers 'reportingApiReportAdded' for all existing reports.
        - enable (boolean): Whether to enable or disable events for the Reporting API
        """
        params = {}
        params["enable"] = enable
        return self.driver.execute_and_wait("Network.enableReportingApi", params)

    def enableDeviceBoundSessions(self, enable):
        """
        Sets up tracking device bound sessions and fetching of initial set of sessions.
        - enable (boolean): Whether to enable or disable events.
        """
        params = {}
        params["enable"] = enable
        return self.driver.execute_and_wait("Network.enableDeviceBoundSessions", params)

    def fetchSchemefulSite(self, origin):
        """
        Fetches the schemeful site for a specific origin.
        - origin (string): The URL origin.
        """
        params = {}
        params["origin"] = origin
        return self.driver.execute_and_wait("Network.fetchSchemefulSite", params)

    def loadNetworkResource(self, url, options, frameId=None):
        """
        Fetches the resource and returns the content.
        - frameId (any): Frame id to get the resource for. Mandatory for frame targets, and
should be omitted for worker targets.
        - url (string): URL of the resource to get content for.
        - options (any): Options for the request.
        """
        params = {}
        if frameId is not None:
            params["frameId"] = frameId
        params["url"] = url
        params["options"] = options
        return self.driver.execute_and_wait("Network.loadNetworkResource", params)

    def setCookieControls(self, enableThirdPartyCookieRestriction, disableThirdPartyCookieMetadata, disableThirdPartyCookieHeuristics):
        """
        Sets Controls for third-party cookie access Page reload is required before the new cookie behavior will be observed
        - enableThirdPartyCookieRestriction (boolean): Whether 3pc restriction is enabled.
        - disableThirdPartyCookieMetadata (boolean): Whether 3pc grace period exception should be enabled; false by default.
        - disableThirdPartyCookieHeuristics (boolean): Whether 3pc heuristics exceptions should be enabled; false by default.
        """
        params = {}
        params["enableThirdPartyCookieRestriction"] = enableThirdPartyCookieRestriction
        params["disableThirdPartyCookieMetadata"] = disableThirdPartyCookieMetadata
        params["disableThirdPartyCookieHeuristics"] = disableThirdPartyCookieHeuristics
        return self.driver.execute_and_wait("Network.setCookieControls", params)

