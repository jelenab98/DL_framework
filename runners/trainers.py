class Trainer:
    def __init__(self):
        return

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return

    def _on_epoch_end(self):
        """
        Check if current model is the best. Conduct validation and update the metrics.
        :return:
        """
        return

    def _save_checkpoint(self):
        """
        Save the current model with unique name from which the epoch and num of iters are readable.
        :return:
        """
        return

    def _check_best_model(self):
        """
        Check if the current model is the best one yet. Will run an evaluator wrapper.
        :return:
        """
        return

    def _validate(self):
        """
        Runs validation of current model.
        :return:
        """
        return

    def train(self):
        """
        Standard train loop.
        :return:
        """
        return

    def _train_step(self):
        """
        Train step different for specific training modes and loss functions.
        :return:
        """
        raise NotImplementedError


class ClassificationTrainer(Trainer):
    def __init__(self):
        super(ClassificationTrainer, self).__init__()

    def _train_step(self):
        return


class SegmentationTrainer(Trainer):
    def __init__(self):
        super(SegmentationTrainer, self).__init__()

    def _train_step(self):
        return


class FlowTrainer(Trainer):
    def __init__(self):
        super(FlowTrainer, self).__init__()

    def _train_step(self):
        return


class StereoTrainer(Trainer):
    def __init__(self):
        super(StereoTrainer, self).__init__()

    def _train_step(self):
        return
