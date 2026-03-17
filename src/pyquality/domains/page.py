class PageDomain:
    def __init__(self, driver):
        self.driver = driver

    def addScriptToEvaluateOnLoad(self, scriptSource):
        """
        Deprecated, please use addScriptToEvaluateOnNewDocument instead.
        - scriptSource (string): 
        """
        params = {}
        params["scriptSource"] = scriptSource
        return self.driver.execute_and_wait("Page.addScriptToEvaluateOnLoad", params)

    def addScriptToEvaluateOnNewDocument(self, source, worldName=None, includeCommandLineAPI=None, runImmediately=None):
        """
        Evaluates given script in every frame upon creation (before loading frame's scripts).
        - source (string): 
        - worldName (string): If specified, creates an isolated world with the given name and evaluates given script in it.
This world name will be used as the ExecutionContextDescription::name when the corresponding
event is emitted.
        - includeCommandLineAPI (boolean): Specifies whether command line API should be available to the script, defaults
to false.
        - runImmediately (boolean): If true, runs the script immediately on existing execution contexts or worlds.
Default: false.
        """
        params = {}
        params["source"] = source
        if worldName is not None:
            params["worldName"] = worldName
        if includeCommandLineAPI is not None:
            params["includeCommandLineAPI"] = includeCommandLineAPI
        if runImmediately is not None:
            params["runImmediately"] = runImmediately
        return self.driver.execute_and_wait("Page.addScriptToEvaluateOnNewDocument", params)

    def bringToFront(self):
        """
        Brings page to front (activates tab).
        """
        params = {}
        return self.driver.execute_and_wait("Page.bringToFront", params)

    def captureScreenshot(self, format=None, quality=None, clip=None, fromSurface=None, captureBeyondViewport=None, optimizeForSpeed=None):
        """
        Capture page screenshot.
        - format (string): Image compression format (defaults to png).
        - quality (integer): Compression quality from range [0..100] (jpeg only).
        - clip (any): Capture the screenshot of a given region only.
        - fromSurface (boolean): Capture the screenshot from the surface, rather than the view. Defaults to true.
        - captureBeyondViewport (boolean): Capture the screenshot beyond the viewport. Defaults to false.
        - optimizeForSpeed (boolean): Optimize image encoding for speed, not for resulting size (defaults to false)
        """
        params = {}
        if format is not None:
            params["format"] = format
        if quality is not None:
            params["quality"] = quality
        if clip is not None:
            params["clip"] = clip
        if fromSurface is not None:
            params["fromSurface"] = fromSurface
        if captureBeyondViewport is not None:
            params["captureBeyondViewport"] = captureBeyondViewport
        if optimizeForSpeed is not None:
            params["optimizeForSpeed"] = optimizeForSpeed
        return self.driver.execute_and_wait("Page.captureScreenshot", params)

    def captureSnapshot(self, format=None):
        """
        Returns a snapshot of the page as a string. For MHTML format, the serialization includes iframes, shadow DOM, external resources, and element-inline styles.
        - format (string): Format (defaults to mhtml).
        """
        params = {}
        if format is not None:
            params["format"] = format
        return self.driver.execute_and_wait("Page.captureSnapshot", params)

    def clearDeviceMetricsOverride(self):
        """
        Clears the overridden device metrics.
        """
        params = {}
        return self.driver.execute_and_wait("Page.clearDeviceMetricsOverride", params)

    def clearDeviceOrientationOverride(self):
        """
        Clears the overridden Device Orientation.
        """
        params = {}
        return self.driver.execute_and_wait("Page.clearDeviceOrientationOverride", params)

    def clearGeolocationOverride(self):
        """
        Clears the overridden Geolocation Position and Error.
        """
        params = {}
        return self.driver.execute_and_wait("Page.clearGeolocationOverride", params)

    def createIsolatedWorld(self, frameId, worldName=None, grantUniveralAccess=None):
        """
        Creates an isolated world for the given frame.
        - frameId (any): Id of the frame in which the isolated world should be created.
        - worldName (string): An optional name which is reported in the Execution Context.
        - grantUniveralAccess (boolean): Whether or not universal access should be granted to the isolated world. This is a powerful
option, use with caution.
        """
        params = {}
        params["frameId"] = frameId
        if worldName is not None:
            params["worldName"] = worldName
        if grantUniveralAccess is not None:
            params["grantUniveralAccess"] = grantUniveralAccess
        return self.driver.execute_and_wait("Page.createIsolatedWorld", params)

    def deleteCookie(self, cookieName, url):
        """
        Deletes browser cookie with given name, domain and path.
        - cookieName (string): Name of the cookie to remove.
        - url (string): URL to match cooke domain and path.
        """
        params = {}
        params["cookieName"] = cookieName
        params["url"] = url
        return self.driver.execute_and_wait("Page.deleteCookie", params)

    def disable(self):
        """
        Disables page domain notifications.
        """
        params = {}
        return self.driver.execute_and_wait("Page.disable", params)

    def enable(self, enableFileChooserOpenedEvent=None):
        """
        Enables page domain notifications.
        - enableFileChooserOpenedEvent (boolean): If true, the `Page.fileChooserOpened` event will be emitted regardless of the state set by
`Page.setInterceptFileChooserDialog` command (default: false).
        """
        params = {}
        if enableFileChooserOpenedEvent is not None:
            params["enableFileChooserOpenedEvent"] = enableFileChooserOpenedEvent
        return self.driver.execute_and_wait("Page.enable", params)

    def getAppManifest(self, manifestId=None):
        """
        Gets the processed manifest for this current document.   This API always waits for the manifest to be loaded.   If manifestId is provided, and it does not match the manifest of the     current document, this API errors out.   If there is not a loaded page, this API errors out immediately.
        - manifestId (string): 
        """
        params = {}
        if manifestId is not None:
            params["manifestId"] = manifestId
        return self.driver.execute_and_wait("Page.getAppManifest", params)

    def getInstallabilityErrors(self):
        """
        Call Page.getInstallabilityErrors
        """
        params = {}
        return self.driver.execute_and_wait("Page.getInstallabilityErrors", params)

    def getManifestIcons(self):
        """
        Deprecated because it's not guaranteed that the returned icon is in fact the one used for PWA installation.
        """
        params = {}
        return self.driver.execute_and_wait("Page.getManifestIcons", params)

    def getAppId(self):
        """
        Returns the unique (PWA) app id. Only returns values if the feature flag 'WebAppEnableManifestId' is enabled
        """
        params = {}
        return self.driver.execute_and_wait("Page.getAppId", params)

    def getAdScriptAncestry(self, frameId):
        """
        Call Page.getAdScriptAncestry
        - frameId (any): 
        """
        params = {}
        params["frameId"] = frameId
        return self.driver.execute_and_wait("Page.getAdScriptAncestry", params)

    def getFrameTree(self):
        """
        Returns present frame tree structure.
        """
        params = {}
        return self.driver.execute_and_wait("Page.getFrameTree", params)

    def getLayoutMetrics(self):
        """
        Returns metrics relating to the layouting of the page, such as viewport bounds/scale.
        """
        params = {}
        return self.driver.execute_and_wait("Page.getLayoutMetrics", params)

    def getNavigationHistory(self):
        """
        Returns navigation history for the current page.
        """
        params = {}
        return self.driver.execute_and_wait("Page.getNavigationHistory", params)

    def resetNavigationHistory(self):
        """
        Resets navigation history for the current page.
        """
        params = {}
        return self.driver.execute_and_wait("Page.resetNavigationHistory", params)

    def getResourceContent(self, frameId, url):
        """
        Returns content of the given resource.
        - frameId (any): Frame id to get resource for.
        - url (string): URL of the resource to get content for.
        """
        params = {}
        params["frameId"] = frameId
        params["url"] = url
        return self.driver.execute_and_wait("Page.getResourceContent", params)

    def getResourceTree(self):
        """
        Returns present frame / resource tree structure.
        """
        params = {}
        return self.driver.execute_and_wait("Page.getResourceTree", params)

    def handleJavaScriptDialog(self, accept, promptText=None):
        """
        Accepts or dismisses a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload).
        - accept (boolean): Whether to accept or dismiss the dialog.
        - promptText (string): The text to enter into the dialog prompt before accepting. Used only if this is a prompt
dialog.
        """
        params = {}
        params["accept"] = accept
        if promptText is not None:
            params["promptText"] = promptText
        return self.driver.execute_and_wait("Page.handleJavaScriptDialog", params)

    def navigate(self, url, referrer=None, transitionType=None, frameId=None, referrerPolicy=None):
        """
        Navigates current page to the given URL.
        - url (string): URL to navigate the page to.
        - referrer (string): Referrer URL.
        - transitionType (any): Intended transition type.
        - frameId (any): Frame id to navigate, if not specified navigates the top frame.
        - referrerPolicy (any): Referrer-policy used for the navigation.
        """
        params = {}
        params["url"] = url
        if referrer is not None:
            params["referrer"] = referrer
        if transitionType is not None:
            params["transitionType"] = transitionType
        if frameId is not None:
            params["frameId"] = frameId
        if referrerPolicy is not None:
            params["referrerPolicy"] = referrerPolicy
        return self.driver.execute_and_wait("Page.navigate", params)

    def navigateToHistoryEntry(self, entryId):
        """
        Navigates current page to the given history entry.
        - entryId (integer): Unique id of the entry to navigate to.
        """
        params = {}
        params["entryId"] = entryId
        return self.driver.execute_and_wait("Page.navigateToHistoryEntry", params)

    def printToPDF(self, landscape=None, displayHeaderFooter=None, printBackground=None, scale=None, paperWidth=None, paperHeight=None, marginTop=None, marginBottom=None, marginLeft=None, marginRight=None, pageRanges=None, headerTemplate=None, footerTemplate=None, preferCSSPageSize=None, transferMode=None, generateTaggedPDF=None, generateDocumentOutline=None):
        """
        Print page as PDF.
        - landscape (boolean): Paper orientation. Defaults to false.
        - displayHeaderFooter (boolean): Display header and footer. Defaults to false.
        - printBackground (boolean): Print background graphics. Defaults to false.
        - scale (number): Scale of the webpage rendering. Defaults to 1.
        - paperWidth (number): Paper width in inches. Defaults to 8.5 inches.
        - paperHeight (number): Paper height in inches. Defaults to 11 inches.
        - marginTop (number): Top margin in inches. Defaults to 1cm (~0.4 inches).
        - marginBottom (number): Bottom margin in inches. Defaults to 1cm (~0.4 inches).
        - marginLeft (number): Left margin in inches. Defaults to 1cm (~0.4 inches).
        - marginRight (number): Right margin in inches. Defaults to 1cm (~0.4 inches).
        - pageRanges (string): Paper ranges to print, one based, e.g., '1-5, 8, 11-13'. Pages are
printed in the document order, not in the order specified, and no
more than once.
Defaults to empty string, which implies the entire document is printed.
The page numbers are quietly capped to actual page count of the
document, and ranges beyond the end of the document are ignored.
If this results in no pages to print, an error is reported.
It is an error to specify a range with start greater than end.
        - headerTemplate (string): HTML template for the print header. Should be valid HTML markup with following
classes used to inject printing values into them:
- `date`: formatted print date
- `title`: document title
- `url`: document location
- `pageNumber`: current page number
- `totalPages`: total pages in the document

For example, `<span class=title></span>` would generate span containing the title.
        - footerTemplate (string): HTML template for the print footer. Should use the same format as the `headerTemplate`.
        - preferCSSPageSize (boolean): Whether or not to prefer page size as defined by css. Defaults to false,
in which case the content will be scaled to fit the paper size.
        - transferMode (string): return as stream
        - generateTaggedPDF (boolean): Whether or not to generate tagged (accessible) PDF. Defaults to embedder choice.
        - generateDocumentOutline (boolean): Whether or not to embed the document outline into the PDF.
        """
        params = {}
        if landscape is not None:
            params["landscape"] = landscape
        if displayHeaderFooter is not None:
            params["displayHeaderFooter"] = displayHeaderFooter
        if printBackground is not None:
            params["printBackground"] = printBackground
        if scale is not None:
            params["scale"] = scale
        if paperWidth is not None:
            params["paperWidth"] = paperWidth
        if paperHeight is not None:
            params["paperHeight"] = paperHeight
        if marginTop is not None:
            params["marginTop"] = marginTop
        if marginBottom is not None:
            params["marginBottom"] = marginBottom
        if marginLeft is not None:
            params["marginLeft"] = marginLeft
        if marginRight is not None:
            params["marginRight"] = marginRight
        if pageRanges is not None:
            params["pageRanges"] = pageRanges
        if headerTemplate is not None:
            params["headerTemplate"] = headerTemplate
        if footerTemplate is not None:
            params["footerTemplate"] = footerTemplate
        if preferCSSPageSize is not None:
            params["preferCSSPageSize"] = preferCSSPageSize
        if transferMode is not None:
            params["transferMode"] = transferMode
        if generateTaggedPDF is not None:
            params["generateTaggedPDF"] = generateTaggedPDF
        if generateDocumentOutline is not None:
            params["generateDocumentOutline"] = generateDocumentOutline
        return self.driver.execute_and_wait("Page.printToPDF", params)

    def reload(self, ignoreCache=None, scriptToEvaluateOnLoad=None, loaderId=None):
        """
        Reloads given page optionally ignoring the cache.
        - ignoreCache (boolean): If true, browser cache is ignored (as if the user pressed Shift+refresh).
        - scriptToEvaluateOnLoad (string): If set, the script will be injected into all frames of the inspected page after reload.
Argument will be ignored if reloading dataURL origin.
        - loaderId (any): If set, an error will be thrown if the target page's main frame's
loader id does not match the provided id. This prevents accidentally
reloading an unintended target in case there's a racing navigation.
        """
        params = {}
        if ignoreCache is not None:
            params["ignoreCache"] = ignoreCache
        if scriptToEvaluateOnLoad is not None:
            params["scriptToEvaluateOnLoad"] = scriptToEvaluateOnLoad
        if loaderId is not None:
            params["loaderId"] = loaderId
        return self.driver.execute_and_wait("Page.reload", params)

    def removeScriptToEvaluateOnLoad(self, identifier):
        """
        Deprecated, please use removeScriptToEvaluateOnNewDocument instead.
        - identifier (any): 
        """
        params = {}
        params["identifier"] = identifier
        return self.driver.execute_and_wait("Page.removeScriptToEvaluateOnLoad", params)

    def removeScriptToEvaluateOnNewDocument(self, identifier):
        """
        Removes given script from the list.
        - identifier (any): 
        """
        params = {}
        params["identifier"] = identifier
        return self.driver.execute_and_wait("Page.removeScriptToEvaluateOnNewDocument", params)

    def screencastFrameAck(self, sessionId):
        """
        Acknowledges that a screencast frame has been received by the frontend.
        - sessionId (integer): Frame number.
        """
        params = {}
        params["sessionId"] = sessionId
        return self.driver.execute_and_wait("Page.screencastFrameAck", params)

    def searchInResource(self, frameId, url, query, caseSensitive=None, isRegex=None):
        """
        Searches for given string in resource content.
        - frameId (any): Frame id for resource to search in.
        - url (string): URL of the resource to search in.
        - query (string): String to search for.
        - caseSensitive (boolean): If true, search is case sensitive.
        - isRegex (boolean): If true, treats string parameter as regex.
        """
        params = {}
        params["frameId"] = frameId
        params["url"] = url
        params["query"] = query
        if caseSensitive is not None:
            params["caseSensitive"] = caseSensitive
        if isRegex is not None:
            params["isRegex"] = isRegex
        return self.driver.execute_and_wait("Page.searchInResource", params)

    def setAdBlockingEnabled(self, enabled):
        """
        Enable Chrome's experimental ad filter on all sites.
        - enabled (boolean): Whether to block ads.
        """
        params = {}
        params["enabled"] = enabled
        return self.driver.execute_and_wait("Page.setAdBlockingEnabled", params)

    def setBypassCSP(self, enabled):
        """
        Enable page Content Security Policy by-passing.
        - enabled (boolean): Whether to bypass page CSP.
        """
        params = {}
        params["enabled"] = enabled
        return self.driver.execute_and_wait("Page.setBypassCSP", params)

    def getPermissionsPolicyState(self, frameId):
        """
        Get Permissions Policy state on given frame.
        - frameId (any): 
        """
        params = {}
        params["frameId"] = frameId
        return self.driver.execute_and_wait("Page.getPermissionsPolicyState", params)

    def getOriginTrials(self, frameId):
        """
        Get Origin Trials on given frame.
        - frameId (any): 
        """
        params = {}
        params["frameId"] = frameId
        return self.driver.execute_and_wait("Page.getOriginTrials", params)

    def setDeviceMetricsOverride(self, width, height, deviceScaleFactor, mobile, scale=None, screenWidth=None, screenHeight=None, positionX=None, positionY=None, dontSetVisibleSize=None, screenOrientation=None, viewport=None):
        """
        Overrides the values of device screen dimensions (window.screen.width, window.screen.height, window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media query results).
        - width (integer): Overriding width value in pixels (minimum 0, maximum 10000000). 0 disables the override.
        - height (integer): Overriding height value in pixels (minimum 0, maximum 10000000). 0 disables the override.
        - deviceScaleFactor (number): Overriding device scale factor value. 0 disables the override.
        - mobile (boolean): Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text
autosizing and more.
        - scale (number): Scale to apply to resulting view image.
        - screenWidth (integer): Overriding screen width value in pixels (minimum 0, maximum 10000000).
        - screenHeight (integer): Overriding screen height value in pixels (minimum 0, maximum 10000000).
        - positionX (integer): Overriding view X position on screen in pixels (minimum 0, maximum 10000000).
        - positionY (integer): Overriding view Y position on screen in pixels (minimum 0, maximum 10000000).
        - dontSetVisibleSize (boolean): Do not set visible view size, rely upon explicit setVisibleSize call.
        - screenOrientation (any): Screen orientation override.
        - viewport (any): The viewport dimensions and scale. If not set, the override is cleared.
        """
        params = {}
        params["width"] = width
        params["height"] = height
        params["deviceScaleFactor"] = deviceScaleFactor
        params["mobile"] = mobile
        if scale is not None:
            params["scale"] = scale
        if screenWidth is not None:
            params["screenWidth"] = screenWidth
        if screenHeight is not None:
            params["screenHeight"] = screenHeight
        if positionX is not None:
            params["positionX"] = positionX
        if positionY is not None:
            params["positionY"] = positionY
        if dontSetVisibleSize is not None:
            params["dontSetVisibleSize"] = dontSetVisibleSize
        if screenOrientation is not None:
            params["screenOrientation"] = screenOrientation
        if viewport is not None:
            params["viewport"] = viewport
        return self.driver.execute_and_wait("Page.setDeviceMetricsOverride", params)

    def setDeviceOrientationOverride(self, alpha, beta, gamma):
        """
        Overrides the Device Orientation.
        - alpha (number): Mock alpha
        - beta (number): Mock beta
        - gamma (number): Mock gamma
        """
        params = {}
        params["alpha"] = alpha
        params["beta"] = beta
        params["gamma"] = gamma
        return self.driver.execute_and_wait("Page.setDeviceOrientationOverride", params)

    def setFontFamilies(self, fontFamilies, forScripts=None):
        """
        Set generic font families.
        - fontFamilies (any): Specifies font families to set. If a font family is not specified, it won't be changed.
        - forScripts (array): Specifies font families to set for individual scripts.
        """
        params = {}
        params["fontFamilies"] = fontFamilies
        if forScripts is not None:
            params["forScripts"] = forScripts
        return self.driver.execute_and_wait("Page.setFontFamilies", params)

    def setFontSizes(self, fontSizes):
        """
        Set default font sizes.
        - fontSizes (any): Specifies font sizes to set. If a font size is not specified, it won't be changed.
        """
        params = {}
        params["fontSizes"] = fontSizes
        return self.driver.execute_and_wait("Page.setFontSizes", params)

    def setDocumentContent(self, frameId, html):
        """
        Sets given markup as the document's HTML.
        - frameId (any): Frame id to set HTML for.
        - html (string): HTML content to set.
        """
        params = {}
        params["frameId"] = frameId
        params["html"] = html
        return self.driver.execute_and_wait("Page.setDocumentContent", params)

    def setDownloadBehavior(self, behavior, downloadPath=None):
        """
        Set the behavior when downloading a file.
        - behavior (string): Whether to allow all or deny all download requests, or use default Chrome behavior if
available (otherwise deny).
        - downloadPath (string): The default path to save downloaded files to. This is required if behavior is set to 'allow'
        """
        params = {}
        params["behavior"] = behavior
        if downloadPath is not None:
            params["downloadPath"] = downloadPath
        return self.driver.execute_and_wait("Page.setDownloadBehavior", params)

    def setGeolocationOverride(self, latitude=None, longitude=None, accuracy=None):
        """
        Overrides the Geolocation Position or Error. Omitting any of the parameters emulates position unavailable.
        - latitude (number): Mock latitude
        - longitude (number): Mock longitude
        - accuracy (number): Mock accuracy
        """
        params = {}
        if latitude is not None:
            params["latitude"] = latitude
        if longitude is not None:
            params["longitude"] = longitude
        if accuracy is not None:
            params["accuracy"] = accuracy
        return self.driver.execute_and_wait("Page.setGeolocationOverride", params)

    def setLifecycleEventsEnabled(self, enabled):
        """
        Controls whether page will emit lifecycle events.
        - enabled (boolean): If true, starts emitting lifecycle events.
        """
        params = {}
        params["enabled"] = enabled
        return self.driver.execute_and_wait("Page.setLifecycleEventsEnabled", params)

    def setTouchEmulationEnabled(self, enabled, configuration=None):
        """
        Toggles mouse event-based touch event emulation.
        - enabled (boolean): Whether the touch event emulation should be enabled.
        - configuration (string): Touch/gesture events configuration. Default: current platform.
        """
        params = {}
        params["enabled"] = enabled
        if configuration is not None:
            params["configuration"] = configuration
        return self.driver.execute_and_wait("Page.setTouchEmulationEnabled", params)

    def startScreencast(self, format=None, quality=None, maxWidth=None, maxHeight=None, everyNthFrame=None):
        """
        Starts sending each frame using the `screencastFrame` event.
        - format (string): Image compression format.
        - quality (integer): Compression quality from range [0..100].
        - maxWidth (integer): Maximum screenshot width.
        - maxHeight (integer): Maximum screenshot height.
        - everyNthFrame (integer): Send every n-th frame.
        """
        params = {}
        if format is not None:
            params["format"] = format
        if quality is not None:
            params["quality"] = quality
        if maxWidth is not None:
            params["maxWidth"] = maxWidth
        if maxHeight is not None:
            params["maxHeight"] = maxHeight
        if everyNthFrame is not None:
            params["everyNthFrame"] = everyNthFrame
        return self.driver.execute_and_wait("Page.startScreencast", params)

    def stopLoading(self):
        """
        Force the page stop all navigations and pending resource fetches.
        """
        params = {}
        return self.driver.execute_and_wait("Page.stopLoading", params)

    def crash(self):
        """
        Crashes renderer on the IO thread, generates minidumps.
        """
        params = {}
        return self.driver.execute_and_wait("Page.crash", params)

    def close(self):
        """
        Tries to close page, running its beforeunload hooks, if any.
        """
        params = {}
        return self.driver.execute_and_wait("Page.close", params)

    def setWebLifecycleState(self, state):
        """
        Tries to update the web lifecycle state of the page. It will transition the page to the given state according to: https://github.com/WICG/web-lifecycle/
        - state (string): Target lifecycle state
        """
        params = {}
        params["state"] = state
        return self.driver.execute_and_wait("Page.setWebLifecycleState", params)

    def stopScreencast(self):
        """
        Stops sending each frame in the `screencastFrame`.
        """
        params = {}
        return self.driver.execute_and_wait("Page.stopScreencast", params)

    def produceCompilationCache(self, scripts):
        """
        Requests backend to produce compilation cache for the specified scripts. `scripts` are appended to the list of scripts for which the cache would be produced. The list may be reset during page navigation. When script with a matching URL is encountered, the cache is optionally produced upon backend discretion, based on internal heuristics. See also: `Page.compilationCacheProduced`.
        - scripts (array): 
        """
        params = {}
        params["scripts"] = scripts
        return self.driver.execute_and_wait("Page.produceCompilationCache", params)

    def addCompilationCache(self, url, data):
        """
        Seeds compilation cache for given url. Compilation cache does not survive cross-process navigation.
        - url (string): 
        - data (string): Base64-encoded data (Encoded as a base64 string when passed over JSON)
        """
        params = {}
        params["url"] = url
        params["data"] = data
        return self.driver.execute_and_wait("Page.addCompilationCache", params)

    def clearCompilationCache(self):
        """
        Clears seeded compilation cache.
        """
        params = {}
        return self.driver.execute_and_wait("Page.clearCompilationCache", params)

    def setSPCTransactionMode(self, mode):
        """
        Sets the Secure Payment Confirmation transaction mode. https://w3c.github.io/secure-payment-confirmation/#sctn-automation-set-spc-transaction-mode
        - mode (string): 
        """
        params = {}
        params["mode"] = mode
        return self.driver.execute_and_wait("Page.setSPCTransactionMode", params)

    def setRPHRegistrationMode(self, mode):
        """
        Extensions for Custom Handlers API: https://html.spec.whatwg.org/multipage/system-state.html#rph-automation
        - mode (string): 
        """
        params = {}
        params["mode"] = mode
        return self.driver.execute_and_wait("Page.setRPHRegistrationMode", params)

    def generateTestReport(self, message, group=None):
        """
        Generates a report for testing.
        - message (string): Message to be displayed in the report.
        - group (string): Specifies the endpoint group to deliver the report to.
        """
        params = {}
        params["message"] = message
        if group is not None:
            params["group"] = group
        return self.driver.execute_and_wait("Page.generateTestReport", params)

    def waitForDebugger(self):
        """
        Pauses page execution. Can be resumed using generic Runtime.runIfWaitingForDebugger.
        """
        params = {}
        return self.driver.execute_and_wait("Page.waitForDebugger", params)

    def setInterceptFileChooserDialog(self, enabled, cancel=None):
        """
        Intercept file chooser requests and transfer control to protocol clients. When file chooser interception is enabled, native file chooser dialog is not shown. Instead, a protocol event `Page.fileChooserOpened` is emitted.
        - enabled (boolean): 
        - cancel (boolean): If true, cancels the dialog by emitting relevant events (if any)
in addition to not showing it if the interception is enabled
(default: false).
        """
        params = {}
        params["enabled"] = enabled
        if cancel is not None:
            params["cancel"] = cancel
        return self.driver.execute_and_wait("Page.setInterceptFileChooserDialog", params)

    def setPrerenderingAllowed(self, isAllowed):
        """
        Enable/disable prerendering manually.  This command is a short-term solution for https://crbug.com/1440085. See https://docs.google.com/document/d/12HVmFxYj5Jc-eJr5OmWsa2bqTJsbgGLKI6ZIyx0_wpA for more details.  TODO(https://crbug.com/1440085): Remove this once Puppeteer supports tab targets.
        - isAllowed (boolean): 
        """
        params = {}
        params["isAllowed"] = isAllowed
        return self.driver.execute_and_wait("Page.setPrerenderingAllowed", params)

    def getAnnotatedPageContent(self, includeActionableInformation=None):
        """
        Get the annotated page content for the main frame. This is an experimental command that is subject to change.
        - includeActionableInformation (boolean): Whether to include actionable information. Defaults to true.
        """
        params = {}
        if includeActionableInformation is not None:
            params["includeActionableInformation"] = includeActionableInformation
        return self.driver.execute_and_wait("Page.getAnnotatedPageContent", params)

