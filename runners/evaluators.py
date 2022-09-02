class Evaluator:
    """
    Context wrapper for evaluation. Evaluates the model for specified metrics and visualizes the predictions.
    """
    def __init__(self):
        """
        Initialize all the variables.
        """
        return

    def __enter__(self):
        """
        Defines paths, variables and lists. Check for existence and create if necessary.
        :return:
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Save everything before exiting.
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        return

    def _validate(self):
        """
        Calculate metrics from the predictions.
        :return:
        """
        raise NotImplementedError

    def _visualize(self):
        """
        Generate visuals of predictions.
        :return:
        """
        raise NotImplementedError


class FlowEvaluator(Evaluator):
    def __init__(self):
        super(FlowEvaluator).__init__()

    def custom_fn(self):
        return

    def _validate(self):
        return

    def _visualize(self):
        return


class StereoEvaluator(Evaluator):
    def __init__(self):
        super(StereoEvaluator).__init__()

    def custom_fn(self):
        return

    def _validate(self):
        return

    def _visualize(self):
        return


class SegmentationEvaluator(Evaluator):
    def __init__(self):
        super(SegmentationEvaluator, self).__init__()

    def custom_fn(self):
        return

    def _validate(self):
        return

    def _visualize(self):
        return


class ClassificationEvaluator(Evaluator):
    def __init__(self):
        super(ClassificationEvaluator, self).__init__()

    def custom_fn(self):
        return

    def _validate(self):
        return

    def _visualize(self):
        return
