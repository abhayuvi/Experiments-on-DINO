import json

 # Path to your original annotations file Train/Validation
 annotation_file_path = "/content/DATASET/annotations/instances_val2017.json"
 # Path to save the modified annotations file Train/Validation
 output_file_path = "/content/DATASET/annotations/val.json"

 # Define the categories (adjust as needed)
 categories = [
     { "id": 1, "name": "person" }
     # Add more categories here if needed
 ]

 # Load existing annotations
 with open(annotation_file_path, 'r') as file:
     data = json.load(file)

 # Add the 'categories' field
 data['categories'] = categories

 # Save the modified annotations
 with open(output_file_path, 'w') as file:
     json.dump(data, file, indent=4)

 print("Added 'categories' field successfully.")
