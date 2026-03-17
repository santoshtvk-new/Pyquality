class EmulationDomain:
    def __init__(self, driver):
        self.driver = driver

    def canEmulate(self):
        """
        Tells whether emulation is supported.
        """
        params = {}
        return self.driver.execute_and_wait("Emulation.canEmulate", params)

    def clearDeviceMetricsOverride(self):
        """
        Clears the overridden device metrics.
        """
        params = {}
        return self.driver.execute_and_wait("Emulation.clearDeviceMetricsOverride", params)

    def clearGeolocationOverride(self):
        """
        Clears the overridden Geolocation Position and Error.
        """
        params = {}
        return self.driver.execute_and_wait("Emulation.clearGeolocationOverride", params)

    def resetPageScaleFactor(self):
        """
        Requests that page scale factor is reset to initial values.
        """
        params = {}
        return self.driver.execute_and_wait("Emulation.resetPageScaleFactor", params)

    def setFocusEmulationEnabled(self, enabled):
        """
        Enables or disables simulating a focused and active page.
        - enabled (boolean): Whether to enable to disable focus emulation.
        """
        params = {}
        params["enabled"] = enabled
        return self.driver.execute_and_wait("Emulation.setFocusEmulationEnabled", params)

    def setAutoDarkModeOverride(self, enabled=None):
        """
        Automatically render all web contents using a dark theme.
        - enabled (boolean): Whether to enable or disable automatic dark mode.
If not specified, any existing override will be cleared.
        """
        params = {}
        if enabled is not None:
            params["enabled"] = enabled
        return self.driver.execute_and_wait("Emulation.setAutoDarkModeOverride", params)

    def setCPUThrottlingRate(self, rate):
        """
        Enables CPU throttling to emulate slow CPUs.
        - rate (number): Throttling rate as a slowdown factor (1 is no throttle, 2 is 2x slowdown, etc).
        """
        params = {}
        params["rate"] = rate
        return self.driver.execute_and_wait("Emulation.setCPUThrottlingRate", params)

    def setDefaultBackgroundColorOverride(self, color=None):
        """
        Sets or clears an override of the default background color of the frame. This override is used if the content does not specify one.
        - color (any): RGBA of the default background color. If not specified, any existing override will be
cleared.
        """
        params = {}
        if color is not None:
            params["color"] = color
        return self.driver.execute_and_wait("Emulation.setDefaultBackgroundColorOverride", params)

    def setSafeAreaInsetsOverride(self, insets):
        """
        Overrides the values for env(safe-area-inset-*) and env(safe-area-max-inset-*). Unset values will cause the respective variables to be undefined, even if previously overridden.
        - insets (any): 
        """
        params = {}
        params["insets"] = insets
        return self.driver.execute_and_wait("Emulation.setSafeAreaInsetsOverride", params)

    def setDeviceMetricsOverride(self, width, height, deviceScaleFactor, mobile, scale=None, screenWidth=None, screenHeight=None, positionX=None, positionY=None, dontSetVisibleSize=None, screenOrientation=None, viewport=None, displayFeature=None, devicePosture=None, scrollbarType=None, screenOrientationLockEmulation=None):
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
        - viewport (any): If set, the visible area of the page will be overridden to this viewport. This viewport
change is not observed by the page, e.g. viewport-relative elements do not change positions.
        - displayFeature (any): If set, the display feature of a multi-segment screen. If not set, multi-segment support
is turned-off.
Deprecated, use Emulation.setDisplayFeaturesOverride.
        - devicePosture (any): If set, the posture of a foldable device. If not set the posture is set
to continuous.
Deprecated, use Emulation.setDevicePostureOverride.
        - scrollbarType (string): Scrollbar type. Default: `default`.
        - screenOrientationLockEmulation (boolean): If set to true, enables screen orientation lock emulation, which
