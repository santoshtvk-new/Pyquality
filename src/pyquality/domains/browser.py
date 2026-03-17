class BrowserDomain:
    def __init__(self, driver):
        self.driver = driver

    def setPermission(self, permission, setting, origin=None, embeddedOrigin=None, browserContextId=None):
        """
        Set permission settings for given embedding and embedded origins.
        - permission (any): Descriptor of permission to override.
        - setting (any): Setting of the permission.
        - origin (string): Embedding origin the permission applies to, all origins if not specified.
        - embeddedOrigin (string): Embedded origin the permission applies to. It is ignored unless the embedding origin is
present and valid. If the embedding origin is provided but the embedded origin isn't, the
embedding origin is used as the embedded origin.
        - browserContextId (any): Context to override. When omitted, default browser context is used.
        """
        params = {}
        params["permission"] = permission
        params["setting"] = setting
        if origin is not None:
            params["origin"] = origin
        if embeddedOrigin is not None:
            params["embeddedOrigin"] = embeddedOrigin
        if browserContextId is not None:
            params["browserContextId"] = browserContextId
        return self.driver.execute_and_wait("Browser.setPermission", params)

    def grantPermissions(self, permissions, origin=None, browserContextId=None):
        """
        Grant specific permissions to the given origin and reject all others. Deprecated. Use setPermission instead.
        - permissions (array): 
        - origin (string): Origin the permission applies to, all origins if not specified.
        - browserContextId (any): BrowserContext to override permissions. When omitted, default browser context is used.
        """
        params = {}
        params["permissions"] = permissions
        if origin is not None:
            params["origin"] = origin
        if browserContextId is not None:
            params["browserContextId"] = browserContextId
        return self.driver.execute_and_wait("Browser.grantPermissions", params)

    def resetPermissions(self, browserContextId=None):
        """
        Reset all permission management for all origins.
        - browserContextId (any): BrowserContext to reset permissions. When omitted, default browser context is used.
        """
        params = {}
        if browserContextId is not None:
            params["browserContextId"] = browserContextId
        return self.driver.execute_and_wait("Browser.resetPermissions", params)

    def setDownloadBehavior(self, behavior, browserContextId=None, downloadPath=None, eventsEnabled=None):
        """
        Set the behavior when downloading a file.
        - behavior (string): Whether to allow all or deny all download requests, or use default Chrome behavior if
available (otherwise deny). |allowAndName| allows download and names files according to
their download guids.
        - browserContextId (any): BrowserContext to set download behavior. When omitted, default browser context is used.
        - downloadPath (string): The default path to save downloaded files to. This is required if behavior is set to 'allow'
or 'allowAndName'.
        - eventsEnabled (boolean): Whether to emit download events (defaults to false).
        """
        params = {}
        params["behavior"] = behavior
        if browserContextId is not None:
            params["browserContextId"] = browserContextId
        if downloadPath is not None:
            params["downloadPath"] = downloadPath
        if eventsEnabled is not None:
            params["eventsEnabled"] = eventsEnabled
        return self.driver.execute_and_wait("Browser.setDownloadBehavior", params)

    def cancelDownload(self, guid, browserContextId=None):
        """
        Cancel a download if in progress
        - guid (string): Global unique identifier of the download.
        - browserContextId (any): BrowserContext to perform the action in. When omitted, default browser context is used.
        """
        params = {}
        params["guid"] = guid
        if browserContextId is not None:
            params["browserContextId"] = browserContextId
        return self.driver.execute_and_wait("Browser.cancelDownload", params)

    def close(self):
        """
        Close browser gracefully.
        """
        params = {}
        return self.driver.execute_and_wait("Browser.close", params)

    def crash(self):
        """
        Crashes browser on the main thread.
        """
        params = {}
        return self.driver.execute_and_wait("Browser.crash", params)

    def crashGpuProcess(self):
        """
        Crashes GPU process.
        """
        params = {}
        return self.driver.execute_and_wait("Browser.crashGpuProcess", params)

    def getVersion(self):
        """
        Returns version information.
        """
        params = {}
        return self.driver.execute_and_wait("Browser.getVersion", params)

    def getBrowserCommandLine(self):
        """
        Returns the command line switches for the browser process if, and only if --enable-automation is on the commandline.
        """
        params = {}
        return self.driver.execute_and_wait("Browser.getBrowserCommandLine", params)

    def getHistograms(self, query=None, delta=None):
        """
        Get Chrome histograms.
        - query (string): Requested substring in name. Only histograms which have query as a
substring in their name are extracted. An empty or absent query returns
all histograms.
        - delta (boolean): If true, retrieve delta since last delta call.
        """
        params = {}
        if query is not None:
            params["query"] = query
        if delta is not None:
            params["delta"] = delta
        return self.driver.execute_and_wait("Browser.getHistograms", params)

    def getHistogram(self, name, delta=None):
        """
        Get a Chrome histogram by name.
        - name (string): Requested histogram name.
        - delta (boolean): If true, retrieve delta since last delta call.
        """
        params = {}
        params["name"] = name
        if delta is not None:
            params["delta"] = delta
        return self.driver.execute_and_wait("Browser.getHistogram", params)

    def getWindowBounds(self, windowId):
        """
        Get position and size of the browser window.
        - windowId (any): Browser window id.
        """
        params = {}
        params["windowId"] = windowId
        return self.driver.execute_and_wait("Browser.getWindowBounds", params)

    def getWindowForTarget(self, targetId=None):
        """
        Get the browser window that contains the devtools target.
        - targetId (any): Devtools agent host id. If called as a part of the session, associated targetId is used.
        """
        params = {}
        if targetId is not None:
            params["targetId"] = targetId
        return self.driver.execute_and_wait("Browser.getWindowForTarget", params)

    def setWindowBounds(self, windowId, bounds):
        """
        Set position and/or size of the browser window.
        - windowId (any): Browser window id.
        - bounds (any): New window bounds. The 'minimized', 'maximized' and 'fullscreen' states cannot be combined
with 'left', 'top', 'width' or 'height'. Leaves unspecified fields unchanged.
        """
        params = {}
        params["windowId"] = windowId
        params["bounds"] = bounds
        return self.driver.execute_and_wait("Browser.setWindowBounds", params)

    def setContentsSize(self, windowId, width=None, height=None):
        """
        Set size of the browser contents resizing browser window as necessary.
        - windowId (any): Browser window id.
        - width (integer): The window contents width in DIP. Assumes current width if omitted.
Must be specified if 'height' is omitted.
        - height (integer): The window contents height in DIP. Assumes current height if omitted.
Must be specified if 'width' is omitted.
        """
        params = {}
        params["windowId"] = windowId
        if width is not None:
            params["width"] = width
        if height is not None:
            params["height"] = height
        return self.driver.execute_and_wait("Browser.setContentsSize", params)

    def setDockTile(self, badgeLabel=None, image=None):
        """
        Set dock tile details, platform-specific.
        - badgeLabel (string): 
        - image (string): Png encoded image. (Encoded as a base64 string when passed over JSON)
        """
        params = {}
        if badgeLabel is not None:
            params["badgeLabel"] = badgeLabel
        if image is not None:
            params["image"] = image
        return self.driver.execute_and_wait("Browser.setDockTile", params)

    def executeBrowserCommand(self, commandId):
        """
        Invoke custom browser commands used by telemetry.
        - commandId (any): 
        """
        params = {}
        params["commandId"] = commandId
        return self.driver.execute_and_wait("Browser.executeBrowserCommand", params)

    def addPrivacySandboxEnrollmentOverride(self, url):
        """
        Allows a site to use privacy sandbox features that require enrollment without the site actually being enrolled. Only supported on page targets.
        - url (string): 
        """
        params = {}
        params["url"] = url
        return self.driver.execute_and_wait("Browser.addPrivacySandboxEnrollmentOverride", params)

    def addPrivacySandboxCoordinatorKeyConfig(self, api, coordinatorOrigin, keyConfig, browserContextId=None):
        """
        Configures encryption keys used with a given privacy sandbox API to talk to a trusted coordinator.  Since this is intended for test automation only, coordinatorOrigin must be a .test domain. No existing coordinator configuration for the origin may exist.
        - api (any): 
        - coordinatorOrigin (string): 
        - keyConfig (string): 
        - browserContextId (any): BrowserContext to perform the action in. When omitted, default browser
context is used.
        """
        params = {}
        params["api"] = api
        params["coordinatorOrigin"] = coordinatorOrigin
        params["keyConfig"] = keyConfig
        if browserContextId is not None:
            params["browserContextId"] = browserContextId
        return self.driver.execute_and_wait("Browser.addPrivacySandboxCoordinatorKeyConfig", params)

