"ServiceDiscovery Class"
import json

class ServiceDiscovery:
    "ServiceDiscovery Class"
    def __init__(self, name="default"):
        self.name = name
        self.targets = []

    def add_targets(self, hosts):
        "add target to service discovery"
        for host in hosts:
            label_match_index = self.label_match(host)
            if label_match_index is not None:
                self.targets[label_match_index].add_targets(host.targets)
            else:
                self.targets.append(host)

    def get_json(self):
        "Return json string of service discovery"
        targets_list = []
        for item in self.targets:
            targets_list.append(item.__dict__)
        return json.dumps(targets_list)

    def label_match(self, host):
        "check for existing targets with exact same label set and return index"
        for index, entity in enumerate(self.targets):
            if entity.labels == host.labels:
                return index
        return None
