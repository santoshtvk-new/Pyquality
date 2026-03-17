class AnimationDomain:
    def __init__(self, driver):
        self.driver = driver

    def disable(self):
        """
        Disables animation domain notifications.
        """
        params = {}
        return self.driver.execute_and_wait("Animation.disable", params)

    def enable(self):
        """
        Enables animation domain notifications.
        """
        params = {}
        return self.driver.execute_and_wait("Animation.enable", params)

    def getCurrentTime(self, id_):
        """
        Returns the current time of the an animation.
        - id (string): Id of animation.
        """
        params = {}
        params["id"] = id_
        return self.driver.execute_and_wait("Animation.getCurrentTime", params)

    def getPlaybackRate(self):
        """
        Gets the playback rate of the document timeline.
        """
        params = {}
        return self.driver.execute_and_wait("Animation.getPlaybackRate", params)

    def releaseAnimations(self, animations):
        """
        Releases a set of animations to no longer be manipulated.
        - animations (array): List of animation ids to seek.
        """
        params = {}
        params["animations"] = animations
        return self.driver.execute_and_wait("Animation.releaseAnimations", params)

    def resolveAnimation(self, animationId):
        """
        Gets the remote object of the Animation.
        - animationId (string): Animation id.
        """
        params = {}
        params["animationId"] = animationId
        return self.driver.execute_and_wait("Animation.resolveAnimation", params)

    def seekAnimations(self, animations, currentTime):
        """
        Seek a set of animations to a particular time within each animation.
        - animations (array): List of animation ids to seek.
        - currentTime (number): Set the current time of each animation.
        """
        params = {}
        params["animations"] = animations
        params["currentTime"] = currentTime
        return self.driver.execute_and_wait("Animation.seekAnimations", params)

    def setPaused(self, animations, paused):
        """
        Sets the paused state of a set of animations.
        - animations (array): Animations to set the pause state of.
        - paused (boolean): Paused state to set to.
        """
        params = {}
        params["animations"] = animations
        params["paused"] = paused
        return self.driver.execute_and_wait("Animation.setPaused", params)

    def setPlaybackRate(self, playbackRate):
        """
        Sets the playback rate of the document timeline.
        - playbackRate (number): Playback rate for animations on page
        """
        params = {}
        params["playbackRate"] = playbackRate
        return self.driver.execute_and_wait("Animation.setPlaybackRate", params)

    def setTiming(self, animationId, duration, delay):
        """
        Sets the timing of an animation node.
        - animationId (string): Animation id.
        - duration (number): Duration of the animation.
        - delay (number): Delay of the animation.
        """
        params = {}
        params["animationId"] = animationId
        params["duration"] = duration
        params["delay"] = delay
        return self.driver.execute_and_wait("Animation.setTiming", params)

