import requests
import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return round(R * c, 2)

def get_nearby_hospitals(lat, lon):
    url = "https://overpass-api.de/api/interpreter"

    query = f"""
    [out:json];
    node
      ["amenity"="hospital"]
      (around:3000,{lat},{lon});
    out tags center;
    """

    response = requests.post(url, data=query)
    data = response.json()

    hospitals = []

    for e in data["elements"]:
        tags = e.get("tags", {})

        h_lat = e["lat"]
        h_lon = e["lon"]

        hospitals.append({
            "name": e.get("tags", {}).get("name", "Unnamed Hospital"),
            "lat": h_lat,
            "lon": h_lon,
            "distance_km": haversine(lat, lon, h_lat, h_lon),

            "phone": e.get("tags", {}).get("phone") 
                or e.get("tags", {}).get("contact:phone")
                or e.get("tags", {}).get("contact:mobile"),

            "website": e.get("tags", {}).get("website")
                    or e.get("tags", {}).get("contact:website"),

            "maps_link": f"https://www.google.com/maps?q={h_lat},{h_lon}"
        })

    return sorted(hospitals, key=lambda x: x["distance_km"])
