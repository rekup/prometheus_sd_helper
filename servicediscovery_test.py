"unittests for servicediscovery class"
import unittest
from servicediscovery import ServiceDiscovery
from targets import Targets

class TestServiceDiscovery(unittest.TestCase):
    "unittest class"

    def test_add_targets(self):
        "add_target method will be tested using the test_label_match method"

    def test_get_json(self):
        "test get_json method"

        service_discovery = ServiceDiscovery()
        target2 = Targets(targets=["host1"], labels={"label_1": "value_1"})
        service_discovery.add_targets([target2])
        json_string = service_discovery.get_json()
        self.assertEqual(json_string, '[{"targets": ["host1"], "labels": {"label_1": "value_1"}}]')

    def test_label_match(self):
        "test label_match method"
        service_discovery = ServiceDiscovery()

        # add first host
        target1 = Targets(targets=["host1"], labels={"label_1": "value_1"})
        service_discovery.add_targets([target1])
        self.assertIsInstance(service_discovery.targets, list)
        self.assertEqual(len(service_discovery.targets), 1)
        self.assertIsInstance(service_discovery.targets[0], Targets)
        self.assertListEqual(service_discovery.targets[0].targets, ["host1"])

        # add second host with same label set
        target1 = Targets(targets=["host2"], labels={"label_1": "value_1"})
        service_discovery.add_targets([target1])
        self.assertIsInstance(service_discovery.targets, list)
        self.assertEqual(len(service_discovery.targets), 1) # targets should get merged so we expect still only 1 target object
        self.assertIsInstance(service_discovery.targets[0], Targets)
        self.assertListEqual(service_discovery.targets[0].targets, ["host1", "host2"])

        # add third host with different label set
        target1 = Targets(targets=["host2"], labels={"label_2": "value_2"})
        service_discovery.add_targets([target1])
        self.assertIsInstance(service_discovery.targets, list)
        self.assertEqual(len(service_discovery.targets), 2) # targets should get merged so we expect still only 1 target object
        self.assertIsInstance(service_discovery.targets[1], Targets)
        self.assertIsInstance(service_discovery.targets[1], Targets)
        self.assertListEqual(service_discovery.targets[1].targets, ["host2"])
