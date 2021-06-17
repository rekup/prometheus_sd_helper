"unittests for servicediscovery class"
import unittest
from targets import Targets

class TestServiceDiscovery(unittest.TestCase):
    "unittest class"

    def test_add_labels(self):
        "test add_labels method"
        targets = Targets(targets=["host4:9100"])
        targets.add_labels({"add_label": "add_value"})
        self.assertDictEqual(targets.labels, {'add_label': 'add_value'})

    def test_add_targets(self):
        "test add_targets method"
        targets = Targets(targets=["host1"])
        self.assertListEqual(targets.targets, ["host1"])
        targets.add_targets(["host2:9100", "host3:9100"])
        self.assertListEqual(targets.targets, ["host1", "host2:9100", "host3:9100"])

    def test_convert_targets_to_list(self):
        "test convert_targets_to_list method"
        targets = Targets(targets=["host1"])
        self.assertListEqual(targets.convert_targets_to_list("host2"), ["host2"])
        self.assertListEqual(targets.convert_targets_to_list(["host2"]), ["host2"])
        self.assertListEqual(targets.convert_targets_to_list(["host2", "host3"]), ["host2", "host3"])
        self.assertRaises(TypeError, targets.convert_targets_to_list, {})

    def test_validate_label_names(self):
        "test validate_label_names method"
        labels = {"label_1": "value_1", "label_2": "value_2"}
        targets = Targets(targets=["host1"])
        self.assertRaises(ValueError, targets.validate_label_names, {"invalid_l@belname": "value"})
        self.assertRaises(TypeError, targets.validate_label_names, ["one", "two"])
        self.assertTrue(targets.validate_label_names(labels))