intercepts screen.orientation.lock() calls from the page and reports
orientation changes via screenOrientationLockChanged events. This is
useful for emulating mobile device orientation lock behavior in
responsive design mode.
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
        if displayFeature is not None:
            params["displayFeature"] = displayFeature
        if devicePosture is not None:
            params["devicePosture"] = devicePosture
        if scrollbarType is not None:
            params["scrollbarType"] = scrollbarType
        if screenOrientationLockEmulation is not None:
            params["screenOrientationLockEmulation"] = screenOrientationLockEmulation
        return self.driver.execute_and_wait("Emulation.setDeviceMetricsOverride", params)

    def setDevicePostureOverride(self, posture):
        """
        Start reporting the given posture value to the Device Posture API. This override can also be set in setDeviceMetricsOverride().
        - posture (any): 
        """
        params = {}
        params["posture"] = posture
        return self.driver.execute_and_wait("Emulation.setDevicePostureOverride", params)

    def clearDevicePostureOverride(self):
        """
        Clears a device posture override set with either setDeviceMetricsOverride() or setDevicePostureOverride() and starts using posture information from the platform again. Does nothing if no override is set.
        """
        params = {}
        return self.driver.execute_and_wait("Emulation.clearDevicePostureOverride", params)

    def setDisplayFeaturesOverride(self, features):
        """
        Start using the given display features to pupulate the Viewport Segments API. This override can also be set in setDeviceMetricsOverride().
        - features (array): 
        """
        params = {}
        params["features"] = features
        return self.driver.execute_and_wait("Emulation.setDisplayFeaturesOverride", params)

    def clearDisplayFeaturesOverride(self):
        """
        Clears the display features override set with either setDeviceMetricsOverride() or setDisplayFeaturesOverride() and starts using display features from the platform again. Does nothing if no override is set.
        """
        params = {}
        return self.driver.execute_and_wait("Emulation.clearDisplayFeaturesOverride", params)

    def setScrollbarsHidden(self, hidden):
        """
        Call Emulation.setScrollbarsHidden
        - hidden (boolean): Whether scrollbars should be always hidden.
        """
        params = {}
        params["hidden"] = hidden
        return self.driver.execute_and_wait("Emulation.setScrollbarsHidden", params)

    def setDocumentCookieDisabled(self, disabled):
        """
        Call Emulation.setDocumentCookieDisabled
        - disabled (boolean): Whether document.coookie API should be disabled.
        """
        params = {}
        params["disabled"] = disabled
        return self.driver.execute_and_wait("Emulation.setDocumentCookieDisabled", params)

    def setEmitTouchEventsForMouse(self, enabled, configuration=None):
        """
        Call Emulation.setEmitTouchEventsForMouse
        - enabled (boolean): Whether touch emulation based on mouse input should be enabled.
        - configuration (string): Touch/gesture events configuration. Default: current platform.
        """
        params = {}
        params["enabled"] = enabled
        if configuration is not None:
            params["configuration"] = configuration
        return self.driver.execute_and_wait("Emulation.setEmitTouchEventsForMouse", params)

    def setEmulatedMedia(self, media=None, features=None):
        """
        Emulates the given media type or media feature for CSS media queries.
        - media (string): Media type to emulate. Empty string disables the override.
        - features (array): Media features to emulate.
        """
        params = {}
        if media is not None:
            params["media"] = media
        if features is not None:
            params["features"] = features
        return self.driver.execute_and_wait("Emulation.setEmulatedMedia", params)

    def setEmulatedVisionDeficiency(self, type_):
        """
        Emulates the given vision deficiency.
        - type (string): Vision deficiency to emulate. Order: best-effort emulations come first, followed by any
physiologically accurate emulations for medically recognized color vision deficiencies.
        """
        params = {}
        params["type"] = type_
        return self.driver.execute_and_wait("Emulation.setEmulatedVisionDeficiency", params)

    def setEmulatedOSTextScale(self, scale=None):
        """
        Emulates the given OS text scale.
        - scale (number): 
        """
        params = {}
        if scale is not None:
            params["scale"] = scale
        return self.driver.execute_and_wait("Emulation.setEmulatedOSTextScale", params)

    def setGeolocationOverride(self, latitude=None, longitude=None, accuracy=None, altitude=None, altitudeAccuracy=None, heading=None, speed=None):
        """
        Overrides the Geolocation Position or Error. Omitting latitude, longitude or accuracy emulates position unavailable.
        - latitude (number): Mock latitude
        - longitude (number): Mock longitude
        - accuracy (number): Mock accuracy
        - altitude (number): Mock altitude
        - altitudeAccuracy (number): Mock altitudeAccuracy
        - heading (number): Mock heading
        - speed (number): Mock speed
        """
        params = {}
        if latitude is not None:
            params["latitude"] = latitude
        if longitude is not None:
            params["longitude"] = longitude
        if accuracy is not None:
            params["accuracy"] = accuracy
        if altitude is not None:
            params["altitude"] = altitude
        if altitudeAccuracy is not None:
            params["altitudeAccuracy"] = altitudeAccuracy
        if heading is not None:
            params["heading"] = heading
        if speed is not None:
            params["speed"] = speed
        return self.driver.execute_and_wait("Emulation.setGeolocationOverride", params)

    def getOverriddenSensorInformation(self, type_):
        """
        Call Emulation.getOverriddenSensorInformation
        - type (any): 
        """
        params = {}
        params["type"] = type_
        return self.driver.execute_and_wait("Emulation.getOverriddenSensorInformation", params)

    def setSensorOverrideEnabled(self, enabled, type_, metadata=None):
        """
        Overrides a platform sensor of a given type. If |enabled| is true, calls to Sensor.start() will use a virtual sensor as backend rather than fetching data from a real hardware sensor. Otherwise, existing virtual sensor-backend Sensor objects will fire an error event and new calls to Sensor.start() will attempt to use a real sensor instead.
        - enabled (boolean): 
        - type (any): 
        - metadata (any): 
        """
        params = {}
        params["enabled"] = enabled
        params["type"] = type_
        if metadata is not None:
            params["metadata"] = metadata
        return self.driver.execute_and_wait("Emulation.setSensorOverrideEnabled", params)

    def setSensorOverrideReadings(self, type_, reading):
        """
        Updates the sensor readings reported by a sensor type previously overridden by setSensorOverrideEnabled.
        - type (any): 
        - reading (any): 
        """
        params = {}
        params["type"] = type_
        params["reading"] = reading
        return self.driver.execute_and_wait("Emulation.setSensorOverrideReadings", params)

    def setPressureSourceOverrideEnabled(self, enabled, source, metadata=None):
        """
        Overrides a pressure source of a given type, as used by the Compute Pressure API, so that updates to PressureObserver.observe() are provided via setPressureStateOverride instead of being retrieved from platform-provided telemetry data.
        - enabled (boolean): 
        - source (any): 
        - metadata (any): 
        """
        params = {}
        params["enabled"] = enabled
        params["source"] = source
        if metadata is not None:
            params["metadata"] = metadata
        return self.driver.execute_and_wait("Emulation.setPressureSourceOverrideEnabled", params)

    def setPressureStateOverride(self, source, state):
        """
        TODO: OBSOLETE: To remove when setPressureDataOverride is merged. Provides a given pressure state that will be processed and eventually be delivered to PressureObserver users. |source| must have been previously overridden by setPressureSourceOverrideEnabled.
        - source (any): 
        - state (any): 
        """
        params = {}
        params["source"] = source
        params["state"] = state
        return self.driver.execute_and_wait("Emulation.setPressureStateOverride", params)

    def setPressureDataOverride(self, source, state, ownContributionEstimate=None):
        """
        Provides a given pressure data set that will be processed and eventually be delivered to PressureObserver users. |source| must have been previously overridden by setPressureSourceOverrideEnabled.
        - source (any): 
        - state (any): 
        - ownContributionEstimate (number): 
        """
        params = {}
        params["source"] = source
        params["state"] = state
        if ownContributionEstimate is not None:
            params["ownContributionEstimate"] = ownContributionEstimate
        return self.driver.execute_and_wait("Emulation.setPressureDataOverride", params)

    def setIdleOverride(self, isUserActive, isScreenUnlocked):
        """
        Overrides the Idle state.
        - isUserActive (boolean): Mock isUserActive
        - isScreenUnlocked (boolean): Mock isScreenUnlocked
        """
        params = {}
        params["isUserActive"] = isUserActive
        params["isScreenUnlocked"] = isScreenUnlocked
        return self.driver.execute_and_wait("Emulation.setIdleOverride", params)

    def clearIdleOverride(self):
        """
        Clears Idle state overrides.
        """
        params = {}
        return self.driver.execute_and_wait("Emulation.clearIdleOverride", params)

    def setNavigatorOverrides(self, platform):
        """
        Overrides value returned by the javascript navigator object.
        - platform (string): The platform navigator.platform should return.
        """
        params = {}
        params["platform"] = platform
        return self.driver.execute_and_wait("Emulation.setNavigatorOverrides", params)

    def setPageScaleFactor(self, pageScaleFactor):
        """
        Sets a specified page scale factor.
        - pageScaleFactor (number): Page scale factor.
        """
        params = {}
        params["pageScaleFactor"] = pageScaleFactor
        return self.driver.execute_and_wait("Emulation.setPageScaleFactor", params)

    def setScriptExecutionDisabled(self, value):
        """
        Switches script execution in the page.
        - value (boolean): Whether script execution should be disabled in the page.
        """
        params = {}
        params["value"] = value
        return self.driver.execute_and_wait("Emulation.setScriptExecutionDisabled", params)

    def setTouchEmulationEnabled(self, enabled, maxTouchPoints=None):
        """
        Enables touch on platforms which do not support them.
        - enabled (boolean): Whether the touch event emulation should be enabled.
        - maxTouchPoints (integer): Maximum touch points supported. Defaults to one.
        """
        params = {}
        params["enabled"] = enabled
        if maxTouchPoints is not None:
            params["maxTouchPoints"] = maxTouchPoints
        return self.driver.execute_and_wait("Emulation.setTouchEmulationEnabled", params)

    def setVirtualTimePolicy(self, policy, budget=None, maxVirtualTimeTaskStarvationCount=None, initialVirtualTime=None):
        """
        Turns on virtual time for all frames (replacing real-time with a synthetic time source) and sets the current virtual time policy.  Note this supersedes any previous time budget.
        - policy (any): 
        - budget (number): If set, after this many virtual milliseconds have elapsed virtual time will be paused and a
virtualTimeBudgetExpired event is sent.
        - maxVirtualTimeTaskStarvationCount (integer): If set this specifies the maximum number of tasks that can be run before virtual is forced
forwards to prevent deadlock.
        - initialVirtualTime (any): If set, base::Time::Now will be overridden to initially return this value.
        """
        params = {}
        params["policy"] = policy
        if budget is not None:
            params["budget"] = budget
        if maxVirtualTimeTaskStarvationCount is not None:
            params["maxVirtualTimeTaskStarvationCount"] = maxVirtualTimeTaskStarvationCount
        if initialVirtualTime is not None:
            params["initialVirtualTime"] = initialVirtualTime
        return self.driver.execute_and_wait("Emulation.setVirtualTimePolicy", params)

    def setLocaleOverride(self, locale=None):
        """
        Overrides default host system locale with the specified one.
        - locale (string): ICU style C locale (e.g. "en_US"). If not specified or empty, disables the override and
restores default host system locale.
        """
        params = {}
        if locale is not None:
            params["locale"] = locale
        return self.driver.execute_and_wait("Emulation.setLocaleOverride", params)

    def setTimezoneOverride(self, timezoneId):
        """
        Overrides default host system timezone with the specified one.
        - timezoneId (string): The timezone identifier. List of supported timezones:
https://source.chromium.org/chromium/chromium/deps/icu.git/+/faee8bc70570192d82d2978a71e2a615788597d1:source/data/misc/metaZones.txt
If empty, disables the override and restores default host system timezone.
        """
        params = {}
        params["timezoneId"] = timezoneId
        return self.driver.execute_and_wait("Emulation.setTimezoneOverride", params)

    def setVisibleSize(self, width, height):
        """
        Resizes the frame/viewport of the page. Note that this does not affect the frame's container (e.g. browser window). Can be used to produce screenshots of the specified size. Not supported on Android.
        - width (integer): Frame width (DIP).
        - height (integer): Frame height (DIP).
        """
        params = {}
        params["width"] = width
        params["height"] = height
        return self.driver.execute_and_wait("Emulation.setVisibleSize", params)

    def setDisabledImageTypes(self, imageTypes):
        """
        Call Emulation.setDisabledImageTypes
        - imageTypes (array): Image types to disable.
        """
        params = {}
        params["imageTypes"] = imageTypes
        return self.driver.execute_and_wait("Emulation.setDisabledImageTypes", params)

    def setDataSaverOverride(self, dataSaverEnabled=None):
        """
        Override the value of navigator.connection.saveData
        - dataSaverEnabled (boolean): Override value. Omitting the parameter disables the override.
        """
        params = {}
        if dataSaverEnabled is not None:
            params["dataSaverEnabled"] = dataSaverEnabled
        return self.driver.execute_and_wait("Emulation.setDataSaverOverride", params)

    def setHardwareConcurrencyOverride(self, hardwareConcurrency):
        """
        Call Emulation.setHardwareConcurrencyOverride
        - hardwareConcurrency (integer): Hardware concurrency to report
        """
        params = {}
        params["hardwareConcurrency"] = hardwareConcurrency
        return self.driver.execute_and_wait("Emulation.setHardwareConcurrencyOverride", params)

    def setUserAgentOverride(self, userAgent, acceptLanguage=None, platform=None, userAgentMetadata=None):
        """
        Allows overriding user agent with the given string. `userAgentMetadata` must be set for Client Hint headers to be sent.
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
        return self.driver.execute_and_wait("Emulation.setUserAgentOverride", params)

    def setAutomationOverride(self, enabled):
        """
        Allows overriding the automation flag.
        - enabled (boolean): Whether the override should be enabled.
        """
        params = {}
        params["enabled"] = enabled
        return self.driver.execute_and_wait("Emulation.setAutomationOverride", params)

    def setSmallViewportHeightDifferenceOverride(self, difference):
        """
        Allows overriding the difference between the small and large viewport sizes, which determine the value of the `svh` and `lvh` unit, respectively. Only supported for top-level frames.
        - difference (integer): This will cause an element of size 100svh to be `difference` pixels smaller than an element
