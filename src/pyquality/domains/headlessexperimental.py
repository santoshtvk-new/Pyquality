class HeadlessExperimentalDomain:
    def __init__(self, driver):
        self.driver = driver

    def beginFrame(self, frameTimeTicks=None, interval=None, noDisplayUpdates=None, screenshot=None):
        """
        Sends a BeginFrame to the target and returns when the frame was completed. Optionally captures a screenshot from the resulting frame. Requires that the target was created with enabled BeginFrameControl. Designed for use with --run-all-compositor-stages-before-draw, see also https://goo.gle/chrome-headless-rendering for more background.
        - frameTimeTicks (number): Timestamp of this BeginFrame in Renderer TimeTicks (milliseconds of uptime). If not set,
the current time will be used.
        - interval (number): The interval between BeginFrames that is reported to the compositor, in milliseconds.
Defaults to a 60 frames/second interval, i.e. about 16.666 milliseconds.
        - noDisplayUpdates (boolean): Whether updates should not be committed and drawn onto the display. False by default. If
true, only side effects of the BeginFrame will be run, such as layout and animations, but
any visual updates may not be visible on the display or in screenshots.
        - screenshot (any): If set, a screenshot of the frame will be captured and returned in the response. Otherwise,
no screenshot will be captured. Note that capturing a screenshot can fail, for example,
during renderer initialization. In such a case, no screenshot data will be returned.
        """
        params = {}
        if frameTimeTicks is not None:
            params["frameTimeTicks"] = frameTimeTicks
        if interval is not None:
            params["interval"] = interval
        if noDisplayUpdates is not None:
            params["noDisplayUpdates"] = noDisplayUpdates
        if screenshot is not None:
            params["screenshot"] = screenshot
        return self.driver.execute_and_wait("HeadlessExperimental.beginFrame", params)

    def disable(self):
        """
        Disables headless events for the target.
        """
        params = {}
        return self.driver.execute_and_wait("HeadlessExperimental.disable", params)

    def enable(self):
        """
        Enables headless events for the target.
        """
        params = {}
        return self.driver.execute_and_wait("HeadlessExperimental.enable", params)

