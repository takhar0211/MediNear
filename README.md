🏥 MediNear  
Find Nearby Hospitals Instantly Using Your Location  

- MediNear is a location-based web application built with Django + OpenStreetMap (OSM) that allows users to quickly find nearby hospitals based on their current geographic location.  
- The application detects the user’s location, fetches nearby hospital data from OpenStreetMap via the Overpass API, calculates distance using the Haversine formula, and displays results in a clean, responsive UI.


## Features
- Automatic location detection (Browser Geolocation API)  
- Fetch nearby hospitals within a 3km radius  
- Distance calculation using Haversine formula  
- One-click navigation via Google Maps  
- Fully responsive UI (mobile + desktop)  
- Lightweight – No heavy frontend frameworks  
- Real-time data from OpenStreetMap  


## Tech Stack

### Backend
- Python 3.12  
- Django 6  
- Django REST Framework  
- Requests (for API calls)  

### Frontend
- HTML5  
- CSS3 (Flexbox + Grid)  
- Vanilla JavaScript  
- LocalStorage  

### External Data Source
- OpenStreetMap (OSM)  
- Overpass API  


## How It Works (Application Flow)

1️⃣ User Interaction  
- User clicks "Find Nearby Hospitals" on the homepage.  

2️⃣ Location Access  
- Browser requests permission and captures:  
- `navigator.geolocation.getCurrentPosition()`  

3️⃣ API Request to Backend  
- Frontend sends a POST request to:  
- `/api/nearby/`  

With:

```json
{
  "latitude": "<user_lat>",
  "longitude": "<user_lon>"
}
```
4️⃣ **Data Processing (Backend)**  
- Overpass API is queried for hospitals within 3000 meters  
- Hospital latitude & longitude extracted  
- Distance calculated using Haversine formula  
- Data sorted by nearest first  

5️⃣ **Results Display**  
- Response returned as JSON  
- Stored in browser localStorage  
- User redirected to `/result/`  
- Hospital cards rendered dynamically  


## Future Enhancements

- Add hospital phone numbers & websites via improved data source  
- Add ratings support  
- Add search radius filter  
- Add user authentication & saved searches  
- Deploy to cloud (Render / Railway)  
- Production setup (Gunicorn + PostgreSQL)  


## Author

**Aman Takhar**  
IT Student | Django Developer | AI Enthusiast  

If you found this project useful, consider giving it a ⭐ on GitHub.
