# prometheus_sd_helper

## Usage

```python
from servicediscovery import ServiceDiscovery
from targets import Targets

sd = ServiceDiscovery()

# Example single host without labels
targets1 = Targets(targets=["host1:9100"])
sd.add_targets([targets1])

# Example add multiple hosts with labels
my_labels = {"label_1": "value_1", "label_2": "value_2"}
targets2 = Targets(targets=["host2:9100", "host3:9100"], labels=my_labels)

# Example additional labels
additional_labels = {"add_label": "add_value"}
targets3 = Targets(targets=["host4:9100"])
targets3.add_labels(additional_labels)

sd.add_targets([targets2, targets3])

json_string = sd.get_json()
print(json_string)
```

The example above will result in the following json object:

```json
[
   {
      "targets":[
         "host1:9100"
      ],
      "labels":{
         
      }
   },
   {
      "targets":[
         "host2:9100",
         "host3:9100"
      ],
      "labels":{
         "label_1":"value_1",
         "label_2":"value_2"
      }
   },
   {
      "targets":[
         "host4:9100"
      ],
      "labels":{
         "add_label":"add_value"
      }
   }
]
```