import json
import os
from jsonmerge import Merger

schema = {
    "properties": {
        "data_file_1": {
            "mergeStrategy": "overwrite",
        },
        "data_file_2": {
            "mergeStrategy": "discard"
        },
        "data_file_3": {
            "mergeStrategy": "discard"
        }
    }
}

output_directory = "./output_2"

file1 = "pos_0.png.json"
file2 = "pos_10010.png.json"
file3 = "pos_10492.png.json"

with open(f"./sampleJson/{file1}", "r") as file:
    data_file_1 = json.load(file)

with open(f"./sampleJson/{file2}", "r") as file:
    data_file_2 = json.load(file)

with open(f"./sampleJson/{file3}", "r") as file:
    data_file_3 = json.load(file)

merger = Merger(schema)
# r2 = merger.merge(data_file_2, data_file_1, merge_options={'version': {'metadata': {'revision': 0}}})
r1 = merger.merge(data_file_2, data_file_1,  merge_options={'version': {'metadata': {'revision': 0}}})
# r3 = merger.merge(data_file_1, data_file_3, merge_options={'version': {'metadata': {'revision': 0}}})

# Check if the directory exists, and if not, create it
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

file_path = f"{output_directory}/solution_2.png.json"
with open(file_path, "w") as f:
    json.dump(r1, f)



# 2nd portion
with open(f"./output_2/solution-2.png.json", "r") as file:
    data_file = json.load(file)

for k, v in data_file.items():
    if k == "classTitle" and data_file["classTitle"] == "Vehicle":
        data_file["classTitle"] = "car"
    else:
        data_file["classTitle"] = "number"
        