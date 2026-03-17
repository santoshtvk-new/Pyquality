class PerformanceTimelineDomain:
    def __init__(self, driver):
        self.driver = driver

    def enable(self, eventTypes):
        """
        Previously buffered events would be reported before method returns. See also: timelineEventAdded
        - eventTypes (array): The types of event to report, as specified in
https://w3c.github.io/performance-timeline/#dom-performanceentry-entrytype
The specified filter overrides any previous filters, passing empty
filter disables recording.
Note that not all types exposed to the web platform are currently supported.
        """
        params = {}
        params["eventTypes"] = eventTypes
        return self.driver.execute_and_wait("PerformanceTimeline.enable", params)

