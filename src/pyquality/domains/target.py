class TargetDomain:
    def __init__(self, driver):
        self.driver = driver

    def activateTarget(self, targetId):
        """
        Activates (focuses) the target.
        - targetId (any): 
        """
        params = {}
        params["targetId"] = targetId
        return self.driver.execute_and_wait("Target.activateTarget", params)

    def attachToTarget(self, targetId, flatten=None):
        """
        Attaches to the target with given id.
        - targetId (any): 
        - flatten (boolean): Enables "flat" access to the session via specifying sessionId attribute in the commands.
We plan to make this the default, deprecate non-flattened mode,
and eventually retire it. See crbug.com/991325.
        """
        params = {}
        params["targetId"] = targetId
        if flatten is not None:
            params["flatten"] = flatten
        return self.driver.execute_and_wait("Target.attachToTarget", params)

    def attachToBrowserTarget(self):
        """
        Attaches to the browser target, only uses flat sessionId mode.
        """
        params = {}
        return self.driver.execute_and_wait("Target.attachToBrowserTarget", params)

    def closeTarget(self, targetId):
        """
        Closes the target. If the target is a page that gets closed too.
        - targetId (any): 
        """
        params = {}
        params["targetId"] = targetId
        return self.driver.execute_and_wait("Target.closeTarget", params)

    def exposeDevToolsProtocol(self, targetId, bindingName=None, inheritPermissions=None):
        """
        Inject object to the target's main frame that provides a communication channel with browser target.  Injected object will be available as `window[bindingName]`.  The object has the following API: - `binding.send(json)` - a method to send messages over the remote debugging protocol - `binding.onmessage = json => handleMessage(json)` - a callback that will be called for the protocol notifications and command responses.
        - targetId (any): 
        - bindingName (string): Binding name, 'cdp' if not specified.
        - inheritPermissions (boolean): If true, inherits the current root session's permissions (default: false).
        """
        params = {}
        params["targetId"] = targetId
        if bindingName is not None:
            params["bindingName"] = bindingName
        if inheritPermissions is not None:
            params["inheritPermissions"] = inheritPermissions
        return self.driver.execute_and_wait("Target.exposeDevToolsProtocol", params)

    def createBrowserContext(self, disposeOnDetach=None, proxyServer=None, proxyBypassList=None, originsWithUniversalNetworkAccess=None):
        """
        Creates a new empty BrowserContext. Similar to an incognito profile but you can have more than one.
        - disposeOnDetach (boolean): If specified, disposes this context when debugging session disconnects.
        - proxyServer (string): Proxy server, similar to the one passed to --proxy-server
        - proxyBypassList (string): Proxy bypass list, similar to the one passed to --proxy-bypass-list
        - originsWithUniversalNetworkAccess (array): An optional list of origins to grant unlimited cross-origin access to.
Parts of the URL other than those constituting origin are ignored.
        """
        params = {}
        if disposeOnDetach is not None:
            params["disposeOnDetach"] = disposeOnDetach
        if proxyServer is not None:
            params["proxyServer"] = proxyServer
        if proxyBypassList is not None:
            params["proxyBypassList"] = proxyBypassList
        if originsWithUniversalNetworkAccess is not None:
            params["originsWithUniversalNetworkAccess"] = originsWithUniversalNetworkAccess
        return self.driver.execute_and_wait("Target.createBrowserContext", params)

    def getBrowserContexts(self):
        """
        Returns all browser contexts created with `Target.createBrowserContext` method.
        """
        params = {}
        return self.driver.execute_and_wait("Target.getBrowserContexts", params)

    def createTarget(self, url, left=None, top=None, width=None, height=None, windowState=None, browserContextId=None, enableBeginFrameControl=None, newWindow=None, background=None, forTab=None, hidden=None, focus=None):
        """
        Creates a new page.
        - url (string): The initial URL the page will be navigated to. An empty string indicates about:blank.
        - left (integer): Frame left origin in DIP (requires newWindow to be true or headless shell).
        - top (integer): Frame top origin in DIP (requires newWindow to be true or headless shell).
        - width (integer): Frame width in DIP (requires newWindow to be true or headless shell).
        - height (integer): Frame height in DIP (requires newWindow to be true or headless shell).
        - windowState (any): Frame window state (requires newWindow to be true or headless shell).
Default is normal.
        - browserContextId (any): The browser context to create the page in.
        - enableBeginFrameControl (boolean): Whether BeginFrames for this target will be controlled via DevTools (headless shell only,
not supported on MacOS yet, false by default).
        - newWindow (boolean): Whether to create a new Window or Tab (false by default, not supported by headless shell).
        - background (boolean): Whether to create the target in background or foreground (false by default, not supported
by headless shell).
        - forTab (boolean): Whether to create the target of type "tab".
        - hidden (boolean): Whether to create a hidden target. The hidden target is observable via protocol, but not
present in the tab UI strip. Cannot be created with `forTab: true`, `newWindow: true` or
`background: false`. The life-time of the tab is limited to the life-time of the session.
        - focus (boolean): If specified, the option is used to determine if the new target should
be focused or not. By default, the focus behavior depends on the
value of the background field. For example, background=false and focus=false
will result in the target tab being opened but the browser window remain
unchanged (if it was in the background, it will remain in the background)
and background=false with focus=undefined will result in the window being focused.
Using background: true and focus: true is not supported and will result in an error.
        """
        params = {}
        params["url"] = url
        if left is not None:
            params["left"] = left
        if top is not None:
            params["top"] = top
        if width is not None:
            params["width"] = width
        if height is not None:
            params["height"] = height
        if windowState is not None:
            params["windowState"] = windowState
        if browserContextId is not None:
            params["browserContextId"] = browserContextId
        if enableBeginFrameControl is not None:
            params["enableBeginFrameControl"] = enableBeginFrameControl
        if newWindow is not None:
            params["newWindow"] = newWindow
        if background is not None:
            params["background"] = background
        if forTab is not None:
            params["forTab"] = forTab
        if hidden is not None:
            params["hidden"] = hidden
        if focus is not None:
            params["focus"] = focus
        return self.driver.execute_and_wait("Target.createTarget", params)

    def detachFromTarget(self, sessionId=None, targetId=None):
        """
        Detaches session with given id.
        - sessionId (any): Session to detach.
        - targetId (any): Deprecated.
        """
        params = {}
        if sessionId is not None:
            params["sessionId"] = sessionId
        if targetId is not None:
            params["targetId"] = targetId
        return self.driver.execute_and_wait("Target.detachFromTarget", params)

    def disposeBrowserContext(self, browserContextId):
        """
        Deletes a BrowserContext. All the belonging pages will be closed without calling their beforeunload hooks.
        - browserContextId (any): 
        """
        params = {}
        params["browserContextId"] = browserContextId
        return self.driver.execute_and_wait("Target.disposeBrowserContext", params)

    def getTargetInfo(self, targetId=None):
        """
        Returns information about a target.
        - targetId (any): 
        """
        params = {}
        if targetId is not None:
            params["targetId"] = targetId
        return self.driver.execute_and_wait("Target.getTargetInfo", params)

    def getTargets(self, filter=None):
        """
        Retrieves a list of available targets.
        - filter (any): Only targets matching filter will be reported. If filter is not specified
and target discovery is currently enabled, a filter used for target discovery
is used for consistency.
        """
        params = {}
        if filter is not None:
            params["filter"] = filter
        return self.driver.execute_and_wait("Target.getTargets", params)

    def sendMessageToTarget(self, message, sessionId=None, targetId=None):
        """
        Sends protocol message over session with given id. Consider using flat mode instead; see commands attachToTarget, setAutoAttach, and crbug.com/991325.
        - message (string): 
        - sessionId (any): Identifier of the session.
        - targetId (any): Deprecated.
        """
        params = {}
        params["message"] = message
        if sessionId is not None:
            params["sessionId"] = sessionId
        if targetId is not None:
            params["targetId"] = targetId
        return self.driver.execute_and_wait("Target.sendMessageToTarget", params)

    def setAutoAttach(self, autoAttach, waitForDebuggerOnStart, flatten=None, filter=None):
        """
        Controls whether to automatically attach to new targets which are considered to be directly related to this one (for example, iframes or workers). When turned on, attaches to all existing related targets as well. When turned off, automatically detaches from all currently attached targets. This also clears all targets added by `autoAttachRelated` from the list of targets to watch for creation of related targets. You might want to call this recursively for auto-attached targets to attach to all available targets.
        - autoAttach (boolean): Whether to auto-attach to related targets.
        - waitForDebuggerOnStart (boolean): Whether to pause new targets when attaching to them. Use `Runtime.runIfWaitingForDebugger`
to run paused targets.
        - flatten (boolean): Enables "flat" access to the session via specifying sessionId attribute in the commands.
We plan to make this the default, deprecate non-flattened mode,
and eventually retire it. See crbug.com/991325.
        - filter (any): Only targets matching filter will be attached.
        """
        params = {}
        params["autoAttach"] = autoAttach
        params["waitForDebuggerOnStart"] = waitForDebuggerOnStart
        if flatten is not None:
            params["flatten"] = flatten
        if filter is not None:
            params["filter"] = filter
        return self.driver.execute_and_wait("Target.setAutoAttach", params)

    def autoAttachRelated(self, targetId, waitForDebuggerOnStart, filter=None):
        """
        Adds the specified target to the list of targets that will be monitored for any related target creation (such as child frames, child workers and new versions of service worker) and reported through `attachedToTarget`. The specified target is also auto-attached. This cancels the effect of any previous `setAutoAttach` and is also cancelled by subsequent `setAutoAttach`. Only available at the Browser target.
        - targetId (any): 
        - waitForDebuggerOnStart (boolean): Whether to pause new targets when attaching to them. Use `Runtime.runIfWaitingForDebugger`
to run paused targets.
        - filter (any): Only targets matching filter will be attached.
        """
        params = {}
        params["targetId"] = targetId
        params["waitForDebuggerOnStart"] = waitForDebuggerOnStart
        if filter is not None:
            params["filter"] = filter
        return self.driver.execute_and_wait("Target.autoAttachRelated", params)

    def setDiscoverTargets(self, discover, filter=None):
        """
        Controls whether to discover available targets and notify via `targetCreated/targetInfoChanged/targetDestroyed` events.
        - discover (boolean): Whether to discover available targets.
        - filter (any): Only targets matching filter will be attached. If `discover` is false,
`filter` must be omitted or empty.
        """
        params = {}
        params["discover"] = discover
        if filter is not None:
            params["filter"] = filter
        return self.driver.execute_and_wait("Target.setDiscoverTargets", params)

    def setRemoteLocations(self, locations):
        """
        Enables target discovery for the specified locations, when `setDiscoverTargets` was set to `true`.
        - locations (array): List of remote locations.
        """
        params = {}
        params["locations"] = locations
        return self.driver.execute_and_wait("Target.setRemoteLocations", params)

    def getDevToolsTarget(self, targetId):
        """
        Gets the targetId of the DevTools page target opened for the given target (if any).
        - targetId (any): Page or tab target ID.
        """
        params = {}
        params["targetId"] = targetId
        return self.driver.execute_and_wait("Target.getDevToolsTarget", params)

    def openDevTools(self, targetId, panelId=None):
        """
        Opens a DevTools window for the target.
        - targetId (any): This can be the page or tab target ID.
        - panelId (string): The id of the panel we want DevTools to open initially. Currently
supported panels are elements, console, network, sources, resources
and performance.
        """
        params = {}
        params["targetId"] = targetId
        if panelId is not None:
            params["panelId"] = panelId
        return self.driver.execute_and_wait("Target.openDevTools", params)

