import json

def convert_geojson(input_file, output_file):
    # Read the input GeoJSON file
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    # Define a function to map properties
    def map_properties(properties):
        new_properties = {
            "NAME": properties.get("prov_name_en", [""])[0]
        }
        return new_properties
    
    # Apply the mapping to each feature in the GeoJSON
    for feature in data['features']:
        feature['properties'] = map_properties(feature['properties'])
    
    # Write the output GeoJSON file
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)
    
    print(f"Converted GeoJSON saved to {output_file}")

# Example usage
input_file = 'new_geojson.json'  # Update this to your input file path
output_file = 'converted_canada_geojson.json'
convert_geojson(input_file, output_file)