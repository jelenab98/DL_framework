class Visualizer:
    def __init__(self):
        return

    def __enter__(self):
        return

    def __exit__(self, exc_type, exc_val, exc_tb):
        return

    def _visualize(self):
        raise NotImplementedError

    def visualize(self):
        self._visualize()
