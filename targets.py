"Targets Class"
import re

class Targets:
    "Targets Class"
    def __init__(self, targets, labels=None):
        self.targets = targets
        if labels is None:
            self.labels = {}
        else:
            self.labels = labels
            self.validate_label_names(labels)

    def add_labels(self, labels):
        "Add labels to target after target class initialization"
        self.validate_label_names(labels)
        self.labels = {**self.labels, **labels}

    def add_targets(self, targets):
        "Add one ore more targets after target class initialization"
        valid_targets = self.convert_targets_to_list(targets)
        self.targets = [*self.targets, *valid_targets]

    @classmethod
    def convert_targets_to_list(cls, targets):
        "convert string to list of strings and rais exception if targets is not string or list"
        if isinstance(targets, str):
            valid_targets = [targets]
        elif isinstance(targets, list):
            valid_targets = targets
        else:
            raise TypeError("Unexpected type {}\nExpected type string or list".format(type(targets)))
        return valid_targets

    @classmethod
    def validate_label_names(cls, labels):
        "Check if label names are valid"
        if isinstance(labels, dict):
            pattern = '^[a-zA-Z_:][a-zA-Z0-9_:]+$' # https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels
            for key in labels:
                if re.match(pattern, key) is None:
                    raise ValueError("Invalid label name {}\nName must match {}".format(key, pattern))
        else:
            raise TypeError("Unexpected type {}\nExpected type dict".format(type(labels)))
        return True
