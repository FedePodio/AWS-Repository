"""Dictionary to JSON"""

import json

menu = {
    "pizza" : 2.50,
    "panino" : 4.0,
    "bibita" : 2.5,
    "acqua" : 1.0,
    "caffe" : 1.3,
}

with open("scontrino.json", "w") as f:
    json.dump(menu, f, indent = 4)

