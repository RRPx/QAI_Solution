import json
import os

class_titles_tags_from_raw_json = []
formatted_output = []
temp_simplify_tag_names_in_dict = {}
annotation_objects = {}
annotation_attributes = {}
current_working_file = "pos_10492.png.json"
output_directory = "./output"

with open(f"./sampleJson/{current_working_file}","r") as file:
    jsonData = json.load(file)

for i in jsonData["objects"]:
    for k, v in i.items():
        if k == "classTitle":
            class_titles_tags_from_raw_json.append({
                "class_name": v,
                "points_exterior": i["points"]["exterior"][0] + i["points"]["exterior"][1],
                "tags_name": [{value["name"]: value["value"]} for value in i["tags"]]
            })

for data in class_titles_tags_from_raw_json:
    for item in data['tags_name']:
        temp_simplify_tag_names_in_dict.update(item)
        data["tags_name"] = temp_simplify_tag_names_in_dict
    temp_simplify_tag_names_in_dict = {}

for data in class_titles_tags_from_raw_json:
    annotation_objects.update({
            data["class_name"]: {
                "presence": 1 if len(data["points_exterior"]) > 0 else 0,
                "bbox": data["points_exterior"]
            }
    })
    annotation_attributes.update({
        data["class_name"]: data['tags_name']
    })

if "Vehicle" not in annotation_objects.keys():
    annotation_objects.update({
        "Vehicle": {
            "presence": 0,
            "bbox": []
        },
    })

    annotation_attributes.update({
        "Vehicle": {
            "Type": None,
            "Pose": None,
            "Model": None,
            "Make": None,
            "Color": None
        }
    })

if "License Plate" not in annotation_objects.keys():
    annotation_objects.update({
        "License Plate": {
            "presence": 0,
            "bbox": []
        },
    })

    annotation_attributes.update({
        "License Plate": {
            "Difficulty Score": None,
            "Value": None
        }
    })

formatted_output = {
    "dataset_name": current_working_file,
    "image_link": "",
    "annotation_type": "image",
    "annotation_objects": annotation_objects,
    "annotation_attributes": annotation_attributes
}

# Check if the directory exists, and if not, create it
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

file_path = f"{output_directory}/{current_working_file}"
with open(file_path, "w") as f:
    json.dump(formatted_output, f)

    

