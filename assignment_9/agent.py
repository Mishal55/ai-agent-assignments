import json

def load_hotels(path="hotels.json"):
    with open(path, "r") as f:
        return json.load(f)

def filter_hotels(hotels, instruction):
    # Example: "show hotels with pool in Karachi"
    city = None
    amenity = None

    words = instruction.lower().split()
    for i, word in enumerate(words):
        if word == "in":
            city = words[i + 1]
        if word == "with":
            amenity = words[i + 1]

    results = []
    for hotel in hotels:
        if city and hotel["city"].lower() != city:
            continue
        if amenity and amenity not in hotel["amenities"]:
            continue
        results.append(hotel)

    return results

if __name__ == "__main__":
    hotels = load_hotels()
    user_input = input("Enter instruction: ")
    filtered = filter_hotels(hotels, user_input)
    print("Matching hotels:")
    for h in filtered:
        print(f"- {h['name']} ({h['city']})")
