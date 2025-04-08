# Create a dictionary of 3 countries you’d like to visit as a key and their capital city a value
countries_tobe_visited = {
    "france": "paris",
    "Canada": "Toronto",
    "Ghana": "Acra",
}
# Print out the dictionary
print(countries_tobe_visited)
# Remove your least favorite country from the dictionary
del countries_tobe_visited["Ghana"]
# Print out the dictionary
print(countries_tobe_visited)
# Add another country you'd like to visit
countries_tobe_visited["USA"] = "Atlanta"
# Print out the dictionary
print(countries_tobe_visited)
# Display the capital of each country (one at a time, don't use a loop)
print(countries_tobe_visited.get("france"))
print(countries_tobe_visited["Canada"])
print(countries_tobe_visited.get("USA"))