of size 100lvh.
        """
        params = {}
        params["difference"] = difference
        return self.driver.execute_and_wait("Emulation.setSmallViewportHeightDifferenceOverride", params)

    def getScreenInfos(self):
        """
        Returns device's screen configuration. In headful mode, the physical screens configuration is returned, whereas in headless mode, a virtual headless screen configuration is provided instead.
        """
        params = {}
        return self.driver.execute_and_wait("Emulation.getScreenInfos", params)

    def addScreen(self, left, top, width, height, workAreaInsets=None, devicePixelRatio=None, rotation=None, colorDepth=None, label=None, isInternal=None):
        """
        Add a new screen to the device. Only supported in headless mode.
        - left (integer): Offset of the left edge of the screen in pixels.
        - top (integer): Offset of the top edge of the screen in pixels.
        - width (integer): The width of the screen in pixels.
        - height (integer): The height of the screen in pixels.
        - workAreaInsets (any): Specifies the screen's work area. Default is entire screen.
        - devicePixelRatio (number): Specifies the screen's device pixel ratio. Default is 1.
        - rotation (integer): Specifies the screen's rotation angle. Available values are 0, 90, 180 and 270. Default is 0.
        - colorDepth (integer): Specifies the screen's color depth in bits. Default is 24.
        - label (string): Specifies the descriptive label for the screen. Default is none.
        - isInternal (boolean): Indicates whether the screen is internal to the device or external, attached to the device. Default is false.
        """
        params = {}
        params["left"] = left
        params["top"] = top
        params["width"] = width
        params["height"] = height
        if workAreaInsets is not None:
            params["workAreaInsets"] = workAreaInsets
        if devicePixelRatio is not None:
            params["devicePixelRatio"] = devicePixelRatio
        if rotation is not None:
            params["rotation"] = rotation
        if colorDepth is not None:
            params["colorDepth"] = colorDepth
        if label is not None:
            params["label"] = label
        if isInternal is not None:
            params["isInternal"] = isInternal
        return self.driver.execute_and_wait("Emulation.addScreen", params)

    def updateScreen(self, screenId, left=None, top=None, width=None, height=None, workAreaInsets=None, devicePixelRatio=None, rotation=None, colorDepth=None, label=None, isInternal=None):
        """
        Updates specified screen parameters. Only supported in headless mode.
        - screenId (any): Target screen identifier.
        - left (integer): Offset of the left edge of the screen in pixels.
        - top (integer): Offset of the top edge of the screen in pixels.
        - width (integer): The width of the screen in pixels.
        - height (integer): The height of the screen in pixels.
        - workAreaInsets (any): Specifies the screen's work area.
        - devicePixelRatio (number): Specifies the screen's device pixel ratio.
        - rotation (integer): Specifies the screen's rotation angle. Available values are 0, 90, 180 and 270.
        - colorDepth (integer): Specifies the screen's color depth in bits.
        - label (string): Specifies the descriptive label for the screen.
        - isInternal (boolean): Indicates whether the screen is internal to the device or external, attached to the device. Default is false.
        """
        params = {}
        params["screenId"] = screenId
        if left is not None:
            params["left"] = left
        if top is not None:
            params["top"] = top
        if width is not None:
            params["width"] = width
        if height is not None:
            params["height"] = height
        if workAreaInsets is not None:
            params["workAreaInsets"] = workAreaInsets
        if devicePixelRatio is not None:
            params["devicePixelRatio"] = devicePixelRatio
        if rotation is not None:
            params["rotation"] = rotation
        if colorDepth is not None:
            params["colorDepth"] = colorDepth
        if label is not None:
            params["label"] = label
        if isInternal is not None:
            params["isInternal"] = isInternal
        return self.driver.execute_and_wait("Emulation.updateScreen", params)

    def removeScreen(self, screenId):
        """
        Remove screen from the device. Only supported in headless mode.
        - screenId (any): 
        """
        params = {}
        params["screenId"] = screenId
        return self.driver.execute_and_wait("Emulation.removeScreen", params)

    def setPrimaryScreen(self, screenId):
        """
        Set primary screen. Only supported in headless mode. Note that this changes the coordinate system origin to the top-left of the new primary screen, updating the bounds and work areas of all existing screens accordingly.
        - screenId (any): 
        """
        params = {}
        params["screenId"] = screenId
        return self.driver.execute_and_wait("Emulation.setPrimaryScreen", params)

