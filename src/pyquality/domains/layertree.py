class LayerTreeDomain:
    def __init__(self, driver):
        self.driver = driver

    def compositingReasons(self, layerId):
        """
        Provides the reasons why the given layer was composited.
        - layerId (any): The id of the layer for which we want to get the reasons it was composited.
        """
        params = {}
        params["layerId"] = layerId
        return self.driver.execute_and_wait("LayerTree.compositingReasons", params)

    def disable(self):
        """
        Disables compositing tree inspection.
        """
        params = {}
        return self.driver.execute_and_wait("LayerTree.disable", params)

    def enable(self):
        """
        Enables compositing tree inspection.
        """
        params = {}
        return self.driver.execute_and_wait("LayerTree.enable", params)

    def loadSnapshot(self, tiles):
        """
        Returns the snapshot identifier.
        - tiles (array): An array of tiles composing the snapshot.
        """
        params = {}
        params["tiles"] = tiles
        return self.driver.execute_and_wait("LayerTree.loadSnapshot", params)

    def makeSnapshot(self, layerId):
        """
        Returns the layer snapshot identifier.
        - layerId (any): The id of the layer.
        """
        params = {}
        params["layerId"] = layerId
        return self.driver.execute_and_wait("LayerTree.makeSnapshot", params)

    def profileSnapshot(self, snapshotId, minRepeatCount=None, minDuration=None, clipRect=None):
        """
        Call LayerTree.profileSnapshot
        - snapshotId (any): The id of the layer snapshot.
        - minRepeatCount (integer): The maximum number of times to replay the snapshot (1, if not specified).
        - minDuration (number): The minimum duration (in seconds) to replay the snapshot.
        - clipRect (any): The clip rectangle to apply when replaying the snapshot.
        """
        params = {}
        params["snapshotId"] = snapshotId
        if minRepeatCount is not None:
            params["minRepeatCount"] = minRepeatCount
        if minDuration is not None:
            params["minDuration"] = minDuration
        if clipRect is not None:
            params["clipRect"] = clipRect
        return self.driver.execute_and_wait("LayerTree.profileSnapshot", params)

    def releaseSnapshot(self, snapshotId):
        """
        Releases layer snapshot captured by the back-end.
        - snapshotId (any): The id of the layer snapshot.
        """
        params = {}
        params["snapshotId"] = snapshotId
        return self.driver.execute_and_wait("LayerTree.releaseSnapshot", params)

    def replaySnapshot(self, snapshotId, fromStep=None, toStep=None, scale=None):
        """
        Replays the layer snapshot and returns the resulting bitmap.
        - snapshotId (any): The id of the layer snapshot.
        - fromStep (integer): The first step to replay from (replay from the very start if not specified).
        - toStep (integer): The last step to replay to (replay till the end if not specified).
        - scale (number): The scale to apply while replaying (defaults to 1).
        """
        params = {}
        params["snapshotId"] = snapshotId
        if fromStep is not None:
            params["fromStep"] = fromStep
        if toStep is not None:
            params["toStep"] = toStep
        if scale is not None:
            params["scale"] = scale
        return self.driver.execute_and_wait("LayerTree.replaySnapshot", params)

    def snapshotCommandLog(self, snapshotId):
        """
        Replays the layer snapshot and returns canvas log.
        - snapshotId (any): The id of the layer snapshot.
        """
        params = {}
        params["snapshotId"] = snapshotId
        return self.driver.execute_and_wait("LayerTree.snapshotCommandLog", params)

